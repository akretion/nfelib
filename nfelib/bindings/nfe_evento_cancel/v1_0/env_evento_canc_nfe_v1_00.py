from dataclasses import dataclass
from nfelib.bindings.nfe_evento_cancel.v1_0.leiaute_evento_canc_nfe_v1_00 import TenvEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class EnvEvento(TenvEvento):
    """
    Schema XML de validação do lote de envio do evento cancelamento.
    """
    class Meta:
        name = "envEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
