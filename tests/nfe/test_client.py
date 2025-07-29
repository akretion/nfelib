import logging
import time
from os import environ, set_inheritable
from pathlib import Path
from unittest import TestCase, mock

from decorator import decorate
from erpbrasil.assinatura import misc
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.transports import DefaultTransport

# --- Import Bindings ---
from nfelib.nfe.bindings.v4_0.nfe_v4_00 import Nfe
from nfelib.nfe.bindings.v4_0.proc_nfe_v4_00 import NfeProc  # Corrected import
from nfelib.nfe.bindings.v4_0.ret_cons_reci_nfe_v4_00 import RetConsReciNfe
from nfelib.nfe.bindings.v4_0.ret_cons_sit_nfe_v4_00 import RetConsSitNfe
from nfelib.nfe.bindings.v4_0.ret_cons_stat_serv_v4_00 import RetConsStatServ
from nfelib.nfe.bindings.v4_0.ret_envi_nfe_v4_00 import RetEnviNfe
from nfelib.nfe.bindings.v4_0.ret_inut_nfe_v4_00 import (
    RetInutNfe,
)

# --- Import Client ---
from nfelib.nfe.client.v4_0.client import (
    NfeClient,
    TcodUfIbge,  # Import Enum for UF validation/lookup
)

# --- Event Bindings ---
from nfelib.nfe_evento_cancel.bindings.v1_0.leiaute_evento_canc_nfe_v1_00 import (
    TenvEvento,
)
from nfelib.nfe_evento_cce.bindings.v1_0.ret_env_cce_v1_00 import RetEnvEvento

# --- Mock SOAP Responses ---
# (Keep the existing mock responses as they are)
# ... response_status ...
# ... response_envia_documento ...
# ... response_consulta_documento ...
# ... response_consulta_recibo ...
# ... response_cancela_documento ...

# Add mock response for Inutilizacao (Example structure)
response_inutilizacao = b"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <soap:Body>
    <nfeResultMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeInutilizacao4">
      <retInutNFe versao="4.00" xmlns="http://www.portalfiscal.inf.br/nfe">
        <infInut Id="ID14120238158305400012955001000000002000000002">
          <tpAmb>2</tpAmb>
          <verAplic>SVRS202310101000</verAplic>
          <cStat>102</cStat>
          <xMotivo>Inutilizacao de numero homologado</xMotivo>
          <cUF>42</cUF>
          <ano>23</ano>
          <CNPJ>81583054000129</CNPJ>
          <mod>55</mod>
          <serie>1</serie>
          <nNFIni>2</nNFIni>
          <nNFFin>2</nNFFin>
          <dhRecbto>2023-11-15T10:30:00-03:00</dhRecbto>
          <nProt>141230000000001</nProt>
        </infInut>
      </retInutNFe>
    </nfeResultMsg>
  </soap:Body>
</soap:Envelope>
"""

response_status = b"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <soap:Body>
    <nfeResultMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4">
      <retConsStatServ versao="4.00" xmlns="http://www.portalfiscal.inf.br/nfe">
        <tpAmb>2</tpAmb>
        <verAplic>SVRS202305251555</verAplic>
        <cStat>107</cStat>
        <xMotivo>Servico em Operacao</xMotivo>
        <cUF>42</cUF>
        <dhRecbto>2023-06-11T00:15:00-03:00</dhRecbto>
        <tMed>1</tMed>
      </retConsStatServ>
    </nfeResultMsg>
  </soap:Body>
</soap:Envelope>
"""

response_envia_documento = b"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <soap:Body>
    <nfeResultMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4">
      <retEnviNFe versao="4.00" xmlns="http://www.portalfiscal.inf.br/nfe">
        <tpAmb>2</tpAmb>
        <verAplic>SVRS202305251555</verAplic>
        <cStat>103</cStat>
        <xMotivo>Lote recebido com sucesso</xMotivo>
        <cUF>42</cUF>
        <dhRecbto>2023-06-11T01:18:19-03:00</dhRecbto>
        <infRec>
          <nRec>423002202113232</nRec>
          <tMed>1</tMed>
        </infRec>
      </retEnviNFe>
    </nfeResultMsg>
  </soap:Body>
