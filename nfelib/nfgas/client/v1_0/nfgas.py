# Copyright (C) 2026 - TODAY KMEE

"""Client of the NFGas 1.00 webservices.

Per the MOC NFGas 1.00g (Visão Geral, item 3): synchronous services, SOAP 1.2,
the request in nfgasDadosMsg, the answer in nfgasResultMsg, no SOAP header,
and only the NFGasRecepcao message gzipped and base64 encoded. SVRS is the
only authorizer.
"""

import base64
import gzip
import logging
import re
from typing import Any, Optional

from brazil_fiscal_client.fiscal_client import FiscalClient

# --- Content Bindings ---
from nfelib.nfgas.bindings.v1_0.cons_sit_nfgas_v1_00 import ConsSitNfgas
from nfelib.nfgas.bindings.v1_0.cons_stat_serv_nfgas_v1_00 import (
    ConsStatServNfgas,
)
from nfelib.nfgas.bindings.v1_0.ev_canc_nfgas_v1_00 import (
    EvCancNfgas,
    EvCancNfgasDescEvento,
)
from nfelib.nfgas.bindings.v1_0.evento_nfgas_v1_00 import EventoNfgas
from nfelib.nfgas.bindings.v1_0.nfgas_tipos_basico_v1_00 import Tnfgas
from nfelib.nfgas.bindings.v1_0.ret_cons_sit_nfgas_v1_00 import RetConsSitNfgas
from nfelib.nfgas.bindings.v1_0.ret_cons_stat_serv_nfgas_v1_00 import (
    RetConsStatServNfgas,
)
from nfelib.nfgas.bindings.v1_0.ret_evento_nfgas_v1_00 import RetEventoNfgas
from nfelib.nfgas.bindings.v1_0.ret_nfgas_v1_00 import RetNfgas
from nfelib.nfgas.bindings.v1_0.tipos_geral_nfgas_v1_00 import Tamb, TcorgaoIbge

# --- Server Definitions ---
from nfelib.nfgas.client.v1_0.servers import Endpoint
from nfelib.nfgas.client.v1_0.servers import servers as SERVERS_NFGAS

# --- SOAP Bindings ---
from nfelib.nfgas.soap.v1_0.nfgasconsulta import NfgasConsultaSoap12NfgasConsultaNf
from nfelib.nfgas.soap.v1_0.nfgasrecepcao import NfgasRecepcaoSoap12NfgasRecepcao
from nfelib.nfgas.soap.v1_0.nfgasrecepcaoevento import (
    NfgasRecepcaoEventoSoap12NfgasRecepcaoEvento,
)
from nfelib.nfgas.soap.v1_0.nfgasstatusservico import (
    NfgasStatusServicoSoap12NfgasStatusServicoNf,
)

_logger = logging.getLogger(__name__)

XML_DECLARATION = re.compile(r"^\s*<\?xml[^>]*\?>")

ACTION_TO_ENDPOINT = {
    NfgasStatusServicoSoap12NfgasStatusServicoNf: Endpoint.NFGASSTATUSSERVICO,
    NfgasConsultaSoap12NfgasConsultaNf: Endpoint.NFGASCONSULTA,
    NfgasRecepcaoSoap12NfgasRecepcao: Endpoint.NFGASRECEPCAO,
    NfgasRecepcaoEventoSoap12NfgasRecepcaoEvento: Endpoint.NFGASRECEPCAOEVENTO,
}


