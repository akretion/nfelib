from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.cte_tipos_basico_v3_00 import TenviCte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class EnviCte(TenviCte):
    """
    Schema XML de validação do Envio de Lote CT-e para concessão de
    autorização.
    """
    class Meta:
        name = "enviCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
