# Copyright (C) 2024  Raphaël Valyi - Akretion <raphael.valyi@akretion.com.br>

import time
from datetime import date, datetime
from os import environ
from typing import Any, Optional, Type

from brazil_fiscal_client.fiscal_client import FiscalClient, Tamb, TcodUfIbge

from nfelib.nfe.bindings.v4_0.cons_reci_nfe_v4_00 import ConsReciNfe
from nfelib.nfe.bindings.v4_0.cons_sit_nfe_v4_00 import ConsSitNfe
from nfelib.nfe.bindings.v4_0.cons_stat_serv_v4_00 import ConsStatServ
from nfelib.nfe.bindings.v4_0.envi_nfe_v4_00 import EnviNfe
from nfelib.nfe.bindings.v4_0.inut_nfe_v4_00 import InutNfe
from nfelib.nfe.bindings.v4_0.leiaute_cons_sit_nfe_v4_00 import TconsSitNfeXServ
from nfelib.nfe.bindings.v4_0.leiaute_cons_stat_serv_v4_00 import TconsStatServXServ
from nfelib.nfe.bindings.v4_0.leiaute_inut_nfe_v4_00 import TinutNfe
from nfelib.nfe.bindings.v4_0.leiaute_nfe_v4_00 import Tnfe
from nfelib.nfe.bindings.v4_0.ret_cons_reci_nfe_v4_00 import RetConsReciNfe
from nfelib.nfe.bindings.v4_0.ret_cons_sit_nfe_v4_00 import RetConsSitNfe
from nfelib.nfe.bindings.v4_0.ret_cons_stat_serv_v4_00 import RetConsStatServ
from nfelib.nfe.bindings.v4_0.ret_envi_nfe_v4_00 import RetEnviNfe
from nfelib.nfe.bindings.v4_0.ret_inut_nfe_v4_00 import RetInutNfe
from nfelib.nfe.soap.v4_0.nfeautorizacao4 import (
    NfeAutorizacao4SoapNfeAutorizacaoLote,
)
from nfelib.nfe.soap.v4_0.nfeconsulta4 import (
    NfeConsultaProtocolo4SoapNfeConsultaNf,
)

