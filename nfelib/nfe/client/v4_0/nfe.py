# Copyright (C) 2019  Luis Felipe Mileo - KMEE
# Copyright (C) 2025  Raphaël Valyi - Akretion

import logging
import time
from datetime import date, datetime
from typing import Any, Optional

from brazil_fiscal_client.fiscal_client import (
    FiscalClient,
    Tamb,
    TcodUfIbge,
    WrappedResponse,
)
from lxml import etree

from nfelib import CommonMixin
from nfelib.nfe.bindings.v4_0.cons_reci_nfe_v4_00 import ConsReciNfe
from nfelib.nfe.bindings.v4_0.cons_sit_nfe_v4_00 import ConsSitNfe
from nfelib.nfe.bindings.v4_0.cons_stat_serv_v4_00 import ConsStatServ
from nfelib.nfe.bindings.v4_0.envi_nfe_v4_00 import EnviNfe
from nfelib.nfe.bindings.v4_0.inut_nfe_v4_00 import InutNfe
from nfelib.nfe.bindings.v4_0.leiaute_cons_sit_nfe_v4_00 import (
    TconsSitNfeXServ,
    TprotNfe,
)
from nfelib.nfe.bindings.v4_0.leiaute_cons_stat_serv_v4_00 import TconsStatServXServ
from nfelib.nfe.bindings.v4_0.leiaute_inut_nfe_v4_00 import InfInutXServ
from nfelib.nfe.bindings.v4_0.leiaute_nfe_v4_00 import TenviNfeIndSinc, Tnfe

# --- Content Bindings ---
from nfelib.nfe.bindings.v4_0.proc_nfe_v4_00 import NfeProc
from nfelib.nfe.bindings.v4_0.ret_cons_reci_nfe_v4_00 import RetConsReciNfe
from nfelib.nfe.bindings.v4_0.ret_cons_sit_nfe_v4_00 import RetConsSitNfe
from nfelib.nfe.bindings.v4_0.ret_cons_stat_serv_v4_00 import RetConsStatServ
from nfelib.nfe.bindings.v4_0.ret_envi_nfe_v4_00 import RetEnviNfe
from nfelib.nfe.bindings.v4_0.ret_inut_nfe_v4_00 import RetInutNfe

# Corrected import for InutNfe.InfInut
from nfelib.nfe.bindings.v4_0.tipos_basico_v4_00 import Tmod
from nfelib.nfe.client.v4_0.servers import Endpoint

# --- Server Definitions ---
# Import Endpoint Enum and the servers dictionary directly
from nfelib.nfe.client.v4_0.servers import servers as SERVERS_NFE

# --- SOAP Bindings ---
from nfelib.nfe.soap.v4_0.nfeautorizacao4 import (
    NfeAutorizacao4SoapNfeAutorizacaoLote,
)
from nfelib.nfe.soap.v4_0.nfeconsulta4 import (
    NfeConsultaProtocolo4SoapNfeConsultaNf,
)
from nfelib.nfe.soap.v4_0.nfeinutilizacao4 import (
    NfeInutilizacao4SoapNfeInutilizacaoNf,
)
from nfelib.nfe.soap.v4_0.nferetautorizacao4 import (
    NfeRetAutorizacao4SoapNfeRetAutorizacaoLote,
)
from nfelib.nfe.soap.v4_0.nfestatusservico4 import (
    NfeStatusServico4SoapNfeStatusServicoNf,
)
from nfelib.nfe.soap.v4_0.recepcaoevento4 import (
    NfeRecepcaoEvento4SoapNfeRecepcaoEvento,
)

# --- Dist DF-e ---
from nfelib.nfe_evento_cancel.bindings.v1_0.e110111_v1_00 import (
    DetEventoDescEvento as DetEventoDescEventoCancel,
)
from nfelib.nfe_evento_cancel.bindings.v1_0.e110111_v1_00 import (
    DetEventoVersao as DetEventoVersaoCancel,
)

