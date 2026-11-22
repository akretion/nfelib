# Copyright (C) 2026 - TODAY KMEE

"""Client of the DC-e 1.00 webservices.

Per the Manual DC-e, Visão Geral (items 4.2.2 and 5): SOAP 1.2,
document/literal, the request in dceDadosMsg, no SOAP header, synchronous
services, one national environment (hosted by the Paraná tax authority) for
every UF. The DC-e goes without compression: the compressed method
(DCeAutorizacaoZip) is optional for the authorizer.
"""

import logging
import re
from typing import Any, Optional

from brazil_fiscal_client.fiscal_client import FiscalClient

# --- Content Bindings ---
from nfelib.dce.bindings.v1_0.cons_sit_dce_v1_00 import ConsSitDce
from nfelib.dce.bindings.v1_0.cons_stat_serv_dce_v1_00 import ConsStatServDce
from nfelib.dce.bindings.v1_0.dce_tipos_basico_v1_00 import Tdce
from nfelib.dce.bindings.v1_0.dce_v1_00 import Dce
from nfelib.dce.bindings.v1_0.ev_canc_dce_v1_00 import (
    EvCancDce,
    EvCancDceDescEvento,
)
from nfelib.dce.bindings.v1_0.evento_dce_v1_00 import EventoDce
from nfelib.dce.bindings.v1_0.ret_cons_sit_dce_v1_00 import RetConsSitDce
from nfelib.dce.bindings.v1_0.ret_cons_stat_serv_dce_v1_00 import (
    RetConsStatServDce,
)
from nfelib.dce.bindings.v1_0.ret_dce_v1_00 import RetDce
from nfelib.dce.bindings.v1_0.ret_evento_dce_v1_00 import RetEventoDce
from nfelib.dce.bindings.v1_0.tipos_geral_dce_v1_00 import (
    Tamb,
    TcodUfIbge,
    TcorgaoIbge,
)

# --- Server Definitions ---
from nfelib.dce.client.v1_0.servers import Endpoint
from nfelib.dce.client.v1_0.servers import servers as SERVERS_DCE

# --- SOAP Bindings ---
from nfelib.dce.soap.v1_0.dceautorizacao import DceAutorizacaoSoap12DceAutorizacao
from nfelib.dce.soap.v1_0.dceconsulta import DceConsultaSoap12DceConsulta
from nfelib.dce.soap.v1_0.dcerecepcaoevento import (
    DceRecepcaoEventoSoap12DceRecepcaoEvento,
)
from nfelib.dce.soap.v1_0.dcestatusservico import (
    DceStatusServicoSoap12DceStatusServico,
)

_logger = logging.getLogger(__name__)

XML_DECLARATION = re.compile(r"^\s*<\?xml[^>]*\?>")

ACTION_TO_ENDPOINT = {
    DceStatusServicoSoap12DceStatusServico: Endpoint.DCESTATUSSERVICO,
    DceConsultaSoap12DceConsulta: Endpoint.DCECONSULTA,
    DceAutorizacaoSoap12DceAutorizacao: Endpoint.DCEAUTORIZACAO,
    DceRecepcaoEventoSoap12DceRecepcaoEvento: Endpoint.DCERECEPCAOEVENTO,
}


