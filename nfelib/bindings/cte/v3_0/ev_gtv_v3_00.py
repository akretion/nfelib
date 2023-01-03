from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bindings.cte.v3_0.cte_tipos_basico_v3_00 import InfEspecieTpEspecie
from nfelib.bindings.cte.v3_0.tipos_geral_cte_v3_00 import Tuf

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class EvGtvDescEvento(Enum):
    INFORMA_ES_DA_GTV = "Informações da GTV"
    INFORMACOES_DA_GTV = "Informacoes da GTV"


@dataclass
class EvGtv:
    """
    Schema XML de validação do evento informações da GTV 110170.

    :ivar descEvento: Descrição do Evento - “Informações da GTV”
    :ivar infGTV: Grupo de Informações das GTV
    """
    class Meta:
        name = "evGTV"
        namespace = "http://www.portalfiscal.inf.br/cte"

    descEvento: Optional[EvGtvDescEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    infGTV: List["EvGtv.InfGtv"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class InfGtv:
        """
        :ivar nDoc: Número da GTV
        :ivar id: Identificador para diferenciar GTV de mesmo número
            (Usar número do AIDF ou  identificador interno da empresa),
        :ivar serie: Série
        :ivar subserie: Subsérie
        :ivar dEmi: Data de Emissão Formato AAAA-MM-DD
        :ivar nDV: Número Dígito Verificador
        :ivar qCarga: Quantidade de volumes/malotes
        :ivar infEspecie: Informações das Espécies transportadas
        :ivar rem: Informações do Remetente da GTV
        :ivar dest: Informações do Destinatário da GTV
        :ivar placa: Placa do veículo
        :ivar UF: UF em que veículo está licenciado Sigla da UF de
            licenciamento do veículo.
        :ivar RNTRC: RNTRC do transportador
        """
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
        id: Optional[str] = field(
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
        serie: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "min_length": 1,
                "max_length": 3,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        subserie: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "min_length": 1,
                "max_length": 3,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        dEmi: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
            }
        )
        nDV: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 1,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        qCarga: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
            }
        )
        infEspecie: List["EvGtv.InfGtv.InfEspecie"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
            }
        )
        rem: Optional["EvGtv.InfGtv.Rem"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        dest: Optional["EvGtv.InfGtv.Dest"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        placa: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[A-Z]{2,3}[0-9]{4}|[A-Z]{3,4}[0-9]{3}|[A-Z0-9]{7}",
            }
        )
        UF: Optional[Tuf] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        RNTRC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{8}|ISENTO",
            }
        )

        @dataclass
        class InfEspecie:
            """
            :ivar tpEspecie: Tipo da Espécie 1 - Numerário 2 - Cheque 3
                - Moeda 4 - Outros
            :ivar vEspecie: Valor Transportada em Espécie indicada
            """
            tpEspecie: Optional[InfEspecieTpEspecie] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            vEspecie: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )

        @dataclass
        class Rem:
            """
            :ivar CNPJ: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar CPF: Número do CPF Informar os zeros não
                significativos.
            :ivar IE: Inscrição Estadual Informar a IE do remetente ou
                ISENTO se remetente é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                remetente não seja contribuinte do ICMS não informar o
                conteúdo.
            :ivar UF: Sigla da UF Informar EX para operações com o
                exterior.
            :ivar xNome: Razão social ou nome do remetente
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
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
                    "required": True,
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

        @dataclass
        class Dest:
            """
            :ivar CNPJ: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar CPF: Número do CPF Informar os zeros não
                significativos.
            :ivar IE: Inscrição Estadual Informar a IE do destinatário
                ou ISENTO se remetente é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                remetente não seja contribuinte do ICMS não informar o
                conteúdo.
            :ivar UF: Sigla da UF Informar EX para operações com o
                exterior.
            :ivar xNome: Razão social ou nome do destinatário
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
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
                    "required": True,
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
