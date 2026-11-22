# Copyright (C) 2026 - TODAY KMEE

"""Scrape the NFAg webservice addresses from the SVRS DF-e portal.

Run from the repository root: python -m nfelib.nfag.client.v1_0.servers_scraper
"""

from pathlib import Path

from nfelib.utils.servers_scraper import fetch_dfe_portal_servers, save_servers

NFAG_URL = "https://dfe-portal.svrs.rs.gov.br/NFAG/Servicos"
OUTPUT_FILE = Path("nfelib/nfag/client/v1_0/servers.py")
ALIASES: dict[str, str] = {}


def main():
    """Cli entry point."""
    servers, endpoints = fetch_dfe_portal_servers(NFAG_URL, ALIASES)
    if servers:
        save_servers(servers, endpoints, OUTPUT_FILE)


if __name__ == "__main__":
    main()
