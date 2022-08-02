from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.cons_reci_mdfe_tipos_basico_v3_00 import TconsReciMdfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class ConsReciMdfe(TconsReciMdfe):
    """
    Schema XML de validação do Pedido de Consulta de MDF-e.
    """
    class Meta:
        name = "consReciMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
