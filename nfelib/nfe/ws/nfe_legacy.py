# Copyright (C) 2019  Luis Felipe Mileo - KMEE
# (adapted here by Raphaël Valyi)

import datetime

from lxml import etree

try:
    from erpbrasil.edoc.nfe import (
        NFe,
        localizar_url,
        WS_NFE_SITUACAO,
        WS_NFE_CONSULTA,
        WS_NFE_AUTORIZACAO,
        WS_NFE_INUTILIZACAO,
        WS_DFE_DISTRIBUICAO,
        WS_NFE_RET_AUTORIZACAO,
        WS_NFE_RECEPCAO_EVENTO,
        TEXTO_CARTA_CORRECAO,
        Metodo,
        METODO_WS,
    )
except ImportError:
    raise RuntimeError(
        "You need to install the erpbrasil.edoc package to use this legacy webservice layer."
    )

from nfelib.bindings.nfe.v4_0.proc_nfe_v4_00 import NfeProc
from nfelib.bindings.nfe.v4_0.inut_nfe_v4_00 import InutNfe
from nfelib.bindings.nfe.v4_0.ret_inut_nfe_v4_00 import RetInutNfe
from nfelib.bindings.nfe.v4_0.cons_stat_serv_v4_00 import ConsStatServ
from nfelib.bindings.nfe.v4_0.ret_cons_stat_serv_v4_00 import RetConsStatServ
from nfelib.bindings.nfe.v4_0.cons_sit_nfe_v4_00 import ConsSitNfe
from nfelib.bindings.nfe.v4_0.ret_cons_sit_nfe_v4_00 import RetConsSitNfe
from nfelib.bindings.nfe.v4_0.envi_nfe_v4_00 import EnviNfe
from nfelib.bindings.nfe.v4_0.ret_envi_nfe_v4_00 import RetEnviNfe
from nfelib.bindings.nfe.v4_0.cons_reci_nfe_v4_00 import ConsReciNfe
from nfelib.bindings.nfe.v4_0.ret_cons_reci_nfe_v4_00 import RetConsReciNfe
from nfelib.bindings.nfe_dist_dfe.v1_0 import DistDfeInt
from nfelib.bindings.nfe_dist_dfe.v1_0 import RetDistDfeInt
from nfelib.bindings.nfe_evento_generico.v1_0.env_evento_v1_00 import (
    EnvEvento as EnvEventoGenerico,
)
from nfelib.bindings.nfe_evento_cce.v1_0.leiaute_cce_v1_00 import Tevento as TeventoCCe
from nfelib.bindings.nfe_evento_generico.v1_0.ret_env_evento_v1_00 import (
    RetEnvEvento as RetEnvEventoGenerico,
)
from nfelib.bindings.nfe_evento_cancel.v1_0.evento_canc_nfe_v1_00 import (
    Evento as EventoCancNfe,
)
from nfelib.bindings.nfe_evento_cce.v1_0.cce_v1_00 import Evento as EventoCCe

from .edoc_legacy import DocumentoElectronicoLegacy

WS_DOWNLOAD_NFE = "nfeDistDfeInteresse"
METODO_WS[WS_DFE_DISTRIBUICAO] = Metodo("NFeDistribuicaoDFe", "nfeDistDfeInteresse")


