from dataclasses import dataclass
from nfelib.bindings.nfe_ator_interessado.v1_0.leiaute_evento_ator_interessado_v1_00 import TenvEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class EnvEvento(TenvEvento):
    """
    Schema XML de validação do lote de envio do evento de Ator Interessado na
    NF-e.
    """
    class Meta:
        name = "envEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
