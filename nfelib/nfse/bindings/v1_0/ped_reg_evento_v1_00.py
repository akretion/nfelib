from dataclasses import dataclass
from nfelib.nfse.bindings.v1_0.tipos_eventos_v1_00 import TcpedRegEvt

__NAMESPACE__ = "http://www.sped.fazenda.gov.br/nfse"


@dataclass
class PedRegEvento(TcpedRegEvt):
    """
    Schema XML do Pedido de Registro de Eventos.
    """
    class Meta:
        name = "pedRegEvento"
        namespace = "http://www.sped.fazenda.gov.br/nfse"
