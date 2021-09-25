from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


class EvNaoEmbBpeDescEvento(Enum):
    N_O_EMBARQUE = "Não Embarque"
    NAO_EMBARQUE = "Nao Embarque"


@dataclass
class EvNaoEmbBpe:
    """
    Schema XML de validação do evento do não embarque 110115.

    :ivar desc_evento: Descrição do Evento - “Não Embarque”
    :ivar n_prot: Número do Protocolo de Status do BP-e.
    :ivar x_just: Justificativa do Não Embarque
    """
    class Meta:
        name = "evNaoEmbBPe"
        namespace = "http://www.portalfiscal.inf.br/bpe"

    desc_evento: Optional[EvNaoEmbBpeDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    n_prot: Optional[str] = field(
        default=None,
        metadata={
            "name": "nProt",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    x_just: Optional[str] = field(
        default=None,
        metadata={
            "name": "xJust",
            "type": "Element",
            "required": True,
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
