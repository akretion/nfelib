from dataclasses import dataclass, field
from typing import Optional
from nfelib.bindings.nfe_evento_mde.v1_0.leiaute_conf_recebto_v1_00 import (
    DetEventoDescEvento,
    DetEventoVersao,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


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

    desc_evento: Optional[DetEventoDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
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
