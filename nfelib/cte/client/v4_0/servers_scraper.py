# Copyright (C) 2024  Raphaël Valyi - Akretion <raphael.valyi@akretion.com.br>

import sys
from pathlib import Path

from nfelib.utils.servers_scraper import fetch_servers, save_servers
from nfelib.utils.soap_generator import generate_soap

# Constants
PROD_URL = "https://www.cte.fazenda.gov.br/portal/webServices.aspx"
DEV_URL = "https://hom.cte.fazenda.gov.br/portal/webServices.aspx"
OUTPUT_FILE = Path("nfelib/cte/client/v4_0/servers.py")


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

    servers, endpoints = fetch_servers(PROD_URL, DEV_URL)
    if servers:
        save_servers(servers, endpoints, OUTPUT_FILE)
        generate_soap(servers, endpoints, download, generate)


if __name__ == "__main__":
    main()
