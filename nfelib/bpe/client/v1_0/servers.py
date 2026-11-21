# Auto-generated file. Do not edit manually.
# ruff: noqa: D101
# ruff: noqa: E501

from __future__ import annotations  # Python 3.8 compat

from enum import Enum
from typing import TypedDict


class Endpoint(Enum):
    BPERECEPCAO = "BPeRecepcao"
    BPERECEPCAOEVENTO = "BPeRecepcaoEvento"
    BPECONSULTA = "BPeConsulta"
    BPESTATUSSERVICO = "BPeStatusServico"
    QRCODE = "QRCode"
    BPERECEPCAOTM = "BPeRecepcaoTM"
    QR_CODE = "QR Code"
    BPERECEPCAOTA = "BPeRecepcaoTA"


class ServerConfig(TypedDict):
    soap_version: str
    prod_endpoints: dict[Endpoint, str]
    dev_endpoints: dict[Endpoint, str]


servers: dict[str, ServerConfig] = {
    "MG": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.BPERECEPCAO: "https://bpe.fazenda.mg.gov.br/bpe/services/BPeRecepcao",
            Endpoint.BPERECEPCAOEVENTO: "https://bpe.fazenda.mg.gov.br/bpe/services/BPeRecepcaoEvento",
            Endpoint.BPECONSULTA: "https://bpe.fazenda.mg.gov.br/bpe/services/BPeConsulta",
            Endpoint.BPESTATUSSERVICO: "https://bpe.fazenda.mg.gov.br/bpe/services/BPeStatusServico",
            Endpoint.QRCODE: "https://portalbpe.fazenda.mg.gov.br/portalbpe/sistema/qrcode.xhtml",
            Endpoint.BPERECEPCAOTM: "https://bpe.fazenda.mg.gov.br/bpe/services/BPeRecepcaoTM",
        },
        "dev_endpoints": {
            Endpoint.BPERECEPCAO: "https://hbpe.fazenda.mg.gov.br/bpe/services/BPeRecepcao",
            Endpoint.BPERECEPCAOEVENTO: "https://hbpe.fazenda.mg.gov.br/bpe/services/BPeRecepcaoEvento",
            Endpoint.BPECONSULTA: "https://bpe.fazenda.mg.gov.br/bpe/services/BPeConsulta",
            Endpoint.BPESTATUSSERVICO: "https://hbpe.fazenda.mg.gov.br/bpe/services/BPeConsulta",
            Endpoint.QRCODE: "https://portalbpe.fazenda.mg.gov.br/portalbpe/sistema/qrcode.xhtml",
            Endpoint.BPERECEPCAOTM: "https://hbpe.fazenda.mg.gov.br/bpe/services/BPeRecepcaoTM",
        },
    },
    "MS": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.BPERECEPCAO: "https://bpe.fazenda.ms.gov.br/ws/BPeRecepcao",
            Endpoint.BPERECEPCAOEVENTO: "https://bpe.fazenda.ms.gov.br/ws/BPeRecepcaoEvento",
            Endpoint.BPECONSULTA: "https://bpe.fazenda.ms.gov.br/ws/BPeConsulta",
            Endpoint.BPESTATUSSERVICO: "https://bpe.fazenda.ms.gov.br/ws/BPeStatusServico",
            Endpoint.QRCODE: "http://www.dfe.ms.gov.br/bpe/qrcode",
        },
        "dev_endpoints": {
            Endpoint.BPERECEPCAO: "https://homologacao.bpe.ms.gov.br/ws/BPeRecepcao",
            Endpoint.BPERECEPCAOEVENTO: "https://homologacao.bpe.ms.gov.br/ws/BPeRecepcaoEvento",
            Endpoint.BPECONSULTA: "https://bpe.fazenda.mg.gov.br/bpe/services/BPeConsulta",
            Endpoint.BPESTATUSSERVICO: "https://homologacao.bpe.ms.gov.br/ws/BPeStatusServico",
            Endpoint.QRCODE: "http://www.dfe.ms.gov.br/bpe/qrcode",
        },
    },
    "MT": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.BPERECEPCAO: "https://www.sefaz.mt.gov.br/bpe-ws/services/BPeRecepcao",
            Endpoint.BPESTATUSSERVICO: "https://www.sefaz.mt.gov.br/bpe-ws/services/BPeStatusServico",
            Endpoint.BPECONSULTA: "https://www.sefaz.mt.gov.br/bpe-ws/services/BPeConsulta",
            Endpoint.BPERECEPCAOEVENTO: "https://www.sefaz.mt.gov.br/bpe-ws/services/BPeRecepcaoEvento",
            Endpoint.QR_CODE: "https://www.sefaz.mt.gov.br/BPe/qrcode",
        },
        "dev_endpoints": {
            Endpoint.BPERECEPCAO: "https://homologacao.sefaz.mt.gov.br/bpe-ws/services/BPeRecepcao",
            Endpoint.BPECONSULTA: "https://homologacao.sefaz.mt.gov.br/bpe-ws/services/BPeConsulta",
            Endpoint.BPESTATUSSERVICO: "https://homologacao.sefaz.mt.gov.br/bpe-ws/services/BPeStatusServico",
            Endpoint.BPERECEPCAOEVENTO: "https://homologacao.sefaz.mt.gov.br/bpe-ws/services/BPeRecepcaoEvento",
            Endpoint.QR_CODE: "https://homologacao.sefaz.mt.gov.br/BPe/qrcode",
        },
    },
    "PR": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.BPERECEPCAO: "https://bpe.fazenda.pr.gov.br/bpe/BPeRecepcao",
            Endpoint.BPERECEPCAOEVENTO: "https://bpe.fazenda.pr.gov.br/bpe/BPeRecepcaoEvento",
            Endpoint.BPECONSULTA: "https://bpe.fazenda.pr.gov.br/bpe/BPeConsulta",
            Endpoint.BPESTATUSSERVICO: "https://bpe.fazenda.pr.gov.br/bpe/BPeStatusServico",
            Endpoint.QRCODE: "https://www.fazenda.pr.gov.br/bpe/qrcode",
        },
        "dev_endpoints": {
            Endpoint.BPERECEPCAO: "https://homologacao.bpe.fazenda.pr.gov.br/bpe/BPeRecepcao",
            Endpoint.BPERECEPCAOEVENTO: "https://homologacao.bpe.fazenda.pr.gov.br/bpe/BPeRecepcaoEvento",
            Endpoint.BPECONSULTA: "https://homologacao.bpe.fazenda.pr.gov.br/bpe/BPeConsulta",
            Endpoint.BPESTATUSSERVICO: "https://homologacao.bpe.fazenda.pr.gov.br/bpe/BPeStatusServico",
            Endpoint.QRCODE: "https://www.fazenda.pr.gov.br/bpe/qrcode",
        },
    },
    "SP": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.BPERECEPCAO: "https://bpe.fazenda.sp.gov.br/BPeWeb/services/BPeRecepcao.asmx",
            Endpoint.BPECONSULTA: "https://bpe.fazenda.sp.gov.br/BPeWeb/services/BPeConsulta.asmx",
            Endpoint.BPERECEPCAOEVENTO: "https://bpe.fazenda.sp.gov.br/BPeWeb/services/BPeRecepcaoEvento.asmx",
            Endpoint.BPESTATUSSERVICO: "https://bpe.fazenda.sp.gov.br/BPeWeb/services/BPeStatusServico.asmx",
            Endpoint.QR_CODE: "https://bpe.fazenda.sp.gov.br/BPe/qrcode",
        },
        "dev_endpoints": {
            Endpoint.BPERECEPCAO: "https://homologacao.bpe.fazenda.sp.gov.br/BPeWeb/services/BPeRecepcao.asmx",
            Endpoint.BPECONSULTA: "https://homologacao.bpe.fazenda.sp.gov.br/BPeWeb/services/BPeConsulta.asmx",
            Endpoint.BPERECEPCAOEVENTO: "https://homologacao.bpe.fazenda.sp.gov.br/BPeWeb/services/BPeRecepcaoEvento.asmx",
            Endpoint.BPESTATUSSERVICO: "https://homologacao.bpe.fazenda.sp.gov.br/BPeWeb/services/BPeStatusServico.asmx",
            Endpoint.QR_CODE: "https://homologacao.bpe.fazenda.sp.gov.br/BPe/qrcode",
        },
    },
    "SVRS": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.BPERECEPCAO: "https://bpe.svrs.rs.gov.br/ws/bpeRecepcao/bpeRecepcao.asmx",
            Endpoint.BPERECEPCAOEVENTO: "https://bpe.svrs.rs.gov.br/ws/bpeRecepcaoEvento/bpeRecepcaoEvento.asmx",
            Endpoint.BPECONSULTA: "https://bpe.svrs.rs.gov.br/ws/bpeConsulta/bpeConsulta.asmx",
            Endpoint.BPESTATUSSERVICO: "https://bpe.svrs.rs.gov.br/ws/bpeStatusServico/bpeStatusServico.asmx",
            Endpoint.QRCODE: "https://dfe-portal.svrs.rs.gov.br/bpe/qrCode",
            Endpoint.BPERECEPCAOTM: "https://bpe.svrs.rs.gov.br/ws/bpeRecepcaoTM/bpeRecepcaoTM.asmx",
            Endpoint.BPERECEPCAOTA: "https://bpe.svrs.rs.gov.br/WS/BPeRecepcaoTA/BPeRecepcaoTA.asmx",
        },
        "dev_endpoints": {
            Endpoint.BPERECEPCAO: "https://bpe-homologacao.svrs.rs.gov.br/ws/bpeRecepcao/bpeRecepcao.asmx",
            Endpoint.BPERECEPCAOEVENTO: "https://bpe-homologacao.svrs.rs.gov.br/ws/bpeRecepcaoEvento/bpeRecepcaoEvento.asmx",
            Endpoint.BPECONSULTA: "https://bpe-homologacao.svrs.rs.gov.br/ws/bpeConsulta/bpeConsulta.asmx",
            Endpoint.BPESTATUSSERVICO: "https://bpe-homologacao.svrs.rs.gov.br/ws/bpeStatusServico/bpeStatusServico.asmx",
            Endpoint.QRCODE: "https://dfe-portal.svrs.rs.gov.br/bpe/qrCode",
            Endpoint.BPERECEPCAOTM: "https://bpe-homologacao.svrs.rs.gov.br/ws/bpeRecepcaoTM/bpeRecepcaoTM.asmx",
            Endpoint.BPERECEPCAOTA: "https://bpe-homologacao.svrs.rs.gov.br/WS/BPeRecepcaoTA/BPeRecepcaoTA.asmx",
        },
    },
    "PB": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.QR_CODE: "http://www.receita.pb.gov.br/bpe/qrCode",
        },
        "dev_endpoints": {
            Endpoint.QR_CODE: "http://www.receita.pb.gov.br/bpe/qrCode",
        },
    },
}
