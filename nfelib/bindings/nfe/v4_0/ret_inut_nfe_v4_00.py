from dataclasses import dataclass
from nfelib.bindings.nfe.v4_0.leiaute_inut_nfe_v4_00 import TretInutNfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetInutNfe(TretInutNfe):
    """
    Schema XML de validação do retorno do Pedido de Inutilização de Numeração
    da Nota Fiscal Eletrônica.
    """
    class Meta:
        name = "retInutNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
