from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.inut_cte_tipos_basico_v3_00 import TinutCte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class InutCte(TinutCte):
    """
    Schema XML de validação do Pedido de Inutilização de Numeração do
    Conhecimento de Transportes eletrônico.
    """
    class Meta:
        name = "inutCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
