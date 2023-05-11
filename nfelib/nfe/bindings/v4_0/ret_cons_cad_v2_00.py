from dataclasses import dataclass
from nfelib.nfe.bindings.v4_0.leiaute_consulta_cadastro_v2_00 import TretConsCad

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetConsCad(TretConsCad):
    """
    Schema XML de validação do retorno da consulta cadastro contribuintes.
    """
    class Meta:
        name = "retConsCad"
        namespace = "http://www.portalfiscal.inf.br/nfe"