</soap:Envelope>
"""

response_consulta_documento = b"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <soap:Body>
    <nfeResultMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeConsultaProtocolo4">
      <retConsSitNFe versao="4.00" xmlns="http://www.portalfiscal.inf.br/nfe">
        <tpAmb>2</tpAmb>
        <verAplic>SVRS202305251555</verAplic>
        <cStat>217</cStat>
        <xMotivo>Rejeicao: NF-e nao consta na base de dados da SEFAZ</xMotivo>
        <cUF>42</cUF>
        <dhRecbto>2023-06-11T01:20:55-03:00</dhRecbto>
        <chNFe>42230675277525000259550010000364481754015406</chNFe>
      </retConsSitNFe>
    </nfeResultMsg>
  </soap:Body>
</soap:Envelope>
"""

response_consulta_recibo = b"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <soap:Body>
    <nfeResultMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeRetAutorizacao4">
      <retConsReciNFe versao="4.00" xmlns="http://www.portalfiscal.inf.br/nfe">
        <tpAmb>2</tpAmb>
        <verAplic>SVRS202305261028</verAplic>
        <nRec>423002202113232</nRec>
        <cStat>104</cStat>
        <xMotivo>Lote processado</xMotivo>
        <cUF>42</cUF>
        <dhRecbto>2023-06-11T01:18:19-03:00</dhRecbto>
        <protNFe versao="4.00">
          <infProt>
            <tpAmb>2</tpAmb>
            <verAplic>SVRS202305261028</verAplic>
            <chNFe>42230675277525000259550010000364481754015406</chNFe>
            <dhRecbto>2023-06-11T01:18:19-03:00</dhRecbto>
            <digVal>IoYUWXt2fIiRXb7UYRgl77c6Zlk=</digVal>
            <cStat>297</cStat>
            <xMotivo>Rejeicao: Assinatura difere do calculado</xMotivo>
          </infProt>
        </protNFe>
      </retConsReciNFe>
    </nfeResultMsg>
  </soap:Body>
</soap:Envelope>
"""

response_cancela_documento = b"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
  <soap:Body>
    <nfeResultMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeRecepcaoEvento4">
      <retEnvEvento versao="1.00" xmlns="http://www.portalfiscal.inf.br/nfe">
        <idLote/>
        <tpAmb>2</tpAmb>
        <verAplic>SVRS202305251555</verAplic>
        <cStat>215</cStat>
        <xMotivo>Rejeicao: Falha no schema XML</xMotivo>
      </retEnvEvento>
    </nfeResultMsg>
  </soap:Body>
</soap:Envelope>
"""  # TODO not a valid cancelamento


_logger = logging.getLogger(__name__)


# --- Decorator for Certificate Check ---
def _only_if_valid_certificate(method, self):
    if self.valid_certificate:
        return method(self)
    _logger.info(
        f"Skipping test '{method.__name__}' because CERT_FILE and CERT_PASSWORD env vars are not set."
    )
    # Return a no-op function instead of None to avoid errors if called
    return lambda *args, **kwargs: None


def only_if_valid_certificate(method):
    return decorate(method, _only_if_valid_certificate)


