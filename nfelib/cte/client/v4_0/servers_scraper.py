from pathlib import Path

from nfelib.utils.servers_scraper import fetch_servers, save_servers

# Constants
PROD_URL = "https://www.cte.fazenda.gov.br/portal/webServices.aspx"
DEV_URL = "https://hom.cte.fazenda.gov.br/portal/webServices.aspx"
OUTPUT_FILE = Path("nfelib/cte/client/servers.py")


def main():
    """Cli entry point."""
    servers, constants = fetch_servers(PROD_URL, DEV_URL)
    if servers:
        save_servers(servers, constants, OUTPUT_FILE)


if __name__ == "__main__":
    main()
