from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class CompTpComp(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_99 = "99"


class EvPagtoOperMdfeDescEvento(Enum):
    PAGAMENTO_OPERA_O_MDF_E = "Pagamento Operação MDF-e"
    PAGAMENTO_OPERACAO_MDF_E = "Pagamento Operacao MDF-e"


class InfPagIndPag(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


@dataclass
class EvPagtoOperMdfe:
    """
    Schema XML de validação do evento de pagamento da operação de transporte
    110116.

    :ivar descEvento: Descrição do Evento - “Pagamento Operação MDF-e”
    :ivar nProt: Número do Protocolo de Status do MDF-e. 1 posição tipo
        de autorizador (9 - SEFAZ Nacional ); 2 posições ano; 10
        seqüencial no ano.
    :ivar infViagens: Informações do total de viagens acobertadas pelo
        Evento “pagamento do frete”
    :ivar infPag: Informações do Pagamento do Frete
    """
    class Meta:
        name = "evPagtoOperMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    descEvento: Optional[EvPagtoOperMdfeDescEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    nProt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    infViagens: Optional["EvPagtoOperMdfe.InfViagens"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    infPag: List["EvPagtoOperMdfe.InfPag"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class InfViagens:
        """
        :ivar qtdViagens: Quantidade total de viagens realizadas com o
            pagamento do Frete
        :ivar nroViagem: Número de referência da viagem do MDFe
            referenciado.
        """
        qtdViagens: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "pattern": r"[0-9]{5}",
            }
        )
        nroViagem: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "pattern": r"[0-9]{5}",
            }
        )

    @dataclass
    class InfPag:
        """
        :ivar xNome: Razão social ou Nome do responsavel pelo pagamento
        :ivar CPF: Número do CPF do responsável pelo pgto Informar os
            zeros não significativos.
        :ivar CNPJ: Número do CNPJ do responsável pelo pgto Informar os
            zeros não significativos.
        :ivar idEstrangeiro: Identificador do responsável pelo pgto em
            caso de ser estrangeiro
        :ivar comp: Componentes do Pagamentoi do Frete
        :ivar vContrato: Valor Total do Contrato
        :ivar indPag: Indicador da Forma de Pagamento:0-Pagamento à
            Vista;1-Pagamento à Prazo;
        :ivar vAdiant: Valor do Adiantamento (usar apenas em pagamento à
            Prazo
        :ivar infPrazo: Informações do pagamento a prazo. Informar
            somente se indPag for à Prazo
        :ivar infBanc: Informações bancárias
        """
        xNome: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "min_length": 2,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
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
        CNPJ: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{0}|[0-9]{14}",
            }
        )
        idEstrangeiro: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "min_length": 2,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"([!-ÿ]{0}|[!-ÿ]{5,20})?",
            }
        )
        comp: List["EvPagtoOperMdfe.InfPag.Comp"] = field(
            default_factory=list,
            metadata={
                "name": "Comp",
                "type": "Element",
                "min_occurs": 1,
            }
        )
        vContrato: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        indPag: Optional[InfPagIndPag] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
            }
        )
        vAdiant: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        infPrazo: List["EvPagtoOperMdfe.InfPag.InfPrazo"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )
        infBanc: Optional["EvPagtoOperMdfe.InfPag.InfBanc"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )

        @dataclass
        class Comp:
            """
            :ivar tpComp: Tipo do Componente 01 - Vale Pedágio; 02 -
                Impostos, taxas e contribuições; 03 - Despesas
                (bancárias, meios de pagamento, outras) ; 99 - Outros
            :ivar vComp: Valor do componente
            :ivar xComp: Descrição do componente do tipo Outros
            """
            tpComp: Optional[CompTpComp] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            vComp: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            xComp: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )

        @dataclass
        class InfPrazo:
            """
            :ivar nParcela: Número da Parcela
            :ivar dVenc: Data de vencimento da Parcela (AAAA-MM-DD)
            :ivar vParcela: Valor da Parcela
            """
            nParcela: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{3}",
                }
            )
            dVenc: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            vParcela: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )

        @dataclass
        class InfBanc:
            """
            :ivar codBanco: Número do banco
            :ivar codAgencia: Número da agência bancária
            :ivar CNPJIPEF: Número do CNPJ da Instituição de Pagamento
                Eletrônico do Frete Informar os zeros não
                significativos.
            :ivar PIX: Chave PIX Informar a chave PIX para recebimento
                do frete. Pode ser email, CPF/ CNPJ (somente numeros),
                Telefone com a seguinte formatação (+5599999999999) ou a
                chave aleatória gerada pela instituição.
            """
            codBanco: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 3,
                    "max_length": 5,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            codAgencia: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 10,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            CNPJIPEF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            PIX: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
