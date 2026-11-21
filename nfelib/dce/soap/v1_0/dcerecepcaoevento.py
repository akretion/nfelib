"""SOAP bindings of the DCeRecepcaoEvento webservice of the DC-e 1.00.

Written in the layout xsdata generates from a WSDL (see nfelib/mdfe/soap): the
DC-e WSDL is only served to a client certificate, so the namespace, the
dceRecepcaoEvento operation and the message elements follow the Manual DC-e,
Visão Geral, items 4.2.2 and 5 (the manual names the operations and
dceDadosMsg, not the namespace nor the answer element; both answer elements are
accepted). Regenerate this module from the WSDL when it can be downloaded.
"""

from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/dce/wsdl/DCeRecepcaoEvento"


@dataclass
class DceDadosMsg:
    class Meta:
        name = "dceDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/dce/wsdl/DCeRecepcaoEvento"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class DceRecepcaoEventoResult:
    class Meta:
        name = "dceRecepcaoEventoResult"
        namespace = "http://www.portalfiscal.inf.br/dce/wsdl/DCeRecepcaoEvento"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class DceResultMsg:
    class Meta:
        name = "dceResultMsg"
        namespace = "http://www.portalfiscal.inf.br/dce/wsdl/DCeRecepcaoEvento"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class DceRecepcaoEventoSoap12DceRecepcaoEventoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["DceRecepcaoEventoSoap12DceRecepcaoEventoInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        dceDadosMsg: Optional[DceDadosMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/dce/wsdl/DCeRecepcaoEvento",
            },
        )


@dataclass
class DceRecepcaoEventoSoap12DceRecepcaoEventoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["DceRecepcaoEventoSoap12DceRecepcaoEventoOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        dceRecepcaoEventoResult: Optional[DceRecepcaoEventoResult] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/dce/wsdl/DCeRecepcaoEvento",
            },
        )
        dceResultMsg: Optional[DceResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/dce/wsdl/DCeRecepcaoEvento",
            },
        )
        fault: Optional["DceRecepcaoEventoSoap12DceRecepcaoEventoOutput.Body.Fault"] = field(
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


class DceRecepcaoEventoSoap12DceRecepcaoEvento:
    style = "document"
    location = "https://dce.fazenda.pr.gov.br/dce/DCeRecepcaoEvento"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/dce/wsdl/DCeRecepcaoEvento/dceRecepcaoEvento"
    input = DceRecepcaoEventoSoap12DceRecepcaoEventoInput
    output = DceRecepcaoEventoSoap12DceRecepcaoEventoOutput
