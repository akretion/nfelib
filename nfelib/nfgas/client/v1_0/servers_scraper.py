# Copyright (C) 2026 - TODAY KMEE

"""Scrape the NFGas webservice addresses from the SVRS DF-e portal.

Run from the repository root: python -m nfelib.nfgas.client.v1_0.servers_scraper
"""

from pathlib import Path

from nfelib.utils.servers_scraper import fetch_dfe_portal_servers, save_servers

NFGAS_URL = "https://dfe-portal.svrs.rs.gov.br/NFGAS/Servicos"
OUTPUT_FILE = Path("nfelib/nfgas/client/v1_0/servers.py")
ALIASES: dict[str, str] = {}
# the portal lists the status service as NFGasSatusServico
SERVICE_ALIASES = {"NFGasSatusServico": "NFGasStatusServico"}


def main():
    """Cli entry point."""
    servers, endpoints = fetch_dfe_portal_servers(NFGAS_URL, ALIASES, SERVICE_ALIASES)
    if servers:
        save_servers(servers, endpoints, OUTPUT_FILE)


if __name__ == "__main__":
    main()
