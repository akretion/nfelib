from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.cons_sit_cte_tipos_basico_v3_00 import TconsSitCte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class ConsSitCte(TconsSitCte):
    """
    Schema de validação XML dp Pedido de Consulta da Situação Atual do CT-e.
    """
    class Meta:
        name = "consSitCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
