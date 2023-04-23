from dataclasses import dataclass, field
from typing import List, Optional
from nfelib.bpe.bindings.v1_0.bpe_tipos_basico_v1_00 import TprotBpe
from nfelib.bpe.bindings.v1_0.evento_bpe_tipos_basico_v1_00 import TprocEvento
from nfelib.bpe.bindings.v1_0.tipos_geral_bpe_v1_00 import (
    Tamb,
    TcodUfIbge,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class TconsSitBpe:
    """
    Tipo Pedido de Consulta da Situação Atual do Bilhete de Passagem Eletrônico.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar xServ: Serviço Solicitado
    :ivar chBPe: Chaves de acesso do BP-e
    :ivar versao:
    """
    class Meta:
        name = "TConsSitBPe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    xServ: str = field(
        init=False,
        default="CONSULTAR",
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    chBPe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "max_length": 44,
            "white_space": "preserve",
            "pattern": r"[0-9]{44}",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"1\.00",
        }
    )


@dataclass
class TretConsSitBpe:
    """
    Tipo Retorno de Pedido de Consulta da Situação Atual do Bilhete de Passagem
    Eletrônico.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar verAplic: Versão do Aplicativo que processou o BP-e
    :ivar cStat: Código do status da mensagem enviada.
    :ivar xMotivo: Descrição literal do status do serviço solicitado.
    :ivar cUF: código da UF de atendimento
    :ivar protBPe:
    :ivar procEventoBPe:
    :ivar versao:
    """
    class Meta:
        name = "TRetConsSitBPe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cStat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    protBPe: List[TprotBpe] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
        }
    )
    procEventoBPe: List[TprocEvento] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"1\.00",
        }
    )
