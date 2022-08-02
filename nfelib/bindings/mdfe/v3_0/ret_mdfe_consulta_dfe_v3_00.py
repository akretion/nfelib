from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.mdfe_consulta_dfe_tipos_basico_v3_00 import TretMdfeConsultaDfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class RetMdfeConsultaDfe(TretMdfeConsultaDfe):
    """
    Schema XML de validação do retorno da consulta do MDF-e.
    """
    class Meta:
        name = "retMDFeConsultaDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
