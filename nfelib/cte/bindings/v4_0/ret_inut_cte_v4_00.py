"""This file was generated by xsdata, v24.2.1, on 2024-02-24 11:16:35

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.cte.bindings.v4_0.inut_cte_tipos_basico_v4_00 import TretInutCte

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class RetInutCte(TretInutCte):
    """
    Schema XML de validação do retorno do Pedido de Inutilização de Numeração do
    CT-e.
    """

    class Meta:
        name = "retInutCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
