"""This file was generated by xsdata, v24.3.1, on 2024-04-05 08:30:20

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass

from nfelib.nf3e.bindings.v1_0.cons_reci_nf3e_tipos_basico_v1_00 import (
    TretConsReciNf3E,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nf3e"


@dataclass
class RetConsReciNf3E(TretConsReciNf3E):
    """
    Schema XML de validação do retorno do Pedido de Consulta da NF-3e.
    """

    class Meta:
        name = "retConsReciNF3e"
        namespace = "http://www.portalfiscal.inf.br/nf3e"
