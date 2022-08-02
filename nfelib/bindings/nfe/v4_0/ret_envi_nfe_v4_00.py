from dataclasses import dataclass
from nfelib.bindings.nfe.v4_0.leiaute_nfe_v4_00 import TretEnviNfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetEnviNfe(TretEnviNfe):
    """
    Schema XML de validação do retorno do Pedido de Concessão de Autorização da
    Nota Fiscal Eletrônica.
    """
    class Meta:
        name = "retEnviNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
