from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from nfelib.nfe_evento_mde.v1_0.leiaute_conf_recebto_v1_00 import (
    DetEventoDescEvento1,
    DetEventoVersao1,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class DetEventoDescEvento2(Enum):
    CIENCIA_DA_OPERACAO = "Ciencia da Operacao"


class DetEventoVersao2(Enum):
    VALUE_1_00 = "1.00"


@dataclass
class DetEvento:
    """
    Schema XML de validação do evento de Ciência da Operação.

    :ivar desc_evento: Descrição do Evento: "Ciência da Operação"
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
    versao: Optional[DetEventoVersao1] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
        }
    )
