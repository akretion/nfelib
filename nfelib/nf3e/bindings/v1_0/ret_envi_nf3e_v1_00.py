"""This file was generated by xsdata, v24.3.1, on 2024-04-05 08:30:20

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass

from nfelib.nf3e.bindings.v1_0.nf3e_tipos_basico_v1_00 import TretEnviNf3E

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nf3e"


@dataclass
class RetEnviNf3E(TretEnviNf3E):
    """
    Schema XML de validação do retorno do recibo de envio do lote de NF-3e.
    """

    class Meta:
        name = "retEnviNF3e"
        namespace = "http://www.portalfiscal.inf.br/nf3e"