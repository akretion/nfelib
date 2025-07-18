"""This file was generated by xsdata, v24.11, on 2025-07-14 04:38:46

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from nfelib import CommonMixin

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class CompTpComp(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_99 = "99"


class EvAlteracaoPagtoServMdfeDescEvento(Enum):
    ALTERA_O_PAGAMENTO_SERVI_O_MDFE = "Alteração Pagamento Serviço MDFe"
    ALTERACAO_PAGAMENTO_SERVICO_MDFE = "Alteracao Pagamento Servico MDFe"


class InfPagIndAntecipaAdiant(Enum):
    VALUE_1 = "1"


class InfPagIndPag(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class InfPagTpAntecip(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"


@dataclass
class EvAlteracaoPagtoServMdfe(CommonMixin):
    """
    Schema XML de validação do evento de alteração do pagamento do serviçp de
    transporte 110118.

    :ivar descEvento: Descrição do Evento - “Alteração Pagamento Serviço
        MDFe”
    :ivar nProt: Número do Protocolo de Status do MDF-e.
    :ivar infPag: Informações do Pagamento do Frete
    """

    class Meta:
        name = "evAlteracaoPagtoServMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    descEvento: Optional[EvAlteracaoPagtoServMdfeDescEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        },
    )
    nProt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        },
    )
    infPag: List["EvAlteracaoPagtoServMdfe.InfPag"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class InfPag(CommonMixin):
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
        :ivar indAntecipaAdiant: Indicador para declarar concordância em
            antecipar o adiantamento Operação de transporte com
            utilização de veículos de frotas dedicadas ou fidelizadas.
            Preencher com “1” para indicar operação de transporte de
            alto desempenho, demais casos não informar a tag
        :ivar infPrazo: Informações do pagamento a prazo. Informar
            somente se indPag for à Prazo
        :ivar tpAntecip: Tipo de Permissão em relação a antecipação das
            parcelas 0 - Não permite antecipar 1 - Permite antecipar as
            parcelas 2 - Permite antecipar as parcelas mediante
            confirmação
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
            },
        )
        CPF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{11}",
            },
        )
        CNPJ: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{0}|[A-Z0-9]{12}[0-9]{2}",
            },
        )
        idEstrangeiro: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "min_length": 2,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"([!-ÿ]{0}|[!-ÿ]{5,20})?",
            },
        )
        comp: List["EvAlteracaoPagtoServMdfe.InfPag.Comp"] = field(
            default_factory=list,
            metadata={
                "name": "Comp",
                "type": "Element",
                "min_occurs": 1,
            },
        )
        vContrato: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            },
        )
        indPag: Optional[InfPagIndPag] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
            },
        )
        vAdiant: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            },
        )
        indAntecipaAdiant: Optional[InfPagIndAntecipaAdiant] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        infPrazo: List["EvAlteracaoPagtoServMdfe.InfPag.InfPrazo"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        tpAntecip: Optional[InfPagTpAntecip] = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        infBanc: Optional["EvAlteracaoPagtoServMdfe.InfPag.InfBanc"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )

        @dataclass
        class Comp(CommonMixin):
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
                },
            )
            vComp: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                },
            )
            xComp: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )

        @dataclass
        class InfPrazo(CommonMixin):
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
                },
            )
            dVenc: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                },
            )
            vParcela: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                },
            )

        @dataclass
        class InfBanc(CommonMixin):
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
                },
            )
            codAgencia: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 10,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            CNPJIPEF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[A-Z0-9]{12}[0-9]{2}",
                },
            )
            PIX: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
