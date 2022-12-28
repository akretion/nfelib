from dataclasses import dataclass, field
from typing import Optional
from nfelib.bindings.nfe_evento_cce.v1_0.leiaute_cce_v1_00 import (
    DetEventoDescEvento,
    DetEventoVersao,
    DetEventoXCondUso,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class DetEvento:
    """
    Schema XML de validação do evento do carta de correção e1101110.

    :ivar descEvento: Descrição do Evento - “Carta de Correção”
    :ivar xCorrecao: Correção a ser considerada
    :ivar xCondUso: Texto Fixo com as condições de uso da Carta de
        Correção
    :ivar versao:
    """
    class Meta:
        name = "detEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    descEvento: Optional[DetEventoDescEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    xCorrecao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 15,
            "max_length": 1000,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xCondUso: Optional[DetEventoXCondUso] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    versao: Optional[DetEventoVersao] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
        }
    )
