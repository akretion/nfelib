# Copyright (C) 2026 - TODAY KMEE

import os
from enum import Enum
from pathlib import Path
from typing import get_type_hints

from erpbrasil.assinatura import misc
from xmldiff import main
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from nfelib import CommonMixin
from nfelib.nfeabi.bindings import v1_0 as bindings
from nfelib.nfeabi.bindings.v1_0.cons_stat_serv_nfe_abitipos_basico_v1_00 import (
    TconsStatServ,
    TretConsStatServ,
)
from nfelib.nfeabi.bindings.v1_0.ev_aprop_cred_ind_nfe_abi_v1_00 import (
    EvApropCredIndNfeAbi,
)
from nfelib.nfeabi.bindings.v1_0.ev_canc_nfe_abi_v1_00 import EvCancNfeAbi
from nfelib.nfeabi.bindings.v1_0.ev_desfazim_alienac_nfe_abi_v1_00 import (
    EvDesfazimAlienac,
)
from nfelib.nfeabi.bindings.v1_0.ev_pag_parcela_nfe_abi_v1_00 import (
    EvPagParcelaNfeAbi,
)
from nfelib.nfeabi.bindings.v1_0.nfe_abi_v1_00 import NfeAbi, Tide
from nfelib.nfeabi.bindings.v1_0.proc_nfe_abi_v1_00 import NfeabiProc

NFEABI_NS = "http://www.portalfiscal.inf.br/nfeabi"
SAMPLES = os.path.join("nfelib", "nfeabi", "samples", "v1_0")


def test_shared_types_are_resolved():
    # the tiposGeralNFeABI types must resolve to their real enum types
    # instead of degrading to str.
    hints = get_type_hints(Tide)
    for name, type_name in (("cUF", "TcodUfIbge"), ("tpAmb", "Tamb")):
        enum_type = hints[name].__args__[0]
        assert issubclass(enum_type, Enum)
        assert enum_type.__name__ == type_name


def test_schema_metadata_is_injected():
    # generate_bindings.py injects the source schema package documented in
    # CHANGELOG_SCHEMAS.md into the binding package __init__.py.
    assert bindings.SCHEMA_VERSION
    assert bindings.SCHEMA_PACKAGE
    assert bindings.NOTA_TECNICA
    assert bindings.SOURCE_URL.startswith("https://")


def test_common_mixin_on_roots():
    # CommonMixin is applied selectively to the NF-e ABI document roots and
    # event details only; shared root names such as TconsStatServ are
    # deliberately left alone.
    for klass in (
        NfeAbi,
        NfeabiProc,
        EvCancNfeAbi,
        EvDesfazimAlienac,
        EvApropCredIndNfeAbi,
        EvPagParcelaNfeAbi,
    ):
        assert issubclass(klass, CommonMixin)
    assert not issubclass(TconsStatServ, CommonMixin)
    assert not issubclass(TretConsStatServ, CommonMixin)


def test_in_out_nfeabi(tmp_path):
    for filename in os.listdir(SAMPLES):
        input_file = os.path.join(SAMPLES, filename)
        obj = XmlParser().from_path(Path(input_file))
        xml = XmlSerializer(config=SerializerConfig(indent="\t")).render(
            obj=obj, ns_map={None: NFEABI_NS}
        )
        output_file = tmp_path / filename
        output_file.write_text(xml)
        diff = main.diff_files(input_file, str(output_file))
        assert len(diff) == 0


def test_signed_sample_is_valid():
    # the sample is unsigned, like the other samples: signed with a fake
    # certificate it must pass the official schema validation.
    password = "testpassword"
    certificate = misc.create_fake_certificate_file(
        valid=True,
        passwd=password,
        issuer="TEST ISSUER",
        country="BR",
        subject="TEST SUBJECT",
    )
    for filename in os.listdir(SAMPLES):
        nfeabi = NfeAbi.from_path(os.path.join(SAMPLES, filename))
        signed_xml = nfeabi.to_xml(
            pkcs12_data=certificate,
            pkcs12_password=password,
            doc_id=nfeabi.infNFeABI.Id,
        )
        assert NfeAbi.schema_validation(signed_xml) == []
