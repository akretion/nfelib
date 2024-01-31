import hashlib
import json
import logging
from os import environ, path
from pathlib import Path

import requests
from bs4 import BeautifulSoup

_logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}

PAGES = {
    "nfe": (
        "https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=BMPFMBoln3w=",
        "div",
        "id",
        "conteudoDinamico",
    ),
    #        "nfe_pynfe_webservices": ("https://raw.githubusercontent.com/TadaSoftware/PyNFe/main/pynfe/utils/webservices.py",),
    #        "nfe_pynfe_comunicacao": ("https://raw.githubusercontent.com/TadaSoftware/PyNFe/main/pynfe/processamento/comunicacao.py"),
    "cte": (
        "https://www.cte.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=0xlG1bdBass=",
        "div",
        "id",
        "conteudoDinamico",
    ),
    "nfse": (
        "https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica",
        "div",
        "id",
        "content-core",
    ),
    # TODO MDF-e content seems loaded with XHR
    #        "mdfe": ("https://portal.fazenda.sp.gov.br/servicos/mdfe/Paginas/Downloads.aspx", "div", "class", "content"),
}


def test_fingerprint():
    if environ.get("SKIP_FINGERPRINT"):
        _logger.info("Skipping fingerprint test")
        return True
    fingerprint = {}
    for code, scrap_params in PAGES.items():
        url = scrap_params[0]
        md5 = "ELEMENT NOT FOUND"
        _logger.info("Fetching %s ..." % (url,))
        if len(scrap_params) > 1:
            page = requests.get(url, headers=HEADERS)
            soup = BeautifulSoup(page.text, "html.parser")
            if scrap_params[2] == "id" and soup.find(
                    scrap_params[1], {"id": scrap_params[3]}
                ):
                fragment = soup.find(
                    scrap_params[1], {"id": scrap_params[3]}
                ).text.encode("utf-8")
                md5 = hashlib.md5(fragment).hexdigest()
        else:
            fragment = requests.get(url, headers=HEADERS).content  # .decode('utf-8')
            md5 = hashlib.md5(fragment).hexdigest()
        fingerprint[code] = (url, md5)

    _logger.info(fingerprint)
    json_string = json.dumps(fingerprint, indent=4)
    target = Path("tests/fingerprint.txt").read_text()
    with open("tests/fingerprint.txt", "w") as outfile:
        outfile.write(json_string)
    assert target.strip() == json_string.strip()
