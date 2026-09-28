# Copyright (C) 2026 - TODAY Raphaël Valyi - Akretion

import os
from enum import Enum
from pathlib import Path
from typing import get_type_hints

from xmldiff import main
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from nfelib import CommonMixin
from nfelib.bpe.bindings import v1_0 as bindings
from nfelib.bpe.bindings.v1_0.bpe_ta_v1_00 import BpeTa
from nfelib.bpe.bindings.v1_0.bpe_tipos_basico_v1_00 import TendeEmi
from nfelib.bpe.bindings.v1_0.bpe_v1_00 import Bpe
from nfelib.bpe.bindings.v1_0.cons_sit_bpe_v1_00 import ConsSitBpe
from nfelib.bpe.bindings.v1_0.cons_stat_serv_bpe_v1_00 import ConsStatServBpe
from nfelib.bpe.bindings.v1_0.evento_bpe_v1_00 import EventoBpe
from nfelib.bpe.bindings.v1_0.proc_bpe_v1_00 import BpeProc

BPE_NS = "http://www.portalfiscal.inf.br/bpe"

# The samples are parsed with their explicit root class: the generated class
# name does not always match the root element name convention (the BPeTM
# element is bound to BpeTm), so name-based root resolution is not reliable.
SAMPLE_ROOTS = {
    "bpe-ta.xml": BpeTa,
    "bpe.xml": Bpe,
}


def test_shared_types_are_resolved():
    # the BPe schemas all carry the bpe targetNamespace (no chameleon include
    # like the NF3e tiposGeralNF3e), but the shared tiposGeralBPe types must
    # still resolve to their real enum types instead of degrading to str.
    hints = get_type_hints(TendeEmi)
    uf_type = hints["UF"].__args__[0]
    assert uf_type is not str
    assert issubclass(uf_type, Enum)
    assert uf_type.__name__ == "TufSemEx"


def test_schema_metadata_is_injected():
    # generate_bindings.py injects the source schema package documented in
    # CHANGELOG_SCHEMAS.md into the binding package __init__.py.
    assert bindings.SCHEMA_VERSION
    assert bindings.SCHEMA_PACKAGE
    assert bindings.NOTA_TECNICA
    assert bindings.SOURCE_URL.startswith("https://")


def test_common_mixin_on_roots():
    # CommonMixin is applied selectively to the BPe document roots only
    # (Tbpe, TbpeTm and the BPe/BPeTM/evento roots via the .xsdata.xml
    # extensions); shared root names such as TconsStatServ are deliberately
    # left alone: they exist in the nfe/cte/mdfe bindings too and a blanket
    # extension would leak the mixin into every binding on the next
    # regeneration.
    assert issubclass(Bpe, CommonMixin)
    assert issubclass(BpeTa, CommonMixin)
    assert issubclass(BpeProc, CommonMixin)
    assert issubclass(EventoBpe, CommonMixin)
    assert not issubclass(ConsStatServBpe, CommonMixin)
    assert not issubclass(ConsSitBpe, CommonMixin)


def test_in_out_bpe(tmp_path):
    path = os.path.join("nfelib", "bpe", "samples", "v1_0")
    for filename in sorted(os.listdir(path)):
        input_file = os.path.join(path, filename)
        obj = XmlParser().from_path(Path(input_file), SAMPLE_ROOTS[filename])
        xml = XmlSerializer(config=SerializerConfig(indent="\t")).render(
            obj=obj, ns_map={None: BPE_NS}
        )
        output_file = tmp_path / filename
        output_file.write_text(xml)
        diff = main.diff_files(input_file, str(output_file))
        assert len(diff) == 0
