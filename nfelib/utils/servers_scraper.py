# Copyright (C) 2024  Raphaël Valyi - Akretion <raphael.valyi@akretion.com.br>

from __future__ import annotations  # Python 3.8 compat

import logging
import sys
from io import StringIO
from os import environ
from pathlib import Path
from typing import Any

import pandas as pd
import requests  # type: ignore[import-untyped]
from brazil_fiscal_client.fiscal_client import FiscalClient, Tamb, TcodUfIbge
from bs4 import BeautifulSoup
from xsdata.formats.dataclass.serializers import PycodeSerializer

if sys.version_info[:2] > (3, 8):
    from nfelib.cte.bindings.v4_0.cons_stat_serv_tipos_basico_v4_00 import TconsStatServ
    from nfelib.cte.soap.v4_0.ctestatusservicov4 import (
        CteStatusServicoV4Soap12CteStatusServicoCt,
    )
    from nfelib.nfe.bindings.v4_0.cons_stat_serv_v4_00 import ConsStatServ
    from nfelib.nfe.bindings.v4_0.leiaute_cons_stat_serv_v4_00 import (
        TconsStatServXServ,
    )
    from nfelib.nfe.soap.v4_0.nfestatusservico4 import (
        NfeStatusServico4SoapNfeStatusServicoNf,
    )

SERVICE_COLUMN = "Serviço"
URL_COLUMN = "URL"

