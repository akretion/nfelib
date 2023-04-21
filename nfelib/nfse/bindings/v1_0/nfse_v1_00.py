from dataclasses import dataclass
from nfelib.nfse.bindings.v1_0.tipos_complexos_v1_00 import Tcnfse

__NAMESPACE__ = "http://www.sped.fazenda.gov.br/nfse"


@dataclass
class Nfse(Tcnfse):
    """Schema XML da Nota Fiscal de Serviços Eletrônica - NFS-e"""
    class Meta:
        name = "NFSe"
        namespace = "http://www.sped.fazenda.gov.br/nfse"
