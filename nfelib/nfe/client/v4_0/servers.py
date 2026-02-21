# Auto-generated file. Do not edit manually.
# ruff: noqa: D101
# ruff: noqa: E501

from __future__ import annotations  # Python 3.8 compat

from enum import Enum
from typing import TypedDict


class Endpoint(Enum):
    NFEINUTILIZACAO = "NfeInutilizacao"
    NFECONSULTAPROTOCOLO = "NfeConsultaProtocolo"
    NFESTATUSSERVICO = "NfeStatusServico"
    NFECONSULTACADASTRO = "NfeConsultaCadastro"
    RECEPCAOEVENTO = "RecepcaoEvento"
    NFEAUTORIZACAO = "NFeAutorizacao"
    NFERETAUTORIZACAO = "NFeRetAutorizacao"
    NFEDISTRIBUICAODFE = "NFeDistribuicaoDFe"


class ServerConfig(TypedDict):
    soap_version: str
    prod_endpoints: dict[Endpoint, str]
    dev_endpoints: dict[Endpoint, str]


servers: dict[str, ServerConfig] = {
    "AM": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfe.sefaz.am.gov.br/services2/services/NfeInutilizacao4",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe.sefaz.am.gov.br/services2/services/NfeConsulta4",
            Endpoint.NFESTATUSSERVICO: "https://nfe.sefaz.am.gov.br/services2/services/NfeStatusServico4",
            Endpoint.NFECONSULTACADASTRO: "https://nfe.sefaz.am.gov.br/services2/services/CadConsultaCadastro4",
            Endpoint.RECEPCAOEVENTO: "https://nfe.sefaz.am.gov.br/services2/services/RecepcaoEvento4",
            Endpoint.NFEAUTORIZACAO: "https://nfe.sefaz.am.gov.br/services2/services/NfeAutorizacao4",
            Endpoint.NFERETAUTORIZACAO: "https://nfe.sefaz.am.gov.br/services2/services/NfeRetAutorizacao4",
        },
        "dev_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://homnfe.sefaz.am.gov.br/services2/services/NfeInutilizacao4",
            Endpoint.NFECONSULTAPROTOCOLO: "https://homnfe.sefaz.am.gov.br/services2/services/NfeConsulta4",
            Endpoint.NFESTATUSSERVICO: "https://homnfe.sefaz.am.gov.br/services2/services/NfeStatusServico4",
            Endpoint.NFECONSULTACADASTRO: "https://homnfe.sefaz.am.gov.br/services2/services/CadConsultaCadastro4",
            Endpoint.RECEPCAOEVENTO: "https://homnfe.sefaz.am.gov.br/services2/services/RecepcaoEvento4",
            Endpoint.NFEAUTORIZACAO: "https://homnfe.sefaz.am.gov.br/services2/services/NfeAutorizacao4",
            Endpoint.NFERETAUTORIZACAO: "https://homnfe.sefaz.am.gov.br/services2/services/NfeRetAutorizacao4",
        },
    },
    "BA": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfe.sefaz.ba.gov.br/webservices/NFeInutilizacao4/NFeInutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe.sefaz.ba.gov.br/webservices/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://nfe.sefaz.ba.gov.br/webservices/NFeStatusServico4/NFeStatusServico4.asmx",
            Endpoint.NFECONSULTACADASTRO: "https://nfe.sefaz.ba.gov.br/webservices/CadConsultaCadastro4/CadConsultaCadastro4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://nfe.sefaz.ba.gov.br/webservices/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://nfe.sefaz.ba.gov.br/webservices/NFeAutorizacao4/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://nfe.sefaz.ba.gov.br/webservices/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx",
        },
        "dev_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://hnfe.sefaz.ba.gov.br/webservices/NFeInutilizacao4/NFeInutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "https://hnfe.sefaz.ba.gov.br/webservices/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://hnfe.sefaz.ba.gov.br/webservices/NFeStatusServico4/NFeStatusServico4.asmx",
            Endpoint.NFECONSULTACADASTRO: "https://hnfe.sefaz.ba.gov.br/webservices/CadConsultaCadastro4/CadConsultaCadastro4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://hnfe.sefaz.ba.gov.br/webservices/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://hnfe.sefaz.ba.gov.br/webservices/NFeAutorizacao4/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://hnfe.sefaz.ba.gov.br/webservices/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx",
        },
    },
    "GO": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfe.sefaz.go.gov.br/nfe/services/NFeInutilizacao4?wsdl",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe.sefaz.go.gov.br/nfe/services/NFeConsultaProtocolo4?wsdl",
            Endpoint.NFESTATUSSERVICO: "https://nfe.sefaz.go.gov.br/nfe/services/NFeStatusServico4?wsdl",
            Endpoint.NFECONSULTACADASTRO: "https://nfe.sefaz.go.gov.br/nfe/services/CadConsultaCadastro4?wsdl",
            Endpoint.RECEPCAOEVENTO: "https://nfe.sefaz.go.gov.br/nfe/services/NFeRecepcaoEvento4?wsdl",
            Endpoint.NFEAUTORIZACAO: "https://nfe.sefaz.go.gov.br/nfe/services/NFeAutorizacao4?wsdl",
            Endpoint.NFERETAUTORIZACAO: "https://nfe.sefaz.go.gov.br/nfe/services/NFeRetAutorizacao4?wsdl",
        },
        "dev_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://homolog.sefaz.go.gov.br/nfe/services/NFeInutilizacao4?wsdl",
            Endpoint.NFECONSULTAPROTOCOLO: "https://homolog.sefaz.go.gov.br/nfe/services/NFeConsultaProtocolo4?wsdl",
            Endpoint.NFESTATUSSERVICO: "https://homolog.sefaz.go.gov.br/nfe/services/NFeStatusServico4?wsdl",
            Endpoint.NFECONSULTACADASTRO: "https://homolog.sefaz.go.gov.br/nfe/services/CadConsultaCadastro4?wsdl",
            Endpoint.RECEPCAOEVENTO: "https://homolog.sefaz.go.gov.br/nfe/services/NFeRecepcaoEvento4?wsdl",
            Endpoint.NFEAUTORIZACAO: "https://homolog.sefaz.go.gov.br/nfe/services/NFeAutorizacao4?wsdl",
            Endpoint.NFERETAUTORIZACAO: "https://homolog.sefaz.go.gov.br/nfe/services/NFeRetAutorizacao4?wsdl",
        },
    },
    "MG": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfe.fazenda.mg.gov.br/nfe2/services/NFeInutilizacao4",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe.fazenda.mg.gov.br/nfe2/services/NFeConsultaProtocolo4",
            Endpoint.NFESTATUSSERVICO: "https://nfe.fazenda.mg.gov.br/nfe2/services/NFeStatusServico4",
            Endpoint.NFECONSULTACADASTRO: "https://nfe.fazenda.mg.gov.br/nfe2/services/CadConsultaCadastro4",
            Endpoint.RECEPCAOEVENTO: "https://nfe.fazenda.mg.gov.br/nfe2/services/NFeRecepcaoEvento4",
            Endpoint.NFEAUTORIZACAO: "https://nfe.fazenda.mg.gov.br/nfe2/services/NFeAutorizacao4",
            Endpoint.NFERETAUTORIZACAO: "https://nfe.fazenda.mg.gov.br/nfe2/services/NFeRetAutorizacao4",
        },
        "dev_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://hnfe.fazenda.mg.gov.br/nfe2/services/NFeInutilizacao4",
            Endpoint.NFECONSULTAPROTOCOLO: "https://hnfe.fazenda.mg.gov.br/nfe2/services/NFeConsultaProtocolo4",
            Endpoint.NFESTATUSSERVICO: "https://hnfe.fazenda.mg.gov.br/nfe2/services/NFeStatusServico4",
            Endpoint.NFECONSULTACADASTRO: "https://hnfe.fazenda.mg.gov.br/nfe2/services/CadConsultaCadastro4",
            Endpoint.RECEPCAOEVENTO: "https://hnfe.fazenda.mg.gov.br/nfe2/services/NFeRecepcaoEvento4",
            Endpoint.NFEAUTORIZACAO: "https://hnfe.fazenda.mg.gov.br/nfe2/services/NFeAutorizacao4",
            Endpoint.NFERETAUTORIZACAO: "https://hnfe.fazenda.mg.gov.br/nfe2/services/NFeRetAutorizacao4",
        },
    },
    "MS": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfe.sefaz.ms.gov.br/ws/NFeInutilizacao4",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe.sefaz.ms.gov.br/ws/NFeConsultaProtocolo4",
            Endpoint.NFESTATUSSERVICO: "https://nfe.sefaz.ms.gov.br/ws/NFeStatusServico4",
            Endpoint.NFECONSULTACADASTRO: "https://nfe.sefaz.ms.gov.br/ws/CadConsultaCadastro4",
            Endpoint.RECEPCAOEVENTO: "https://nfe.sefaz.ms.gov.br/ws/NFeRecepcaoEvento4",
            Endpoint.NFEAUTORIZACAO: "https://nfe.sefaz.ms.gov.br/ws/NFeAutorizacao4",
            Endpoint.NFERETAUTORIZACAO: "https://nfe.sefaz.ms.gov.br/ws/NFeRetAutorizacao4",
        },
        "dev_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://hom.nfe.sefaz.ms.gov.br/ws/NFeInutilizacao4",
            Endpoint.NFECONSULTAPROTOCOLO: "https://hom.nfe.sefaz.ms.gov.br/ws/NFeConsultaProtocolo4",
            Endpoint.NFESTATUSSERVICO: "https://hom.nfe.sefaz.ms.gov.br/ws/NFeStatusServico4",
            Endpoint.NFECONSULTACADASTRO: "https://hom.nfe.sefaz.ms.gov.br/ws/CadConsultaCadastro4",
            Endpoint.RECEPCAOEVENTO: "https://hom.nfe.sefaz.ms.gov.br/ws/NFeRecepcaoEvento4",
            Endpoint.NFEAUTORIZACAO: "https://hom.nfe.sefaz.ms.gov.br/ws/NFeAutorizacao4",
            Endpoint.NFERETAUTORIZACAO: "https://hom.nfe.sefaz.ms.gov.br/ws/NFeRetAutorizacao4",
        },
    },
    "MT": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfe.sefaz.mt.gov.br/nfews/v2/services/NfeInutilizacao4?wsdl",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe.sefaz.mt.gov.br/nfews/v2/services/NfeConsulta4?wsdl",
            Endpoint.NFESTATUSSERVICO: "https://nfe.sefaz.mt.gov.br/nfews/v2/services/NfeStatusServico4?wsdl",
            Endpoint.NFECONSULTACADASTRO: "https://nfe.sefaz.mt.gov.br/nfews/v2/services/CadConsultaCadastro4?wsdl",
            Endpoint.RECEPCAOEVENTO: "https://nfe.sefaz.mt.gov.br/nfews/v2/services/RecepcaoEvento4?wsdl",
            Endpoint.NFEAUTORIZACAO: "https://nfe.sefaz.mt.gov.br/nfews/v2/services/NfeAutorizacao4?wsdl",
            Endpoint.NFERETAUTORIZACAO: "https://nfe.sefaz.mt.gov.br/nfews/v2/services/NfeRetAutorizacao4?wsdl",
        },
        "dev_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://homologacao.sefaz.mt.gov.br/nfews/v2/services/NfeInutilizacao4?wsdl",
            Endpoint.NFECONSULTAPROTOCOLO: "https://homologacao.sefaz.mt.gov.br/nfews/v2/services/NfeConsulta4?wsdl",
            Endpoint.NFESTATUSSERVICO: "https://homologacao.sefaz.mt.gov.br/nfews/v2/services/NfeStatusServico4?wsdl",
            Endpoint.NFECONSULTACADASTRO: "https://homologacao.sefaz.mt.gov.br/nfews/v2/services/CadConsultaCadastro4?wsdl",
            Endpoint.RECEPCAOEVENTO: "https://homologacao.sefaz.mt.gov.br/nfews/v2/services/RecepcaoEvento4?wsdl",
            Endpoint.NFEAUTORIZACAO: "https://homologacao.sefaz.mt.gov.br/nfews/v2/services/NfeAutorizacao4?wsdl",
            Endpoint.NFERETAUTORIZACAO: "https://homologacao.sefaz.mt.gov.br/nfews/v2/services/NfeRetAutorizacao4?wsdl",
        },
    },
    "PE": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfe.sefaz.pe.gov.br/nfe-service/services/NFeInutilizacao4",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe.sefaz.pe.gov.br/nfe-service/services/NFeConsultaProtocolo4",
            Endpoint.NFESTATUSSERVICO: "https://nfe.sefaz.pe.gov.br/nfe-service/services/NFeStatusServico4",
            Endpoint.NFECONSULTACADASTRO: "https://nfe.sefaz.pe.gov.br/nfe-service/services/CadConsultaCadastro4?wsdl",
            Endpoint.RECEPCAOEVENTO: "https://nfe.sefaz.pe.gov.br/nfe-service/services/NFeRecepcaoEvento4",
            Endpoint.NFEAUTORIZACAO: "https://nfe.sefaz.pe.gov.br/nfe-service/services/NFeAutorizacao4",
            Endpoint.NFERETAUTORIZACAO: "https://nfe.sefaz.pe.gov.br/nfe-service/services/NFeRetAutorizacao4",
        },
        "dev_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfehomolog.sefaz.pe.gov.br/nfe-service/services/NFeInutilizacao4?wsdl",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfehomolog.sefaz.pe.gov.br/nfe-service/services/NFeConsultaProtocolo4?wsdl",
            Endpoint.NFESTATUSSERVICO: "https://nfehomolog.sefaz.pe.gov.br/nfe-service/services/NFeStatusServico4?wsdl",
            Endpoint.NFECONSULTACADASTRO: "https://nfehomolog.sefaz.pe.gov.br/nfe-service/services/CadConsultaCadastro4?wsdl",
            Endpoint.RECEPCAOEVENTO: "https://nfehomolog.sefaz.pe.gov.br/nfe-service/services/NFeRecepcaoEvento4?wsdl",
            Endpoint.NFEAUTORIZACAO: "https://nfehomolog.sefaz.pe.gov.br/nfe-service/services/NFeAutorizacao4?wsdl",
            Endpoint.NFERETAUTORIZACAO: "https://nfehomolog.sefaz.pe.gov.br/nfe-service/services/NFeRetAutorizacao4?wsdl",
        },
    },
    "PR": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfe.sefa.pr.gov.br/nfe/NFeInutilizacao4?wsdl",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe.sefa.pr.gov.br/nfe/NFeConsultaProtocolo4?wsdl",
            Endpoint.NFESTATUSSERVICO: "https://nfe.sefa.pr.gov.br/nfe/NFeStatusServico4?wsdl",
            Endpoint.NFECONSULTACADASTRO: "https://nfe.sefa.pr.gov.br/nfe/CadConsultaCadastro4?wsdl",
            Endpoint.RECEPCAOEVENTO: "https://nfe.sefa.pr.gov.br/nfe/NFeRecepcaoEvento4?wsdl",
            Endpoint.NFEAUTORIZACAO: "https://nfe.sefa.pr.gov.br/nfe/NFeAutorizacao4?wsdl",
            Endpoint.NFERETAUTORIZACAO: "https://nfe.sefa.pr.gov.br/nfe/NFeRetAutorizacao4?wsdl",
        },
        "dev_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://homologacao.nfe.sefa.pr.gov.br/nfe/NFeInutilizacao4?wsdl",
            Endpoint.NFECONSULTAPROTOCOLO: "https://homologacao.nfe.sefa.pr.gov.br/nfe/NFeConsultaProtocolo4?wsdl",
            Endpoint.NFESTATUSSERVICO: "https://homologacao.nfe.sefa.pr.gov.br/nfe/NFeStatusServico4?wsdl",
            Endpoint.NFECONSULTACADASTRO: "https://homologacao.nfe.sefa.pr.gov.br/nfe/CadConsultaCadastro4?wsdl",
            Endpoint.RECEPCAOEVENTO: "https://homologacao.nfe.sefa.pr.gov.br/nfe/NFeRecepcaoEvento4?wsdl",
            Endpoint.NFEAUTORIZACAO: "https://homologacao.nfe.sefa.pr.gov.br/nfe/NFeAutorizacao4?wsdl",
            Endpoint.NFERETAUTORIZACAO: "https://homologacao.nfe.sefa.pr.gov.br/nfe/NFeRetAutorizacao4?wsdl",
        },
    },
    "RS": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfe.sefazrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe.sefazrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://nfe.sefazrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx",
            Endpoint.NFECONSULTACADASTRO: "https://cad.svrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://nfe.sefazrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://nfe.sefazrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://nfe.sefazrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        },
        "dev_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfe-homologacao.sefazrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe-homologacao.sefazrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://nfe-homologacao.sefazrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx",
            Endpoint.NFECONSULTACADASTRO: "https://cad-homologacao.svrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://nfe-homologacao.sefazrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://nfe-homologacao.sefazrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://nfe-homologacao.sefazrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        },
    },
    "SP": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfe.fazenda.sp.gov.br/ws/nfeinutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe.fazenda.sp.gov.br/ws/nfeconsultaprotocolo4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://nfe.fazenda.sp.gov.br/ws/nfestatusservico4.asmx",
            Endpoint.NFECONSULTACADASTRO: "https://nfe.fazenda.sp.gov.br/ws/cadconsultacadastro4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://nfe.fazenda.sp.gov.br/ws/nferecepcaoevento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://nfe.fazenda.sp.gov.br/ws/nfeautorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://nfe.fazenda.sp.gov.br/ws/nferetautorizacao4.asmx",
        },
        "dev_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://homologacao.nfe.fazenda.sp.gov.br/ws/nfeinutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "https://homologacao.nfe.fazenda.sp.gov.br/ws/nfeconsultaprotocolo4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://homologacao.nfe.fazenda.sp.gov.br/ws/nfestatusservico4.asmx",
            Endpoint.NFECONSULTACADASTRO: "https://homologacao.nfe.fazenda.sp.gov.br/ws/cadconsultacadastro4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://homologacao.nfe.fazenda.sp.gov.br/ws/nferecepcaoevento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://homologacao.nfe.fazenda.sp.gov.br/ws/nfeautorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://homologacao.nfe.fazenda.sp.gov.br/ws/nferetautorizacao4.asmx",
        },
    },
    "SVAN": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://www.sefazvirtual.fazenda.gov.br/NFeInutilizacao4/NFeInutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "https://www.sefazvirtual.fazenda.gov.br/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://www.sefazvirtual.fazenda.gov.br/NFeStatusServico4/NFeStatusServico4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://www.sefazvirtual.fazenda.gov.br/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://www.sefazvirtual.fazenda.gov.br/NFeAutorizacao4/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://www.sefazvirtual.fazenda.gov.br/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx",
        },
        "dev_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://hom.sefazvirtual.fazenda.gov.br/NFeInutilizacao4/NFeInutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "https://hom.sefazvirtual.fazenda.gov.br/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://hom.sefazvirtual.fazenda.gov.br/NFeStatusServico4/NFeStatusServico4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://hom.sefazvirtual.fazenda.gov.br/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://hom.sefazvirtual.fazenda.gov.br/NFeAutorizacao4/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://hom.sefazvirtual.fazenda.gov.br/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx",
        },
    },
    "SVRS": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfe.svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe.svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://nfe.svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx",
            Endpoint.NFECONSULTACADASTRO: "https://cad.svrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://nfe.svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://nfe.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://nfe.svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        },
        "dev_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://nfe-homologacao.svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx",
            Endpoint.NFECONSULTACADASTRO: "https://cad-homologacao.svrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://nfe-homologacao.svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        },
    },
    "SVC-AN": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://www.sefazvirtual.fazenda.gov.br/NFeInutilizacao4/NFeInutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "https://www.sefazvirtual.fazenda.gov.br/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://www.sefazvirtual.fazenda.gov.br/NFeStatusServico4/NFeStatusServico4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://www.sefazvirtual.fazenda.gov.br/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://www.sefazvirtual.fazenda.gov.br/NFeAutorizacao4/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://www.sefazvirtual.fazenda.gov.br/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx",
        },
        "dev_endpoints": {
            Endpoint.NFEINUTILIZACAO: "https://hom.sefazvirtual.fazenda.gov.br/NFeInutilizacao4/NFeInutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "https://hom.sefazvirtual.fazenda.gov.br/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://hom.sefazvirtual.fazenda.gov.br/NFeStatusServico4/NFeStatusServico4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://hom.sefazvirtual.fazenda.gov.br/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://hom.sefazvirtual.fazenda.gov.br/NFeAutorizacao4/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://hom.sefazvirtual.fazenda.gov.br/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx",
        },
    },
    "SVC-RS": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe.svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://nfe.svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://nfe.svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://nfe.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://nfe.svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        },
        "dev_endpoints": {
            Endpoint.NFECONSULTAPROTOCOLO: "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx",
            Endpoint.NFESTATUSSERVICO: "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx",
            Endpoint.RECEPCAOEVENTO: "https://nfe-homologacao.svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx",
            Endpoint.NFEAUTORIZACAO: "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        },
    },
    "AN": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.RECEPCAOEVENTO: "https://www.nfe.fazenda.gov.br/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx",
            Endpoint.NFEDISTRIBUICAODFE: "https://www1.nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx",
        },
        "dev_endpoints": {
            Endpoint.NFEDISTRIBUICAODFE: "https://hom1.nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx",
            Endpoint.RECEPCAOEVENTO: "https://hom1.nfe.fazenda.gov.br/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx",
        },
    },
}
