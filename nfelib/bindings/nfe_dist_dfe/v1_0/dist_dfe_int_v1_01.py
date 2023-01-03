from dataclasses import dataclass, field
from typing import Optional
from nfelib.bindings.nfe_dist_dfe.v1_0.tipos_dist_dfe_v1_01 import (
    Tamb,
    TcodUfIbge,
    TverDistDfe,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class DistDfeInt:
    """
    Schema de pedido de distribuição de DF-e de interesse.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar cUFAutor: Código da UF do Autor
    :ivar CNPJ: CNPJ do interessado no DF-e
    :ivar CPF: CPF do interessado no DF-e
    :ivar distNSU: Grupo para distribuir DF-e de interesse
    :ivar consNSU: Grupo para consultar um DF-e a partir de um NSU
        específico
    :ivar consChNFe: Grupo para consultar uma NF-e a partir da chave de
        acesso
    :ivar versao:
    """
    class Meta:
        name = "distDFeInt"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    cUFAutor: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    CPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    distNSU: Optional["DistDfeInt.DistNsu"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    consNSU: Optional["DistDfeInt.ConsNsu"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    consChNFe: Optional["DistDfeInt.ConsChNfe"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    versao: Optional[TverDistDfe] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class DistNsu:
        """
        :ivar ultNSU: Último NSU recebido pelo ator. Caso seja informado
            com zero, ou com um NSU muito antigo, a consulta retornará
            unicamente as informações resumidas e documentos fiscais
            eletrônicos que tenham sido recepcionados pelo Ambiente
            Nacional nos últimos 3 meses.
        """
        ultNSU: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "pattern": r"[0-9]{15}",
            }
        )

    @dataclass
    class ConsNsu:
        """
        :ivar NSU: Número Sequencial Único. Geralmente esta consulta
            será utilizada quando identificado pelo interessado um NSU
            faltante. O Web Service retornará o documento ou informará
            que o NSU não existe no Ambiente Nacional. Assim, esta
            consulta fechará a lacuna do NSU identificado como faltante.
        """
        NSU: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "pattern": r"[0-9]{15}",
            }
        )

    @dataclass
    class ConsChNfe:
        """
        :ivar chNFe: Chave de acesso da NF-e a ser consultada
        """
        chNFe: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
