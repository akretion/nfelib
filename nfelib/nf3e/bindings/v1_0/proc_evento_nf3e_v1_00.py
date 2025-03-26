"""This file was generated by xsdata, v24.3.1, on 2024-04-05 08:30:20

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass

from nfelib.nf3e.bindings.v1_0.evento_nf3e_tipos_basico_v1_00 import (
    TprocEvento,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nf3e"


@dataclass
class ProcEventoNf3E(TprocEvento):
    """
    Pedido de Registro de Evento de NF-3e processado.
    """

    class Meta:
        name = "procEventoNF3e"
        namespace = "http://www.portalfiscal.inf.br/nf3e"
