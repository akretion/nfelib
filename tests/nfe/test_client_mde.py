# FILEPATH: tests/nfe/test_mde_client.py
import logging
from os import environ
from pathlib import Path
from unittest import TestCase, mock

from decorator import decorate
from erpbrasil.assinatura import misc
from xsdata.formats.dataclass.transports import DefaultTransport

# --- Import Bindings ---
from nfelib.nfe_evento_mde.bindings.v1_0.leiaute_conf_recebto_v1_00 import TretEnvEvento

# --- Import Client ---
from nfelib.nfe.client.v4_0.mde import MdeClient

_logger = logging.getLogger(__name__)

# --- Mock SOAP Responses ---
# Using the corrected response name that the FiscalClient will handle
response_confirmacao = b"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <nfeRecepcaoEventoNFResult xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeRecepcaoEvento4">
            <retEnvEvento versao="1.00" xmlns="http://www.portalfiscal.inf.br/nfe">
                <idLote>1</idLote><tpAmb>1</tpAmb><verAplic>AN_1.1.3</verAplic><cOrgao>91</cOrgao><cStat>128</cStat><xMotivo>Lote de evento processado</xMotivo>
                <retEvento versao="1.00"><infEvento><tpAmb>1</tpAmb><verAplic>AN_1.1.3</verAplic><cOrgao>91</cOrgao><cStat>135</cStat><xMotivo>Evento registrado e vinculado a NF-e</xMotivo><chNFe>35200309091076000144550010001807401003642343</chNFe><tpEvento>210200</tpEvento><xEvento>Confirmacao da Operacao</xEvento><nSeqEvento>1</nSeqEvento><dhRegEvento>2020-11-20T07:55:58-03:00</dhRegEvento><nProt>123456789012345</nProt></infEvento></retEvento>
            </retEnvEvento>
        </nfeRecepcaoEventoNFResult>
    </soap:Body>
</soap:Envelope>"""

response_ciencia = b"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <nfeRecepcaoEventoNFResult xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeRecepcaoEvento4">
            <retEnvEvento versao="1.00" xmlns="http://www.portalfiscal.inf.br/nfe">
                <idLote>1</idLote><tpAmb>1</tpAmb><verAplic>AN_1.1.3</verAplic><cOrgao>91</cOrgao><cStat>128</cStat><xMotivo>Lote de evento processado</xMotivo>
                <retEvento versao="1.00"><infEvento><tpAmb>1</tpAmb><verAplic>AN_1.1.3</verAplic><cOrgao>91</cOrgao><cStat>135</cStat><xMotivo>Evento registrado e vinculado a NF-e</xMotivo><chNFe>35200309091076000144550010001807401003642343</chNFe><tpEvento>210210</tpEvento><xEvento>Ciencia da Operacao</xEvento><nSeqEvento>1</nSeqEvento><dhRegEvento>2020-11-20T07:55:59-03:00</dhRegEvento><nProt>123456789012346</nProt></infEvento></retEvento>
            </retEnvEvento>
        </nfeRecepcaoEventoNFResult>
    </soap:Body>
</soap:Envelope>"""

response_desconhecimento = b"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <nfeRecepcaoEventoNFResult xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeRecepcaoEvento4">
            <retEnvEvento versao="1.00" xmlns="http://www.portalfiscal.inf.br/nfe">
                <idLote>1</idLote><tpAmb>1</tpAmb><verAplic>AN_1.1.3</verAplic><cOrgao>91</cOrgao><cStat>128</cStat><xMotivo>Lote de evento processado</xMotivo>
                <retEvento versao="1.00"><infEvento><tpAmb>1</tpAmb><verAplic>AN_1.1.3</verAplic><cOrgao>91</cOrgao><cStat>135</cStat><xMotivo>Evento registrado e vinculado a NF-e</xMotivo><chNFe>35200309091076000144550010001807401003642343</chNFe><tpEvento>210220</tpEvento><xEvento>Desconhecimento da Operacao</xEvento><nSeqEvento>1</nSeqEvento><dhRegEvento>2020-11-20T07:55:59-03:00</dhRegEvento><nProt>123456789012347</nProt></infEvento></retEvento>
            </retEnvEvento>
        </nfeRecepcaoEventoNFResult>
    </soap:Body>
</soap:Envelope>"""

response_operacao_nao_realizada = b"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Body>
        <nfeRecepcaoEventoNFResult xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeRecepcaoEvento4">
            <retEnvEvento versao="1.00" xmlns="http://www.portalfiscal.inf.br/nfe">
                <idLote>1</idLote><tpAmb>1</tpAmb><verAplic>AN_1.1.3</verAplic><cOrgao>91</cOrgao><cStat>128</cStat><xMotivo>Lote de evento processado</xMotivo>
                <retEvento versao="1.00"><infEvento><tpAmb>1</tpAmb><verAplic>AN_1.1.3</verAplic><cOrgao>91</cOrgao><cStat>135</cStat><xMotivo>Evento registrado e vinculado a NF-e</xMotivo><chNFe>35200309091076000144550010001807401003642343</chNFe><tpEvento>210240</tpEvento><xEvento>Operacao nao Realizada</xEvento><nSeqEvento>1</nSeqEvento><dhRegEvento>2020-11-20T07:55:59-03:00</dhRegEvento><nProt>123456789012348</nProt></infEvento></retEvento>
            </retEnvEvento>
        </nfeRecepcaoEventoNFResult>
    </soap:Body>
</soap:Envelope>"""

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


