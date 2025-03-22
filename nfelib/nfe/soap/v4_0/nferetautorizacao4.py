from dataclasses import dataclass, field
from nfelib import CommonMixin
from typing import List, Optional


@dataclass
class NfeDadosMsg(CommonMixin):
    class Meta:
        name = "nfeDadosMsg"
        namespace = (
            "http://www.portalfiscal.inf.br/nfe/wsdl/NFeRetAutorizacao4"
        )

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class NfeResultMsg(CommonMixin):
    class Meta:
        name = "nfeResultMsg"
        nillable = True
        namespace = (
            "http://www.portalfiscal.inf.br/nfe/wsdl/NFeRetAutorizacao4"
        )

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteInput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body(CommonMixin):
        nfeDadosMsg: Optional[NfeDadosMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeRetAutorizacao4",
            },
        )


@dataclass
class NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteOutput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional[
        "NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteOutput.Body"
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
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeRetAutorizacao4",
                "nillable": True,
            },
        )
        Fault: Optional[
            "NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteOutput.Body.Fault"
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


class NfeRetAutorizacao4SoapNfeRetAutorizacaoLote:
    style = "document"
    location = "https://nfe.svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeRetAutorizacao4/nfeRetAutorizacaoLote"
    input = NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteInput
    output = NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteOutput
