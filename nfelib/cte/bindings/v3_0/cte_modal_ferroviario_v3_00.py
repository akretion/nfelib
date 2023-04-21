from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.cte.bindings.v3_0.tipos_geral_cte_v3_00 import Tuf

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class FerrovTpTraf(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TrafMutFerrEmi(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


class TrafMutRespFat(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


@dataclass
class TenderFer:
    """
    Tipo Dados do Endereço.

    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município Utilizar a tabela do IBGE Informar
        9999999 para operações com o exterior.
    :ivar xMun: Nome do município Informar EXTERIOR para operações com o
        exterior.
    :ivar CEP: CEP
    :ivar UF: Sigla da UF Informar EX para operações com o exterior.
    """
    class Meta:
        name = "TEnderFer"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 2,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )


@dataclass
class Ferrov:
    """
    Informações do modal Ferroviário.

    :ivar tpTraf: Tipo de Tráfego Preencher com: 0-Próprio; 1-Mútuo;
        2-Rodoferroviário; 3-Rodoviário.
    :ivar trafMut: Detalhamento de informações para o tráfego mútuo
    :ivar fluxo: Fluxo Ferroviário Trata-se de um número identificador
        do contrato firmado com o cliente
    """
    class Meta:
        name = "ferrov"
        namespace = "http://www.portalfiscal.inf.br/cte"

    tpTraf: Optional[FerrovTpTraf] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    trafMut: Optional["Ferrov.TrafMut"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fluxo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )

    @dataclass
    class TrafMut:
        """
        :ivar respFat: Responsável pelo Faturamento Preencher com:
            1-Ferrovia de origem; 2-Ferrovia de destino
        :ivar ferrEmi: Ferrovia Emitente do CTe Preencher com:
            1-Ferrovia de origem; 2-Ferrovia de destino
        :ivar vFrete: Valor do Frete do Tráfego Mútuo
        :ivar chCTeFerroOrigem: Chave de acesso do CT-e emitido pelo
            ferrovia de origem
        :ivar ferroEnv: Informações das Ferrovias Envolvidas
        """
        respFat: Optional[TrafMutRespFat] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
            }
        )
        ferrEmi: Optional[TrafMutFerrEmi] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
            }
        )
        vFrete: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        chCTeFerroOrigem: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        ferroEnv: List["Ferrov.TrafMut.FerroEnv"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )

        @dataclass
        class FerroEnv:
            """
            :ivar CNPJ: Número do CNPJ Informar o CNPJ da Ferrovia
                Envolvida. Caso a Ferrovia envolvida não seja inscrita
                no CNPJ o campo deverá preenchido com zeros. Informar os
                zeros não significativos.
            :ivar cInt: Código interno da Ferrovia envolvida Uso da
                transportadora
            :ivar IE: Inscrição Estadual
            :ivar xNome: Razão Social ou Nome
            :ivar enderFerro: Dados do endereço da ferrovia envolvida
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            cInt: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 10,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            enderFerro: Optional[TenderFer] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