class DceClient(FiscalClient):
    """A façade for the DC-e v1.00 SOAP webservices."""

    def __init__(self, **kwargs: Any):
        self.mod = kwargs.pop("mod", "99")
        kwargs.setdefault("soap12_envelope", True)
        super().__init__(service="dce", versao="1.00", **kwargs)

    def _get_location(self, endpoint_type: Endpoint) -> str:
        """Constructs the full HTTPS URL for the specified service."""
        server_data = SERVERS_DCE["AN"]
        endpoints = (
            server_data["prod_endpoints"]
            if self.ambiente == "1"  # production
            else server_data["dev_endpoints"]
        )
        # the portal lists the addresses of the WSDL (?wsdl)
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
        """Builds and sends a request, wrapping the payload in dceDadosMsg."""
        self._soap_action = action_class.soapAction
        response = super().send(
            action_class=action_class,
            location=self._get_location(ACTION_TO_ENDPOINT[action_class]),
            wrapped_obj={"Body": {"dceDadosMsg": dados_msg}},
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
        """Return the payload element of the DC-e SOAP response Body.

        The answer element is not named in the manual: it is read from the
        <operation>Result element or from dceResultMsg.
        """
        for attr in (
            "dceAutorizacaoResult",
            "dceRecepcaoEventoResult",
            "dceStatusServicoResult",
            "dceResultMsg",
        ):
            result = getattr(body, attr, None)
            if result is not None and result.content:
                return result.content[0]
        fault = body.fault.faultstring if body.fault is not None else None
        raise ValueError(f"No known result element in the DC-e SOAP response: {fault}")

    def status_servico(self) -> RetConsStatServDce:
        """Consulta o status do serviço DC-e."""
        payload = ConsStatServDce(
            tpAmb=Tamb(self.ambiente), cUF=TcodUfIbge(self.uf), versao=self.versao
        )
        return self.send(DceStatusServicoSoap12DceStatusServico, {"content": [payload]})

    def consulta_documento(self, chave: str) -> RetConsSitDce:
        """Consulta a situação de uma DC-e pela chave de acesso."""
        payload = ConsSitDce(tpAmb=Tamb(self.ambiente), chDCe=chave, versao=self.versao)
        return self.send(DceConsultaSoap12DceConsulta, {"content": [payload]})

    def envia_documento(self, dce_obj: Tdce) -> RetDce:
        """Envia uma DC-e de forma síncrona.

        The signed DC-e is injected raw with a placeholder so the signature
        survives the payload serialization.
        """
        signed_xml = dce_obj.to_xml(
            pkcs12_data=self.pkcs12_data,
            pkcs12_password=self.pkcs12_password,
            doc_id=dce_obj.infDCe.Id,
        )
        return self.send(
            DceAutorizacaoSoap12DceAutorizacao,
            {"content": [Dce()]},
            placeholder_exp=r"<DCe[^>]*/>|<DCe[ >].*?</DCe>",
            placeholder_content=XML_DECLARATION.sub("", signed_xml),
        )

    def envia_evento(
        self,
        chave: str,
        tpEvento: str,
        nSeqEvento: str,
        detEvento: Any,
        tp_emit: str,
        cnpj_autor: str,
        cnpj_cpf_emitente: str,
        dhEvento: Optional[str] = None,
    ) -> RetEventoDce:
        """Envia um evento genérico para uma DC-e.

        Args:
            chave: the access key of the DC-e.
            tpEvento: the event type (110111 for the cancellation).
            nSeqEvento: the sequence number of the event.
            detEvento: the event detail binding (EvCancDce for instance).
            tp_emit: the tpEmit of the DC-e (0 fisco, 1 marketplace,
                2 own issuer, 3 carrier).
            cnpj_autor: the CNPJ that signs the event (the one of the key).
            cnpj_cpf_emitente: the CNPJ or CPF of the issuing user.
            dhEvento: the event date, now by default.
        """
        inf_evento = EventoDce.InfEvento(
            # the XSD takes "ID" + tpEvento + chDCe + nSeqEvento (3 digits)
            Id=f"ID{tpEvento}{chave}{nSeqEvento.zfill(3)}",
            # the UF of the access key
            cOrgao=TcorgaoIbge(chave[:2]),
            tpAmb=Tamb(self.ambiente),
            tpEmit=tp_emit,
            CNPJAutor=cnpj_autor,
            chDCe=chave,
            dhEvento=dhEvento or self._timestamp(),
            tpEvento=tpEvento,
            nSeqEvento=nSeqEvento,
            detEvento=EventoDce.InfEvento.DetEvento(
                any_element=detEvento, versaoEvento=self.versao
            ),
        )
        if len(cnpj_cpf_emitente) == 14:
            inf_evento.CNPJUsEmit = cnpj_cpf_emitente
        else:
            inf_evento.CPFUsEmit = cnpj_cpf_emitente

        evento = EventoDce(versao=self.versao, infEvento=inf_evento)
        signed_xml = evento.to_xml(
            pkcs12_data=self.pkcs12_data,
            pkcs12_password=self.pkcs12_password,
            doc_id=evento.infEvento.Id,
        )
        return self.send(
            DceRecepcaoEventoSoap12DceRecepcaoEvento,
            {"content": [EventoDce(versao=self.versao)]},
            placeholder_exp=r"<eventoDCe[^>]*/>|<eventoDCe.*?>.*?</eventoDCe>",
            placeholder_content=XML_DECLARATION.sub("", signed_xml),
        )

    def cancela_documento(
        self,
        chave: str,
        protocolo_autorizacao: str,
        justificativa: str,
        tp_emit: str,
        cnpj_autor: str,
        cnpj_cpf_emitente: str,
    ) -> RetEventoDce:
        """Cancela uma DC-e autorizada."""
        det_evento = EvCancDce(
            descEvento=EvCancDceDescEvento.CANCELAMENTO,
            nProt=protocolo_autorizacao,
            xJust=justificativa,
        )
        return self.envia_evento(
            chave=chave,
            tpEvento="110111",
            nSeqEvento="1",
            detEvento=det_evento,
            tp_emit=tp_emit,
            cnpj_autor=cnpj_autor,
            cnpj_cpf_emitente=cnpj_cpf_emitente,
        )
