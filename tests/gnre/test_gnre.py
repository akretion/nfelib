import os
from pathlib import Path

import xmlschema
from xmldiff import main
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from nfelib.gnre.bindings import v2_0 as bindings
from nfelib.gnre.bindings.v2_0.lote_gnre_v2_00 import TloteGnre

GNRE_NS = "http://www.gnre.pe.gov.br"
SAMPLES = os.path.join("nfelib", "gnre", "samples", "v2_0")
SCHEMAS = os.path.join("nfelib", "gnre", "schemas", "v2_0")


def test_schema_metadata_is_injected():
    assert bindings.SCHEMA_VERSION
    assert bindings.SCHEMA_PACKAGE
    assert bindings.SOURCE_URL.startswith("https://")


def test_lote_sample_validates_against_xsd():
    schema = xmlschema.XMLSchema(os.path.join(SCHEMAS, "lote_gnre_v2.00.xsd"))
    for filename in os.listdir(SAMPLES):
        schema.validate(os.path.join(SAMPLES, filename))


def test_in_out_lote(tmp_path):
    for filename in os.listdir(SAMPLES):
        input_file = os.path.join(SAMPLES, filename)
        obj = XmlParser().from_path(Path(input_file), TloteGnre)
        item = obj.guias.TDadosGNRE[0].itensGNRE.item[0]
        assert [valor.tipo.value for valor in item.valor] == ["11", "12"]
        xml = XmlSerializer(config=SerializerConfig(indent="\t")).render(
            obj=obj, ns_map={None: GNRE_NS}
        )
        output_file = tmp_path / filename
        output_file.write_text(xml)
        diff = main.diff_files(input_file, str(output_file))
        assert len(diff) == 0
