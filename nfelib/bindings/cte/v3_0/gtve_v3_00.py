from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.cte_tipos_basico_v3_00 import Tgtve

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class Gtve(Tgtve):
    """
    Guia de Trasnsporte Eletrônica.
    """
    class Meta:
        name = "GTVe"
        namespace = "http://www.portalfiscal.inf.br/cte"
