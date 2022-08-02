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

    :ivar desc_evento: Descrição do Evento - “Encerramento”
    :ivar n_prot: Número do Protocolo de Status do MDF-e. 1 posição tipo
        de autorizador (9 - SEFAZ Nacional ); 2 posições ano; 10
        seqüencial no ano.
    :ivar dt_enc: Data que o Manifesto foi encerrado
    :ivar c_uf: UF de encerramento do Manifesto
    :ivar c_mun: Código do Município de Encerramento do manifesto
    """
    class Meta:
        name = "evEncMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    desc_evento: Optional[EvEncMdfeDescEvento] = field(
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
    dt_enc: Optional[str] = field(
        default=None,
        metadata={
            "name": "dtEnc",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
        }
    )
    c_uf: Optional[TcodUfIbgeEx] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "required": True,
        }
    )
    c_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMun",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
