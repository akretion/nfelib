from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.cons_sit_cte_tipos_basico_v3_00 import TretConsSitCte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class RetConsSitCte(TretConsSitCte):
    """
    Schema XML de validação do retorno da consulta da situação atual do CT-e.
    """
    class Meta:
        name = "retConsSitCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
