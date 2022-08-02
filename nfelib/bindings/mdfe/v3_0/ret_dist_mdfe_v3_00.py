from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.leiaute_dist_mdfe_v3_00 import TretDistDfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class RetDistMdfe(TretDistDfe):
    """
    Retorno de pedido de distribuição de MDF-e.
    """
    class Meta:
        name = "retDistMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
