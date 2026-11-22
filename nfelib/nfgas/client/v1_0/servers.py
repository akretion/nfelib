# Auto-generated file. Do not edit manually.
# ruff: noqa: D101
# ruff: noqa: E501

from __future__ import annotations  # Python 3.8 compat

from enum import Enum
from typing import TypedDict


class Endpoint(Enum):
    NFGASRECEPCAOEVENTO = "NFGasRecepcaoEvento"
    NFGASCONSULTA = "NFGasConsulta"
    NFGASSTATUSSERVICO = "NFGasStatusServico"
    NFGASRECEPCAO = "NFGasRecepcao"
    QRCODE = "QRCode"


class ServerConfig(TypedDict):
    soap_version: str
    prod_endpoints: dict[Endpoint, str]
    dev_endpoints: dict[Endpoint, str]


servers: dict[str, ServerConfig] = {
    "SVRS": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.NFGASRECEPCAOEVENTO: "https://nfgas.svrs.rs.gov.br/WS/NFGasRecepcaoEvento/NFGasRecepcaoEvento.asmx",
            Endpoint.NFGASCONSULTA: "https://nfgas.svrs.rs.gov.br/WS/NFGasConsulta/NFGasConsulta.asmx",
            Endpoint.NFGASSTATUSSERVICO: "https://nfgas.svrs.rs.gov.br/WS/NFGasStatusServico/NFGasStatusServico.asmx",
            Endpoint.NFGASRECEPCAO: "https://nfgas.svrs.rs.gov.br/WS/NFGasRecepcao/NFGasRecepcao.asmx",
            Endpoint.QRCODE: "https://dfe-portal.svrs.rs.gov.br/nfgas/qrCode",
        },
        "dev_endpoints": {
            Endpoint.NFGASCONSULTA: "https://nfgas-homologacao.svrs.rs.gov.br/WS/NFGasConsulta/NFGasConsulta.asmx",
            Endpoint.NFGASRECEPCAO: "https://nfgas-homologacao.svrs.rs.gov.br/WS/NFGasRecepcao/NFGasRecepcao.asmx",
            Endpoint.NFGASSTATUSSERVICO: "https://nfgas-homologacao.svrs.rs.gov.br/WS/NFGasStatusServico/NFGasStatusServico.asmx",
            Endpoint.NFGASRECEPCAOEVENTO: "https://nfgas-homologacao.svrs.rs.gov.br/WS/NFGasRecepcaoEvento/NFGasRecepcaoEvento.asmx",
            Endpoint.QRCODE: "https://dfe-portal.svrs.rs.gov.br/nfgas/qrCode",
        },
    },
}
