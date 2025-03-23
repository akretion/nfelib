# Copyright (C) 2024  Raphaël Valyi - Akretion <raphael.valyi@akretion.com.br>

import logging
import os
import subprocess
from os import environ

import urllib3
from requests import Session
from requests_pkcs12 import Pkcs12Adapter

# Configure logging
_logger = logging.getLogger(__name__)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Constants
SERVER = "https://nfe-homologacao.svrs.rs.gov.br"  # TODO: Make this a parameter
WSDL_DIRS = {
    "nfe": ("nfelib/nfe/wsdl/v4_0", "nfe"),
    "mdfe": ("nfelib/mdfe/wsdl/v3_0", "mdfe"),
    "cte": ("nfelib/cte/wsdl/v4_0", "cte"),
    "bpe": ("nfelib/bpe/wsdl/v1_0", "bpe"),
}


def download_wsdl_files(*wsdl_urls, generate=False):
    """Download WSDL files for NF-e, CT-e, MDF-e, and BP-e."""
    # Access the certificate and password from environment variables
    CERT_FILE = environ.get("CERT_FILE")
    CERT_PASSWORD = environ.get("CERT_PASSWORD")

    if not CERT_FILE or not CERT_PASSWORD:
        raise ValueError(
            "Certificate file or password not provided in environment variables."
        )

    session = Session()
    session.verify = False  # Disable SSL verification (use with caution)

    for url in wsdl_urls:
        try:
            # Determine the server and mount the PKCS12 adapter
            if not url.startswith("http"):
                url = SERVER + url
                server = SERVER
            else:
                server = "https://" + url.split("/")[2]

            session.mount(
                server,
                Pkcs12Adapter(
                    pkcs12_filename=CERT_FILE,
                    pkcs12_password=CERT_PASSWORD,
                ),
            )

            # Ensure the URL ends with ?wsdl
            if not url.endswith("?wsdl"):
                url += "?wsdl"

            # Fetch the WSDL content
            response = session.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors

            # Determine the output file path
            filename = (
                url.split("/")[-1]
                .replace("?wsdl", "")
                .replace(".asmx", ".wsdl")
                .lower()
            )

            # Identify the document type (NF-e, CT-e, MDF-e, BP-e)
            doc_type = None
            for key, (_, prefix) in WSDL_DIRS.items():
                if key in url.lower():
                    doc_type = key
                    break
            if not doc_type:
                raise ValueError(f"Cannot determine document type for URL: {url}")

            # Create the output directory if it doesn't exist
            wsdl_dir, _ = WSDL_DIRS[doc_type]
            os.makedirs(wsdl_dir, exist_ok=True)

            # Write the WSDL content to the file
            wsdl_file = os.path.join(wsdl_dir, filename)
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
                try:
                    subprocess.run(command, check=True)
                    logging.info("Successfully generated SOAP bindings for {wsdl_file}")
                except subprocess.CalledProcessError as e:
                    logging.error(
                        f"Failed to generate SOAP bindings for {wsdl_file}: {e}"
                    )

        except Exception as e:
            _logger.error(f"Failed to download or save WSDL from {url}: {e}")
            raise
