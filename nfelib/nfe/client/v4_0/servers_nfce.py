# Copyright (C) 2023 Ygor de Carvalho - KMEE
# Copyright (C) 2025 Raphaël Valyi - Akretion

ESTADO_QRCODE = {
    "AC": {
        "1": "www.sefaznet.ac.gov.br/nfce/qrcode?p=",
        "2": "www.hml.sefaznet.ac.gov.br/nfce/qrcode?p=",
    },
    "AL": {
        "1": "nfce.sefaz.al.gov.br/QRCode/consultarNFCe.jsp?p=",
        "2": "nfce.sefaz.al.gov.br/QRCode/consultarNFCe.jsp?p=",
    },
    "AM": {
        "1": "sistemas.sefaz.am.gov.br/nfceweb/consultarNFCe.jsp?p=",
        "2": "homnfce.sefaz.am.gov.br/nfceweb/consultarNFCe.jsp?p=",
    },
    "AP": {
        "1": "www.sefaz.ap.gov.br/nfce/nfcep.php?p=",
        "2": "www.sefaz.ap.gov.br/nfcehml/nfce.php?p=",  # FIXME 404
    },
    "BA": {
        "1": "nfe.sefaz.ba.gov.br/servicos/nfce/qrcode.aspx?p=",
        "2": "hnfe.sefaz.ba.gov.br/servicos/nfce/qrcode.aspx?p=",
    },
    "CE": {
        "1": "nfce.sefaz.ce.gov.br/pages/ShowNFCe.html?p=",
        "2": "nfceh.sefaz.ce.gov.br/pages/ShowNFCe.html?p=",
    },
    "DF": {
        "1": "ww1.receita.fazenda.df.gov.br/DecVisualizador/Nfce/qrcode?p=",
        "2": "ww1.receita.fazenda.df.gov.br/DecVisualizador/Nfce/qrcode?p=",
    },
    "ES": {
        "1": "app.sefaz.es.gov.br/ConsultaNFCe?p=",
        "2": "homologacao.sefaz.es.gov.br/ConsultaNFCe?p=",
    },
    "GO": {
        "1": "nfe.sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe?p=",
        "2": "homolog.sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe?p=",  # FIXME connection error
    },
    "MA": {
        "1": "nfce.sefaz.ma.gov.br/portal/consultarNFCe.jsp?p=",
        "2": "homologacao.sefaz.ma.gov.br/portal/consultarNFCe.jsp?p=",
    },
    "MG": {
        "1": "portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=",
        "2": "hnfce.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=",
    },
    "MS": {
        "1": "www.dfe.ms.gov.br/nfce/qrcode?p=",
        "2": "www.dfe.ms.gov.br/nfce/qrcode?p=",
    },
    "MT": {
        "1": "www.sefaz.mt.gov.br/nfce/consultanfce?p=",
        "2": "homologacao.sefaz.mt.gov.br/nfce/consultanfce?p=",
    },
    "PA": {
        "1": "appnfc.sefa.pa.gov.br/portal/view/consultas/nfce/nfceForm.seam?p=",
        "2": "appnfc.sefa.pa.gov.br/portal-homologacao/view/consultas/nfce/nfceForm.seam?p=",
    },
    "PB": {
        "1": "www4.sefaz.pb.gov.br/atf/seg/SEGf_AcessarFuncao.jsp?cdFuncao=FIS_1410&chNFe=",
        "2": "www7.sefaz.pb.gov.br/atf/seg/SEGf_AcessarFuncao.jsp?cdFuncao=FIS_1410&chNFe=",
    },
    "PE": {
        "1": "nfce.sefaz.pe.gov.br:444/nfce/consulta?p=",
        "2": "nfcehomolog.sefaz.pe.gov.br/nfce/consulta?p=",
    },
    "PI": {
        "1": "www.sefaz.pi.gov.br/nfce/qrcode?p=",
        "2": "www.sefaz.pi.gov.br/nfce/qrcode?p=",
    },
    "PR": {
        "1": "www.fazenda.pr.gov.br/nfce/qrcode?p=",
        "2": "www.fazenda.pr.gov.br/nfce/qrcode?p=",
    },
    "RJ": {
        "1": "www4.fazenda.rj.gov.br/consultaNFCe/QRCode?p=",
        "2": "www4.fazenda.rj.gov.br/consultaNFCe/QRCode?p=",
    },
    "RN": {
        "1": "nfce.set.rn.gov.br/portalDFE/NFCe/mDadosNFCe.aspx?p=",
        "2": "hom.nfce.set.rn.gov.br/consultarNFCe.aspx?p=",  # FIXME timeout
    },
    "RO": {
        "1": "www.nfce.sefin.ro.gov.br/home.jsp",
        "2": "www.nfce.sefin.ro.gov.br/home.jsp",
    },
    "RR": {
        "1": "www.sefaz.rr.gov.br/nfce/servlet/qrcode?p=",
        "2": "200.174.88.103:8080/nfce/servlet/qrcode?p=",  # FIXME timeout
    },
    "RS": {
        "1": "www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?p=",  # FIXME read timeout
        "2": "www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?p=",
    },
    "SC": {
        "1": "sat.sef.sc.gov.br/nfce/consulta?p=",
        "2": "hom.sat.sef.sc.gov.br/nfce/consulta?p=",
    },
    "SE": {
        "1": "nfce.sefaz.se.gov.br/portal/portalNoticias.jsp",  # updated redirect target
        "2": "www.hom.nfe.se.gov.br/nfce/qrcode?p=",  # FIXME timeout
    },
    "SP": {
        "1": "www.nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaQRCode.aspx?p=",
        "2": "www.homologacao.nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaQRCode.aspx?p=",
    },
    "TO": {
        "1": "www.sefaz.to.gov.br/nfce/qrcode?p=",
        "2": "homologacao.sefaz.to.gov.br/nfce/qrcode?p=",
    },
}


