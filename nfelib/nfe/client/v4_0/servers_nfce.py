# FILEPATH: nfelib/nfe/client/v4_0/servers_nfce.py
# Copyright (C) 2023 Ygor de Carvalho - KMEE
# Copyright (C) 2025 Raphaël Valyi - Akretion
#
# This file contains the static URL configurations for NFC-e QR Codes and
# consultation pages, adapted from the legacy erpbrasil.edoc project.

# URL base para a consulta via QR Code da NFC-e por UF
# Formato: { "UF_SIGLA": { "1": "producao_url", "2": "homologacao_url" } }
ESTADO_QRCODE = {
    "AC": {
        "1": "http://www.sefaznet.ac.gov.br/nfce/qrcode?p=",
        "2": "http://www.hml.sefaznet.ac.gov.br/nfce/qrcode?p=",
    },
    "AL": {
        "1": "http://nfce.sefaz.al.gov.br/QRCode/consultarNFCe.jsp?p=",
        "2": "http://nfce.sefaz.al.gov.br/QRCode/consultarNFCe.jsp?p=",
    },
    "AM": {
        "1": "http://sistemas.sefaz.am.gov.br/nfceweb/consultarNFCe.jsp?p=",
        "2": "http://homnfce.sefaz.am.gov.br/nfceweb/consultarNFCe.jsp?p=",
    },
    "AP": {
        "1": "https://www.sefaz.ap.gov.br/nfce/nfcep.php?p=",
        "2": "https://www.sefaz.ap.gov.br/nfcehml/nfce.php?p=",
    },
    "BA": {
        "1": "http://nfe.sefaz.ba.gov.br/servicos/nfce/qrcode.aspx?p=",
        "2": "http://hnfe.sefaz.ba.gov.br/servicos/nfce/qrcode.aspx?p=",
    },
    "CE": {
        "1": "http://nfce.sefaz.ce.gov.br/pages/ShowNFCe.html?p=",
        "2": "http://nfceh.sefaz.ce.gov.br/pages/ShowNFCe.html?p=",
    },
    "DF": {
        "1": "http://www.fazenda.df.gov.br/nfce/qrcode?p=",
        "2": "http://www.fazenda.df.gov.br/nfce/qrcode?p=",
    },
    "ES": {
        "1": "http://app.sefaz.es.gov.br/ConsultaNFCe?p=",
        "2": "http://homologacao.sefaz.es.gov.br/ConsultaNFCe?p=",
    },
    "GO": {
        "1": "http://nfe.sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe?p=",
        "2": "http://homolog.sefaz.go.gov.br/nfeweb/sites/nfce/danfeNFCe?p=",
    },
    "MA": {
        "1": "http://nfce.sefaz.ma.gov.br/portal/consultarNFCe.jsp?p=",
        "2": "http://homologacao.sefaz.ma.gov.br/portal/consultarNFCe.jsp?p=",
    },
    "MG": {
        "1": "https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=",
        "2": "https://portalsped.fazenda.mg.gov.br/portalnfce/sistema/qrcode.xhtml?p=",
    },
    "MS": {
        "1": "http://www.dfe.ms.gov.br/nfce/qrcode?p=",
        "2": "http://www.dfe.ms.gov.br/nfce/qrcode?p=",
    },
    "MT": {
        "1": "http://www.sefaz.mt.gov.br/nfce/consultanfce?p=",
        "2": "http://homologacao.sefaz.mt.gov.br/nfce/consultanfce?p=",
    },
    "PA": {
        "1": "https://appnfc.sefa.pa.gov.br/portal/view/consultas/nfce/nfceForm.seam?p=",
        "2": "https://appnfc.sefa.pa.gov.br/portal-homologacao/view/consultas/nfce/nfceForm.seam?p=",
    },
    "PB": {
        "1": "http://www.sefaz.pb.gov.br/nfce?p=",
        "2": "http://www.sefaz.pb.gov.br/nfcehom?p=",
    },
    "PE": {
        "1": "http://nfce.sefaz.pe.gov.br/nfce/consulta?p=",
        "2": "http://nfcehomolog.sefaz.pe.gov.br/nfce/consulta?p=",
    },
    "PI": {
        "1": "http://www.sefaz.pi.gov.br/nfce/qrcode?p=",
        "2": "http://www.sefaz.pi.gov.br/nfce/qrcode?p=",
    },
    "PR": {
        "1": "http://www.fazenda.pr.gov.br/nfce/qrcode?p=",
        "2": "http://www.fazenda.pr.gov.br/nfce/qrcode?p=",
    },
    "RJ": {
        "1": "http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?p=",
        "2": "http://www4.fazenda.rj.gov.br/consultaNFCe/QRCode?p=",
    },
    "RN": {
        "1": "http://nfce.set.rn.gov.br/consultarNFCe.aspx?p=",
        "2": "http://hom.nfce.set.rn.gov.br/consultarNFCe.aspx?p=",
    },
    "RO": {
        "1": "http://www.nfce.sefin.ro.gov.br/consultanfce/consulta.jsp?p=",
        "2": "http://www.nfce.sefin.ro.gov.br/consultanfce/consulta.jsp?p=",
    },
    "RR": {
        "1": "https://www.sefaz.rr.gov.br/nfce/servlet/qrcode?p=",
        "2": "http://200.174.88.103:8080/nfce/servlet/qrcode?p=",
    },
    "RS": {
        "1": "https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?p=",
        "2": "https://www.sefaz.rs.gov.br/NFCE/NFCE-COM.aspx?p=",
    },
    "SC": {
        "1": "https://sat.sef.sc.gov.br/nfce/consulta?p=",
        "2": "https://hom.sat.sef.sc.gov.br/nfce/consulta?p=",
    },
    "SE": {
        "1": "http://www.nfce.se.gov.br/nfce/qrcode?p=",
        "2": "http://www.hom.nfe.se.gov.br/nfce/qrcode?p=",
    },
    "SP": {
        "1": "https://www.nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaQRCode.aspx?p=",
        "2": "https://www.homologacao.nfce.fazenda.sp.gov.br/NFCeConsultaPublica/Paginas/ConsultaQRCode.aspx?p=",
    },
    "TO": {
        "1": "http://www.sefaz.to.gov.br/nfce/qrcode?p=",
        "2": "http://homologacao.sefaz.to.gov.br/nfce/qrcode?p=",
    },
}

