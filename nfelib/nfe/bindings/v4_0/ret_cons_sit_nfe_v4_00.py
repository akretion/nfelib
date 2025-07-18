"""This file was generated by xsdata, v24.11, on 2025-07-14 02:30:14

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""

from dataclasses import dataclass

from nfelib.nfe.bindings.v4_0.leiaute_cons_sit_nfe_v4_00 import TretConsSitNfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetConsSitNfe(TretConsSitNfe):
    """
    Schema XML de validação do retorno da consulta da situação atual da NF-e.
    """

    class Meta:
        name = "retConsSitNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
