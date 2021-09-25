from dataclasses import dataclass
from nfelib.nfe_entrega.v1_0.leiaute_evento_entrega_nfe_v1_00 import TretEnvEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetEnvEvento(TretEnvEvento):
    """
    Schema XML de Retorno da envio do evento de Comprovante de Entrega da NFe.
    """
    class Meta:
        name = "retEnvEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