class NFeLegacy(DocumentoElectronicoLegacy, NFe):
    def status_servico(self):
        raiz = ConsStatServ(  # CHANGED FOR XSDATA
            versao=self.versao,
            tpAmb=self.ambiente,
            cUF=self.uf,
            xServ="STATUS",
        )
        # raiz.original_tagname_ = 'consStatServ'  # CHANGED FOR XSDATA
        return self._post_xsdata(
            raiz,
            # 'https://hom.sefazvirtual.fazenda.gov.br/NFeStatusServico4/NFeStatusServico4.asmx?wsdl',
            localizar_url(WS_NFE_SITUACAO, str(self.uf), self.mod, int(self.ambiente)),
            "nfeStatusServicoNF",
            RetConsStatServ,  # CHANGED FOR XSDATA
        )

    def consulta_documento(self, chave):
        raiz = ConsSitNfe(  # CHANGED FOR XSDATA
            versao=self.versao,
            tpAmb=self.ambiente,
            xServ="CONSULTAR",
            chNFe=chave,
        )
        # raiz.original_tagname_ = 'consSitNFe'  # CHANGED FOR XSDATA
        return self._post_xsdata(
            raiz,
            # 'https://hom.sefazvirtual.fazenda.gov.br/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx?wsdl',
            localizar_url(WS_NFE_CONSULTA, str(self.uf), self.mod, int(self.ambiente)),
            "nfeConsultaNF",
            RetConsSitNfe,  # CHANGED FOR XSDATA
        )

    def envia_documento(self, edoc):
        """

        Exportar o documento
        Assinar o documento
        Adicionar o mesmo ao envio

        :param edoc:
        :return:
        """
        xml_assinado = self.assina_raiz(edoc, edoc.infNFe.Id)

        raiz = EnviNfe(  # CHANGED FOR XSDATA
            versao=self.versao,
            idLote=datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            indSinc="0",
        )
        # raiz.original_tagname_ = 'enviNFe'  # CHANGED FOR XSDATA
        xml_envio_string, xml_envio_etree = self.render_edoc_xsdata(raiz)
        xml_envio_etree.append(etree.fromstring(xml_assinado))

        # teste_string, teste_etree = self.render_edoc_xsdata(xml_envio_etree)

        return self._post_xsdata(
            xml_envio_etree,
            # 'https://hom.sefazvirtual.fazenda.gov.br/NFeAutorizacao4/NFeAutorizacao4.asmx?wsdl',
            localizar_url(
                WS_NFE_AUTORIZACAO, str(self.uf), self.mod, int(self.ambiente)
            ),
            "nfeAutorizacaoLote",
            RetEnviNfe,  # CHANGED FOR XSDATA
        )

    def envia_inutilizacao(self, evento):
        tinut = InutNfe(  # CHANGED FOR XSDATA
            versao=self.versao, infInut=evento, signature=None
        )  # CHANGED FOR XSDATA
        # tinut.original_tagname_ = 'inutNFe'  # CHANGED FOR XSDATA

        xml_assinado = self.assina_raiz(tinut, tinut.infInut.Id)

        xml_envio_etree = etree.fromstring(xml_assinado)

        return self._post_xsdata(
            xml_envio_etree,
            localizar_url(
                WS_NFE_INUTILIZACAO, str(self.uf), self.mod, int(self.ambiente)
            ),
            "nfeInutilizacaoNF",
            RetInutNfe,  # CHANGED FOR XSDATA
        )

    def consulta_recibo(self, numero=False, proc_envio=False):
        if proc_envio:
            numero = proc_envio.resposta.infRec.nRec

        if not numero:
            return

        raiz = ConsReciNfe(  # CHANGED FOR XSDATA
            versao=self.versao,
            tpAmb=self.ambiente,
            nRec=numero,
        )
        # raiz.original_tagname_ = 'consReciNFe'  # CHANGED FOR XSDATA
        return self._post_xsdata(
            raiz,
            localizar_url(
                WS_NFE_RET_AUTORIZACAO, str(self.uf), self.mod, int(self.ambiente)
            ),
            # 'ws/nferetautorizacao4.asmx'
            "nfeRetAutorizacaoLote",
            RetConsReciNfe,  # CHANGED FOR XSDATA
        )

    def enviar_lote_evento(self, lista_eventos, numero_lote=False):
        if not numero_lote:
            numero_lote = self._gera_numero_lote()

        raiz = EnvEventoGenerico(
            versao="1.00", idLote=numero_lote
        )  # CHANGED FOR XSDATA
        # raiz.original_tagname_ = 'envEvento'  # CHANGED FOR XSDATA
        xml_envio_string, xml_envio_etree = self.render_edoc_xsdata(raiz)

        for inf_evento in lista_eventos:  # CHANGED FOR XSDATA BEGIN
            if isinstance(inf_evento, TeventoCCe.InfEvento):
                Evento = TeventoCCe
            if isinstance(inf_evento, EventoCancNfe.InfEvento):
                Evento = EventoCancNfe
            else:
                raise RuntimeError("Tipo de evento errado!")

            evento = Evento(
                versao="1.00",
                inf_evento=inf_evento,
            )
            # evento.original_tagname_ = 'evento'  # CHANGED FOR XSDATA END
            xml_assinado = self.assina_raiz(evento, evento.infEvento.Id)
            xml_envio_etree.append(etree.fromstring(xml_assinado))

        return self._post_xsdata(
            xml_envio_etree,
            localizar_url(
                WS_NFE_RECEPCAO_EVENTO, str(self.uf), self.mod, int(self.ambiente)
            ),
            "nfeRecepcaoEvento",
            RetEnvEventoGenerico,  # CHANGED FOR XSDATA
        )

    def cancela_documento(
        self, chave, protocolo_autorizacao, justificativa, data_hora_evento=False
    ):
        tipo_evento = "110111"
        sequencia = "1"
        raiz = EventoCancNfe.InfEvento(  # CHANGED FOR XSDATA
            Id="ID" + tipo_evento + chave + sequencia.zfill(2),
            cOrgao=self.uf,
            tpAmb=self.ambiente,
            CNPJ=chave[6:20],
            chNFe=chave,
            dhEvento=data_hora_evento or self._hora_agora(),
            tpEvento="110111",
            nSeqEvento="1",
            verEvento="1.00",
            detEvento=EventoCancNfe.InfEvento.DetEvento(  # CHANGED FOR XSDATA
                versao="1.00",
                descEvento="Cancelamento",
                nProt=protocolo_autorizacao,
                xJust=justificativa,
            ),
        )
        # raiz.original_tagname_ = 'infEvento'  # CHANGED FOR XSDATA
        return raiz

    def carta_correcao(self, chave, sequencia, justificativa, data_hora_evento=False):
        tipo_evento = "110110"
        raiz = EventoCCe.InfEvento(  # CHANGED FOR XSDATA
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
            detEvento=EventoCCe.InfEvento.DetEvento(  # CHANGED FOR XSDATA
                versao="1.00",
                descEvento="Carta de Correcao",
                xCorrecao=justificativa,
                xCondUso=TEXTO_CARTA_CORRECAO,
            ),
        )
        # raiz.original_tagname_ = 'infEvento' # CHANGED FOR XSDATA
        return raiz

    def inutilizacao(self, cnpj, mod, serie, num_ini, num_fin, justificativa):
        ano = str(datetime.date.today().year)[2:]
        uf = str(self.uf)
        raiz = InutNfe.InfInut(  # CHANGED FOR XSDATA
            Id="ID"
            + uf
            + ano
            + cnpj
            + mod
            + serie.zfill(3)
            + str(num_ini).zfill(9)
            + str(num_fin).zfill(9),
            tpAmb=self.ambiente,
            xServ="INUTILIZAR",
            cUF=self.uf,
            ano=ano,
            CNPJ=cnpj,
            mod=mod,
            serie=serie,
            nNFIni=str(num_ini),
            nNFFin=str(num_fin),
            xJust=justificativa,
        )
        # raiz.original_tagname_ = 'infInut' # CHANGED FOR XSDATA
        return raiz

    def consultar_distribuicao(
        self, cnpj_cpf, ultimo_nsu=False, nsu_especifico=False, chave=False
    ):
        """

        :param cnpj_cpf: CPF ou CNPJ a ser consultado
        :param ultimo_nsu: Último NSU para pesquisa. Formato: '999999999999999'
        :param nsu_especifico: NSU Específico para pesquisa.
                                Formato: '999999999999999'
        :param chave: Chave de acesso do documento
        :return: Retorna uma estrutura contendo as estruturas de envio
        e retorno preenchidas
        """

        if not ultimo_nsu and not nsu_especifico and not chave:
            return

        distNSU = consNSU = consChNFe = None
        if ultimo_nsu:
            distNSU = DistDfeInt.DistNsu(ultNSU=ultimo_nsu)  # CHANGED FOR XSDATA
        if nsu_especifico:
            consNSU = DistDfeInt.ConsNsu(NSU=nsu_especifico)
        if chave:
            consChNFe = DistDfeInt.ConsChNfe(chNFe=chave)

        if distNSU and consNSU or distNSU and consChNFe or consNSU and consChNFe:
            # TODO: Raise?
            return

        raiz = DistDfeInt(  # CHANGED FOR XSDATA
            versao=self.versao,
            tpAmb=self.ambiente,
            cUFAutor=self.uf,
            CNPJ=cnpj_cpf if len(cnpj_cpf) > 11 else None,
            CPF=cnpj_cpf if len(cnpj_cpf) <= 11 else None,
            distNSU=distNSU,
            consNSU=consNSU,
            consChNFe=consChNFe,
        )

        return self._post_xsdata(
            raiz,
            localizar_url(
                WS_DFE_DISTRIBUICAO, str(self.uf), self.mod, int(self.ambiente)
            ),
            "nfeDistDfeInteresse",
            RetDistDfeInt,  # CHANGED FOR XSDATA
        )

    def monta_processo(self, edoc, proc_envio, proc_recibo):
        nfe = proc_envio.envio_raiz.find("{" + self._namespace + "}NFe")
        protocolos = proc_recibo.resposta.protNFe
        if nfe and protocolos:
            if not isinstance(protocolos, list):  # CHANGED FOR XSDATA
                protocolos = [protocolos]
            for protocolo in protocolos:
                nfe_proc = NfeProc(
                    versao=self.versao,
                    protNFe=protocolo,
                )
                # nfe_proc.original_tagname_ = 'nfeProc'  # CHANGED FOR XSDATA
                xml_file, nfe_proc = self.render_edoc_xsdata(nfe_proc)
                prot_nfe = nfe_proc.find("{" + self._namespace + "}protNFe")
                prot_nfe.addprevious(nfe)
                proc_recibo.processo = nfe_proc
                proc_recibo.processo_xml = self.render_edoc_xsdata(nfe_proc)[0]
                proc_recibo.protocolo = protocolo
            return True

    # TODO falta por as classes no nfelib verao xsdata


#    def consultar_cadastro(self, uf, cnpj=None, cpf=None, ie=None):
#
#        if not cnpj and not cpf and not ie:
#            return
#
#        infCons = retConsCad.infConsType(  # CHANGED FOR XSDATA
#            xServ='CONS-CAD',
#            UF=uf,
#            IE=ie,
#            CNPJ=cnpj,
#            CPF=cpf,
#        )
#
#        raiz = retConsCad.TConsCad(  # CHANGED FOR XSDATA
#            versao='2.00',
#            infCons=infCons,
#        )
#        # raiz.original_tagname_ = 'ConsCad'  # CHANGED FOR XSDATA
#
#        return self._post_xsdata(
#            raiz,
#            localizar_url(
#                WS_NFE_CADASTRO, str(self.uf), self.mod, int(self.ambiente)),
#            'consultaCadastro',
#            retConsCad   # CHANGED FOR XSDATA
#        )
