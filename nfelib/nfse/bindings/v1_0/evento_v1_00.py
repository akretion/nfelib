from dataclasses import dataclass
from nfelib.nfse.bindings.v1_0.tipos_eventos_v1_00 import Tcevento

__NAMESPACE__ = "http://www.sped.fazenda.gov.br/nfse"


@dataclass
class Evento(Tcevento):
    """
    Schema XML do Pedido de Registro de Eventos.
    """
    class Meta:
        name = "evento"
        namespace = "http://www.sped.fazenda.gov.br/nfse"
