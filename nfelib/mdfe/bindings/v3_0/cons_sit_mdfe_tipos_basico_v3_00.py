from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.mdfe.bindings.v3_0.tipos_geral_mdfe_v3_00 import (
    Tamb,
    TcodUfIbge,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class ProcEventoMdfeVersao(Enum):
    VALUE_1_00 = "1.00"
    VALUE_3_00 = "3.00"


class ProtMdfeVersao(Enum):
    VALUE_1_00 = "1.00"
    VALUE_3_00 = "3.00"


@dataclass
class TconsSitMdfe:
    """
    Tipo Pedido de Consulta da Situação Atual do MDF-e.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar xServ: Serviço Solicitado
    :ivar chMDFe: Chaves de acesso do MDF-e, compostas por: UF do
        emitente, AAMM da emissão do MDF-e, CNPJ do emitente, modelo,
        série, tipo de emissão e número do MDF-e e código numérico + DV.
    :ivar versao:
    """
    class Meta:
        name = "TConsSitMDFe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    xServ: str = field(
        init=False,
        default="CONSULTAR",
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    chMDFe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
class TretConsSitMdfe:
    """
    Tipo Retorno de Pedido de Consulta da Situação Atual do MDF-e.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar verAplic: Versão do Aplicativo que processou o MDF-e
    :ivar cStat: Código do status da mensagem enviada.
    :ivar xMotivo: Descrição literal do status do serviço solicitado.
    :ivar cUF: código da UF de atendimento
    :ivar protMDFe:
    :ivar procEventoMDFe:
    :ivar versao:
    """
    class Meta:
        name = "TRetConsSitMDFe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    protMDFe: Optional["TretConsSitMdfe.ProtMdfe"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    procEventoMDFe: List["TretConsSitMdfe.ProcEventoMdfe"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
    class ProtMdfe:
        """
        :ivar any_element: Retornar protMDFe da versão correspondente do
            MDF-e autorizado
        :ivar versao:
        """
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            }
        )
        versao: Optional[ProtMdfeVersao] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
            }
        )

    @dataclass
    class ProcEventoMdfe:
        """
        :ivar any_element: Retornar procEventoMDFe da versão
            correspondente do evento MDF-e autorizado
        :ivar versao:
        """
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            }
        )
        versao: Optional[ProcEventoMdfeVersao] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
            }
        )
