from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.cons_sit_mdfe_tipos_basico_v3_00 import TretConsSitMdfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class RetConsSitMdfe(TretConsSitMdfe):
    """
    Schema XML de validação do retorno da consulta da situação atual do MDF-e.
    """
    class Meta:
        name = "retConsSitMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
