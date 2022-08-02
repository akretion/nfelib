from dataclasses import dataclass
from nfelib.bindings.nfe.v4_0.leiaute_nfe_v4_00 import TenviNfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class EnviNfe(TenviNfe):
    """
    Schema XML de validação do Pedido de Concessão de Autorização da Nota
    Fiscal Eletrônica.
    """
    class Meta:
        name = "enviNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
