from dataclasses import dataclass

from nfelib.cte.bindings.v4_0.cte_tipos_basico_v4_00 import TretCteSimp

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class RetCteSimp(TretCteSimp):
    """
    Schema XML de validação do retorno do recibo de envio do CT-e Simplificado
    (Modelo 57)
    """

    class Meta:
        name = "retCTeSimp"
        namespace = "http://www.portalfiscal.inf.br/cte"
