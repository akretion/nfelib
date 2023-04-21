from dataclasses import dataclass
from nfelib.nfse.bindings.v1_0.tipos_complexos_v1_00 import Tcdps

__NAMESPACE__ = "http://www.sped.fazenda.gov.br/nfse"


@dataclass
class Dps(Tcdps):
    """Schema XML da Declaração de Prestação de Serviços - DPS"""
    class Meta:
        name = "DPS"
        namespace = "http://www.sped.fazenda.gov.br/nfse"
