from dataclasses import dataclass
from nfelib.bindings.nfe_evento_mde.v1_0.leiaute_conf_recebto_v1_00 import Tevento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class Evento(Tevento):
    """
    Schema XML de validação do evento Confirmação de recebimento.
    """
    class Meta:
        name = "evento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
