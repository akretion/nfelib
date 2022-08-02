from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.cte_tipos_basico_v3_00 import TretCte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class RetCte(TretCte):
    """
    Schema XML de validação do retorno do recibo de envio do CT-e (Modelo 57)
    """
    class Meta:
        name = "retCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
