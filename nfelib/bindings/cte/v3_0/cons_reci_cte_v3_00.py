from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.cons_reci_cte_tipos_basico_v3_00 import TconsReciCte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class ConsReciCte(TconsReciCte):
    """
    Schema XML de validação do Pedido de Consulta de Lote de CT-e.
    """
    class Meta:
        name = "consReciCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
