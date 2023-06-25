import logging
import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from enum import EnumMeta
from typing import Any, Dict, Optional, Type

# NOTE: eventually would be great not having a hard dependency on erpbrasil.assinatura
from erpbrasil.assinatura.assinatura import Assinatura
from erpbrasil.assinatura.certificado import ArquivoCertificado
from lxml import etree
from requests.adapters import HTTPAdapter, Retry
from xsdata.formats.dataclass.client import Client, Config
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

_logger = logging.Logger(__name__)

RETRIES = 5
BACKOFF_FACTOR = 0.1
RETRY_ERRORS = (500, 502, 503, 504)
TIMEOUT = 5.0
PRETTY_PRINT = True  # since waiting the fisc server 3+ sec, perf penaly is OK


@dataclass
class SoapClient(Client):
    certificate = object()
    server: str = "undef"
    ambiente: int = 2  # (Portuguese to match erpbrasil.edoc)
    uf: str = "undef"
    versao = "undef"
    response_bindings_packages = []
    serializer = XmlSerializer(config=SerializerConfig(pretty_print=PRETTY_PRINT))
    parser = XmlParser()

    @classmethod
    def from_service(
        cls, tpAmb: int, cUF: str, certificate: Any, **kwargs: str
    ) -> Client:
        """Instantiate client from a service definition."""
        obj = None
        client = cls(config=Config.from_service(obj, **kwargs))
        client.certificate = certificate
        client.uf = cUF
        if not kwargs.get("location"):
            client.server = client.get_server("nfe", cUF)
        return client

    @classmethod
    def get_server(cls, service: str, cUF: str) -> str:
        return "not implemented here"

    def send(
        self,
        action_class: Type,
        obj: Any,
        return_type: Type,
        headers: Optional[Dict] = None,
        placeholder_exp: str = "",
        placeholder_content: str = "",
    ) -> Any:
        path = "/".join(["/ws"] + action_class.location.split("/")[-2:])
        # FIXME some UF may not have /ws and might need a "?wsdl" suffix
        location = self.server + path
        self.config = Config.from_service(action_class, location=location)

        if not isinstance(obj, dict) and not isinstance(obj, Type):
            obj = {"Body": {"nfeDadosMsg": {"content": [obj]}}}

        with ArquivoCertificado(self.certificate, "r") as (key, cert):
            self.transport.session.cert = (key, cert)
            self.transport.session.verify = False  # TODO improve (param)

            retries = Retry(  # retry in case of errors
                total=RETRIES,
                backoff_factor=BACKOFF_FACTOR,
                status_forcelist=RETRY_ERRORS,
            )
            self.transport.session.mount("https://", HTTPAdapter(max_retries=retries))
            self.transport.timeout = TIMEOUT

            print("\n", self.config.location)
            data = self.prepare_payload(obj, placeholder_exp, placeholder_content)
            _logger.debug(data)
            print("-----REQUEST------")
            print(data)
            print("-----------")
            headers = self.prepare_headers(headers or {})
            response = self.transport.post(
                self.config.location, data=data, headers=headers
            )
            print("-----RESPONSE------")
            print(response)
            print("-----------")
            response = self.parser.from_bytes(response, self.config.output)
            _logger.debug(response)

            # the challenge with the Fiscal SOAP is the return type
            # is a wildcard in the WSDL, so here we help xsdata to figure
            # out which dataclass to use to parse the resultMsg content
            # based on the XML qname of the element.
            anyElement = response.body.nfeResultMsg.content[0]  # TODO safe guard
            anyElement.qname = None
            anyElement.text = None
            # TODO deal with children or attributes (and remove their qname and text) ?

            xml = self.serializer.render(
                obj=anyElement, ns_map={None: "http://www.portalfiscal.inf.br/nfe"}
            )
            print(xml)
            return self.parser.from_string(xml, return_type)

    def prepare_payload(
        self,
        obj: Any,
        placeholder_exp: str = "",
        placeholder_content: str = "",
    ) -> Any:
        """
        Prepare and serialize payload to be sent.
        Overriden to skip namespaces to please the Fazenda
        """
        if isinstance(obj, Dict):
            obj = self.dict_converter.convert(obj, self.config.input)
        data = self.serializer.render(
            obj=obj, ns_map={None: "http://www.portalfiscal.inf.br/nfe"}
        )
        if placeholder_exp and placeholder_content:
            # used to match "<NFe/>" in the payload for instance
            # this allows injecting the signed XML in the payload without
            # having to serialize the XML again and possibly screw the signature
            exp = re.compile(placeholder_exp)
            matches = exp.search(data)
            if matches:
                data = (
                    data.replace(matches[0], placeholder_content)
                    .replace("\n", "")
                    .replace("\r", "")
                )

        print(data)
        return data

    def sign_xml(self, xml: str, Id: str) -> str:
        xml_etree = etree.fromstring(xml.encode("utf-8"))
        signed_xml = Assinatura(self.certificate).assina_xml2(xml_etree, Id)
        return signed_xml

    def _gera_numero_lote(self):
        return datetime.now().strftime("%Y%m%d%H%M%S")

    def _aguarda_tempo_medio(self, proc_envio: Any):
        pass

    def _hora_agora(self):
        FORMAT = "%Y-%m-%dT%H:%M:%S"
        # return datetime.today().strftime(FORMAT) + '-00:00'
        return (
            datetime.strftime(datetime.now(tz=timezone(timedelta(hours=-3))), FORMAT)
            + str(timezone(timedelta(hours=-3)))[3:]
        )
