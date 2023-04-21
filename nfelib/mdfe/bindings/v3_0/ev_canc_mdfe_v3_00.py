from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class EvCancMdfeDescEvento(Enum):
    CANCELAMENTO = "Cancelamento"


@dataclass
class EvCancMdfe:
    """
    Schema XML de validação do evento do cancelamento 110111.

    :ivar descEvento: Descrição do Evento - “Cancelamento”
    :ivar nProt: Número do Protocolo de Status do MDF-e. 1 posição tipo
        de autorizador (9 -SEFAZ Nacional ); 2 posições ano; 10
        seqüencial no ano.
    :ivar xJust: Justificativa do Cancelamento
    """
    class Meta:
        name = "evCancMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    descEvento: Optional[EvCancMdfeDescEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    nProt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    xJust: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
