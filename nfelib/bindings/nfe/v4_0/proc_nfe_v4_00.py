from dataclasses import dataclass
from nfelib.bindings.nfe.v4_0.leiaute_nfe_v4_00 import TnfeProc

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class NfeProc(TnfeProc):
    """
    NF-e processada.
    """
    class Meta:
        name = "nfeProc"
        namespace = "http://www.portalfiscal.inf.br/nfe"
