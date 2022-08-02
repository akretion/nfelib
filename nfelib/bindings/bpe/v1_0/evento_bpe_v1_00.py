from dataclasses import dataclass
from nfelib.bindings.bpe.v1_0.evento_bpe_tipos_basico_v1_00 import Tevento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class EventoBpe(Tevento):
    """
    Schema XML de validação do Pedido de Registro de Evento do BP-e.
    """
    class Meta:
        name = "eventoBPe"
        namespace = "http://www.portalfiscal.inf.br/bpe"
