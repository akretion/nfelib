from dataclasses import dataclass
from nfelib.bindings.nfe.v4_0.leiaute_cons_sit_nfe_v4_00 import TconsSitNfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class ConsSitNfe(TconsSitNfe):
    """
    Schema de validação XML dp Pedido de Consulta da Situação Atual da Nota
    Fiscal Eletrônica.
    """
    class Meta:
        name = "consSitNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
