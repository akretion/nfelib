from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.cons_sit_mdfe_tipos_basico_v3_00 import TconsSitMdfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class ConsSitMdfe(TconsSitMdfe):
    """
    Schema de validação XML dp Pedido de Consulta da Situação Atual do MDF-e.
    """
    class Meta:
        name = "consSitMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