# URL para a consulta pública de NFC-e por chave de acesso
ESTADO_CONSULTA_NFCE = {
    "AC": {
        "1": "www.sefaznet.ac.gov.br/nfce/consulta",
        "2": "www.sefaznet.ac.gov.br/nfce/consulta",
    },
    "AL": {
        "1": "www.sefaz.al.gov.br/nfce/consulta",
        "2": "www.sefaz.al.gov.br/nfce/consulta",
    },
    "AM": {
        "1": "www.sefaz.am.gov.br/nfce/consulta",
        "2": "www.sefaz.am.gov.br/nfce/consulta",
    },
    "AP": {
        "1": "www.sefaz.ap.gov.br/nfce/consulta",
        "2": "www.sefaz.ap.gov.br/nfce/consulta",
    },
    "BA": {
        "1": "www.sefaz.ba.gov.br/nfce/consulta",
        "2": "http://hinternet.sefaz.ba.gov.br/nfce/consulta",
    },
    "CE": {
        "1": "www.sefaz.ce.gov.br/nfce/consulta",
        "2": "www.sefaz.ce.gov.br/nfce/consulta",
    },
    "DF": {
        "1": "www.fazenda.df.gov.br/nfce/consulta",
        "2": "www.fazenda.df.gov.br/nfce/consulta",
    },
    "ES": {
        "1": "www.sefaz.es.gov.br/nfce/consulta",
        "2": "www.sefaz.es.gov.br/nfce/consulta",
    },
    "GO": {
        "1": "www.sefaz.go.gov.br/nfce/consulta",
        "2": "www.sefaz.go.gov.br/nfce/consulta",
    },
    "MA": {
        "1": "www.sefaz.ma.gov.br/nfce/consulta",
        "2": "www.sefaz.ma.gov.br/nfce/consulta",
    },
    "MG": {
        "1": "https://portalsped.fazenda.mg.gov.br/portalnfce",
        "2": "https://hportalsped.fazenda.mg.gov.br/portalnfce",
    },
    "MS": {
        "1": "www.dfe.ms.gov.br/nfce/consulta",
        "2": "www.dfe.ms.gov.br/nfce/consulta",
    },
    "MT": {
        "1": "http://www.sefaz.mt.gov.br/nfce/consultanfce",
        "2": "http://homologacao.sefaz.mt.gov.br/nfce/consultanfce",
    },
    "PA": {
        "1": "www.sefa.pa.gov.br/nfce/consulta",
        "2": "www.sefa.pa.gov.br/nfce/consulta",
    },
    "PB": {
        "1": "www.sefaz.pb.gov.br/nfce/consulta",
        "2": "www.sefaz.pb.gov.br/nfcehom",
    },
    "PE": {
        "1": "http://nfce.sefaz.pe.gov.br/nfce/consulta",
        "2": "http://nfce.sefaz.pe.gov.br/nfce/consulta",
    },
    "PI": {
        "1": "www.sefaz.pi.gov.br/nfce/consulta",
        "2": "www.sefaz.pi.gov.br/nfce/consulta",
    },
    "PR": {
        "1": "http://www.fazenda.pr.gov.br/nfce/consulta",
        "2": "http://www.fazenda.pr.gov.br/nfce/consulta",
    },
    "RJ": {
        "1": "www.fazenda.rj.gov.br/nfce/consulta",
        "2": "www.fazenda.rj.gov.br/nfce/consulta",
    },
    "RN": {
        "1": "www.set.rn.gov.br/nfce/consulta",
        "2": "www.set.rn.gov.br/nfce/consulta",
    },
    "RO": {
        "1": "www.sefin.ro.gov.br/nfce/consulta",
        "2": "www.sefin.ro.gov.br/nfce/consulta",
    },
    "RR": {
        "1": "www.sefaz.rr.gov.br/nfce/consulta",
        "2": "www.sefaz.rr.gov.br/nfce/consulta",
    },
    "RS": {
        "1": "www.sefaz.rs.gov.br/nfce/consulta",
        "2": "www.sefaz.rs.gov.br/nfce/consulta",
    },
    "SC": {
        "1": "https://sat.sef.sc.gov.br/nfce/consulta",
        "2": "https://hom.sat.sef.sc.gov.br/nfce/consulta",
    },
    "SE": {
        "1": "http://www.nfce.se.gov.br/nfce/consulta",
        "2": "http://www.hom.nfe.se.gov.br/nfce/consulta",
    },
    "SP": {
        "1": "https://www.nfce.fazenda.sp.gov.br/consulta",
        "2": "https://www.homologacao.nfce.fazenda.sp.gov.br/consulta",
    },
    "TO": {
        "1": "www.sefaz.to.gov.br/nfce/consulta",
        "2": "http://homologacao.sefaz.to.gov.br/nfce/consulta.jsf",
    },
}
