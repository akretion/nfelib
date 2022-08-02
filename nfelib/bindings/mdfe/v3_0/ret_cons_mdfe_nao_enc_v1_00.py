from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.cons_mdfe_nao_enc_tipos_basico_v3_00 import TretConsMdfeNaoEnc

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class RetConsMdfeNaoEnc(TretConsMdfeNaoEnc):
    """
    Schema XML de validação do retorno da consulta MDF-e não encerrados.
    """
    class Meta:
        name = "retConsMDFeNaoEnc"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
