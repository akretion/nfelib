from dataclasses import dataclass, field
from nfelib import CommonMixin
from typing import List, Optional


@dataclass
class NfeDistDfeInteresse(CommonMixin):
    class Meta:
        name = "nfeDistDFeInteresse"
        namespace = (
            "http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe"
        )

    nfeDadosMsg: Optional["NfeDistDfeInteresse.NfeDadosMsg"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class NfeDadosMsg(CommonMixin):
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class NfeDistDfeInteresseResponse(CommonMixin):
    class Meta:
        name = "nfeDistDFeInteresseResponse"
        namespace = (
            "http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe"
        )

    nfeDistDFeInteresseResult: Optional[
        "NfeDistDfeInteresseResponse.NfeDistDfeInteresseResult"
    ] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class NfeDistDfeInteresseResult(CommonMixin):
        content: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "mixed": True,
            },
        )


@dataclass
class NfeDistribuicaoDfeSoapNfeDistDfeInteresseInput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeDistribuicaoDfeSoapNfeDistDfeInteresseInput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body(CommonMixin):
        nfeDistDFeInteresse: Optional[NfeDistDfeInteresse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe",
            },
        )


@dataclass
class NfeDistribuicaoDfeSoapNfeDistDfeInteresseOutput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["NfeDistribuicaoDfeSoapNfeDistDfeInteresseOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body(CommonMixin):
        nfeDistDFeInteresseResponse: Optional[NfeDistDfeInteresseResponse] = (
            field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe",
                },
            )
        )
        Fault: Optional[
            "NfeDistribuicaoDfeSoapNfeDistDfeInteresseOutput.Body.Fault"
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


class NfeDistribuicaoDfeSoapNfeDistDfeInteresse:
    style = "document"
    location = "https://www1.nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe/nfeDistDFeInteresse"
    input = NfeDistribuicaoDfeSoapNfeDistDfeInteresseInput
    output = NfeDistribuicaoDfeSoapNfeDistDfeInteresseOutput
