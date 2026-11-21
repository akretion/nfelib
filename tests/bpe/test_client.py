# Copyright (C) 2026 - TODAY KMEE

import base64
import gzip
from pathlib import Path
from unittest import TestCase, mock

from erpbrasil.assinatura import misc
from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.transports import DefaultTransport

from nfelib.bpe.bindings.v1_0 import (
    RetBpe,
    RetConsSitBpe,
    RetConsStatServBpe,
    RetEventoBpe,
)
from nfelib.bpe.bindings.v1_0.bpe_v1_00 import Bpe
from nfelib.bpe.client.v1_0.bpe import BpeClient
from nfelib.bpe.client.v1_0.servers import Endpoint

BPE_NS = "http://www.portalfiscal.inf.br/bpe"
DS_NS = "http://www.w3.org/2000/09/xmldsig#"
CHAVE = "43240100000000000100630010000000011000000017"

SOAP_RESPONSE = (
    '<?xml version="1.0" encoding="utf-8"?>'
    '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
    "<soap:Body>"
    '<bpeResultMsg xmlns="http://www.portalfiscal.inf.br/bpe/wsdl/{service}">'
    "{content}</bpeResultMsg></soap:Body></soap:Envelope>"
)

RET_CONS_STAT_SERV = (
    '<retConsStatServBPe xmlns="http://www.portalfiscal.inf.br/bpe" versao="1.00">'
    "<tpAmb>2</tpAmb><verAplic>RS20240101</verAplic><cStat>107</cStat>"
    "<xMotivo>Servico em Operacao</xMotivo><cUF>43</cUF>"
    "<dhRecbto>2026-11-21T10:00:00-03:00</dhRecbto></retConsStatServBPe>"
)

RET_CONS_SIT = (
    '<retConsSitBPe xmlns="http://www.portalfiscal.inf.br/bpe" versao="1.00">'
    "<tpAmb>2</tpAmb><verAplic>RS20240101</verAplic><cStat>100</cStat>"
    "<xMotivo>Autorizado o uso do BP-e</xMotivo><cUF>43</cUF></retConsSitBPe>"
)

RET_BPE = (
    '<retBPe xmlns="http://www.portalfiscal.inf.br/bpe" versao="1.00">'
    "<tpAmb>2</tpAmb><cUF>43</cUF><verAplic>RS20240101</verAplic>"
    "<cStat>100</cStat><xMotivo>Autorizado o uso do BP-e</xMotivo>"
    '<protBPe versao="1.00"><infProt>'
    "<tpAmb>2</tpAmb><verAplic>RS20240101</verAplic>"
    f"<chBPe>{CHAVE}</chBPe><dhRecbto>2026-11-21T10:00:01-03:00</dhRecbto>"
    "<nProt>143260000000001</nProt><digVal>bm90LWNoZWNrZWQ=</digVal>"
    "<cStat>100</cStat><xMotivo>Autorizado o uso do BP-e</xMotivo>"
    "</infProt></protBPe></retBPe>"
)

