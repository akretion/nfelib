"""SOAP bindings of the NFAgStatusServico webservice of the NFAg 1.00.

Written in the layout xsdata generates from a WSDL (see nfelib/mdfe/soap): the
NFAg WSDL is only served to a client certificate, so the namespace, the
NFAgStatusServicoNF operation and the message elements follow the MOC NFAg
1.00l, Visão Geral, item 3. Regenerate this module from the WSDL when it can be
downloaded.
"""

from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgStatusServico"


@dataclass
class NfagDadosMsg:
    class Meta:
        name = "nfagDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgStatusServico"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class NfagResultMsg:
    class Meta:
        name = "nfagResultMsg"
        namespace = "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgStatusServico"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class NfagStatusServicoSoap12NfagStatusServicoNfInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfagStatusServicoSoap12NfagStatusServicoNfInput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgStatusServico",
            },
        )


@dataclass
class NfagStatusServicoSoap12NfagStatusServicoNfOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfagStatusServicoSoap12NfagStatusServicoNfOutput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgStatusServico",
            },
        )
        fault: Optional["NfagStatusServicoSoap12NfagStatusServicoNfOutput.Body.Fault"] = field(
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


class NfagStatusServicoSoap12NfagStatusServicoNf:
    style = "document"
    location = "https://nfag.svrs.rs.gov.br/WS/NFAgStatusServico/NFAgStatusServico.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgStatusServico/NFAgStatusServicoNF"
    input = NfagStatusServicoSoap12NfagStatusServicoNfInput
    output = NfagStatusServicoSoap12NfagStatusServicoNfOutput
