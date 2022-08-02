from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.mdfe_tipos_basico_v3_00 import Tmdfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class Mdfe(Tmdfe):
    """
    Manisfesto Eletrônico de Documentos Fiscais.
    """
    class Meta:
        name = "MDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
