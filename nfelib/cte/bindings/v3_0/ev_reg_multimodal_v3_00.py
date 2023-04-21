from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class EvRegMultimodalDescEvento(Enum):
    REGISTRO_MULTIMODAL = "Registro Multimodal"


@dataclass
class EvRegMultimodal:
    """
    Schema XML de validação do evento Registro Multimodal 110160.

    :ivar descEvento: Descrição do Evento - “Registro Multimodal”
    :ivar xRegistro: Informação complementar sobre o registro, indicação
        do tipo de documento utilizado e demais situações ocorridas no
        Multimodal (Texto Livre).
    :ivar nDoc: Numero do Documento lançado no CT-e Multimodal
    """
    class Meta:
        name = "evRegMultimodal"
        namespace = "http://www.portalfiscal.inf.br/cte"

    descEvento: Optional[EvRegMultimodalDescEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    xRegistro: Optional[str] = field(
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
    nDoc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 44,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,44}",
        }
    )
