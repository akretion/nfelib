from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bindings.mdfe.v3_0.mdfe_modal_rodoviario_v3_00 import (
    CompTpComp,
    InfPagIndPag,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class EvPagtoOperMdfeDescEvento(Enum):
    PAGAMENTO_OPERA_O_MDF_E = "Pagamento Operação MDF-e"
    PAGAMENTO_OPERACAO_MDF_E = "Pagamento Operacao MDF-e"


@dataclass
class EvPagtoOperMdfe:
    """
    Schema XML de validação do evento de pagamento da operação de transporte
    110116.

    :ivar desc_evento: Descrição do Evento - “Pagamento Operação MDF-e”
    :ivar n_prot: Número do Protocolo de Status do MDF-e. 1 posição tipo
        de autorizador (9 - SEFAZ Nacional ); 2 posições ano; 10
        seqüencial no ano.
    :ivar inf_viagens: Informações do total de viagens acobertadas pelo
        Evento “pagamento do frete”
    :ivar inf_pag: Informações do Pagamento do Frete
    """
    class Meta:
        name = "evPagtoOperMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    desc_evento: Optional[EvPagtoOperMdfeDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    n_prot: Optional[str] = field(
        default=None,
        metadata={
            "name": "nProt",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    inf_viagens: Optional["EvPagtoOperMdfe.InfViagens"] = field(
        default=None,
        metadata={
            "name": "infViagens",
            "type": "Element",
            "required": True,
        }
    )
    inf_pag: List["EvPagtoOperMdfe.InfPag"] = field(
        default_factory=list,
        metadata={
            "name": "infPag",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class InfViagens:
        """
        :ivar qtd_viagens: Quantidade total de viagens realizadas com o
            pagamento do Frete
        :ivar nro_viagem: Número de referência da viagem do MDFe
            referenciado.
        """
        qtd_viagens: Optional[str] = field(
            default=None,
            metadata={
                "name": "qtdViagens",
                "type": "Element",
                "required": True,
                "pattern": r"[0-9]{5}",
            }
        )
        nro_viagem: Optional[str] = field(
            default=None,
            metadata={
                "name": "nroViagem",
                "type": "Element",
                "required": True,
                "pattern": r"[0-9]{5}",
            }
        )

    @dataclass
    class InfPag:
        """
        :ivar x_nome: Razão social ou Nome do responsavel pelo pagamento
        :ivar cpf: Número do CPF do responsável pelo pgto Informar os
            zeros não significativos.
        :ivar cnpj: Número do CNPJ do responsável pelo pgto Informar os
            zeros não significativos.
        :ivar id_estrangeiro: Identificador do responsável pelo pgto em
            caso de ser estrangeiro
        :ivar comp: Componentes do Pagamentoi do Frete
        :ivar v_contrato: Valor Total do Contrato
        :ivar ind_pag: Indicador da Forma de Pagamento:0-Pagamento à
            Vista;1-Pagamento à Prazo;
        :ivar v_adiant: Valor do Adiantamento (usar apenas em pagamento
            à Prazo
        :ivar inf_prazo: Informações do pagamento a prazo. Informar
            somente se indPag for à Prazo
        :ivar inf_banc: Informações bancárias
        """
        x_nome: Optional[str] = field(
            default=None,
            metadata={
                "name": "xNome",
                "type": "Element",
                "min_length": 2,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
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
        cnpj: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJ",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{0}|[0-9]{14}",
            }
        )
        id_estrangeiro: Optional[str] = field(
            default=None,
            metadata={
                "name": "idEstrangeiro",
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
        v_contrato: Optional[str] = field(
            default=None,
            metadata={
                "name": "vContrato",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        ind_pag: Optional[InfPagIndPag] = field(
            default=None,
            metadata={
                "name": "indPag",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
            }
        )
        v_adiant: Optional[str] = field(
            default=None,
            metadata={
                "name": "vAdiant",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        inf_prazo: List["EvPagtoOperMdfe.InfPag.InfPrazo"] = field(
            default_factory=list,
            metadata={
                "name": "infPrazo",
                "type": "Element",
            }
        )
        inf_banc: Optional["EvPagtoOperMdfe.InfPag.InfBanc"] = field(
            default=None,
            metadata={
                "name": "infBanc",
                "type": "Element",
                "required": True,
            }
        )

        @dataclass
        class Comp:
            """
            :ivar tp_comp: Tipo do Componente 01 - Vale Pedágio; 02 -
                Impostos, taxas e contribuições; 03 - Despesas
                (bancárias, meios de pagamento, outras) ; 99 - Outros
            :ivar v_comp: Valor do componente
            :ivar x_comp: Descrição do componente do tipo Outros
            """
            tp_comp: Optional[CompTpComp] = field(
                default=None,
                metadata={
                    "name": "tpComp",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            v_comp: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vComp",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            x_comp: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xComp",
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
            :ivar n_parcela: Número da Parcela
            :ivar d_venc: Data de vencimento da Parcela (AAAA-MM-DD)
            :ivar v_parcela: Valor da Parcela
            """
            n_parcela: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nParcela",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{3}",
                }
            )
            d_venc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dVenc",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            v_parcela: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vParcela",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )

        @dataclass
        class InfBanc:
            """
            :ivar cod_banco: Número do banco
            :ivar cod_agencia: Número da agência bancária
            :ivar cnpjipef: Número do CNPJ da Instituição de Pagamento
                Eletrônico do Frete Informar os zeros não
                significativos.
            :ivar pix: Chave PIX Informar a chave PIX para recebimento
                do frete. Pode ser email, CPF/ CNPJ (somente numeros),
                Telefone com a seguinte formatação (+5599999999999) ou a
                chave aleatória gerada pela instituição.
            """
            cod_banco: Optional[str] = field(
                default=None,
                metadata={
                    "name": "codBanco",
                    "type": "Element",
                    "min_length": 3,
                    "max_length": 5,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            cod_agencia: Optional[str] = field(
                default=None,
                metadata={
                    "name": "codAgencia",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 10,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            cnpjipef: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJIPEF",
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            pix: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PIX",
                    "type": "Element",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
