from dataclasses import dataclass
from nfelib.bindings.bpe.v1_0.cons_sit_bpe_tipos_basico_v1_00 import TconsSitBpe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class ConsSitBpe(TconsSitBpe):
    """
    Schema de validação XML dp Pedido de Consulta da Situação Atual do BP-e.
    """
    class Meta:
        name = "consSitBPe"
        namespace = "http://www.portalfiscal.inf.br/bpe"
