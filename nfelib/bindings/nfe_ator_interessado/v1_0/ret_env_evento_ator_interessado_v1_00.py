from dataclasses import dataclass
from nfelib.bindings.nfe_ator_interessado.v1_0.leiaute_evento_ator_interessado_v1_00 import TretEnvEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetEnvEvento(TretEnvEvento):
    """
    Schema XML de Retorno da envio do Evento Ator Interessado na NF-e.
    """
    class Meta:
        name = "retEnvEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
