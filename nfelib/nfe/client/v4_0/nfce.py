# FILEPATH: nfelib/nfe/client/v4_0/nfce.py
# Copyright (C) 2023 Ygor de Carvalho - KMEE
# Copyright (C) 2025 Raphaël Valyi - Akretion

import binascii
import hashlib
import logging
from typing import List, Optional

from lxml import etree

from nfelib.nfe.bindings.v4_0.leiaute_nfe_v4_00 import TenviNfeIndSinc, Tnfe
from nfelib.nfe.bindings.v4_0.ret_envi_nfe_v4_00 import RetEnviNfe
from nfelib.nfe.client.v4_0.nfe import NfeClient
from nfelib.nfe.client.v4_0.servers_nfce import (
    ESTADO_CONSULTA_NFCE,
    ESTADO_QRCODE,
)

_logger = logging.getLogger(__name__)

# --- Constants ---
NAMESPACES = {
    "nfe": "http://www.portalfiscal.inf.br/nfe",
    "ds": "http://www.w3.org/2000/09/xmldsig#",
}

# TODO Migration Impact: Medium. Every call to envia_documento for NFC-e will 
# now need to include the CSC credentials. This requires code changes but makes the 
# system more robust for multi-establishment scenarios.
# Move csc_token and csc_code from __init__ to the envia_documento method 
# signature. This makes the client stateless regarding CSCs and more versatile.

