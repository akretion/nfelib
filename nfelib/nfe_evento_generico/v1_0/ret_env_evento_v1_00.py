from dataclasses import dataclass
from nfelib.nfe_evento_generico.v1_0.leiaute_evento_v1_00 import TretEnvEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetEnvEvento(TretEnvEvento):
    """
    Schema XML de Retorno da envio do Evento.
    """
    class Meta:
        name = "retEnvEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
