# Copyright (C) 2026 - TODAY KMEE

"""Scrape the DC-e webservice addresses from the SVRS DF-e portal.

Run from the repository root: python -m nfelib.dce.client.v1_0.servers_scraper
"""

from pathlib import Path

from nfelib.utils.servers_scraper import fetch_dfe_portal_servers, save_servers

DCE_URL = "https://dfe-portal.svrs.rs.gov.br/DCE/Servicos"
OUTPUT_FILE = Path("nfelib/dce/client/v1_0/servers.py")
ALIASES = {"Ambiente Nacional da DCe": "AN"}


def main():
    """Cli entry point."""
    servers, endpoints = fetch_dfe_portal_servers(DCE_URL, ALIASES)
    if servers:
        save_servers(servers, endpoints, OUTPUT_FILE)


if __name__ == "__main__":
    main()
