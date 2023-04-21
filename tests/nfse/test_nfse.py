# Copyright (C) 2019 - TODAY Raphaël Valyi - Akretion

import os
from xmldiff import main

from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from pathlib import Path

from nfelib.nfse.bindings.v1_0 import nfse_v1_00
from nfelib.nfse.bindings.v1_0 import dps_v1_00


def test_in_out_nfse():
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

def test_in_out_dps():
    path = os.path.join("nfelib", "nfse", "samples", "v1_0")
    for filename in ["GerarNFSeEnvio-env-loterps.xml", "ConsultarNFSeRPS-ped-sitnfserps.xml"]:
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

def test_in_out_pedRegEvento():
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
