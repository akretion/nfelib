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

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar c_ufautor: Código da UF do Autor
    :ivar cnpj: CNPJ do interessado no DF-e
    :ivar cpf: CPF do interessado no DF-e
    :ivar dist_nsu: Grupo para distribuir DF-e de interesse
    :ivar cons_nsu: Grupo para consultar um DF-e a partir de um NSU
        específico
    :ivar cons_ch_nfe: Grupo para consultar uma NF-e a partir da chave
        de acesso
    :ivar versao:
    """
    class Meta:
        name = "distDFeInt"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "required": True,
        }
    )
    c_ufautor: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUFAutor",
            "type": "Element",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Element",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    dist_nsu: Optional["DistDfeInt.DistNsu"] = field(
        default=None,
        metadata={
            "name": "distNSU",
            "type": "Element",
        }
    )
    cons_nsu: Optional["DistDfeInt.ConsNsu"] = field(
        default=None,
        metadata={
            "name": "consNSU",
            "type": "Element",
        }
    )
    cons_ch_nfe: Optional["DistDfeInt.ConsChNfe"] = field(
        default=None,
        metadata={
            "name": "consChNFe",
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
        :ivar ult_nsu: Último NSU recebido pelo ator. Caso seja
            informado com zero, ou com um NSU muito antigo, a consulta
            retornará unicamente as informações resumidas e documentos
            fiscais eletrônicos que tenham sido recepcionados pelo
            Ambiente Nacional nos últimos 3 meses.
        """
        ult_nsu: Optional[str] = field(
            default=None,
            metadata={
                "name": "ultNSU",
                "type": "Element",
                "required": True,
                "pattern": r"[0-9]{15}",
            }
        )

    @dataclass
    class ConsNsu:
        """
        :ivar nsu: Número Sequencial Único. Geralmente esta consulta
            será utilizada quando identificado pelo interessado um NSU
            faltante. O Web Service retornará o documento ou informará
            que o NSU não existe no Ambiente Nacional. Assim, esta
            consulta fechará a lacuna do NSU identificado como faltante.
        """
        nsu: Optional[str] = field(
            default=None,
            metadata={
                "name": "NSU",
                "type": "Element",
                "required": True,
                "pattern": r"[0-9]{15}",
            }
        )

    @dataclass
    class ConsChNfe:
        """
        :ivar ch_nfe: Chave de acesso da NF-e a ser consultada
        """
        ch_nfe: Optional[str] = field(
            default=None,
            metadata={
                "name": "chNFe",
                "type": "Element",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
