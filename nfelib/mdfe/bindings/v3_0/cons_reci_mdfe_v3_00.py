"""This file was generated by xsdata, v24.11, on 2025-07-14 04:38:46

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""

from dataclasses import dataclass

from nfelib.mdfe.bindings.v3_0.cons_reci_mdfe_tipos_basico_v3_00 import (
    TconsReciMdfe,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class ConsReciMdfe(TconsReciMdfe):
    """
    Schema XML de validação do Pedido de Consulta de MDF-e.
    """

    class Meta:
        name = "consReciMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
