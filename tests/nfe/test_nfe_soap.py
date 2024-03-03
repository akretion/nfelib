import io
import logging
from os import environ
from pathlib import Path
from re import I
from unittest import TestCase, mock

from decorator import decorate
from erpbrasil.assinatura import certificado as cert, misc
from erpbrasil.assinatura.certificado import ArquivoCertificado
from requests import Session
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.transports import DefaultTransport

import nfelib
from nfelib.nfe.bindings.v4_0.nfe_v4_00 import Nfe
from nfelib.nfe.bindings.v4_0.proc_nfe_v4_00 import TnfeProc
from nfelib.nfe.ws.soap_client import NfeSoapClient as SoapClient

# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


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
    if self.valid_cerificate:
        return method(self)
    else:
        return lambda: _logger.info(
            "Skipping test today because you didn't provide a valid A1 certificate"
        )


def only_if_valid_certificate(method):
    return decorate(method, _only_if_valid_certificate)


SERVER = "https://nfe-homologacao.svrs.rs.gov.br"  # TODO should be a parameter


class SoapTest(TestCase):
    """
    IMPORTANT: requires a very recent version of xsdata to run, Currently the code you
    need is not published yet (will be published in version after 23.5).
    So you need to install xsdata this way:
    sudo python -m pip install git+https://github.com/tefra/xsdata.git@master#egg=xsdata

    Tests are mocked because the fisc server requires a valid A1 certificate.
    But for each test, you can also activate the non mocked version
    if you export the CERT_FILE and CERT_PASSWORD ENV variables before running the test:
    export CERT_PASSWORD=...
    export CERT_FILE=...
    export NFE_FILE=...

    To fix/adjust the _mocked tests, a way is to use a real A1 certificate and make the
    associated non mocked test fail (like by using assertEqual with a bad value)
    while priting the response in the SoapClient send method. Then use it as the mocked
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
            nfe_path = "nfelib/nfe/samples/v4_0/leiauteNFe/41170706117473000150550010000463202612756525-procNFe.xml"

        nfe_proc = parser.from_path(
            Path(nfe_path),
            TnfeProc,
        )

        cls.valid_cerificate = False
        if environ.get("CERT_FILE") and environ.get("CERT_PASSWORD"):
            certificado = cert.Certificado(
                arquivo=environ["CERT_FILE"],
                senha=environ["CERT_PASSWORD"],
            )
            cls.valid_cerificate = certificado
        else:
            valid = (True,)
            passwd = "123456"
            issuer = "EMISSOR A TESTE"
            country = "BR"
            subject = "CERTIFICADO VALIDO TESTE"
            cert_type = "nfe-e"
            cert_file = misc.create_fake_certificate_file(
                valid, passwd, issuer, country, subject
            )
            certificado = cert.Certificado(
                arquivo=cert_file,
                senha=passwd,
            )
            cls.fake_certificate = certificado

        cls.nfe = Nfe(infNFe=nfe_proc.NFe.infNFe)  # , signature=nfe_proc.NFe.signature)
        serializer = XmlSerializer()
        cls.nfe_xml = serializer.render(
            obj=cls.nfe, ns_map={None: "http://www.portalfiscal.inf.br/nfe"}
        )  # .replace('\n', '').replace('\r', '')
        cls.client = SoapClient.from_service(
            tpAmb=2, cUF=cls.nfe.infNFe.ide.cUF.value, certificate=certificado
        )
        #        cls.signed_nfe_xml = cls.nfe_xml
        cls.signed_nfe_xml = cls.client.sign_xml(cls.nfe_xml, cls.nfe.infNFe.Id)

    @only_if_valid_certificate
    def test_0_download_wsdl_files(self):
        test_mode = True
        WSDLS = (
            "/ws/nfeinutilizacao/nfeinutilizacao4.asmx",
            "/ws/NfeConsulta/NfeConsulta4.asmx",
            "/ws/NfeStatusServico/NfeStatusServico4.asmx",
            "/ws/cadconsultacadastro/cadconsultacadastro4.asmx",
            "/ws/recepcaoevento/recepcaoevento4.asmx",
            "/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
            "/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
            "https://www1.nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx",
            #"https://mdfe.svrs.rs.gov.br/ws/MDFeRecepcao/MDFeRecepcao.asmx",
        )

        with ArquivoCertificado(self.client.certificate, "r") as (key, cert):
            session = Session()
            session.cert = (key, cert)
            session.verify = False
            for url in WSDLS:
                if not url.startswith("http"):
                    url = SERVER + url
                if not url.endswith("?wsdl"):
                    url += "?wsdl"
                response = session.get(url)
                filename = (
                    url.split("/")[-1]
                    .replace("?wsdl", "")
                    .replace(".asmx", ".wsdl")
                    .lower()
                )
                output = "/tmp/%s" % (filename,)
                if "mdfe" in url:  # TODO move to mdfe test suite
                    wsdl_file = nfelib.__path__[0] + "/mdfe/wsdl/" + filename
                else:
                    wsdl_file = nfelib.__path__[0] + "/nfe/wsdl/" + filename
                if test_mode:
                    with open(output, "w") as file:
                        file.write(response.text)
                    print(
                        "downloaded %s in %s",
                        (
                            url,
                            filename,
                        ),
                    )
                    self.assertListEqual(
                        list(io.open(output)),
                        list(io.open(wsdl_file)),
                        filename + " differs",
                    )
                else:
                    with open(wsdl_file, "w") as file:
                        file.write(response.text)

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
        res = self.client.envia_documento(self.signed_nfe_xml)
        self.assertEqual(res.cStat, "103")

    @mock.patch.object(DefaultTransport, "post")
    def test_1_envia_documento_mocked(self, mock_post):
        mock_post.return_value = response_envia_documento
        res = self.client.envia_documento(self.signed_nfe_xml)
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
