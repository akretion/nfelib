"""This file was generated by xsdata, v24.2.1, on 2025-03-24 16:11:22

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""

from dataclasses import dataclass, field
from nfelib import CommonMixin
from typing import List, Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte/wsdl/CTeRecepcaoGTVeV4"


@dataclass
class CteRecepcaoGtveV4Soap12CteRecepcaoGtveInput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["CteRecepcaoGtveV4Soap12CteRecepcaoGtveInput.Body"] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )

    @dataclass
    class Body(CommonMixin):
        cteDadosMsg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte/wsdl/CTeRecepcaoGTVeV4",
            },
        )


@dataclass
class CteDadosMsg(CommonMixin):
    class Meta:
        name = "cteDadosMsg"
        namespace = "http://www.portalfiscal.inf.br/cte/wsdl/CTeRecepcaoGTVeV4"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class CteRecepcaoGtveResult(CommonMixin):
    class Meta:
        name = "cteRecepcaoGTVeResult"
        namespace = "http://www.portalfiscal.inf.br/cte/wsdl/CTeRecepcaoGTVeV4"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class CteRecepcaoGtveV4Soap12CteRecepcaoGtveOutput(CommonMixin):
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    Body: Optional["CteRecepcaoGtveV4Soap12CteRecepcaoGtveOutput.Body"] = (
        field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
    )

    @dataclass
    class Body(CommonMixin):
        cteRecepcaoGTVeResult: Optional[CteRecepcaoGtveResult] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte/wsdl/CTeRecepcaoGTVeV4",
            },
        )
        Fault: Optional[
            "CteRecepcaoGtveV4Soap12CteRecepcaoGtveOutput.Body.Fault"
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


class CteRecepcaoGtveV4Soap12CteRecepcaoGtve:
    style = "document"
    location = "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoGTVeV4/CTeRecepcaoGTVeV4.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/cte/wsdl/CTeRecepcaoGTVeV4/cteRecepcaoGTVe"
    input = CteRecepcaoGtveV4Soap12CteRecepcaoGtveInput
    output = CteRecepcaoGtveV4Soap12CteRecepcaoGtveOutput
