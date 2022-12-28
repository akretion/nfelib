from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class EvCancCteDescEvento(Enum):
    CANCELAMENTO = "Cancelamento"


@dataclass
class EvCancCte:
    """
    Schema XML de validação do evento do cancelamento 110111.

    :ivar descEvento: Descrição do Evento - “Cancelamento”
    :ivar nProt: Número do Protocolo de Status do CT-e. 1 posição tipo
        de autorizador (1 – Secretaria de Fazenda Estadual,  3 - SEFAZ
        Virtual RS, 5 - SEFAZ Virtual SP ); 2 posições ano; 10
        seqüencial no ano.
    :ivar xJust: Justificativa do Cancelamento
    """
    class Meta:
        name = "evCancCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"

    descEvento: Optional[EvCancCteDescEvento] = field(
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
