"""This file was generated by xsdata, v24.2.1, on 2024-02-24 11:16:29

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.nfe_ator_interessado.bindings.v1_0.leiaute_evento_ator_interessado_v1_00 import (
    TretEnvEvento,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetEnvEvento(TretEnvEvento):
    """
    Schema XML de Retorno da envio do Evento Ator Interessado na NF-e.
    """

    class Meta:
        name = "retEnvEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"
