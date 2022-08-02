from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.cons_stat_serv_tipos_basico_v3_00 import TconsStatServ

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class ConsStatServCte(TconsStatServ):
    """
    Schema XML de validação do Pedido de Consulta do Status do Serviço CT-e.
    """
    class Meta:
        name = "consStatServCte"
        namespace = "http://www.portalfiscal.inf.br/cte"
