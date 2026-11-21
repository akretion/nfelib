"""SOAP bindings of the NFGasRecepcaoEvento webservice of the NFGas 1.00.

Written in the layout xsdata generates from a WSDL (see nfelib/mdfe/soap): the
NFGas WSDL is only served to a client certificate, so the namespace, the
NFGasRecepcaoEvento operation and the message elements follow the MOC NFGas
1.00g, Visão Geral, item 3. Regenerate this module from the WSDL when it can be
downloaded.
"""

from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/NFGas/wsdl/NFGasRecepcaoEvento"


@dataclass
class NfgasDadosMsg:
    class Meta:
        name = "nfgasDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/NFGas/wsdl/NFGasRecepcaoEvento"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class NfgasResultMsg:
    class Meta:
        name = "nfgasResultMsg"
        namespace = "http://www.portalfiscal.inf.br/NFGas/wsdl/NFGasRecepcaoEvento"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class NfgasRecepcaoEventoSoap12NfgasRecepcaoEventoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfgasRecepcaoEventoSoap12NfgasRecepcaoEventoInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        nfgasDadosMsg: Optional[NfgasDadosMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/NFGas/wsdl/NFGasRecepcaoEvento",
            },
        )


@dataclass
class NfgasRecepcaoEventoSoap12NfgasRecepcaoEventoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfgasRecepcaoEventoSoap12NfgasRecepcaoEventoOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        },
    )

    @dataclass
    class Body:
        nfgasResultMsg: Optional[NfgasResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/NFGas/wsdl/NFGasRecepcaoEvento",
            },
        )
        fault: Optional["NfgasRecepcaoEventoSoap12NfgasRecepcaoEventoOutput.Body.Fault"] = field(
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


class NfgasRecepcaoEventoSoap12NfgasRecepcaoEvento:
    style = "document"
    location = "https://nfgas.svrs.rs.gov.br/WS/NFGasRecepcaoEvento/NFGasRecepcaoEvento.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/NFGas/wsdl/NFGasRecepcaoEvento/NFGasRecepcaoEvento"
    input = NfgasRecepcaoEventoSoap12NfgasRecepcaoEventoInput
    output = NfgasRecepcaoEventoSoap12NfgasRecepcaoEventoOutput