ESTADO_CONSULTA_NFCE = {
    "AC": [
        "www.sefaznet.ac.gov.br/nfce/consulta",
        "www.hml.sefaznet.ac.gov.br/nfce/consulta",  # FIXME ConnectTimeout
    ],
    "AM": [
        "www.sefaz.am.gov.br/nfce/formConsulta.do",
        "www.sefaz.am.gov.br/nfce/formConsulta.do",
    ],
    "AP": [
        "www.sefaz.ap.gov.br/nfce/consulta",
        "www.sefaz.ap.gov.br/nfce/consulta",
    ],
    # BA: homolog off-line
    "BA": [
        "hinternet.sefaz.ba.gov.br/nfce/consulta",  # FIXME ConnectionError
    ],
    "DF": [
        "ww1.receita.fazenda.df.gov.br/documentosfiscais/consultar",
        "ww1.receita.fazenda.df.gov.br/documentosfiscais/consultar",
    ],
    "MA": [
        "www.sefaz.ma.gov.br/nfce/consulta",
        "www.sefaz.ma.gov.br/nfce/consulta",
    ],
    "MG": [
        "hnfce.fazenda.mg.gov.br/portalnfce",
    ],
    "MT": [
        "www.sefaz.mt.gov.br/nfce/consultanfce",
        "homologacao.sefaz.mt.gov.br/nfce/consultanfce",
    ],
    "PE": [
        "nfce.sefaz.pe.gov.br:444/nfce/consulta",
        "nfce.sefaz.pe.gov.br:444/nfce/consulta",
    ],
    "PR": [
        "www.fazenda.pr.gov.br/nfce/consulta",
        "www.fazenda.pr.gov.br/nfce/consulta",
    ],
    # RJ: 404
    "RJ": [
        "portal.fazenda.rj.gov.br/dfe/consultaNFCe",  # FIXME HTTP 404
        "portal.fazenda.rj.gov.br/dfe/consultaNFCe",  # FIXME HTTP 404
    ],
    # RN: ReadTimeout
    "RN": [
        "www.set.rn.gov.br/nfce/consulta",  # FIXME ReadTimeout
        "www.set.rn.gov.br/nfce/consulta",  # FIXME ReadTimeout
    ],
    # RR: 404
    "RR": [
        "portalapp.sefaz.rr.gov.br/nfce/consulta",  # FIXME HTTP 404
        "portalapp.sefaz.rr.gov.br/nfce/consulta",  # FIXME HTTP 404
    ],
    # RS: ReadTimeout
    "RS": [
        "www.sefaz.rs.gov.br/nfce/consulta",  # FIXME ReadTimeout
        "www.sefaz.rs.gov.br/nfce/consulta",  # FIXME ReadTimeout
    ],
    # TODO SC
    # SE: redirects to HTTPS
    "SE": [
        "nfce.sefaz.se.gov.br",
        "www.hom.nfe.se.gov.br/nfce/consulta",  # FIXME ReadTimeout
    ],
    "SP": [
        "ww.nfce.fazenda.sp.gov.br/consulta",
        "www.homologacao.nfce.fazenda.sp.gov.br/consulta",
    ],
    "TO": [
        "www.sefaz.to.gov.br/nfce/consulta",
        "homologacao.sefaz.to.gov.br/nfce/consulta.jsf",
    ],
}
