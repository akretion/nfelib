from dataclasses import dataclass, field
from typing import Optional
from nfelib.nfe_evento_mde.bindings.v1_0.leiaute_conf_recebto_v1_00 import (
    DetEventoDescEvento,
    DetEventoVersao,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class DetEvento:
    """
    Schema XML de validação do evento de Recusa de Recebimento (Operação não
    Realizada)

    :ivar descEvento: Descrição do Evento:"Operação não Realizada"
    :ivar xJust: Justificativa de recusa do recebimento da mercadoria
    :ivar versao:
    """
    class Meta:
        name = "detEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    descEvento: Optional[DetEventoDescEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
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
    versao: Optional[DetEventoVersao] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
        }
    )
