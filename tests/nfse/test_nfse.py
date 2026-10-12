# Copyright (C) 2023 - TODAY Raphaël Valyi - Akretion

import os
from pathlib import Path
from unittest import TestCase

from lxml import etree
from xmldiff import main
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from nfelib.nfse.bindings.v1_0 import (
    dps_v1_01,
    nfse_v1_01,
    ped_reg_evento_v1_01,  # noqa: F401
)

SAMPLES = os.path.join("nfelib", "nfse", "samples", "v1_0")
SCHEMAS = os.path.join("nfelib", "nfse", "schemas", "v1_0")
NAMESPACE = "http://www.sped.fazenda.gov.br/nfse"


class NFseTests(TestCase):
    def test_in_out_consulta(self):
        for filename in ["ConsultarNFSeEnvio-ped-sitnfse.xml"]:
            input_file = os.path.join(SAMPLES, filename)
            parser = XmlParser()
            obj = parser.from_path(Path(input_file))
            serializer = XmlSerializer(config=SerializerConfig(indent="  "))
            xml = serializer.render(obj=obj, ns_map={None: NAMESPACE})

            output_file = "tests/output_nfse.xml"
            with open(output_file, "w") as f:
                f.write(xml)

            diff = main.diff_files(input_file, output_file)
            assert len(diff) == 0
            if len(diff) != 0:
                break

    def test_in_out_dps(self):
        for filename in ["dps-simples.xml", "dps-regime-normal.xml"]:
            input_file = os.path.join(SAMPLES, filename)
            parser = XmlParser()
            obj = parser.from_path(Path(input_file))
            serializer = XmlSerializer(config=SerializerConfig(indent="  "))
            xml = serializer.render(obj=obj, ns_map={None: NAMESPACE})

            output_file = "tests/output_nfse_dps.xml"
            with open(output_file, "w") as f:
                f.write(xml)

            diff = main.diff_files(input_file, output_file)
            assert len(diff) == 0
            if len(diff) != 0:
                break

    def test_in_out_pedRegEvento(self):
        for filename in ["CancelarNFSe-ped-cannfse.xml"]:
            input_file = os.path.join(SAMPLES, filename)
            parser = XmlParser()
            obj = parser.from_path(Path(input_file))
            serializer = XmlSerializer(config=SerializerConfig(indent="  "))
            xml = serializer.render(obj=obj, ns_map={None: NAMESPACE})

            output_file = "tests/output_nfse_pedRegEvento.xml"
            with open(output_file, "w") as f:
                f.write(xml)

            diff = main.diff_files(input_file, output_file)
            assert len(diff) == 0
            if len(diff) != 0:
                break

    def test_in_out_nfse_ibscbs(self):
        """The 1.01 sample (tax reform groups) round-trips unchanged."""
        input_file = os.path.join(SAMPLES, "nfse-ibscbs.xml")
        obj = XmlParser().from_path(Path(input_file), nfse_v1_01.Nfse)
        serializer = XmlSerializer(config=SerializerConfig(indent="  "))
        xml = serializer.render(obj=obj, ns_map={None: NAMESPACE})

        output_file = "tests/output_nfse_ibscbs.xml"
        with open(output_file, "w") as f:
            f.write(xml)

        assert len(main.diff_files(input_file, output_file)) == 0

    def test_ibscbs_groups(self):
        nfse = nfse_v1_01.Nfse.from_path(os.path.join(SAMPLES, "nfse-ibscbs.xml"))
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

    def test_dps_schema_validation(self):
        nfse = nfse_v1_01.Nfse.from_path(os.path.join(SAMPLES, "nfse-ibscbs.xml"))
        dps = dps_v1_01.Dps(infDPS=nfse.infNFSe.DPS.infDPS, versao="1.01")
        self.assertTrue(dps_v1_01.Dps._get_schema_path().endswith("DPS_v1.01.xsd"))
        self.assertEqual(dps.validate_xml(), [])

    def test_legacy_100_dps_still_reads(self):
        """A 1.00 document is read and re-serialized unchanged by the 1.01
        bindings: the 1.00 layouts stay importable from the single v1_0 folder.
        """
        for filename in ["dps-regime-normal.xml", "dps-simples.xml"]:
            input_file = os.path.join(SAMPLES, filename)
            obj = dps_v1_01.Dps.from_path(input_file)
            self.assertIsInstance(obj, dps_v1_01.Dps)
            self.assertEqual(obj.versao, "1.00")
            output_file = "tests/output_nfse_dps_legacy.xml"
            with open(output_file, "w") as f:
                f.write(
                    XmlSerializer(config=SerializerConfig(indent="  ")).render(
                        obj=obj, ns_map={None: NAMESPACE}
                    )
                )
            assert len(main.diff_files(input_file, output_file)) == 0
