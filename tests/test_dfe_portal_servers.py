"""Tests for the SVRS DF-e portal server list parser."""

from unittest import mock

from nfelib.utils.servers_scraper import fetch_dfe_portal_servers

PAGE = """<html><body>
<table><caption>SEFAZ Minas Gerais (MG) - Produção</caption>
<tr><th></th><th>Serviço</th><th>Versão</th><th>URL</th><th></th></tr>
<tr><td></td><td>XRecepcao</td><td>1.00</td>
<td>https:// x.mg.gov.br/XRecepcao</td><td></td></tr>
<tr><td></td><td>XSatusServico</td><td>1.00</td>
<td>https://x.mg.gov.br/XStatusServico</td><td></td></tr>
</table>
<table><caption>SEFAZ Minas Gerais (MG) - Homologação</caption>
<tr><th></th><th>Serviço</th><th>Versão</th><th>URL</th><th></th></tr>
<tr><td></td><td>XRecepcao</td><td>1.00</td>
<td>https://hx.mg.gov.br/XRecepcao?wsdl</td><td></td></tr>
</table>
<table><caption>SEFAZ Rio Grande do Sul (RS/SVRS) - Produção</caption>
<tr><th></th><th>Serviço</th><th>Versão</th><th>URL</th><th></th></tr>
<tr><td></td><td>QR Code</td><td></td>
<td>https://x.svrs.rs.gov.br/qrCode</td><td></td></tr>
</table>
<table><caption>Ambiente Nacional - Produção</caption>
<tr><th></th><th>Serviço</th><th>Versão</th><th>URL</th><th></th></tr>
<tr><td></td><td>XRecepcao</td><td>1.00</td>
<td>https://x.an.gov.br/XRecepcao</td><td></td></tr>
</table>
<table><caption>UFs que mais autorizaram DFes.</caption>
<tr><th>#</th><th>UF</th><th>DFes Autorizados</th><th>Referente ao total</th></tr>
<tr><td>1</td><td></td><td>0000</td><td>0%</td></tr>
</table>
</body></html>"""


@mock.patch("nfelib.utils.servers_scraper.requests.get")
def test_fetch_dfe_portal_servers(mock_get):
    mock_get.return_value.content = PAGE.encode()
    servers, endpoints = fetch_dfe_portal_servers(
        "https://dfe-portal.svrs.rs.gov.br/X/Servicos",
        aliases={"RS/SVRS": "SVRS", "Ambiente Nacional": "AN"},
        service_aliases={"XSatusServico": "XStatusServico"},
    )

    assert list(servers) == ["MG", "SVRS", "AN"]
    assert endpoints == {
        "XRECEPCAO": "XRecepcao",
        "XSTATUSSERVICO": "XStatusServico",
        "QR_CODE": "QR Code",
    }
    assert servers["MG"] == {
        "soap_version": "1.2",
        "prod_endpoints": {
            # the space typed in the URL is removed
            "XRecepcao": "https://x.mg.gov.br/XRecepcao",
            "XStatusServico": "https://x.mg.gov.br/XStatusServico",
        },
        "dev_endpoints": {"XRecepcao": "https://hx.mg.gov.br/XRecepcao?wsdl"},
    }
    assert servers["SVRS"]["prod_endpoints"] == {
        "QR Code": "https://x.svrs.rs.gov.br/qrCode"
    }
    assert servers["AN"]["dev_endpoints"] == {}
