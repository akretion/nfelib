# Copyright (C) 2026 - TODAY KMEE

from pathlib import Path
from unittest import TestCase, mock

from erpbrasil.assinatura import misc
from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.transports import DefaultTransport

from nfelib.dce.bindings.v1_0 import (
    RetConsSitDce,
    RetConsStatServDce,
    RetDce,
    RetEventoDce,
)
from nfelib.dce.bindings.v1_0.dce_v1_00 import Dce
from nfelib.dce.client.v1_0.dce import DceClient
from nfelib.dce.client.v1_0.servers import Endpoint

DCE_NS = "http://www.portalfiscal.inf.br/dce"
DS_NS = "http://www.w3.org/2000/09/xmldsig#"
CHAVE = "35261111222333000181990010000000421105839212"

SOAP_RESPONSE = (
    '<?xml version="1.0" encoding="utf-8"?>'
    '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
    "<soap:Body>"
    '<{result} xmlns="http://www.portalfiscal.inf.br/dce/wsdl/{service}">'
    "{content}</{result}></soap:Body></soap:Envelope>"
)

RET_CONS_STAT_SERV = (
    '<retConsStatServDCe xmlns="http://www.portalfiscal.inf.br/dce" versao="1.00">'
    "<tpAmb>2</tpAmb><verAplic>PR-v1_0_0</verAplic><cStat>107</cStat>"
    "<xMotivo>Servico em Operacao</xMotivo><cUF>35</cUF>"
    "<dhRecbto>2026-11-21T10:00:00-03:00</dhRecbto></retConsStatServDCe>"
)

RET_CONS_SIT = (
    '<retConsSitDCe xmlns="http://www.portalfiscal.inf.br/dce" versao="1.00">'
    "<tpAmb>2</tpAmb><verAplic>PR-v1_0_0</verAplic><cStat>100</cStat>"
    "<xMotivo>Autorizado o uso da DCe</xMotivo><cUF>35</cUF></retConsSitDCe>"
)

RET_DCE = (
    '<retDCe xmlns="http://www.portalfiscal.inf.br/dce" versao="1.00">'
    "<tpAmb>2</tpAmb><verAplic>PR-v1_0_0</verAplic>"
    "<cStat>100</cStat><xMotivo>Autorizado o uso da DCe</xMotivo>"
    "<cUF>35</cUF><dhRecbto>2026-11-21T10:00:01-03:00</dhRecbto>"
    '<protDCe versao="1.00"><infProt>'
    "<tpAmb>2</tpAmb><verAplic>PR-v1_0_0</verAplic><chDCe>"
    f"{CHAVE}</chDCe><dhRecbto>2026-11-21T10:00:01-03:00</dhRecbto>"
    "<nProt>341260000000001</nProt><digVal>bm90LWNoZWNrZWQ=</digVal>"
    "<cStat>100</cStat><xMotivo>Autorizado o uso da DCe</xMotivo>"
    "</infProt></protDCe></retDCe>"
)

RET_EVENTO = (
    '<retEventoDCe xmlns="http://www.portalfiscal.inf.br/dce" versao="1.00">'
    "<infEvento><tpAmb>2</tpAmb><verAplic>PR-v1_0_0</verAplic>"
    "<cOrgao>35</cOrgao><cStat>135</cStat>"
    "<xMotivo>Evento registrado e vinculado a DCe</xMotivo>"
    f"<chDCe>{CHAVE}</chDCe><tpEvento>110111</tpEvento>"
    "<xEvento>Cancelamento</xEvento><nSeqEvento>1</nSeqEvento>"
    "<dhRegEvento>2026-11-21T10:05:00-03:00</dhRegEvento>"
    "<nProt>341260000000002</nProt></infEvento></retEventoDCe>"
)

SOAP_FAULT = (
    '<?xml version="1.0" encoding="utf-8"?>'
    '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">'
    "<soap:Body><soap:Fault><faultcode>soap:Server</faultcode>"
    "<faultstring>Server was unable to process request</faultstring>"
    "</soap:Fault></soap:Body></soap:Envelope>"
)


def response(service, result, content):
    return SOAP_RESPONSE.format(
        service=service, result=result, content=content
    ).encode()


def dados_msg(mock_post):
    """Return the dceDadosMsg element of the posted SOAP envelope."""
    data = mock_post.call_args.kwargs["data"]
    envelope = etree.fromstring(data)
    return envelope.find(".//{*}dceDadosMsg")