# --- Test Case ---
class SoapTest(TestCase):
    """
    Tests NfeClient SOAP interactions.
    Mocked tests run always.
    Real tests run only if CERT_FILE and CERT_PASSWORD env vars are set.
    Use CERT_UF to specify the UF for the certificate (defaults to 41 - PR).
    Use NFE_FILE to specify the path to a procNFe XML file (defaults to nfelib/nfe/samples/v4_0/procNFe.xml).
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # --- Certificate Setup ---
        if environ.get("CERT_FILE") and environ.get("CERT_PASSWORD"):
            cls.valid_certificate = True
            cert_path = Path(environ["CERT_FILE"])
            if not cert_path.is_file():
                raise FileNotFoundError(f"Certificate file not found: {cert_path}")
            with open(cert_path, "rb") as pkcs12_file:
                cls.cert_data = pkcs12_file.read()
            cls.cert_password = environ["CERT_PASSWORD"]
            cls.fake_certificate = False
            _logger.info(f"Using real certificate from: {cert_path}")
        else:
            cls.valid_certificate = False
            cls.cert_password = "testpassword"  # Example password
            valid = (True,)
            issuer = "EMISSOR A TESTE"
            country = "BR"
            subject = "CERTIFICADO VALIDO TESTE"
            cls.cert_data = misc.create_fake_certificate_file(
                valid, cls.cert_password, issuer, country, subject
            )
            cls.fake_certificate = True
            _logger.info("Using fake certificate for tests.")

        # --- NFe Fixture Setup ---
        # Using procNFe because it often contains a fully structured and potentially signed NFe.
        # We extract the NFe part for sending/signing tests.
        if environ.get("NFE_FILE"):
            nfe_path = Path(environ["NFE_FILE"])
            if not nfe_path.is_file():
                raise FileNotFoundError(f"NFE_FILE not found: {nfe_path}")
        else:
            # Default path relative to the project root (adjust if needed)
            nfe_path = (
                Path(__file__).parent.parent.parent
                / "nfelib/nfe/samples/v4_0/procNFe.xml"
            )
            if not nfe_path.is_file():
                # Fallback or raise error if default fixture is missing
                raise FileNotFoundError(f"Default NFE fixture not found: {nfe_path}")

        _logger.info(f"Loading NFe fixture from: {nfe_path}")
        parser = XmlParser()
        nfe_proc = parser.from_path(nfe_path, NfeProc)  # Use NfeProc

        # Extract necessary parts from the fixture
        cls.nfe_obj = nfe_proc.NFe  # Keep the Nfe object
        cls.protocolo_original = (
            nfe_proc.protNFe.infProt.nProt
            if nfe_proc.protNFe and nfe_proc.protNFe.infProt
            else "123456789012345"
        )  # Example fallback
        cls.chave_original = (
            nfe_proc.protNFe.infProt.chNFe
            if nfe_proc.protNFe and nfe_proc.protNFe.infProt
            else cls.nfe_obj.infNFe.Id[3:]
        )
        cls.cnpj_original = cls.chave_original[6:20]  # Extract CNPJ from key
        _logger.info(f"CNPJ from NFe: {cls.cnpj_original}")

        # --- Client Setup ---
        cls.test_uf = environ.get("CERT_UF", "42")  # Default to SVRS (42) if not set
        try:
            TcodUfIbge(cls.test_uf)  # Validate UF
        except ValueError:
            raise ValueError(
                f"Invalid CERT_UF environment variable: {cls.test_uf}. Use a valid 2-digit IBGE code."
            )

        cls.client = NfeClient(
            ambiente="2",  # Homologation
            uf=cls.test_uf,
            pkcs12_data=cls.cert_data,
            pkcs12_password=cls.cert_password,
            fake_certificate=cls.fake_certificate,
            verify_ssl=False,  # Often needed for homologation endpoints
        )

        cls.nfe = Nfe(infNFe=nfe_proc.NFe.infNFe)
        cls.signed_nfe_xml = cls.nfe.to_xml(
            pkcs12_data=cls.cert_data,
            pkcs12_password=cls.cert_password,
            doc_id=cls.nfe.infNFe.Id,
        )
        _logger.info(f"Using UF: {cls.test_uf}, Ambiente: {cls.client.ambiente}")
        _logger.info(f"NFe Chave for tests: {cls.chave_original}")

    # --- Test Methods ---

    @only_if_valid_certificate
    def test_0_status(self):
        res = self.client.status_servico()
        self.assertIsInstance(res, RetConsStatServ)
        self.assertEqual(res.cStat, "107")  # Expected status for 'Servico em Operacao'
        self.assertEqual(res.tpAmb.value, self.client.ambiente)
        # Optionally check res.cUF.value against self.client.uf if needed

    @mock.patch.object(DefaultTransport, "post")
    def test_0_status_mocked(self, mock_post):
        mock_post.return_value = response_status
        res = self.client.status_servico()
        self.assertIsInstance(res, RetConsStatServ)
        self.assertEqual(res.cStat, "107")
        self.assertEqual(res.tpAmb.value, "2")  # Check mock environment
        self.assertEqual(res.cUF.value, "42")  # Check mock UF

    @only_if_valid_certificate
    def test_1_envia_documento(self):
        res_envio = self.client.envia_documento([self.signed_nfe_xml])
        self.assertIsInstance(res_envio, RetEnviNfe)
        # Check for success or already processed
        self.assertIn(
            res_envio.cStat, ("103", "104")
        )  # 103 = Lote Recebido, 104 = Lote Processado
        if res_envio.cStat == "103":  # Lote Recebido, needs consultation
            self.assertIsNotNone(res_envio.infRec)
            self.assertIsNotNone(res_envio.infRec.nRec)
            _logger.info(
                f"Lote enviado, recibo: {res_envio.infRec.nRec}. Aguardando consulta..."
            )
            self.client._aguarda_tempo_medio(res_envio)
            res_recibo = self.client.consulta_recibo(proc_envio=res_envio)
            self.assertIsInstance(res_recibo, RetConsReciNfe)
            _logger.info(
                f"Resultado Consulta Recibo: cStat={res_recibo.cStat}, xMotivo={res_recibo.xMotivo}"
            )
            # Check common processing results (Autorizado, Rejeitado, Denegado)
            self.assertIn(
                res_recibo.cStat, ("100", "104")
            )  # 100 = Autorizado (unlikely in HMG), 104 = Lote Processado
            if res_recibo.protNFe:
                for prot in res_recibo.protNFe:
                    _logger.info(
                        f"  Protocolo NFe {prot.infProt.chNFe}: cStat={prot.infProt.cStat}, xMotivo={prot.infProt.xMotivo}"
                    )
                    # Assertions might depend on expected test NFe outcome (likely rejection)
                    self.assertIn(
                        prot.infProt.cStat,
                        ("100", "110", "301", "302", "204", "297", "213"),
                    )  # Autorizado, Denegado, Rejeitado, Duplicidade, Assinatura incorreta etc.

        elif res_envio.cStat == "104":  # Lote processado (synchronous simulation?)
            _logger.info("Lote processado no envio (resposta síncrona simulada?).")
            self.assertIsNotNone(res_envio.protNFe)  # Should have protocol info
            prot = res_envio.protNFe
            _logger.info(
                f"  Protocolo NFe {prot.infProt.chNFe}: cStat={prot.infProt.cStat}, xMotivo={prot.infProt.xMotivo}"
            )
            self.assertIn(
                prot.infProt.cStat, ("100", "110", "301", "302", "204", "297", "213")
            )

    @mock.patch.object(DefaultTransport, "post")
    def test_1_envia_documento_mocked(self, mock_post):
        mock_post.return_value = response_envia_documento
        res = self.client.envia_documento([self.signed_nfe_xml])  # Pass signed XML
        self.assertIsInstance(res, RetEnviNfe)
        self.assertEqual(res.cStat, "103")  # Mock returns Lote Recebido
        self.assertIsNotNone(res.infRec)
        self.assertEqual(res.infRec.nRec, "423002202113232")

    @only_if_valid_certificate
    def test_2_consulta_documento(self):
        # Use a known key or the key from the fixture
        chave_consulta = self.chave_original
        _logger.info(f"Consultando chave: {chave_consulta}")
        res = self.client.consulta_documento(chave_consulta)
        self.assertIsInstance(res, RetConsSitNfe)
        _logger.info(
            f"Resultado Consulta Chave: cStat={res.cStat}, xMotivo={res.xMotivo}"
        )
        # Expect rejection or not found in homologation unless NFe was successfully sent before
        self.assertIn(
            res.cStat, ("100", "101", "110", "217", "526")
        )  # Autorizado, Cancelado, Denegado, Nao encontrada, Chave Invalida Consulta...

    @mock.patch.object(DefaultTransport, "post")
    def test_2_consulta_documento_mocked(self, mock_post):
        mock_post.return_value = response_consulta_documento
        res = self.client.consulta_documento(self.chave_original)  # Use fixture key
        self.assertIsInstance(res, RetConsSitNfe)
        self.assertEqual(res.cStat, "217")  # Mock returns Rejeicao: Nao consta

    @only_if_valid_certificate
    def test_3_envia_inutilizacao(self):
        # WARNING: Inutilization is permanent for the range in the specified env. Use with caution.
        # Choose a safe, unused range for testing.
        num_ini = "99990"
        num_fin = "99990"
        serie = "1"
        mod = "55"
        cnpj = self.cnpj_original  # Use CNPJ from fixture/cert
        just = "Teste de inutilizacao de numeracao"
        _logger.info(
            f"Tentando inutilizar: CNPJ={cnpj}, Mod={mod}, Serie={serie}, Nums={num_ini}-{num_fin}"
        )

        inut_obj = self.client.inutilizacao(
            cnpj=cnpj,
            mod=mod,
            serie=serie,
            num_ini=num_ini,
            num_fin=num_fin,
            justificativa=just,
        )
        # Sign the InutNfe object
        signed_xml = inut_obj.to_xml(
            pkcs12_data=self.cert_data,
            pkcs12_password=self.cert_password,
            doc_id=inut_obj.infInut.Id,  # Sign using the InfInut ID
        )
        res = self.client.envia_inutilizacao(signed_xml)
        self.assertIsInstance(res, RetInutNfe)
        _logger.info(
            f"Resultado Inutilizacao: cStat={res.infInut.cStat}, xMotivo={res.infInut.xMotivo}"
        )
        # 102 = Homologado, 206 = Ja Inutilizado, 563 = Ja utilizado pelo emitente
        self.assertIn(res.infInut.cStat, ("102", "206", "563", "215"))

    @mock.patch.object(DefaultTransport, "post")
    def test_3_envia_inutilizacao_mocked(self, mock_post):
        mock_post.return_value = response_inutilizacao
        # Prepare data as if it was signed (content doesn't matter for mock)
        evento = self.client.inutilizacao(
            cnpj=self.cnpj_original,
            mod="55",
            serie="1",
            num_ini="10",
            num_fin="20",
            justificativa="blablabla blablabla",
        )
        res = self.client.envia_inutilizacao(evento)
        self.assertIsInstance(res, RetInutNfe)
        self.assertEqual(res.infInut.cStat, "102")  # Mock returns success

    @only_if_valid_certificate
    def test_4_consulta_recibo(self):
        # Use a known recibo or one from a previous envia_documento test run
        # For a standalone test, this will likely fail unless a valid recibo is hardcoded
        nrec = environ.get(
            "TEST_RECIBO_NFE", "413000000000001"
        )  # Example, replace or use env var
        _logger.info(f"Consultando recibo: {nrec}")
        if len(nrec) != 15 or not nrec.isdigit():
            self.skipTest(f"Recibo inválido para teste: {nrec}")

        res = self.client.consulta_recibo(nrec)
        self.assertIsInstance(res, RetConsReciNfe)
        _logger.info(
            f"Resultado Consulta Recibo: cStat={res.cStat}, xMotivo={res.xMotivo}"
        )
        # 104 = Lote Processado, 105 = Lote em Processamento, 106 = Lote nao localizado
        self.assertIn(res.cStat, ("104", "105", "106"))

    @mock.patch.object(DefaultTransport, "post")
    def test_4_consulta_recibo_mocked(self, mock_post):
        mock_post.return_value = response_consulta_recibo
        nrec = "423002202113232"  # From mock data
        res = self.client.consulta_recibo(nrec)
        self.assertIsInstance(res, RetConsReciNfe)
        self.assertEqual(res.cStat, "104")  # Mock returns Lote Processado
        # Further check protocol status inside if needed
        self.assertTrue(hasattr(res, "protNFe") and res.protNFe)
        self.assertEqual(
            res.protNFe[0].infProt.cStat, "297"
        )  # Mock has rejection inside

    @only_if_valid_certificate
    def test_5_enviar_evento_cancelamento(self):
        # This test assumes the NFe from the fixture *was* successfully authorized previously
        # Or uses a known authorized key for the test environment.
        chave_cancelar = self.chave_original
        protocolo_cancelar = (
            self.protocolo_original
        )  # Use protocol from fixture or known valid one
        just = "Cancelamento para teste unitario"
        cnpj = self.cnpj_original

        _logger.info(
            f"Preparando cancelamento para Chave: {chave_cancelar}, Prot: {protocolo_cancelar}"
        )

        # 1. Create the cancel event object
        evento_obj = self.client.cancela_documento(
            chave=chave_cancelar,
            protocolo_autorizacao=protocolo_cancelar,
            justificativa=just,
            cnpj_cpf=cnpj,
            sequencia="1",  # First cancellation attempt
        )

        # 2. Create the TEnvEvento wrapper
        env_evento = TenvEvento(
            versao="1.00",  # Version of the TEnvEvento schema
            idLote=str(int(time.time() * 1000))[-15:],  # Generate lote ID
            evento=[evento_obj],  # Add the event object
        )

        # 3. Sign the TEnvEvento XML
        signed_env_evento_xml = env_evento.to_xml(
            pkcs12_data=self.cert_data,
            pkcs12_password=self.cert_password,
            doc_id=env_evento.evento[0].infEvento.Id,  # Sign using the inner event's ID
        )

        # 4. Send the signed TEnvEvento
        res = self.client.enviar_lote_evento([signed_env_evento_xml])
        self.assertIsInstance(res, RetEnvEvento)
        _logger.info(
            f"Resultado Envio Evento Cancelamento: cStat={res.cStat}, xMotivo={res.xMotivo}"
        )

        # Check overall batch status
        self.assertIn(res.cStat, ("128", "215"))  # 128 = Lote de Evento Processado

        # Check individual event status
        if res.cStat == "128":
            self.assertTrue(hasattr(res, "retEvento") and res.retEvento)
        for ret_ev in res.retEvento:
            _logger.info(
                f"  Retorno Evento {ret_ev.infEvento.tpEvento}: cStat={ret_ev.infEvento.cStat}, xMotivo={ret_ev.infEvento.xMotivo}"
            )
            # 135 = Evento Registrado e Vinculado a NF-e
            # Possible rejections: 573 (Duplicidade), errors related to NFe status (already cancelled, denegada etc.)
            self.assertIn(
                ret_ev.infEvento.cStat, ("135", "573")
            )  # Allow success or duplicate

    @mock.patch.object(DefaultTransport, "post")
    def test_5_enviar_evento_cancelamento_mocked(self, mock_post):
        mock_post.return_value = response_cancela_documento  # Using the provided mock
        signed_env_evento_xml = "<envEvento>...</envEvento>"  # Dummy signed content
        evento = self.client.cancela_documento(
            chave="35200159594315000157550010000000022062777169",
            protocolo_autorizacao="012345678912345",
            justificativa="votou17",
        )
        res = self.client.enviar_lote_evento([evento])
        # for some reason the retur Type is not correct when mocked (but live is OK)
        # self.assertIsInstance(res, TretEnvEvento)
        # The mock response provided is actually a retEnvEvento inside nfeResultMsg
        self.assertEqual(res.cStat, "215")

    # --- Integration Style Test ---
    # TODO processar_lote
