# Copyright (C) 2026 - TODAY KMEE

"""Client of the NFAg 1.00 webservices.

Per the MOC NFAg 1.00l (Visão Geral, item 3): synchronous services, SOAP 1.2,
the request in nfagDadosMsg, the answer in nfagResultMsg, no SOAP header,
and only the NFAgRecepcao message gzipped and base64 encoded. SVRS is the
only authorizer (Visão Geral, item 12).
"""

import base64
import gzip
import logging
import re
from typing import Any, Optional

from brazil_fiscal_client.fiscal_client import FiscalClient

# --- Content Bindings ---
from nfelib.nfag.bindings.v1_0.cons_sit_nfag_v1_00 import ConsSitNfag
from nfelib.nfag.bindings.v1_0.cons_stat_serv_nfag_v1_00 import (
    ConsStatServNfag,
)
from nfelib.nfag.bindings.v1_0.ev_canc_nfag_v1_00 import (
    EvCancNfag,
    EvCancNfagDescEvento,
)
from nfelib.nfag.bindings.v1_0.evento_nfag_v1_00 import EventoNfag
from nfelib.nfag.bindings.v1_0.nfag_tipos_basico_v1_00 import Tnfag
from nfelib.nfag.bindings.v1_0.ret_cons_sit_nfag_v1_00 import RetConsSitNfag
from nfelib.nfag.bindings.v1_0.ret_cons_stat_serv_nfag_v1_00 import (
    RetConsStatServNfag,
)
from nfelib.nfag.bindings.v1_0.ret_evento_nfag_v1_00 import RetEventoNfag
from nfelib.nfag.bindings.v1_0.ret_nfag_v1_00 import RetNfag
from nfelib.nfag.bindings.v1_0.tipos_geral_nfag_v1_00 import Tamb, TcorgaoIbge

# --- Server Definitions ---
from nfelib.nfag.client.v1_0.servers import Endpoint
from nfelib.nfag.client.v1_0.servers import servers as SERVERS_NFAG

# --- SOAP Bindings ---
from nfelib.nfag.soap.v1_0.nfagconsulta import NfagConsultaSoap12NfagConsultaNf
from nfelib.nfag.soap.v1_0.nfagrecepcao import NfagRecepcaoSoap12NfagRecepcao
from nfelib.nfag.soap.v1_0.nfagrecepcaoevento import (
    NfagRecepcaoEventoSoap12NfagRecepcaoEvento,
)
from nfelib.nfag.soap.v1_0.nfagstatusservico import (
    NfagStatusServicoSoap12NfagStatusServicoNf,
)

_logger = logging.getLogger(__name__)

XML_DECLARATION = re.compile(r"^\s*<\?xml[^>]*\?>")

ACTION_TO_ENDPOINT = {
    NfagStatusServicoSoap12NfagStatusServicoNf: Endpoint.NFAGSTATUSSERVICO,
    NfagConsultaSoap12NfagConsultaNf: Endpoint.NFAGCONSULTA,
    NfagRecepcaoSoap12NfagRecepcao: Endpoint.NFAGRECEPCAO,
    NfagRecepcaoEventoSoap12NfagRecepcaoEvento: Endpoint.NFAGRECEPCAOEVENTO,
}


