from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.evento_cte_tipos_basico_v3_00 import TretEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class RetEventoCte(TretEvento):
    """
    Schema XML de validação do retorno Pedido de Evento do CT-e.
    """
    class Meta:
        name = "retEventoCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
