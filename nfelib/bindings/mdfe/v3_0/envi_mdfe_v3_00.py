from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.mdfe_tipos_basico_v3_00 import TenviMdfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class EnviMdfe(TenviMdfe):
    """
    Schema XML de validação do Envio de Lote MDF-e para concessão de
    autorização.
    """
    class Meta:
        name = "enviMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
