import base64
import gzip
import logging
from datetime import datetime
from typing import Any, Optional

from brazil_fiscal_client.fiscal_client import FiscalClient, Tamb, TcodUfIbge

from nfelib.mdfe.bindings.v3_0 import (
    ConsStatServMdfe,
    EvCancMdfe,
    EvEncMdfe,
    EventoMdfe,
    RetConsSitMdfe,
    RetEventoMdfe,
    RetMdfe,
)

# --- Content Bindings ---
# Import necessary MDFe content bindings (adjust based on actual methods implemented)
from nfelib.mdfe.bindings.v3_0.cons_mdfe_nao_enc_v3_00 import ConsMdfeNaoEnc

# Import MDFe Base Types needed for request construction
# from nfelib.mdfe.bindings.v3_0.cons_stat_serv_tipos_basico_v3_00 import TconsStatServ
from nfelib.mdfe.bindings.v3_0.cons_sit_mdfe_v3_00 import ConsSitMdfe
from nfelib.mdfe.bindings.v3_0.cons_stat_serv_mdfe_v3_00 import ConsStatServMdfe
from nfelib.mdfe.bindings.v3_0.dist_mdfe_v3_00 import DistMdfe
from nfelib.mdfe.bindings.v3_0.envi_mdfe_v3_00 import EnviMdfe
from nfelib.mdfe.bindings.v3_0.ev_canc_mdfe_v3_00 import EvCancMdfe
from nfelib.mdfe.bindings.v3_0.ev_enc_mdfe_v3_00 import EvEncMdfe

# --- Event Bindings (Example for Cancel/Encerramento) ---
# Adapt imports based on which events you need
from nfelib.mdfe.bindings.v3_0.evento_mdfe_tipos_basico_v3_00 import (
    #    TenvEvento as TenvEventoMdfe, # Renamed for clarity
    #    TretEvento as TretEventoMdfe,
    Tevento as TeventoMdfe,
)
from nfelib.mdfe.bindings.v3_0.mdfe_tipos_basico_v3_00 import TenviMdfe, Tmdfe
from nfelib.mdfe.bindings.v3_0.mdfe_v3_00 import Mdfe
from nfelib.mdfe.bindings.v3_0.ret_cons_mdfe_nao_enc_v3_00 import RetConsMdfeNaoEnc
from nfelib.mdfe.bindings.v3_0.ret_cons_sit_mdfe_v3_00 import RetConsSitMdfe
from nfelib.mdfe.bindings.v3_0.ret_cons_stat_serv_mdfe_v3_00 import RetConsStatServMdfe
from nfelib.mdfe.bindings.v3_0.ret_dist_mdfe_v3_00 import RetDistMdfe
from nfelib.mdfe.bindings.v3_0.ret_envi_mdfe_v3_00 import RetEnviMdfe
from nfelib.mdfe.bindings.v3_0.ret_evento_mdfe_v3_00 import RetEventoMdfe
from nfelib.mdfe.bindings.v3_0.ret_mdfe_v3_00 import RetMdfe
from nfelib.mdfe.client.v3_0.servers import Endpoint

# --- Server Definitions ---
# Import Endpoint Enum and the servers dictionary directly
from nfelib.mdfe.client.v3_0.servers import servers as SERVERS_MDFE

# Add others as needed (ConsultaNaoEnc, DistDFe)
from nfelib.mdfe.soap.v3_0.mdfeconsnaoenc import (
    MdfeConsNaoEncSoap12MdfeConsNaoEnc,
)
from nfelib.mdfe.soap.v3_0.mdfeconsulta import (
    MdfeConsultaSoap12MdfeConsultaMdf,
)
from nfelib.mdfe.soap.v3_0.mdfedistribuicaodfe import (
    MdfeDistribuicaoDfeSoap12MdfeDistDfeInteresse,
)
from nfelib.mdfe.soap.v3_0.mdferecepcaoevento import (
    MdfeRecepcaoEventoSoap12MdfeRecepcaoEvento,
)
from nfelib.mdfe.soap.v3_0.mdferecepcaosinc import (
    MdfeRecepcaoSincSoap12MdfeRecepcao,
)

