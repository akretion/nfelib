from dataclasses import dataclass
from nfelib.bindings.nfe_ator_interessado.v1_0.leiaute_evento_ator_interessado_v1_00 import TprocEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class ProcEventoNfe(TprocEvento):
    """
    Schema XML de validação do proc evento Ator Interessado.
    """
    class Meta:
        name = "procEventoNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
