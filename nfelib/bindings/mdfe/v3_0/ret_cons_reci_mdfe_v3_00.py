from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.cons_reci_mdfe_tipos_basico_v3_00 import TretConsReciMdfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class RetConsReciMdfe(TretConsReciMdfe):
    """
    Schema XML de validação do retorno do Pedido de Consulta do MDF-e.
    """
    class Meta:
        name = "retConsReciMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
