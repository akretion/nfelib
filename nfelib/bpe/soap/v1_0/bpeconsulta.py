"""SOAP bindings of the BPeConsulta webservice of the BP-e 1.00.

Written in the layout xsdata generates from a WSDL (see nfelib/mdfe/soap): the
BP-e WSDL is only served to a client certificate, so the namespace, the
bpeConsultaBP operation and the message elements follow the MOC BP-e 1.00b,
Visão Geral, items 3.3 and 3.4. Regenerate this module from the WSDL when it
can be downloaded.
"""

from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe/wsdl/BPeConsulta"


@dataclass
class BpeDadosMsg:
    class Meta:
        name = "bpeDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/bpe/wsdl/BPeConsulta"

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
        namespace = "http://www.portalfiscal.inf.br/bpe/wsdl/BPeConsulta"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class BpeConsultaSoap12BpeConsultaBpInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["BpeConsultaSoap12BpeConsultaBpInput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/bpe/wsdl/BPeConsulta",
            },
        )


@dataclass
class BpeConsultaSoap12BpeConsultaBpOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["BpeConsultaSoap12BpeConsultaBpOutput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/bpe/wsdl/BPeConsulta",
            },
        )
        fault: Optional["BpeConsultaSoap12BpeConsultaBpOutput.Body.Fault"] = field(
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


class BpeConsultaSoap12BpeConsultaBp:
    style = "document"
    location = "https://bpe.svrs.rs.gov.br/ws/bpeConsulta/bpeConsulta.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/bpe/wsdl/BPeConsulta/bpeConsultaBP"
    input = BpeConsultaSoap12BpeConsultaBpInput
    output = BpeConsultaSoap12BpeConsultaBpOutput
