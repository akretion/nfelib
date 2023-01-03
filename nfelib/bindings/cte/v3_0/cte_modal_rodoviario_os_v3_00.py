from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from nfelib.bindings.cte.v3_0.tipos_geral_cte_v3_00 import Tuf

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class InfFretamentoTpFretamento(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


class PropTpProp(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"


@dataclass
class RodoOs:
    """
    Informações do modal Rodoviário.

    :ivar TAF: Termo de Autorização de Fretamento – TAF Registro
        obrigatório do emitente do CT-e OS junto à ANTT, de acordo com a
        Resolução ANTT nº 4.777/2015
    :ivar NroRegEstadual: Número do Registro Estadual Registro
        obrigatório do emitente do CT-e OS junto à Agência Reguladora
        Estadual.
    :ivar veic: Dados do Veículo
    :ivar infFretamento: Dados do fretamento (apenas para Transporte de
        Pessoas)
    """
    class Meta:
        name = "rodoOS"
        namespace = "http://www.portalfiscal.inf.br/cte"

    TAF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 12,
            "white_space": "preserve",
            "pattern": r"[0-9]{12}",
        }
    )
    NroRegEstadual: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 25,
            "white_space": "preserve",
            "pattern": r"[0-9]{25}",
        }
    )
    veic: Optional["RodoOs.Veic"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    infFretamento: Optional["RodoOs.InfFretamento"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class Veic:
        """
        :ivar placa: Placa do veículo
        :ivar RENAVAM: RENAVAM do veículo
        :ivar prop: Proprietário ou possuidor do Veículo. Só preenchido
            quando o veículo não pertencer à empresa emitente do CT-e OS
        :ivar UF: UF em que veículo está licenciado Sigla da UF de
            licenciamento do veículo.
        """
        placa: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[A-Z]{2,3}[0-9]{4}|[A-Z]{3,4}[0-9]{3}|[A-Z0-9]{7}",
            }
        )
        RENAVAM: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "min_length": 9,
                "max_length": 11,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        prop: Optional["RodoOs.Veic.Prop"] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        UF: Optional[Tuf] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )

        @dataclass
        class Prop:
            """
            :ivar CPF: Número do CPF Informar os zeros não
                significativos.
            :ivar CNPJ: Número do CNPJ Informar os zeros não
                significativos.
            :ivar TAF: Termo de Autorização de Fretamento – TAF De
                acordo com a Resolução ANTT nº 4.777/2015
            :ivar NroRegEstadual: Número do Registro Estadual Registro
                obrigatório do emitente do CT-e OS junto à Agência
                Reguladora  Estadual
            :ivar xNome: Razão Social ou Nome do proprietário
            :ivar IE: Inscrição Estadual
            :ivar UF: UF
            :ivar tpProp: Tipo Proprietário ou possuidor Preencher com:
                0-TAC – Agregado; 1-TAC Independente; ou 2 – Outros.
            """
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            TAF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "max_length": 12,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{12}",
                }
            )
            NroRegEstadual: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "max_length": 25,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{25}",
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
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            UF: Optional[Tuf] = field(
                default=None,
                metadata={
                    "type": "Element",
                }
            )
            tpProp: Optional[PropTpProp] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                }
            )

    @dataclass
    class InfFretamento:
        """
        :ivar tpFretamento: Tipo Fretamento Preencher com: 1 - Eventual
            2 - Continuo
        :ivar dhViagem: Data e hora da viagem (Apenas para fretamento
            eventual) Formato AAAA-MM-DDTHH:MM:DD TZD
        """
        tpFretamento: Optional[InfFretamentoTpFretamento] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
            }
        )
        dhViagem: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
