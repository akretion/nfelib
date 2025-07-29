# FILEPATH: tests/mdfe/test_client.py
import logging
from os import environ
from pathlib import Path
from unittest import TestCase, mock

from decorator import decorate
from erpbrasil.assinatura import misc
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.transports import DefaultTransport

# --- Import Bindings ---
from nfelib.mdfe.bindings.v3_0 import (
    RetConsStatServMdfe,
    RetEnviMdfe,
    Tmdfe,
)

# --- Import Client ---
from nfelib.mdfe.client.v3_0.mdfe import MdfeClient

_logger = logging.getLogger(__name__)

# --- Mock SOAP Responses ---
response_status_servico = b"""<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
    <soap12:Header>
        <mdfeCabecMsg xmlns="http://www.portalfiscal.inf.br/mdfe/wsdl/MDFeStatusServico">
            <cUF>41</cUF>
            <versaoDados>3.00</versaoDados>
        </mdfeCabecMsg>
    </soap12:Header>
    <soap12:Body>
        <mdfeStatusServicoMDFResult xmlns="http://www.portalfiscal.inf.br/mdfe/wsdl/MDFeStatusServico">
            <retConsStatServMDFe versao="3.00" xmlns="http://www.portalfiscal.inf.br/mdfe">
                <tpAmb>2</tpAmb>
                <verAplic>MDFe_2.2.2</verAplic>
                <cStat>107</cStat>
                <xMotivo>Servico em Operacao</xMotivo>
                <cUF>41</cUF>
                <dhRecbto>2024-02-15T15:00:00-03:00</dhRecbto>
                <tMed>1</tMed>
            </retConsStatServMDFe>
        </mdfeStatusServicoMDFResult>
    </soap12:Body>
</soap12:Envelope>
"""

response_envia_documento = b"""<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
    <soap12:Body>
        <mdfeRecepcaoResult xmlns="http://www.portalfiscal.inf.br/mdfe/wsdl/MDFeRecepcaoSinc">
            <retEnviMDFe versao="3.00" xmlns="http://www.portalfiscal.inf.br/mdfe">
                <tpAmb>2</tpAmb>
                <cUF>41</cUF>
                <verAplic>MDFe_2.2.2</verAplic>
                <cStat>104</cStat>
                <xMotivo>Lote processado</xMotivo>
                <protMDFe versao="3.00">
                    <infProt>
                        <tpAmb>2</tpAmb>
                        <verAplic>MDFe_2.2.2</verAplic>
                        <chMDFe>41240200000000000100580010000000101000000104</chMDFe>
                        <dhRecbto>2024-02-15T15:01:00-03:00</dhRecbto>
                        <nProt>141000000000001</nProt>
                        <cStat>215</cStat>
                        <xMotivo>Rejeicao: Falha no schema XML</xMotivo>
                    </infProt>
                </protMDFe>
            </retEnviMDFe>
        </mdfeRecepcaoResult>
    </soap12:Body>
</soap12:Envelope>
"""

# Decorator for Certificate Check
def _only_if_valid_certificate(method, self):
    if self.valid_certificate:
        return method(self)
    _logger.info(
        f"Skipping test '{method.__name__}' because CERT_FILE and CERT_PASSWORD env vars are not set."
    )
    return lambda *args, **kwargs: None


def only_if_valid_certificate(method):
    return decorate(method, _only_if_valid_certificate)


class MdfeSoapTest(TestCase):
    """Tests MdfeClient SOAP interactions."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.valid_certificate = False
        cls.cert_password = "testpassword"
        cls.cert_data = misc.create_fake_certificate_file(
            valid=True,
            passwd=cls.cert_password,
            issuer="TEST ISSUER",
            country="BR",
            subject="TEST SUBJECT",
        )
        cls.fake_certificate = True
        
        mdfe_path = (
            Path(__file__).parent.parent.parent
            / "nfelib/mdfe/samples/v3_0/mdfe.xml"
        )
        if not mdfe_path.is_file():
            raise FileNotFoundError(f"MDF-e fixture not found: {mdfe_path}")

        cls.mdfe_obj = XmlParser().from_path(mdfe_path, Tmdfe)
        
        # Client for a state that uses SVRS
        cls.client = MdfeClient(
            ambiente="2",
            uf="41",  # Paraná
            pkcs12_data=cls.cert_data,
            pkcs12_password=cls.cert_password,
            fake_certificate=cls.fake_certificate,
            verify_ssl=False,
        )

    @mock.patch.object(DefaultTransport, "post")
    def test_status_servico_mocked(self, mock_post):
        mock_post.return_value = response_status_servico
        res = self.client.status_servico()
        self.assertIsInstance(res, RetConsStatServMdfe)
        self.assertEqual(res.cStat, "107")

    @mock.patch.object(DefaultTransport, "post")
    def test_envia_documento_mocked(self, mock_post):
        """Testa o envio síncrono de um MDF-e."""
        mock_post.return_value = response_envia_documento
        res = self.client.envia_documento(self.mdfe_obj)
        self.assertIsInstance(res, RetEnviMdfe)
        self.assertEqual(res.cStat, "104") # Lote Processado
        self.assertIsNotNone(res.protMDFe)
        self.assertEqual(res.protMDFe.infProt.cStat, "215")

    @only_if_valid_certificate
    def test_status_servico_real(self):
        """Testa a consulta de status de serviço (requer certificado válido)."""
        res = self.client.status_servico()
        self.assertIsInstance(res, RetConsStatServMdfe)
        self.assertEqual(res.cStat, "107")

    @only_if_valid_certificate
    def test_envia_documento_real(self):
        """
        Testa o envio de um MDF-e real.
        Espera-se uma rejeição, já que os dados são de exemplo.
        """
        # Adjusting the object to be valid for sending (e.g., current timestamp)
        self.mdfe_obj.infMDFe.ide.dhEmi = self.client._timestamp()
        
        res = self.client.envia_documento(self.mdfe_obj)
        self.assertIsInstance(res, RetEnviMdfe)
        self.assertEqual(res.cStat, "104")
        self.assertIsNotNone(res.protMDFe)
        # Check for common rejection codes in homologation
        self.assertNotEqual(res.protMDFe.infProt.cStat, "100") 
        _logger.info(f"Envio real rejeitado com: {res.protMDFe.infProt.xMotivo}")
