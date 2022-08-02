from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.mdfe_consulta_dfe_tipos_basico_v3_00 import TmdfeConsultaDfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class MdfeConsultaDfe(TmdfeConsultaDfe):
    """
    Schema de validação XML do Pedido de Consulta do MDF-e.
    """
    class Meta:
        name = "mdfeConsultaDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
