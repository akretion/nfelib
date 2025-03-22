import logging
import os
import subprocess
import sys
from nfelib.utils.wsdl_downloader import download_wsdl_files


def main():
    logging.basicConfig(level=logging.INFO)

    generate = False
    if "--generate" in sys.argv:
        generate = True
        sys.argv.remove(
            "--generate"
        )  # Remove the --generate flag to avoid interfering with argparse

    # Call the generic download_wsdl_files method with NFE-specific URLs
    download_wsdl_files(
        # NF-e
        "https://nfe.svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx",
        "https://nfe.svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx",
        "https://nfe.svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx",
        # "https://nfe.svrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx",
        "https://nfe.svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx",
        "https://nfe.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
        "https://nfe.svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
        "https://www1.nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx",
        generate=generate,
    )


if __name__ == "__main__":
    main()
