from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.evento_mdfe_tipos_basico_v3_00 import TprocEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class ProcEventoMdfe(TprocEvento):
    """
    Pedido de Registro de Evento de MDF-e processado.
    """
    class Meta:
        name = "procEventoMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
