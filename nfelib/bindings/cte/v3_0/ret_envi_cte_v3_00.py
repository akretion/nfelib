from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.cte_tipos_basico_v3_00 import TretEnviCte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class RetEnviCte(TretEnviCte):
    """
    Schema XML de validação do retorno do recibo de envio do lote de CT-e.
    """
    class Meta:
        name = "retEnviCte"
        namespace = "http://www.portalfiscal.inf.br/cte"
