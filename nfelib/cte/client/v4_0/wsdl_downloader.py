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

    # Call the generic download_wsdl_files method with CTe-specific URLs
    download_wsdl_files(
        "https://cte.svrs.rs.gov.br/ws/CTeStatusServicoV4/CTeStatusServicoV4.asmx",
        "https://cte.svrs.rs.gov.br/ws/CTeConsultaV4/CTeConsultaV4.asmx",
        "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoSincV4/CTeRecepcaoSincV4.asmx",
        "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoOSV4/CTeRecepcaoOSV4.asmx",
        "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoGTVeV4/CTeRecepcaoGTVeV4.asmx",
        "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoEventoV4/CTeRecepcaoEventoV4.asmx",
        generate=generate,
    )


if __name__ == "__main__":
    main()