class NfceClient(NfeClient):
    """A façade for the NFC-e SOAP webservices, extending the NFe client."""

    def __init__(
        self,
        qrcode_versao: str = "2",
        csc_token: Optional[str] = None,
        csc_code: Optional[str] = None,
        **kwargs,
    ):
        # ... (init method remains the same) ...
        kwargs["mod"] = "65"
        super().__init__(**kwargs)
        self.envio_sincrono = True

        if not csc_token or not csc_code:
            raise ValueError("csc_token and csc_code are required for NfceClient")

        self.qrcode_versao = str(qrcode_versao)
        self.csc_token = str(csc_token)
        self.csc_code = str(csc_code)

    # ... (_build_pre_qrcode_normal, _compute_qr_hash, _build_qrcode, monta_qrcode, _generate_qrcode_contingency remain the same) ...

    def _build_pre_qrcode_normal(self, nfce_chave: str) -> str:
        return f"{nfce_chave}|{self.qrcode_versao}|{self.ambiente}|{self.csc_token}"

    def _compute_qr_hash(self, pre_qrcode_with_csc: str) -> str:
        hash_object = hashlib.sha1(pre_qrcode_with_csc.encode("utf-8"))
        return hash_object.hexdigest().upper()

    def _build_qrcode(self, pre_qrcode_without_csc: str, qr_hash: str) -> str:
        uf_sigla = self.uf_code_to_sigla(self.uf)
        base_url = ESTADO_QRCODE.get(uf_sigla, {}).get(self.ambiente)
        if not base_url:
            raise ValueError(
                f"URL de QR Code não encontrada para UF {uf_sigla} no ambiente {self.ambiente}"
            )
        return f"{base_url}{pre_qrcode_without_csc}|{qr_hash}"

    def monta_qrcode(self, chave: str) -> str:
        pre_qrcode_normal = self._build_pre_qrcode_normal(chave)
        pre_qrcode_with_csc = f"{pre_qrcode_normal}{self.csc_code}"
        qr_hash = self._compute_qr_hash(pre_qrcode_with_csc)
        return self._build_qrcode(pre_qrcode_normal, qr_hash)

    def _generate_qrcode_contingency(self, edoc_obj: Tnfe, signed_xml: str) -> str:
        xml_tree = etree.fromstring(signed_xml.encode("utf-8"))
        chave_nfce = edoc_obj.infNFe.Id.replace("NFe", "")
        data_emissao_dia = edoc_obj.infNFe.ide.dhEmi[8:10]
        total_nfe = xml_tree.find(".//nfe:ICMSTot/nfe:vNF", namespaces=NAMESPACES).text
        digest_value_b64 = xml_tree.find(
            ".//ds:DigestValue", namespaces=NAMESPACES
        ).text
        digest_value_hex = binascii.hexlify(digest_value_b64.encode()).decode()
        pre_qrcode_contingency = (
            f"{chave_nfce}|{self.qrcode_versao}|{self.ambiente}|{data_emissao_dia}"
            f"|{total_nfe}|{digest_value_hex}|{self.csc_token}"
        )
        pre_qrcode_with_csc = f"{pre_qrcode_contingency}{self.csc_code}"
        qr_hash = self._compute_qr_hash(pre_qrcode_with_csc)
        return self._build_qrcode(pre_qrcode_contingency, qr_hash)

    def _update_qrcode_nfce(
        self, edoc_obj: Tnfe, signed_xml: Optional[str] = None
    ) -> None:
        is_contingency = edoc_obj.infNFe.ide.tpEmis != "1"
        chave = edoc_obj.infNFe.Id.replace("NFe", "")

        if is_contingency:
            if not signed_xml:
                raise ValueError(
                    "Signed XML is required for contingency QR Code generation."
                )
            qr_code_text = self._generate_qrcode_contingency(edoc_obj, signed_xml)
        else:
            qr_code_text = self.monta_qrcode(chave)

        if not edoc_obj.infNFeSupl:
            edoc_obj.infNFeSupl = Tnfe.InfNfeSupl()
        edoc_obj.infNFeSupl.qrCode = qr_code_text

    def envia_documento(
        self, lista_nfes: List[Tnfe], id_lote: Optional[str] = None
    ) -> RetEnviNfe:
        if len(lista_nfes) != 1:
            raise ValueError(
                "NfceClient.envia_documento supports only one NFC-e at a time."
            )

        edoc_obj = lista_nfes[0]
        is_contingency = edoc_obj.infNFe.ide.tpEmis != "1"

        if is_contingency:
            # 1. Sign once to get the digest for the QR code
            initial_signed_xml = edoc_obj.to_xml(
                pkcs12_data=self.pkcs12_data,
                pkcs12_password=self.pkcs12_password,
                doc_id=edoc_obj.infNFe.Id,
            )
            # 2. Update the QR code using the digest from the signed XML
            self._update_qrcode_nfce(edoc_obj, initial_signed_xml)
            # 3. Re-sign the object now that it contains the final QR code
            _logger.info(
                "Contingency emission detected. Re-signing NFe with updated QR Code."
            )
            final_signed_xml = edoc_obj.to_xml(
                pkcs12_data=self.pkcs12_data,
                pkcs12_password=self.pkcs12_password,
                doc_id=edoc_obj.infNFe.Id,
            )
        else:  # Normal Emission
            # 1. Update the QR code (doesn't need digest)
            self._update_qrcode_nfce(edoc_obj, None)
            # 2. Sign the final object once
            final_signed_xml = edoc_obj.to_xml(
                pkcs12_data=self.pkcs12_data,
                pkcs12_password=self.pkcs12_password,
                doc_id=edoc_obj.infNFe.Id,
            )

        return super().envia_documento(
            lista_nfes=[final_signed_xml],
            id_lote=id_lote,
            ind_sinc=TenviNfeIndSinc.VALUE_1,
        )

    def consulta_recibo(self, proc_envio: RetEnviNfe) -> RetEnviNfe:
        _logger.info("NFC-e is synchronous; returning original send result.")
        return proc_envio

    def get_consulta_url(self) -> str:
        uf_sigla = self.uf_code_to_sigla(self.uf)
        url = ESTADO_CONSULTA_NFCE.get(uf_sigla, {})[int(self.ambiente) - 1]
        if not url:
            raise ValueError(
                f"URL de Consulta não encontrada para UF {uf_sigla} no ambiente {self.ambiente}"
            )
        return url

    @staticmethod
    def uf_code_to_sigla(uf_code: str) -> str:
        uf_map = {
            "12": "AC",
            "27": "AL",
            "16": "AP",
            "13": "AM",
            "29": "BA",
            "23": "CE",
            "53": "DF",
            "32": "ES",
            "52": "GO",
            "21": "MA",
            "51": "MT",
            "50": "MS",
            "31": "MG",
            "15": "PA",
            "25": "PB",
            "41": "PR",
            "26": "PE",
            "22": "PI",
            "33": "RJ",
            "24": "RN",
            "43": "RS",
            "11": "RO",
            "14": "RR",
            "42": "SC",
            "35": "SP",
            "28": "SE",
            "17": "TO",
        }
        sigla = uf_map.get(str(uf_code))
        if not sigla:
            raise ValueError(f"Invalid UF code: {uf_code}")
        return sigla
