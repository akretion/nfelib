# FILEPATH: nfelib/mdfe/client/v3_0/mdfe.py
# Copyright (C) 2019  Luis Felipe Mileo - KMEE
# Copyright (C) 2025  Raphaël Valyi - Akretion

import binascii
import logging
from datetime import datetime
from typing import Any, Optional

from brazil_fiscal_client.fiscal_client import FiscalClient, Tamb, TcodUfIbge
from lxml import etree

# --- Content Bindings ---
from nfelib.mdfe.bindings.v3_0.cons_mdfe_nao_enc_v3_00 import ConsMdfeNaoEnc
from nfelib.mdfe.bindings.v3_0.cons_sit_mdfe_v3_00 import ConsSitMdfe
from nfelib.mdfe.bindings.v3_0.cons_stat_serv_mdfe_v3_00 import ConsStatServMdfe
from nfelib.mdfe.bindings.v3_0.ev_canc_mdfe_v3_00 import (
    EvCancMdfe,
    EvCancMdfeDescEvento,
)
from nfelib.mdfe.bindings.v3_0.ev_enc_mdfe_v3_00 import EvEncMdfe, EvEncMdfeDescEvento
from nfelib.mdfe.bindings.v3_0.evento_mdfe_v3_00 import EventoMdfe
from nfelib.mdfe.bindings.v3_0.mdfe_tipos_basico_v3_00 import Tmdfe
from nfelib.mdfe.bindings.v3_0.ret_cons_mdfe_nao_enc_v3_00 import RetConsMdfeNaoEnc
from nfelib.mdfe.bindings.v3_0.ret_cons_sit_mdfe_v3_00 import RetConsSitMdfe
from nfelib.mdfe.bindings.v3_0.ret_cons_stat_serv_mdfe_v3_00 import (
    RetConsStatServMdfe,
)
from nfelib.mdfe.bindings.v3_0.ret_envi_mdfe_v3_00 import RetEnviMdfe
from nfelib.mdfe.bindings.v3_0.ret_evento_mdfe_v3_00 import RetEventoMdfe

# --- Server Definitions ---
from nfelib.mdfe.client.v3_0.servers import Endpoint
from nfelib.mdfe.client.v3_0.servers import servers as SERVERS_MDFE

# --- SOAP Bindings ---
from nfelib.mdfe.soap.v3_0.mdfeconsnaoenc import MdfeConsNaoEncSoap12MdfeConsNaoEnc
from nfelib.mdfe.soap.v3_0.mdfeconsulta import MdfeConsultaSoap12MdfeConsultaMdf
from nfelib.mdfe.soap.v3_0.mdferecepcaoevento import (
    MdfeRecepcaoEventoSoap12MdfeRecepcaoEvento,
)
from nfelib.mdfe.soap.v3_0.mdferecepcaosinc import MdfeRecepcaoSincSoap12MdfeRecepcao
from nfelib.mdfe.soap.v3_0.mdfestatusservico import (
    MdfeStatusServicoSoap12MdfeStatusServicoMdf,
    MdfeCabecMsg,
)

_logger = logging.getLogger(__name__)


# TODO The event methods in MdfeClient should follow the same high-level pattern 
# proposed for NfeClient: accept data primitives (chave, protocolo, etc.) and 
# handle the creation and signing of the detEvento internally.

