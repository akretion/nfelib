import time
from dataclasses import dataclass
from datetime import date, datetime

from ...nfe_evento_cancel.bindings import v1_0 as cancel_v1
from ...nfe_evento_cancel.bindings.v1_0.evento_canc_nfe_v1_00 import (
    Tevento as TeventoCancel,
)
from ...nfe_evento_cancel.bindings.v1_0.leiaute_evento_canc_nfe_v1_00 import (
    TenvEvento,
    TretEnvEvento,
)
from ...nfe_evento_cce.bindings.v1_0.leiaute_cce_v1_00 import Tevento as TeventoCCe
from ...soap_client import SoapClient
from ..bindings import v4_0 as nfe_v4
from ..bindings.v4_0.cons_reci_nfe_v4_00 import ConsReciNfe
from ..bindings.v4_0.cons_sit_nfe_v4_00 import ConsSitNfe
from ..bindings.v4_0.cons_stat_serv_v4_00 import ConsStatServ
from ..bindings.v4_0.envi_nfe_v4_00 import EnviNfe
from ..bindings.v4_0.inut_nfe_v4_00 import InutNfe
from ..bindings.v4_0.leiaute_inut_nfe_v4_00 import TinutNfe
from ..bindings.v4_0.leiaute_nfe_v4_00 import Tnfe
from ..bindings.v4_0.ret_cons_reci_nfe_v4_00 import RetConsReciNfe
from ..bindings.v4_0.ret_cons_sit_nfe_v4_00 import RetConsSitNfe
from ..bindings.v4_0.ret_cons_stat_serv_v4_00 import RetConsStatServ
from ..bindings.v4_0.ret_envi_nfe_v4_00 import RetEnviNfe
from ..bindings.v4_0.ret_inut_nfe_v4_00 import RetInutNfe
from ..soap.nfeautorizacao4 import NfeAutorizacao4SoapNfeAutorizacaoLote
from ..soap.nfeconsulta4 import NfeConsultaProtocolo4SoapNfeConsultaNf
from ..soap.nfeinutilizacao4 import NfeInutilizacao4SoapNfeInutilizacaoNf
from ..soap.nferetautorizacao4 import NfeRetAutorizacao4SoapNfeRetAutorizacaoLote
from ..soap.nfestatusservico4 import NfeStatusServico4SoapNfeStatusServicoNf
from ..soap.recepcaoevento4 import NfeRecepcaoEvento4SoapNfeRecepcaoEvento

# NOTE about erpbrasil.edoc we emulate here: sometimes the erpbrasil.edoc API seems bad:
# in general it forces coupling with the binding classes and coupling with the sign lib.
# also takes 1 NFe, shouldn't it be a list??


