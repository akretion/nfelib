"""SOAP bindings of the NFAgRecepcao webservice of the NFAg 1.00.

Written in the layout xsdata generates from a WSDL (see nfelib/mdfe/soap): the
NFAg WSDL is only served to a client certificate, so the namespace, the
NFAgRecepcao operation and the message elements follow the MOC NFAg 1.00l,
Visão Geral, item 3. The message goes gzipped and base64 encoded as the text of
nfagDadosMsg. Regenerate this module from the WSDL when it can be downloaded.
"""

from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgRecepcao"


@dataclass
class NfagDadosMsg:
    class Meta:
        name = "nfagDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgRecepcao"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class NfagResultMsg:
    class Meta:
        name = "nfagResultMsg"
        namespace = "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgRecepcao"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class NfagRecepcaoSoap12NfagRecepcaoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfagRecepcaoSoap12NfagRecepcaoInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        nfagDadosMsg: Optional[NfagDadosMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgRecepcao",
            },
        )


@dataclass
class NfagRecepcaoSoap12NfagRecepcaoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfagRecepcaoSoap12NfagRecepcaoOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        nfagResultMsg: Optional[NfagResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgRecepcao",
            },
        )
        fault: Optional["NfagRecepcaoSoap12NfagRecepcaoOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            },
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                },
            )


class NfagRecepcaoSoap12NfagRecepcao:
    style = "document"
    location = "https://nfag.svrs.rs.gov.br/WS/NFAgRecepcao/NFAgRecepcao.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgRecepcao/NFAgRecepcao"
    input = NfagRecepcaoSoap12NfagRecepcaoInput
    output = NfagRecepcaoSoap12NfagRecepcaoOutput
