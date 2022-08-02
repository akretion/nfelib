from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.evento_mdfe_tipos_basico_v3_00 import TretEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class RetEventoMdfe(TretEvento):
    """
    Schema XML de validação do retorno Pedido de Cancelamento do MDF-e.
    """
    class Meta:
        name = "retEventoMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
