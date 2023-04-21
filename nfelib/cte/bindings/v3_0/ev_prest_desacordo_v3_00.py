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

    :ivar descEvento: Descrição do Evento - “Prestação do Serviço em
        Desacordo”
    :ivar indDesacordoOper: Indicador de operação em desacordo
    :ivar xObs: Observações do tomador
    """
    class Meta:
        name = "evPrestDesacordo"
        namespace = "http://www.portalfiscal.inf.br/cte"

    descEvento: Optional[EvPrestDesacordoDescEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    indDesacordoOper: Optional[EvPrestDesacordoIndDesacordoOper] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    xObs: Optional[str] = field(
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
