# Auto-generated file. Do not edit manually.
# ruff: noqa: D101
# ruff: noqa: E501

from __future__ import annotations  # Python 3.8 compat

from enum import Enum
from typing import TypedDict


class Endpoint(Enum):
    QRCODE = "qrcode"
    CTESTATUSSERVICOV4 = "CteStatusServicoV4"
    CTECONSULTAV4 = "CteConsultaV4"
    CTERECEPCAOEVENTOV4 = "CteRecepcaoEventoV4"
    CTERECEPCAOOSV4 = "CTeRecepcaoOSV4"
    CTERECEPCAOSINCV4 = "CTeRecepcaoSincV4"
    CTERECEPCAOGTVEV4 = "CTeRecepcaoGTVeV4"
    CTERECEPCAOSIMPV4 = "CTeRecepcaoSimpV4"


class ServerConfig(TypedDict):
    prod_server: str
    dev_server: str
    soap_version: str
    endpoints: dict[Endpoint, str]


servers: dict[str, ServerConfig] = {
    "MT": {
        "prod_server": "cte.sefaz.mt.gov.br",
        "dev_server": "homologacao.sefaz.mt.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.QRCODE: "/cte/qrcode",
            Endpoint.CTESTATUSSERVICOV4: "/ctews2/services/CTeStatusServicoV4?wsdl",
            Endpoint.CTECONSULTAV4: "/ctews2/services/CTeConsultaV4?wsdl",
            Endpoint.CTERECEPCAOEVENTOV4: "/ctews2/services/CTeRecepcaoEventoV4?wsdl",
            Endpoint.CTERECEPCAOOSV4: "/ctews/services/CTeRecepcaoOSV4?wsdl",
            Endpoint.CTERECEPCAOSINCV4: "/ctews2/services/CTeRecepcaoSincV4?wsdl",
            Endpoint.CTERECEPCAOGTVEV4: "/ctews2/services/CTeRecepcaoGTVeV4?wsdl",
            Endpoint.CTERECEPCAOSIMPV4: "/cte-ws/services/CTeRecepcaoSimpV4",
        },
    },
    "MS": {
        "prod_server": "producao.cte.ms.gov.br",
        "dev_server": "homologacao.cte.ms.gov.br",
        "soap_version": "1.1",
        "endpoints": {
            Endpoint.QRCODE: "/cte/qrcode",
            Endpoint.CTESTATUSSERVICOV4: "/ws/CTeStatusServicoV4",
            Endpoint.CTECONSULTAV4: "/ws/CTeConsultaV4",
            Endpoint.CTERECEPCAOEVENTOV4: "/ws/CTeRecepcaoEventoV4",
            Endpoint.CTERECEPCAOOSV4: "/ws/CTeRecepcaoOSV4",
            Endpoint.CTERECEPCAOSINCV4: "/ws/CTeRecepcaoSincV4",
            Endpoint.CTERECEPCAOGTVEV4: "/ws/CTeRecepcaoGTVeV4",
            Endpoint.CTERECEPCAOSIMPV4: "/ws/CTeRecepcaoSimpV4",
        },
    },
    "MG": {
        "prod_server": "cte.fazenda.mg.gov.br",
        "dev_server": "hcte.fazenda.mg.gov.br",
        "soap_version": "1.2",
        "endpoints": {
            Endpoint.QRCODE: "/portalcte/sistema/qrcode.xhtml",
            Endpoint.CTESTATUSSERVICOV4: "/cte/services/CTeStatusServicoV4",
            Endpoint.CTECONSULTAV4: "/cte/services/CTeConsultaV4",
            Endpoint.CTERECEPCAOEVENTOV4: "/cte/services/CTeRecepcaoEventoV4",
            Endpoint.CTERECEPCAOOSV4: "/cte/services/CTeRecepcaoOSV4",
            Endpoint.CTERECEPCAOSINCV4: "/cte/services/CTeRecepcaoSincV4",
            Endpoint.CTERECEPCAOGTVEV4: "/cte/services/CTeRecepcaoGTVeV4",
            Endpoint.CTERECEPCAOSIMPV4: "/cte/services/CTeRecepcaoSimpV4",
        },
    },
    "PR": {
        "prod_server": "cte.fazenda.pr.gov.br",
        "dev_server": "homologacao.cte.fazenda.pr.gov.br",
        "soap_version": "1.2",
        "endpoints": {
            Endpoint.QRCODE: "/cte/qrcode",
            Endpoint.CTESTATUSSERVICOV4: "/cte4/CTeStatusServicoV4?wsdl",
            Endpoint.CTECONSULTAV4: "/cte4/CTeConsultaV4?wsdl",
            Endpoint.CTERECEPCAOEVENTOV4: "/cte4/CTeRecepcaoEventoV4?wsdl",
            Endpoint.CTERECEPCAOOSV4: "/cte4/CTeRecepcaoOSV4?wsdl",
            Endpoint.CTERECEPCAOSINCV4: "/cte4/CTeRecepcaoSincV4?wsdl",
            Endpoint.CTERECEPCAOGTVEV4: "/cte4/CTeRecepcaoGTVeV4?wsdl",
            Endpoint.CTERECEPCAOSIMPV4: "/cte4/CTeRecepcaoSimpV4",
        },
    },
    "RS": {
        "prod_server": "cte.svrs.rs.gov.br",
        "dev_server": "cte-homologacao.svrs.rs.gov.br",
        "soap_version": "1.2",
        "endpoints": {
            Endpoint.QRCODE: "/cte/qrCode",
            Endpoint.CTESTATUSSERVICOV4: "/ws/CTeStatusServicoV4/CTeStatusServicoV4.asmx",
            Endpoint.CTECONSULTAV4: "/ws/CTeConsultaV4/CTeConsultaV4.asmx",
            Endpoint.CTERECEPCAOEVENTOV4: "/ws/CTeRecepcaoEventoV4/CTeRecepcaoEventoV4.asmx",
            Endpoint.CTERECEPCAOOSV4: "/ws/CTeRecepcaoOSV4/CTeRecepcaoOSV4.asmx",
            Endpoint.CTERECEPCAOSINCV4: "/ws/CTeRecepcaoSincV4/CTeRecepcaoSincV4.asmx",
            Endpoint.CTERECEPCAOGTVEV4: "/ws/CTeRecepcaoGTVeV4/CTeRecepcaoGTVeV4.asmx",
            Endpoint.CTERECEPCAOSIMPV4: "/ws/CTeRecepcaoSimpV4/CTeRecepcaoSimpV4.asmx",
        },
    },
    "SP": {
        "prod_server": "nfe.fazenda.sp.gov.br",
        "dev_server": "homologacao.nfe.fazenda.sp.gov.br",
        "soap_version": "1.2",
        "endpoints": {
            Endpoint.QRCODE: "/CTeConsulta/qrCode",
            Endpoint.CTESTATUSSERVICOV4: "/CTeWS/WS/CTeStatusServicoV4.asmx",
            Endpoint.CTECONSULTAV4: "/CTeWS/WS/CTeConsultaV4.asmx",
            Endpoint.CTERECEPCAOEVENTOV4: "/CTeWS/WS/CTeRecepcaoEventoV4.asmx",
            Endpoint.CTERECEPCAOOSV4: "/CTeWS/WS/CTeRecepcaoOSV4.asmx",
            Endpoint.CTERECEPCAOSINCV4: "/CTeWS/WS/CTeRecepcaoSincV4.asmx",
            Endpoint.CTERECEPCAOGTVEV4: "/CTeWS/WS/CTeRecepcaoGTVeV4.asmx",
            Endpoint.CTERECEPCAOSIMPV4: "/CTeWS/WS/CTeRecepcaoSimpV4.asmx",
        },
    },
    "SVRS": {
        "prod_server": "cte.svrs.rs.gov.br",
        "dev_server": "cte-homologacao.svrs.rs.gov.br",
        "soap_version": "1.2",
        "endpoints": {
            Endpoint.QRCODE: "/cte/qrCode",
            Endpoint.CTESTATUSSERVICOV4: "/ws/CTeStatusServicoV4/CTeStatusServicoV4.asmx",
            Endpoint.CTECONSULTAV4: "/ws/CTeConsultaV4/CTeConsultaV4.asmx",
            Endpoint.CTERECEPCAOEVENTOV4: "/ws/CTeRecepcaoEventoV4/CTeRecepcaoEventoV4.asmx",
            Endpoint.CTERECEPCAOOSV4: "/ws/CTeRecepcaoOSV4/CTeRecepcaoOSV4.asmx",
            Endpoint.CTERECEPCAOSINCV4: "/ws/CTeRecepcaoSincV4/CTeRecepcaoSincV4.asmx",
            Endpoint.CTERECEPCAOGTVEV4: "/ws/CTeRecepcaoGTVeV4/CTeRecepcaoGTVeV4.asmx",
            Endpoint.CTERECEPCAOSIMPV4: "/ws/CTeRecepcaoSimpV4/CTeRecepcaoSimpV4.asmx",
        },
    },
    "SVSP": {
        "prod_server": "nfe.fazenda.sp.gov.br",
        "dev_server": "homologacao.nfe.fazenda.sp.gov.br",
        "soap_version": "1.2",
        "endpoints": {
            Endpoint.QRCODE: "/CTeConsulta/qrCode",
            Endpoint.CTESTATUSSERVICOV4: "/CTeWS/WS/CTeStatusServicoV4.asmx",
            Endpoint.CTECONSULTAV4: "/CTeWS/WS/CTeConsultaV4.asmx",
            Endpoint.CTERECEPCAOEVENTOV4: "/CTeWS/WS/CTeRecepcaoEventoV4.asmx",
            Endpoint.CTERECEPCAOOSV4: "/CTeWS/WS/CTeRecepcaoOSV4.asmx",
            Endpoint.CTERECEPCAOSINCV4: "/CTeWS/WS/CTeRecepcaoSincV4.asmx",
            Endpoint.CTERECEPCAOGTVEV4: "/CTeWS/WS/CTeRecepcaoGTVeV4.asmx",
            Endpoint.CTERECEPCAOSIMPV4: "/CTeWS/WS/CTeRecepcaoSimpV4.asmx",
        },
    },
    "AN": {
        "prod_server": "www1.cte.fazenda.gov.br",
        "dev_server": "hom1.cte.fazenda.gov.br",
        "soap_version": "1.1",
        "endpoints": {},
    },
}
