# Copyright (C) 2026  Raphaël Valyi - Akretion
# Copyright 2026 Escodoo - Marcel Savegnago <marcel.savegnago@escodoo.com.br>

"""Minimal REST client for the national NFS-e system (ADN).

The ADN (Ambiente de Dados Nacional) exposes a plain REST API — no SOAP
envelope — with mutual TLS authentication (A1 certificate) and GZip+Base64
XML payloads inside JSON bodies.
"""

from __future__ import annotations  # Python 3.9 compat

import base64
import gzip
import logging
import tempfile
from dataclasses import dataclass
from typing import Any

_logger = logging.getLogger(__name__)

AMBIENTE_PRODUCAO = "1"
AMBIENTE_PRODUCAO_RESTRITA = "2"

ADN_SERVERS = {
    AMBIENTE_PRODUCAO: "https://adn.nfse.gov.br/contribuinte",
    AMBIENTE_PRODUCAO_RESTRITA: "https://adn.producaorestrita.nfse.gov.br/contribuinte",
}

# Distribution (tomador feed) lives on the ADN root. It is not under the
# ``/contribuinte`` emission prefix.
ADN_DFE_SERVERS = {
    AMBIENTE_PRODUCAO: "https://adn.nfse.gov.br",
    AMBIENTE_PRODUCAO_RESTRITA: "https://adn.producaorestrita.nfse.gov.br",
}

# The authorized note lookup is served by Sefin Nacional, not the ADN
# distribution host. Keep this endpoint separate from the ADN routes so a
# caller cannot accidentally query the wrong service.
SEFIN_SERVERS = {
    AMBIENTE_PRODUCAO: "https://sefin.nfse.gov.br/SefinNacional",
    AMBIENTE_PRODUCAO_RESTRITA: (
        "https://sefin.producaorestrita.nfse.gov.br/SefinNacional"
    ),
}


@dataclass
class NfseResponse:
    """Normalized answer of an ADN request.

    :ivar status_code: HTTP status code.
    :ivar body: decoded JSON body (dict) when the answer is JSON.
    :ivar content: raw response bytes.
    :ivar headers: response headers.
    :ivar text: response body decoded as text.
    """

    status_code: int
    body: dict | None
    content: bytes
    headers: dict | None = None
    text: str = ""

    @property
    def ok(self):
        """Whether the response has a successful HTTP status code."""
        return 200 <= self.status_code < 300


