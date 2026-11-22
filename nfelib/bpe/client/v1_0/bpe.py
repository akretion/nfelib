# Copyright (C) 2026 - TODAY KMEE

"""Client of the BP-e 1.00 webservices.

Per the MOC BP-e 1.00b (Visão Geral, items 3.3 and 3.4): SOAP 1.2, the
request in bpeDadosMsg, the answer in bpeResultMsg, no SOAP header, and only
the BPeRecepcao message gzipped and base64 encoded.
"""

import base64
import gzip
import logging
import re
from typing import Any, Optional

from brazil_fiscal_client.fiscal_client import FiscalClient

# --- Content Bindings ---
from nfelib.bpe.bindings.v1_0.bpe_tipos_basico_v1_00 import Tbpe
from nfelib.bpe.bindings.v1_0.cons_sit_bpe_v1_00 import ConsSitBpe
from nfelib.bpe.bindings.v1_0.cons_stat_serv_bpe_v1_00 import ConsStatServBpe
from nfelib.bpe.bindings.v1_0.ev_canc_bpe_v1_00 import (
    EvCancBpe,
    EvCancBpeDescEvento,
)
from nfelib.bpe.bindings.v1_0.evento_bpe_v1_00 import EventoBpe
from nfelib.bpe.bindings.v1_0.ret_bpe_v1_00 import RetBpe
from nfelib.bpe.bindings.v1_0.ret_cons_sit_bpe_v1_00 import RetConsSitBpe
from nfelib.bpe.bindings.v1_0.ret_cons_stat_serv_bpe_v1_00 import (
    RetConsStatServBpe,
)
from nfelib.bpe.bindings.v1_0.ret_evento_bpe_v1_00 import RetEventoBpe
from nfelib.bpe.bindings.v1_0.tipos_geral_bpe_v1_00 import Tamb, TcorgaoIbge

# --- Server Definitions ---
from nfelib.bpe.client.v1_0.servers import Endpoint
from nfelib.bpe.client.v1_0.servers import servers as SERVERS_BPE

# --- SOAP Bindings ---
from nfelib.bpe.soap.v1_0.bpeconsulta import BpeConsultaSoap12BpeConsultaBp
from nfelib.bpe.soap.v1_0.bperecepcao import BpeRecepcaoSoap12BpeRecepcao
from nfelib.bpe.soap.v1_0.bperecepcaoevento import (
    BpeRecepcaoEventoSoap12BpeRecepcaoEvento,
)
from nfelib.bpe.soap.v1_0.bpestatusservico import (
    BpeStatusServicoSoap12BpeStatusServicoBp,
)

_logger = logging.getLogger(__name__)

XML_DECLARATION = re.compile(r"^\s*<\?xml[^>]*\?>")

ACTION_TO_ENDPOINT = {
    BpeStatusServicoSoap12BpeStatusServicoBp: Endpoint.BPESTATUSSERVICO,
    BpeConsultaSoap12BpeConsultaBp: Endpoint.BPECONSULTA,
    BpeRecepcaoSoap12BpeRecepcao: Endpoint.BPERECEPCAO,
    BpeRecepcaoEventoSoap12BpeRecepcaoEvento: Endpoint.BPERECEPCAOEVENTO,
}


def _get_server_key_for_uf(uf_ibge_code: str) -> str:
    """Gets the server key ('MG', 'SVRS', etc.) for a given UF."""
    uf_map = {
        "31": "MG",
        "50": "MS",
        "51": "MT",
        "41": "PR",
        "35": "SP",
    }
    # every other UF is authorized by SVRS
    return uf_map.get(uf_ibge_code, "SVRS")


