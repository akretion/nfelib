"""SOAP bindings of the DCeStatusServico webservice of the DC-e 1.00.

Written in the layout xsdata generates from a WSDL (see nfelib/mdfe/soap): the
DC-e WSDL is only served to a client certificate, so the namespace, the
dceStatusServico operation and the message elements follow the Manual DC-e,
Visão Geral, items 4.2.2 and 5 (the manual names the operations and
dceDadosMsg, not the namespace nor the answer element; both answer elements are
accepted). Regenerate this module from the WSDL when it can be downloaded.
"""

from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/dce/wsdl/DCeStatusServico"


@dataclass
class DceDadosMsg:
    class Meta:
        name = "dceDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/dce/wsdl/DCeStatusServico"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class DceStatusServicoResult:
    class Meta:
        name = "dceStatusServicoResult"
        namespace = "http://www.portalfiscal.inf.br/dce/wsdl/DCeStatusServico"

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
        namespace = "http://www.portalfiscal.inf.br/dce/wsdl/DCeStatusServico"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class DceStatusServicoSoap12DceStatusServicoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["DceStatusServicoSoap12DceStatusServicoInput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/dce/wsdl/DCeStatusServico",
            },
        )


@dataclass
class DceStatusServicoSoap12DceStatusServicoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["DceStatusServicoSoap12DceStatusServicoOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        dceStatusServicoResult: Optional[DceStatusServicoResult] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/dce/wsdl/DCeStatusServico",
            },
        )
        dceResultMsg: Optional[DceResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/dce/wsdl/DCeStatusServico",
            },
        )
        fault: Optional["DceStatusServicoSoap12DceStatusServicoOutput.Body.Fault"] = field(
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


class DceStatusServicoSoap12DceStatusServico:
    style = "document"
    location = "https://dce.fazenda.pr.gov.br/dce/DCeStatusServico"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/dce/wsdl/DCeStatusServico/dceStatusServico"
    input = DceStatusServicoSoap12DceStatusServicoInput
    output = DceStatusServicoSoap12DceStatusServicoOutput
