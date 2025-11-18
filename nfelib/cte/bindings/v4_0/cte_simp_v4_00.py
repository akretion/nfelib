from dataclasses import dataclass

from nfelib.cte.bindings.v4_0.cte_tipos_basico_v4_00 import TcteSimp

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class CteSimp(TcteSimp):
    """
    Conhecimento de Transporte Eletrônico Simplificado.
    """

    class Meta:
        name = "CTeSimp"
        namespace = "http://www.portalfiscal.inf.br/cte"
