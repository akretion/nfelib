from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.cte_tipos_basico_v3_00 import Tcte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class Cte(Tcte):
    """
    Conhecimento de Transporte Eletrônico.
    """
    class Meta:
        name = "CTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