RET_EVENTO = (
    '<retEventoBPe xmlns="http://www.portalfiscal.inf.br/bpe" versao="1.00">'
    "<infEvento><tpAmb>2</tpAmb><verAplic>RS20240101</verAplic>"
    "<cOrgao>43</cOrgao><cStat>135</cStat>"
    "<xMotivo>Evento registrado e vinculado a BP-e</xMotivo>"
    f"<chBPe>{CHAVE}</chBPe><tpEvento>110111</tpEvento>"
    "<xEvento>Cancelamento</xEvento><nSeqEvento>1</nSeqEvento>"
    "<dhRegEvento>2026-11-21T10:05:00-03:00</dhRegEvento>"
    "<nProt>143260000000002</nProt></infEvento></retEventoBPe>"
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
    """Return the bpeDadosMsg element of the posted SOAP envelope."""
    data = mock_post.call_args.kwargs["data"]
    envelope = etree.fromstring(data)
    return envelope.find(".//{*}bpeDadosMsg")


class BpeClientTest(TestCase):
    """Tests BpeClient against a simulated authorizer."""

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
        bpe_path = (
            Path(__file__).parent.parent.parent / "nfelib/bpe/samples/v1_0/bpe.xml"
        )
        cls.bpe_obj = XmlParser().from_path(bpe_path, Bpe)
        cls.client = cls.make_client(uf="43")  # Rio Grande do Sul: SVRS

    @classmethod
    def make_client(cls, ambiente="2", **kwargs):
        return BpeClient(
            ambiente=ambiente,
            pkcs12_data=cls.cert_data,
            pkcs12_password=cls.cert_password,
            fake_certificate=True,
            verify_ssl=False,
            **kwargs,
        )

    @mock.patch.object(DefaultTransport, "post")
    def test_status_servico(self, mock_post):
        mock_post.return_value = response("BPeStatusServico", RET_CONS_STAT_SERV)
        res = self.client.status_servico()
        self.assertIsInstance(res, RetConsStatServBpe)
        self.assertEqual(res.cStat, "107")

        location = mock_post.call_args.args[0]
        self.assertEqual(
            location,
            "https://bpe-homologacao.svrs.rs.gov.br"
            "/ws/bpeStatusServico/bpeStatusServico.asmx",
        )
        headers = mock_post.call_args.kwargs["headers"]
        self.assertIn("application/soap+xml", headers["content-type"])
        self.assertIn(
            'action="http://www.portalfiscal.inf.br/bpe/wsdl/BPeStatusServico'
            '/bpeStatusServicoBP"',
            headers["content-type"],
        )
        data = mock_post.call_args.kwargs["data"].decode()
        self.assertIn("http://www.w3.org/2003/05/soap-envelope", data)
        self.assertNotIn("Header", data)
        message = dados_msg(mock_post)
        self.assertEqual(message[0].tag, f"{{{BPE_NS}}}consStatServBPe")

    @mock.patch.object(DefaultTransport, "post")
    def test_consulta_documento(self, mock_post):
        mock_post.return_value = response("BPeConsulta", RET_CONS_SIT)
        res = self.client.consulta_documento(CHAVE)
        self.assertIsInstance(res, RetConsSitBpe)
        self.assertEqual(res.cStat, "100")
        self.assertEqual(dados_msg(mock_post).findtext(f".//{{{BPE_NS}}}chBPe"), CHAVE)

    @mock.patch.object(DefaultTransport, "post")
    def test_envia_documento(self, mock_post):
        """The signed BP-e goes gzipped and base64 encoded (MOC item 3.4)."""
        mock_post.return_value = response("BPeRecepcao", RET_BPE)
        res = self.client.envia_documento(self.bpe_obj)
        self.assertIsInstance(res, RetBpe)
        self.assertEqual(res.protBPe.infProt.nProt, "143260000000001")

        sent = gzip.decompress(base64.b64decode(dados_msg(mock_post).text))
        bpe = etree.fromstring(sent)
        self.assertEqual(bpe.tag, f"{{{BPE_NS}}}BPe")
        self.assertIsNotNone(bpe.find(f"{{{DS_NS}}}Signature"))

    @mock.patch.object(DefaultTransport, "post")
    def test_cancela_documento(self, mock_post):
        mock_post.return_value = response("BPeRecepcaoEvento", RET_EVENTO)
        res = self.client.cancela_documento(
            CHAVE, "143260000000001", "Viagem cancelada pela empresa", "00000000000100"
        )
        self.assertIsInstance(res, RetEventoBpe)
        self.assertEqual(res.infEvento.cStat, "135")

        evento = dados_msg(mock_post)[0]
        self.assertEqual(evento.tag, f"{{{BPE_NS}}}eventoBPe")
        inf_evento = evento.find(f"{{{BPE_NS}}}infEvento")
        self.assertEqual(inf_evento.get("Id"), f"ID110111{CHAVE}01")
        self.assertIsNotNone(evento.find(f"{{{DS_NS}}}Signature"))

    @mock.patch.object(DefaultTransport, "post")
    def test_wrap_response(self, mock_post):
        mock_post.return_value = response("BPeStatusServico", RET_CONS_STAT_SERV)
        client = self.make_client(uf="43", wrap_response=True)
        res = client.status_servico()
        self.assertIsInstance(res.resposta, RetConsStatServBpe)
        self.assertEqual(res.webservice, "bpeStatusServicoBP")

    @mock.patch.object(DefaultTransport, "post")
    def test_soap_fault(self, mock_post):
        mock_post.return_value = SOAP_FAULT.encode()
        with self.assertRaises(ValueError):
            self.client.status_servico()

    def test_location_by_uf(self):
        """MG, MS, MT, PR and SP have their own authorizer, the others SVRS."""
        for uf, prefix in (
            ("35", "https://homologacao.bpe.fazenda.sp.gov.br/"),
            ("31", "https://hbpe.fazenda.mg.gov.br/"),
            ("29", "https://bpe-homologacao.svrs.rs.gov.br/"),
        ):
            location = self.make_client(uf=uf)._get_location(Endpoint.BPERECEPCAO)
            self.assertTrue(location.startswith(prefix), location)
        location = self.make_client(ambiente="1", uf="29")._get_location(
            Endpoint.BPERECEPCAO
        )
        self.assertEqual(
            location, "https://bpe.svrs.rs.gov.br/ws/bpeRecepcao/bpeRecepcao.asmx"
        )
