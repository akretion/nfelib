# Copyright (C) 2024  Raphaël Valyi - Akretion <raphael.valyi@akretion.com.br>

from __future__ import annotations  # Python 3.8 compat

import logging
from io import StringIO
from pathlib import Path
from typing import Any

import pandas as pd
import requests  # type: ignore[import-untyped]
from bs4 import BeautifulSoup
from xsdata.formats.dataclass.serializers import PycodeSerializer

SERVICE_COLUMN = "Serviço"
URL_COLUMN = "URL"
QRCODE = "qrcode"

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_servers(prod_url: str, dev_url: str) -> tuple[dict[str, Any], dict[str, Any]]:
    """Fetches the NFe server list from the webpage using pandas and BeautifulSoup."""
    servers = {}
    constants = {}  # To store dynamically generated constants

    try:
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
                    # if QRCODE in action.lower():
                    #    continue
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
                "endpoints": action_dict,
            }

        logger.info("Successfully fetched servers.")
        return servers, constants

    except requests.RequestException as e:
        logger.error(f"Failed to fetch servers: {e}")
        return {}, {}
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return {}, {}


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
    endpoints: dict[Endpoint, str]


{formatted_servers}"""

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(content, encoding="utf-8")
    logger.info(f"Servers and constants saved to {output_file}")
