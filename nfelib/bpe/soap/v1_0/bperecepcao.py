"""SOAP bindings of the BPeRecepcao webservice of the BP-e 1.00.

Written in the layout xsdata generates from a WSDL (see nfelib/mdfe/soap): the
BP-e WSDL is only served to a client certificate, so the namespace, the
bpeRecepcao operation and the message elements follow the MOC BP-e 1.00b, Visão
Geral, items 3.3 and 3.4. The message goes gzipped and base64 encoded as the
text of bpeDadosMsg. Regenerate this module from the WSDL when it can be
downloaded.
"""

from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcao"


@dataclass
class BpeDadosMsg:
    class Meta:
        name = "bpeDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcao"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class BpeResultMsg:
    class Meta:
        name = "bpeResultMsg"
        namespace = "http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcao"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class BpeRecepcaoSoap12BpeRecepcaoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["BpeRecepcaoSoap12BpeRecepcaoInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        bpeDadosMsg: Optional[BpeDadosMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcao",
            },
        )


@dataclass
class BpeRecepcaoSoap12BpeRecepcaoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["BpeRecepcaoSoap12BpeRecepcaoOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        bpeResultMsg: Optional[BpeResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcao",
            },
        )
        fault: Optional["BpeRecepcaoSoap12BpeRecepcaoOutput.Body.Fault"] = field(
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


class BpeRecepcaoSoap12BpeRecepcao:
    style = "document"
    location = "https://bpe.svrs.rs.gov.br/ws/bpeRecepcao/bpeRecepcao.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcao/bpeRecepcao"
    input = BpeRecepcaoSoap12BpeRecepcaoInput
    output = BpeRecepcaoSoap12BpeRecepcaoOutput
