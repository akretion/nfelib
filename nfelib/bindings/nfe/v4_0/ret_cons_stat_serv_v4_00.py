from dataclasses import dataclass
from nfelib.bindings.nfe.v4_0.leiaute_cons_stat_serv_v4_00 import TretConsStatServ

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetConsStatServ(TretConsStatServ):
    """
    Schema XML de validação do Resultado da Consulta do Status do Serviço.
    """
    class Meta:
        name = "retConsStatServ"
        namespace = "http://www.portalfiscal.inf.br/nfe"
