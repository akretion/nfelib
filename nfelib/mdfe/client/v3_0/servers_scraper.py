# Copyright (C) 2024  Raphaël Valyi - Akretion <raphael.valyi@akretion.com.br>

from __future__ import annotations  # Python 3.8 compat

import logging
import sys
from pathlib import Path
from typing import Any

import requests  # type: ignore[import-untyped]
from bs4 import BeautifulSoup

from nfelib.utils.servers_scraper import save_servers
from nfelib.utils.soap_generator import generate_soap

# Constants
MDFE_SVRS_URL = "https://dfe-portal.svrs.rs.gov.br/Mdfe/Servicos"
OUTPUT_FILE = Path("nfelib/mdfe/client/v3_0/servers.py")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_mdfe_servers(url: str) -> dict[Any, Any]:
    """Fetches the MDFe server actions for production and homologation."""
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
            "soap_version": "1.1",
            "endpoints": {},
        }
    }

    # Find all tables with server information
    tables = soup.find_all("table")
    for table in tables:
        # Determine if the table is for production or homologation
        caption = table.find("caption")
        if not caption:
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
            if service_name not in servers["SVRS"]["endpoints"]:
                servers["SVRS"]["endpoints"][service_name] = {}

            servers["SVRS"]["endpoints"][service_name] = "/" + "/".join(
                service_url.split("/")[3:]
            )

    logger.info("Successfully fetched MDFe servers.")
    return servers


def main():
    """Cli entry point."""
    download = False
    if "--download" in sys.argv:
        download = True
        sys.argv.remove(
            "--download"
        )  # Remove the --download flag to avoid interfering with argparse

    generate = False
    if "--generate" in sys.argv:
        generate = True
        sys.argv.remove(
            "--generate"
        )  # Remove the --generate flag to avoid interfering with argparse

    # Fetch the MDFe server actions
    servers = fetch_mdfe_servers(MDFE_SVRS_URL)
    endpoints = {
        "MDFERECEPCAOEVENTO": "MDFeRecepcaoEvento",
        "MDFECONSULTA": "MDFeConsulta",
        "MDFESTATUSSERVICO": "MDFeStatusServico",
        "MDFECONSNAOENC": "MDFeConsNaoEnc",
        "MDFEDISTRIBUICAODFE": "MDFeDistribuicaoDFe",
        "MDFERECEPCAOSINC": "MDFeRecepcaoSinc",
        "QRCODE": "QR Code",
    }

    # Save the results to a file
    if servers:
        save_servers(servers, endpoints, OUTPUT_FILE)
        generate_soap(servers, endpoints, download, generate)


if __name__ == "__main__":
    main()
