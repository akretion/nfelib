import logging
import sys

from nfelib.utils.wsdl_downloader import download_wsdl_files


def main() -> None:
    """Cli entry point."""
    logging.basicConfig(level=logging.INFO)

    generate = False
    if "--generate" in sys.argv:
        generate = True
        sys.argv.remove(
            "--generate"
        )  # Remove the --generate flag to avoid interfering with argparse

    # Call the generic download_wsdl_files method with MDFe-specific URLs
    download_wsdl_files(
        "https://mdfe.svrs.rs.gov.br/ws/MDFeRecepcaoEvento/MDFeRecepcaoEvento.asmx",
        "https://mdfe.svrs.rs.gov.br/ws/MDFeConsulta/MDFeConsulta.asmx",
        "https://mdfe.svrs.rs.gov.br/ws/MDFeConsulta/MDFeConsulta.asmx",
        "https://mdfe.svrs.rs.gov.br/ws/MDFeConsNaoEnc/MDFeConsNaoEnc.asmx",
        "https://mdfe.svrs.rs.gov.br/ws/MDFeDistribuicaoDFe/MDFeDistribuicaoDFe.asmx",
        "https://mdfe.svrs.rs.gov.br/ws/MDFeRecepcaoSinc/MDFeRecepcaoSinc.asmx",
        # "https://dfe-portal.svrs.rs.gov.br/Mdfe/QrCode",  # not a wsdl!
        generate=generate,
    )


if __name__ == "__main__":
    main()
