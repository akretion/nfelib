# Copyright (C) 2019 - TODAY Raphaël Valyi - Akretion

import os
from pathlib import Path
from unittest import TestCase

from xmldiff import main
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from nfelib.nfe_evento_cce.bindings.v1_0.cce_v1_00 import Evento


class CCeTests(TestCase):
    def test_in_out_leiauteCCe(self):
        path = os.path.join("nfelib", "nfe_evento_cce", "samples", "v1_0")
        for filename in os.listdir(path):
            input_file = os.path.join(path, filename)
            parser = XmlParser()
            obj = parser.from_path(Path(input_file), Evento)
            serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
            xml = serializer.render(
                obj=obj, ns_map={None: "http://www.portalfiscal.inf.br/nfe"}
            )

            output_file = "tests/output_nfe_evento_cce.xml"
            with open(output_file, "w") as f:
                f.write(xml)

            diff = main.diff_files(input_file, output_file)
            self.assertEqual(len(diff), 0)
            if len(diff) != 0:
                break
