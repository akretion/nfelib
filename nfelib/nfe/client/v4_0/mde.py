# FILEPATH: nfelib/nfe/client/v4_0/mde.py
# Copyright (C) 2020 - KMEE
# Copyright (C) 2025  Raphaël Valyi - Akretion

import logging
from datetime import datetime
from typing import Any, Optional

from brazil_fiscal_client.fiscal_client import FiscalClient, Tamb

# --- Server Definitions & SOAP Bindings ---
from nfelib.nfe.client.v4_0.servers import Endpoint
from nfelib.nfe.client.v4_0.servers import servers as SERVERS_NFE
from nfelib.nfe.soap.v4_0.recepcaoevento4 import (
    NfeRecepcaoEvento4SoapNfeRecepcaoEvento,
)

# --- MD-e Event Bindings ---
from nfelib.nfe_evento_mde.bindings.v1_0.leiaute_conf_recebto_v1_00 import (
    DetEventoDescEvento,
    InfEventoTpEvento,
    TcorgaoIbge,
    TenvEvento,
    Tevento,
    TretEnvEvento,
)

_logger = logging.getLogger(__name__)

# TODO Flaw/Inconsistency: Method names like confirmacao_da_operacao are 
# not Pythonic. The use of _ separates words but the name itself is a noun phrase, 
# not a verb.
# TODO confirmacao_da_operacao -> confirmar_operacao;
# ciencia_da_operacao -> registrar_ciencia; 
# desconhecimento_da_operacao -> registrar_desconhecimento; 
# operacao_nao_realizada -> registrar_operacao_nao_realizada 
# (and require justificativa as a non-optional argument).


