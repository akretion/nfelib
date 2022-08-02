from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class EvPrestDesacordoDescEvento(Enum):
    PRESTA_O_DO_SERVI_O_EM_DESACORDO = "Prestação do Serviço em Desacordo"
    PRESTACAO_DO_SERVICO_EM_DESACORDO = "Prestacao do Servico em Desacordo"


class EvPrestDesacordoIndDesacordoOper(Enum):
    VALUE_1 = "1"


@dataclass
class EvPrestDesacordo:
    """
    Schema XML de validação do evento Prestação do Serviço em Desacordo 610110.

    :ivar desc_evento: Descrição do Evento - “Prestação do Serviço em
        Desacordo”
    :ivar ind_desacordo_oper: Indicador de operação em desacordo
    :ivar x_obs: Observações do tomador
    """
    class Meta:
        name = "evPrestDesacordo"
        namespace = "http://www.portalfiscal.inf.br/cte"

    desc_evento: Optional[EvPrestDesacordoDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    ind_desacordo_oper: Optional[EvPrestDesacordoIndDesacordoOper] = field(
        default=None,
        metadata={
            "name": "indDesacordoOper",
            "type": "Element",
            "required": True,
        }
    )
    x_obs: Optional[str] = field(
        default=None,
        metadata={
            "name": "xObs",
            "type": "Element",
            "required": True,
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
