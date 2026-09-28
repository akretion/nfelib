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
from nfelib.nfcom.bindings import v1_0 as bindings
from nfelib.nfcom.bindings.v1_0.cons_stat_serv_nfcom_tipos_basico_v1_00 import (
    TconsStatServ,
    TretConsStatServ,
)
from nfelib.nfcom.bindings.v1_0.ev_canc_nfcom_v1_00 import EvCancNfcom
from nfelib.nfcom.bindings.v1_0.nfcom_tipos_basico_v1_00 import TendeEmi
from nfelib.nfcom.bindings.v1_0.nfcom_v1_00 import Nfcom
from nfelib.nfcom.bindings.v1_0.proc_nfcom_v1_00 import NfcomProc

NFCOM_NS = "http://www.portalfiscal.inf.br/nfcom"


def test_shared_types_are_resolved():
    # NFCom schemas all carry the nfcom targetNamespace (no chameleon include
    # like the NF3e tiposGeralNF3e), but the shared tiposGeralNFCom types must
    # still resolve to their real enum types instead of degrading to str.
    hints = get_type_hints(TendeEmi)
    uf_type = hints["UF"].__args__[0]
    assert uf_type is not str
    assert issubclass(uf_type, Enum)
    assert uf_type.__name__ == "Tuf"


def test_schema_metadata_is_injected():
    # generate_bindings.py injects the source schema package documented in
    # CHANGELOG_SCHEMAS.md into the binding package __init__.py.
    assert bindings.SCHEMA_VERSION
    assert bindings.SCHEMA_PACKAGE
    assert bindings.NOTA_TECNICA
    assert bindings.SOURCE_URL.startswith("https://")


def test_common_mixin_on_roots():
    # CommonMixin is applied selectively to the NFCom document roots only
    # (Tnfcom via the .xsdata.xml extension); shared root names such as
    # TconsStatServ are deliberately left alone: they exist in the
    # nfe/cte/mdfe bindings too and a blanket extension would leak the
    # mixin into every binding on the next regeneration.
    assert issubclass(NfcomProc, CommonMixin)
    assert issubclass(Nfcom, CommonMixin)
    assert issubclass(EvCancNfcom, CommonMixin)
    assert not issubclass(TconsStatServ, CommonMixin)
    assert not issubclass(TretConsStatServ, CommonMixin)


def test_in_out_nfcom(tmp_path):
    path = os.path.join("nfelib", "nfcom", "samples", "v1_0")
    for filename in os.listdir(path):
        input_file = os.path.join(path, filename)
        obj = XmlParser().from_path(Path(input_file))
        xml = XmlSerializer(config=SerializerConfig(indent="\t")).render(
            obj=obj, ns_map={None: NFCOM_NS}
        )
        output_file = tmp_path / filename
        output_file.write_text(xml)
        diff = main.diff_files(input_file, str(output_file))
        assert len(diff) == 0
