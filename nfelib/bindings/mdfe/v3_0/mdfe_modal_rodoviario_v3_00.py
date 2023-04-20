from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bindings.mdfe.v3_0.ev_pagto_oper_mdfe_v3_00 import (
    CompTpComp,
    InfPagIndPag,
)
from nfelib.bindings.mdfe.v3_0.tipos_geral_mdfe_v3_00 import Tuf

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class DispTpValePed(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"


class InfPagIndAltoDesemp(Enum):
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

    :ivar infANTT: Grupo de informações para Agência Reguladora
    :ivar veicTracao: Dados do Veículo com a Tração
    :ivar veicReboque: Dados dos reboques
    :ivar codAgPorto: Código de Agendamento no porto
    :ivar lacRodo: Lacres
    """
    class Meta:
        name = "rodo"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    infANTT: Optional["Rodo.InfAntt"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    veicTracao: Optional["Rodo.VeicTracao"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    veicReboque: List["Rodo.VeicReboque"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 3,
        }
    )
    codAgPorto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 0,
            "max_length": 16,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    lacRodo: List["Rodo.LacRodo"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class InfAntt:
        """
        :ivar RNTRC: Registro Nacional de Transportadores Rodoviários de
            Carga Registro obrigatório do emitente do MDF-e junto à ANTT
            para exercer a atividade de transportador rodoviário de
            cargas por conta de terceiros e mediante remuneração.
        :ivar infCIOT: Dados do CIOT
        :ivar valePed: Informações de Vale Pedágio Outras informações
            sobre Vale-Pedágio obrigatório que não tenham campos
            específicos devem ser informadas no campo de observações
            gerais de uso livre pelo contribuinte, visando atender as
            determinações legais vigentes.
        :ivar infContratante: Grupo de informações dos contratantes do
            serviço de transporte
        :ivar infPag: Informações do Pagamento do Frete
        """
        RNTRC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{8}",
            }
        )
        infCIOT: List["Rodo.InfAntt.InfCiot"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )
        valePed: Optional["Rodo.InfAntt.ValePed"] = field(
            default=None,
            metadata={
                "type": "Element",
            }
        )
        infContratante: List["Rodo.InfAntt.InfContratante"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )
        infPag: List["Rodo.InfAntt.InfPag"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            }
        )

        @dataclass
        class InfCiot:
            """
            :ivar CIOT: Código Identificador da Operação de Transporte
                Também Conhecido como conta frete
            :ivar CPF: Número do CPF responsável pela geração do CIOT
                Informar os zeros não significativos.
            :ivar CNPJ: Número do CNPJ responsável pela geração do CIOT
                Informar os zeros não significativos.
            """
            CIOT: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{12}",
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

        @dataclass
        class ValePed:
            """
            :ivar disp: Informações dos dispositivos do Vale Pedágio
            :ivar categCombVeic: Categoria de Combinação Veicular
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
            categCombVeic: Optional[ValePedCategCombVeic] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "white_space": "preserve",
                }
            )

            @dataclass
            class Disp:
                """
                :ivar CNPJForn: CNPJ da empresa fornecedora do Vale-
                    Pedágio - CNPJ da Empresa Fornecedora do Vale-
                    Pedágio, ou seja, empresa que fornece ao Responsável
                    pelo Pagamento do Vale-Pedágio os dispositivos do
                    Vale-Pedágio. - Informar os zeros não
                    significativos.
                :ivar CNPJPg: CNPJ do responsável pelo pagamento do
                    Vale-Pedágio - responsável pelo pagamento do Vale
                    Pedágio. Informar somente quando o responsável não
                    for o emitente do MDF-e. - Informar os zeros não
                    significativos.
                :ivar CPFPg: CNPJ do responsável pelo pagamento do Vale-
                    Pedágio Informar os zeros não significativos.
                :ivar nCompra: Número do comprovante de compra Número de
                    ordem do comprovante de compra do Vale-Pedágio
                    fornecido para cada veículo ou combinação veicular,
                    por viagem.
                :ivar vValePed: Valor do Vale-Pedagio Valor do Vale-
                    Pedágio obrigatório necessário à livre circulação,
                    desde a origem da operação de transporte até o
                    destino, do transportador contratado.
                :ivar tpValePed: Tipo do Vale Pedagio 01 - TAG; 02 -
                    Cupom; 03 - Cartão
                """
                CNPJForn: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{14}",
                    }
                )
                CNPJPg: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{0}|[0-9]{14}",
                    }
                )
                CPFPg: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{11}",
                    }
                )
                nCompra: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "pattern": r"[0-9]{1,20}",
                    }
                )
                vValePed: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                tpValePed: Optional[DispTpValePed] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "white_space": "preserve",
                    }
                )

        @dataclass
        class InfContratante:
            """
            :ivar xNome: Razão social ou Nome do contratante
            :ivar CPF: Número do CPF do contratante do serviço Informar
                os zeros não significativos.
            :ivar CNPJ: Número do CNPJ do contratante do serviço
                Informar os zeros não significativos.
            :ivar idEstrangeiro: Identificador do contratante em caso de
                contratante estrangeiro
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

        @dataclass
        class InfPag:
            """
            :ivar xNome: Razão social ou Nome do respnsável pelo
                pagamento
            :ivar CPF: Número do CPF do responsável pelo pgto Informar
                os zeros não significativos.
            :ivar CNPJ: Número do CNPJ do responsável pelo pgto Informar
                os zeros não significativos.
            :ivar idEstrangeiro: Identificador do responsável pelo pgto
                em caso de ser estrangeiro
            :ivar comp: Componentes do Pagamentoi do Frete
            :ivar vContrato: Valor Total do Contrato
            :ivar indAltoDesemp: Indicador de operação de transporte de
                alto desempenho Operação de transporte com utilização de
                veículos de frotas dedicadas ou fidelizadas. Preencher
                com “1” para indicar operação de transporte de alto
                desempenho, demais casos não informar a tag
            :ivar indPag: Indicador da Forma de Pagamento:0-Pagamento à
                Vista;1-Pagamento à Prazo;
            :ivar vAdiant: Valor do Adiantamento (usar apenas em
                pagamento à Prazo
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
            comp: List["Rodo.InfAntt.InfPag.Comp"] = field(
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
            indAltoDesemp: Optional[InfPagIndAltoDesemp] = field(
                default=None,
                metadata={
                    "type": "Element",
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
            infPrazo: List["Rodo.InfAntt.InfPag.InfPrazo"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                }
            )
            infBanc: Optional["Rodo.InfAntt.InfPag.InfBanc"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )

            @dataclass
            class Comp:
                """
                :ivar tpComp: Tipo do Componente Preencher com: 01 -
                    Vale Pedágio; 02 - Impostos, taxas e contribuições;
                    03 - Despesas (bancárias, meios de pagamento,
                    outras) ; 99 - Outros
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
                :ivar CNPJIPEF: Número do CNPJ da Instituição de
                    Pagamento Eletrônico do Frete Informar os zeros não
                    significativos.
                :ivar PIX: Chave PIX Informar a chave PIX para
                    recebimento do frete. Pode ser email, CPF/ CNPJ
                    (somente numeros), Telefone com a seguinte
                    formatação (+5599999999999) ou a chave aleatória
                    gerada pela instituição.
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

    @dataclass
    class VeicTracao:
        """
        :ivar cInt: Código interno do veículo
        :ivar placa: Placa do veículo
        :ivar RENAVAM: RENAVAM do veículo
        :ivar tara: Tara em KG
        :ivar capKG: Capacidade em KG
        :ivar capM3: Capacidade em M3
        :ivar prop: Proprietário ou possuidor do Veículo. Só preenchido
            quando o veículo não pertencer à empresa emitente do MDF-e
        :ivar condutor: Informações do(s) Condutor(es) do veículo
        :ivar tpRod: Tipo de Rodado Preencher com: 01 - Truck; 02 -
            Toco; 03 - Cavalo Mecânico; 04 - VAN; 05 - Utilitário; 06 -
            Outros.
        :ivar tpCar: Tipo de Carroceria Preencher com: 00 - não
            aplicável; 01 - Aberta; 02 - Fechada/Baú; 03 - Granelera; 04
            - Porta Container; 05 - Sider
        :ivar UF: UF em que veículo está licenciado Sigla da UF de
            licenciamento do veículo.
        """
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
        tara: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,5}",
            }
        )
        capKG: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,5}",
            }
        )
        capM3: Optional[str] = field(
            default=None,
            metadata={
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
        tpRod: Optional[VeicTracaoTpRod] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
            }
        )
        tpCar: Optional[VeicTracaoTpCar] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
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
            :ivar RNTRC: Registro Nacional dos Transportadores
                Rodoviários de Carga Registro obrigatório do
                proprietário, co-proprietário ou arrendatário do veículo
                junto à ANTT para exercer a atividade de transportador
                rodoviário de cargas por conta de terceiros e mediante
                remuneração.
            :ivar xNome: Razão Social ou Nome do proprietário
            :ivar IE: Inscrição Estadual
            :ivar UF: UF
            :ivar tpProp: Tipo Proprietário ou possuidor Preencher com:
                0-TAC Agregado; 1-TAC Independente; 2 – Outros.
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
            RNTRC: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
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
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO|PR[0-9]{4,8}",
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
        class Condutor:
            """
            :ivar xNome: Nome do Condutor
            :ivar CPF: CPF do Condutor
            """
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
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )

    @dataclass
    class VeicReboque:
        """
        :ivar cInt: Código interno do veículo
        :ivar placa: Placa do veículo
        :ivar RENAVAM: RENAVAM do veículo
        :ivar tara: Tara em KG
        :ivar capKG: Capacidade em KG
        :ivar capM3: Capacidade em M3
        :ivar prop: Proprietários ou possuidor do Veículo. Só preenchido
            quando o veículo não pertencer à empresa emitente do MDF-e
        :ivar tpCar: Tipo de Carroceria Preencher com: 00 - não
            aplicável; 01 - Aberta; 02 - Fechada/Baú; 03 - Granelera; 04
            - Porta Container; 05 - Sider
        :ivar UF: UF em que veículo está licenciado Sigla da UF de
            licenciamento do veículo.
        """
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
        tara: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,5}",
            }
        )
        capKG: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,5}",
            }
        )
        capM3: Optional[str] = field(
            default=None,
            metadata={
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
        tpCar: Optional[VeicReboqueTpCar] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
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
            :ivar RNTRC: Registro Nacional dos Transportadores
                Rodoviários de Carga Registro obrigatório do
                proprietário, co-proprietário ou arrendatário do veículo
                junto à ANTT para exercer a atividade de transportador
                rodoviário de cargas por conta de terceiros e mediante
                remuneração.
            :ivar xNome: Razão Social ou Nome do proprietário
            :ivar IE: Inscrição Estadual
            :ivar UF: UF
            :ivar tpProp: Tipo Proprietário ou possuidor Preencher com:
                0-TAC Agregado; 1-TAC Independente; 2 – Outros.
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
            RNTRC: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            xNome: Optional[str] = field(
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
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO|PR[0-9]{4,8}",
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
    class LacRodo:
        """
        :ivar nLacre: Número do Lacre
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
