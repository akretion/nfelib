"""SOAP bindings of the DCeAutorizacao webservice of the DC-e 1.00.

Written in the layout xsdata generates from a WSDL (see nfelib/mdfe/soap): the
DC-e WSDL is only served to a client certificate, so the namespace, the
dceAutorizacao operation and the message elements follow the Manual DC-e, Visão
Geral, items 4.2.2 and 5 (the manual names the operations and dceDadosMsg, not
the namespace nor the answer element; both answer elements are accepted).
Regenerate this module from the WSDL when it can be downloaded.
"""

from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/dce/wsdl/DCeAutorizacao"


@dataclass
class DceDadosMsg:
    class Meta:
        name = "dceDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/dce/wsdl/DCeAutorizacao"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class DceAutorizacaoResult:
    class Meta:
        name = "dceAutorizacaoResult"
        namespace = "http://www.portalfiscal.inf.br/dce/wsdl/DCeAutorizacao"

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
        namespace = "http://www.portalfiscal.inf.br/dce/wsdl/DCeAutorizacao"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class DceAutorizacaoSoap12DceAutorizacaoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["DceAutorizacaoSoap12DceAutorizacaoInput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/dce/wsdl/DCeAutorizacao",
            },
        )


@dataclass
class DceAutorizacaoSoap12DceAutorizacaoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["DceAutorizacaoSoap12DceAutorizacaoOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        dceAutorizacaoResult: Optional[DceAutorizacaoResult] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/dce/wsdl/DCeAutorizacao",
            },
        )
        dceResultMsg: Optional[DceResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/dce/wsdl/DCeAutorizacao",
            },
        )
        fault: Optional["DceAutorizacaoSoap12DceAutorizacaoOutput.Body.Fault"] = field(
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


class DceAutorizacaoSoap12DceAutorizacao:
    style = "document"
    location = "https://dce.fazenda.pr.gov.br/dce/DCeAutorizacao"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/dce/wsdl/DCeAutorizacao/dceAutorizacao"
    input = DceAutorizacaoSoap12DceAutorizacaoInput
    output = DceAutorizacaoSoap12DceAutorizacaoOutput
