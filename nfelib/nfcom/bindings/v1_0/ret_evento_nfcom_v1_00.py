"""This file was generated by xsdata, v24.3.1, on 2024-04-05 08:28:03

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass

from nfelib.nfcom.bindings.v1_0.evento_nfcom_tipos_basico_v1_00 import (
    TretEvento,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfcom"


@dataclass
class RetEventoNfcom(TretEvento):
    """
    Schema XML de validação do retorno Pedido de Evento da NFCom.
    """

    class Meta:
        name = "retEventoNFCom"
        namespace = "http://www.portalfiscal.inf.br/nfcom"
