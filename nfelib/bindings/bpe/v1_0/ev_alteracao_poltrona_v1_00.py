from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


class EvAlteracaoPoltronaDescEvento(Enum):
    ALTERA_O_POLTRONA = "Alteração Poltrona"
    ALTERACAO_POLTRONA = "Alteracao Poltrona"


@dataclass
class EvAlteracaoPoltrona:
    """
    Schema XML de validação do evento de alteração de poltrona 110116.

    :ivar descEvento: Descrição do Evento - “Alteração de Poltrona”
    :ivar nProt: Número do Protocolo de Status do BP-e.
    :ivar poltrona: Número da Poltrona / assento / cabine
    """
    class Meta:
        name = "evAlteracaoPoltrona"
        namespace = "http://www.portalfiscal.inf.br/bpe"

    descEvento: Optional[EvAlteracaoPoltronaDescEvento] = field(
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
    poltrona: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 3,
            "white_space": "preserve",
            "pattern": r"0|[1-9]{1}[0-9]{0,2}",
        }
    )