class MdeClient(FiscalClient):
    """A façade for the NFe Manifestação do Destinatário (MD-e) SOAP webservices."""

    def __init__(self, **kwargs: Any):
        # The user provides their own UF, but for endpoint resolution, MD-e always uses Ambiente Nacional (AN).
        # We will override _get_location to enforce this.
        super().__init__(
            service="nfe",
            versao="1.00",  # MD-e events have their own versioning, typically 1.00
            **kwargs,
        )

    def _get_location(self, endpoint_type: Endpoint) -> str:
        """Overrides the parent method to always use the Ambiente Nacional (AN)
        server for MD-e event reception, regardless of the client's configured UF.
        """
        if endpoint_type != Endpoint.RECEPCAOEVENTO:
            raise ValueError(
                f"Endpoint {endpoint_type.name} is not supported for MDeClient. "
                "Only RecepcaoEvento is allowed."
            )

        server_key = "AN"  # Always use Ambiente Nacional
        server_data = SERVERS_NFE[server_key]
        server_host = (
            server_data["prod_server"]
            if self.ambiente == Tamb.PROD.value
            else server_data["dev_server"]
        )
        path = server_data["endpoints"][endpoint_type]
        location = f"https://{server_host}{path}"
        _logger.debug(
            f"Determined MD-e location for {endpoint_type.name} "
            f"(Amb: {self.ambiente}): {location}"
        )
        return location

    def send(
        self,
        action_class: type,
        obj: Any,
        placeholder_exp: Optional[str] = None,
        placeholder_content: Optional[str] = None,
        **kwargs: Any,
    ) -> Any:
        """Builds and sends a request for the input object, correctly wrapping it."""
        endpoint_type = Endpoint.RECEPCAOEVENTO
        location = self._get_location(endpoint_type)

        wrapped_obj = {"Body": {"nfeDadosMsg": {"content": [obj]}}}

        response = super().send(
            action_class=action_class,
            location=location,
            wrapped_obj=wrapped_obj,
            placeholder_exp=placeholder_exp,
            placeholder_content=placeholder_content,
            **kwargs,
        )

        if not self.wrap_response:
            return response.body.nfeResultMsg.content[0]

        # Adapt the wrapped response to contain the direct result
        response.resposta = response.resposta.body.nfeResultMsg.content[0]
        return response

    def nfe_recepcao_envia_lote_evento(
        self, lista_eventos: list[Tevento], numero_lote: Optional[str] = None
    ) -> TretEnvEvento:
        """Signs and sends a batch of manifestation events.

        :param lista_eventos: A list of fully formed Tevento objects to be sent.
        :param numero_lote: Optional batch number. If not provided, one is generated.
        :return: The processing result from the SEFAZ.
        """
        if not numero_lote:
            numero_lote = str(int(datetime.now().timestamp() * 1000))[-15:]

        signed_events_xml = []
        for evento in lista_eventos:
            signed_xml = evento.to_xml(
                pkcs12_data=self.pkcs12_data,
                pkcs12_password=self.pkcs12_password,
                doc_id=evento.infEvento.Id,
            )
            signed_events_xml.append(signed_xml)

        env_evento_payload = TenvEvento(
            versao="1.00",
            idLote=numero_lote,
            evento=[Tevento()],  # Placeholder for replacement
        )

        # The placeholder should match the entire <evento> tag block
        placeholder_exp = r"<evento.*?>.*?</evento>"

        return self.send(
            NfeRecepcaoEvento4SoapNfeRecepcaoEvento,
            env_evento_payload,
            placeholder_exp=placeholder_exp,
            placeholder_content="".join(signed_events_xml),
        )

    def _monta_evento(
        self,
        chave: str,
        cnpj_cpf: str,
        tpEvento: InfEventoTpEvento,
        descEvento: DetEventoDescEvento,
        nSeqEvento: str = "1",
        xJust: Optional[str] = None,
    ) -> Tevento:
        """Helper method to create the full Tevento structure for a manifestation event."""
        if not (isinstance(chave, str) and len(chave) == 44 and chave.isdigit()):
            raise ValueError(f"Chave de acesso inválida: {chave}")
        if not (1 <= int(nSeqEvento) <= 20):
            raise ValueError("Sequência do evento inválida (1-20).")

        doc_destinatario = {}
        if len(cnpj_cpf) == 14 and cnpj_cpf.isdigit():
            doc_destinatario = {"CNPJ": cnpj_cpf, "CPF": None}
        elif len(cnpj_cpf) == 11 and cnpj_cpf.isdigit():
            doc_destinatario = {"CNPJ": None, "CPF": cnpj_cpf}
        else:
            raise ValueError(f"CNPJ/CPF do destinatário inválido: {cnpj_cpf}")

        inf_evento = Tevento.InfEvento(
            Id="ID" + tpEvento.value + chave + nSeqEvento.zfill(2),
            cOrgao=TcorgaoIbge.VALUE_91,
            tpAmb=Tamb(self.ambiente),
            CNPJ=doc_destinatario["CNPJ"],
            CPF=doc_destinatario["CPF"],
            chNFe=chave,
            dhEvento=self._timestamp(),
            tpEvento=tpEvento,
            nSeqEvento=nSeqEvento,
            verEvento="1.00",
            detEvento=Tevento.InfEvento.DetEvento(
                versao="1.00", descEvento=descEvento, xJust=xJust
            ),
        )
        return Tevento(versao="1.00", infEvento=inf_evento)

    def _enviar_evento_unitario(
        self,
        chave: str,
        cnpj_cpf: str,
        tpEvento: InfEventoTpEvento,
        descEvento: DetEventoDescEvento,
        xJust: Optional[str] = None,
    ) -> TretEnvEvento:
        """Creates and sends a single manifestation event."""
        evento = self._monta_evento(
            chave=chave,
            cnpj_cpf=cnpj_cpf,
            tpEvento=tpEvento,
            descEvento=descEvento,
            xJust=xJust,
        )
        return self.nfe_recepcao_envia_lote_evento(
            lista_eventos=[evento], numero_lote="1"
        )

    def confirmacao_da_operacao(self, chave: str, cnpj_cpf: str) -> TretEnvEvento:
        return self._enviar_evento_unitario(
            chave=chave,
            cnpj_cpf=cnpj_cpf,
            tpEvento=InfEventoTpEvento.VALUE_210200,
            descEvento=DetEventoDescEvento.CONFIRMACAO_DA_OPERACAO,
        )

    def ciencia_da_operacao(self, chave: str, cnpj_cpf: str) -> TretEnvEvento:
        return self._enviar_evento_unitario(
            chave=chave,
            cnpj_cpf=cnpj_cpf,
            tpEvento=InfEventoTpEvento.VALUE_210210,
            descEvento=DetEventoDescEvento.CIENCIA_DA_OPERACAO,
        )

    def desconhecimento_da_operacao(self, chave: str, cnpj_cpf: str) -> TretEnvEvento:
        return self._enviar_evento_unitario(
            chave=chave,
            cnpj_cpf=cnpj_cpf,
            tpEvento=InfEventoTpEvento.VALUE_210220,
            descEvento=DetEventoDescEvento.DESCONHECIMENTO_DA_OPERACAO,
        )

    def operacao_nao_realizada(
        self, chave: str, cnpj_cpf: str, justificativa: str
    ) -> TretEnvEvento:
        if not (15 <= len(justificativa) <= 255):
            raise ValueError(
                "Justificativa para 'Operação não Realizada' deve ter entre 15 e 255 caracteres."
            )
        return self._enviar_evento_unitario(
            chave=chave,
            cnpj_cpf=cnpj_cpf,
            tpEvento=InfEventoTpEvento.VALUE_210240,
            descEvento=DetEventoDescEvento.OPERACAO_NAO_REALIZADA,
            xJust=justificativa,
        )
