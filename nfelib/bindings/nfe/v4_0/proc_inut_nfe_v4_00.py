from dataclasses import dataclass
from nfelib.bindings.nfe.v4_0.leiaute_inut_nfe_v4_00 import TprocInutNfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class ProcInutNfe(TprocInutNfe):
    """
    Pedido de inutilização de númeração de  NF-e processado.
    """
    class Meta:
        name = "ProcInutNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
