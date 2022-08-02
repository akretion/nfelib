from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from nfelib.bindings.cte.v3_0.tipos_geral_cte_v3_00 import (
    Tamb,
    TcorgaoIbge,
)
from nfelib.bindings.cte.v3_0.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class TmodTransp(Enum):
    """
    Tipo Modal transporte.
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"


@dataclass
class Tevento:
    """
    Tipo Evento.
    """
    class Meta:
        name = "TEvento"

    inf_evento: Optional["Tevento.InfEvento"] = field(
        default=None,
        metadata={
            "name": "infEvento",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"3\.00",
        }
    )

    @dataclass
    class InfEvento:
        """
        :ivar c_orgao: Código do órgão de recepção do Evento. Utilizar a
            Tabela do IBGE extendida, utilizar 90 para identificar
            SUFRAMA
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar cnpj: CNPJ do emissor do evento
        :ivar cpf: CPF do emissor do evento Informar zeros não
            significativos. Usar com série específica 920-969 para
            emitente pessoa física com inscrição estadual
        :ivar ch_cte: Chave de Acesso do CT-e vinculado ao evento
        :ivar dh_evento: Data e Hora do Evento, formato UTC (AAAA-MM-
            DDThh:mm:ssTZD)
        :ivar tp_evento: Tipo do Evento
        :ivar n_seq_evento: Seqüencial do evento para o mesmo tipo de
            evento.  Para maioria dos eventos será 1, nos casos em que
            possa existir mais de um evento o autor do evento deve
            numerar de forma seqüencial.
        :ivar det_evento: Detalhamento do evento específico
        :ivar inf_solic_nff: Grupo de informações do pedido de registro
            de evento da Nota Fiscal Fácil
        :ivar id: Identificador da TAG a ser assinada, a regra de
            formação do Id é: “ID” + tpEvento +  chave do CT-e +
            nSeqEvento
        """
        c_orgao: Optional[TcorgaoIbge] = field(
            default=None,
            metadata={
                "name": "cOrgao",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        cnpj: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJ",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[0-9]{14}",
            }
        )
        cpf: Optional[str] = field(
            default=None,
            metadata={
                "name": "CPF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[0-9]{11}",
            }
        )
        ch_cte: Optional[str] = field(
            default=None,
            metadata={
                "name": "chCTe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        dh_evento: Optional[str] = field(
            default=None,
            metadata={
                "name": "dhEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        tp_evento: Optional[str] = field(
            default=None,
            metadata={
                "name": "tpEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{6}",
            }
        )
        n_seq_evento: Optional[str] = field(
            default=None,
            metadata={
                "name": "nSeqEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[1-9][0-9]|0?[1-9]",
            }
        )
        det_evento: Optional["Tevento.InfEvento.DetEvento"] = field(
            default=None,
            metadata={
                "name": "detEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        inf_solic_nff: Optional["Tevento.InfEvento.InfSolicNff"] = field(
            default=None,
            metadata={
                "name": "infSolicNFF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "required": True,
                "pattern": r"ID[0-9]{52}",
            }
        )

        @dataclass
        class DetEvento:
            """
            :ivar any_element: XML do evento Insira neste local o XML
                específico do tipo de evento (cancelamento,
                encerramento, registro de passagem).
            :ivar versao_evento:
            """
            any_element: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                }
            )
            versao_evento: Optional[str] = field(
                default=None,
                metadata={
                    "name": "versaoEvento",
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"3\.(0[0-9]|[1-9][0-9])",
                }
            )

        @dataclass
        class InfSolicNff:
            """
            :ivar x_solic: Solicitação do pedido de registro de evento
                da NFF. Será preenchido com a totalidade de campos
                informados no aplicativo emissor serializado.
            """
            x_solic: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xSolic",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )


@dataclass
class TretEvento:
    """
    Tipo retorno do Evento.
    """
    class Meta:
        name = "TRetEvento"

    inf_evento: Optional["TretEvento.InfEvento"] = field(
        default=None,
        metadata={
            "name": "infEvento",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"3\.00",
        }
    )

    @dataclass
    class InfEvento:
        """
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar ver_aplic: Versão do Aplicativo que recebeu o Evento
        :ivar c_orgao: Código do órgão de recepção do Evento. Utilizar a
            Tabela do IBGE extendida, utilizar 90 para identificar
            SUFRAMA
        :ivar c_stat: Código do status da registro do Evento
        :ivar x_motivo: Descrição literal do status do registro do
            Evento
        :ivar ch_cte: Chave de Acesso CT-e vinculado
        :ivar tp_evento: Tipo do Evento vinculado
        :ivar x_evento: Descrição do Evento
        :ivar n_seq_evento: Seqüencial do evento
        :ivar dh_reg_evento: Data e Hora de do recebimento do evento ou
            do registro do evento formato AAAA-MM-DDThh:mm:ssTZD
        :ivar n_prot: Número do protocolo de registro do evento
        :ivar id:
        """
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        ver_aplic: Optional[str] = field(
            default=None,
            metadata={
                "name": "verAplic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        c_orgao: Optional[TcorgaoIbge] = field(
            default=None,
            metadata={
                "name": "cOrgao",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        c_stat: Optional[str] = field(
            default=None,
            metadata={
                "name": "cStat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        x_motivo: Optional[str] = field(
            default=None,
            metadata={
                "name": "xMotivo",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        ch_cte: Optional[str] = field(
            default=None,
            metadata={
                "name": "chCTe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        tp_evento: Optional[str] = field(
            default=None,
            metadata={
                "name": "tpEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[0-9]{6}",
            }
        )
        x_evento: Optional[str] = field(
            default=None,
            metadata={
                "name": "xEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "min_length": 4,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        n_seq_evento: Optional[str] = field(
            default=None,
            metadata={
                "name": "nSeqEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[1-9][0-9]|0?[1-9]",
            }
        )
        dh_reg_evento: Optional[str] = field(
            default=None,
            metadata={
                "name": "dhRegEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        n_prot: Optional[str] = field(
            default=None,
            metadata={
                "name": "nProt",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "pattern": r"ID[0-9]{15}",
            }
        )


@dataclass
class TprocEvento:
    """
    Tipo procEvento.

    :ivar evento_cte:
    :ivar ret_evento_cte:
    :ivar versao:
    :ivar ip_transmissor: IP do transmissor do documento fiscal para o
        ambiente autorizador
    :ivar n_porta_con: Porta de origem utilizada na conexão (De 0 a
        65535)
    :ivar dh_conexao: Data e Hora da Conexão de Origem
    """
    class Meta:
        name = "TProcEvento"

    evento_cte: Optional[Tevento] = field(
        default=None,
        metadata={
            "name": "eventoCTe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    ret_evento_cte: Optional[TretEvento] = field(
        default=None,
        metadata={
            "name": "retEventoCTe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"3\.00",
        }
    )
    ip_transmissor: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipTransmissor",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])",
        }
    )
    n_porta_con: Optional[str] = field(
        default=None,
        metadata={
            "name": "nPortaCon",
            "type": "Attribute",
            "pattern": r"[0-9]{1,5}",
        }
    )
    dh_conexao: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhConexao",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
