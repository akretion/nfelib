from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.cons_stat_serv_tipos_basico_v3_00 import TretConsStatServ

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class RetConsStatServMdfe(TretConsStatServ):
    """
    Schema XML de validação do Resultado da Consulta do Status do Serviço de
    MDF-e.
    """
    class Meta:
        name = "retConsStatServMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