# here we manually maintain a list of servers requiring SOAP 1.2 headers
# when we detect new ones with SOAP 1.2 detection feature in the end
# of the file. Thus we don't always need to export a proper CERT_FILE env var
# to scrap the server URLs.
FORCE_SOAP_12_NFE = {"SVC-RS", "SVC-AN", "SP", "PR"}
FORCE_SOAP_12_CTE = {"SVSP", "RS", "SVRS", "MG", "SP", "PR"}

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_servers(prod_url: str, dev_url: str) -> tuple[dict[str, Any], dict[str, Any]]:
    """Fetches the NFe server list from the webpage using pandas and BeautifulSoup."""
    servers = {}
    constants = {}  # To store dynamically generated constants
    force_soap_12 = FORCE_SOAP_12_NFE if "nfe" in prod_url else FORCE_SOAP_12_CTE
    status_key = "NfeStatusServico" if "nfe" in prod_url else "CteStatusServicoV4"

    # Fetch production servers
    prod_response = requests.get(prod_url)
    prod_response.raise_for_status()
    soup = BeautifulSoup(prod_response.content, "lxml")
    captions = soup.find_all("caption")

    servers_list = [
        str(caption).split("(")[1].split(")")[0]
        for caption in captions
        if "(" in str(caption)
    ]

    # Fetch development servers
    dev_response = requests.get(dev_url)
    dev_response.raise_for_status()
    dev_html = dev_response.content.decode(dev_response.apparent_encoding)
    dev_tables = pd.read_html(StringIO(dev_html))  # Wrap HTML in StringIO

    dev_servers = {
        servers_list[index]: urls[-1].split("/")[2]
        for index, table in enumerate(dev_tables)
        if SERVICE_COLUMN in table.columns
        for urls in [list(table.to_dict()[URL_COLUMN].values())]
    }

    # Fetch production server details and generate constants
    prod_html = prod_response.content.decode(prod_response.apparent_encoding)
    prod_tables = pd.read_html(StringIO(prod_html))  # Wrap HTML in StringIO

    for index, table in enumerate(prod_tables):
        if SERVICE_COLUMN not in table.columns or URL_COLUMN not in table.columns:
            logger.warning(f"Skipping table {index}: missing required columns.")
            continue

        actions = list(dict(table.to_dict())[SERVICE_COLUMN].values())
        urls = list(dict(table.to_dict())[URL_COLUMN].values())

        # Generate constants from the first table
        if index == 0:
            for action in actions:
                constant_name = action.upper().replace(" ", "_")
                constants[constant_name] = action

        paths = ["/" + "/".join(url.split("/")[3:]) for url in urls]
        prod_server = urls[-1].split("/")[2]

        server = servers_list[index]
        action_dict = {}

        # Use dynamically generated constants as keys
        for action, path in zip(actions, paths):
            # if QRCODE in action.lower():
            #    continue
            constant_name = action.upper().replace(" ", "_")
            if constant_name in constants:
                action_dict[constants[constant_name]] = path

        # Handle special case for Ambiente Nacional (AN)
        if server == "AN" and "NFeDistribuicaoDFe" in actions:
            constant_name = "NFEDISTRIBUICAODFE"
            if constant_name not in constants:
                constants[constant_name] = "NFeDistribuicaoDFe"
            action_dict[constants[constant_name]] = paths[
                actions.index("NFeDistribuicaoDFe")
            ]

        servers[server] = {
            "prod_server": prod_server,
            "dev_server": dev_servers[server],
            "soap_version": "1.2" if server in force_soap_12 else "1.1",
            "endpoints": action_dict,
        }

    logger.info("Successfully fetched servers.")

    if environ.get("CERT_FILE") and sys.version_info[:2] > (3, 8):
        logger.info("\nNow, let's test if some servers require SOAP 1.2 headers...")
        soap_12_servers = force_soap_12

        cert_path = Path(environ["CERT_FILE"])
        if not cert_path.is_file():
            raise FileNotFoundError(f"Certificate file not found: {cert_path}")
        with open(cert_path, "rb") as pkcs12_file:
            cert_data = pkcs12_file.read()

        for server, server_config in servers.items():
            if hasattr(TcodUfIbge, server):
                uf = getattr(TcodUfIbge, server)
            else:
                uf = {
                    "SVRS": TcodUfIbge.SC,
                    "AN": TcodUfIbge.PR,
                    "SVAN": TcodUfIbge.MA,
                    "SVC-AN": TcodUfIbge.RJ,
                    "SVC-RS": TcodUfIbge.MA,
                    "SVSP": TcodUfIbge.SP,
                }[server]

            if not server_config["endpoints"].get(status_key):
                continue

            logger.info(f"\n\nTesting SOAP version for {server} - {uf} {uf.value}")

            client = FiscalClient(
                uf=uf.value,
                ambiente="2",
                versao="4.00",
                pkcs12_data=cert_data,
                pkcs12_password=environ.get("CERT_PASSWORD"),
                soap12_envelope=server_config["soap_version"] == "1.2",
            )

            try:
                if "nfe" in prod_url:
                    client.send(
                        NfeStatusServico4SoapNfeStatusServicoNf,
                        f"https://{server_config['dev_server']}{server_config['endpoints'][status_key]}",
                        {
                            "Body": {
                                "nfeDadosMsg": {
                                    "content": [
                                        ConsStatServ(
                                            tpAmb=Tamb.DEV,
                                            cUF=uf.value,
                                            xServ=TconsStatServXServ.STATUS,
                                            versao="4.00",
                                        )
                                    ]
                                }
                            },
                        },
                        raise_on_soap_mismatch=True,
                    )

                elif "cte" in prod_url:
                    client.send(
                        CteStatusServicoV4Soap12CteStatusServicoCt,
                        f"https://{server_config['dev_server']}{server_config['endpoints'][status_key]}",
                        {
                            "Body": {
                                "cteDadosMsg": {
                                    "content": [
                                        TconsStatServ(
                                            tpAmb=Tamb.DEV,
                                            cUF=uf.value,
                                            versao="4.00",
                                        )
                                    ]
                                }
                            },
                        },
                        raise_on_soap_mismatch=True,
                    )
            except Exception as e:
                if "Envelope" in str(e):
                    logger.error(
                        f"\nAn unexpected SOAP VERSION MISMATCH error occurred: {e}"
                    )
                    server_config["soap_version"] = "1.2"
                    soap_12_servers.add(server)
                else:
                    logger.error(f"\nAn unexpected error occurred: {e}")

    if environ.get("CERT_FILE"):
        logger.info(f"sniffed 1.2 headers for {soap_12_servers}")
    return servers, constants


def save_servers(
    servers: dict[str, Any], endpoints: dict[str, str], output_file: Path
) -> None:
    """Saves the extracted server data and constants as a Python file."""
    # Generate the constants section
    actions = "\n".join([f'    {key} = "{value}"' for key, value in endpoints.items()])

    # Use PycodeSerializer to format the servers dictionary
    serializer = PycodeSerializer()
    formatted_servers = "\n".join(
        serializer.render(servers, var_name="servers").replace("'", '"').split("\n")[2:]
    )
    for key, value in endpoints.items():
        formatted_servers = formatted_servers.replace(f'"{value}"', f"Endpoint.{key}")
    formatted_servers = formatted_servers.replace(
        "servers =", "servers: dict[str, ServerConfig] ="
    )

    # Write the formatted output to the file
    content = f"""# Auto-generated file. Do not edit manually.
# ruff: noqa: D101
# ruff: noqa: E501

from __future__ import annotations  # Python 3.8 compat

from enum import Enum
from typing import TypedDict


class Endpoint(Enum):
{actions}


class ServerConfig(TypedDict):
    prod_server: str
    dev_server: str
    soap_version: str
    endpoints: dict[Endpoint, str]


{formatted_servers}"""

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(content, encoding="utf-8")
    logger.info(f"Servers and constants saved to {output_file}")
