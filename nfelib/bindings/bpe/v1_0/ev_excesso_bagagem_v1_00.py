from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


class EvExcessoBagagemDescEvento(Enum):
    EXCESSO_BAGAGEM = "Excesso Bagagem"


@dataclass
class EvExcessoBagagem:
    """
    Schema XML de validação do evento de excesso de bagagem 110117.

    :ivar descEvento: Descrição do Evento - “Excesso Bagagem”
    :ivar nProt: Número do Protocolo de Status do BP-e.
    :ivar qBagagem: Quantidade de volumes de bagagem carregados
    :ivar vTotBag: Valor total do serviço Pode conter zeros quando o
        BP-e for de complemento de ICMS
    """
    class Meta:
        name = "evExcessoBagagem"
        namespace = "http://www.portalfiscal.inf.br/bpe"

    descEvento: Optional[EvExcessoBagagemDescEvento] = field(
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
    qBagagem: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
        }
    )
    vTotBag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
