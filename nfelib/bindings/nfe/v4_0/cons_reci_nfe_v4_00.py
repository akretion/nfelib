from dataclasses import dataclass
from nfelib.bindings.nfe.v4_0.leiaute_nfe_v4_00 import TconsReciNfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class ConsReciNfe(TconsReciNfe):
    """
    Schema XML de validação do Pedido de Consulta do Recido do Lote de Notas
    Fiscais Eletrônicas.
    """
    class Meta:
        name = "consReciNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
