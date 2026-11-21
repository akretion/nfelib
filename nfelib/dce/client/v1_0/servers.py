# Auto-generated file. Do not edit manually.
# ruff: noqa: D101
# ruff: noqa: E501

from __future__ import annotations  # Python 3.8 compat

from enum import Enum
from typing import TypedDict


class Endpoint(Enum):
    DCESTATUSSERVICO = "DCeStatusServico"
    DCEAUTORIZACAO = "DCeAutorizacao"
    DCECONSULTA = "DCeConsulta"
    DCERECEPCAOEVENTO = "DCeRecepcaoEvento"
    QRCODE = "QRCode"


class ServerConfig(TypedDict):
    soap_version: str
    prod_endpoints: dict[Endpoint, str]
    dev_endpoints: dict[Endpoint, str]


servers: dict[str, ServerConfig] = {
    "AN": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.DCESTATUSSERVICO: "https://dce.fazenda.pr.gov.br/dce/DCeStatusServico?wsdl",
            Endpoint.DCEAUTORIZACAO: "https://dce.fazenda.pr.gov.br/dce/DCeAutorizacao?wsdl",
            Endpoint.DCECONSULTA: "https://dce.fazenda.pr.gov.br/dce/DCeConsulta?wsdl",
            Endpoint.DCERECEPCAOEVENTO: "https://dce.fazenda.pr.gov.br/dce/DCeRecepcaoEvento?wsdl",
            Endpoint.QRCODE: "https://www.fazenda.pr.gov.br/dce/qrcode",
        },
        "dev_endpoints": {
            Endpoint.DCESTATUSSERVICO: "https://homologacao.dce.fazenda.pr.gov.br/dce/DCeStatusServico?wsdl",
            Endpoint.DCEAUTORIZACAO: "https://homologacao.dce.fazenda.pr.gov.br/dce/DCeAutorizacao?wsdl",
            Endpoint.DCECONSULTA: "https://homologacao.dce.fazenda.pr.gov.br/dce/DCeConsulta?wsdl",
            Endpoint.DCERECEPCAOEVENTO: "https://homologacao.dce.fazenda.pr.gov.br/dce/DCeRecepcaoEvento?wsdl",
            Endpoint.QRCODE: "https://www.fazenda.pr.gov.br/dce/qrcode",
        },
    },
}