# TODO distribuição:
from nfelib.nfe.soap.v4_0.nfedistribuicaodfe import (
    NfeDistribuicaoDfeSoapNfeDistDfeInteresse,
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
from nfelib.nfe_evento_cancel.bindings.v1_0.evento_canc_nfe_v1_00 import (
    Tevento as TeventoCancel,
)
from nfelib.nfe_evento_cancel.bindings.v1_0.leiaute_evento_canc_nfe_v1_00 import (
    TenvEvento,
    TretEnvEvento,
)
from nfelib.nfe_evento_cce.bindings.v1_0.leiaute_cce_v1_00 import Tevento as TeventoCCe

from nfelib.nfe.client.v4_0.servers import servers as SERVERS_NFE


UF_TO_SERVER = {  # NOTE this is fixed compared to erpbrasil.edoc
    "11": "SVRS",
    "12": "SVRS",
    "13": "AM",
    "14": "SVRS",
    "15": "BA",
    "16": "SVRS",
    "17": "SVRS",
    "21": "SVRS",
    "22": "GO",
    "23": "SVAN",
    "24": "SP",
    "25": "MT",
    "26": "MS",
    "27": "MG",
    "28": "PE",
    "29": "SVRS",
    "31": "SVRS",
    "32": "SVRS",
    "33": "SVRS",
    "35": "PR",
    "41": "SVRS",
    "42": "SVRS",
    "43": "SVRS",
    "50": "SVRS",
    "51": "SVRS",
    "52": "RS",
    "53": "SVRS",
    "AN": "AN",
}


class NfeClient(FiscalClient):
    """A façade for the NFe SOAP webserices."""

    def __init__(self, **kwargs: Any):
        super().__init__(
            service="nfe",
            versao="4.00",
            # server=self._get_server("nfe", kwargs.get("uf")),
            **kwargs,
        )

    def _get_location(self, action_class: Type) -> str:
        action_class_to_action = {
            NfeInutilizacao4SoapNfeInutilizacaoNf: "NfeInutilizacao",
            NfeConsultaProtocolo4SoapNfeConsultaNf: "NfeConsultaProtocolo",
            NfeStatusServico4SoapNfeStatusServicoNf: "NfeStatusServico",
            # NfeConsultaCadastro: "NfeConsultaCadastro",  # TODO
            NfeRecepcaoEvento4SoapNfeRecepcaoEvento: "RecepcaoEvento",
            NfeAutorizacao4SoapNfeAutorizacaoLote: "NFeAutorizacao",
            NfeRetAutorizacao4SoapNfeRetAutorizacaoLote: "NFeRetAutorizacao",
            NfeDistribuicaoDfeSoapNfeDistDfeInteresse: "NFeDistribuicaoDFe",
        }
        action_key = action_class_to_action[action_class]
        # FIXME if action_key == "NfeConsultaCadastro" and state: AC, ES, RN, PB, SC
        # then use SVRS server as per the doc at the top of
        # https://www.nfe.fazenda.gov.br/portal/webServices.aspx?tipoConteudo=OUC/YVNWZfo=
        # TODO Contingência
        server_key = UF_TO_SERVER[self.uf]
        server_data = SERVERS_NFE[server_key]
        if self.ambiente == Tamb.PROD:
            server = server_data["prod_server"]
        else:
            server = server_data["dev_server"]
        path = server_data[action_key]
        return "https://" + server + path

    def send(
        self,
        action_class: Type,
        obj: Any,
        placeholder_exp: Optional[str] = None,
        placeholder_content: Optional[str] = None,
        **kwargs: Any,
    ) -> Any:
        """Build and send a request for the input object.

        Args:
            action_class: Type generated with xsdata for the SOAP wsdl
            obj: The request model instance or a pure dictionary
            placeholder_content: a string content to be injected in the
            payload. Used for signed content to avoid signature issues.
            placeholder_exp: placeholder where to inject placeholder_content
            the response into the right class. Usually useless if the
            proper return type has been imported already.
            kwargs: keyword arguments

        Returns:
            The response model instance.
        """
        location = self._get_location(action_class)
        wrapped_obj = {"Body": {"nfeDadosMsg": {"content": [obj]}}}
        response = super().send(
            action_class,
            location,
            wrapped_obj,
            placeholder_exp=placeholder_exp,
            placeholder_content=placeholder_content,
            **kwargs,
        )
        return response.body.nfeResultMsg.content[0]

    ######################################
    # Webservices
    ######################################

    # OK 100%
    def status_servico(self) -> RetConsStatServ:
        return self.send(
            NfeStatusServico4SoapNfeStatusServicoNf,
            ConsStatServ(
                tpAmb=self.ambiente,
                cUF=self.uf,
                xServ=TconsStatServXServ(value="STATUS"),
                versao=self.versao,
            ),
        )

    # OK 100%
    def consulta_documento(self, chave: str) -> RetConsSitNfe:
        return self.send(
            NfeConsultaProtocolo4SoapNfeConsultaNf,
            ConsSitNfe(
                versao=self.versao,
                tpAmb=self.ambiente,
                xServ=TconsSitNfeXServ(value="CONSULTAR"),
                chNFe=chave,
            ),
        )

    # NOTE: I changed the signature from erpbrasil.edoc to support a list of NFe's
    # OK 100%
    # TODO call autoriza_documento that returns the protocol without waiting
    def envia_documento(
        self, lista_nfes: list, id_lote=None, ind_sinc="0"
    ) -> RetEnviNfe:
        # TODO see if NFe's should be signed
        # for nfe in nfe_list...
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
            placeholder_content="".join(lista_nfes),
        )

    # NOTE erpbrasil.edoc coupling with TinutNfe seems bad, better take signed xml?
    # in wmixvideo inutilizaNota(final int anoInutilizacaoNumeracao, final String cnpjEmitente, final String serie, final String numeroInicial, final String numeroFinal, final String justificativa, final DFModelo modelo)
    # and inutilizaNotaAssinada(final eventoAssinadoXml, modelo)
    def envia_inutilizacao(self, evento: InutNfe.InfInut) -> RetInutNfe:
        # NOTE: sure we don't take a signed xml input?
        signed_xml = evento.to_xml(
            pkcs12_data=self.pkcs12_data,
            pkcs12_password=self.pkcs12_password,
            doc_id=evento.infInut.Id,
        )
        return self.send(
            NfeInutilizacao4SoapNfeInutilizacaoNf,
            InutNfe(),
            #                versao=self.versao,
            #                infInut=InutNfe.InfInut(),  # placeholder for signed xml
            #                signature=None,
            #            ),
            placeholder_exp="<inutNFe/>",
            placeholder_content=signed_xml,
        )

    # OK 100%
    def consulta_recibo(
        self, numero: str = "", proc_envio: RetEnviNfe = None
    ) -> RetConsReciNfe:
        if proc_envio:
            numero = proc_envio.infRec.nRec

        if not numero:
            raise ValueError("Sem numero para consultar!")

        return self.send(
            NfeRetAutorizacao4SoapNfeRetAutorizacaoLote,
            ConsReciNfe(
                versao=self.versao,
                tpAmb=self.ambiente,
                nRec=numero,
            ),
        )

    # NOTE bad name from erpbrasil.edoc
    # in wmixvideo cancelaNota(chaveDeAcessoDaNota, protocoloDaNota, motivoCancelaamento)
    # and cancelaNotaAssinada(chave, eventoAssinadoXml)
    # ver tb cancelaNotaPorSubstituicao permitido para a NFCe
    def enviar_lote_evento(self, lista_eventos, numero_lote: str = "") -> TretEnvEvento:
        if not numero_lote:
            numero_lote = datetime.now().strftime("%Y%m%d%H%M%S")

        signed_events_xml = ""
        for inf_evento in lista_eventos:
            evento = TeventoCancel(  # seems bad to use specific event in generic method
                versao="1.00",
                infEvento=inf_evento,
            )
            signed_xml = evento.to_xml(
                pkcs12_data=self.pkcs12_data,
                pkcs12_password=self.pkcs12_password,
                doc_id=evento.infEvento.Id,
            )
            signed_events_xml += signed_xml  # TODO ensure this works!
        return self.send(
            NfeRecepcaoEvento4SoapNfeRecepcaoEvento,
            TenvEvento(
                versao="1.00",
                idLote=numero_lote,
                evento=[TeventoCancel()],  # placeholder
            ),
            placeholder_exp='<ns2:TEnvEvento versao="1.00"><evento/></ns2:TEnvEvento>',  # "<TEnvento/>",
            placeholder_content=signed_events_xml,
        )

    # TODO
    # consultaCadastro(final String cnpj, final DFUnidadeFederativa uf)
    # Realiza a consulta de cadastro de pessoa juridica com inscricao estadual

    ######################################
    # Binding façades
    ######################################

    # OK 100%
    def cancela_documento(
        self,
        chave: str,
        protocolo_autorizacao: str,
        justificativa: str,
        data_hora_evento=False,
    ):
        """Binding details in:
        nfelib/nfe_evento_cancel/bindings/v1_0/leiaute_evento_canc_nfe_v1_00.py
        """
        tipo_evento = "110111"
        sequencia = "1"
        return TeventoCancel.InfEvento(
            Id="ID" + tipo_evento + chave + sequencia.zfill(2),
            cOrgao=self.uf,
            tpAmb=self.ambiente,
            CNPJ=chave[6:20],
            # CPF TODO
            chNFe=chave,
            dhEvento=data_hora_evento or self._timestamp(),
            tpEvento="110111",
            nSeqEvento="1",
            verEvento="1.00",
            detEvento=TeventoCancel.InfEvento.DetEvento(
                versao="1.00",
                descEvento="Cancelamento",
                nProt=protocolo_autorizacao,
                xJust=justificativa,
            ),
        )

    # OK 100%
    def carta_correcao(
        self, chave: str, sequencia: str, justificativa: str, data_hora_evento: str = ""
    ):
        """Binding details:
        nfelib/nfe_evento_cancel/bindings/v1_0/leiaute_evento_canc_nfe_v1_00.py
        """
        return TeventoCCe.InfEvento(
            Id="ID" + tipo_evento + chave + sequencia.zfill(2),
            cOrgao=self.uf,
            tpAmb=self.ambiente,
            CNPJ=chave[6:20],
            CPF=None,  # TODO
            chNFe=chave,
            dhEvento=data_hora_evento or self._timestamp(),
            tpEvento=tipo_evento,
            nSeqEvento=sequencia,
            verEvento="1.00",
            detEvento=TeventoCCe.InfEvento.DetEvento(
                versao="1.00",
                descEvento="Carta de Correcao",
                xCorrecao=justificativa,
                xCondUso=TEXTO_CARTA_CORRECAO,
            ),
        )

    # OK 100%
    def inutilizacao(
        self,
        cnpj: str,
        mod: str,
        serie: str,
        num_ini: str,
        num_fin: str,
        justificativa: str,
    ) -> TinutNfe:
        """Binding details in:
        nfelib/nfe/bindings/v4_0/leiaute_inut_nfe_v4_00.py
        """
        year = str(date.today().year)[2:]
        return InutNfe(
            infInut=InutNfe.InfInut(
                Id="ID"
                + self.uf
                + year
                + cnpj
                + mod
                + serie.zfill(3)
                + str(num_ini).zfill(9)
                + str(num_fin).zfill(9),
                tpAmb=self.ambiente,
                xServ="INUTILIZAR",
                cUF=self.uf,
                ano=year,
                CNPJ=cnpj,
                mod=mod,
                serie=serie,
                nNFIni=str(num_ini),
                nNFFin=str(num_fin),
                xJust=justificativa,
            ),
            versao=self.versao,
        )

    ######################################
    # Misc
    ######################################

    def _aguarda_tempo_medio(self, proc_envio: EnviNfe):
        time.sleep(float(proc_envio.infRec.tMed) * 1.3)

    ######################################
    # DF-e
    ######################################

    def consultar_distribuicao(
        self, cnpj_cpf, ultimo_nsu=False, nsu_especifico=False, chave=False
    ):
        return self.send(
            NfeDistribuicaoDfeSoapNfeDistDfeInteresse,
            # TODO
        )

    #    def monta_processo(self, edoc, proc_envio, proc_recibo):
    #        nfe = proc_envio.envio_raiz.find('{' + self._namespace + '}NFe')
    #        protocolos = proc_recibo.resposta.protNFe
    #        if nfe and protocolos:
    #            if type(protocolos) != list:
    #                protocolos = [protocolos]
    #            for protocolo in protocolos:
    #                nfe_proc = retEnviNFe.TNfeProc(
    #                    versao=self.versao,
    #                    protNFe=protocolo,
    #                )
    #                nfe_proc.original_tagname_ = 'nfeProc'
    #                xml_file, nfe_proc = self._generateds_to_string_etree(nfe_proc)
    #                prot_nfe = nfe_proc.find('{' + self._namespace + '}protNFe')
    #                prot_nfe.addprevious(nfe)
    #                proc_recibo.processo = nfe_proc
    #                proc_recibo.processo_xml = \
    #                    self._generateds_to_string_etree(nfe_proc)[0]
    #                proc_recibo.protocolo = protocolo
    #            return True
