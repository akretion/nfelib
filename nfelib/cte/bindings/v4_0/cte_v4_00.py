from dataclasses import dataclass
from nfelib.cte.bindings.v4_0.cte_tipos_basico_v4_00 import Tcte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class Cte(Tcte):
    """
    Conhecimento de Transporte Eletrônico.
    """
    class Meta:
        name = "CTe"
        namespace = "http://www.portalfiscal.inf.br/cte"