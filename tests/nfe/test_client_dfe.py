import sys
from unittest import TestCase, mock, skipIf

from erpbrasil.assinatura import misc
from xsdata.formats.dataclass.transports import DefaultTransport

# --- Conditional Imports for Python 3.9+ ---
# The DfeClient module uses syntax not supported in Python 3.8 (e.g., dict[str, Any]).
# We must prevent the import from happening to avoid a SyntaxError/RuntimeError.
if sys.version_info >= (3, 9):
    from nfelib.nfe.client.v4_0.dfe import DfeClient
    from nfelib.nfe_dist_dfe.bindings.v1_0 import RetDistDfeInt
else:
    # Define dummies so the class definition below doesn't throw a NameError
    DfeClient = None
    RetDistDfeInt = None


# --- Mock SOAP Response ---
# A realistic SOAP response for a successful query with multiple documents.
response_sucesso_multiplos = b"""<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <nfeDistDFeInteresseResponse xmlns="http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe">
            <nfeDistDFeInteresseResult>
                <retDistDFeInt xmlns="http://www.portalfiscal.inf.br/nfe" versao="1.01">
                    <tpAmb>1</tpAmb>
                    <verAplic>1.4.0</verAplic>
                    <cStat>138</cStat>
                    <xMotivo>Documento(s) localizado(s)</xMotivo>
                    <dhResp>2022-04-04T11:54:49-03:00</dhResp>
                    <ultNSU>000000000000201</ultNSU>
                    <maxNSU>000000000000201</maxNSU>
                    <loteDistDFeInt>
                        <docZip NSU="000000000000200" schema="resNFe_v1.00.xsd">H4sIAAAAAAAEAIVS22qDQBD9FfFdd9Z7ZLKQphosqQ3mQuibMZto8RJcifn8rjG9PZUdZg7DOWeGYbHlIg65cqvKWvg3cZyqedddfEL6vtd7U2/aMzEAKNm/LtdZzqtU/SYX/5O1ohZdWmdcVa68FWkzVakO8PD4o780bZeWp0JkaakX9Uk/tKQ+cZVhlssVmUkNoPLZnjcAGKBtDwVMzzIodak3AIO6HpJRg/N49cL+apDcm3iLm4qz99lKWSSzMJrPlEAJnqPNWyJRlATLCMnIwShgUkqpNLEAHBOJ7OAxD6qCGWCARkEDZwPg30MDU2YkIwG7SxwyiuRe8SqTN3H1iXQZMB6L8y4t2W73sXdtJ+6TUDhGveaLbc9DsXyyt1NpNZLkzIRnh675PZZOfMP2LfNn7IOD9aptOkaHy5meDS44FnWRjG3M1kU3HEmu9gWRjP+BfQI6BY33GAIAAA==</docZip>
                        <docZip NSU="000000000000201" schema="procNFe_v4.00.xsd">H4sIAAAAAAAAA51WzXKjRhC+5ykoX1MWMyAssTWeiozQhpSFKEu7dwxjmwQYLUJYldfJOS+QY/bF0t0DWF5nt7JRqejub3q6p3/mR9QPKml0ZnWqOaT6+mI6YezCOlVlfbi+eGrb/Tvbfn5+nux106blQ3HI0nJS1A+T+8aGuRdSxCv1Xfog4JTXDqP8+gJQ13MY457v+VOXewz5mQeUs/7HHXblzGYzfsXRVK6kyD6spOsJG6nI4pUcNAACSdRpu9nLj6rOU2EbQVQ6lx7MQSoOqimU5MI2jKhhFkhIRP4UVoV0mMMuGYf/jjvvGIP/j4zDV9hGAfS2aRHW7bdVex3R7o0LohDFUh1alHtOZOtjvXoPUTHOPQfiMDLMi6q9mYgMyOD8YADiRLb8iCISGF1U99LBQWTEQwEhUaA9B6XIV0WdluR74BFNGnWQjEBixR56BAMFbGAFVBBbR25yra2bJj0UpbUJFlbHp8IeBjEo8KSqAuIK4uQX+bq6wiZQnGJdKbkLt7vQurS2RbUv1cGK06zQsChhm3FxWqWQwG+o0biAYqsmJJ+n28dG3h1TK0mPpbaWRXoANQRF3WjpzaFPkKGkv045TMbvojxWn/+sCw3zCIVG2ybCxn4LwkTyOXcwGggFJJElKdaEeXOwQrw4ETEpAiMGfNC1kg53obl9/wqakQBhn609CiW0v+vOwT53XWEDIIK7HdYLCSiTXk5dQ4mc86nv+jMfszv3X2c3Xl2GVriOdtFyAdRarG+iMIZMLkPr5816c7t5vwgWG0wsjH5c3G7urFW0DRa3Y/5pcaZJx8Ru0+qoSmutm4M6Ty3HXUmpPQX7EnbG339ZKezCBhwEuv71WLfa4h7EQuPidJMWDajfNFr/VhY14D0y1MZjLpu/qs328x/aVPYrxWFTb3bFrv5XcTyPc3c6mzvQrK/LYzIAuyMKx707Cli26RWbOj6cQq47NWVTVVqUMisLVbeK/zQwk0xXcDZiJXEcTgkykavWqqNWVdcXeNDBnstx8UjCy2Cz5rjJE4OGi1hiwd7vohhQFCEoHAvS+6IGS89F+2QtNRQIA6RZcbCW/pS5LjUuSiJYbRLpcQbdT6w4BrqSH+JoKWxixSf88gmjOSSI7kNN4HTCxh/sfoOKjpzRIIAv6901xf0XayZIHIn0Pg30icjo1YDgwMBv/JpxqMZOD3VBjs4t8A4nhj600FJRsN6a7zbmjEuhm+IRzzeiIthutjE0Cu40YsU+aFQOjDOZka9BFh0yxpBkExc66xyB6r/4sHuvSYR5qD9J3/cxfOAQjHfoeCc9F73i/u5Bm2Yk0ZY+m2PbGMWp3yt2NwH4phQAJ/aoyvqUkQCl6CEsBAL2aMkmOdisonik/8FHP2F0MxjozgYwFz1snxu2R3QsCHQ+Xo26xTsI80Rl+8JpRwnsAZNMIrDxdH2OG0B0qyAZYGTRHsQyWqS4XgASQe8FMUIP3sEKz3GU/7XHu1WjWjXqkgB+1OPoCFjRwSKzASEegonGKCIUkxc56YGl6nR5hhr5bYG/UocOK6AH1AiiwwdJHwK+SeyxAHZfkbZJ64N5Opl4fHo+9bHZw/A+faTTK0GKz4f0cXhIIEI4biqj0OF3TB0i9jDX3hsLD4u8yHpmBc9JLZc6O1YKLw+8/YpcW/DYfGet0yazlqrS6G1U7oUiMxw9e2z6wnnQvnmIkiOoYUsv0iiHO8xx+NxxvKnD5t7F21dV9oTWvufhChue5ogaHckvXMCVSbDItm0Ko5gaw8KNp9ui03JxbOGQ+j2FyLV1PGgrTy242/Hy7TUoVmPG7uMErn/ryx/+AZs2W+n2CwAA</docZip>
                    </loteDistDFeInt>
                </retDistDFeInt>
            </nfeDistDFeInteresseResult>
        </nfeDistDFeInteresseResponse>
    </soap:Body>
</soap:Envelope>"""