class NfgasClient(FiscalClient):
    """A façade for the NFGas v1.00 SOAP webservices."""

    def __init__(self, **kwargs: Any):
        self.mod = kwargs.pop("mod", "76")
        kwargs.setdefault("soap12_envelope", True)
        super().__init__(service="nfgas", versao="1.00", **kwargs)

    def _get_location(self, endpoint_type: Endpoint) -> str:
        """Constructs the full HTTPS URL for the specified service."""
        server_data = SERVERS_NFGAS["SVRS"]
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
        """Builds and sends a request, wrapping the payload in nfgasDadosMsg."""
        self._soap_action = action_class.soapAction
        response = super().send(
            action_class=action_class,
            location=self._get_location(ACTION_TO_ENDPOINT[action_class]),
            wrapped_obj={"Body": {"nfgasDadosMsg": dados_msg}},
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
        """Return the payload element of the NFGas SOAP response Body."""
        if body.fault is not None or body.nfgasResultMsg is None:
            fault = body.fault.faultstring if body.fault is not None else None
            raise ValueError(f"No nfgasResultMsg in the NFGas SOAP response: {fault}")
        return body.nfgasResultMsg.content[0]

    def status_servico(self) -> RetConsStatServNfgas:
        """Consulta o status do serviço NFGas."""
        payload = ConsStatServNfgas(tpAmb=Tamb(self.ambiente), versao=self.versao)
        return self.send(
            NfgasStatusServicoSoap12NfgasStatusServicoNf, {"content": [payload]}
        )

    def consulta_documento(self, chave: str) -> RetConsSitNfgas:
        """Consulta a situação de uma NFGas pela chave de acesso."""
        payload = ConsSitNfgas(
            tpAmb=Tamb(self.ambiente), chNFGas=chave, versao=self.versao
        )
        return self.send(NfgasConsultaSoap12NfgasConsultaNf, {"content": [payload]})

    def envia_documento(self, nfgas_obj: Tnfgas) -> RetNfgas:
        """Envia uma NFGas de forma síncrona.

        The signed NFGas goes gzipped and base64 encoded as the text of
        nfgasDadosMsg.
        """
        signed_xml = nfgas_obj.to_xml(
            pkcs12_data=self.pkcs12_data,
            pkcs12_password=self.pkcs12_password,
            doc_id=nfgas_obj.infNFGas.Id,
        )
        xml = XML_DECLARATION.sub("", signed_xml)
        value = base64.b64encode(gzip.compress(xml.encode("utf-8"))).decode()
        return self.send(NfgasRecepcaoSoap12NfgasRecepcao, {"value": value})

    def envia_evento(
        self,
        chave: str,
        tpEvento: str,
        nSeqEvento: str,
        detEvento: Any,
        cnpj: str,
        dhEvento: Optional[str] = None,
    ) -> RetEventoNfgas:
        """Envia um evento genérico para uma NFGas."""
        inf_evento = EventoNfgas.InfEvento(
            # MOC NFGas: "ID" + tpEvento + chNFGas + nSeqEvento (55 chars)
            Id=f"ID{tpEvento}{chave}{nSeqEvento.zfill(3)}",
            cOrgao=TcorgaoIbge(self.uf),
            tpAmb=Tamb(self.ambiente),
            CNPJ=cnpj,
            chNFGas=chave,
            dhEvento=dhEvento or self._timestamp(),
            tpEvento=tpEvento,
            nSeqEvento=nSeqEvento,
            detEvento=EventoNfgas.InfEvento.DetEvento(
                any_element=detEvento, versaoEvento=self.versao
            ),
        )
        evento = EventoNfgas(versao=self.versao, infEvento=inf_evento)
        signed_xml = evento.to_xml(
            pkcs12_data=self.pkcs12_data,
            pkcs12_password=self.pkcs12_password,
            doc_id=evento.infEvento.Id,
        )

        # The signed event XML is injected raw with a placeholder so the
        # signature survives the payload serialization.
        return self.send(
            NfgasRecepcaoEventoSoap12NfgasRecepcaoEvento,
            {"content": [EventoNfgas(versao=self.versao)]},
            placeholder_exp=r"<eventoNFGas[^>]*/>|<eventoNFGas.*?>.*?</eventoNFGas>",
            placeholder_content=XML_DECLARATION.sub("", signed_xml),
        )

    def cancela_documento(
        self, chave: str, protocolo_autorizacao: str, justificativa: str, cnpj: str
    ) -> RetEventoNfgas:
        """Cancela uma NFGas autorizada."""
        det_evento = EvCancNfgas(
            descEvento=EvCancNfgasDescEvento.CANCELAMENTO,
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
