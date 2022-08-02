from dataclasses import dataclass
from nfelib.bindings.nfe_evento_cancel.v1_0.leiaute_evento_canc_nfe_v1_00 import TretEnvEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetEnvEvento(TretEnvEvento):
    """
    Schema XML de Retorno da envio do Evento Cancelamento.
    """
    class Meta:
        name = "retEnvEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