# --- SOAP Bindings ---
# Import the MDFe SOAP binding classes
from nfelib.mdfe.soap.v3_0.mdfestatusservico import (
    MdfeStatusServicoSoap12MdfeStatusServicoMdf,
)

# --- Logging ---
_logger = logging.getLogger(__name__)

# --- Constants ---
MDFE_VERSION = "3.00"
# Define MDFe event types if needed
TIPO_EVENTO_CANCEL_MDFE = "110111"
TIPO_EVENTO_ENC_MDFE = "110112"
# ... other event types ...


class MdfeClient(FiscalClient):
    """A façade for the MDFe v3.00 SOAP webservices."""

    def __init__(self, **kwargs: Any):
        # MDFe uses SVRS, so UF is primarily for the mdfeCabecMsg header
        uf_code = kwargs.get("uf")
        if not isinstance(uf_code, str) or len(uf_code) != 2 or not uf_code.isdigit():
            _logger.warning(
                "MdfeClient initialized with potentially invalid "
                "UF code: {uf_code}. Expected 2-digit string for header."
            )
            # Should still work as server is fixed, but header needs valid UF

        super().__init__(
            service="mdfe",  # Service name for ns_map in prepare_payload
            versao=MDFE_VERSION,
            **kwargs,
        )
        # MDFe always uses SVRS server key
        self.server_key = "SVRS"

    def _get_location(self, endpoint_type: Endpoint) -> str:
        """Constructs the full HTTPS URL for the specified service."""
        try:
            server_data = SERVERS_MDFE[self.server_key]
        except KeyError:
            # Should not happen if servers.py is correct
            raise ValueError(
                "MDFe server configuration not foundfor key: {self.server_key}"
            )

        if self.ambiente == Tamb.PROD.value:
            server_host = server_data["prod_server"]
        else:
            server_host = server_data["dev_server"]

        if endpoint_type not in server_data["endpoints"]:
            raise ValueError(
                f"Endpoint {endpoint_type.name} not configured "
                "for server key: {self.server_key}"
            )

        path = server_data["endpoints"][endpoint_type]
        location = f"https://{server_host}{path}"
        _logger.debug(
            f"Determined location for {endpoint_type.name} (Amb: {self.ambiente}, "
            "ServerKey: {self.server_key}): {location}"
        )
        return location

    def _get_header(self) -> Optional[dict]:
        """Constructs the mdfeCabecMsg header."""
        # Most MDFe operations require this header
        header_obj = {
            # Assuming a common structure, adjust namespace if needed
            "mdfeCabecMsg": {"cUF": self.uf, "versaoDados": self.versao}
        }
        # Some WSDLs might have slightly different header element names or namespaces
        # Example: StatusServico uses 'mdfeCabecMsg' in the correct namespace
        #          Consulta uses 'mdfeCabecMsg'
        #          RecepcaoEvento uses 'mdfeCabecMsg'
        # Check each SOAP binding's *Input class for the exact header structure
        # if issues arise
        _logger.debug(f"Generated MDFe Header: {header_obj}")
        return header_obj

    def send(
        self,
        action_class: type,
        payload_obj: Any,
        requires_header: bool = True,
        payload_is_base64: bool = False,  # Flag for MDFeRecepcaoSinc
        placeholder_exp: Optional[
            str
        ] = None,  # Not typically used with MDFe wrapper style?
        placeholder_content: Optional[str] = None,
        **kwargs: Any,
    ) -> Any:
        """Build and send an MDFe request. Handles header and base64 encoding."""
        try:
            action_to_endpoint_map: dict[type, Endpoint] = {
                MdfeStatusServicoSoap12MdfeStatusServicoMdf: Endpoint.MDFESTATUSSERVICO,
                MdfeConsultaSoap12MdfeConsultaMdf: Endpoint.MDFECONSULTA,
                MdfeRecepcaoSincSoap12MdfeRecepcao: Endpoint.MDFERECEPCAOSINC,
                MdfeRecepcaoEventoSoap12MdfeRecepcaoEvento: Endpoint.MDFERECEPCAOEVENTO,
                MdfeConsNaoEncSoap12MdfeConsNaoEnc: Endpoint.MDFECONSNAOENC,
                MdfeDistribuicaoDfeSoap12MdfeDistDfeInteresse: (
                    Endpoint.MDFEDISTRIBUICAODFE,
                ),
            }
            endpoint_type = action_to_endpoint_map[action_class]
            location = self._get_location(endpoint_type)
        except KeyError:
            raise ValueError(
                "Could not determine Endpoint for action_class: {action_class.__name__}"
            )

        # Prepare the body content (mdfeDadosMsg wrapper)
        if payload_is_base64:
            # For RecepcaoSinc, the payload_obj is already the base64 string
            if not isinstance(payload_obj, str):
                raise TypeError(
                    "payload_obj must be a base64 string for MDFeRecepcaoSinc"
                )
            body_content = {"mdfeDadosMsg": {"value": payload_obj}}
        else:
            # Standard case: wrap the content object
            body_content = {"mdfeDadosMsg": {"content": [payload_obj]}}

        # Construct the full SOAP object including header if needed
        wrapped_obj = {"Body": body_content}
        if requires_header:
            wrapped_obj["Header"] = self._get_header()

        response = super().send(
            action_class,
            location,
            wrapped_obj,
            placeholder_exp=placeholder_exp,
            placeholder_content=placeholder_content,
            **kwargs,
        )
        return response.body.mdfeStatusServicoMDFResult.content[0]

    ######################################
    # Webservices
    ######################################

    def status_servico(self) -> Optional[RetConsStatServMdfe]:
        """Consulta o status do serviço MDFe."""
        # MDFe Status request payload (TConsStatServ) doesn't need cUF inside
        payload = ConsStatServMdfe(
            tpAmb=Tamb(self.ambiente),
            # xServ="STATUS" is implicitly set in TconsStatServ
            versao=self.versao,
        )
        return self.send(
            MdfeStatusServicoSoap12MdfeStatusServicoMdf, payload, requires_header=True
        )

    def consulta_mdfe(self, chave: str) -> Optional[RetConsSitMdfe]:
        """Consulta a situação de um MDF-e pela chave de acesso."""
        if not (isinstance(chave, str) and len(chave) == 44 and chave.isdigit()):
            raise ValueError(f"Chave de acesso do MDFe inválida: {chave}")

        payload = ConsSitMdfe(
            tpAmb=Tamb(self.ambiente),
            # xServ="CONSULTAR" is implicitly set in TconsSitMdfe
            chMDFe=chave,
            versao=self.versao,
        )
        return self.send(
            MdfeConsultaSoap12MdfeConsultaMdf, payload, requires_header=True
        )

    def envia_mdfe_sincrono(self, signed_mdfe_xml: str) -> Optional[RetMdfe]:
        """Envia um MDF-e assinado para autorização síncrona."""
        if not signed_mdfe_xml:
            raise ValueError("XML do MDF-e assinado não pode estar vazio.")

        # RecepcaoSinc expects the XML directly in the mdfeDadosMsg value, not wrapped
        # in content[]
        # It also seems to NOT require the mdfeCabecMsg header based on WSDL/Legacy

        # Compress with Gzip and encode Base64
        try:
            gzipped_xml = gzip.compress(signed_mdfe_xml.encode("utf-8"))
            base64_gzipped_xml = base64.b64encode(gzipped_xml).decode("utf-8")
        except Exception as e:
            _logger.error(f"Erro ao comprimir/codificar XML do MDF-e: {e}")
            raise

        # Pass the base64 string directly as the payload_obj
        return self.send(
            MdfeRecepcaoSincSoap12MdfeRecepcao,
            payload_obj=base64_gzipped_xml,
            requires_header=False,  # Sincrono usually doesn't have the header
            payload_is_base64=True,  # Signal to send to handle it differently
        )

    def envia_evento(
        self, evento, tipo, chave, sequencia="001", data_hora: str = False
    ):
        EventoMdfe(
            versao="3.00",
            infEvento=EventoMdfe.InfEvento(
                Id="ID" + tipo + chave + sequencia.zfill(2),
                cOrgao=self.uf,
                tpAmb=self.ambiente,
                CNPJ=chave[6:20],
                chMDFe=chave,
                dhEvento=data_hora or self._hora_agora(),
                tpEvento=tipo,
                nSeqEvento=sequencia,
                detEvento=EventoMdfe.InfEvento.DetEvento(
                    versaoEvento="3.00", any_element=evento
                ),
            ),
        )
        # FIXME:
        return self.send(
            MdfeRecepcaoEventoSoap12MdfeRecepcaoEvento,
            payload_obj=payload_for_wrapping,  # This needs to be wrapped
        )

    # --- Need to Refine FiscalClient.send for pre-signed ---
    # Let's add a flag to FiscalClient.send to bypass prepare_payload if content is already XML

    def consulta_nao_encerrados(
        self, cnpj: Optional[str] = None, cpf: Optional[str] = None
    ) -> Optional[RetConsMdfeNaoEnc]:
        """Consulta MDF-es não encerrados para um CNPJ/CPF."""
        if not cnpj and not cpf:
            raise ValueError("É necessário fornecer CNPJ ou CPF para a consulta.")
        if cnpj and cpf:
            raise ValueError("Forneça apenas CNPJ ou CPF, não ambos.")
        if cnpj and not (isinstance(cnpj, str) and len(cnpj) == 14 and cnpj.isdigit()):
            raise ValueError(f"CNPJ inválido: {cnpj}")
        if cpf and not (isinstance(cpf, str) and len(cpf) == 11 and cpf.isdigit()):
            raise ValueError(f"CPF inválido: {cpf}")

        payload = ConsMdfeNaoEnc(
            tpAmb=Tamb(self.ambiente),
            # xServ="CONSULTAR NÃO ENCERRADOS" is implicitly set
            CNPJ=cnpj,
            CPF=cpf,
            versao=self.versao,
        )
        return self.send(
            MdfeConsNaoEncSoap12MdfeConsNaoEnc, payload, requires_header=True
        )

    # --- Add other MDFe specific methods like consulta_recibo, distribuicao_dfe ---

    ######################################
    # Binding Façades (Input Assembly) - Adapt from Legacy/NFe if needed
    ######################################

    def FIXMEcancela_mdfe(
        self,
        chave: str,
        protocolo_autorizacao: str,
        justificativa: str,
        cnpj_cpf_autor: Optional[str] = None,  # CNPJ/CPF of the event author
        data_hora_evento: Optional[str] = None,
        sequencia: str = "1",
    ) -> TeventoMdfe:
        """Monta o objeto TeventoMdfe para um evento de cancelamento."""
        # ... (Input Validations like NFe cancela_documento) ...
        if not (15 <= len(justificativa) <= 255):
            raise ValueError("Justificativa deve ter entre 15 e 255 caracteres.")

        # Determine CNPJ or CPF of the event author
        doc_autor = self._get_doc_autor(cnpj_cpf_autor, chave)

        # Detail specific to cancellation event
        det_evento_canc = EvCancMdfe(
            descEvento="Cancelamento",  # Use Enum if defined
            nProt=protocolo_autorizacao,
            xJust=justificativa,
        )

        inf_evento = TeventoMdfe.InfEvento(
            Id="ID" + TIPO_EVENTO_CANCEL_MDFE + chave + sequencia.zfill(2),
            cOrgao=TcodUfIbge(self.uf),  # Or specific organ code if needed
            tpAmb=Tamb(self.ambiente),
            CNPJ=doc_autor["CNPJ"],
            CPF=doc_autor["CPF"],
            chMDFe=chave,  # Use chMDFe field name
            dhEvento=data_hora_evento or self._timestamp(),
            tpEvento=TIPO_EVENTO_CANCEL_MDFE,
            nSeqEvento=sequencia,
            detEvento=TeventoMdfe.InfEvento.DetEvento(
                versaoEvento=self.versao,  # Version of the detail schema
                any_element=det_evento_canc,  # Embed the specific event detail
            ),
        )
        return TeventoMdfe(versao=self.versao, infEvento=inf_evento)

    def encerra_mdfe(
        self,
        chave: str,
        protocolo_autorizacao: str,
        dt_enc: str,  # Format YYYY-MM-DD
        cod_uf_enc: str,  # IBGE code for UF of encerrramento
        cod_mun_enc: str,  # IBGE code for Mun of encerrramento
        cnpj_cpf_autor: Optional[str] = None,
        data_hora_evento: Optional[str] = None,
        sequencia: str = "1",
    ) -> TeventoMdfe:
        """Monta o objeto TeventoMdfe para um evento de encerramento."""
        # ... (Input Validations) ...
        try:
            datetime.strptime(dt_enc, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Formato inválido para dtEnc. Use AAAA-MM-DD.")
        # Validate cod_uf_enc, cod_mun_enc formats/values...

        doc_autor = self._get_doc_autor(cnpj_cpf_autor, chave)

        det_evento_enc = EvEncMdfe(
            descEvento="Encerramento",  # Use Enum if defined
            nProt=protocolo_autorizacao,
            dtEnc=dt_enc,
            cUF=TcodUfIbge(cod_uf_enc),  # Make sure TcodUfIbge includes all UFs
            cMun=cod_mun_enc,
        )

        inf_evento = TeventoMdfe.InfEvento(
            Id="ID" + TIPO_EVENTO_ENC_MDFE + chave + sequencia.zfill(2),
            cOrgao=TcodUfIbge(
                self.uf
            ),  # Or UF of encerrramento? Check docs. Usually UF emitting event.
            tpAmb=Tamb(self.ambiente),
            CNPJ=doc_autor["CNPJ"],
            CPF=doc_autor["CPF"],
            chMDFe=chave,
            dhEvento=data_hora_evento or self._timestamp(),
            tpEvento=TIPO_EVENTO_ENC_MDFE,
            nSeqEvento=sequencia,
            detEvento=TeventoMdfe.InfEvento.DetEvento(
                versaoEvento=self.versao, any_element=det_evento_enc
            ),
        )
        return TeventoMdfe(versao=self.versao, infEvento=inf_evento)

    # --- Add other façade methods (inclusao condutor, inclusao DFe, etc.) ---

    # --- Helper for Author CNPJ/CPF ---
    def _get_doc_autor(
        self, cnpj_cpf_autor: Optional[str], chave: str
    ) -> dict[str, Optional[str]]:
        """Determines the CNPJ/CPF of the event author."""
        if cnpj_cpf_autor:
            if len(cnpj_cpf_autor) == 14 and cnpj_cpf_autor.isdigit():
                return {"CNPJ": cnpj_cpf_autor, "CPF": None}
            if len(cnpj_cpf_autor) == 11 and cnpj_cpf_autor.isdigit():
                return {"CNPJ": None, "CPF": cnpj_cpf_autor}
            raise ValueError("CNPJ/CPF do autor do evento inválido.")
        # Fallback to extracting from chave (assuming CNPJ)
        _logger.warning(
            "CNPJ/CPF do autor não fornecido, extraindo da chave (assumindo CNPJ)."
        )
        return {"CNPJ": chave[6:20], "CPF": None}

    # --- Overwrite timestamp if MDFe format differs (unlikely) ---
    # @classmethod
    # def _timestamp(cls):
    #     return super()._timestamp() # Or specific MDFe format

    # --- Need _aguarda_tempo_medio equivalent? MDFe RecepcaoSinc doesn't return tMed ---
    # def _aguarda_tempo_medio(self, proc_recibo: Optional[RetEnviMdfe]):
    #     # MDFe sync response (RetMdfe) doesn't have tMed. Async (RetConsReciMDFe) does.
    #     # This method might only be relevant if using async submission.
    #     pass
