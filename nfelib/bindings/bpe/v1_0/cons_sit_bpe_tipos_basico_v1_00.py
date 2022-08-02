from dataclasses import dataclass, field
from typing import List, Optional
from nfelib.bindings.bpe.v1_0.bpe_tipos_basico_v1_00 import TprotBpe
from nfelib.bindings.bpe.v1_0.evento_bpe_tipos_basico_v1_00 import TprocEvento
from nfelib.bindings.bpe.v1_0.tipos_geral_bpe_v1_00 import (
    Tamb,
    TcodUfIbge,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


@dataclass
class TconsSitBpe:
    """
    Tipo Pedido de Consulta da Situação Atual do Bilhete de Passagem
    Eletrônico.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar x_serv: Serviço Solicitado
    :ivar ch_bpe: Chaves de acesso do BP-e
    :ivar versao:
    """
    class Meta:
        name = "TConsSitBPe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    x_serv: str = field(
        init=False,
        default="CONSULTAR",
        metadata={
            "name": "xServ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    ch_bpe: Optional[str] = field(
        default=None,
        metadata={
            "name": "chBPe",
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

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que processou o BP-e
    :ivar c_stat: Código do status da mensagem enviada.
    :ivar x_motivo: Descrição literal do status do serviço solicitado.
    :ivar c_uf: código da UF de atendimento
    :ivar prot_bpe:
    :ivar proc_evento_bpe:
    :ivar versao:
    """
    class Meta:
        name = "TRetConsSitBPe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "cStat",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    x_motivo: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMotivo",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_uf: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    prot_bpe: List[TprotBpe] = field(
        default_factory=list,
        metadata={
            "name": "protBPe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
        }
    )
    proc_evento_bpe: List[TprocEvento] = field(
        default_factory=list,
        metadata={
            "name": "procEventoBPe",
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
