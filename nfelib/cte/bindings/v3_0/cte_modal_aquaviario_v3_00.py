from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class AquavDirec(Enum):
    N = "N"
    S = "S"
    L = "L"
    O = "O"


class AquavTpNav(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


@dataclass
class Aquav:
    """
    Informações do modal Aquaviário.

    :ivar vPrest: Valor da Prestação Base de Cálculo do AFRMM
    :ivar vAFRMM: AFRMM (Adicional de Frete para Renovação da Marinha
        Mercante)
    :ivar xNavio: Identificação do Navio
    :ivar balsa: Grupo de informações das balsas
    :ivar nViag: Número da Viagem
    :ivar direc: Direção Preencher com: N-Norte, L-Leste, S-Sul, O-Oeste
    :ivar irin: Irin do navio sempre deverá ser informado
    :ivar detCont: Grupo de informações de detalhamento dos conteiners
        (Somente para Redespacho Intermediário e Serviço Vinculado a
        Multimodal)
    :ivar tpNav: Tipo de Navegação Preencher com: 0 - Interior; 1 -
        Cabotagem
    """
    class Meta:
        name = "aquav"
        namespace = "http://www.portalfiscal.inf.br/cte"

    vPrest: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    vAFRMM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    xNavio: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    balsa: List["Aquav.Balsa"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 3,
        }
    )
    nViag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"[1-9]{1}[0-9]{0,9}",
        }
    )
    direc: Optional[AquavDirec] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    irin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "white_space": "preserve",
        }
    )
    detCont: List["Aquav.DetCont"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    tpNav: Optional[AquavTpNav] = field(
        default=None,
        metadata={
            "type": "Element",
            "white_space": "preserve",
        }
    )

    @dataclass
    class Balsa:
        """
        :ivar xBalsa: Identificador da Balsa
        """
        xBalsa: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )

    @dataclass
    class DetCont:
        """
        :ivar nCont: Identificação do Container
        :ivar lacre: Grupo de informações dos lacres dos cointainers da
            qtde da carga
        :ivar infDoc: Informações dos documentos dos conteiners
        """
        nCont: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[A-Z0-9]+",
            }
        )
        lacre: List["Aquav.DetCont.Lacre"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "max_occurs": 3,
            }
        )
        infDoc: Optional["Aquav.DetCont.InfDoc"] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )

        @dataclass
        class Lacre:
            """
            :ivar nLacre: Lacre
            """
            nLacre: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )

        @dataclass
        class InfDoc:
            """
            :ivar infNF: Informações das NF
            :ivar infNFe: Informações das NFe
            """
            infNF: List["Aquav.DetCont.InfDoc.InfNf"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                }
            )
            infNFe: List["Aquav.DetCont.InfDoc.InfNfe"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                }
            )

            @dataclass
            class InfNf:
                """
                :ivar serie: Série
                :ivar nDoc: Número
                :ivar unidRat: Unidade de medida rateada (Peso,Volume)
                """
                serie: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 3,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                nDoc: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                unidRat: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,3}(\.[0-9]{2,3})?",
                    }
                )

            @dataclass
            class InfNfe:
                """
                :ivar chave: Chave de acesso da NF-e
                :ivar unidRat: Unidade de medida rateada (Peso,Volume)
                """
                chave: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "max_length": 44,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{44}",
                    }
                )
                unidRat: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,3}(\.[0-9]{2,3})?",
                    }
                )
