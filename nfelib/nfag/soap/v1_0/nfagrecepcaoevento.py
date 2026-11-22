"""SOAP bindings of the NFAgRecepcaoEvento webservice of the NFAg 1.00.

Written in the layout xsdata generates from a WSDL (see nfelib/mdfe/soap): the
NFAg WSDL is only served to a client certificate, so the namespace, the
NFAgRecepcaoEvento operation and the message elements follow the MOC NFAg
1.00l, Visão Geral, item 3. Regenerate this module from the WSDL when it can be
downloaded.
"""

from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgRecepcaoEvento"


@dataclass
class NfagDadosMsg:
    class Meta:
        name = "nfagDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgRecepcaoEvento"

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
        namespace = "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgRecepcaoEvento"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class NfagRecepcaoEventoSoap12NfagRecepcaoEventoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfagRecepcaoEventoSoap12NfagRecepcaoEventoInput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgRecepcaoEvento",
            },
        )


@dataclass
class NfagRecepcaoEventoSoap12NfagRecepcaoEventoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfagRecepcaoEventoSoap12NfagRecepcaoEventoOutput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgRecepcaoEvento",
            },
        )
        fault: Optional["NfagRecepcaoEventoSoap12NfagRecepcaoEventoOutput.Body.Fault"] = field(
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


class NfagRecepcaoEventoSoap12NfagRecepcaoEvento:
    style = "document"
    location = "https://nfag.svrs.rs.gov.br/WS/NFAgRecepcaoEvento/NFAgRecepcaoEvento.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/NFAg/wsdl/NFAgRecepcaoEvento/NFAgRecepcaoEvento"
    input = NfagRecepcaoEventoSoap12NfagRecepcaoEventoInput
    output = NfagRecepcaoEventoSoap12NfagRecepcaoEventoOutput
