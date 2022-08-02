from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.mdfe_tipos_basico_v3_00 import TretMdfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class RetMdfe(TretMdfe):
    """
    Manisfesto Eletrônico de Documentos Fiscais.
    """
    class Meta:
        name = "retMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
