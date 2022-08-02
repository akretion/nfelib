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

    :ivar desc_evento: Descrição do Evento - “Excesso Bagagem”
    :ivar n_prot: Número do Protocolo de Status do BP-e.
    :ivar q_bagagem: Quantidade de volumes de bagagem carregados
    :ivar v_tot_bag: Valor total do serviço Pode conter zeros quando o
        BP-e for de complemento de ICMS
    """
    class Meta:
        name = "evExcessoBagagem"
        namespace = "http://www.portalfiscal.inf.br/bpe"

    desc_evento: Optional[EvExcessoBagagemDescEvento] = field(
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
    q_bagagem: Optional[str] = field(
        default=None,
        metadata={
            "name": "qBagagem",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
        }
    )
    v_tot_bag: Optional[str] = field(
        default=None,
        metadata={
            "name": "vTotBag",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