class DceClientTest(TestCase):
    """Tests DceClient against a simulated authorizer."""

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
        dce_path = (
            Path(__file__).parent.parent.parent
            / "nfelib/dce/samples/v1_0/dce-v1_00.xml"
        )
        cls.dce_obj = XmlParser().from_path(dce_path, Dce)
        cls.client = cls.make_client()

    @classmethod
    def make_client(cls, ambiente="2", **kwargs):
        return DceClient(
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
        mock_post.return_value = response(
            "DCeStatusServico", "dceStatusServicoResult", RET_CONS_STAT_SERV
        )
        res = self.client.status_servico()
        self.assertIsInstance(res, RetConsStatServDce)
        self.assertEqual(res.cStat, "107")

        # the portal lists the WSDL address: the request goes without ?wsdl
        location = mock_post.call_args.args[0]
        self.assertEqual(
            location, "https://homologacao.dce.fazenda.pr.gov.br/dce/DCeStatusServico"
        )
        headers = mock_post.call_args.kwargs["headers"]
        self.assertIn(
            'action="http://www.portalfiscal.inf.br/dce/wsdl/DCeStatusServico'
            '/dceStatusServico"',
            headers["content-type"],
        )
        message = dados_msg(mock_post)[0]
        self.assertEqual(message.tag, f"{{{DCE_NS}}}consStatServDCe")
        self.assertEqual(message.findtext(f"{{{DCE_NS}}}cUF"), "35")

    @mock.patch.object(DefaultTransport, "post")
    def test_result_msg_is_accepted(self, mock_post):
        """The answer element is not in the manual: dceResultMsg works too."""
        mock_post.return_value = response(
            "DCeStatusServico", "dceResultMsg", RET_CONS_STAT_SERV
        )
        self.assertEqual(self.client.status_servico().cStat, "107")

    @mock.patch.object(DefaultTransport, "post")
    def test_consulta_documento(self, mock_post):
        mock_post.return_value = response("DCeConsulta", "dceResultMsg", RET_CONS_SIT)
        res = self.client.consulta_documento(CHAVE)
        self.assertIsInstance(res, RetConsSitDce)
        self.assertEqual(res.cStat, "100")
        self.assertEqual(dados_msg(mock_post).findtext(f".//{{{DCE_NS}}}chDCe"), CHAVE)

    @mock.patch.object(DefaultTransport, "post")
    def test_envia_documento(self, mock_post):
        """The signed DC-e goes as is inside dceDadosMsg, without compression."""
        mock_post.return_value = response(
            "DCeAutorizacao", "dceAutorizacaoResult", RET_DCE
        )
        res = self.client.envia_documento(self.dce_obj)
        self.assertIsInstance(res, RetDce)
        self.assertEqual(res.protDCe.infProt.nProt, "341260000000001")

        dce = dados_msg(mock_post)[0]
        self.assertEqual(dce.tag, f"{{{DCE_NS}}}DCe")
        self.assertIsNotNone(dce.find(f"{{{DS_NS}}}Signature"))
        self.assertEqual(
            dce.find(f"{{{DCE_NS}}}infDCe").get("Id"), self.dce_obj.infDCe.Id
        )

    @mock.patch.object(DefaultTransport, "post")
    def test_cancela_documento(self, mock_post):
        mock_post.return_value = response(
            "DCeRecepcaoEvento", "dceRecepcaoEventoResult", RET_EVENTO
        )
        res = self.client.cancela_documento(
            CHAVE,
            "341260000000001",
            "Venda desfeita antes do envio",
            tp_emit="1",
            cnpj_autor="11222333000181",
            cnpj_cpf_emitente="12345678909",
        )
        self.assertIsInstance(res, RetEventoDce)
        self.assertEqual(res.infEvento.cStat, "135")

        evento = dados_msg(mock_post)[0]
        self.assertEqual(evento.tag, f"{{{DCE_NS}}}eventoDCe")
        inf_evento = evento.find(f"{{{DCE_NS}}}infEvento")
        self.assertEqual(inf_evento.get("Id"), f"ID110111{CHAVE}001")
        self.assertEqual(inf_evento.findtext(f"{{{DCE_NS}}}cOrgao"), "35")
        self.assertEqual(inf_evento.findtext(f"{{{DCE_NS}}}CPFUsEmit"), "12345678909")
        self.assertIsNotNone(evento.find(f"{{{DS_NS}}}Signature"))

    @mock.patch.object(DefaultTransport, "post")
    def test_soap_fault(self, mock_post):
        mock_post.return_value = SOAP_FAULT.encode()
        with self.assertRaises(ValueError):
            self.client.status_servico()

    def test_production_location(self):
        location = self.make_client(ambiente="1")._get_location(Endpoint.DCEAUTORIZACAO)
        self.assertEqual(location, "https://dce.fazenda.pr.gov.br/dce/DCeAutorizacao")
