from dataclasses import dataclass
from nfelib.bindings.nfe_evento_cce.v1_0.leiaute_cce_v1_00 import TprocEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class ProcEventoNfe(TprocEvento):
    """
    Schema XML de validação do proc Carta de Correção da NFe.
    """
    class Meta:
        name = "procEventoNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
