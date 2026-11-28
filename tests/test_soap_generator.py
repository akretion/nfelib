"""Tests for the WSDL/soap generator helpers."""

import logging

from nfelib.utils.soap_generator import (
    generate_soap,
    get_distribuicao_dfe_wsdl_urls,
    get_document_type,
)


def test_distribuicao_dfe_wsdl_urls_are_collected_from_every_server():
    """The DF-e distribution webservices are hosted by the Ambiente Nacional.

    They are missing from the SERVER (SVRS) endpoints the WSDL list is built
    from, so they must be collected from the whole server list.
    """
    servers = {
        "SVRS": {
            "prod_endpoints": {
                "CTeStatusServicoV4": "https://cte.svrs.rs.gov.br/ws/CTeStatusServicoV4/CTeStatusServicoV4.asmx",
            },
            "dev_endpoints": {},
        },
        "AN": {
            "prod_endpoints": {
                "CTeDistribuicaoDFe": "https://www1.cte.fazenda.gov.br/CTeDistribuicaoDFe/CTeDistribuicaoDFe.asmx",
            },
            "dev_endpoints": {
                "CTeDistribuicaoDFe": "https://hom1.cte.fazenda.gov.br/CTeDistribuicaoDFe/CTeDistribuicaoDFe.asmx",
            },
        },
    }

    assert get_distribuicao_dfe_wsdl_urls(servers) == [
        "https://www1.cte.fazenda.gov.br/CTeDistribuicaoDFe/CTeDistribuicaoDFe.asmx"
    ]


def test_distribuicao_dfe_wsdl_urls_are_not_duplicated():
    """The MDF-e distribution lives in the SVRS table, the NF-e one in the AN."""
    nfe_dist_dfe = (
        "https://www1.nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx"
    )
    mdfe_dist_dfe = "https://dfe-portal.svrs.rs.gov.br/Mdfe/MDFeDistribuicaoDFe"
    servers = {
        "SVRS": {
            "prod_endpoints": {"MDFeDistribuicaoDFe": mdfe_dist_dfe},
            "dev_endpoints": {"MDFeDistribuicaoDFe": mdfe_dist_dfe},
        },
        "AN": {
            "prod_endpoints": {"NFeDistribuicaoDFe": nfe_dist_dfe},
            "dev_endpoints": {"NFeDistribuicaoDFe": nfe_dist_dfe},
        },
    }

    assert get_distribuicao_dfe_wsdl_urls(servers) == [mdfe_dist_dfe, nfe_dist_dfe]


def test_document_type_from_url():
    assert (
        get_document_type(
            "https://www1.cte.fazenda.gov.br/CTeDistribuicaoDFe/CTeDistribuicaoDFe.asmx"
        )
        == "cte"
    )
    assert (
        get_document_type(
            "https://www1.nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx"
        )
        == "nfe"
    )
    assert (
        get_document_type("https://dfe-portal.svrs.rs.gov.br/Mdfe/MDFeDistribuicaoDFe")
        == "mdfe"
    )
    assert get_document_type("https://example.com/unknown") is None


def test_generate_soap_keeps_the_document_type_of_urls_that_omit_it(caplog):
    """Not every WSDL URL names its document type.

    The cadconsultacadastro one is hosted by sefazvirtual.rs.gov.br, so the
    document type of the previous URL must be reused instead of dropping it.
    """
    servers = {
        "SVRS": {
            "prod_endpoints": {
                "NfeStatusServico": (
                    "https://nfe.svrs.rs.gov.br/ws/NfeStatusServico/"
                    "NfeStatusServico4.asmx"
                ),
                "NfeConsultaCadastro": (
                    "https://www.sefazvirtual.rs.gov.br/ws/CadConsultaCadastro/"
                    "CadConsultaCadastro4.asmx"
                ),
            },
            "dev_endpoints": {},
        }
    }
    endpoints = {
        "NFESTATUSSERVICO": "NfeStatusServico",
        "NFECONSULTACADASTRO": "NfeConsultaCadastro",
    }

    with caplog.at_level(logging.ERROR):
        generate_soap(servers, endpoints, download=False, generate=False)

    assert "Cannot determine document type" not in caplog.text
