from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.cons_reci_cte_tipos_basico_v3_00 import TretConsReciCte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class RetConsReciCte(TretConsReciCte):
    """
    Schema XML de validação do retorno do Pedido de  Consulta do Lote de CT-e.
    """
    class Meta:
        name = "retConsReciCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
