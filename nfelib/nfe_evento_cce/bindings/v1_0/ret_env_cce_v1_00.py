"""This file was generated by xsdata, v24.2.1, on 2024-02-24 11:16:25

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.nfe_evento_cce.bindings.v1_0.leiaute_cce_v1_00 import TretEnvEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetEnvEvento(TretEnvEvento):
    """
    Schema XML de Retorno da envio do Evento Carta de Correção.
    """

    class Meta:
        name = "retEnvEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
