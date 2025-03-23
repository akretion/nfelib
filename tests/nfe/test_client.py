import logging
import io
import os
import time
from os import environ
from pathlib import Path
from unittest import TestCase, mock

from decorator import decorate
from erpbrasil.assinatura import certificado as cert
from erpbrasil.assinatura import misc
from nfelib.nfe.bindings.v4_0.nfe_v4_00 import Nfe
from nfelib.nfe.bindings.v4_0.proc_nfe_v4_00 import TnfeProc
from requests import Session
from requests_pkcs12 import Pkcs12Adapter
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.transports import DefaultTransport

from nfelib.nfe.client.v4_0 import NfeClient

response_status = b"""
<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><nfeResultMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4"><retConsStatServ versao="4.00" xmlns="http://www.portalfiscal.inf.br/nfe"><tpAmb>2</tpAmb><verAplic>SVRS202305251555</verAplic><cStat>107</cStat><xMotivo>Servico em Operacao</xMotivo><cUF>42</cUF><dhRecbto>2023-06-11T00:15:00-03:00</dhRecbto><tMed>1</tMed></retConsStatServ></nfeResultMsg></soap:Body></soap:Envelope>"""

response_envia_documento = b"""
<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><nfeResultMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4"><retEnviNFe versao="4.00" xmlns="http://www.portalfiscal.inf.br/nfe"><tpAmb>2</tpAmb><verAplic>SVRS202305251555</verAplic><cStat>103</cStat><xMotivo>Lote recebido com sucesso</xMotivo><cUF>42</cUF><dhRecbto>2023-06-11T01:18:19-03:00</dhRecbto><infRec><nRec>423002202113232</nRec><tMed>1</tMed></infRec></retEnviNFe></nfeResultMsg></soap:Body></soap:Envelope>"""

response_consulta_documento = b"""
<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><nfeResultMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeConsultaProtocolo4"><retConsSitNFe versao="4.00" xmlns="http://www.portalfiscal.inf.br/nfe"><tpAmb>2</tpAmb><verAplic>SVRS202305251555</verAplic><cStat>217</cStat><xMotivo>Rejeicao: NF-e nao consta na base de dados da SEFAZ</xMotivo><cUF>42</cUF><dhRecbto>2023-06-11T01:20:55-03:00</dhRecbto><chNFe>42230675277525000259550010000364481754015406</chNFe></retConsSitNFe></nfeResultMsg></soap:Body></soap:Envelope>"""

response_consulta_recibo = b"""
<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><nfeResultMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeRetAutorizacao4"><retConsReciNFe versao="4.00" xmlns="http://www.portalfiscal.inf.br/nfe"><tpAmb>2</tpAmb><verAplic>SVRS202305261028</verAplic><nRec>423002202113232</nRec><cStat>104</cStat><xMotivo>Lote processado</xMotivo><cUF>42</cUF><dhRecbto>2023-06-11T01:18:19-03:00</dhRecbto><protNFe versao="4.00"><infProt><tpAmb>2</tpAmb><verAplic>SVRS202305261028</verAplic><chNFe>42230675277525000259550010000364481754015406</chNFe><dhRecbto>2023-06-11T01:18:19-03:00</dhRecbto><digVal>IoYUWXt2fIiRXb7UYRgl77c6Zlk=</digVal><cStat>297</cStat><xMotivo>Rejeicao: Assinatura difere do calculado</xMotivo></infProt></protNFe></retConsReciNFe></nfeResultMsg></soap:Body></soap:Envelope>"""

response_cancela_documento = b"""<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><nfeResultMsg xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeRecepcaoEvento4"><retEnvEvento versao="1.00" xmlns="http://www.portalfiscal.inf.br/nfe"><idLote /><tpAmb>2</tpAmb><verAplic>SVRS202305251555</verAplic><cStat>215</cStat><xMotivo>Rejeicao: Falha no schema XML</xMotivo></retEnvEvento></nfeResultMsg></soap:Body></soap:Envelope>"""  # TODO not a valid cancelamento


_logger = logging.getLogger(__name__)


def _only_if_valid_certificate(method, self):
    if self.valid_certificate:
        return method(self)
    return lambda: _logger.info(
        "Skipping test because you didn't provide a valid A1 certificate"
    )


def only_if_valid_certificate(method):
    return decorate(method, _only_if_valid_certificate)


SERVER = "https://nfe-homologacao.svrs.rs.gov.br"  # TODO should be a parameter


