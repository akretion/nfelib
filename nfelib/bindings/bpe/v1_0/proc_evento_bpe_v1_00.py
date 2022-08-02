from dataclasses import dataclass
from nfelib.bindings.bpe.v1_0.evento_bpe_tipos_basico_v1_00 import TprocEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class ProcEventoBpe(TprocEvento):
    """
    Pedido de Registro de Evento de BP-e processado.
    """
    class Meta:
        name = "procEventoBPe"
        namespace = "http://www.portalfiscal.inf.br/bpe"
