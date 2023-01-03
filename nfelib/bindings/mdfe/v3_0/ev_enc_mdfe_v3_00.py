from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from nfelib.bindings.mdfe.v3_0.tipos_geral_mdfe_v3_00 import TcodUfIbgeEx

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class EvEncMdfeDescEvento(Enum):
    ENCERRAMENTO = "Encerramento"


@dataclass
class EvEncMdfe:
    """
    Schema XML de validação do evento do encerramento 110112.

    :ivar descEvento: Descrição do Evento - “Encerramento”
    :ivar nProt: Número do Protocolo de Status do MDF-e. 1 posição tipo
        de autorizador (9 - SEFAZ Nacional ); 2 posições ano; 10
        seqüencial no ano.
    :ivar dtEnc: Data que o Manifesto foi encerrado
    :ivar cUF: UF de encerramento do Manifesto
    :ivar cMun: Código do Município de Encerramento do manifesto
    """
    class Meta:
        name = "evEncMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    descEvento: Optional[EvEncMdfeDescEvento] = field(
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
    dtEnc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
        }
    )
    cUF: Optional[TcodUfIbgeEx] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