class MdfeClient(FiscalClient):
    """A façade for the MDFe v3.00 SOAP webservices."""

    def __init__(self, **kwargs: Any):
        self.mod = kwargs.pop("mod", "58")
        self.soap12_envelope = True
        super().__init__(service="mdfe", versao="3.00", **kwargs)

    def _get_location(self, endpoint_type: Endpoint) -> str:
        """Constructs the full HTTPS URL for the specified service."""
        server_key = "SVRS"
        server_data = SERVERS_MDFE[server_key]

        server_host = (
            server_data["prod_server"]
            if self.ambiente == Tamb.PROD.value
            else server_data["dev_server"]
        )
        path = server_data["endpoints"][endpoint_type]
        location = f"https://{server_host}{path}"
        _logger.debug(f"Determined location for {endpoint_type.name}: {location}")
        return location

    def send(
        self,
        action_class: type,
        obj: Any,
        placeholder_exp: Optional[str] = None,
        placeholder_content: Optional[str] = None,
        **kwargs: Any,
    ) -> Any:
        """Builds and sends a request, adding the mdfeCabecMsg header if required."""
        action_to_endpoint_map = {
            MdfeStatusServicoSoap12MdfeStatusServicoMdf: Endpoint.MDFESTATUSSERVICO,
            MdfeConsultaSoap12MdfeConsultaMdf: Endpoint.MDFECONSULTA,
            MdfeRecepcaoSincSoap12MdfeRecepcao: Endpoint.MDFERECEPCAOSINC,
            MdfeConsNaoEncSoap12MdfeConsNaoEnc: Endpoint.MDFECONSNAOENC,
            MdfeRecepcaoEventoSoap12MdfeRecepcaoEvento: Endpoint.MDFERECEPCAOEVENTO,
        }
        endpoint_type = action_to_endpoint_map[action_class]
        location = self._get_location(endpoint_type)

        # Conditionally create the header
        header_obj = None
        if hasattr(action_class.input, "Header"):
            header_obj = action_class.input.Header(
                    mdfeCabecMsg=MdfeCabecMsg(
                    cUF=str(self.uf), versaoDados=self.versao
                )
            )

        wrapped_obj = {
            "Body": {"mdfeDadosMsg": {"content": [obj]}},
        }
        if header_obj:
            wrapped_obj["Header"] = header_obj

        response = super().send(
            action_class=action_class,
            location=location,
            wrapped_obj=wrapped_obj,
            placeholder_exp=placeholder_exp,
            placeholder_content=placeholder_content,
            **kwargs,
        )

        if not self.wrap_response:
            return response.body.content[0].content[0]

        response.resposta = response.resposta.body.content[0].content[0]
        return response

    def status_servico(self) -> RetConsStatServMdfe:
        """Consulta o status do serviço MDF-e."""
        payload = ConsStatServMdfe(tpAmb=Tamb(self.ambiente), versao=self.versao)
        return self.send(MdfeStatusServicoSoap12MdfeStatusServicoMdf, payload)

    def consulta_documento(
        self, chave: str
    ) -> RetConsSitMdfe:  # NOTE consulta_documento in erpbrasil
        """Consulta a situação de um MDF-e pela chave de acesso."""
        payload = ConsSitMdfe(
            tpAmb=Tamb(self.ambiente), chMDFe=chave, versao=self.versao
        )
        return self.send(MdfeConsultaSoap12MdfeConsultaMdf, payload)

    def consulta_nao_encerrados(
        self, cnpj_cpf: str
    ) -> RetConsMdfeNaoEnc:  # NOTE consulta_nao_encerrados in erpbrasil
        """Consulta MDF-es não encerrados para um CNPJ/CPF."""
        payload = ConsMdfeNaoEnc(tpAmb=Tamb(self.ambiente), versao=self.versao)
        if len(cnpj_cpf) == 14:
            payload.CNPJ = cnpj_cpf
        else:
            payload.CPF = cnpj_cpf
        return self.send(MdfeConsNaoEncSoap12MdfeConsNaoEnc, payload)

    def envia_documento(
        self, mdfe_obj: Tmdfe
    ) -> RetEnviMdfe:  # NOTE envia_documento in erpbrasil
        """Envia um lote com um único MDF-e de forma síncrona."""
        signed_xml = mdfe_obj.to_xml(
            pkcs12_data=self.pkcs12_data,
            pkcs12_password=self.pkcs12_password,
            doc_id=mdfe_obj.infMDFe.Id,
        )
        # The webservice expects the signed MDFe directly inside mdfeDadosMsg
        # This service specifically does not use the mdfeCabecMsg header
        return self.send(
            MdfeRecepcaoSincSoap12MdfeRecepcao, etree.fromstring(signed_xml)
        )

    def envia_evento(  # NOTE envia_evento in erpbrasil
        self,
        chave: str,
        tpEvento: str,
        nSeqEvento: str,
        detEvento: Any,
        cnpj_cpf: str,
        dhEvento: Optional[str] = None,
    ) -> RetEventoMdfe:
        """Envia um evento genérico para um MDF-e."""
        inf_evento = EventoMdfe.InfEvento(
            Id=f"ID{tpEvento}{chave}{nSeqEvento.zfill(3)}",
            cOrgao=TcodUfIbge(self.uf),
            tpAmb=Tamb(self.ambiente),
            chMDFe=chave,
            dhEvento=dhEvento or self._timestamp(),
            tpEvento=tpEvento,
            nSeqEvento=nSeqEvento,
            detEvento=EventoMdfe.InfEvento.DetEvento(
                any_element=detEvento, versaoEvento=self.versao
            ),
        )
        if len(cnpj_cpf) == 14:
            inf_evento.CNPJ = cnpj_cpf
        else:
            inf_evento.CPF = cnpj_cpf

        evento = EventoMdfe(versao=self.versao, infEvento=inf_evento)
        signed_xml = evento.to_xml(
            self.pkcs12_data, self.pkcs12_password, evento.infEvento.Id
        )

        return self.send(
            MdfeRecepcaoEventoSoap12MdfeRecepcaoEvento, etree.fromstring(signed_xml)
        )

    def cancela_documento(  # NOTE cancela_documento in erpbrasil
        self, chave: str, protocolo_autorizacao: str, justificativa: str, cnpj_cpf: str
    ) -> RetEventoMdfe:
        """Cancela um MDF-e autorizado."""
        det_evento = EvCancMdfe(
            descEvento=EvCancMdfeDescEvento.CANCELAMENTO,
            nProt=protocolo_autorizacao,
            xJust=justificativa,
        )
        return self.envia_evento(
            chave=chave,
            tpEvento="110111",
            nSeqEvento="1",
            detEvento=det_evento,
            cnpj_cpf=cnpj_cpf,
        )

    def encerra_documento(  # NOTE encerra_documento in erpbrasil
        self,
        chave: str,
        protocolo_autorizacao: str,
        estado_ibge: str,
        municipio_ibge: str,
        cnpj_cpf: str,
    ) -> RetEventoMdfe:
        """Encerra um MDF-e."""
        det_evento = EvEncMdfe(
            descEvento=EvEncMdfeDescEvento.ENCERRAMENTO,
            dtEnc=datetime.now().strftime("%Y-%m-%d"),
            nProt=protocolo_autorizacao,
            cUF=TcodUfIbge(estado_ibge),
            cMun=municipio_ibge,
        )
        return self.envia_evento(
            chave=chave,
            tpEvento="110112",
            nSeqEvento="1",
            detEvento=det_evento,
            cnpj_cpf=cnpj_cpf,
        )

    def montar_qrcode(
        self, chave: str, signed_xml: str
    ) -> str:  # NOTE monta_qrcode in erpbrasil
        """Monta a URL do QR Code para o DAMDFE."""
        server_data = SERVERS_MDFE["SVRS"]
        host = (
            server_data["prod_server"]
            if self.ambiente == Tamb.PROD.value
            else server_data["dev_server"]
        )
        path = server_data["endpoints"][Endpoint.QRCODE]

        base_url = f"https://{host}{path}"

        params = f"?chMDFe={chave}&tpAmb={self.ambiente}"

        xml_tree = etree.fromstring(signed_xml.encode("utf-8"))
        tpEmis = xml_tree.find(".//{http://www.portalfiscal.inf.br/mdfe}tpEmis").text

        if tpEmis != "1":
            digest_value_b64_element = xml_tree.find(
                ".//{http://www.w3.org/2000/09/xmldsig#}DigestValue"
            )
            if digest_value_b64_element is not None:
                digest_value_b64 = digest_value_b64_element.text
                sign = binascii.hexlify(digest_value_b64.encode()).decode()
                params += f"&sign={sign}"

        return base_url + params
