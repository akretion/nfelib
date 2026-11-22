"""SOAP bindings of the BPeRecepcaoEvento webservice of the BP-e 1.00.

Written in the layout xsdata generates from a WSDL (see nfelib/mdfe/soap): the
BP-e WSDL is only served to a client certificate, so the namespace, the
bpeRecepcaoEvento operation and the message elements follow the MOC BP-e 1.00b,
Visão Geral, items 3.3 and 3.4. Regenerate this module from the WSDL when it
can be downloaded.
"""

from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcaoEvento"


@dataclass
class BpeDadosMsg:
    class Meta:
        name = "bpeDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcaoEvento"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class BpeResultMsg:
    class Meta:
        name = "bpeResultMsg"
        namespace = "http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcaoEvento"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class BpeRecepcaoEventoSoap12BpeRecepcaoEventoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["BpeRecepcaoEventoSoap12BpeRecepcaoEventoInput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcaoEvento",
            },
        )


@dataclass
class BpeRecepcaoEventoSoap12BpeRecepcaoEventoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["BpeRecepcaoEventoSoap12BpeRecepcaoEventoOutput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcaoEvento",
            },
        )
        fault: Optional["BpeRecepcaoEventoSoap12BpeRecepcaoEventoOutput.Body.Fault"] = field(
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


class BpeRecepcaoEventoSoap12BpeRecepcaoEvento:
    style = "document"
    location = "https://bpe.svrs.rs.gov.br/ws/bpeRecepcaoEvento/bpeRecepcaoEvento.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/bpe/wsdl/BPeRecepcaoEvento/bpeRecepcaoEvento"
    input = BpeRecepcaoEventoSoap12BpeRecepcaoEventoInput
    output = BpeRecepcaoEventoSoap12BpeRecepcaoEventoOutput
