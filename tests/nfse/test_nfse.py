# Copyright (C) 2023 - TODAY Raphaël Valyi - Akretion

import os
from pathlib import Path
from unittest import TestCase

from xmldiff import main
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from nfelib.nfse.bindings.v1_0 import (
    dps_v1_00,  # noqa: F401
    nfse_v1_00,  # noqa: F401
)


class NFseTests(TestCase):
    def test_in_out_consulta(self):
        path = os.path.join("nfelib", "nfse", "samples", "v1_0")
        for filename in ["ConsultarNFSeEnvio-ped-sitnfse.xml"]:
            input_file = os.path.join(path, filename)
            parser = XmlParser()
            obj = parser.from_path(Path(input_file))
            serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
            xml = serializer.render(
                obj=obj, ns_map={None: "http://www.sped.fazenda.gov.br/nfse"}
            )

            output_file = "tests/output_nfse.xml"
            with open(output_file, "w") as f:
                f.write(xml)

            diff = main.diff_files(input_file, output_file)
            assert len(diff) == 0
            if len(diff) != 0:
                break

    def test_in_out_dps(self):
        path = os.path.join("nfelib", "nfse", "samples", "v1_0")
        for filename in ["dps-simples.xml", "dps-regime-normal.xml"]:
            input_file = os.path.join(path, filename)
            parser = XmlParser()
            obj = parser.from_path(Path(input_file))
            serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
            xml = serializer.render(
                obj=obj, ns_map={None: "http://www.sped.fazenda.gov.br/nfse"}
            )

            output_file = "tests/output_nfse_dps.xml"
            with open(output_file, "w") as f:
                f.write(xml)

            diff = main.diff_files(input_file, output_file)
            assert len(diff) == 0
            if len(diff) != 0:
                break

    def test_in_out_pedRegEvento(self):
        path = os.path.join("nfelib", "nfse", "samples", "v1_0")
        for filename in ["CancelarNFSe-ped-cannfse.xml"]:
            input_file = os.path.join(path, filename)
            parser = XmlParser()
            obj = parser.from_path(Path(input_file))
            serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
            xml = serializer.render(
                obj=obj, ns_map={None: "http://www.sped.fazenda.gov.br/nfse"}
            )

            output_file = "tests/output_nfse_pedRegEvento.xml"
            with open(output_file, "w") as f:
                f.write(xml)

            diff = main.diff_files(input_file, output_file)
            assert len(diff) == 0
            if len(diff) != 0:
                break
