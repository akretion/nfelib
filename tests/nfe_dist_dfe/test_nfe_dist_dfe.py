# Copyright (C) 2026 - TODAY Antônio Neto

import re
from dataclasses import fields
from pathlib import Path

from lxml import etree
from xmldiff import main
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from nfelib.nfe_dist_dfe.bindings.v1_0 import ResNfe, RetDistDfeInt

NFE_NS = "http://www.portalfiscal.inf.br/nfe"
SCHEMA_DIR = Path("nfelib") / "nfe_dist_dfe" / "schemas" / "v1_0"

# CNPJ alfanumérico (NT Conjunta 2025.001) e uma chave de acesso que o contém
CNPJ_ALFANUMERICO = "12ABC34501DE35"
CHAVE_ALFANUMERICA = "352609" + CNPJ_ALFANUMERICO + "550010000001231123456780"

RES_NFE_XML = f"""<resNFe xmlns="{NFE_NS}" versao="1.01">
  <chNFe>{CHAVE_ALFANUMERICA}</chNFe>
  <CNPJ>{CNPJ_ALFANUMERICO}</CNPJ>
  <xNome>EMITENTE TESTE</xNome>
  <IE>123456789012</IE>
  <dhEmi>2026-09-28T10:00:00-03:00</dhEmi>
  <tpNF>1</tpNF>
  <vNF>100.00</vNF>
  <digVal>vFL68WETQ+mvj1aJAMDx+oVi928=</digVal>
  <dhRecbto>2026-09-28T10:00:05-03:00</dhRecbto>
  <nProt>135260000000001</nProt>
  <cSitNFe>1</cSitNFe>
</resNFe>"""

RET_DIST_DFE_INT_XML = f"""<retDistDFeInt xmlns="{NFE_NS}" versao="1.01">
  <tpAmb>2</tpAmb>
  <verAplic>1.0</verAplic>
  <cStat>138</cStat>
  <xMotivo>Documento localizado</xMotivo>
  <dhResp>2026-09-28T10:00:00-03:00</dhResp>
  <ultNSU>000000000000001</ultNSU>
  <maxNSU>000000000000001</maxNSU>
  <loteDistDFeInt>
    <docZip schema="resNFe_v1.01.xsd">H4sIAAAAAAAAAA==</docZip>
  </loteDistDFeInt>
</retDistDFeInt>"""


def _validate(xml: str, xsd_name: str) -> None:
    schema = etree.XMLSchema(etree.parse(str(SCHEMA_DIR / xsd_name)))
    schema.assertValid(etree.fromstring(xml.encode()))


def _pattern(klass, field_name: str) -> str:
    field = next(f for f in fields(klass) if f.name == field_name)
    return field.metadata["pattern"]


def test_schemas_accept_cnpj_alfanumerico():
    _validate(RES_NFE_XML, "resNFe_v1.01.xsd")


def test_schemas_accept_doc_zip_without_nsu():
    _validate(RET_DIST_DFE_INT_XML, "retDistDFeInt_v1.01.xsd")


def test_bindings_patterns_cnpj_alfanumerico():
    cnpj_pattern = _pattern(ResNfe, "CNPJ")
    chave_pattern = _pattern(ResNfe, "chNFe")
    assert re.fullmatch(cnpj_pattern, CNPJ_ALFANUMERICO)
    assert re.fullmatch(chave_pattern, CHAVE_ALFANUMERICA)
    # CNPJ e chave numéricos continuam válidos
    assert re.fullmatch(cnpj_pattern, "12345678000195")
    assert re.fullmatch(chave_pattern, "3" * 44)


def test_bindings_doc_zip_nsu_optional():
    nsu = next(
        f for f in fields(RetDistDfeInt.LoteDistDfeInt.DocZip) if f.name == "NSU"
    )
    assert not nsu.metadata.get("required")

    ret = XmlParser().from_string(RET_DIST_DFE_INT_XML, RetDistDfeInt)
    doc_zip = ret.loteDistDFeInt.docZip[0]
    assert doc_zip.NSU is None
    assert doc_zip.schema == "resNFe_v1.01.xsd"


def test_in_out_res_nfe(tmp_path):
    res_nfe = XmlParser().from_string(RES_NFE_XML, ResNfe)
    assert res_nfe.CNPJ == CNPJ_ALFANUMERICO

    input_file = tmp_path / "input.xml"
    output_file = tmp_path / "output.xml"
    input_file.write_text(RES_NFE_XML)
    output_file.write_text(XmlSerializer().render(obj=res_nfe, ns_map={None: NFE_NS}))
    assert len(main.diff_files(str(input_file), str(output_file))) == 0
