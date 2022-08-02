from dataclasses import dataclass
from nfelib.bindings.bpe.v1_0.bpe_tipos_basico_v1_00 import TbpeTm

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class BpeTm(TbpeTm):
    """
    Bilhete de Passagem Eletrônico Transporte Metropolitano.
    """
    class Meta:
        name = "BPeTM"
        namespace = "http://www.portalfiscal.inf.br/bpe"
