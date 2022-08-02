from dataclasses import dataclass
from nfelib.bindings.bpe.v1_0.cons_stat_serv_bpe_tipos_basico_v1_00 import TretConsStatServ

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class RetConsStatServBpe(TretConsStatServ):
    """
    Schema XML de validação do Resultado da Consulta do Status do Serviço de
    BP-e.
    """
    class Meta:
        name = "retConsStatServBPe"
        namespace = "http://www.portalfiscal.inf.br/bpe"
