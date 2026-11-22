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
from nfelib.nfgas.bindings import v1_0 as bindings
from nfelib.nfgas.bindings.v1_0.cons_stat_serv_nfgas_tipos_basico_v1_00 import (
    TconsStatServ,
    TretConsStatServ,
)
from nfelib.nfgas.bindings.v1_0.ev_canc_nfgas_v1_00 import EvCancNfgas
from nfelib.nfgas.bindings.v1_0.nfgas_tipos_basico_v1_00 import TendeEmi, Timp
from nfelib.nfgas.bindings.v1_0.nfgas_v1_00 import Nfgas
from nfelib.nfgas.bindings.v1_0.proc_nfgas_v1_00 import NfgasProc

NFGAS_NS = "http://www.portalfiscal.inf.br/nfgas"
SAMPLES = os.path.join("nfelib", "nfgas", "samples", "v1_0")


def test_shared_types_are_resolved():
    # the tiposGeralNFGas types must resolve to their real enum types instead
    # of degrading to str.
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
    # CommonMixin is applied selectively to the NFGas document roots only;
    # shared root names such as TconsStatServ are deliberately left alone.
    assert issubclass(Nfgas, CommonMixin)
    assert issubclass(NfgasProc, CommonMixin)
    assert issubclass(EvCancNfgas, CommonMixin)
    assert not issubclass(TconsStatServ, CommonMixin)
    assert not issubclass(TretConsStatServ, CommonMixin)


def test_tx_reg_keeps_its_tag():
    # imposto has a TxReg field and a nested TxReg class: the field is renamed
    # by an .xsdata.xml substitution, the XML tag stays the same.
    tx_reg = Timp.__dataclass_fields__["txReg"]
    assert tx_reg.metadata["name"] == "TxReg"
    assert tx_reg.default is None


def test_in_out_nfgas(tmp_path):
    for filename in os.listdir(SAMPLES):
        input_file = os.path.join(SAMPLES, filename)
        obj = XmlParser().from_path(Path(input_file))
        xml = XmlSerializer(config=SerializerConfig(indent="\t")).render(
            obj=obj, ns_map={None: NFGAS_NS}
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
        nfgas = Nfgas.from_path(os.path.join(SAMPLES, filename))
        signed_xml = nfgas.to_xml(
            pkcs12_data=certificate,
            pkcs12_password=password,
            doc_id=nfgas.infNFGas.Id,
        )
        assert Nfgas.schema_validation(signed_xml) == []
