from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class EvCancCecteDescEvento(Enum):
    CANCELAMENTO_DO_COMPROVANTE_DE_ENTREGA_DO_CT_E = "Cancelamento do Comprovante de Entrega do CT-e"


@dataclass
class EvCancCecte:
    """
    Schema XML de validação do evento cancelamento do comprovante de entrega
    eletrônico do CT-e 110181.

    :ivar desc_evento: Descrição do Evento - “Cancelamento do
        Comprovante de Entrega do CT-e”
    :ivar n_prot: Número do Protocolo de autorização do CT-e
    :ivar n_prot_ce: Número do Protocolo de autorização do evento a ser
        cancelado
    """
    class Meta:
        name = "evCancCECTe"
        namespace = "http://www.portalfiscal.inf.br/cte"

    desc_evento: Optional[EvCancCecteDescEvento] = field(
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
    n_prot_ce: Optional[str] = field(
        default=None,
        metadata={
            "name": "nProtCE",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
