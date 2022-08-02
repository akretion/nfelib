from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.cons_stat_serv_tipos_basico_v3_00 import TconsStatServ

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class ConsStatServMdfe(TconsStatServ):
    """
    Schema XML de validação do Pedido de Consulta do Status do Serviço MDF-e.
    """
    class Meta:
        name = "consStatServMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
