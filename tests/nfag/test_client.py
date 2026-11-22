# Copyright (C) 2026 - TODAY KMEE

import base64
import gzip
from pathlib import Path
from unittest import TestCase, mock

from erpbrasil.assinatura import misc
from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.transports import DefaultTransport

from nfelib.nfag.bindings.v1_0 import (
    RetConsSitNfag,
    RetConsStatServNfag,
    RetEventoNfag,
    RetNfag,
)
from nfelib.nfag.bindings.v1_0.nfag_v1_00 import Nfag
from nfelib.nfag.client.v1_0.nfag import NfagClient
from nfelib.nfag.client.v1_0.servers import Endpoint

NFAG_NS = "http://www.portalfiscal.inf.br/nfag"
DS_NS = "http://www.w3.org/2000/09/xmldsig#"
CHAVE = "35261159594315000157750010000001231045678910"

SOAP_RESPONSE = (
    '<?xml version="1.0" encoding="utf-8"?>'
    '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
    "<soap:Body>"
    '<nfagResultMsg xmlns="http://www.portalfiscal.inf.br/NFAg/wsdl/{service}">'
    "{content}</nfagResultMsg></soap:Body></soap:Envelope>"
)

RET_CONS_STAT_SERV = (
    '<retConsStatServNFAg xmlns="http://www.portalfiscal.inf.br/nfag" '
    'versao="1.00"><tpAmb>2</tpAmb><verAplic>RS20261030</verAplic>'
    "<cStat>107</cStat><xMotivo>Servico em Operacao</xMotivo><cUF>35</cUF>"
    "<dhRecbto>2026-11-21T10:00:00-03:00</dhRecbto></retConsStatServNFAg>"
)

RET_CONS_SIT = (
    '<retConsSitNFAg xmlns="http://www.portalfiscal.inf.br/nfag" versao="1.00">'
    "<tpAmb>2</tpAmb><verAplic>RS20261030</verAplic><cStat>100</cStat>"
    "<xMotivo>Autorizado o uso da NFAg</xMotivo><cUF>35</cUF></retConsSitNFAg>"
)

RET_NFAG = (
    '<retNFAg xmlns="http://www.portalfiscal.inf.br/nfag" versao="1.00">'
    "<tpAmb>2</tpAmb><cUF>35</cUF><verAplic>RS20261030</verAplic>"
    "<cStat>100</cStat><xMotivo>Autorizado o uso da NFAg</xMotivo>"
    '<protNFAg versao="1.00"><infProt>'
    "<tpAmb>2</tpAmb><verAplic>RS20261030</verAplic>"
    f"<chNFAg>{CHAVE}</chNFAg><dhRecbto>2026-11-21T10:00:01-03:00</dhRecbto>"
    "<nProt>3762600000000001</nProt><digVal>bm90LWNoZWNrZWQ=</digVal>"
    "<cStat>100</cStat><xMotivo>Autorizado o uso da NFAg</xMotivo>"
    "</infProt></protNFAg></retNFAg>"
)

RET_EVENTO = (
    '<retEventoNFAg xmlns="http://www.portalfiscal.inf.br/nfag" versao="1.00">'
    "<infEvento><tpAmb>2</tpAmb><verAplic>RS20261030</verAplic>"
    "<cOrgao>35</cOrgao><cStat>135</cStat>"
    "<xMotivo>Evento registrado e vinculado a NFAg</xMotivo>"
    f"<chNFAg>{CHAVE}</chNFAg><tpEvento>110111</tpEvento>"
    "<xEvento>Cancelamento</xEvento><nSeqEvento>1</nSeqEvento>"
    "<dhRegEvento>2026-11-21T10:05:00-03:00</dhRegEvento>"
    "<nProt>3762600000000002</nProt></infEvento></retEventoNFAg>"
)

SOAP_FAULT = (
    '<?xml version="1.0" encoding="utf-8"?>'
    '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
    "<soap:Body><soap:Fault><faultcode>soap:Server</faultcode>"
    "<faultstring>Server was unable to process request</faultstring>"
    "</soap:Fault></soap:Body></soap:Envelope>"
)


def response(service, content):
    return SOAP_RESPONSE.format(service=service, content=content).encode()


def dados_msg(mock_post):
    """Return the nfagDadosMsg element of the posted SOAP envelope."""
    data = mock_post.call_args.kwargs["data"]
    envelope = etree.fromstring(data)
    return envelope.find(".//{*}nfagDadosMsg")


