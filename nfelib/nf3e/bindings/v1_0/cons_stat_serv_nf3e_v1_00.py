"""This file was generated by xsdata, v24.3.1, on 2024-04-05 08:30:20

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass

from nfelib.nf3e.bindings.v1_0.cons_stat_serv_nf3e_tipos_basico_v1_00 import (
    TconsStatServ,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nf3e"


@dataclass
class ConsStatServNf3E(TconsStatServ):
    """
    Schema XML de validação do Pedido de Consulta do Status do Serviço NF-3e.
    """

    class Meta:
        name = "consStatServNF3e"
        namespace = "http://www.portalfiscal.inf.br/nf3e"