@dataclass
class NfeSoapClient(SoapClient):
    """
    A façade for the NFe SOAP webserices.
    The API is the same as the erpbrasil.edoc package.
    """

    versao = "4.00"
    response_bindings_packages = [nfe_v4, cancel_v1]

    @classmethod
    def get_server(cls, service: str, cUF: str) -> str:
        return "https://nfe-homologacao.svrs.rs.gov.br"  # TODO implement

    ######################################
    # Webservices
    ######################################

    def status_servico(self, xServ: str = "STATUS") -> RetConsStatServ:
        return self.send(
            NfeStatusServico4SoapNfeStatusServicoNf,
            ConsStatServ(
                tpAmb=self.ambiente,
                cUF=self.uf,
                xServ=xServ,
                versao=self.versao,
            ),
            RetConsStatServ,
        )

    def consulta_documento(self, chave: str, xServ: str = "CONSULTAR") -> RetConsSitNfe:
        return self.send(
            NfeConsultaProtocolo4SoapNfeConsultaNf,
            ConsSitNfe(
                versao=self.versao,
                tpAmb=self.ambiente,
                xServ=xServ,
                chNFe=chave,
            ),
            RetConsSitNfe,
        )

    # NOTE: I changed the signature from erpbrasil.edoc
    # shouldn't we have a list of signed_nfe??
    def envia_documento(self, signed_nfe: str) -> RetEnviNfe:
        return self.send(
            NfeAutorizacao4SoapNfeAutorizacaoLote,
            EnviNfe(
                idLote=datetime.now().strftime("%Y%m%d%H%M%S"),
                versao=self.versao,
                indSinc="0",
                # we pass an empty placeholder_exp for the NFe to avoid an extra
                # XML parsing/serialization and possibly screwing the signature.
                NFe=[Tnfe()],
            ),
            RetEnviNfe,
            placeholder_exp="<NFe/>",
            placeholder_content=signed_nfe,
        )

    # NOTE erpbrasil.edoc coupling with TinutNfe seems bad, better take signed xml?
    def envia_inutilizacao(self, evento: InutNfe.InfInut) -> RetInutNfe:
        # NOTE: sure we don't take a signed xml input?
        evento_xml = self.serializer.render(
            evento, ns_map={None: "http://www.portalfiscal.inf.br/nfe"}
        )
        print("EEEEEEEEEEE", evento_xml)
        signed_xml = self.sign_xml(evento_xml, evento.infInut.Id)
        return self.send(
            NfeInutilizacao4SoapNfeInutilizacaoNf,
            InutNfe(),
#                versao=self.versao,
#                infInut=InutNfe.InfInut(),  # placeholder for signed xml
#                signature=None,
#            ),
            RetInutNfe,
            placeholder_exp='<inutNFe/>',
            placeholder_content=signed_xml,
        )

    # TODO not used in Odoo, seems broken
    def consulta_recibo(self, numero: str = "", proc_envio=False) -> RetConsReciNfe:
        if proc_envio:
            # FIXME: what is the proc_envio type with resposta inside? Seems broken
            numero = proc_envio.infRec.nRec

        if not numero:
            raise RuntimeError("Sem numero para consultar!")

        return self.send(
            NfeRetAutorizacao4SoapNfeRetAutorizacaoLote,
            ConsReciNfe(
                versao=self.versao,
                tpAmb=self.ambiente,
                nRec=numero,
            ),
            RetConsReciNfe,
        )

    def enviar_lote_evento(self, lista_eventos, numero_lote: str = "") -> TretEnvEvento:
        if not numero_lote:
            numero_lote = self._gera_numero_lote()

        signed_events_xml = ""
        for inf_evento in lista_eventos:
            evento = TeventoCancel(  # seems bad to use specific event in generic method
                versao="1.00",
                infEvento=inf_evento,
            )
            evento_xml = self.serializer.render(
                evento, ns_map={None: "http://www.portalfiscal.inf.br/nfe"}
            )
            signed_xml = self.sign_xml(evento_xml, evento.infEvento.Id)
            signed_events_xml += signed_xml  # TODO ensure this works!
        return self.send(
            NfeRecepcaoEvento4SoapNfeRecepcaoEvento,
            TenvEvento(
                versao="1.00", idLote=numero_lote, evento=[TeventoCancel()]  # placeholder
            ),
            TretEnvEvento,
            placeholder_exp='<ns2:TEnvEvento versao="1.00"><evento/></ns2:TEnvEvento>', #"<TEnvento/>",
            placeholder_content=signed_events_xml,
        )

    ######################################
    # Binding façades
    ######################################

    def cancela_documento(
        self,
        chave: str,
        protocolo_autorizacao: str,
        justificativa: str,
        data_hora_evento=False,
    ):
        tipo_evento = "110111"
        sequencia = "1"
        return TeventoCancel.InfEvento(
            Id="ID" + tipo_evento + chave + sequencia.zfill(2),
            cOrgao=self.uf,
            tpAmb=self.ambiente,
            CNPJ=chave[6:20],
            chNFe=chave,
            dhEvento=data_hora_evento or self._hora_agora(),
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

    def carta_correcao(
        self, chave: str, sequencia: str, justificativa: str, data_hora_evento: str = ""
    ):
        return TeventoCCe.InfEvento(
            Id="ID" + tipo_evento + chave + sequencia.zfill(2),
            cOrgao=self.uf,
            tpAmb=self.ambiente,
            CNPJ=chave[6:20],
            CPF=None,
            chNFe=chave,
            dhEvento=data_hora_evento or self._hora_agora(),
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

    def inutilizacao(
        self,
        cnpj: str,
        mod: str,
        serie: str,
        num_ini: str,
        num_fin: str,
        justificativa: str,
    ) -> TinutNfe:
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
        pass

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

    def consultar_cadastro(self, uf, cnpj=None, cpf=None, ie=None):
        pass
