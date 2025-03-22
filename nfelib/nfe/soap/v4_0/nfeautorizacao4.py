from dataclasses import dataclass, field
from nfelib import CommonMixin
from typing import Dict, List, Optional


@dataclass
class NfeAutorizacao4SoapNfeAutorizacaoLoteZipInput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteZipInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body(CommonMixin):
        nfeDadosMsgZip: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
            },
        )


@dataclass
class NfeDadosMsg(CommonMixin):
    class Meta:
        name = "nfeDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class NfeDadosMsgZip(CommonMixin):
    class Meta:
        name = "nfeDadosMsgZip"
        namespace = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class NfeMonitoria(CommonMixin):
    class Meta:
        name = "nfeMonitoria"
        namespace = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4"

    nomeServidor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    dhServidor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    any_attributes: Dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class NfeResultMsg(CommonMixin):
    class Meta:
        name = "nfeResultMsg"
        nillable = True
        namespace = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )
    Header: Optional[
        "NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput.Header"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body(CommonMixin):
        nfeResultMsg: Optional[NfeResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
                "nillable": True,
            },
        )
        Fault: Optional[
            "NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault(CommonMixin):
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

    @dataclass
    class Header(CommonMixin):
        nfeMonitoria: Optional[NfeMonitoria] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
            },
        )


@dataclass
class NfeAutorizacao4SoapNfeAutorizacaoLoteInput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body(CommonMixin):
        nfeDadosMsg: Optional[NfeDadosMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
            },
        )


@dataclass
class NfeAutorizacao4SoapNfeAutorizacaoLoteOutput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteOutput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    Header: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteOutput.Header"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body(CommonMixin):
        nfeResultMsg: Optional[NfeResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
                "nillable": True,
            },
        )
        Fault: Optional[
            "NfeAutorizacao4SoapNfeAutorizacaoLoteOutput.Body.Fault"
        ] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass
        class Fault(CommonMixin):
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

    @dataclass
    class Header(CommonMixin):
        nfeMonitoria: Optional[NfeMonitoria] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
            },
        )


class NfeAutorizacao4SoapNfeAutorizacaoLote:
    style = "document"
    location = (
        "https://nfe.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4/nfeAutorizacaoLote"
    input = NfeAutorizacao4SoapNfeAutorizacaoLoteInput
    output = NfeAutorizacao4SoapNfeAutorizacaoLoteOutput


class NfeAutorizacao4SoapNfeAutorizacaoLoteZip:
    style = "document"
    location = (
        "https://nfe.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4/nfeAutorizacaoLoteZip"
    input = NfeAutorizacao4SoapNfeAutorizacaoLoteZipInput
    output = NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput
