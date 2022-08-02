from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.evento_mdfe_tipos_basico_v3_00 import Tevento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class EventoMdfe(Tevento):
    """
    Schema XML de validação do Pedido de Registro de Evento do MDF-e.
    """
    class Meta:
        name = "eventoMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
