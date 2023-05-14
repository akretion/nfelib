from dataclasses import dataclass
from nfelib.nfe.bindings.v4_0.leiaute_consulta_cadastro_v2_00 import TconsCad

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class ConsCad(TconsCad):
    """
    Schema XML de validação do retorno da consulta cadastro contribuintes.
    """
    class Meta:
        namespace = "http://www.portalfiscal.inf.br/nfe"
