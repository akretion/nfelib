"""This file was generated by xsdata, v24.11, on 2025-07-14 05:12:19

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""

from dataclasses import dataclass

from nfelib.cte.bindings.v4_0.evento_cte_tipos_basico_v4_00 import TprocEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class ProcEventoCte(TprocEvento):
    """
    Pedido de Registro de Eventos de CT-e processado.
    """

    class Meta:
        name = "procEventoCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"
