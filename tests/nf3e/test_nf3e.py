# Copyright (C) 2026 - TODAY Raphaël Valyi - Akretion

import os
from pathlib import Path
from typing import get_type_hints

from xmldiff import main
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from nfelib import CommonMixin
from nfelib.nf3e.bindings.v1_0.cons_stat_serv_nf3e_tipos_basico_v1_00 import (
    TconsStatServ,
    TretConsStatServ,
)
from nfelib.nf3e.bindings.v1_0.nf3e_tipos_basico_v1_00 import TendeEmi
from nfelib.nf3e.bindings.v1_0.nf3e_v1_00 import Nf3E
from nfelib.nf3e.bindings.v1_0.proc_nf3e_v1_00 import Nf3EProc

NF3E_NS = "http://www.portalfiscal.inf.br/nf3e"


def test_patched_xsdata_for_chameleon_types():
    # the NF3e schemas share chameleon-included simple types (tiposGeralNF3e
    # has no targetNamespace of its own); without the generator chameleon
    # fix those fall back to plain str instead of the resolved enum type.
    hints = get_type_hints(TendeEmi)
    assert "TufSemEx" in str(hints["UF"])
    assert hints["UF"] is not str


def test_common_mixin_on_roots():
    # CommonMixin is applied selectively to the NF3e document roots only
    # (Tnf3E via the .xsdata.xml extension); shared root names such as
    # TconsStatServ are deliberately left alone: they exist in the
    # nfe/cte/mdfe bindings too and a blanket extension would leak the
    # mixin into every binding on the next regeneration.
    assert issubclass(Nf3EProc, CommonMixin)
    assert issubclass(Nf3E, CommonMixin)
    assert not issubclass(TconsStatServ, CommonMixin)
    assert not issubclass(TretConsStatServ, CommonMixin)


def test_in_out_nf3e(tmp_path):
    path = os.path.join("nfelib", "nf3e", "samples", "v1_0")
    for filename in os.listdir(path):
        input_file = os.path.join(path, filename)
        obj = XmlParser().from_path(Path(input_file))
        xml = XmlSerializer(config=SerializerConfig(indent="\t")).render(
            obj=obj, ns_map={None: NF3E_NS}
        )
        output_file = tmp_path / filename
        output_file.write_text(xml)
        diff = main.diff_files(input_file, str(output_file))
        assert len(diff) == 0
