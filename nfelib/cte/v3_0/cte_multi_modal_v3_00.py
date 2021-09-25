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

    :ivar cotm: Número do Certificado do Operador de Transporte
        Multimodal
    :ivar ind_negociavel: Indicador Negociável Preencher com: 0 - Não
        Negociável; 1 - Negociável
    :ivar seg: Informações de Seguro do Multimodal
    """
    class Meta:
        name = "multimodal"
        namespace = "http://www.portalfiscal.inf.br/cte"

    cotm: Optional[str] = field(
        default=None,
        metadata={
            "name": "COTM",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    ind_negociavel: Optional[MultimodalIndNegociavel] = field(
        default=None,
        metadata={
            "name": "indNegociavel",
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
        :ivar inf_seg: Informações da seguradora
        :ivar n_apol: Número da Apólice Obrigatório pela lei 11.442/07
            (RCTRC)
        :ivar n_aver: Número da Averbação Não é obrigatório, pois muitas
            averbações ocorrem aapós a emissão do CT, mensalmente, por
            exemplo.
        """
        inf_seg: Optional["Multimodal.Seg.InfSeg"] = field(
            default=None,
            metadata={
                "name": "infSeg",
                "type": "Element",
                "required": True,
            }
        )
        n_apol: Optional[str] = field(
            default=None,
            metadata={
                "name": "nApol",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        n_aver: Optional[str] = field(
            default=None,
            metadata={
                "name": "nAver",
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
            :ivar x_seg: Nome da Seguradora
            :ivar cnpj: Número do CNPJ da seguradora Obrigatório apenas
                se responsável pelo seguro for (2) responsável pela
                contratação do transporte - pessoa jurídica
            """
            x_seg: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xSeg",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 30,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
