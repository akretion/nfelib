from dataclasses import dataclass
from nfelib.cte.bindings.v4_0.cte_tipos_basico_v4_00 import TcteOs

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class CteOs(TcteOs):
    """
    Conhecimento de Transporte Eletrônico Outros Serviços.
    """
    class Meta:
        name = "CTeOS"
        namespace = "http://www.portalfiscal.inf.br/cte"