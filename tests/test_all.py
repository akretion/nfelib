# Copyright (C) 2019 - TODAY Raphaël Valyi - Akretion

import os
import sys
from os import path
import importlib
import inspect
from enum import EnumMeta
from xmldiff import main

sys.path.append(path.join(path.dirname(__file__), "..", "nfelib"))

from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from pathlib import Path
import pkgutil


def visit_nested_classes(cls, classes):
    classes.add(cls)
    for attr in dir(cls):
        nested = getattr(cls, attr)
        if (
            not inspect.isclass(nested)
            or nested.__name__ == "type"
            or nested.__name__.endswith(".Meta")
        ):
            continue
        visit_nested_classes(nested, classes)


def test_init_all():
    for binding in pkgutil.walk_packages(["nfelib/bindings"]):
        if binding.name in ("nfe_epec"):
            # FIXME this binding is buggy!! (circular def)
            continue
        binding_path = "nfelib/bindings/" + binding.name
        for version in pkgutil.walk_packages([binding_path]):
            version_path = "nfelib/bindings/%s/%s" % (
                binding.name,
                version.name,
            )
            for modpkg in pkgutil.walk_packages([version_path]):
                if modpkg.name in ("e110140_v1_00", "leiaute_epec_v1_00"):
                    continue
                mod_name = "nfelib.bindings.%s.%s.%s" % (
                    binding.name,
                    version.name,
                    modpkg.name,
                )
                mod = importlib.import_module(mod_name)

                for _klass_name, klass in mod.__dict__.items():
                    if isinstance(klass, type) and type(klass) != EnumMeta:
                        classes = set()
                        visit_nested_classes(klass, classes)
                        for cls in classes:
                            if cls.__name__ in ("XmlDateTime", "XmlDate"):
                                continue
                            cls()
