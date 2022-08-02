from dataclasses import dataclass
from nfelib.bindings.cte.v3_0.cons_stat_serv_tipos_basico_v3_00 import TretConsStatServ

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class RetConsStatServCte(TretConsStatServ):
    """
    Schema XML de validação do Resultado da Consulta do Status do Serviço de
    CT-e.
    """
    class Meta:
        name = "retConsStatServCte"
        namespace = "http://www.portalfiscal.inf.br/cte"
