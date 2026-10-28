import sys
from pathlib import Path

import pytest

from nfelib.cte.client.v4_0.servers_scraper import main

OUTPUT_FILE = Path("nfelib/cte/client/v4_0/servers.py")


def read_current_servers():
    return OUTPUT_FILE.read_text(encoding="utf-8") if OUTPUT_FILE.exists() else ""


def test_ambiente_nacional_distribuicao_dfe():
    """The CT-e DF-e distribution service must be scraped from the AN table.

    It is published only in the Ambiente Nacional table of the portal, so it
    needs the dedicated handling of the scraper to make it to servers.py.
    """
    from nfelib.cte.client.v4_0.servers import Endpoint, servers

    an_config = servers["AN"]
    assert Endpoint.CTEDISTRIBUICAODFE in an_config["prod_endpoints"]
    assert Endpoint.CTEDISTRIBUICAODFE in an_config["dev_endpoints"]
    assert an_config["prod_endpoints"][Endpoint.CTEDISTRIBUICAODFE].endswith(
        "/CTeDistribuicaoDFe/CTeDistribuicaoDFe.asmx"
    )
    assert an_config["dev_endpoints"][Endpoint.CTEDISTRIBUICAODFE].endswith(
        "/CTeDistribuicaoDFe/CTeDistribuicaoDFe.asmx"
    )
    # the CT-e distribution webservice expects a SOAP 1.2 envelope
    assert an_config["soap_version"] == "1.2"


@pytest.mark.skipif(
    sys.version_info.major != 3 or sys.version_info.minor != 11,
    reason="This test is intended to run only on Python 3.11",
)
def test_scraper():
    old_content = read_current_servers()
    main()
    new_content = read_current_servers()
    assert new_content == old_content, (
        "Server list has changed. Review and commit the new file."
    )
