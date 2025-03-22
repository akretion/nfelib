from dataclasses import dataclass, field
from nfelib import CommonMixin
from typing import List, Optional


@dataclass
class NfeDadosMsg(CommonMixin):
    class Meta:
        name = "nfeDadosMsg"
        namespace = (
            "http://www.portalfiscal.inf.br/nfe/wsdl/NFeConsultaProtocolo4"
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
            "http://www.portalfiscal.inf.br/nfe/wsdl/NFeConsultaProtocolo4"
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
class NfeConsultaProtocolo4SoapNfeConsultaNfInput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeConsultaProtocolo4SoapNfeConsultaNfInput.Body"] = field(
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
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeConsultaProtocolo4",
            },
        )


@dataclass
class NfeConsultaProtocolo4SoapNfeConsultaNfOutput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeConsultaProtocolo4SoapNfeConsultaNfOutput.Body"] = (
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
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeConsultaProtocolo4",
                "nillable": True,
            },
        )
        Fault: Optional[
            "NfeConsultaProtocolo4SoapNfeConsultaNfOutput.Body.Fault"
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


class NfeConsultaProtocolo4SoapNfeConsultaNf:
    style = "document"
    location = "https://nfe.svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeConsultaProtocolo4/nfeConsultaNF"
    input = NfeConsultaProtocolo4SoapNfeConsultaNfInput
    output = NfeConsultaProtocolo4SoapNfeConsultaNfOutput
