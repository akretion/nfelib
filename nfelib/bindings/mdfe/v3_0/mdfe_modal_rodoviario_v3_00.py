from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bindings.mdfe.v3_0.tipos_geral_mdfe_v3_00 import Tuf

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class CompTpComp(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_99 = "99"


class DispTpValePed(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"


class InfPagIndAltoDesemp(Enum):
    VALUE_1 = "1"


class InfPagIndPag(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class PropTpProp(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"


class ValePedCategCombVeic(Enum):
    VALUE_02 = "02"
    VALUE_04 = "04"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"


class VeicReboqueTpCar(Enum):
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"


class VeicTracaoTpCar(Enum):
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"


class VeicTracaoTpRod(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"


@dataclass
class Rodo:
    """
    Informações do modal Rodoviário.

    :ivar inf_antt: Grupo de informações para Agência Reguladora
    :ivar veic_tracao: Dados do Veículo com a Tração
    :ivar veic_reboque: Dados dos reboques
    :ivar cod_ag_porto: Código de Agendamento no porto
    :ivar lac_rodo: Lacres
    """
    class Meta:
        name = "rodo"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    inf_antt: Optional["Rodo.InfAntt"] = field(
        default=None,
        metadata={
            "name": "infANTT",
            "type": "Element",
        }
    )
    veic_tracao: Optional["Rodo.VeicTracao"] = field(
        default=None,
        metadata={
            "name": "veicTracao",
            "type": "Element",
            "required": True,
        }
    )
    veic_reboque: List["Rodo.VeicReboque"] = field(
        default_factory=list,
        metadata={
            "name": "veicReboque",
            "type": "Element",
            "max_occurs": 3,
        }
    )
    cod_ag_porto: Optional[str] = field(
        default=None,
        metadata={
            "name": "codAgPorto",
            "type": "Element",
            "min_length": 0,
            "max_length": 16,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    lac_rodo: List["Rodo.LacRodo"] = field(
        default_factory=list,
        metadata={
            "name": "lacRodo",
            "type": "Element",
        }
    )

    @dataclass
    class InfAntt:
        """
        :ivar rntrc: Registro Nacional de Transportadores Rodoviários de
            Carga Registro obrigatório do emitente do MDF-e junto à ANTT
            para exercer a atividade de transportador rodoviário de
            cargas por conta de terceiros e mediante remuneração.
        :ivar inf_ciot: Dados do CIOT
        :ivar vale_ped: Informações de Vale Pedágio Outras informações
            sobre Vale-Pedágio obrigatório que não tenham campos
            específicos devem ser informadas no campo de observações
            gerais de uso livre pelo contribuinte, visando atender as
            determinações legais vigentes.
        :ivar inf_contratante: Grupo de informações dos contratantes do
            serviço de transporte
        :ivar inf_pag: Informações do Pagamento do Frete
        """
        rntrc: Optional[str] = field(
            default=None,
            metadata={
                "name": "RNTRC",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{8}",
            }
        )
        inf_ciot: List["Rodo.InfAntt.InfCiot"] = field(
            default_factory=list,
            metadata={
                "name": "infCIOT",
                "type": "Element",
            }
        )
        vale_ped: Optional["Rodo.InfAntt.ValePed"] = field(
            default=None,
            metadata={
                "name": "valePed",
                "type": "Element",
            }
        )
        inf_contratante: List["Rodo.InfAntt.InfContratante"] = field(
            default_factory=list,
            metadata={
                "name": "infContratante",
                "type": "Element",
            }
        )
        inf_pag: List["Rodo.InfAntt.InfPag"] = field(
            default_factory=list,
            metadata={
                "name": "infPag",
                "type": "Element",
            }
        )

        @dataclass
        class InfCiot:
            """
            :ivar ciot: Código Identificador da Operação de Transporte
                Também Conhecido como conta frete
            :ivar cpf: Número do CPF responsável pela geração do CIOT
                Informar os zeros não significativos.
            :ivar cnpj: Número do CNPJ responsável pela geração do CIOT
                Informar os zeros não significativos.
            """
            ciot: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CIOT",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{12}",
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

        @dataclass
        class ValePed:
            """
            :ivar disp: Informações dos dispositivos do Vale Pedágio
            :ivar categ_comb_veic: Categoria de Combinação Veicular
                Preencher com: 02 Veículo Comercial 2 eixos;0 4 Veículo
                Comercial 3 eixos; 06 Veículo Comercial 4 eixos;0 7
                Veículo Comercial 5 eixos; 0 8 Veículo Comercial 6
                eixos; 10 Veículo Comercial 7 eixos; 11 Veículo
                Comercial 8 eixos; 12 Veículo Comercial 9 eixos; 13
                Veículo Comercial 10 eixos; 14 Veículo Comercial Acima
                de 10 eixos;
            """
            disp: List["Rodo.InfAntt.ValePed.Disp"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                }
            )
            categ_comb_veic: Optional[ValePedCategCombVeic] = field(
                default=None,
                metadata={
                    "name": "categCombVeic",
                    "type": "Element",
                    "white_space": "preserve",
                }
            )

            @dataclass
            class Disp:
                """
                :ivar cnpjforn: CNPJ da empresa fornecedora do Vale-
                    Pedágio - CNPJ da Empresa Fornecedora do Vale-
                    Pedágio, ou seja, empresa que fornece ao Responsável
                    pelo Pagamento do Vale-Pedágio os dispositivos do
                    Vale-Pedágio. - Informar os zeros não
                    significativos.
                :ivar cnpjpg: CNPJ do responsável pelo pagamento do
                    Vale-Pedágio - responsável pelo pagamento do Vale
                    Pedágio. Informar somente quando o responsável não
                    for o emitente do MDF-e. - Informar os zeros não
                    significativos.
                :ivar cpfpg: CNPJ do responsável pelo pagamento do Vale-
                    Pedágio Informar os zeros não significativos.
                :ivar n_compra: Número do comprovante de compra Número
                    de ordem do comprovante de compra do Vale-Pedágio
                    fornecido para cada veículo ou combinação veicular,
                    por viagem.
                :ivar v_vale_ped: Valor do Vale-Pedagio Valor do Vale-
                    Pedágio obrigatório necessário à livre circulação,
                    desde a origem da operação de transporte até o
                    destino, do transportador contratado.
                :ivar tp_vale_ped: Tipo do Vale Pedagio 01 - TAG; 02 -
                    Cupom; 03 - Cartão
                """
                cnpjforn: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CNPJForn",
                        "type": "Element",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{14}",
                    }
                )
                cnpjpg: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CNPJPg",
                        "type": "Element",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{0}|[0-9]{14}",
                    }
                )
                cpfpg: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CPFPg",
                        "type": "Element",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{11}",
                    }
                )
                n_compra: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nCompra",
                        "type": "Element",
                        "pattern": r"[0-9]{1,20}",
                    }
                )
                v_vale_ped: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vValePed",
                        "type": "Element",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                tp_vale_ped: Optional[DispTpValePed] = field(
                    default=None,
                    metadata={
                        "name": "tpValePed",
                        "type": "Element",
                        "white_space": "preserve",
                    }
                )

        @dataclass
        class InfContratante:
            """
            :ivar x_nome: Razão social ou Nome do contratante
            :ivar cpf: Número do CPF do contratante do serviço Informar
                os zeros não significativos.
            :ivar cnpj: Número do CNPJ do contratante do serviço
                Informar os zeros não significativos.
            :ivar id_estrangeiro: Identificador do contratante em caso
                de contratante estrangeiro
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

        @dataclass
        class InfPag:
            """
            :ivar x_nome: Razão social ou Nome do respnsável pelo
                pagamento
            :ivar cpf: Número do CPF do responsável pelo pgto Informar
                os zeros não significativos.
            :ivar cnpj: Número do CNPJ do responsável pelo pgto Informar
                os zeros não significativos.
            :ivar id_estrangeiro: Identificador do responsável pelo pgto
                em caso de ser estrangeiro
            :ivar comp: Componentes do Pagamentoi do Frete
            :ivar v_contrato: Valor Total do Contrato
            :ivar ind_alto_desemp: Indicador de operação de transporte
                de alto desempenho Operação de transporte com utilização
                de veículos de frotas dedicadas ou fidelizadas.
                Preencher com “1” para indicar operação de transporte de
                alto desempenho, demais casos não informar a tag
            :ivar ind_pag: Indicador da Forma de Pagamento:0-Pagamento à
                Vista;1-Pagamento à Prazo;
            :ivar v_adiant: Valor do Adiantamento (usar apenas em
                pagamento à Prazo
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
            comp: List["Rodo.InfAntt.InfPag.Comp"] = field(
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
            ind_alto_desemp: Optional[InfPagIndAltoDesemp] = field(
                default=None,
                metadata={
                    "name": "indAltoDesemp",
                    "type": "Element",
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
            inf_prazo: List["Rodo.InfAntt.InfPag.InfPrazo"] = field(
                default_factory=list,
                metadata={
                    "name": "infPrazo",
                    "type": "Element",
                }
            )
            inf_banc: Optional["Rodo.InfAntt.InfPag.InfBanc"] = field(
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
                :ivar tp_comp: Tipo do Componente Preencher com: 01 -
                    Vale Pedágio; 02 - Impostos, taxas e contribuições;
                    03 - Despesas (bancárias, meios de pagamento,
                    outras) ; 99 - Outros
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
                :ivar cnpjipef: Número do CNPJ da Instituição de
                    Pagamento Eletrônico do Frete Informar os zeros não
                    significativos.
                :ivar pix: Chave PIX Informar a chave PIX para
                    recebimento do frete. Pode ser email, CPF/ CNPJ
                    (somente numeros), Telefone com a seguinte
                    formatação (+5599999999999) ou a chave aleatória
                    gerada pela instituição.
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

    @dataclass
    class VeicTracao:
        """
        :ivar c_int: Código interno do veículo
        :ivar placa: Placa do veículo
        :ivar renavam: RENAVAM do veículo
        :ivar tara: Tara em KG
        :ivar cap_kg: Capacidade em KG
        :ivar cap_m3: Capacidade em M3
        :ivar prop: Proprietário ou possuidor do Veículo. Só preenchido
            quando o veículo não pertencer à empresa emitente do MDF-e
        :ivar condutor: Informações do(s) Condutor(es) do veículo
        :ivar tp_rod: Tipo de Rodado Preencher com: 01 - Truck; 02 -
            Toco; 03 - Cavalo Mecânico; 04 - VAN; 05 - Utilitário; 06 -
            Outros.
        :ivar tp_car: Tipo de Carroceria Preencher com: 00 - não
            aplicável; 01 - Aberta; 02 - Fechada/Baú; 03 - Granelera; 04
            - Porta Container; 05 - Sider
        :ivar uf: UF em que veículo está licenciado Sigla da UF de
            licenciamento do veículo.
        """
        c_int: Optional[str] = field(
            default=None,
            metadata={
                "name": "cInt",
                "type": "Element",
                "min_length": 1,
                "max_length": 10,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        placa: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[A-Z]{2,3}[0-9]{4}|[A-Z]{3,4}[0-9]{3}|[A-Z0-9]{7}",
            }
        )
        renavam: Optional[str] = field(
            default=None,
            metadata={
                "name": "RENAVAM",
                "type": "Element",
                "min_length": 9,
                "max_length": 11,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        tara: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,5}",
            }
        )
        cap_kg: Optional[str] = field(
            default=None,
            metadata={
                "name": "capKG",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,5}",
            }
        )
        cap_m3: Optional[str] = field(
            default=None,
            metadata={
                "name": "capM3",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,2}",
            }
        )
        prop: Optional["Rodo.VeicTracao.Prop"] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        condutor: List["Rodo.VeicTracao.Condutor"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 10,
            }
        )
        tp_rod: Optional[VeicTracaoTpRod] = field(
            default=None,
            metadata={
                "name": "tpRod",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
            }
        )
        tp_car: Optional[VeicTracaoTpCar] = field(
            default=None,
            metadata={
                "name": "tpCar",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
            }
        )
        uf: Optional[Tuf] = field(
            default=None,
            metadata={
                "name": "UF",
                "type": "Element",
            }
        )

        @dataclass
        class Prop:
            """
            :ivar cpf: Número do CPF Informar os zeros não
                significativos.
            :ivar cnpj: Número do CNPJ Informar os zeros não
                significativos.
            :ivar rntrc: Registro Nacional dos Transportadores
                Rodoviários de Carga Registro obrigatório do
                proprietário, co-proprietário ou arrendatário do veículo
                junto à ANTT para exercer a atividade de transportador
                rodoviário de cargas por conta de terceiros e mediante
                remuneração.
            :ivar x_nome: Razão Social ou Nome do proprietário
            :ivar ie: Inscrição Estadual
            :ivar uf: UF
            :ivar tp_prop: Tipo Proprietário ou possuidor Preencher com:
                0-TAC Agregado; 1-TAC Independente; 2 – Outros.
            """
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
            rntrc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "RNTRC",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
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
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO|PR[0-9]{4,8}",
                }
            )
            uf: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UF",
                    "type": "Element",
                }
            )
            tp_prop: Optional[PropTpProp] = field(
                default=None,
                metadata={
                    "name": "tpProp",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                }
            )

        @dataclass
        class Condutor:
            """
            :ivar x_nome: Nome do Condutor
            :ivar cpf: CPF do Condutor
            """
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
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )

    @dataclass
    class VeicReboque:
        """
        :ivar c_int: Código interno do veículo
        :ivar placa: Placa do veículo
        :ivar renavam: RENAVAM do veículo
        :ivar tara: Tara em KG
        :ivar cap_kg: Capacidade em KG
        :ivar cap_m3: Capacidade em M3
        :ivar prop: Proprietários ou possuidor do Veículo. Só preenchido
            quando o veículo não pertencer à empresa emitente do MDF-e
        :ivar tp_car: Tipo de Carroceria Preencher com: 00 - não
            aplicável; 01 - Aberta; 02 - Fechada/Baú; 03 - Granelera; 04
            - Porta Container; 05 - Sider
        :ivar uf: UF em que veículo está licenciado Sigla da UF de
            licenciamento do veículo.
        """
        c_int: Optional[str] = field(
            default=None,
            metadata={
                "name": "cInt",
                "type": "Element",
                "min_length": 1,
                "max_length": 10,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        placa: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[A-Z]{2,3}[0-9]{4}|[A-Z]{3,4}[0-9]{3}|[A-Z0-9]{7}",
            }
        )
        renavam: Optional[str] = field(
            default=None,
            metadata={
                "name": "RENAVAM",
                "type": "Element",
                "min_length": 9,
                "max_length": 11,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        tara: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,5}",
            }
        )
        cap_kg: Optional[str] = field(
            default=None,
            metadata={
                "name": "capKG",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,5}",
            }
        )
        cap_m3: Optional[str] = field(
            default=None,
            metadata={
                "name": "capM3",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,2}",
            }
        )
        prop: Optional["Rodo.VeicReboque.Prop"] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        tp_car: Optional[VeicReboqueTpCar] = field(
            default=None,
            metadata={
                "name": "tpCar",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
            }
        )
        uf: Optional[Tuf] = field(
            default=None,
            metadata={
                "name": "UF",
                "type": "Element",
            }
        )

        @dataclass
        class Prop:
            """
            :ivar cpf: Número do CPF Informar os zeros não
                significativos.
            :ivar cnpj: Número do CNPJ Informar os zeros não
                significativos.
            :ivar rntrc: Registro Nacional dos Transportadores
                Rodoviários de Carga Registro obrigatório do
                proprietário, co-proprietário ou arrendatário do veículo
                junto à ANTT para exercer a atividade de transportador
                rodoviário de cargas por conta de terceiros e mediante
                remuneração.
            :ivar x_nome: Razão Social ou Nome do proprietário
            :ivar ie: Inscrição Estadual
            :ivar uf: UF
            :ivar tp_prop: Tipo Proprietário ou possuidor Preencher com:
                0-TAC Agregado; 1-TAC Independente; 2 – Outros.
            """
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
            rntrc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "RNTRC",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO|PR[0-9]{4,8}",
                }
            )
            uf: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UF",
                    "type": "Element",
                }
            )
            tp_prop: Optional[PropTpProp] = field(
                default=None,
                metadata={
                    "name": "tpProp",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                }
            )

    @dataclass
    class LacRodo:
        """
        :ivar n_lacre: Número do Lacre
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
