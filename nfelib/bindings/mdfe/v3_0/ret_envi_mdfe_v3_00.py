from dataclasses import dataclass
from nfelib.bindings.mdfe.v3_0.mdfe_tipos_basico_v3_00 import TretEnviMdfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class RetEnviMdfe(TretEnviMdfe):
    """
    Schema XML de validação do retorno do recibo de envio do lote de MDF-e.
    """
    class Meta:
        name = "retEnviMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
