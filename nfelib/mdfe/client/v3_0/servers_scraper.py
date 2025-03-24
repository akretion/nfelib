# Copyright (C) 2024  Raphaël Valyi - Akretion <raphael.valyi@akretion.com.br>

from __future__ import annotations  # Python 3.8 compat

import logging
from pathlib import Path
from typing import Any

import requests
from bs4 import BeautifulSoup
from xsdata.formats.dataclass.serializers import PycodeSerializer

# Constants
MDFE_SVRS_URL = "https://dfe-portal.svrs.rs.gov.br/Mdfe/Servicos"
OUTPUT_FILE = Path("nfelib/nfe/client/servers_mdfe.py")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_mdfe_servers(url: str) -> dict[Any, Any]:
    """Fetches the MDFe server actions for production and homologation."""
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.content, "lxml")

        # Initialize dictionaries to store server actions
        servers: dict[Any, Any] = {
            "SVRS": {
                "prod_server": "mdfe.svrs.rs.gov.br",
                "dev_server": "mdfe-homologacao.svrs.rs.gov.br",
                "services": {},
            }
        }

        # Find all tables with server information
        tables = soup.find_all("table")
        for table in tables:
            # Determine if the table is for production or homologation
            caption = table.find("caption")
            if not caption:
                continue

            if "Produção" in caption.text:
                environment = "prod"
            elif "Homologação" in caption.text:
                environment = "dev"
            else:
                continue

            # Extract server actions from the table
            rows = table.find_all("tr")[1:]  # Skip the header row
            for row in rows:
                cols = row.find_all("td")
                if len(cols) < 4:  # Ensure there are enough columns
                    continue

                service_name = cols[1].text.strip()
                service_url = cols[3].text.strip()

                # Add the service to the servers dictionary
                if service_name not in servers["SVRS"]["services"]:
                    servers["SVRS"]["services"][service_name] = {}

                servers["SVRS"]["services"][service_name][environment] = "/" + "/".join(
                    service_url.split("/")[3:]
                )

        logger.info("Successfully fetched MDFe servers.")
        return servers

    except requests.RequestException as e:
        logger.error(f"Failed to fetch MDFe servers: {e}")
        return {}
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return {}


def save_servers(servers: dict[str, Any], output_file: Path) -> None:
    """Saves the extracted server data and constants as a Python file."""
    # Generate the constants section
    constants = {
        "MDFERECEPCAOEVENTO": "MDFeRecepcaoEvento",
        "MDFECONSULTA": "MDFeConsulta",
        "MDFESTATUSSERVICO": "MDFeStatusServico",
        "MDFECONSNAOENC": "MDFeConsNaoEnc",
        "MDFEDISTRIBUICAODFE": "MDFeDistribuicaoDFe",
        "MDFERECEPCAOSINC": "MDFeRecepcaoSinc",
        "QRCODE": "QR Code",
    }
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
    logger.info(f"MDFe servers and constants saved to {output_file}")


def main():
    """Cli entry point."""
    # Fetch the MDFe server actions
    servers = fetch_mdfe_servers(MDFE_SVRS_URL)

    # Save the results to a file
    if servers:
        save_servers(servers, OUTPUT_FILE)


if __name__ == "__main__":
    main()
