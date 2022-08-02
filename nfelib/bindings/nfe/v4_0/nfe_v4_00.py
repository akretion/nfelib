from dataclasses import dataclass
from nfelib.bindings.nfe.v4_0.leiaute_nfe_v4_00 import Tnfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class Nfe(Tnfe):
    """
    Nota Fiscal Eletrônica.
    """
    class Meta:
        name = "NFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
