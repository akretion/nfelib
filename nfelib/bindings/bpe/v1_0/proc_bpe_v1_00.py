from dataclasses import dataclass, field
from typing import Optional
from nfelib.bindings.bpe.v1_0.bpe_tipos_basico_v1_00 import (
    Tbpe,
    TprotBpe,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class BpeProc:
    """
    BP-e processado.

    :ivar BPe:
    :ivar protBPe:
    :ivar versao:
    :ivar ipTransmissor: IP do transmissor do documento fiscal para o
        ambiente autorizador
    :ivar nPortaCon: Porta de origem utilizada na conexão (De 0 a 65535)
    :ivar dhConexao: Data e Hora da Conexão de Origem
    """
    class Meta:
        name = "bpeProc"
        namespace = "http://www.portalfiscal.inf.br/bpe"

    BPe: Optional[Tbpe] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    protBPe: Optional[TprotBpe] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"1\.00",
        }
    )
    ipTransmissor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])",
        }
    )
    nPortaCon: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]{1,5}",
        }
    )
    dhConexao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
