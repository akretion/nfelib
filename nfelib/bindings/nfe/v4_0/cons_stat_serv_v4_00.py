from dataclasses import dataclass
from nfelib.bindings.nfe.v4_0.leiaute_cons_stat_serv_v4_00 import TconsStatServ

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class ConsStatServ(TconsStatServ):
    """
    Schema XML de validação do Pedido de Consulta do Status do Serviço.
    """
    class Meta:
        name = "consStatServ"
        namespace = "http://www.portalfiscal.inf.br/nfe"
