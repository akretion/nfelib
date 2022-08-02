from dataclasses import dataclass
from nfelib.bindings.nfe_epec.v1_0.leiaute_epec_v1_00 import TretEnvEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetEnvEvento(TretEnvEvento):
    """
    Schema XML de Retorno da envio do Evento Emissão Prévia em Contingência.
    """
    class Meta:
        name = "retEnvEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
