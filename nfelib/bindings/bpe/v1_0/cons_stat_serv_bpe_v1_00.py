from dataclasses import dataclass
from nfelib.bindings.bpe.v1_0.cons_stat_serv_bpe_tipos_basico_v1_00 import TconsStatServ

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class ConsStatServBpe(TconsStatServ):
    """
    Schema XML de validação do Pedido de Consulta do Status do Serviço BP-e.
    """
    class Meta:
        name = "consStatServBPe"
        namespace = "http://www.portalfiscal.inf.br/bpe"
