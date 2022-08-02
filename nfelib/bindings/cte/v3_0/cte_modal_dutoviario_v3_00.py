from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class Duto:
    """
    Informações do modal Dutoviário.

    :ivar v_tar: Valor da tarifa
    :ivar d_ini: Data de Início da prestação do serviço
    :ivar d_fim: Data de Fim da prestação do serviço
    """
    class Meta:
        name = "duto"
        namespace = "http://www.portalfiscal.inf.br/cte"

    v_tar: Optional[str] = field(
        default=None,
        metadata={
            "name": "vTar",
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"0\.[1-9]{1}[0-9]{5}|0\.[0-9]{1}[1-9]{1}[0-9]{4}|0\.[0-9]{2}[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}[0-9]{2}|0\.[0-9]{4}[1-9]{1}[0-9]{1}|0\.[0-9]{5}[1-9]{1}|[1-9]{1}[0-9]{0,8}(\.[0-9]{6})?",
        }
    )
    d_ini: Optional[str] = field(
        default=None,
        metadata={
            "name": "dIni",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
        }
    )
    d_fim: Optional[str] = field(
        default=None,
        metadata={
            "name": "dFim",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
        }
    )
