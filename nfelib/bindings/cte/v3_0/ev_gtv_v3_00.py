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

    :ivar desc_evento: Descrição do Evento - “Informações da GTV”
    :ivar inf_gtv: Grupo de Informações das GTV
    """
    class Meta:
        name = "evGTV"
        namespace = "http://www.portalfiscal.inf.br/cte"

    desc_evento: Optional[EvGtvDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    inf_gtv: List["EvGtv.InfGtv"] = field(
        default_factory=list,
        metadata={
            "name": "infGTV",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class InfGtv:
        """
        :ivar n_doc: Número da GTV
        :ivar id: Identificador para diferenciar GTV de mesmo número
            (Usar número do AIDF ou  identificador interno da empresa),
        :ivar serie: Série
        :ivar subserie: Subsérie
        :ivar d_emi: Data de Emissão Formato AAAA-MM-DD
        :ivar n_dv: Número Dígito Verificador
        :ivar q_carga: Quantidade de volumes/malotes
        :ivar inf_especie: Informações das Espécies transportadas
        :ivar rem: Informações do Remetente da GTV
        :ivar dest: Informações do Destinatário da GTV
        :ivar placa: Placa do veículo
        :ivar uf: UF em que veículo está licenciado Sigla da UF de
            licenciamento do veículo.
        :ivar rntrc: RNTRC do transportador
        """
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
        d_emi: Optional[str] = field(
            default=None,
            metadata={
                "name": "dEmi",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
            }
        )
        n_dv: Optional[str] = field(
            default=None,
            metadata={
                "name": "nDV",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 1,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        q_carga: Optional[str] = field(
            default=None,
            metadata={
                "name": "qCarga",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
            }
        )
        inf_especie: List["EvGtv.InfGtv.InfEspecie"] = field(
            default_factory=list,
            metadata={
                "name": "infEspecie",
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
        uf: Optional[Tuf] = field(
            default=None,
            metadata={
                "name": "UF",
                "type": "Element",
            }
        )
        rntrc: Optional[str] = field(
            default=None,
            metadata={
                "name": "RNTRC",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{8}|ISENTO",
            }
        )

        @dataclass
        class InfEspecie:
            """
            :ivar tp_especie: Tipo da Espécie 1 - Numerário 2 - Cheque 3
                - Moeda 4 - Outros
            :ivar v_especie: Valor Transportada em Espécie indicada
            """
            tp_especie: Optional[InfEspecieTpEspecie] = field(
                default=None,
                metadata={
                    "name": "tpEspecie",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            v_especie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vEspecie",
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )

        @dataclass
        class Rem:
            """
            :ivar cnpj: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar cpf: Número do CPF Informar os zeros não
                significativos.
            :ivar ie: Inscrição Estadual Informar a IE do remetente ou
                ISENTO se remetente é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                remetente não seja contribuinte do ICMS não informar o
                conteúdo.
            :ivar uf: Sigla da UF Informar EX para operações com o
                exterior.
            :ivar x_nome: Razão social ou nome do remetente
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            uf: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UF",
                    "type": "Element",
                    "required": True,
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
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
            :ivar cnpj: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar cpf: Número do CPF Informar os zeros não
                significativos.
            :ivar ie: Inscrição Estadual Informar a IE do destinatário
                ou ISENTO se remetente é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                remetente não seja contribuinte do ICMS não informar o
                conteúdo.
            :ivar uf: Sigla da UF Informar EX para operações com o
                exterior.
            :ivar x_nome: Razão social ou nome do destinatário
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            uf: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UF",
                    "type": "Element",
                    "required": True,
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
