import os
from pathlib import Path
from unittest import TestCase

from lxml import etree
from xmldiff import main
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from nfelib.nfse.bindings.v1_01.nfse_v1_01 import Nfse

SAMPLES = os.path.join("nfelib", "nfse", "samples", "v1_01")
SCHEMAS = os.path.join("nfelib", "nfse", "schemas", "v1_01")
NAMESPACE = "http://www.sped.fazenda.gov.br/nfse"


class NFse101Tests(TestCase):
    def test_in_out_nfse(self):
        input_file = os.path.join(SAMPLES, "nfse-ibscbs.xml")
        obj = XmlParser().from_path(Path(input_file), Nfse)
        serializer = XmlSerializer(config=SerializerConfig(indent="  "))
        xml = serializer.render(obj=obj, ns_map={None: NAMESPACE})

        output_file = "tests/output_nfse_v1_01.xml"
        with open(output_file, "w") as f:
            f.write(xml)

        diff = main.diff_files(input_file, output_file)
        assert len(diff) == 0

    def test_ibscbs_groups(self):
        nfse = Nfse.from_path(os.path.join(SAMPLES, "nfse-ibscbs.xml"))
        totals = nfse.infNFSe.IBSCBS.totCIBS
        self.assertEqual(nfse.infNFSe.IBSCBS.valores.vBC, "1000.00")
        self.assertEqual(totals.gIBS.vIBSTot, "1.00")
        self.assertEqual(totals.gCBS.vCBS, "9.00")
        classification = nfse.infNFSe.DPS.infDPS.IBSCBS.valores.trib.gIBSCBS
        self.assertEqual(classification.CST, "000")
        self.assertEqual(classification.cClassTrib, "000001")

    def test_sample_schema(self):
        schema = etree.XMLSchema(etree.parse(os.path.join(SCHEMAS, "NFSe_v1.01.xsd")))
        doc = etree.parse(os.path.join(SAMPLES, "nfse-ibscbs.xml"))
        self.assertTrue(schema.validate(doc), schema.error_log)
