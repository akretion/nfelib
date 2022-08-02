from dataclasses import dataclass
from nfelib.bindings.nfe_evento_mde.v1_0.leiaute_conf_recebto_v1_00 import TenvEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class EnvEvento(TenvEvento):
    """
    Schema XML de validação do lote de envio do evento confirmação de
    recebimento.
    """
    class Meta:
        name = "envEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
