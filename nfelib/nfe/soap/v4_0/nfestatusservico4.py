from dataclasses import dataclass, field
from nfelib import CommonMixin
from typing import List, Optional


@dataclass
class NfeDadosMsg(CommonMixin):
    class Meta:
        name = "nfeDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4"

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
        namespace = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class NfeStatusServico4SoapNfeStatusServicoNfInput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeStatusServico4SoapNfeStatusServicoNfInput.Body"] = (
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
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4",
            },
        )


@dataclass
class NfeStatusServico4SoapNfeStatusServicoNfOutput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeStatusServico4SoapNfeStatusServicoNfOutput.Body"] = (
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
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4",
                "nillable": True,
            },
        )
        Fault: Optional[
            "NfeStatusServico4SoapNfeStatusServicoNfOutput.Body.Fault"
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


class NfeStatusServico4SoapNfeStatusServicoNf:
    style = "document"
    location = (
        "https://nfe.svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx"
    )
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4/nfeStatusServicoNF"
    input = NfeStatusServico4SoapNfeStatusServicoNfInput
    output = NfeStatusServico4SoapNfeStatusServicoNfOutput
