"""This file was generated by xsdata, v24.3.1, on 2024-04-05 08:30:20

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass

from nfelib.nf3e.bindings.v1_0.nf3e_tipos_basico_v1_00 import Tnf3E

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nf3e"


@dataclass
class Nf3E(Tnf3E):
    """
    Nota Fiscal Eletrônica de Energia Elétrica.
    """

    class Meta:
        name = "NF3e"
        namespace = "http://www.portalfiscal.inf.br/nf3e"
