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

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar xServ: Serviço Solicitado
    :ivar chCTe: Chaves de acesso da CT-e, compostas por: UF do
        emitente, AAMM da emissão da CT-e, CNPJ do emitente, modelo,
        série e número da CT-e e código numérico + DV.
    :ivar versao:
    """
    class Meta:
        name = "TConsSitCTe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    xServ: str = field(
        init=False,
        default="CONSULTAR",
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    chCTe: Optional[str] = field(
        default=None,
        metadata={
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

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar verAplic: Versão do Aplicativo que processou o CT-e
    :ivar cStat: Código do status da mensagem enviada.
    :ivar xMotivo: Descrição literal do status do serviço solicitado.
    :ivar cUF: código da UF de atendimento
    :ivar protCTe:
    :ivar procEventoCTe:
    :ivar versao:
    """
    class Meta:
        name = "TRetConsSitCTe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    protCTe: Optional["TretConsSitCte.ProtCte"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    procEventoCTe: List["TretConsSitCte.ProcEventoCte"] = field(
        default_factory=list,
        metadata={
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
