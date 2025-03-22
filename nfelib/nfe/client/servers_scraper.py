import pandas as pd
import requests
from io import StringIO
from pathlib import Path

import logging
import os
import time
from os import environ
from xsdata.formats.dataclass.serializers import PycodeSerializer
from unittest import TestCase
from bs4 import BeautifulSoup
from pprint import pp
import requests
import pandas as pd

PROD_URL = "https://hom.nfe.fazenda.gov.br/portal/webServices.aspx"
DEV_URL = "https://hom.nfe.fazenda.gov.br/portal/webServices.aspx"

OUTPUT_FILE = Path("nfelib/nfe/client/servers.py")


def fetch_servers(prod_url: str, dev_url: str) -> dict:
    """Fetches the NFe server list from the webpage using pandas."""
    constants = ""
    servers_list = []
    servers = {}

    prod_response = requests.get(prod_url)
    soup = BeautifulSoup(prod_response.content, 'lxml')
    captions = soup.find_all('caption')

    servers_list = []
    for caption in captions:
        if "(" not in str(caption):
            continue
        servers_list.append(str(caption).split("(")[1].split(")")[0])

    dev_response = requests.get(dev_url)
    tables = pd.read_html(dev_response.content.decode(dev_response.apparent_encoding))
    dev_servers = {}
    for index, table in enumerate(list(tables)):
        if list(table.to_dict().keys())[0] != "Serviço":
            continue
        urls = list(dict(table.to_dict())["URL"].values())
        dev_server = urls[-1].split("/")[2]
        server = servers_list[index]
        dev_servers[server] = dev_server

    #response = requests.get("https://www.cte.fazenda.gov.br/portal/webServices.aspx?tipoConteudo=wpdBtfbTMrw=")

    tables = pd.read_html(prod_response.content.decode(prod_response.apparent_encoding))
    for index, table in enumerate(list(tables)):
        if list(table.to_dict().keys())[0] != "Serviço":
            continue
        actions = list(dict(table.to_dict())["Serviço"].values())
        urls = list(dict(table.to_dict())["URL"].values())

        if index == 0:
            for action in actions:
                if "qrcode" in action.lower():
                    continue
                constants += f'{action.upper()} = "{action}"\n'
        paths = ["/" + "/".join(url.split("/")[3:]) for url in urls]
        prod_server = urls[-1].split("/")[2]

        server = servers_list[index]
        action_dict = {"prod_server": prod_server, "dev_server": dev_servers[server]}
        for index, action in enumerate(actions):
            if "qrcode" in action.lower():
                continue
            action_dict[action] = paths[index]

        servers[server] = action_dict

    print("\n")

    serializer = PycodeSerializer()
    servers = serializer.render(servers, var_name="servers")
    print(constants)
    print(servers)
    return servers


def save_servers(servers: dict, output_file: Path) -> None:
    """Saves the extracted server data as a Python dictionary."""
    content = f"# Auto-generated file. Do not edit manually.\nservers = {servers}\n"
    output_file.write_text(content, encoding="utf-8")


def main():
    servers = fetch_servers(PROD_URL, DEV_URL)
    save_servers(servers, OUTPUT_FILE)


if __name__ == "__main__":
    main()

