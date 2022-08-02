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

    :ivar desc_evento: Descrição do Evento - “Carta de Correção”
    :ivar x_correcao: Correção a ser considerada
    :ivar x_cond_uso: Texto Fixo com as condições de uso da Carta de
        Correção
    :ivar versao:
    """
    class Meta:
        name = "detEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    desc_evento: Optional[DetEventoDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    x_correcao: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCorrecao",
            "type": "Element",
            "required": True,
            "min_length": 15,
            "max_length": 1000,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_cond_uso: Optional[DetEventoXCondUso] = field(
        default=None,
        metadata={
            "name": "xCondUso",
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
