from dataclasses import dataclass
from nfelib.bindings.bpe.v1_0.bpe_tipos_basico_v1_00 import Tbpe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class Bpe(Tbpe):
    """
    Bilhete de Passagem Eletrônico.
    """
    class Meta:
        name = "BPe"
        namespace = "http://www.portalfiscal.inf.br/bpe"
