from dataclasses import dataclass
from nfelib.bindings.nfe_cons.v2_0.leiaute_cons_sit_nfe_v2_01 import TretConsSitNfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetConsSitNfe(TretConsSitNfe):
    """
    Schema XML de validação do retorno da consulta da situação atual da NF-e.
    """
    class Meta:
        name = "retConsSitNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
