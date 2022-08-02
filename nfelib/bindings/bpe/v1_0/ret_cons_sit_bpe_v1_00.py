from dataclasses import dataclass
from nfelib.bindings.bpe.v1_0.cons_sit_bpe_tipos_basico_v1_00 import TretConsSitBpe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class RetConsSitBpe(TretConsSitBpe):
    """
    Schema XML de validação do retorno da consulta da situação atual do BP-e.
    """
    class Meta:
        name = "retConsSitBPe"
        namespace = "http://www.portalfiscal.inf.br/bpe"
