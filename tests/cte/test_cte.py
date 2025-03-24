# Copyright (C) 2023 - TODAY Raphaël Valyi - Akretion

import os
from pathlib import Path
from unittest import TestCase

from xmldiff import main
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from nfelib.cte.bindings import v4_0  # noqa: F401


class CTeTests(TestCase):
    def test_in_out_cte(self):
        path = os.path.join("nfelib", "cte", "samples", "v4_0")
        for filename in os.listdir(path):
            input_file = os.path.join(path, filename)
            parser = XmlParser()
            obj = parser.from_path(Path(input_file))
            serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
            xml = serializer.render(
                obj=obj, ns_map={None: "http://www.portalfiscal.inf.br/cte"}
            )

            output_file = "tests/output_cte.xml"
            with open(output_file, "w") as f:
                f.write(xml)

            diff = main.diff_files(input_file, output_file)
            self.assertEqual(len(diff), 0)
            if len(diff) != 0:
                break
