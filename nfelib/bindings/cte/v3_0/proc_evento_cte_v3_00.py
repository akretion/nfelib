from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.evento_cte_tipos_basico_v3_00 import TprocEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class ProcEventoCte(TprocEvento):
    """
    Pedido de Registro de Eventos de CT-e processado.
    """
    class Meta:
        name = "procEventoCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
