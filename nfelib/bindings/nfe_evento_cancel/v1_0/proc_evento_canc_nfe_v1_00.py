from dataclasses import dataclass
from nfelib.bindings.nfe_evento_cancel.v1_0.leiaute_evento_canc_nfe_v1_00 import TprocEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class ProcEventoNfe(TprocEvento):
    """
    Schema XML de validação do proc Cancelamento.
    """
    class Meta:
        name = "procEventoNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