class NfseClient:
    """A façade for the national NFS-e REST webservices (ADN).

    Example:
        client = NfseClient(
            ambiente="2",  # 1=production, 2=homologation (producao restrita)
            pkcs12_data=pkcs12_bytes,     # decoded content of the A1 certificate
            pkcs12_password="password",
        )
        ret = client.envia_dps(dps)            # submit a signed DPS
        ret = client.consulta_nfse(chave)      # fetch a generated NFS-e
        ret = client.cancela_documento(chave, ped_reg_evento)  # cancellation
    """

    def __init__(
        self,
        ambiente: str,
        pkcs12_data: bytes,
        pkcs12_password: str,
        timeout: int = 30,
    ):
        try:
            import requests
            from requests.adapters import HTTPAdapter
        except ImportError as exc:
            raise RuntimeError(
                "The NfseClient requires the requests package: pip install requests"
            ) from exc

        self.ambiente = ambiente
        self.base_url = ADN_SERVERS[ambiente]
        self.dfe_base_url = ADN_DFE_SERVERS[ambiente]
        self.sefin_base_url = SEFIN_SERVERS[ambiente]
        self.timeout = timeout
        self.pkcs12_data = pkcs12_data
        self.pkcs12_password = pkcs12_password

        cert_pem, key_pem = self._pkcs12_to_pem()
        self._cert_files = (
            self._write_temp_file(cert_pem),
            self._write_temp_file(key_pem),
        )
        self.session = requests.Session()
        self.session.cert = self._cert_files
        self.session.verify = True
        adapter = HTTPAdapter(max_retries=2)
        self.session.mount("https://", adapter)

    def _pkcs12_to_pem(self) -> tuple[bytes, bytes]:
        """Convert the PKCS12 certificate to PEM parts for requests.

        The certificate may be given as raw DER bytes, as base64 text (like
        Odoo Binary fields) or as a path to a .pfx file.
        """
        try:
            from cryptography.hazmat.primitives import serialization
            from cryptography.hazmat.primitives.serialization import pkcs12
        except ImportError as exc:
            raise RuntimeError(
                "The NfseClient requires the cryptography package to handle "
                "PKCS12 certificates"
            ) from exc

        from nfelib import CommonMixin

        pkcs12_data = CommonMixin.normalize_pkcs12(self.pkcs12_data)
        if isinstance(pkcs12_data, bytes):
            pkcs12_data = pkcs12_data.decode("ascii")
        raw_pfx = base64.b64decode(pkcs12_data)

        private_key, certificate, _cas = pkcs12.load_key_and_certificates(
            raw_pfx, self.pkcs12_password.encode()
        )
        if private_key is None or certificate is None:
            raise RuntimeError(
                "Invalid PKCS12 certificate: no private key or certificate found"
            )
        cert_pem = certificate.public_bytes(serialization.Encoding.PEM)
        key_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
        return cert_pem, key_pem

    @staticmethod
    def _write_temp_file(content: bytes) -> str:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(content)
            return tmp.name

    def _request(
        self,
        method: str,
        path: str,
        json: dict | None = None,
        params: dict | None = None,
        base_url: str | None = None,
    ) -> NfseResponse:
        """Fire one request against the ADN and normalize the answer.

        ``base_url`` defaults to the emission host (``/contribuinte``).
        Distribution calls pass the ADN root so the path is not nested
        under that prefix.
        """
        root = self.base_url if base_url is None else base_url
        response = self.session.request(
            method,
            f"{root}{path}",
            json=json,
            params=params,
            timeout=self.timeout,
        )
        _logger.debug("ADN %s %s -> %s", method, path, response.status_code)
        try:
            body = response.json()
        except ValueError:
            body = None
        try:
            headers = dict(getattr(response, "headers", {}) or {})
        except (TypeError, ValueError):
            headers = {}
        text = getattr(response, "text", "")
        text = text if isinstance(text, str) else ""
        return NfseResponse(
            status_code=response.status_code,
            body=body,
            content=response.content,
            headers=headers,
            text=text,
        )

    @staticmethod
    def _compress_b64(xml: str | bytes) -> str:
        """GZip + Base64 encode an XML payload, as the ADN expects."""
        if isinstance(xml, str):
            xml = xml.encode("utf-8")
        return base64.b64encode(gzip.compress(xml)).decode("ascii")

    def _sign(self, xml: str, doc_id: str) -> str:
        """Sign an XML document with the client certificate."""
        from nfelib import CommonMixin

        return CommonMixin.sign_xml(
            xml=xml,
            pkcs12_data=self.pkcs12_data,
            pkcs12_password=self.pkcs12_password,
            doc_id=doc_id,
        )

    # ------------------------------------------------------------------
    # Webservices
    # ------------------------------------------------------------------

    def envia_dps(self, dps: Any) -> NfseResponse:
        """Submit a DPS: POST /nfse (synchronous NFS-e generation)."""
        xml = dps.to_xml()
        signed_xml = self._sign(xml, dps.infDPS.Id)
        return self._request(
            "POST", "/nfse", json={"dpsXmlGZipB64": self._compress_b64(signed_xml)}
        )

    def consulta_nfse(self, chave: str) -> NfseResponse:
        """Fetch an NFS-e by its access key: GET /nfse/{chaveAcesso}."""
        return self._request("GET", f"/nfse/{chave}")

    def consulta_nfse_sefin(self, chave: str) -> NfseResponse:
        """Fetch an authorized NFS-e from the Sefin Nacional service.

        The Sefin route has the same path as the ADN emission route but is
        hosted at ``/SefinNacional``. It is therefore exposed separately
        instead of changing the existing ``consulta_nfse`` endpoint.
        """
        return self._request("GET", f"/nfse/{chave}", base_url=self.sefin_base_url)

    def consulta_dps(self, dps_id: str) -> NfseResponse:
        """Resolve the NFS-e key from a DPS id: GET /dps/{id}."""
        return self._request("GET", f"/dps/{dps_id}")

    def registra_evento(self, chave: str, evento: Any) -> NfseResponse:
        """Register an event on an NFS-e: POST /nfse/{chaveAcesso}/eventos.

        The `evento` binding (e.g. a PedRegEvento) is signed and packed the
        same way as a DPS.
        """
        xml = evento.to_xml()
        signed_xml = self._sign(xml, evento.infPedReg.Id)
        return self._request(
            "POST",
            f"/nfse/{chave}/eventos",
            json={"pedidoRegistroEventoXmlGZipB64": self._compress_b64(signed_xml)},
        )

    def cancela_documento(self, chave: str, evento_cancelamento: Any) -> NfseResponse:
        """Cancel an NFS-e by registering its cancellation event."""
        return self.registra_evento(chave, evento_cancelamento)

    def consulta_evento(
        self, chave: str, tipo_evento: int, num_seq: int = 1
    ) -> NfseResponse:
        """Fetch one event: GET /nfse/{chaveAcesso}/eventos/{tipoEvento}/{numSeq}."""
        return self._request("GET", f"/nfse/{chave}/eventos/{tipo_evento}/{num_seq}")

    def consulta_dfe(self, nsu: int | str, cnpj: str | None = None) -> NfseResponse:
        """Fetch one distribution batch: GET /contribuintes/DFe/{nsu}.

        ``lote=true`` asks for the batch. ``cnpjConsulta`` limits it to one
        company when given. The host is the ADN root, not ``/contribuinte``.
        """
        params = {"lote": "true"}
        if cnpj:
            params["cnpjConsulta"] = cnpj
        return self._request(
            "GET",
            f"/contribuintes/DFe/{nsu}",
            params=params,
            base_url=self.dfe_base_url,
        )

    def consulta_eventos(self, chave: str) -> NfseResponse:
        """List the events of one NFS-e: GET /contribuintes/NFSe/{chave}/Eventos."""
        return self._request(
            "GET",
            f"/contribuintes/NFSe/{chave}/Eventos",
            base_url=self.dfe_base_url,
        )