# --- Event Bindings ---
from nfelib.nfe_evento_cancel.bindings.v1_0.evento_canc_nfe_v1_00 import (
    Evento as TeventoCancel,
)
from nfelib.nfe_evento_cancel.bindings.v1_0.leiaute_evento_canc_nfe_v1_00 import (
    InfEventoTpEvento as InfEventoTpEventoCancel,
)
from nfelib.nfe_evento_cancel.bindings.v1_0.leiaute_evento_canc_nfe_v1_00 import (
    InfEventoVerEvento as InfEventoVerEventoCancel,
)
from nfelib.nfe_evento_cancel.bindings.v1_0.leiaute_evento_canc_nfe_v1_00 import (
    TretEnvEvento,
)
from nfelib.nfe_evento_cce.bindings.v1_0.leiaute_cce_v1_00 import (
    DetEventoDescEvento as DetEventoDescEventoCCe,
)
from nfelib.nfe_evento_cce.bindings.v1_0.leiaute_cce_v1_00 import (
    DetEventoVersao as DetEventoVersaoCCe,
)
from nfelib.nfe_evento_cce.bindings.v1_0.leiaute_cce_v1_00 import (
    DetEventoXCondUso,
)
from nfelib.nfe_evento_cce.bindings.v1_0.leiaute_cce_v1_00 import (
    InfEventoTpEvento as InfEventoTpEventoCCe,
)
from nfelib.nfe_evento_cce.bindings.v1_0.leiaute_cce_v1_00 import (
    InfEventoVerEvento as InfEventoVerEventoCCe,
)
from nfelib.nfe_evento_cce.bindings.v1_0.leiaute_cce_v1_00 import (
    Tevento as TeventoCCe,
)

# --- Constants ---
TIPO_EVENTO_CCE = "110110"
TIPO_EVENTO_CANCEL = "110111"

_logger = logging.getLogger(__name__)


# --- UF to Server Key Mapping & Logic (based on SEFAZ page) ---

# 1. Define sets for easier checking based on SEFAZ rules
_SVRS_CONSULTACADASTRO_UFS = {"12", "32", "24", "25", "42"}  # AC, ES, RN, PB, SC
_SVRS_NORMAL_UFS = {
    "12",
    "27",
    "16",
    "23",
    "53",
    "32",
    "15",
    "25",
    "22",
    "33",
    "24",
    "11",
    "14",
    "42",
    "28",
    "17",
}  # AC, AL, AP, CE, DF, ES, PA, PB, PI, RJ, RN, RO, RR, SC, SE, TO
_SVAN_NORMAL_UFS = {"21"}  # MA

# UFs with their own dedicated servers (not using SVRS/SVAN normally)
_OWN_SERVER_UFS = {
    "13": "AM",  # Amazonas
    "29": "BA",  # Bahia
    "52": "GO",  # Goiás
    "31": "MG",  # Minas Gerais
    "50": "MS",  # Mato Grosso do Sul
    "51": "MT",  # Mato Grosso do Sul
    "26": "PE",  # Pernambuco
    "41": "PR",  # Paraná <= Uses SVRS now based on the page
    "43": "RS",  # Rio Grande do Sul
    "35": "SP",  # São Paulo
}

_SVAN_NORMAL_UFS = {"21", "15"}  # MA, PA
_SVRS_NORMAL_UFS = {  # Re-list SVRS UFs excluding MA, PA
    "12",
    "27",
    "16",
    "23",
    "53",
    "32",
    "25",
    "22",
    "33",
    "24",
    "11",
    "14",
    "42",
    "28",
    "17",
}  # AC, AL, AP, CE, DF, ES, PB, PI, RJ, RN, RO, RR, SC, SE, TO
_OWN_SERVER_UFS = {  # Re-list Own Server UFs excluding CE
    "13": "AM",  # Amazonas
    "29": "BA",  # Bahia
    "52": "GO",  # Goiás
    "31": "MG",  # Minas Gerais
    "50": "MS",  # Mato Grosso do Sul
    "51": "MT",  # Mato Grosso do Sul
    "26": "PE",  # Pernambuco
    "41": "PR",  # Paraná
    "43": "RS",  # Rio Grande do Sul
    "35": "SP",  # São Paulo
}


def _get_server_key_for_uf(uf_ibge_code: str, endpoint: Endpoint) -> str:
    """Get the server key ('AM', 'SVRS', 'AN', etc.) for a given UF and Endpoint."""
    # 1. Check ConsultaCadastro special rule
    if (
        endpoint == Endpoint.NFECONSULTACADASTRO
        and uf_ibge_code in _SVRS_CONSULTACADASTRO_UFS
    ):
        _logger.debug(f"Using SVRS for ConsultaCadastro for UF {uf_ibge_code}")
        return "SVRS"

    # 2. Check UFs with their own servers
    if uf_ibge_code in _OWN_SERVER_UFS:
        return _OWN_SERVER_UFS[uf_ibge_code]

    # 3. Check UFs using SVAN
    if uf_ibge_code in _SVAN_NORMAL_UFS:
        return "SVAN"

    # 4. Check UFs using SVRS (default for most others listed)
    if uf_ibge_code in _SVRS_NORMAL_UFS:
        return "SVRS"

    # 5. Fallback/Error Handling - Should not happen if all UFs are mapped
    _logger.error(
        f"Could not determine server key for UF {uf_ibge_code} and endpoint "
        "{endpoint.name}. Check mappings."
    )
    # Defaulting to SVRS might hide configuration issues, raising an error is safer.
    raise ValueError(f"Server mapping not found for UF {uf_ibge_code}")


