# Auto-generated file. Do not edit manually.
# ruff: noqa: D101
# ruff: noqa: E501

from __future__ import annotations  # Python 3.8 compat

from enum import Enum
from typing import TypedDict


class Endpoint(Enum):
    NFAGRECEPCAO = "NFAgRecepcao"
    NFAGRECEPCAOEVENTO = "NFAgRecepcaoEvento"
    NFAGCONSULTA = "NFAgConsulta"
    NFAGSTATUSSERVICO = "NFAgStatusServico"
    QRCODE = "QRCode"


class ServerConfig(TypedDict):
    soap_version: str
    prod_endpoints: dict[Endpoint, str]
    dev_endpoints: dict[Endpoint, str]


servers: dict[str, ServerConfig] = {
    "SVRS": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.NFAGRECEPCAO: "https://nfag.svrs.rs.gov.br/WS/NFAgRecepcao/NFAgRecepcao.asmx",
            Endpoint.NFAGRECEPCAOEVENTO: "https://nfag.svrs.rs.gov.br/WS/NFAgRecepcaoEvento/NFAgRecepcaoEvento.asmx",
            Endpoint.NFAGCONSULTA: "https://nfag.svrs.rs.gov.br/WS/NFAgConsulta/NFAgConsulta.asmx",
            Endpoint.NFAGSTATUSSERVICO: "https://nfag.svrs.rs.gov.br/WS/NFAgStatusServico/NFAgStatusServico.asmx",
            Endpoint.QRCODE: "https://dfe-portal.svrs.rs.gov.br/nfag/qrCode",
        },
        "dev_endpoints": {
            Endpoint.NFAGCONSULTA: "https://nfag-homologacao.svrs.rs.gov.br/WS/NFAgConsulta/NFAgConsulta.asmx",
            Endpoint.NFAGSTATUSSERVICO: "https://nfag-homologacao.svrs.rs.gov.br/WS/NFAgStatusServico/NFAgStatusServico.asmx",
            Endpoint.NFAGRECEPCAO: "https://nfag-homologacao.svrs.rs.gov.br/WS/NFAgRecepcao/NFAgRecepcao.asmx",
            Endpoint.NFAGRECEPCAOEVENTO: "https://nfag-homologacao.svrs.rs.gov.br/WS/NFAgRecepcaoEvento/NFAgRecepcaoEvento.asmx",
            Endpoint.QRCODE: "https://dfe-portal.svrs.rs.gov.br/nfag/qrCode",
        },
    },
}