# --- Test Case ---
class MDeSoapTest(TestCase):
    """
    Tests MdeClient SOAP interactions for Manifestação do Destinatário.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Certificate Setup
        if environ.get("CERT_FILE") and environ.get("CERT_PASSWORD"):
            cls.valid_certificate = True
            cert_path = Path(environ["CERT_FILE"])
            with open(cert_path, "rb") as pkcs12_file:
                cls.cert_data = pkcs12_file.read()
            cls.cert_password = environ["CERT_PASSWORD"]
            cls.fake_certificate = False
        else:
            cls.valid_certificate = False
            cls.cert_password = "testpassword"
            cls.cert_data = misc.create_fake_certificate_file(
                valid=True,
                passwd=cls.cert_password,
                issuer="EMISSOR A TESTE",
                country="BR",
                subject="CERTIFICADO VALIDO TESTE",
            )
            cls.fake_certificate = True

        # Client Setup
        # The UF here is for the company doing the manifestation, but the client will resolve the endpoint to AN.
        cls.client = MdeClient(
            ambiente="1",
            uf="35",  # UF of the destinatário
            pkcs12_data=cls.cert_data,
            pkcs12_password=cls.cert_password,
            fake_certificate=cls.fake_certificate,
            verify_ssl=False,
        )

        cls.chave = environ.get(
            "CHAVE_NFE", "35200309091076000144550010001807401003642343"
        )
        cls.cnpj_cpf = environ.get("CNPJ_CPF_DEST", "23765766000162")

    # --- Test Methods ---

    @mock.patch.object(DefaultTransport, "post")
    def test_confirmacao_da_operacao_mocked(self, mock_post):
        mock_post.return_value = response_confirmacao
        res = self.client.confirmacao_da_operacao(
            chave=self.chave, cnpj_cpf=self.cnpj_cpf
        )
        self.assertIsInstance(res, TretEnvEvento)
        self.assertEqual(res.cStat, "128")
        self.assertEqual(res.retEvento[0].infEvento.cStat, "135")
        self.assertEqual(res.retEvento[0].infEvento.tpEvento, "210200")

    @only_if_valid_certificate
    def test_confirmacao_da_operacao_real(self):
        res = self.client.confirmacao_da_operacao(
            chave=self.chave, cnpj_cpf=self.cnpj_cpf
        )
        self.assertIsInstance(res, TretEnvEvento)
        self.assertEqual(res.cStat, "128")
        self.assertIn(res.retEvento[0].infEvento.cStat, ["135", "573"])

    @mock.patch.object(DefaultTransport, "post")
    def test_ciencia_da_operacao_mocked(self, mock_post):
        mock_post.return_value = response_ciencia
        res = self.client.ciencia_da_operacao(
            chave=self.chave, cnpj_cpf=self.cnpj_cpf
        )
        self.assertIsInstance(res, TretEnvEvento)
        self.assertEqual(res.cStat, "128")
        self.assertEqual(res.retEvento[0].infEvento.cStat, "135")
        self.assertEqual(res.retEvento[0].infEvento.tpEvento, "210210")

    @only_if_valid_certificate
    def test_ciencia_da_operacao_real(self):
        res = self.client.ciencia_da_operacao(
            chave=self.chave, cnpj_cpf=self.cnpj_cpf
        )
        self.assertIsInstance(res, TretEnvEvento)
        self.assertEqual(res.cStat, "128")
        self.assertIn(res.retEvento[0].infEvento.cStat, ["135", "573"])

    @mock.patch.object(DefaultTransport, "post")
    def test_desconhecimento_da_operacao_mocked(self, mock_post):
        mock_post.return_value = response_desconhecimento
        res = self.client.desconhecimento_da_operacao(
            chave=self.chave, cnpj_cpf=self.cnpj_cpf
        )
        self.assertIsInstance(res, TretEnvEvento)
        self.assertEqual(res.cStat, "128")
        self.assertEqual(res.retEvento[0].infEvento.cStat, "135")
        self.assertEqual(res.retEvento[0].infEvento.tpEvento, "210220")

    @only_if_valid_certificate
    def test_desconhecimento_da_operacao_real(self):
        res = self.client.desconhecimento_da_operacao(
            chave=self.chave, cnpj_cpf=self.cnpj_cpf
        )
        self.assertIsInstance(res, TretEnvEvento)
        self.assertEqual(res.cStat, "128")
        self.assertIn(res.retEvento[0].infEvento.cStat, ["135", "573"])

    @mock.patch.object(DefaultTransport, "post")
    def test_operacao_nao_realizada_mocked(self, mock_post):
        mock_post.return_value = response_operacao_nao_realizada
        res = self.client.operacao_nao_realizada(
            chave=self.chave,
            cnpj_cpf=self.cnpj_cpf,
            justificativa="Justificativa de teste com mais de 15 caracteres",
        )
        self.assertIsInstance(res, TretEnvEvento)
        self.assertEqual(res.cStat, "128")
        self.assertEqual(res.retEvento[0].infEvento.cStat, "135")
        self.assertEqual(res.retEvento[0].infEvento.tpEvento, "210240")

    @only_if_valid_certificate
    def test_operacao_nao_realizada_real(self):
        res = self.client.operacao_nao_realizada(
            chave=self.chave,
            cnpj_cpf=self.cnpj_cpf,
            justificativa="Teste de operacao nao realizada para fins de auditoria.",
        )
        self.assertIsInstance(res, TretEnvEvento)
        self.assertEqual(res.cStat, "128")
        self.assertIn(res.retEvento[0].infEvento.cStat, ["135", "573"])