class NfagClient(FiscalClient):
    """A façade for the NFAg v1.00 SOAP webservices."""

    def __init__(self, **kwargs: Any):
        self.mod = kwargs.pop("mod", "75")
        kwargs.setdefault("soap12_envelope", True)
        super().__init__(service="nfag", versao="1.00", **kwargs)

    def _get_location(self, endpoint_type: Endpoint) -> str:
        """Constructs the full HTTPS URL for the specified service."""
        server_data = SERVERS_NFAG["SVRS"]
        endpoints = (
            server_data["prod_endpoints"]
            if self.ambiente == "1"  # production
            else server_data["dev_endpoints"]
        )
        location = endpoints[endpoint_type].split("?")[0]
        _logger.debug(f"Determined location for {endpoint_type.name}: {location}")
        return location

    def prepare_headers(self, headers: dict) -> dict:
        """SOAP 1.2 carries the action in the content type."""
        result = super().prepare_headers(headers)
        result["content-type"] = (
            f'application/soap+xml; charset=utf-8; action="{self._soap_action}"'
        )
        return result

    def send(
        self,
        action_class: type,
        dados_msg: dict,
        placeholder_exp: Optional[str] = None,
        placeholder_content: Optional[str] = None,
        **kwargs: Any,
    ) -> Any:
        """Builds and sends a request, wrapping the payload in nfagDadosMsg."""
        self._soap_action = action_class.soapAction
        response = super().send(
            action_class=action_class,
            location=self._get_location(ACTION_TO_ENDPOINT[action_class]),
            wrapped_obj={"Body": {"nfagDadosMsg": dados_msg}},
            placeholder_exp=placeholder_exp or "",
            placeholder_content=placeholder_content or "",
            **kwargs,
        )

        if not self.wrap_response:
            return self._unwrap_body(response.body)

        response.resposta = self._unwrap_body(response.resposta.body)
        return response

    @staticmethod
    def _unwrap_body(body: Any) -> Any:
        """Return the payload element of the NFAg SOAP response Body."""
        if body.fault is not None or body.nfagResultMsg is None:
            fault = body.fault.faultstring if body.fault is not None else None
            raise ValueError(f"No nfagResultMsg in the NFAg SOAP response: {fault}")
        return body.nfagResultMsg.content[0]

    def status_servico(self) -> RetConsStatServNfag:
        """Consulta o status do serviço NFAg."""
        payload = ConsStatServNfag(tpAmb=Tamb(self.ambiente), versao=self.versao)
        return self.send(
            NfagStatusServicoSoap12NfagStatusServicoNf, {"content": [payload]}
        )

    def consulta_documento(self, chave: str) -> RetConsSitNfag:
        """Consulta a situação de uma NFAg pela chave de acesso."""
        payload = ConsSitNfag(
            tpAmb=Tamb(self.ambiente), chNFAg=chave, versao=self.versao
        )
        return self.send(NfagConsultaSoap12NfagConsultaNf, {"content": [payload]})

    def envia_documento(self, nfag_obj: Tnfag) -> RetNfag:
        """Envia uma NFAg de forma síncrona.

        The signed NFAg goes gzipped and base64 encoded as the text of
        nfagDadosMsg.
        """
        signed_xml = nfag_obj.to_xml(
            pkcs12_data=self.pkcs12_data,
            pkcs12_password=self.pkcs12_password,
            doc_id=nfag_obj.infNFAg.Id,
        )
        xml = XML_DECLARATION.sub("", signed_xml)
        value = base64.b64encode(gzip.compress(xml.encode("utf-8"))).decode()
        return self.send(NfagRecepcaoSoap12NfagRecepcao, {"value": value})

    def envia_evento(
        self,
        chave: str,
        tpEvento: str,
        nSeqEvento: str,
        detEvento: Any,
        cnpj: str,
        dhEvento: Optional[str] = None,
    ) -> RetEventoNfag:
        """Envia um evento genérico para uma NFAg."""
        inf_evento = EventoNfag.InfEvento(
            # MOC NFAg: "ID" + tpEvento + chNFAg + nSeqEvento (55 chars)
            Id=f"ID{tpEvento}{chave}{nSeqEvento.zfill(3)}",
            cOrgao=TcorgaoIbge(self.uf),
            tpAmb=Tamb(self.ambiente),
            CNPJ=cnpj,
            chNFAg=chave,
            dhEvento=dhEvento or self._timestamp(),
            tpEvento=tpEvento,
            nSeqEvento=nSeqEvento,
            detEvento=EventoNfag.InfEvento.DetEvento(
                any_element=detEvento, versaoEvento=self.versao
            ),
        )
        evento = EventoNfag(versao=self.versao, infEvento=inf_evento)
        signed_xml = evento.to_xml(
            pkcs12_data=self.pkcs12_data,
            pkcs12_password=self.pkcs12_password,
            doc_id=evento.infEvento.Id,
        )

        # The signed event XML is injected raw with a placeholder so the
        # signature survives the payload serialization.
        return self.send(
            NfagRecepcaoEventoSoap12NfagRecepcaoEvento,
            {"content": [EventoNfag(versao=self.versao)]},
            placeholder_exp=r"<eventoNFAg[^>]*/>|<eventoNFAg.*?>.*?</eventoNFAg>",
            placeholder_content=XML_DECLARATION.sub("", signed_xml),
        )

    def cancela_documento(
        self, chave: str, protocolo_autorizacao: str, justificativa: str, cnpj: str
    ) -> RetEventoNfag:
        """Cancela uma NFAg autorizada."""
        det_evento = EvCancNfag(
            descEvento=EvCancNfagDescEvento.CANCELAMENTO,
            nProt=protocolo_autorizacao,
            xJust=justificativa,
        )
        return self.envia_evento(
            chave=chave,
            tpEvento="110111",
            nSeqEvento="1",
            detEvento=det_evento,
            cnpj=cnpj,
        )
