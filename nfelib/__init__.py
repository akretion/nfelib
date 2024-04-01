# Copyright (C) 2023  Raphaël Valyi - Akretion <raphael.valyi@akretion.com.br>

import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

__version__ = "2.0.4"


class CommonMixin:
    """Generic helper class. Can be overriden for specific documents."""

    schema_path = None
    namespace = None

    @classmethod
    def from_xml(cls, xml: str) -> Any:
        """Parse xml and retun an instance of the class."""
        return XmlParser().from_string(xml)

    @classmethod
    def from_path(cls, path: str) -> Any:
        """Parse xml at given path and return an instance of the class."""
        xml = Path(path).read_text()
        return cls.from_xml(xml)

    @classmethod
    def schema_validation(cls, xml: str, schema_path: Optional[str] = None) -> List:
        """Validate xml against xsd schema at given path."""
        validation_messages = []
        doc_etree = etree.fromstring(xml.encode("utf-8"))
        if schema_path is None:
            if cls.schema_path is not None:
                schema_path = cls.schema_path
            else:
                schema_path = cls._get_schema_path()
        xmlschema_doc = etree.parse(schema_path)
        parser = etree.XMLSchema(xmlschema_doc)

        if not parser.validate(doc_etree):
            for e in parser.error_log:
                validation_messages.append(e.message)
        return validation_messages

    @classmethod
    def _get_package(cls) -> str:
        return cls.__module__.split("nfelib.")[1].split(".bindings")[0].split("_")[0]

    @classmethod
    def _get_schema_path(cls) -> str:
        package = cls._get_package()
        if package == "nfe":
            return os.path.join(
                os.path.dirname(__file__),
                "nfe",
                "schemas",
                "v4_0",
                "nfe_v4.00.xsd",
            )
        if package == "nfse":
            return os.path.join(
                os.path.dirname(__file__),
                "nfse",
                "schemas",
                "v1_0",
                "DPS_v1.00.xsd",
            )
        if package == "mdfe":
            return os.path.join(
                os.path.dirname(__file__),
                "mdfe",
                "schemas",
                "v3_0",
                "mdfe_v3.00.xsd",
            )
        if package == "cte":
            return os.path.join(
                os.path.dirname(__file__),
                "cte",
                "schemas",
                "v4_0",
                "cte_v4.00.xsd",
            )
        if package == "bpe":
            return os.path.join(
                os.path.dirname(__file__),
                "bpe",
                "schemas",
                "v1_0",
                "bpe_v1.00.xsd",
            )
        return "undef"

    def to_xml(self, pretty_print: bool = True, ns_map: Optional[Dict] = None) -> str:
        """Serialize binding as an xml string."""
        serializer = XmlSerializer(SerializerConfig(pretty_print=pretty_print))
        if ns_map is None:
            if self.namespace:
                ns_map = {None: self.namespace}
            elif hasattr(self.Meta, "namespace"):
                ns_map = {None: self.Meta.namespace}
            else:
                package = self._get_package()
                ns_map = {None: f"http://www.portalfiscal.inf.br/{package}"}
        return serializer.render(obj=self, ns_map=ns_map)

    def validate_xml(self, schema_path: Optional[str] = None) -> List:
        """Serialize binding as xml, validate it and return possible errors."""
        xml = self.to_xml()
        return self.schema_validation(xml, schema_path)
