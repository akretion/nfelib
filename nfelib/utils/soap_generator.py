# Copyright (C) 2024  Raphaël Valyi - Akretion <raphael.valyi@akretion.com.br>

from __future__ import annotations  # Python 3.8 compat

import logging
import os
import re
import subprocess
from os import environ
from typing import Any

import urllib3
from requests import Session  # type: ignore[import-untyped]
from requests_pkcs12 import Pkcs12Adapter  # type: ignore[import-untyped]

# Configure logging
_logger = logging.getLogger(__name__)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Constants
SERVER = "SVRS"
WSDL_DIRS = {
    "nfe": ("nfelib/nfe/wsdl/v4_0", "nfe"),
    "mdfe": ("nfelib/mdfe/wsdl/v3_0", "mdfe"),
    "cte": ("nfelib/cte/wsdl/v4_0", "cte"),
    "bpe": ("nfelib/bpe/wsdl/v1_0", "bpe"),
}

# The DF-e distribution webservices (NFeDistribuicaoDFe, CTeDistribuicaoDFe...)
DISTRIBUICAO_DFE = re.compile(r"distribuicaodfe", re.IGNORECASE)


def get_distribuicao_dfe_wsdl_urls(servers: dict[str, Any]) -> list[str]:
    """Collect the WSDL URLs of the DF-e distribution webservices.

    Those webservices are hosted by the Ambiente Nacional (AN), not by the
    SVRS server the other endpoints are read from, so they must be picked up
    from the whole server list.
    """
    urls: list[str] = []
    for server_config in servers.values():
        for name, url in server_config.get("prod_endpoints", {}).items():
            if DISTRIBUICAO_DFE.search(str(name)) and url not in urls:
                urls.append(url)
    return urls


def get_document_type(url: str) -> str | None:
    """Identify the document type (NF-e, CT-e, MDF-e, BP-e) from its URL."""
    for key in WSDL_DIRS:
        if key in url.lower():
            return key
    return None


def generate_soap(
    servers: dict[str, Any],
    endpoints: dict[str, str],
    download: bool = False,
    generate: bool = False,
) -> None:
    """Download WSDL files for NF-e, CT-e, MDF-e, and BP-e."""
    wsdl_urls = [
        servers[SERVER]["prod_endpoints"].get(value, f"SKIP {key}")
        for key, value in endpoints.items()
    ]
    wsdl_urls.extend(get_distribuicao_dfe_wsdl_urls(servers))
    # the MDF-e distribution endpoint is already part of the SVRS endpoints
    wsdl_urls = list(dict.fromkeys(wsdl_urls))

    wsdl_dir = ""
    for url in wsdl_urls:
        if "SKIP" in url:
            _logger.error(
                f"Skipping WSDL download for {url} (not found on server {SERVER})"
            )
            continue
        try:
            # Ensure the URL ends with ?wsdl
            if not url.endswith("?wsdl"):
                url += "?wsdl"

            # Determine the output file path
            filename = (
                url.split("/")[-1]
                .replace("?wsdl", "")
                .replace(".asmx", ".wsdl")
                .lower()
            )

            doc_type = get_document_type(url)
            if not doc_type:
                raise ValueError(f"Cannot determine document type for URL: {url}")

            if doc_type == "nfe" and "cadconsultacadastro4" in url:
                "the server is different in this case"
                url = "https://cad.svrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx"

            # Create the output directory if it doesn't exist
            wsdl_dir, _ = WSDL_DIRS[doc_type]
            os.makedirs(wsdl_dir, exist_ok=True)

            # Write the WSDL content to the file
            wsdl_file = os.path.join(wsdl_dir, filename)

            if download:
                cert_file = environ.get("CERT_FILE")
                cert_password = environ.get("CERT_PASSWORD")
                if not cert_file or not cert_password:
                    raise ValueError(
                        "Certificate file or password not provided "
                        "in environment variables."
                    )

                session = Session()
                session.verify = False  # Disable SSL verification (use with caution)
                session.mount(
                    url,
                    Pkcs12Adapter(
                        pkcs12_filename=cert_file,
                        pkcs12_password=cert_password,
                    ),
                )
                # Fetch the WSDL content
                response = session.get(url)
                response.raise_for_status()
                _logger.info(f"Writing to {wsdl_file}")
                with open(wsdl_file, "w") as file:
                    file.write(response.text)

            if generate:
                soap_dir = wsdl_dir.replace("wsdl", "soap").replace("/", ".")
                command = [
                    "xsdata",
                    "generate",
                    "--package",
                    soap_dir,
                    "--include-header",
                    wsdl_file,
                ]
                logging.info(" ".join(command))
                try:
                    subprocess.run(command, check=True)
                    logging.info("Successfully generated SOAP bindings for {wsdl_file}")
                except subprocess.CalledProcessError as e:
                    logging.error(
                        f"Failed to generate SOAP bindings for {wsdl_file}: {e}"
                    )

        except Exception as e:
            _logger.error(f"Failed to download or save WSDL from {url}: {e}")
            continue

    if generate:
        # reset the __init__.py file to avoid arbitrary imports depending on gen order
        init_file = os.path.join(wsdl_dir.replace("wsdl", "soap"), "__init__.py")
        with open(init_file, "w") as file:
            file.write("")
