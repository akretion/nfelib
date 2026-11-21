# Copyright (C) 2026 - TODAY KMEE

import base64
import gzip
from pathlib import Path
from unittest import TestCase, mock

from erpbrasil.assinatura import misc
from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.transports import DefaultTransport

from nfelib.nfgas.bindings.v1_0 import (
    RetConsSitNfgas,
    RetConsStatServNfgas,
    RetEventoNfgas,
    RetNfgas,
)
from nfelib.nfgas.bindings.v1_0.nfgas_v1_00 import Nfgas
from nfelib.nfgas.client.v1_0.nfgas import NfgasClient
from nfelib.nfgas.client.v1_0.servers import Endpoint

NFGAS_NS = "http://www.portalfiscal.inf.br/nfgas"
DS_NS = "http://www.w3.org/2000/09/xmldsig#"
CHAVE = "35261159594315000157760010000001231045678910"

SOAP_RESPONSE = (
    '<?xml version="1.0" encoding="utf-8"?>'
    '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
    "<soap:Body>"
    '<nfgasResultMsg xmlns="http://www.portalfiscal.inf.br/NFGas/wsdl/{service}">'
    "{content}</nfgasResultMsg></soap:Body></soap:Envelope>"
)

RET_CONS_STAT_SERV = (
    '<retConsStatServNFGas xmlns="http://www.portalfiscal.inf.br/nfgas" '
    'versao="1.00"><tpAmb>2</tpAmb><verAplic>RS20261030</verAplic>'
    "<cStat>107</cStat><xMotivo>Servico em Operacao</xMotivo><cUF>35</cUF>"
    "<dhRecbto>2026-11-21T10:00:00-03:00</dhRecbto></retConsStatServNFGas>"
)

RET_CONS_SIT = (
    '<retConsSitNFGas xmlns="http://www.portalfiscal.inf.br/nfgas" versao="1.00">'
    "<tpAmb>2</tpAmb><verAplic>RS20261030</verAplic><cStat>100</cStat>"
    "<xMotivo>Autorizado o uso da NFGas</xMotivo><cUF>35</cUF></retConsSitNFGas>"
)

RET_NFGAS = (
    '<retNFGas xmlns="http://www.portalfiscal.inf.br/nfgas" versao="1.00">'
    "<tpAmb>2</tpAmb><cUF>35</cUF><verAplic>RS20261030</verAplic>"
    "<cStat>100</cStat><xMotivo>Autorizado o uso da NFGas</xMotivo>"
    '<protNFGas versao="1.00"><infProt>'
    "<tpAmb>2</tpAmb><verAplic>RS20261030</verAplic>"
    f"<chNFGas>{CHAVE}</chNFGas><dhRecbto>2026-11-21T10:00:01-03:00</dhRecbto>"
    "<nProt>3762600000000001</nProt><digVal>bm90LWNoZWNrZWQ=</digVal>"
    "<cStat>100</cStat><xMotivo>Autorizado o uso da NFGas</xMotivo>"
    "</infProt></protNFGas></retNFGas>"
)

