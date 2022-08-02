from dataclasses import dataclass
from nfelib.bindings.nfe_ator_interessado.v1_0.leiaute_evento_ator_interessado_v1_00 import Tevento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class Evento(Tevento):
    """
    Schema XML de validação do evento de Ator Interessado na NF-e.
    """
    class Meta:
        name = "evento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
