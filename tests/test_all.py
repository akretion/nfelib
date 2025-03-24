# Copyright (C) 2019 - TODAY Raphaël Valyi - Akretion

import importlib
import inspect
import logging
import pkgutil
from enum import EnumMeta

_logger = logging.getLogger(__name__)


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
    for pkg_name in pkgutil.walk_packages(["nfelib/"]):
        pkg_path = "nfelib/" + pkg_name.name + "/bindings"
        _logger.info(pkg_path)
        for version in pkgutil.walk_packages([pkg_path]):
            if pkg_name.name == "v4_00":
                version_path = pkg_path
            else:
                version_path = f"nfelib/{pkg_name.name}/bindings/{version.name}"
            _logger.info("  walking over:  " + version_path)
            for modpkg in pkgutil.walk_packages([version_path]):
                if pkg_name.name == "v4_00":
                    mod_name = (pkg_path + "/" + modpkg.name).replace("/", ".")
                else:
                    mod_name = (
                        f"nfelib.{pkg_name.name}.bindings.{version.name}.{modpkg.name}"
                    )
                _logger.info("    " + mod_name)
                mod = importlib.import_module(mod_name)

                for _klass_name, klass in mod.__dict__.items():
                    if isinstance(klass, type) and type(klass) is not EnumMeta:
                        classes = set()
                        visit_nested_classes(klass, classes)
                        for cls in classes:
                            if (
                                cls.__name__
                                in ("XmlDateTime", "XmlDate", "MixedContainer")
                                or "FixedOffsetTZ" in cls.__name__
                            ):
                                continue
                            cls()
