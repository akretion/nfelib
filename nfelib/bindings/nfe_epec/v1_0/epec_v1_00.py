from dataclasses import dataclass
from nfelib.bindings.nfe_epec.v1_0.leiaute_epec_v1_00 import Tevento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class Evento(Tevento):
    """
    Schema XML de validação do Evento Prévio de Emissão em Contingência.
    """
    class Meta:
        name = "evento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