class SoapTest(TestCase):
    """
    Tests are mocked because the fisc server requires a valid A1 certificate.
    But for each test, you can also activate the non mocked version
    if you export the CERT_FILE and CERT_PASSWORD ENV variables before running the test:
    export CERT_PASSWORD=...
    export CERT_FILE=...
    export NFE_FILE=...

    To fix/adjust the _mocked tests, a way is to use a real A1 certificate and make the
    associated non mocked test fail (like by using assertEqual with a bad value)
    while priting the response in the NfeClient send method. Then use it as the mocked
    response.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # TODO customize NFe path via ENV var?
        parser = XmlParser()
        if environ.get("NFE_FILE"):
            nfe_path = environ["NFE_FILE"]
        else:
            nfe_path = "tests/nfe/fixtures/procNFe.xml"

        nfe_proc = parser.from_path(
            Path(nfe_path),
            TnfeProc,
        )

        if environ.get("CERT_FILE") and environ.get("CERT_PASSWORD"):
            cls.valid_certificate = True
            with open(environ["CERT_FILE"], "rb") as pkcs12_file:
                cls.cert_data = pkcs12_file.read()
            cls.cert_password = environ["CERT_PASSWORD"]
            cls.fake_certificate = False
        else:
            cls.valid_certificate = False
            valid = (True,)
            cls.cert_password = "123456"
            issuer = "EMISSOR A TESTE"
            country = "BR"
            subject = "CERTIFICADO VALIDO TESTE"
            #            cert_type = "nfe-e"
            cls.cert_data = misc.create_fake_certificate_file(
                valid, cls.cert_password, issuer, country, subject
            )
            cls.fake_certificate = True

        cls.nfe = Nfe(infNFe=nfe_proc.NFe.infNFe)  # , signature=nfe_proc.NFe.signature)
        serializer = XmlSerializer()
        cls.nfe_xml = serializer.render(
            obj=cls.nfe, ns_map={None: "http://www.portalfiscal.inf.br/nfe"}
        )  # .replace('\n', '').replace('\r', '')
        cls.client = NfeClient(
            ambiente="2",
            uf="41",  # cls.nfe.infNFe.ide.cUF.value,
            pkcs12_data=cls.cert_data,
            pkcs12_password=cls.cert_password,
            fake_certificate=cls.fake_certificate,
        )
        cls.signed_nfe_xml = cls.nfe.to_xml(pkcs12_data=cls.cert_data, pkcs12_password=cls.cert_password, doc_id=cls.nfe.infNFe.Id)

    @only_if_valid_certificate
    def test_0_status(self):
        res = self.client.status_servico()
        self.assertEqual(res.cStat, "107")

    @mock.patch.object(DefaultTransport, "post")
    def test_0_status_mocked(self, mock_post):
        mock_post.return_value = response_status
        res = self.client.status_servico()
        self.assertEqual(res.cStat, "107")

    @only_if_valid_certificate
    def test_1_envia_documento(self):
        res = self.client.envia_documento([self.signed_nfe_xml])
        self.assertEqual(res.cStat, "103")
        print(res)
        import time

        time.sleep(int(res.infRec.tMed))
        res = self.client.consulta_recibo(numero=res.infRec.nRec)
        print(res)
        # res = self.client.consulta_documento(self.nfe.infNFe.Id[3:])
        # # we actually test the NFe is not found because it is the test environment
        # print(res)
        # breakpoint()
        # self.assertIn(res.cStat, ("217", "526"))

    @mock.patch.object(DefaultTransport, "post")
    def test_1_envia_documento_mocked(self, mock_post):
        mock_post.return_value = response_envia_documento
        res = self.client.envia_documento([self.signed_nfe_xml])
        self.assertEqual(res.cStat, "103")

    @only_if_valid_certificate
    def test_2_consulta_documento(self):
        res = self.client.consulta_documento(self.nfe.infNFe.Id[3:])
        # we actually test the NFe is not found because it is the test environment
        self.assertIn(res.cStat, ("217", "526"))

    @mock.patch.object(DefaultTransport, "post")
    def test_2_consulta_documento_mocked(self, mock_post):
        mock_post.return_value = response_consulta_documento
        res = self.client.consulta_documento(self.nfe.infNFe.Id[3:])
        # we actually test the NFe is not found because it is the test environment
        self.assertEqual(res.cStat, "217")

    def test_3_envia_inutilizacao(self):
        pass

    @only_if_valid_certificate
    def test_4_consulta_recibo(self):
        nrec = "423002202113232"
        res = self.client.consulta_recibo(nrec)
        # we actually test the NFe is not found because it is the test environment
        self.assertEqual(res.cStat, "106")  # TODO should be 104 normally

    @mock.patch.object(DefaultTransport, "post")
    def test_4_consulta_recibo_mocked(self, mock_post):
        mock_post.return_value = response_consulta_recibo
        nrec = "423002202113232"
        res = self.client.consulta_recibo(nrec)
        # we actually test the NFe is not found because it is the test environment
        self.assertEqual(res.cStat, "104")

    def test_5_enviar_lote_evento(self):  # (cancela documento)
        pass

    @only_if_valid_certificate
    def test_envia_e_consulta_e_cancela(self):
        "isso mais ou menos test o processa_documento do erpbrasil.edoc"
        proc_envio = self.client.envia_documento(self.signed_nfe_xml)
        self.client._aguarda_tempo_medio(proc_envio)
        res = self.client.consulta_recibo(proc_envio=proc_envio)
        # TODO por algum motivo eu pego um erro como:
        # <infProt><tpAmb>2</tpAmb><verAplic>SVRS202305261028</verAplic><chNFe>42230675277525000259550010000364481754015406</chNFe><dhRecbto>2023-06-12T22:57:51-03:00</dhRecbto><digVal>IoYUWXt2fIiRXb7UYRgl77c6Zlk=</digVal><cStat>297</cStat><xMotivo>Rejeicao: Assinatura difere do calculado</xMotivo></infProt>
        self.assertEqual(res.cStat, "104")

        cancel_event = self.client.cancela_documento(
            self.nfe.infNFe.Id[3:], "423002202113232", "Era apenas um teste."
        )
        self.client.enviar_lote_evento([cancel_event])

    #        self.assertEqual(1, 2)

    @only_if_valid_certificate
    def test_inutilizacao(self):
        inut_event = self.client.inutilizacao(
            "81583054000129", "55", "1", "2", "2", "Era apenas um teste"
        )
        self.client.envia_inutilizacao(inut_event)

