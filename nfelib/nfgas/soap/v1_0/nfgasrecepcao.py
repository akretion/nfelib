"""SOAP bindings of the NFGasRecepcao webservice of the NFGas 1.00.

Written in the layout xsdata generates from a WSDL (see nfelib/mdfe/soap): the
NFGas WSDL is only served to a client certificate, so the namespace, the
NFGasRecepcao operation and the message elements follow the MOC NFGas 1.00g,
Visão Geral, item 3. The message goes gzipped and base64 encoded as the text of
nfgasDadosMsg. Regenerate this module from the WSDL when it can be downloaded.
"""

from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/NFGas/wsdl/NFGasRecepcao"


@dataclass
class NfgasDadosMsg:
    class Meta:
        name = "nfgasDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/NFGas/wsdl/NFGasRecepcao"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class NfgasResultMsg:
    class Meta:
        name = "nfgasResultMsg"
        namespace = "http://www.portalfiscal.inf.br/NFGas/wsdl/NFGasRecepcao"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class NfgasRecepcaoSoap12NfgasRecepcaoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfgasRecepcaoSoap12NfgasRecepcaoInput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/NFGas/wsdl/NFGasRecepcao",
            },
        )


@dataclass
class NfgasRecepcaoSoap12NfgasRecepcaoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfgasRecepcaoSoap12NfgasRecepcaoOutput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/NFGas/wsdl/NFGasRecepcao",
            },
        )
        fault: Optional["NfgasRecepcaoSoap12NfgasRecepcaoOutput.Body.Fault"] = field(
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


class NfgasRecepcaoSoap12NfgasRecepcao:
    style = "document"
    location = "https://nfgas.svrs.rs.gov.br/WS/NFGasRecepcao/NFGasRecepcao.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/NFGas/wsdl/NFGasRecepcao/NFGasRecepcao"
    input = NfgasRecepcaoSoap12NfgasRecepcaoInput
    output = NfgasRecepcaoSoap12NfgasRecepcaoOutput
