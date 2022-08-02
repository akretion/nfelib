from dataclasses import dataclass
from nfelib.bindings.nfe.v4_0.leiaute_inut_nfe_v4_00 import TinutNfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class InutNfe(TinutNfe):
    """
    Schema XML de validação do Pedido de Inutilização de Numeração da Nota
    Fiscal Eletrônica.
    """
    class Meta:
        name = "inutNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
