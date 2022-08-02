from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.inut_cte_tipos_basico_v3_00 import TretInutCte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class RetInutCte(TretInutCte):
    """
    Schema XML de validação do retorno do Pedido de Inutilização de Numeração
    do CT-e.
    """
    class Meta:
        name = "retInutCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
