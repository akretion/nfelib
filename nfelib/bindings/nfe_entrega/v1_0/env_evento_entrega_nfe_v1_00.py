from dataclasses import dataclass
from nfelib.bindings.nfe_entrega.v1_0.leiaute_evento_entrega_nfe_v1_00 import TenvEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class EnvEvento(TenvEvento):
    """
    Schema XML de validação do lote de envio do evento de Comprovante de
    Entrega da NFe.
    """
    class Meta:
        name = "envEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
