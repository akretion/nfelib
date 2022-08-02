from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bindings.cte.v3_0.tipos_geral_cte_v3_00 import (
    Tamb,
    TcodUfIbge,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class ProcEventoCteVersao(Enum):
    VALUE_1_04 = "1.04"
    VALUE_2_00 = "2.00"
    VALUE_3_00 = "3.00"


class ProtCteVersao(Enum):
    VALUE_1_03 = "1.03"
    VALUE_1_04 = "1.04"
    VALUE_2_00 = "2.00"
    VALUE_3_00 = "3.00"


@dataclass
class TconsSitCte:
    """
    Tipo Pedido de Consulta da Situação Atual do Conhecimento de Transporte
    eletrônico.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar x_serv: Serviço Solicitado
    :ivar ch_cte: Chaves de acesso da CT-e, compostas por: UF do
        emitente, AAMM da emissão da CT-e, CNPJ do emitente, modelo,
        série e número da CT-e e código numérico + DV.
    :ivar versao:
    """
    class Meta:
        name = "TConsSitCTe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    x_serv: str = field(
        init=False,
        default="CONSULTAR",
        metadata={
            "name": "xServ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    ch_cte: Optional[str] = field(
        default=None,
        metadata={
            "name": "chCTe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "pattern": r"3\.00",
        }
    )


@dataclass
class TretConsSitCte:
    """
    Tipo Retorno de Pedido de Consulta da Situação Atual do Conhecimento de
    Transporte eletrônico.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que processou o CT-e
    :ivar c_stat: Código do status da mensagem enviada.
    :ivar x_motivo: Descrição literal do status do serviço solicitado.
    :ivar c_uf: código da UF de atendimento
    :ivar prot_cte:
    :ivar proc_evento_cte:
    :ivar versao:
    """
    class Meta:
        name = "TRetConsSitCTe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    prot_cte: Optional["TretConsSitCte.ProtCte"] = field(
        default=None,
        metadata={
            "name": "protCTe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    proc_evento_cte: List["TretConsSitCte.ProcEventoCte"] = field(
        default_factory=list,
        metadata={
            "name": "procEventoCTe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"3\.00",
        }
    )

    @dataclass
    class ProtCte:
        """
        :ivar any_element: Retornar protCTe da versão correspondente do
            CT-e autorizado
        :ivar versao:
        """
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            }
        )
        versao: Optional[ProtCteVersao] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
            }
        )

    @dataclass
    class ProcEventoCte:
        """
        :ivar any_element: Retornar procEventoCTe da versão
            correspondente do evento CT-e autorizado
        :ivar versao:
        """
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            }
        )
        versao: Optional[ProcEventoCteVersao] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
            }
        )
