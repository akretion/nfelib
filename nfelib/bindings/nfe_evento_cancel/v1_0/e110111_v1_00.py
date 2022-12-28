from dataclasses import dataclass, field
from typing import Optional
from nfelib.bindings.nfe_evento_cancel.v1_0.leiaute_evento_canc_nfe_v1_00 import (
    DetEventoDescEvento,
    DetEventoVersao,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class DetEvento:
    """
    Schema XML de validação do evento do cancelamento 1101111.

    :ivar descEvento: Descrição do Evento - “Cancelamento”
    :ivar nProt: Número do Protocolo de Status da NF-e. 1 posição (1 –
        Secretaria de Fazenda Estadual 2 – Receita Federal); 2 posições
        ano; 10 seqüencial no ano.
    :ivar xJust: Justificativa do cancelamento
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
    nProt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
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
