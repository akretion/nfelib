# Copyright (C) 2023 - TODAY Raphaël Valyi - Akretion

import os
from pathlib import Path
from unittest import TestCase

from xmldiff import main
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from nfelib.cte.bindings import v4_0  # noqa: F401
from nfelib.cte.bindings.v4_0.cte_tipos_basico_v4_00 import Tcte, TcteOs, TcteSimp


class CTeTests(TestCase):
    def test_patched_xsdata_for_ibscsb(self):
        # see https://github.com/akretion/nfelib/pull/151
        # IBSCBS should be TtribCte, not str
        assert (
            str(Tcte.InfCte.Imp().__annotations__["IBSCBS"])
            == "typing.Optional[nfelib.cte.bindings.v4_0.dfe_tipos_basicos_v1_00.TtribCte]"
            # Python < 3.9:
            or str(Tcte.InfCte.Imp().__annotations__["IBSCBS"])
            == "typing.Union[nfelib.cte.bindings.v4_0.dfe_tipos_basicos_v1_00.TtribCte, NoneType]"
        )
        assert (
            str(TcteOs.InfCte.Imp().__annotations__["IBSCBS"])
            == "typing.Optional[nfelib.cte.bindings.v4_0.dfe_tipos_basicos_v1_00.TtribCte]"
            # Python < 3.9:
            or str(TcteOs.InfCte.Imp().__annotations__["IBSCBS"])
            == "typing.Union[nfelib.cte.bindings.v4_0.dfe_tipos_basicos_v1_00.TtribCte, NoneType]"
        )
        assert (
            str(TcteSimp.InfCte.Imp().__annotations__["IBSCBS"])
            == "typing.Optional[nfelib.cte.bindings.v4_0.dfe_tipos_basicos_v1_00.TtribCte]"
            # Python < 3.9:
            or str(TcteSimp.InfCte.Imp().__annotations__["IBSCBS"])
            == "typing.Union[nfelib.cte.bindings.v4_0.dfe_tipos_basicos_v1_00.TtribCte, NoneType]"
        )

    def test_in_out_cte(self):
        path = os.path.join("nfelib", "cte", "samples", "v4_0")
        for filename in os.listdir(path):
            input_file = os.path.join(path, filename)
            parser = XmlParser()
            obj = parser.from_path(Path(input_file))
            serializer = XmlSerializer(config=SerializerConfig(indent="  "))
            xml = serializer.render(
                obj=obj, ns_map={None: "http://www.portalfiscal.inf.br/cte"}
            )

            output_file = "tests/output_cte.xml"
            with open(output_file, "w") as f:
                f.write(xml)

            diff = main.diff_files(input_file, output_file)
            self.assertEqual(
                len(diff),
                0,
                f"Error {output_file} != {input_file}. "
                "Stopping tests here so you can compare XML files.",
            )
            if len(diff) != 0:
                break
