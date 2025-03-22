import logging
from pathlib import Path
from typing import Dict, Any
from io import StringIO  # Add this import

import pandas as pd
import requests
from bs4 import BeautifulSoup
from xsdata.formats.dataclass.serializers import PycodeSerializer

SERVICE_COLUMN = "Serviço"
URL_COLUMN = "URL"
QRCODE = "qrcode"

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_servers(prod_url: str, dev_url: str) -> Dict[str, Any]:
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
                    if QRCODE in action.lower():
                        continue
                    constant_name = action.upper().replace(" ", "_")
                    constants[constant_name] = action

            paths = ["/" + "/".join(url.split("/")[3:]) for url in urls]
            prod_server = urls[-1].split("/")[2]

            server = servers_list[index]
            action_dict = {
                "prod_server": prod_server,
                "dev_server": dev_servers[server],
            }

            # Use dynamically generated constants as keys
            for action, path in zip(actions, paths):
                if QRCODE in action.lower():
                    continue
                constant_name = action.upper().replace(" ", "_")
                if constant_name in constants:
                    action_dict[constants[constant_name]] = path

            # Handle special case for Ambiente Nacional (AN)
            if server == "AN":
                # Ensure NFeDistribuicaoDFe is included
                if "NFeDistribuicaoDFe" in actions:
                    constant_name = "NFEDISTRIBUICAODFE"
                    if constant_name not in constants:
                        constants[constant_name] = "NFeDistribuicaoDFe"
                    action_dict[constants[constant_name]] = paths[
                        actions.index("NFeDistribuicaoDFe")
                    ]

            servers[server] = action_dict

        logger.info("Successfully fetched servers.")
        return servers, constants

    except requests.RequestException as e:
        logger.error(f"Failed to fetch servers: {e}")
        return {}, {}
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return {}, {}


def save_servers(
    servers: Dict[str, Any], constants: Dict[str, str], output_file: Path
) -> None:
    """Saves the extracted server data and constants as a Python file."""
    # Generate the constants section
    constants_section = "\n".join(
        [f'{key} = "{value}"' for key, value in constants.items()]
    )

    # Use PycodeSerializer to format the servers dictionary
    serializer = PycodeSerializer()
    formatted_servers = serializer.render(servers, var_name="servers")

    # Write the formatted output to the file
    content = f"""# Auto-generated file. Do not edit manually.

# Constants
{constants_section}

# Servers
{formatted_servers}
"""
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(content, encoding="utf-8")
    logger.info(f"Servers and constants saved to {output_file}")
