"""Certificate input normalization tests.

Odoo stores the PFX in a Binary field (base64 when read) but some callers
(and the Odoo 18 core certificate module consumers) hand over the decoded
PFX bytes: both must sign identically.
"""

import base64

from erpbrasil.assinatura import misc

from nfelib import CommonMixin

XML = """<?xml version="1.0" encoding="UTF-8"?>
<retConsStatServ versao="4.00" xmlns="http://www.portalfiscal.inf.br/nfe">
    <tpAmb>2</tpAmb>
    <cStat>107</cStat>
    <xMotivo>Servico em Operacao</xMotivo>
</retConsStatServ>
"""

PASSWORD = "testpassword"


def _fake_pkcs12():
    """Return (base64 content, raw decoded bytes) of a fake certificate."""
    b64_pfx = misc.create_fake_certificate_file(
        valid=True,
        passwd=PASSWORD,
        issuer="EMISSOR A TESTE",
        country="BR",
        subject="CERTIFICADO VALIDO TESTE",
    )
    if isinstance(b64_pfx, str):
        b64_pfx = b64_pfx.encode()
    return b64_pfx, base64.b64decode(b64_pfx)


def test_normalize_pkcs12_accepts_both_polarities():
    b64_pfx, raw_pfx = _fake_pkcs12()
    # raw DER PFX -> re-encoded to the base64 form Certificado expects
    assert CommonMixin.normalize_pkcs12(raw_pfx) == b64_pfx
    # base64 input (Odoo Binary field) is left untouched
    assert CommonMixin.normalize_pkcs12(b64_pfx) == b64_pfx
    # a path is left untouched as well
    assert CommonMixin.normalize_pkcs12("/tmp/cert.pfx") == "/tmp/cert.pfx"
    assert CommonMixin.normalize_pkcs12(None) is None


def test_sign_xml_accepts_raw_and_base64_pkcs12():
    b64_pfx, raw_pfx = _fake_pkcs12()
    signed_from_base64 = CommonMixin.sign_xml(XML, b64_pfx, PASSWORD)
    signed_from_raw = CommonMixin.sign_xml(XML, raw_pfx, PASSWORD)
    assert "<Signature" in signed_from_base64
    # RSA PKCS#1 v1.5 signing is deterministic
    assert signed_from_base64 == signed_from_raw
