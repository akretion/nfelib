from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.leiaute_dist_mdfe_v3_00 import TdistDfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class DistMdfe(TdistDfe):
    """
    solicitação de distribuição de MDF-e para o Ambiente Autorizador.
    """
    class Meta:
        name = "distMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
