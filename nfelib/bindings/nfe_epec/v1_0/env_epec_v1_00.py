from dataclasses import dataclass
from nfelib.bindings.nfe_epec.v1_0.leiaute_epec_v1_00 import TenvEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class EnvEvento(TenvEvento):
    """
    Schema XML de validação do lote de envio do Evento Prévio de Emissão em
    Contingência.
    """
    class Meta:
        name = "envEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
