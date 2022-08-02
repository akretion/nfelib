from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.cte_tipos_basico_v3_00 import TretGtve

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class RetGtve(TretGtve):
    """
    Schema XML de validação do retorno do recibo de envio da GTV-e (Modelo 64)
    """
    class Meta:
        name = "retGTVe"
        namespace = "http://www.portalfiscal.inf.br/cte"
