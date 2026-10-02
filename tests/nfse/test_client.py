# Copyright (C) 2026  Raphaël Valyi - Akretion
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import base64
import gzip
from unittest import TestCase, mock

from erpbrasil.assinatura import misc

from nfelib.nfse.bindings.v1_0.dps_v1_00 import Dps
from nfelib.nfse.bindings.v1_0.tipos_complexos_v1_00 import TcinfDps
from nfelib.nfse.client.v1_0.nfse import NfseClient


class NfseClientTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pkcs12_data = misc.create_fake_certificate_file(
            valid=True,
            passwd="123456",
            issuer="TEST",
            country="BR",
            subject="TEST",
        )
        cls.dps = Dps(
            infDPS=TcinfDps(
                Id="DPS35034061234567890001900000000000000000000000001",
            )
        )

    def _client(self):
        """Build a client whose HTTP layer is mocked for the whole test."""
        patcher = mock.patch("requests.Session.request")
        mock_request = patcher.start()
        self.addCleanup(patcher.stop)
        client = NfseClient(
            ambiente="2",
            pkcs12_data=self.pkcs12_data,
            pkcs12_password="123456",
        )
        return client, mock_request

    def test_producao_restrita_url(self):
        client, _ = self._client()
        self.assertEqual(
            client.base_url,
            "https://adn.producaorestrita.nfse.gov.br/contribuinte",
        )

    def test_envia_dps(self):
        client, mock_request = self._client()
        response = mock.Mock(status_code=200)
        response.json.return_value = {
            "chaveAcesso": "35200000000000000000000000000000000000000000000001"
        }
        mock_request.return_value = response

        ret = client.envia_dps(self.dps)

        self.assertEqual(ret.status_code, 200)
        self.assertEqual(
            ret.body["chaveAcesso"],
            "35200000000000000000000000000000000000000000000001",
        )
        args, kwargs = mock_request.call_args
        self.assertEqual(args[0], "POST")
        self.assertEqual(
            args[1],
            "https://adn.producaorestrita.nfse.gov.br/contribuinte/nfse",
        )
        # the payload is a signed DPS, gzip+base64 encoded
        payload = kwargs["json"]["dpsXmlGZipB64"]
        xml = gzip.decompress(base64.b64decode(payload)).decode("utf-8")
        self.assertIn("Signature", xml)
        self.assertIn(self.dps.infDPS.Id, xml)

    def test_consulta_nfse(self):
        client, mock_request = self._client()
        response = mock.Mock(status_code=200)
        response.json.return_value = {"nfseXmlGZipB64": "eA=="}
        mock_request.return_value = response

        chave = "35200000000000000000000000000000000000000000000001"
        ret = client.consulta_nfse(chave)

        self.assertEqual(ret.status_code, 200)
        args, _kwargs = mock_request.call_args
        self.assertEqual(args[0], "GET")
        self.assertTrue(args[1].endswith(f"/nfse/{chave}"))

    def test_consulta_dps(self):
        client, mock_request = self._client()
        response = mock.Mock(status_code=200)
        response.json.return_value = {"chaveAcesso": "35"}
        mock_request.return_value = response

        client.consulta_dps("DPS3501")

        args, _kwargs = mock_request.call_args
        self.assertEqual(args[0], "GET")
        self.assertTrue(args[1].endswith("/dps/DPS3501"))

    def test_registra_evento(self):
        client, mock_request = self._client()
        response = mock.Mock(status_code=201)
        response.json.return_value = {}
        mock_request.return_value = response

        evento = mock.Mock()
        evento.to_xml.return_value = "<pedRegEvento/>"
        evento.infPedReg.Id = "PRE3501"
        chave = "35200000000000000000000000000000000000000000000001"

        with mock.patch.object(NfseClient, "_sign", return_value="<signedEvento/>"):
            client.registra_evento(chave, evento)

        args, kwargs = mock_request.call_args
        self.assertEqual(args[0], "POST")
        self.assertTrue(args[1].endswith(f"/nfse/{chave}/eventos"))
        payload = kwargs["json"]["pedidoRegistroEventoXmlGZipB64"]
        self.assertEqual(gzip.decompress(base64.b64decode(payload)), b"<signedEvento/>")