# TODO methods -> verbs
# TODO enviar_documento -> envior_lote


class NfeClient(FiscalClient):
    """A façade for the NFe SOAP webservices."""

    def __init__(self, **kwargs: Any):
        self.mod = kwargs.pop("mod", "55")
        super().__init__(
            service="nfe",
            versao="4.00",
            **kwargs,
        )

    def _get_location(self, endpoint_type: Endpoint) -> str:
        """Construct the full HTTPS URL for the specified service."""
        server_key = _get_server_key_for_uf(self.uf, endpoint_type)
        try:
            server_data = SERVERS_NFE[server_key]
        except KeyError:
            raise ValueError(
                f"No server configuration found for key: {server_key} "
                "(derived from UF {self.uf})"
            )

        if self.ambiente == Tamb.PROD.value:
            server_host = server_data["prod_server"]
        else:
            server_host = server_data["dev_server"]

        try:
            path = server_data["endpoints"][endpoint_type]
        except KeyError:
            raise ValueError(
                f"Endpoint {endpoint_type.name} not configured for server key: "
                "{server_key}"
            )

        location = f"https://{server_host}{path}"
        _logger.debug(
            f"Determined location for {endpoint_type.name} (UF: {self.uf}, "
            "Amb: {self.ambiente}): {location}"
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
        """Build and send a request for the input object.

        Args:
            action_class: type generated with xsdata for the SOAP wsdl action
                          (e.g., NfeStatusServico4SoapNfeStatusServicoNf).
            obj: The *content* model instance (e.g., ConsStatServ) or a dictionary.
                 This will be wrapped inside nfeDadosMsg.
            placeholder_content: A string content to be injected in the payload.
                                 Used for signed content to avoid signature issues.
            placeholder_exp: Placeholder expression where to inject placeholder_content.
            kwargs: Additional keyword arguments for FiscalClient.send.

        Returns:
            The *content* response model instance (e.g., RetConsStatServ).
        """
        try:
            # Determine the correct endpoint enum based on the action class
            action_to_endpoint_map: dict[type, Endpoint] = {
                NfeStatusServico4SoapNfeStatusServicoNf: Endpoint.NFESTATUSSERVICO,
                NfeConsultaProtocolo4SoapNfeConsultaNf: Endpoint.NFECONSULTAPROTOCOLO,
                NfeAutorizacao4SoapNfeAutorizacaoLote: Endpoint.NFEAUTORIZACAO,
                NfeRetAutorizacao4SoapNfeRetAutorizacaoLote: Endpoint.NFERETAUTORIZACAO,
                NfeInutilizacao4SoapNfeInutilizacaoNf: Endpoint.NFEINUTILIZACAO,
                NfeRecepcaoEvento4SoapNfeRecepcaoEvento: Endpoint.RECEPCAOEVENTO,
            }
            endpoint_type = action_to_endpoint_map[action_class]
            location = self._get_location(endpoint_type)

        except KeyError:
            raise ValueError(
                "Could not determine Endpoint for action_class: {action_class.__name__}"
            )
        wrapped_obj = {"Body": {"nfeDadosMsg": {"content": [obj]}}}

        response = super().send(
            action_class,
            location,
            wrapped_obj,
            placeholder_exp=placeholder_exp,
            placeholder_content=placeholder_content,
            **kwargs,
        )
        if not self.wrap_response:
            return response.body.nfeResultMsg.content[0]
        response.resposta = response.resposta.body.nfeResultMsg.content[0]
        return response

    ######################################
    # Webservices
    ######################################

    def status_servico(self) -> Optional[RetConsStatServ]:
        """Consulta o status do serviço NFe."""
        payload = ConsStatServ(
            tpAmb=Tamb(self.ambiente),
            cUF=TcodUfIbge(self.uf),
            xServ=TconsStatServXServ.STATUS,
            versao=self.versao,
        )
        return self.send(NfeStatusServico4SoapNfeStatusServicoNf, payload)

    def consulta_documento(self, chave: str) -> Optional[RetConsSitNfe]:
        """Consulta a situação de uma NF-e pela chave de acesso."""
        if not (isinstance(chave, str) and len(chave) == 44 and chave.isdigit()):
            raise ValueError(f"Chave de acesso inválida: {chave}")

        payload = ConsSitNfe(
            versao=self.versao,
            tpAmb=Tamb(self.ambiente),
            xServ=TconsSitNfeXServ.CONSULTAR,
            chNFe=chave,
        )
        return self.send(NfeConsultaProtocolo4SoapNfeConsultaNf, payload)

    # NOTE: I changed the signature from erpbrasil.edoc to support a list of NFe's
    def envia_documento(
        self,
        lista_nfes: list,
        id_lote: str = "",
        ind_sinc: TenviNfeIndSinc = TenviNfeIndSinc.VALUE_1,
    ) -> RetEnviNfe:
        """Autoriza uma lista de NFe's."""
        signed_nfes = []
        for nfe in lista_nfes:
            if isinstance(nfe, str):
                if "X509Certificate" in nfe:
                    signed_nfes.append(nfe)
                else:
                    nfe_etree = etree.fromstring(nfe.encode("utf-8"))
                    ns = {"nfe": "http://www.portalfiscal.inf.br/nfe"}
                    doc_id = nfe_etree.xpath("//nfe:infNFe/@Id", namespaces=ns)[0]
                    signed_nfes.append(
                        CommonMixin.sign_xml(
                            xml=nfe,
                            pkcs12_data=self.pkcs12_data,
                            pkcs12_password=self.pkcs12_password,
                            doc_id=doc_id,
                        )
                    )
            else:
                signed_nfes.append(
                    nfe.to_xml(
                        pkcs12_data=self.pkcs12_data,
                        pkcs12_password=self.pkcs12_password,
                        doc_id=nfe.infNFe.Id,
                    )
                )

        return self.send(
            NfeAutorizacao4SoapNfeAutorizacaoLote,
            EnviNfe(
                idLote=id_lote or datetime.now().strftime("%Y%m%d%H%M%S"),
                versao=self.versao,
                indSinc=ind_sinc,
                # we pass an empty placeholder_exp for the NFe to avoid an extra
                # XML parsing/serialization and possibly screwing the signature.
                NFe=[Tnfe()],
            ),
            placeholder_exp="<NFe/>",
            placeholder_content="".join(signed_nfes),
        )

    def processar_lote(self, lista_nfes: list):  # adapted from processar_documento
        if False:  # TODO self._consulta_servico_ao_enviar:
            pass
        if False:  # self._consulta_documento_antes_de_enviar:
            pass

        proc_envio = self.envia_documento(lista_nfes)
        # if self.envio_sincrono:  # TODO
        #    self.monta_processo(proc_envio)
        yield proc_envio

        if (
            (proc_envio.resposta if self.wrap_response else proc_envio).cStat
            not in ("103", "104")
            # TODO or self.envio_sincrono
        ):
            return

        #
        # Aguarda o tempo do processamento antes da consulta
        #
        self._aguarda_tempo_medio(proc_envio)
        #
        # Consulta o recibo do lote, para ver o que aconteceu
        #
        proc_recibo = self.consulta_recibo(proc_envio=proc_envio)
        if not (proc_recibo.resposta if self.wrap_response else proc_recibo):
            return

        #
        # Tenta receber o resultado do processamento do lote, caso ainda
        # esteja em processamento
        #
        tentativa = 0
        while (
            (proc_recibo.resposta if self.wrap_response else proc_recibo).cStat
            == "105"  # em processamento
            and tentativa < self._maximo_tentativas_consulta_recibo
        ):
            self._aguarda_tempo_medio(proc_envio)
            tentativa += 1
            #
            # Consulta o recibo do lote, para ver o que aconteceu
            #
            proc_recibo = self.consulta_recibo(proc_envio=proc_envio)
        self.monta_processo(proc_envio, proc_recibo, lista_nfes)
        yield proc_recibo

    def monta_processo(self, proc_envio, proc_recibo=None, lista_nfes=[]):
        nfe = lista_nfes[0]  # TODO could be a collection...
        # nfe = proc_envio.envio_raiz.find(
        # "{" + self._namespace + "}NFe"
        # )  # Se proc_envio for 'None', debugar o método 'analisar_retorno_raw'

        if proc_recibo:
            if self.wrap_response:
                proc_recibo = proc_recibo.resposta
            protocolos = proc_recibo.protNFe
        else:
            # A falta do recibo indica envio no modo síncrono
            # o protocolo é recuperado diretamente da resposta do envio.
            if self.wrap_response:
                proc_envio = proc_envio.resposta
            protocolos = proc_envio.protNFe
        if False:  # TODO finish if len(nfe) and protocolos:
            if not isinstance(protocolos, list):
                protocolos = [protocolos]
            for protocolo in protocolos:
                from nfelib.nfe.bindings.v4_0.proc_nfe_v4_00 import NfeProc

                nfe_proc = NfeProc(
                    versao=self.versao,
                    protNFe=protocolo,
                )
                xml_file, nfe_proc = self._generateds_to_string_etree(nfe_proc)
                prot_nfe = nfe_proc.find("{" + self._namespace + "}protNFe")
                prot_nfe.addprevious(nfe)

                proc = proc_recibo if proc_recibo else proc_envio
                proc.processo = nfe_proc
                proc.processo_xml = self._generateds_to_string_etree(nfe_proc)[0]
                proc.protocolo = protocolo
            return True

    def monta_nfe_proc(self, nfe, prot_nfe: TprotNfe):
        """Constrói e retorna o XML do processo da NF-e,
        incorporando a NF-e com o seu protocolo de autorização.
        """
        if isinstance(nfe, bytes):
            nfe = nfe.decode("utf-8")
        if isinstance(nfe, str):
            nfe = Tnfe.from_xml(nfe)
        else:
            nfe = etree.tostring(nfe).decode("utf-8")

        if isinstance(prot_nfe, WrappedResponse):
            # TODO it seems monta_nfe_proc is called
            # in two different ways accross Odoo tests
            # we could probably avoid these ifs
            prot_nfe = prot_nfe.resposta

        nfe_proc = NfeProc(
            versao=self.versao,
            NFe=nfe,
            protNFe=prot_nfe,
        )

        return nfe_proc.to_xml()

    def envia_inutilizacao(self, inut: Any) -> Optional[RetInutNfe]:
        """Envia um pedido de inutilização de numeração (XML já assinado)."""
        if not isinstance(inut, str):
            inut = inut.to_xml()
        if "X509Certificate" not in inut:
            inut_etree = etree.fromstring(inut.encode("utf-8"))
            ns = {"nfe": "http://www.portalfiscal.inf.br/nfe"}
            doc_id = inut_etree.xpath("//nfe:infInut/@Id", namespaces=ns)[0]
            inut = CommonMixin.sign_xml(
                xml=inut,
                pkcs12_data=self.pkcs12_data,
                pkcs12_password=self.pkcs12_password,
                doc_id=doc_id,
            )

        # Placeholder object for wrapping. The actual content comes
        # from signed_inut_xml.
        payload_for_wrapping = InutNfe(versao=self.versao)  # Minimal object

        # The placeholder should match the <inutNFe> tag within
        # the SOAP Body's nfeDadosMsg
        # Example: <nfeDadosMsg><inutNFe>...</inutNFe></nfeDadosMsg>
        placeholder_exp = r"<inutNFe.*?>.*?</inutNFe>"

        return self.send(
            NfeInutilizacao4SoapNfeInutilizacaoNf,
            payload_for_wrapping,  # Pass the object to be wrapped
            placeholder_exp=placeholder_exp,
            placeholder_content=inut,  # The actual signed XML content
        )

    def consulta_recibo(
        self, numero: str = "", proc_envio: Optional[RetEnviNfe] = None
    ) -> Optional[RetConsReciNfe]:
        """Consulta o resultado do processamento de um lote enviado."""
        recibo_a_consultar = numero
        if proc_envio:
            if self.wrap_response:
                proc_envio = proc_envio.resposta
            # Ensure infRec exists and has nRec
            if proc_envio.infRec and proc_envio.infRec.nRec:
                recibo_a_consultar = proc_envio.infRec.nRec
            else:
                _logger.warning("proc_envio fornecido sem infRec.nRec válido.")

        if not recibo_a_consultar:
            raise ValueError(
                "Número do recibo (nRec) não fornecido ou encontrado em proc_envio."
            )
        if not (
            isinstance(recibo_a_consultar, str)
            and len(recibo_a_consultar) == 15
            and recibo_a_consultar.isdigit()
        ):
            raise ValueError(f"Número do recibo inválido: {recibo_a_consultar}")

        payload = ConsReciNfe(
            versao=self.versao,
            tpAmb=Tamb(self.ambiente),
            nRec=recibo_a_consultar,
        )
        return self.send(NfeRetAutorizacao4SoapNfeRetAutorizacaoLote, payload)

    def enviar_lote_evento(
        self, lista_eventos: list[TeventoCancel], numero_lote: str = False
    ) -> Optional[TretEnvEvento]:
        """Envia um lote de eventos."""
        # TODO seems cancel event is hardcoded or what?
        # it's called by cancela_documento. Does it make sense as a separated meth?
        if not numero_lote:
            numero_lote = datetime.now().strftime("%Y%m%d%H%M%S")
        signed_events = []
        for event in lista_eventos:
            if isinstance(event, str):
                if "X509Certificate" in event:
                    signed_events.append(event)
                else:
                    event_etree = etree.fromstring(event.encode("utf-8"))
                    ns = {"nfe": "http://www.portalfiscal.inf.br/nfe"}
                    doc_id = event_etree.xpath("//nfe:infEvento/@Id", namespaces=ns)[0]
                    signed_events.append(
                        CommonMixin.sign_xml(
                            xml=event,
                            pkcs12_data=self.pkcs12_data,
                            pkcs12_password=self.pkcs12_password,
                            doc_id=doc_id,
                        )
                    )
            else:
                signed_events.append(
                    event.to_xml(
                        pkcs12_data=self.pkcs12_data,
                        pkcs12_password=self.pkcs12_password,
                        doc_id=event.infEvento.Id,
                    )
                )

        # Placeholder object for wrapping.
        payload_for_wrapping = TeventoCancel(versao="1.00")
        placeholder_exp = r"<envEvento.*?>.*?</envEvento>"

        return self.send(
            NfeRecepcaoEvento4SoapNfeRecepcaoEvento,
            payload_for_wrapping,  # Pass the object to be wrapped
            placeholder_exp=placeholder_exp,
            placeholder_content=signed_events,  # The actual signed XML content
        )

    # NEW HIGH-LEVEL METHOD FOR CANCELLATION
    # TODO
    def cancelar_nfe(
        self,
        chave: str,
        protocolo_autorizacao: str,
        justificativa: str,
        cnpj_cpf: Optional[str] = None,
        data_hora_evento: Optional[str] = None,
        sequencia: str = "1",
    ) -> TretEnvEvento:
        """Cria, assina e envia um evento de cancelamento para uma NF-e.

        :param chave: Chave de acesso da NF-e a ser cancelada.
        :param protocolo_autorizacao: Protocolo de autorização da NF-e.
        :param justificativa: Justificativa do cancelamento (15-255 caracteres).
        :param cnpj_cpf: CNPJ ou CPF do autor do evento. Se omitido, será extraído da chave.
        :param data_hora_evento: Data e hora do evento (opcional, default: now).
        :param sequencia: Sequencial do evento (default: "1").
        :return: Objeto de retorno do processamento do lote de eventos.
        """
        evento_obj = self._monta_evento_cancelamento(
            chave,
            protocolo_autorizacao,
            justificativa,
            cnpj_cpf,
            data_hora_evento,
            sequencia,
        )
        return self._enviar_lote_evento([evento_obj])

    # NEW HIGH-LEVEL METHOD FOR CC-e
    # TODO
    def enviar_cce(
        self,
        chave: str,
        sequencia: str,
        justificativa: str,
        cnpj_cpf: Optional[str] = None,
        data_hora_evento: Optional[str] = None,
    ) -> TretEnvEvento:
        """Cria, assina e envia um evento de Carta de Correção (CC-e) para uma NF-e.

        :param chave: Chave de acesso da NF-e a ser corrigida.
        :param sequencia: Sequencial do evento (1-20).
        :param justificativa: Texto da correção (15-1000 caracteres).
        :param cnpj_cpf: CNPJ ou CPF do autor do evento. Se omitido, será extraído da chave.
        :param data_hora_evento: Data e hora do evento (opcional, default: now).
        :return: Objeto de retorno do processamento do lote de eventos.
        """
        evento_obj = self._monta_evento_cce(
            chave, sequencia, justificativa, cnpj_cpf, data_hora_evento
        )
        return self._enviar_lote_evento([evento_obj])

    ######################################
    # Binding Façades (Input Assembly)
    ######################################

    def cancela_documento(
        self,
        chave: str,
        protocolo_autorizacao: str,
        justificativa: str,
        cnpj_cpf: Optional[str] = None,
        data_hora_evento: Optional[str] = None,
        sequencia: str = "1",  # Default sequence
    ) -> TeventoCancel:
        """Monta o objeto Tevento para um evento de cancelamento."""
        if not (isinstance(chave, str) and len(chave) == 44 and chave.isdigit()):
            raise ValueError(f"Chave de acesso inválida: {chave}")
        if not (
            isinstance(protocolo_autorizacao, str)
            and len(protocolo_autorizacao) == 15
            and protocolo_autorizacao.isdigit()
        ):
            raise ValueError(
                f"Número do protocolo de autorização inválido: {protocolo_autorizacao}"
            )
        if not (1 <= len(justificativa) <= 255):
            raise ValueError("Justificativa deve ter entre 1 e 255 caracteres.")
        if not (
            isinstance(sequencia, str)
            and sequencia.isdigit()
            and 1 <= int(sequencia) <= 99
        ):
            raise ValueError("Sequência do evento inválida (1-99).")

        # Determine CNPJ or CPF based on input or fallback to chave
        doc_emitente = None
        if cnpj_cpf:
            if len(cnpj_cpf) == 14 and cnpj_cpf.isdigit():
                doc_emitente = {"CNPJ": cnpj_cpf, "CPF": None}
            elif len(cnpj_cpf) == 11 and cnpj_cpf.isdigit():
                doc_emitente = {"CNPJ": None, "CPF": cnpj_cpf}
            else:
                raise ValueError("CNPJ/CPF inválido fornecido.")
        else:
            # Fallback to extracting from chave (assuming CNPJ)
            doc_emitente = {"CNPJ": chave[6:20], "CPF": None}
            _logger.warning(
                "CNPJ/CPF não fornecido para cancelamento, extraindo da chave "
                "(assumindo CNPJ)."
            )

        return TeventoCancel(
            versao="1.00",
            infEvento=TeventoCancel.InfEvento(
                Id="ID" + TIPO_EVENTO_CANCEL + chave + sequencia.zfill(2),
                cOrgao=TcodUfIbge(self.uf),
                tpAmb=Tamb(self.ambiente),
                CNPJ=doc_emitente["CNPJ"],
                CPF=doc_emitente["CPF"],
                chNFe=chave,
                dhEvento=data_hora_evento or self._timestamp(),
                tpEvento=InfEventoTpEventoCancel.VALUE_110111,
                nSeqEvento=sequencia,
                verEvento=InfEventoVerEventoCancel.VALUE_1_00,
                detEvento=TeventoCancel.InfEvento.DetEvento(
                    versao=DetEventoVersaoCancel.VALUE_1_00,
                    descEvento=DetEventoDescEventoCancel.CANCELAMENTO,
                    nProt=protocolo_autorizacao,
                    xJust=justificativa,
                ),
            ),
        )

    def carta_correcao(
        self,
        chave: str,
        sequencia: str,
        justificativa: str,
        cnpj_cpf: Optional[str] = None,
        data_hora_evento: Optional[str] = None,
    ) -> TeventoCCe:
        """Monta o objeto Tevento para um evento de Carta de Correção (CC-e)."""
        if not (isinstance(chave, str) and len(chave) == 44 and chave.isdigit()):
            raise ValueError(f"Chave de acesso inválida: {chave}")
        if not (15 <= len(justificativa) <= 1000):
            raise ValueError(
                "Correção (justificativa) deve ter entre 15 e 1000 caracteres."
            )
        if not (
            isinstance(sequencia, str)
            and sequencia.isdigit()
            and 1 <= int(sequencia) <= 99
        ):
            raise ValueError("Sequência do evento inválida (1-99).")

        # Determine CNPJ or CPF
        doc_emitente = None
        if cnpj_cpf:
            if len(cnpj_cpf) == 14 and cnpj_cpf.isdigit():
                doc_emitente = {"CNPJ": cnpj_cpf, "CPF": None}
            elif len(cnpj_cpf) == 11 and cnpj_cpf.isdigit():
                doc_emitente = {"CNPJ": None, "CPF": cnpj_cpf}
            else:
                raise ValueError("CNPJ/CPF inválido fornecido.")
        else:
            # Fallback to extracting from chave (assuming CNPJ)
            doc_emitente = {"CNPJ": chave[6:20], "CPF": None}
            _logger.warning(
                "CNPJ/CPF não fornecido para CC-e, extraindo da chave (assumindo CNPJ)."
            )

        return TeventoCCe(
            versao="1.00",
            infEvento=TeventoCCe.InfEvento(
                Id="ID" + TIPO_EVENTO_CCE + chave + sequencia.zfill(2),
                cOrgao=TcodUfIbge(self.uf),
                tpAmb=Tamb(self.ambiente),
                CNPJ=doc_emitente["CNPJ"],
                CPF=doc_emitente["CPF"],
                chNFe=chave,
                dhEvento=data_hora_evento or self._timestamp(),
                tpEvento=InfEventoTpEventoCCe.VALUE_110110,
                nSeqEvento=sequencia,
                verEvento=InfEventoVerEventoCCe.VALUE_1_00,
                detEvento=TeventoCCe.InfEvento.DetEvento(
                    versao=DetEventoVersaoCCe.VALUE_1_00,
                    descEvento=DetEventoDescEventoCCe.CARTA_DE_CORRE_O,
                    xCorrecao=justificativa,
                    xCondUso=DetEventoXCondUso.A_CARTA_DE_CORRE_O_DISCIPLINADA_PELO_1_A_DO_ART_7_DO_CONV_NIO_S_N_DE_15_DE_DEZEMBRO_DE_1970_E_PODE_SER_UTILIZADA_PARA_REGULARIZA_O_DE_ERRO_OCORRIDO_NA_EMISS_O_DE_DOCUMENTO_FISCAL_DESDE_QUE_O_ERRO_N_O_ESTEJA_RELACIONADO_COM_I_AS_VARI_VEIS_QUE_DETERMINAM_O_VALOR_DO_IMPOSTO_TAIS_COMO_BASE_DE_C_LCULO_AL_QUOTA_DIFEREN_A_DE_PRE_O_QUANTIDADE_VALOR_DA_OPERA_O_OU_DA_PRESTA_O_II_A_CORRE_O_DE_DADOS_CADASTRAIS_QUE_IMPLIQUE_MUDAN_A_DO_REMETENTE_OU_DO_DESTINAT_RIO_III_A_DATA_DE_EMISS_O_OU_DE_SA_DA,
                ),
            ),
        )

    def inutilizacao(
        self,
        cnpj: str,
        mod: str,
        serie: str,
        num_ini: str,
        num_fin: str,
        justificativa: str,
    ) -> InutNfe:
        """Monta o objeto InutNfe para um pedido de inutilização."""
        if not (isinstance(cnpj, str) and len(cnpj) == 14 and cnpj.isdigit()):
            raise ValueError(f"CNPJ inválido: {cnpj}")
        # Add validation for mod, serie, num_ini, num_fin if needed
        if not (15 <= len(justificativa) <= 255):
            raise ValueError("Justificativa deve ter entre 15 e 255 caracteres.")

        year = str(date.today().year)[2:]
        num_ini_str = str(num_ini)
        num_fin_str = str(num_fin)
        serie_str = str(serie)

        # Check if numbers are valid
        if not (num_ini_str.isdigit() and 1 <= int(num_ini_str) <= 999999999):
            raise ValueError(f"Número inicial inválido: {num_ini_str}")
        if not (num_fin_str.isdigit() and 1 <= int(num_fin_str) <= 999999999):
            raise ValueError(f"Número final inválido: {num_fin_str}")
        if int(num_fin_str) < int(num_ini_str):
            raise ValueError(
                f"Número final ({num_fin_str}) não pode ser menor que o inicial "
                "({num_ini_str})."
            )
        if not (serie_str.isdigit() and 0 <= int(serie_str) <= 999):
            raise ValueError(f"Série inválida: {serie_str}")

        from nfelib.nfe.bindings.v4_0.leiaute_inut_nfe_v4_00 import TinutNfe

        return InutNfe(
            versao=self.versao,
            infInut=TinutNfe.InfInut(
                Id="ID"
                + self.uf
                + year
                + cnpj
                + mod
                + serie_str.zfill(3)
                + num_ini_str.zfill(9)
                + num_fin_str.zfill(9),
                tpAmb=Tamb(self.ambiente),
                xServ=InfInutXServ.INUTILIZAR,
                cUF=TcodUfIbge(self.uf),
                ano=year,
                CNPJ=cnpj,
                mod=Tmod(mod),
                serie=serie_str,
                nNFIni=num_ini_str,
                nNFFin=num_fin_str,
                xJust=justificativa,
            ),
        )

    ######################################
    # Misc
    ######################################

    def _aguarda_tempo_medio(self, proc_recibo: Optional[RetEnviNfe]):
        """Aguarda um tempo baseado no tMed retornado pela SEFAZ."""
        if self.wrap_response:
            proc_recibo = proc_recibo.resposta
        if (
            proc_recibo
            and hasattr(proc_recibo, "infRec")
            and proc_recibo.infRec
            and hasattr(proc_recibo.infRec, "tMed")
            and proc_recibo.infRec.tMed
        ):
            try:
                tempo_medio = float(proc_recibo.infRec.tMed)
                # Add a small buffer (e.g., 30% or min 1 second)
                tempo_espera = max(1.0, tempo_medio * 1.3)
                _logger.info(
                    f"Aguardando {tempo_espera:.2f} segundos (tMed={tempo_medio})..."
                )
                time.sleep(tempo_espera)
            except (ValueError, TypeError):
                _logger.warning(
                    f"Não foi possível converter tMed '{proc_recibo.infRec.tMed}' "
                    "para float. Aguardando 2 segundos por padrão."
                )
                time.sleep(2.0)
        else:
            _logger.warning(
                "Retorno do envio (RetEnviNfe) inválido ou sem tMed. "
                "Aguardando 2 segundos por padrão."
            )
            time.sleep(2.0)  # Default wait if tMed is missing
