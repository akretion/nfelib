from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.cte_tipos_basico_v3_00 import TretCteOs

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class RetCteOs(TretCteOs):
    """
    Schema XML de validação do retorno do recibo de envio do CT-e OS (Modelo
    67)
    """
    class Meta:
        name = "retCTeOS"
        namespace = "http://www.portalfiscal.inf.br/cte"
