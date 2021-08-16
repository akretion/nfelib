from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from nfelib.nfe_evento_cancel.v1_0.leiaute_evento_canc_nfe_v1_00 import (
    DetEventoDescEvento1,
    DetEventoVersao1,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class DetEventoDescEvento2(Enum):
    CANCELAMENTO = "Cancelamento"


class DetEventoVersao2(Enum):
    VALUE_1_00 = "1.00"


@dataclass
class DetEvento:
    """
    Schema XML de validação do evento do cancelamento 1101111.

    :ivar desc_evento: Descrição do Evento - “Cancelamento”
    :ivar n_prot: Número do Protocolo de Status da NF-e. 1 posição (1 –
        Secretaria de Fazenda Estadual 2 – Receita Federal); 2 posições
        ano; 10 seqüencial no ano.
    :ivar x_just: Justificativa do cancelamento
    :ivar versao:
    """
    class Meta:
        name = "detEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    desc_evento: Optional[DetEventoDescEvento1] = field(
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
    versao: Optional[DetEventoVersao1] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
        }
    )
