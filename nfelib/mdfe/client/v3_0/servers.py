# Auto-generated file. Do not edit manually.
# ruff: noqa: D101
# ruff: noqa: E501

from __future__ import annotations  # Python 3.8 compat

from enum import Enum
from typing import TypedDict


class Endpoint(Enum):
    MDFERECEPCAOEVENTO = "MDFeRecepcaoEvento"
    MDFECONSULTA = "MDFeConsulta"
    MDFESTATUSSERVICO = "MDFeStatusServico"
    MDFECONSNAOENC = "MDFeConsNaoEnc"
    MDFEDISTRIBUICAODFE = "MDFeDistribuicaoDFe"
    MDFERECEPCAOSINC = "MDFeRecepcaoSinc"
    QRCODE = "QR Code"


class ServerConfig(TypedDict):
    prod_server: str
    dev_server: str
    soap_version: str
    endpoints: dict[Endpoint, str]


servers: dict[str, ServerConfig] = {
    "SVRS": {
        "prod_server": "mdfe.svrs.rs.gov.br",
        "dev_server": "mdfe-homologacao.svrs.rs.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.MDFERECEPCAOEVENTO: "/ws/MDFeRecepcaoEvento/MDFeRecepcaoEvento.asmx",
            Endpoint.MDFECONSULTA: "/ws/MDFeConsulta/MDFeConsulta.asmx",
            Endpoint.MDFESTATUSSERVICO: "/ws/MDFeStatusServico/MDFeStatusServico.asmx",
            Endpoint.MDFECONSNAOENC: "/ws/MDFeConsNaoEnc/MDFeConsNaoEnc.asmx",
            Endpoint.MDFEDISTRIBUICAODFE: "/ws/MDFeDistribuicaoDFe/MDFeDistribuicaoDFe.asmx",
            Endpoint.MDFERECEPCAOSINC: "/ws/MDFeRecepcaoSinc/MDFeRecepcaoSinc.asmx",
            Endpoint.QRCODE: "/mdfe/qrCode",
        },
    },
}
