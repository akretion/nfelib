# Copyright (C) 2023 - TODAY Raphaël Valyi - Akretion

import os
from xmldiff import main

from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from pathlib import Path

from nfelib.mdfe.bindings import v3_0


def test_in_out_mdfe():
    path = os.path.join("nfelib", "mdfe", "samples", "v3_0")
    for filename in os.listdir(path):
        input_file = os.path.join(path, filename)
        parser = XmlParser()
        obj = parser.from_path(Path(input_file))
        serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
        xml = serializer.render(
            obj=obj,
            ns_map={None: "http://www.portalfiscal.inf.br/mdfe"}
        )

        output_file = "tests/output_mdfe.xml"
        with open(output_file, "w") as f:
            f.write(xml)

        diff = main.diff_files(input_file, output_file)
        assert len(diff) == 0
        if len(diff) != 0:
            break
