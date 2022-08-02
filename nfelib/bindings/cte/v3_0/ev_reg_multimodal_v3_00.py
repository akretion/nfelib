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

    :ivar desc_evento: Descrição do Evento - “Registro Multimodal”
    :ivar x_registro: Informação complementar sobre o registro,
        indicação do tipo de documento utilizado e demais situações
        ocorridas no Multimodal (Texto Livre).
    :ivar n_doc: Numero do Documento lançado no CT-e Multimodal
    """
    class Meta:
        name = "evRegMultimodal"
        namespace = "http://www.portalfiscal.inf.br/cte"

    desc_evento: Optional[EvRegMultimodalDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    x_registro: Optional[str] = field(
        default=None,
        metadata={
            "name": "xRegistro",
            "type": "Element",
            "required": True,
            "min_length": 15,
            "max_length": 1000,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    n_doc: Optional[str] = field(
        default=None,
        metadata={
            "name": "nDoc",
            "type": "Element",
            "min_length": 1,
            "max_length": 44,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,44}",
        }
    )
