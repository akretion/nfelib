from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class MultimodalIndNegociavel(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


@dataclass
class Multimodal:
    """
    Informações do Multimodal.

    :ivar COTM: Número do Certificado do Operador de Transporte
        Multimodal
    :ivar indNegociavel: Indicador Negociável Preencher com: 0 - Não
        Negociável; 1 - Negociável
    :ivar seg: Informações de Seguro do Multimodal
    """
    class Meta:
        name = "multimodal"
        namespace = "http://www.portalfiscal.inf.br/cte"

    COTM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    indNegociavel: Optional[MultimodalIndNegociavel] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    seg: Optional["Multimodal.Seg"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class Seg:
        """
        :ivar infSeg: Informações da seguradora
        :ivar nApol: Número da Apólice Obrigatório pela lei 11.442/07
            (RCTRC)
        :ivar nAver: Número da Averbação Não é obrigatório, pois muitas
            averbações ocorrem aapós a emissão do CT, mensalmente, por
            exemplo.
        """
        infSeg: Optional["Multimodal.Seg.InfSeg"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        nApol: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        nAver: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )

        @dataclass
        class InfSeg:
            """
            :ivar xSeg: Nome da Seguradora
            :ivar CNPJ: Número do CNPJ da seguradora Obrigatório apenas
                se responsável pelo seguro for (2) responsável pela
                contratação do transporte - pessoa jurídica
            """
            xSeg: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 30,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
