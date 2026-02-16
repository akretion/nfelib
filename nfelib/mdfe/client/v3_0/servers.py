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
    soap_version: str
    prod_endpoints: dict[Endpoint, str]
    dev_endpoints: dict[Endpoint, str]


servers: dict[str, ServerConfig] = {
    "SVRS": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.MDFERECEPCAOEVENTO: "https://mdfe.svrs.rs.gov.br/ws/MDFeRecepcaoEvento/MDFeRecepcaoEvento.asmx",
            Endpoint.MDFECONSULTA: "https://mdfe.svrs.rs.gov.br/ws/MDFeConsulta/MDFeConsulta.asmx",
            Endpoint.MDFESTATUSSERVICO: "https://mdfe.svrs.rs.gov.br/ws/MDFeStatusServico/MDFeStatusServico.asmx",
            Endpoint.MDFECONSNAOENC: "https://mdfe.svrs.rs.gov.br/ws/MDFeConsNaoEnc/MDFeConsNaoEnc.asmx",
            Endpoint.MDFEDISTRIBUICAODFE: "https://mdfe.svrs.rs.gov.br/ws/MDFeDistribuicaoDFe/MDFeDistribuicaoDFe.asmx",
            Endpoint.MDFERECEPCAOSINC: "https://mdfe.svrs.rs.gov.br/ws/MDFeRecepcaoSinc/MDFeRecepcaoSinc.asmx",
            Endpoint.QRCODE: "https://dfe-portal.svrs.rs.gov.br/mdfe/qrCode",
        },
        "dev_endpoints": {
            Endpoint.MDFERECEPCAOEVENTO: "https://mdfe-homologacao.svrs.rs.gov.br/ws/MDFeRecepcaoEvento/MDFeRecepcaoEvento.asmx",
            Endpoint.MDFECONSULTA: "https://mdfe-homologacao.svrs.rs.gov.br/ws/MDFeConsulta/MDFeConsulta.asmx",
            Endpoint.MDFESTATUSSERVICO: "https://mdfe-homologacao.svrs.rs.gov.br/ws/MDFeStatusServico/MDFeStatusServico.asmx",
            Endpoint.MDFECONSNAOENC: "https://mdfe-homologacao.svrs.rs.gov.br/ws/MDFeConsNaoEnc/MDFeConsNaoEnc.asmx",
            Endpoint.MDFEDISTRIBUICAODFE: "https://mdfe-homologacao.svrs.rs.gov.br/ws/MDFeDistribuicaoDFe/MDFeDistribuicaoDFe.asmx",
            Endpoint.MDFERECEPCAOSINC: "https://mdfe-homologacao.svrs.rs.gov.br/ws/MDFeRecepcaoSinc/MDFeRecepcaoSinc.asmx",
            Endpoint.QRCODE: "https://dfe-portal.svrs.rs.gov.br/mdfe/qrCode",
        },
    },
}
