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

    :ivar v_prest: Valor da Prestação Base de Cálculo do AFRMM
    :ivar v_afrmm: AFRMM (Adicional de Frete para Renovação da Marinha
        Mercante)
    :ivar x_navio: Identificação do Navio
    :ivar balsa: Grupo de informações das balsas
    :ivar n_viag: Número da Viagem
    :ivar direc: Direção Preencher com: N-Norte, L-Leste, S-Sul, O-Oeste
    :ivar irin: Irin do navio sempre deverá ser informado
    :ivar det_cont: Grupo de informações de detalhamento dos conteiners
        (Somente para Redespacho Intermediário e Serviço Vinculado a
        Multimodal)
    :ivar tp_nav: Tipo de Navegação Preencher com: 0 - Interior; 1 -
        Cabotagem
    """
    class Meta:
        name = "aquav"
        namespace = "http://www.portalfiscal.inf.br/cte"

    v_prest: Optional[str] = field(
        default=None,
        metadata={
            "name": "vPrest",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_afrmm: Optional[str] = field(
        default=None,
        metadata={
            "name": "vAFRMM",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    x_navio: Optional[str] = field(
        default=None,
        metadata={
            "name": "xNavio",
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
    n_viag: Optional[str] = field(
        default=None,
        metadata={
            "name": "nViag",
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
    det_cont: List["Aquav.DetCont"] = field(
        default_factory=list,
        metadata={
            "name": "detCont",
            "type": "Element",
        }
    )
    tp_nav: Optional[AquavTpNav] = field(
        default=None,
        metadata={
            "name": "tpNav",
            "type": "Element",
            "white_space": "preserve",
        }
    )

    @dataclass
    class Balsa:
        """
        :ivar x_balsa: Identificador da Balsa
        """
        x_balsa: Optional[str] = field(
            default=None,
            metadata={
                "name": "xBalsa",
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
        :ivar n_cont: Identificação do Container
        :ivar lacre: Grupo de informações dos lacres dos cointainers da
            qtde da carga
        :ivar inf_doc: Informações dos documentos dos conteiners
        """
        n_cont: Optional[str] = field(
            default=None,
            metadata={
                "name": "nCont",
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
        inf_doc: Optional["Aquav.DetCont.InfDoc"] = field(
            default=None,
            metadata={
                "name": "infDoc",
                "type": "Element",
            }
        )

        @dataclass
        class Lacre:
            """
            :ivar n_lacre: Lacre
            """
            n_lacre: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nLacre",
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
            :ivar inf_nf: Informações das NF
            :ivar inf_nfe: Informações das NFe
            """
            inf_nf: List["Aquav.DetCont.InfDoc.InfNf"] = field(
                default_factory=list,
                metadata={
                    "name": "infNF",
                    "type": "Element",
                }
            )
            inf_nfe: List["Aquav.DetCont.InfDoc.InfNfe"] = field(
                default_factory=list,
                metadata={
                    "name": "infNFe",
                    "type": "Element",
                }
            )

            @dataclass
            class InfNf:
                """
                :ivar serie: Série
                :ivar n_doc: Número
                :ivar unid_rat: Unidade de medida rateada (Peso,Volume)
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
                n_doc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nDoc",
                        "type": "Element",
                        "required": True,
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                unid_rat: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "unidRat",
                        "type": "Element",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,3}(\.[0-9]{2,3})?",
                    }
                )

            @dataclass
            class InfNfe:
                """
                :ivar chave: Chave de acesso da NF-e
                :ivar unid_rat: Unidade de medida rateada (Peso,Volume)
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
                unid_rat: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "unidRat",
                        "type": "Element",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,3}(\.[0-9]{2,3})?",
                    }
                )