class BpeClient(FiscalClient):
    """A façade for the BP-e v1.00 SOAP webservices."""

    def __init__(self, **kwargs: Any):
        self.mod = kwargs.pop("mod", "63")
        kwargs.setdefault("soap12_envelope", True)
        super().__init__(service="bpe", versao="1.00", **kwargs)

    def _get_location(self, endpoint_type: Endpoint) -> str:
        """Constructs the full HTTPS URL for the specified service."""
        server_data = SERVERS_BPE[_get_server_key_for_uf(self.uf)]
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
        """Builds and sends a request, wrapping the payload in bpeDadosMsg."""
        self._soap_action = action_class.soapAction
        response = super().send(
            action_class=action_class,
            location=self._get_location(ACTION_TO_ENDPOINT[action_class]),
            wrapped_obj={"Body": {"bpeDadosMsg": dados_msg}},
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
        """Return the payload element of the BP-e SOAP response Body."""
        if body.fault is not None or body.bpeResultMsg is None:
            fault = body.fault.faultstring if body.fault is not None else None
            raise ValueError(f"No bpeResultMsg in the BP-e SOAP response: {fault}")
        return body.bpeResultMsg.content[0]

    def status_servico(self) -> RetConsStatServBpe:
        """Consulta o status do serviço BP-e."""
        payload = ConsStatServBpe(tpAmb=Tamb(self.ambiente), versao=self.versao)
        return self.send(
            BpeStatusServicoSoap12BpeStatusServicoBp, {"content": [payload]}
        )

    def consulta_documento(self, chave: str) -> RetConsSitBpe:
        """Consulta a situação de um BP-e pela chave de acesso."""
        payload = ConsSitBpe(tpAmb=Tamb(self.ambiente), chBPe=chave, versao=self.versao)
        return self.send(BpeConsultaSoap12BpeConsultaBp, {"content": [payload]})

    def envia_documento(self, bpe_obj: Tbpe) -> RetBpe:
        """Envia um BP-e de forma síncrona.

        The signed BP-e goes gzipped and base64 encoded as the text of
        bpeDadosMsg (MOC BP-e 1.00b, item 3.4).
        """
        signed_xml = bpe_obj.to_xml(
            pkcs12_data=self.pkcs12_data,
            pkcs12_password=self.pkcs12_password,
            doc_id=bpe_obj.infBPe.Id,
        )
        xml = XML_DECLARATION.sub("", signed_xml)
        value = base64.b64encode(gzip.compress(xml.encode("utf-8"))).decode()
        return self.send(BpeRecepcaoSoap12BpeRecepcao, {"value": value})

    def envia_evento(
        self,
        chave: str,
        tpEvento: str,
        nSeqEvento: str,
        detEvento: Any,
        cnpj: str,
        dhEvento: Optional[str] = None,
    ) -> RetEventoBpe:
        """Envia um evento genérico para um BP-e."""
        inf_evento = EventoBpe.InfEvento(
            # MOC BP-e 1.00b: "ID" + tpEvento + chBPe + nSeqEvento (54 chars)
            Id=f"ID{tpEvento}{chave}{nSeqEvento.zfill(2)}",
            cOrgao=TcorgaoIbge(self.uf),
            tpAmb=Tamb(self.ambiente),
            CNPJ=cnpj,
            chBPe=chave,
            dhEvento=dhEvento or self._timestamp(),
            tpEvento=tpEvento,
            nSeqEvento=nSeqEvento,
            detEvento=EventoBpe.InfEvento.DetEvento(
                any_element=detEvento, versaoEvento=self.versao
            ),
        )
        evento = EventoBpe(versao=self.versao, infEvento=inf_evento)
        signed_xml = evento.to_xml(
            pkcs12_data=self.pkcs12_data,
            pkcs12_password=self.pkcs12_password,
            doc_id=evento.infEvento.Id,
        )

        # The signed event XML is injected raw with a placeholder so the
        # signature survives the payload serialization.
        return self.send(
            BpeRecepcaoEventoSoap12BpeRecepcaoEvento,
            {"content": [EventoBpe(versao=self.versao)]},
            placeholder_exp=r"<eventoBPe[^>]*/>|<eventoBPe.*?>.*?</eventoBPe>",
            placeholder_content=XML_DECLARATION.sub("", signed_xml),
        )

    def cancela_documento(
        self, chave: str, protocolo_autorizacao: str, justificativa: str, cnpj: str
    ) -> RetEventoBpe:
        """Cancela um BP-e autorizado."""
        det_evento = EvCancBpe(
            descEvento=EvCancBpeDescEvento.CANCELAMENTO,
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
