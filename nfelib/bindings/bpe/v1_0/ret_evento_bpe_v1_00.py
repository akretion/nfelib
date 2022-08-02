from dataclasses import dataclass
from nfelib.bindings.bpe.v1_0.evento_bpe_tipos_basico_v1_00 import TretEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class RetEventoBpe(TretEvento):
    """
    Schema XML de validação do retorno Pedido de Evento do BP-e.
    """
    class Meta:
        name = "retEventoBPe"
        namespace = "http://www.portalfiscal.inf.br/bpe"