class NfagClientTest(TestCase):
    """Tests NfagClient against a simulated authorizer."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.cert_password = "testpassword"
        cls.cert_data = misc.create_fake_certificate_file(
            valid=True,
            passwd=cls.cert_password,
            issuer="TEST ISSUER",
            country="BR",
            subject="TEST SUBJECT",
        )
        nfag_path = (
            Path(__file__).parent.parent.parent
            / "nfelib/nfag/samples/v1_0/nfag-v1_00.xml"
        )
        cls.nfag_obj = XmlParser().from_path(nfag_path, Nfag)
        cls.client = cls.make_client()

    @classmethod
    def make_client(cls, ambiente="2", **kwargs):
        return NfagClient(
            ambiente=ambiente,
            uf="35",
            pkcs12_data=cls.cert_data,
            pkcs12_password=cls.cert_password,
            fake_certificate=True,
            verify_ssl=False,
            **kwargs,
        )

    @mock.patch.object(DefaultTransport, "post")
    def test_status_servico(self, mock_post):
        mock_post.return_value = response("NFAgStatusServico", RET_CONS_STAT_SERV)
        res = self.client.status_servico()
        self.assertIsInstance(res, RetConsStatServNfag)
        self.assertEqual(res.cStat, "107")

        location = mock_post.call_args.args[0]
        self.assertEqual(
            location,
            "https://nfag-homologacao.svrs.rs.gov.br"
            "/WS/NFAgStatusServico/NFAgStatusServico.asmx",
        )
        headers = mock_post.call_args.kwargs["headers"]
        self.assertIn("application/soap+xml", headers["content-type"])
        self.assertIn(
            'action="http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgStatusServico'
            '/NFAgStatusServicoNF"',
            headers["content-type"],
        )
        data = mock_post.call_args.kwargs["data"].decode()
        self.assertIn("http://www.w3.org/2003/05/soap-envelope", data)
        self.assertNotIn("Header", data)
        message = dados_msg(mock_post)
        self.assertEqual(message[0].tag, f"{{{NFAG_NS}}}consStatServNFAg")

    @mock.patch.object(DefaultTransport, "post")
    def test_consulta_documento(self, mock_post):
        mock_post.return_value = response("NFAgConsulta", RET_CONS_SIT)
        res = self.client.consulta_documento(CHAVE)
        self.assertIsInstance(res, RetConsSitNfag)
        self.assertEqual(res.cStat, "100")
        self.assertEqual(
            dados_msg(mock_post).findtext(f".//{{{NFAG_NS}}}chNFAg"), CHAVE
        )

    @mock.patch.object(DefaultTransport, "post")
    def test_envia_documento(self, mock_post):
        """The signed NFAg goes gzipped and base64 encoded."""
        mock_post.return_value = response("NFAgRecepcao", RET_NFAG)
        res = self.client.envia_documento(self.nfag_obj)
        self.assertIsInstance(res, RetNfag)
        self.assertEqual(res.protNFAg.infProt.nProt, "3762600000000001")

        sent = gzip.decompress(base64.b64decode(dados_msg(mock_post).text))
        nfag = etree.fromstring(sent)
        self.assertEqual(nfag.tag, f"{{{NFAG_NS}}}NFAg")
        self.assertIsNotNone(nfag.find(f"{{{DS_NS}}}Signature"))

    @mock.patch.object(DefaultTransport, "post")
    def test_cancela_documento(self, mock_post):
        mock_post.return_value = response("NFAgRecepcaoEvento", RET_EVENTO)
        res = self.client.cancela_documento(
            CHAVE, "3762600000000001", "Conta emitida em duplicidade", "59594315000157"
        )
        self.assertIsInstance(res, RetEventoNfag)
        self.assertEqual(res.infEvento.cStat, "135")

        evento = dados_msg(mock_post)[0]
        self.assertEqual(evento.tag, f"{{{NFAG_NS}}}eventoNFAg")
        inf_evento = evento.find(f"{{{NFAG_NS}}}infEvento")
        self.assertEqual(inf_evento.get("Id"), f"ID110111{CHAVE}001")
        self.assertIsNotNone(evento.find(f"{{{DS_NS}}}Signature"))

    @mock.patch.object(DefaultTransport, "post")
    def test_wrap_response(self, mock_post):
        mock_post.return_value = response("NFAgStatusServico", RET_CONS_STAT_SERV)
        res = self.make_client(wrap_response=True).status_servico()
        self.assertIsInstance(res.resposta, RetConsStatServNfag)
        self.assertEqual(res.webservice, "NFAgStatusServicoNF")

    @mock.patch.object(DefaultTransport, "post")
    def test_soap_fault(self, mock_post):
        mock_post.return_value = SOAP_FAULT.encode()
        with self.assertRaises(ValueError):
            self.client.status_servico()

    def test_production_location(self):
        location = self.make_client(ambiente="1")._get_location(Endpoint.NFAGRECEPCAO)
        self.assertEqual(
            location,
            "https://nfag.svrs.rs.gov.br/WS/NFAgRecepcao/NFAgRecepcao.asmx",
        )
