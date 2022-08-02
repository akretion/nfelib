from dataclasses import dataclass
from nfelib.bindings.nfe.v4_0.leiaute_nfe_v4_00 import TretConsReciNfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetConsReciNfe(TretConsReciNfe):
    """
    Schema XML de validação do retorno do Pedido de  Consulta do Recido do Lote
    de Notas Fiscais Eletrônicas.
    """
    class Meta:
        name = "retConsReciNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
