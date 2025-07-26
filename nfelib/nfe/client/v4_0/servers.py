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
    prod_server: str
    dev_server: str
    soap_version: str
    endpoints: dict[Endpoint, str]


servers: dict[str, ServerConfig] = {
    "AM": {
        "prod_server": "nfe.sefaz.am.gov.br",
        "dev_server": "homnfe.sefaz.am.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.NFEINUTILIZACAO: "/services2/services/NfeInutilizacao4",
            Endpoint.NFECONSULTAPROTOCOLO: "/services2/services/NfeConsulta4",
            Endpoint.NFESTATUSSERVICO: "/services2/services/NfeStatusServico4",
            Endpoint.NFECONSULTACADASTRO: "/services2/services/CadConsultaCadastro4",
            Endpoint.RECEPCAOEVENTO: "/services2/services/RecepcaoEvento4",
            Endpoint.NFEAUTORIZACAO: "/services2/services/NfeAutorizacao4",
            Endpoint.NFERETAUTORIZACAO: "/services2/services/NfeRetAutorizacao4",
        },
    },
    "BA": {
        "prod_server": "nfe.sefaz.ba.gov.br",
        "dev_server": "hnfe.sefaz.ba.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.NFEINUTILIZACAO: "/webservices/NFeInutilizacao4/NFeInutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "/webservices/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx",
            Endpoint.NFESTATUSSERVICO: "/webservices/NFeStatusServico4/NFeStatusServico4.asmx",
            Endpoint.NFECONSULTACADASTRO: "/webservices/CadConsultaCadastro4/CadConsultaCadastro4.asmx",
            Endpoint.RECEPCAOEVENTO: "/webservices/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx",
            Endpoint.NFEAUTORIZACAO: "/webservices/NFeAutorizacao4/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "/webservices/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx",
        },
    },
    "GO": {
        "prod_server": "nfe.sefaz.go.gov.br",
        "dev_server": "homolog.sefaz.go.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.NFEINUTILIZACAO: "/nfe/services/NFeInutilizacao4?wsdl",
            Endpoint.NFECONSULTAPROTOCOLO: "/nfe/services/NFeConsultaProtocolo4?wsdl",
            Endpoint.NFESTATUSSERVICO: "/nfe/services/NFeStatusServico4?wsdl",
            Endpoint.NFECONSULTACADASTRO: "/nfe/services/CadConsultaCadastro4?wsdl",
            Endpoint.RECEPCAOEVENTO: "/nfe/services/NFeRecepcaoEvento4?wsdl",
            Endpoint.NFEAUTORIZACAO: "/nfe/services/NFeAutorizacao4?wsdl",
            Endpoint.NFERETAUTORIZACAO: "/nfe/services/NFeRetAutorizacao4?wsdl",
        },
    },
    "MG": {
        "prod_server": "nfe.fazenda.mg.gov.br",
        "dev_server": "hnfe.fazenda.mg.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.NFEINUTILIZACAO: "/nfe2/services/NFeInutilizacao4",
            Endpoint.NFECONSULTAPROTOCOLO: "/nfe2/services/NFeConsultaProtocolo4",
            Endpoint.NFESTATUSSERVICO: "/nfe2/services/NFeStatusServico4",
            Endpoint.NFECONSULTACADASTRO: "/nfe2/services/CadConsultaCadastro4",
            Endpoint.RECEPCAOEVENTO: "/nfe2/services/NFeRecepcaoEvento4",
            Endpoint.NFEAUTORIZACAO: "/nfe2/services/NFeAutorizacao4",
            Endpoint.NFERETAUTORIZACAO: "/nfe2/services/NFeRetAutorizacao4",
        },
    },
    "MS": {
        "prod_server": "nfe.sefaz.ms.gov.br",
        "dev_server": "hom.nfe.sefaz.ms.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.NFEINUTILIZACAO: "/ws/NFeInutilizacao4",
            Endpoint.NFECONSULTAPROTOCOLO: "/ws/NFeConsultaProtocolo4",
            Endpoint.NFESTATUSSERVICO: "/ws/NFeStatusServico4",
            Endpoint.NFECONSULTACADASTRO: "/ws/CadConsultaCadastro4",
            Endpoint.RECEPCAOEVENTO: "/ws/NFeRecepcaoEvento4",
            Endpoint.NFEAUTORIZACAO: "/ws/NFeAutorizacao4",
            Endpoint.NFERETAUTORIZACAO: "/ws/NFeRetAutorizacao4",
        },
    },
    "MT": {
        "prod_server": "nfe.sefaz.mt.gov.br",
        "dev_server": "homologacao.sefaz.mt.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.NFEINUTILIZACAO: "/nfews/v2/services/NfeInutilizacao4?wsdl",
            Endpoint.NFECONSULTAPROTOCOLO: "/nfews/v2/services/NfeConsulta4?wsdl",
            Endpoint.NFESTATUSSERVICO: "/nfews/v2/services/NfeStatusServico4?wsdl",
            Endpoint.NFECONSULTACADASTRO: "/nfews/v2/services/CadConsultaCadastro4?wsdl",
            Endpoint.RECEPCAOEVENTO: "/nfews/v2/services/RecepcaoEvento4?wsdl",
            Endpoint.NFEAUTORIZACAO: "/nfews/v2/services/NfeAutorizacao4?wsdl",
            Endpoint.NFERETAUTORIZACAO: "/nfews/v2/services/NfeRetAutorizacao4?wsdl",
        },
    },
    "PE": {
        "prod_server": "nfe.sefaz.pe.gov.br",
        "dev_server": "nfehomolog.sefaz.pe.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.NFEINUTILIZACAO: "/nfe-service/services/NFeInutilizacao4",
            Endpoint.NFECONSULTAPROTOCOLO: "/nfe-service/services/NFeConsultaProtocolo4",
            Endpoint.NFESTATUSSERVICO: "/nfe-service/services/NFeStatusServico4",
            Endpoint.NFECONSULTACADASTRO: "/nfe-service/services/CadConsultaCadastro4?wsdl",
            Endpoint.RECEPCAOEVENTO: "/nfe-service/services/NFeRecepcaoEvento4",
            Endpoint.NFEAUTORIZACAO: "/nfe-service/services/NFeAutorizacao4",
            Endpoint.NFERETAUTORIZACAO: "/nfe-service/services/NFeRetAutorizacao4",
        },
    },
    "PR": {
        "prod_server": "nfe.sefa.pr.gov.br",
        "dev_server": "homologacao.nfe.sefa.pr.gov.br",
        "soap_version": "1.2",
        "endpoints": {
            Endpoint.NFEINUTILIZACAO: "/nfe/NFeInutilizacao4?wsdl",
            Endpoint.NFECONSULTAPROTOCOLO: "/nfe/NFeConsultaProtocolo4?wsdl",
            Endpoint.NFESTATUSSERVICO: "/nfe/NFeStatusServico4?wsdl",
            Endpoint.NFECONSULTACADASTRO: "/nfe/CadConsultaCadastro4?wsdl",
            Endpoint.RECEPCAOEVENTO: "/nfe/NFeRecepcaoEvento4?wsdl",
            Endpoint.NFEAUTORIZACAO: "/nfe/NFeAutorizacao4?wsdl",
            Endpoint.NFERETAUTORIZACAO: "/nfe/NFeRetAutorizacao4?wsdl",
        },
    },
    "RS": {
        "prod_server": "nfe.sefazrs.rs.gov.br",
        "dev_server": "nfe-homologacao.sefazrs.rs.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.NFEINUTILIZACAO: "/ws/nfeinutilizacao/nfeinutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "/ws/NfeConsulta/NfeConsulta4.asmx",
            Endpoint.NFESTATUSSERVICO: "/ws/NfeStatusServico/NfeStatusServico4.asmx",
            Endpoint.NFECONSULTACADASTRO: "/ws/cadconsultacadastro/cadconsultacadastro4.asmx",
            Endpoint.RECEPCAOEVENTO: "/ws/recepcaoevento/recepcaoevento4.asmx",
            Endpoint.NFEAUTORIZACAO: "/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        },
    },
    "SP": {
        "prod_server": "nfe.fazenda.sp.gov.br",
        "dev_server": "homologacao.nfe.fazenda.sp.gov.br",
        "soap_version": "1.2",
        "endpoints": {
            Endpoint.NFEINUTILIZACAO: "/ws/nfeinutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "/ws/nfeconsultaprotocolo4.asmx",
            Endpoint.NFESTATUSSERVICO: "/ws/nfestatusservico4.asmx",
            Endpoint.NFECONSULTACADASTRO: "/ws/cadconsultacadastro4.asmx",
            Endpoint.RECEPCAOEVENTO: "/ws/nferecepcaoevento4.asmx",
            Endpoint.NFEAUTORIZACAO: "/ws/nfeautorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "/ws/nferetautorizacao4.asmx",
        },
    },
    "SVAN": {
        "prod_server": "www.sefazvirtual.fazenda.gov.br",
        "dev_server": "hom.sefazvirtual.fazenda.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.NFEINUTILIZACAO: "/NFeInutilizacao4/NFeInutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx",
            Endpoint.NFESTATUSSERVICO: "/NFeStatusServico4/NFeStatusServico4.asmx",
            Endpoint.RECEPCAOEVENTO: "/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx",
            Endpoint.NFEAUTORIZACAO: "/NFeAutorizacao4/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx",
        },
    },
    "SVRS": {
        "prod_server": "nfe.svrs.rs.gov.br",
        "dev_server": "nfe-homologacao.svrs.rs.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.NFEINUTILIZACAO: "/ws/nfeinutilizacao/nfeinutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "/ws/NfeConsulta/NfeConsulta4.asmx",
            Endpoint.NFESTATUSSERVICO: "/ws/NfeStatusServico/NfeStatusServico4.asmx",
            Endpoint.NFECONSULTACADASTRO: "/ws/cadconsultacadastro/cadconsultacadastro4.asmx",
            Endpoint.RECEPCAOEVENTO: "/ws/recepcaoevento/recepcaoevento4.asmx",
            Endpoint.NFEAUTORIZACAO: "/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        },
    },
    "SVC-AN": {
        "prod_server": "www.sefazvirtual.fazenda.gov.br",
        "dev_server": "hom.sefazvirtual.fazenda.gov.br",
        "soap_version": "1.2",
        "endpoints": {
            Endpoint.NFEINUTILIZACAO: "/NFeInutilizacao4/NFeInutilizacao4.asmx",
            Endpoint.NFECONSULTAPROTOCOLO: "/NFeConsultaProtocolo4/NFeConsultaProtocolo4.asmx",
            Endpoint.NFESTATUSSERVICO: "/NFeStatusServico4/NFeStatusServico4.asmx",
            Endpoint.RECEPCAOEVENTO: "/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx",
            Endpoint.NFEAUTORIZACAO: "/NFeAutorizacao4/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "/NFeRetAutorizacao4/NFeRetAutorizacao4.asmx",
        },
    },
    "SVC-RS": {
        "prod_server": "nfe.svrs.rs.gov.br",
        "dev_server": "nfe-homologacao.svrs.rs.gov.br",
        "soap_version": "1.2",
        "endpoints": {
            Endpoint.NFECONSULTAPROTOCOLO: "/ws/NfeConsulta/NfeConsulta4.asmx",
            Endpoint.NFESTATUSSERVICO: "/ws/NfeStatusServico/NfeStatusServico4.asmx",
            Endpoint.RECEPCAOEVENTO: "/ws/recepcaoevento/recepcaoevento4.asmx",
            Endpoint.NFEAUTORIZACAO: "/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
            Endpoint.NFERETAUTORIZACAO: "/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        },
    },
    "AN": {
        "prod_server": "www.nfe.fazenda.gov.br",
        "dev_server": "hom1.nfe.fazenda.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.RECEPCAOEVENTO: "/NFeRecepcaoEvento4/NFeRecepcaoEvento4.asmx",
            Endpoint.NFEDISTRIBUICAODFE: "/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx",
        },
    },
}
