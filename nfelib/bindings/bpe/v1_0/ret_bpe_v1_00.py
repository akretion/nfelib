from dataclasses import dataclass
from nfelib.bindings.bpe.v1_0.bpe_tipos_basico_v1_00 import TretBpe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class RetBpe(TretBpe):
    """
    Schema XML de validação do retorno do BP-e.
    """
    class Meta:
        name = "retBPe"
        namespace = "http://www.portalfiscal.inf.br/bpe"