@skipIf(sys.version_info < (3, 9), "DfeClient requires Python 3.9+")
class DfeClientTest(TestCase):
    """Tests DfeClient SOAP interactions."""

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
        cls.fake_certificate = True

        # Client Setup
        cls.client = DfeClient(
            ambiente="1",  # DF-e distribution is only available in production
            uf="35",  # The UF of the interested party (CNPJ/CPF)
            pkcs12_data=cls.cert_data,
            pkcs12_password=cls.cert_password,
            fake_certificate=cls.fake_certificate,
            verify_ssl=False,
        )

    @mock.patch.object(DefaultTransport, "post")
    def test_consultar_distribuicao_mocked(self, mock_post):
        """
        Tests the DF-e distribution query with a mocked successful response.
        """
        mock_post.return_value = response_sucesso_multiplos

        # Define test parameters
        cnpj_cpf = "00000000000191"
        ultimo_nsu = "000000000000000"

        # Call the client method
        res = self.client.consultar_distribuicao(
            cnpj_cpf=cnpj_cpf, ultimo_nsu=ultimo_nsu
        )

        # Assertions
        self.assertIsInstance(res, RetDistDfeInt)
        self.assertEqual(res.cStat, "138")
        self.assertEqual(res.xMotivo, "Documento(s) localizado(s)")
        self.assertEqual(res.ultNSU, "000000000000201")
        self.assertIsNotNone(res.loteDistDFeInt)
        self.assertEqual(len(res.loteDistDFeInt.docZip), 2)
        self.assertEqual(res.loteDistDFeInt.docZip[0].NSU, "000000000000200")
        self.assertEqual(res.loteDistDFeInt.docZip[1].NSU, "000000000000201")

        # Verify that the mock was called
        mock_post.assert_called_once()
