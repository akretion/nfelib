from dataclasses import dataclass
from nfelib.bindings.nfe_entrega.v1_0.leiaute_evento_entrega_nfe_v1_00 import TprocEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class ProcEventoNfe(TprocEvento):
    """
    Schema XML de validação do proc do evento de Cancelamento do Comprovante de
    Entrega da NFe.
    """
    class Meta:
        name = "procEventoNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
