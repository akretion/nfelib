# Copyright (C) 2023  Raphaël Valyi - Akretion <raphael.valyi@akretion.com.br>

import os
import warnings
from os import environ
from pathlib import Path
from typing import Any, List, Optional

import xsdata
from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

__version__ = "2.0.5"


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

    @classmethod
    def sign_xml(
        cls,
        xml: str,
        pkcs12_data: Optional[bytes] = None,
        pkcs12_password: Optional[str] = None,
        doc_id: Optional[str] = None,
    ) -> str:
        """Sign xml file with pkcs12_data/pkcs12_password certificate.

        Sometimes you need to test with a real certificate.
        You can use the CERT_FILE and CERT_PASSWORD environment
        variables to do tests with a real certificate data.
        """
        try:
            from erpbrasil.assinatura import certificado as cert
            from erpbrasil.assinatura.assinatura import Assinatura
        except ImportError:
            raise (RuntimeError("erpbrasil.assinatura package is not installed!"))

        certificate = cert.Certificado(
            arquivo=environ.get("CERT_FILE", pkcs12_data),
            senha=environ.get("CERT_PASSWORD", pkcs12_password),
        )
        xml_etree = etree.fromstring(xml.encode("utf-8"))
        return Assinatura(certificate).assina_xml2(xml_etree, doc_id)

    def to_xml(
        self,
        indent: str = "  ",
        ns_map: Optional[dict] = None,
        pkcs12_data: Optional[bytes] = None,
        pkcs12_password: Optional[str] = None,
        doc_id: Optional[str] = None,
        pretty_print: Optional[str] = None,  # deprecated
    ) -> str:
        """Serialize binding as xml. You can fill the signature params to sign it."""

        if xsdata.__version__.split(".")[0] in ("20", "21", "22", "23"):
            serializer = XmlSerializer(
                config=SerializerConfig(pretty_print=pretty_print)
            )
        else:
            # deal with pretty_print deprecation in xsdata >= 24:
            if indent is True:  # (means pretty_print was passed)
                indent = "  "
            if pretty_print:
                warnings.warn(
                    "Setting `pretty_print` is deprecated, use `indent` instead",
                    DeprecationWarning,
                )
                indent = "  "
            elif pretty_print is False:
                indent = None

            if pkcs12_data:
                indent = None

            serializer = XmlSerializer(config=SerializerConfig(indent=indent))

        if ns_map is None:
            if self.namespace:
                ns_map = {None: self.namespace}
            elif hasattr(self.Meta, "namespace"):
                ns_map = {None: self.Meta.namespace}
            else:
                package = self._get_package()
                ns_map = {None: f"http://www.portalfiscal.inf.br/{package}"}
        xml = serializer.render(obj=self, ns_map=ns_map)
        if pkcs12_data:
            return self.sign_xml(xml, pkcs12_data, pkcs12_password, doc_id=doc_id)
        return xml

    def validate_xml(self, schema_path: Optional[str] = None) -> List:
        """Serialize binding as xml, validate it and return possible errors."""
        xml = self.to_xml()
        return self.schema_validation(xml, schema_path)

    def to_pdf(
        self,
        engine: str = "brazilfiscalreport",
        config: Any = None,  # (actually expects a DanfeConfig)
        pkcs12_data: Optional[bytes] = None,
        pkcs12_password: Optional[str] = None,
        doc_id: Optional[str] = None,
    ) -> bytes:
        """Serialize binding into pdf bytes."""
        xml = self.to_xml()
        if pkcs12_data:
            xml = self.sign_xml(xml, pkcs12_data, pkcs12_password, doc_id)

        if engine == "brazilfiscalreport":
            try:
                from brazilfiscalreport.danfe import Danfe
            except ImportError:
                raise (RuntimeError("the BrazilFiscalReport package is not installed!"))
            return bytes(
                Danfe(
                    xml=xml,
                    config=config,
                ).output(dest="S")
            )
        try:
            from erpbrasil.edoc.pdf import base
        except ImportError:
            raise (RuntimeError("the erpbrasil.edoc.pdf package is not installed!"))
        return base.ImprimirXml.imprimir(string_xml=xml)

    # this was an attempt to keep the signature inside the
    # binding before serializing it again. But at the moment it fails
    # because xsdata will serialize the Signature elements with their namespaces.
    # def sign(self, pkcs12_data: bytes = None, pkcs12_password: str = None,
    #     doc_id: str=None
    # ) -> str:
    #     xml = self.to_xml(indent=None)
    #     signed_xml = self.sign_xml(xml, pkcs12_data, pkcs12_password, element)
    #     nfe = self.from_xml(signed_xml)
    #     return nfe
