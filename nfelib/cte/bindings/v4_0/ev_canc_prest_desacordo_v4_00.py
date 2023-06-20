from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class EvCancPrestDesacordoDescEvento(Enum):
    CANCELAMENTO_PRESTA_O_DO_SERVI_O_EM_DESACORDO = "Cancelamento Prestação do Serviço em Desacordo"
    CANCELAMENTO_PRESTACAO_DO_SERVICO_EM_DESACORDO = "Cancelamento Prestacao do Servico em Desacordo"


@dataclass
class EvCancPrestDesacordo:
    """
    Schema XML de validação do evento Cancelamento Prestação do Serviço em
    Desacordo 610111.

    :ivar descEvento: Descrição do Evento - “Cancelamento Prestação do
        Serviço em Desacordo”
    :ivar nProtEvPrestDes: Protocolo do evento que será cancelado
        Informar o número do protocolo de autorização do evento de
        prestação de serviço em desacordo que será cancelado
    """
    class Meta:
        name = "evCancPrestDesacordo"
        namespace = "http://www.portalfiscal.inf.br/cte"

    descEvento: Optional[EvCancPrestDesacordoDescEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    nProtEvPrestDes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )