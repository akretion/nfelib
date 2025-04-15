# Copyright (C) 2024  Raphaël Valyi - Akretion <raphael.valyi@akretion.com.br>

from __future__ import annotations  # Python 3.8 compat

import logging
import os
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


def generate_soap(
    servers: dict[str, Any],
    endpoints: dict[str, str],
    download: bool = False,
    generate: bool = False,
) -> None:
    """Download WSDL files for NF-e, CT-e, MDF-e, and BP-e."""
    # Access the certificate and password from environment variables
    server = servers[SERVER]["prod_server"]
    wsdl_urls = [
        f"https://{server}{servers[SERVER]['endpoints'].get(value, ' SKIP ' + key)}"
        for key, value in endpoints.items()
    ]

    # TODO make extra wsdl urls a param
    wsdl_urls.append(
        "https://www1.nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx"
    )

    doc_type = None
    wsdl_dir = ""
    for url in wsdl_urls:
        if "SKIP" in url and "NFeDistribuicaoDFe" not in url:
            _logger.error(
                f"Skipping WSDL download for {url} (not found on server {server})"
            )
            continue
        try:
            # Determine the server and mount the PKCS12 adapter
            # url = f"https://{server}{path}"

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

            if doc_type is None:
                # Identify the document type (NF-e, CT-e, MDF-e, BP-e)
                for key, (_, _prefix) in WSDL_DIRS.items():
                    if key in url.lower():
                        doc_type = key
                        break
                if not doc_type:
                    raise ValueError(f"Cannot determine document type for URL: {url}")

            if doc_type == "nfe":
                if "cadconsultacadastro4" in url:
                    "the server is different in this case"
                    url = "https://cad.svrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx"
            elif "NFeDistribuicaoDFe" in url:  # only for NFe
                continue

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