RET_EVENTO = (
    '<retEventoNFGas xmlns="http://www.portalfiscal.inf.br/nfgas" versao="1.00">'
    "<infEvento><tpAmb>2</tpAmb><verAplic>RS20261030</verAplic>"
    "<cOrgao>35</cOrgao><cStat>135</cStat>"
    "<xMotivo>Evento registrado e vinculado a NFGas</xMotivo>"
    f"<chNFGas>{CHAVE}</chNFGas><tpEvento>110111</tpEvento>"
    "<xEvento>Cancelamento</xEvento><nSeqEvento>1</nSeqEvento>"
    "<dhRegEvento>2026-11-21T10:05:00-03:00</dhRegEvento>"
    "<nProt>3762600000000002</nProt></infEvento></retEventoNFGas>"
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
    """Return the nfgasDadosMsg element of the posted SOAP envelope."""
    data = mock_post.call_args.kwargs["data"]
    envelope = etree.fromstring(data)
    return envelope.find(".//{*}nfgasDadosMsg")


class NfgasClientTest(TestCase):
    """Tests NfgasClient against a simulated authorizer."""

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
        nfgas_path = (
            Path(__file__).parent.parent.parent
            / "nfelib/nfgas/samples/v1_0/nfgas-v1_00.xml"
        )
        cls.nfgas_obj = XmlParser().from_path(nfgas_path, Nfgas)
        cls.client = cls.make_client()

    @classmethod
    def make_client(cls, ambiente="2", **kwargs):
        return NfgasClient(
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
        mock_post.return_value = response("NFGasStatusServico", RET_CONS_STAT_SERV)
        res = self.client.status_servico()
        self.assertIsInstance(res, RetConsStatServNfgas)
        self.assertEqual(res.cStat, "107")

        location = mock_post.call_args.args[0]
        self.assertEqual(
            location,
            "https://nfgas-homologacao.svrs.rs.gov.br"
            "/WS/NFGasStatusServico/NFGasStatusServico.asmx",
        )
        headers = mock_post.call_args.kwargs["headers"]
        self.assertIn("application/soap+xml", headers["content-type"])
        self.assertIn(
            'action="http://www.portalfiscal.inf.br/NFGas/wsdl/NFGasStatusServico'
            '/NFGasStatusServicoNF"',
            headers["content-type"],
        )
        data = mock_post.call_args.kwargs["data"].decode()
        self.assertIn("http://www.w3.org/2003/05/soap-envelope", data)
        self.assertNotIn("Header", data)
        message = dados_msg(mock_post)
        self.assertEqual(message[0].tag, f"{{{NFGAS_NS}}}consStatServNFGas")

    @mock.patch.object(DefaultTransport, "post")
    def test_consulta_documento(self, mock_post):
        mock_post.return_value = response("NFGasConsulta", RET_CONS_SIT)
        res = self.client.consulta_documento(CHAVE)
        self.assertIsInstance(res, RetConsSitNfgas)
        self.assertEqual(res.cStat, "100")
        self.assertEqual(
            dados_msg(mock_post).findtext(f".//{{{NFGAS_NS}}}chNFGas"), CHAVE
        )

    @mock.patch.object(DefaultTransport, "post")
    def test_envia_documento(self, mock_post):
        """The signed NFGas goes gzipped and base64 encoded."""
        mock_post.return_value = response("NFGasRecepcao", RET_NFGAS)
        res = self.client.envia_documento(self.nfgas_obj)
        self.assertIsInstance(res, RetNfgas)
        self.assertEqual(res.protNFGas.infProt.nProt, "3762600000000001")

        sent = gzip.decompress(base64.b64decode(dados_msg(mock_post).text))
        nfgas = etree.fromstring(sent)
        self.assertEqual(nfgas.tag, f"{{{NFGAS_NS}}}NFGas")
        self.assertIsNotNone(nfgas.find(f"{{{DS_NS}}}Signature"))

    @mock.patch.object(DefaultTransport, "post")
    def test_cancela_documento(self, mock_post):
        mock_post.return_value = response("NFGasRecepcaoEvento", RET_EVENTO)
        res = self.client.cancela_documento(
            CHAVE, "3762600000000001", "Fatura emitida em duplicidade", "59594315000157"
        )
        self.assertIsInstance(res, RetEventoNfgas)
        self.assertEqual(res.infEvento.cStat, "135")

        evento = dados_msg(mock_post)[0]
        self.assertEqual(evento.tag, f"{{{NFGAS_NS}}}eventoNFGas")
        inf_evento = evento.find(f"{{{NFGAS_NS}}}infEvento")
        self.assertEqual(inf_evento.get("Id"), f"ID110111{CHAVE}001")
        self.assertIsNotNone(evento.find(f"{{{DS_NS}}}Signature"))

    @mock.patch.object(DefaultTransport, "post")
    def test_wrap_response(self, mock_post):
        mock_post.return_value = response("NFGasStatusServico", RET_CONS_STAT_SERV)
        res = self.make_client(wrap_response=True).status_servico()
        self.assertIsInstance(res.resposta, RetConsStatServNfgas)
        self.assertEqual(res.webservice, "NFGasStatusServicoNF")

    @mock.patch.object(DefaultTransport, "post")
    def test_soap_fault(self, mock_post):
        mock_post.return_value = SOAP_FAULT.encode()
        with self.assertRaises(ValueError):
            self.client.status_servico()

    def test_production_location(self):
        location = self.make_client(ambiente="1")._get_location(Endpoint.NFGASRECEPCAO)
        self.assertEqual(
            location,
            "https://nfgas.svrs.rs.gov.br/WS/NFGasRecepcao/NFGasRecepcao.asmx",
        )
