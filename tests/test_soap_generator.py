"""Tests for the WSDL/soap generator helpers."""

from nfelib.utils.soap_generator import (
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
