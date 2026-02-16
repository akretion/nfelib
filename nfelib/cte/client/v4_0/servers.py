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
    soap_version: str
    prod_endpoints: dict[Endpoint, str]
    dev_endpoints: dict[Endpoint, str]


servers: dict[str, ServerConfig] = {
    "MT": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.QRCODE: "https://www.sefaz.mt.gov.br/cte/qrcode",
            Endpoint.CTESTATUSSERVICOV4: "https://cte.sefaz.mt.gov.br/ctews2/services/CTeStatusServicoV4?wsdl",
            Endpoint.CTECONSULTAV4: "https://cte.sefaz.mt.gov.br/ctews2/services/CTeConsultaV4?wsdl",
            Endpoint.CTERECEPCAOEVENTOV4: "https://cte.sefaz.mt.gov.br/ctews2/services/CTeRecepcaoEventoV4?wsdl",
            Endpoint.CTERECEPCAOOSV4: "https://cte.sefaz.mt.gov.br/ctews/services/CTeRecepcaoOSV4?wsdl",
            Endpoint.CTERECEPCAOSINCV4: "https://cte.sefaz.mt.gov.br/ctews2/services/CTeRecepcaoSincV4?wsdl",
            Endpoint.CTERECEPCAOGTVEV4: "https://cte.sefaz.mt.gov.br/ctews2/services/CTeRecepcaoGTVeV4?wsdl",
            Endpoint.CTERECEPCAOSIMPV4: "https://cte.sefaz.mt.gov.br/cte-ws/services/CTeRecepcaoSimpV4",
        },
        "dev_endpoints": {
            Endpoint.QRCODE: "https://homologacao.sefaz.mt.gov.br/cte/qrcode",
            Endpoint.CTESTATUSSERVICOV4: "https://homologacao.sefaz.mt.gov.br/ctews2/services/CTeStatusServicoV4?wsdl",
            Endpoint.CTECONSULTAV4: "https://homologacao.sefaz.mt.gov.br/ctews2/services/CTeConsultaV4?wsdl",
            Endpoint.CTERECEPCAOEVENTOV4: "https://homologacao.sefaz.mt.gov.br/ctews2/services/CTeRecepcaoEventoV4?wsdl",
            Endpoint.CTERECEPCAOOSV4: "https://homologacao.sefaz.mt.gov.br/ctews/services/CTeRecepcaoOSV4?wsdl",
            Endpoint.CTERECEPCAOSINCV4: "https://homologacao.sefaz.mt.gov.br/ctews2/services/CTeRecepcaoSincV4?wsdl",
            Endpoint.CTERECEPCAOGTVEV4: "https://homologacao.sefaz.mt.gov.br/ctews2/services/CTeRecepcaoGTVeV4?wsdl",
            Endpoint.CTERECEPCAOSIMPV4: "https://homologacao.sefaz.mt.gov.br/cte-ws/services/CTeRecepcaoSimpV4",
        },
    },
    "MS": {
        "soap_version": "1.1",
        "prod_endpoints": {
            Endpoint.QRCODE: "http://www.dfe.ms.gov.br/cte/qrcode",
            Endpoint.CTESTATUSSERVICOV4: "https://producao.cte.ms.gov.br/ws/CTeStatusServicoV4",
            Endpoint.CTECONSULTAV4: "https://producao.cte.ms.gov.br/ws/CTeConsultaV4",
            Endpoint.CTERECEPCAOEVENTOV4: "https://producao.cte.ms.gov.br/ws/CTeRecepcaoEventoV4",
            Endpoint.CTERECEPCAOOSV4: "https://producao.cte.ms.gov.br/ws/CTeRecepcaoOSV4",
            Endpoint.CTERECEPCAOSINCV4: "https://producao.cte.ms.gov.br/ws/CTeRecepcaoSincV4",
            Endpoint.CTERECEPCAOGTVEV4: "https://producao.cte.ms.gov.br/ws/CTeRecepcaoGTVeV4",
            Endpoint.CTERECEPCAOSIMPV4: "https://producao.cte.ms.gov.br/ws/CTeRecepcaoSimpV4",
        },
        "dev_endpoints": {
            Endpoint.QRCODE: "http://www.dfe.ms.gov.br/cte/qrcode",
            Endpoint.CTESTATUSSERVICOV4: "https://homologacao.cte.ms.gov.br/ws/CTeStatusServicoV4",
            Endpoint.CTECONSULTAV4: "https://homologacao.cte.ms.gov.br/ws/CTeConsultaV4",
            Endpoint.CTERECEPCAOEVENTOV4: "https://homologacao.cte.ms.gov.br/ws/CTeRecepcaoEventoV4",
            Endpoint.CTERECEPCAOOSV4: "https://homologacao.cte.ms.gov.br/ws/CTeRecepcaoOSV4",
            Endpoint.CTERECEPCAOSINCV4: "https://homologacao.cte.ms.gov.br/ws/CTeRecepcaoSincV4",
            Endpoint.CTERECEPCAOGTVEV4: "https://homologacao.cte.ms.gov.br/ws/CTeRecepcaoGTVeV4",
            Endpoint.CTERECEPCAOSIMPV4: "https://homologacao.cte.ms.gov.br/ws/CTeRecepcaoSimpV4",
        },
    },
    "MG": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.QRCODE: "https://portalcte.fazenda.mg.gov.br/portalcte/sistema/qrcode.xhtml",
            Endpoint.CTESTATUSSERVICOV4: "https://cte.fazenda.mg.gov.br/cte/services/CTeStatusServicoV4",
            Endpoint.CTECONSULTAV4: "https://cte.fazenda.mg.gov.br/cte/services/CTeConsultaV4",
            Endpoint.CTERECEPCAOEVENTOV4: "https://cte.fazenda.mg.gov.br/cte/services/CTeRecepcaoEventoV4",
            Endpoint.CTERECEPCAOOSV4: "https://cte.fazenda.mg.gov.br/cte/services/CTeRecepcaoOSV4",
            Endpoint.CTERECEPCAOSINCV4: "https://cte.fazenda.mg.gov.br/cte/services/CTeRecepcaoSincV4",
            Endpoint.CTERECEPCAOGTVEV4: "https://cte.fazenda.mg.gov.br/cte/services/CTeRecepcaoGTVeV4",
            Endpoint.CTERECEPCAOSIMPV4: "https://cte.fazenda.mg.gov.br/cte/services/CTeRecepcaoSimpV4",
        },
        "dev_endpoints": {
            Endpoint.QRCODE: "https://portalcte.fazenda.mg.gov.br/portalcte/sistema/qrcode.xhtml",
            Endpoint.CTESTATUSSERVICOV4: "https://hcte.fazenda.mg.gov.br/cte/services/CTeStatusServicoV4",
            Endpoint.CTECONSULTAV4: "https://hcte.fazenda.mg.gov.br/cte/services/CTeConsultaV4",
            Endpoint.CTERECEPCAOEVENTOV4: "https://hcte.fazenda.mg.gov.br/cte/services/CTeRecepcaoEventoV4",
            Endpoint.CTERECEPCAOOSV4: "https://hcte.fazenda.mg.gov.br/cte/services/CTeRecepcaoOSV4",
            Endpoint.CTERECEPCAOSINCV4: "https://hcte.fazenda.mg.gov.br/cte/services/CTeRecepcaoSincV4",
            Endpoint.CTERECEPCAOGTVEV4: "https://hcte.fazenda.mg.gov.br/cte/services/CTeRecepcaoGTVeV4",
            Endpoint.CTERECEPCAOSIMPV4: "https://hcte.fazenda.mg.gov.br/cte/services/CTeRecepcaoSimpV4",
        },
    },
    "PR": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.QRCODE: "http://www.fazenda.pr.gov.br/cte/qrcode",
            Endpoint.CTESTATUSSERVICOV4: "https://cte.fazenda.pr.gov.br/cte4/CTeStatusServicoV4?wsdl",
            Endpoint.CTECONSULTAV4: "https://cte.fazenda.pr.gov.br/cte4/CTeConsultaV4?wsdl",
            Endpoint.CTERECEPCAOEVENTOV4: "https://cte.fazenda.pr.gov.br/cte4/CTeRecepcaoEventoV4?wsdl",
            Endpoint.CTERECEPCAOOSV4: "https://cte.fazenda.pr.gov.br/cte4/CTeRecepcaoOSV4?wsdl",
            Endpoint.CTERECEPCAOSINCV4: "https://cte.fazenda.pr.gov.br/cte4/CTeRecepcaoSincV4?wsdl",
            Endpoint.CTERECEPCAOGTVEV4: "https://cte.fazenda.pr.gov.br/cte4/CTeRecepcaoGTVeV4?wsdl",
            Endpoint.CTERECEPCAOSIMPV4: "https://cte.fazenda.pr.gov.br/cte4/CTeRecepcaoSimpV4",
        },
        "dev_endpoints": {
            Endpoint.QRCODE: "http://www.fazenda.pr.gov.br/cte/qrcode",
            Endpoint.CTESTATUSSERVICOV4: "https://homologacao.cte.fazenda.pr.gov.br/cte4/CTeStatusServicoV4?wsdl",
            Endpoint.CTECONSULTAV4: "https://homologacao.cte.fazenda.pr.gov.br/cte4/CTeConsultaV4?wsdl",
            Endpoint.CTERECEPCAOEVENTOV4: "https://homologacao.cte.fazenda.pr.gov.br/cte4/CTeRecepcaoEventoV4?wsdl",
            Endpoint.CTERECEPCAOOSV4: "https://homologacao.cte.fazenda.pr.gov.br/cte4/CTeRecepcaoOSV4?wsdl",
            Endpoint.CTERECEPCAOSINCV4: "https://homologacao.cte.fazenda.pr.gov.br/cte4/CTeRecepcaoSincV4?wsdl",
            Endpoint.CTERECEPCAOGTVEV4: "https://homologacao.cte.fazenda.pr.gov.br/cte4/CTeRecepcaoGTVeV4?wsdl",
            Endpoint.CTERECEPCAOSIMPV4: "https://homologacao.cte.fazenda.pr.gov.br/cte4/CTeRecepcaoSimpV4",
        },
    },
    "RS": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.QRCODE: "https://dfe-portal.svrs.rs.gov.br/cte/qrCode",
            Endpoint.CTESTATUSSERVICOV4: "https://cte.svrs.rs.gov.br/ws/CTeStatusServicoV4/CTeStatusServicoV4.asmx",
            Endpoint.CTECONSULTAV4: "https://cte.svrs.rs.gov.br/ws/CTeConsultaV4/CTeConsultaV4.asmx",
            Endpoint.CTERECEPCAOEVENTOV4: "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoEventoV4/CTeRecepcaoEventoV4.asmx",
            Endpoint.CTERECEPCAOOSV4: "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoOSV4/CTeRecepcaoOSV4.asmx",
            Endpoint.CTERECEPCAOSINCV4: "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoSincV4/CTeRecepcaoSincV4.asmx",
            Endpoint.CTERECEPCAOGTVEV4: "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoGTVeV4/CTeRecepcaoGTVeV4.asmx",
            Endpoint.CTERECEPCAOSIMPV4: "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoSimpV4/CTeRecepcaoSimpV4.asmx",
        },
        "dev_endpoints": {
            Endpoint.QRCODE: "https://dfe-portal.svrs.rs.gov.br/cte/qrCode",
            Endpoint.CTESTATUSSERVICOV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeStatusServicoV4/CTeStatusServicoV4.asmx",
            Endpoint.CTECONSULTAV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeConsultaV4/CTeConsultaV4.asmx",
            Endpoint.CTERECEPCAOEVENTOV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeRecepcaoEventoV4/CTeRecepcaoEventoV4.asmx",
            Endpoint.CTERECEPCAOOSV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeRecepcaoOSV4/CTeRecepcaoOSV4.asmx",
            Endpoint.CTERECEPCAOSINCV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeRecepcaoSincV4/CTeRecepcaoSincV4.asmx",
            Endpoint.CTERECEPCAOGTVEV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeRecepcaoGTVeV4/CTeRecepcaoGTVeV4.asmx",
            Endpoint.CTERECEPCAOSIMPV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeRecepcaoSimpV4/CTeRecepcaoSimpV4.asmx",
        },
    },
    "SP": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.QRCODE: "https://nfe.fazenda.sp.gov.br/CTeConsulta/qrCode",
            Endpoint.CTESTATUSSERVICOV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeStatusServicoV4.asmx",
            Endpoint.CTECONSULTAV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeConsultaV4.asmx",
            Endpoint.CTERECEPCAOEVENTOV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoEventoV4.asmx",
            Endpoint.CTERECEPCAOOSV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoOSV4.asmx",
            Endpoint.CTERECEPCAOSINCV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoSincV4.asmx",
            Endpoint.CTERECEPCAOGTVEV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoGTVeV4.asmx",
            Endpoint.CTERECEPCAOSIMPV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoSimpV4.asmx",
        },
        "dev_endpoints": {
            Endpoint.QRCODE: "https://homologacao.nfe.fazenda.sp.gov.br/CTeConsulta/qrCode",
            Endpoint.CTESTATUSSERVICOV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeStatusServicoV4.asmx",
            Endpoint.CTECONSULTAV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeConsultaV4.asmx",
            Endpoint.CTERECEPCAOEVENTOV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoEventoV4.asmx",
            Endpoint.CTERECEPCAOOSV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoOSV4.asmx",
            Endpoint.CTERECEPCAOSINCV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoSincV4.asmx",
            Endpoint.CTERECEPCAOGTVEV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoGTVeV4.asmx",
            Endpoint.CTERECEPCAOSIMPV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoSimpV4.asmx",
        },
    },
    "SVRS": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.QRCODE: "https://dfe-portal.svrs.rs.gov.br/cte/qrCode",
            Endpoint.CTESTATUSSERVICOV4: "https://cte.svrs.rs.gov.br/ws/CTeStatusServicoV4/CTeStatusServicoV4.asmx",
            Endpoint.CTECONSULTAV4: "https://cte.svrs.rs.gov.br/ws/CTeConsultaV4/CTeConsultaV4.asmx",
            Endpoint.CTERECEPCAOEVENTOV4: "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoEventoV4/CTeRecepcaoEventoV4.asmx",
            Endpoint.CTERECEPCAOOSV4: "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoOSV4/CTeRecepcaoOSV4.asmx",
            Endpoint.CTERECEPCAOSINCV4: "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoSincV4/CTeRecepcaoSincV4.asmx",
            Endpoint.CTERECEPCAOGTVEV4: "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoGTVeV4/CTeRecepcaoGTVeV4.asmx",
            Endpoint.CTERECEPCAOSIMPV4: "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoSimpV4/CTeRecepcaoSimpV4.asmx",
        },
        "dev_endpoints": {
            Endpoint.QRCODE: "https://dfe-portal.svrs.rs.gov.br/cte/qrCode",
            Endpoint.CTESTATUSSERVICOV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeStatusServicoV4/CTeStatusServicoV4.asmx",
            Endpoint.CTECONSULTAV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeConsultaV4/CTeConsultaV4.asmx",
            Endpoint.CTERECEPCAOEVENTOV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeRecepcaoEventoV4/CTeRecepcaoEventoV4.asmx",
            Endpoint.CTERECEPCAOOSV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeRecepcaoOSV4/CTeRecepcaoOSV4.asmx",
            Endpoint.CTERECEPCAOSINCV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeRecepcaoSincV4/CTeRecepcaoSincV4.asmx",
            Endpoint.CTERECEPCAOGTVEV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeRecepcaoGTVeV4/CTeRecepcaoGTVeV4.asmx",
            Endpoint.CTERECEPCAOSIMPV4: "https://cte-homologacao.svrs.rs.gov.br/ws/CTeRecepcaoSimpV4/CTeRecepcaoSimpV4.asmx",
        },
    },
    "SVSP": {
        "soap_version": "1.2",
        "prod_endpoints": {
            Endpoint.QRCODE: "https://nfe.fazenda.sp.gov.br/CTeConsulta/qrCode",
            Endpoint.CTESTATUSSERVICOV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeStatusServicoV4.asmx",
            Endpoint.CTECONSULTAV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeConsultaV4.asmx",
            Endpoint.CTERECEPCAOEVENTOV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoEventoV4.asmx",
            Endpoint.CTERECEPCAOOSV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoOSV4.asmx",
            Endpoint.CTERECEPCAOSINCV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoSincV4.asmx",
            Endpoint.CTERECEPCAOGTVEV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoGTVeV4.asmx",
            Endpoint.CTERECEPCAOSIMPV4: "https://nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoSimpV4.asmx",
        },
        "dev_endpoints": {
            Endpoint.QRCODE: "https://homologacao.nfe.fazenda.sp.gov.br/CTeConsulta/qrCode",
            Endpoint.CTESTATUSSERVICOV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeStatusServicoV4.asmx",
            Endpoint.CTECONSULTAV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeConsultaV4.asmx",
            Endpoint.CTERECEPCAOEVENTOV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoEventoV4.asmx",
            Endpoint.CTERECEPCAOOSV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoOSV4.asmx",
            Endpoint.CTERECEPCAOSINCV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoSincV4.asmx",
            Endpoint.CTERECEPCAOGTVEV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoGTVeV4.asmx",
            Endpoint.CTERECEPCAOSIMPV4: "https://homologacao.nfe.fazenda.sp.gov.br/CTeWS/WS/CTeRecepcaoSimpV4.asmx",
        },
    },
    "AN": {
        "soap_version": "1.1",
        "prod_endpoints": {},
        "dev_endpoints": {},
    },
}
