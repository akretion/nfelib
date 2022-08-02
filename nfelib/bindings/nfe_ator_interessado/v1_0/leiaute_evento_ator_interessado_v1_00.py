from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bindings.nfe_ator_interessado.v1_0.tipos_basico_v1_03 import (
    Tamb,
    TcorgaoIbge,
    TcodUfIbge,
)
from nfelib.bindings.nfe_ator_interessado.v1_0.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class DetEventoDescEvento(Enum):
    ATOR_INTERESSADO_NA_NF_E = "Ator interessado na NF-e"


class DetEventoTpAutor(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class DetEventoTpAutorizacao(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class DetEventoVersao(Enum):
    VALUE_1_00 = "1.00"


class DetEventoXCondUso(Enum):
    O_EMITENTE_OU_DESTINAT_RIO_DA_NF_E_DECLARA_QUE_PERMITE_O_TRANSPORTADOR_DECLARADO_NO_CAMPO_CNPJ_CPF_DESTE_EVENTO_A_AUTORIZAR_OS_TRANSPORTADORES_SUBCONTRATADOS_OU_REDESPACHADOS_A_TEREM_ACESSO_AO_DOWNLOAD_DA_NF_E = "O emitente ou destinatário da NF-e, declara que permite o transportador declarado no campo CNPJ/CPF deste evento a autorizar os transportadores subcontratados ou redespachados a terem acesso ao download da NF-e"


class InfEventoTpEvento(Enum):
    VALUE_110150 = "110150"


class InfEventoVerEvento(Enum):
    VALUE_1_00 = "1.00"


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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "pattern": r"1\.00",
        }
    )

    @dataclass
    class InfEvento:
        """
        :ivar c_orgao: Código do órgão de recepção do Evento. Utilizar a
            Tabela do IBGE extendida, utilizar 91 para identificar o
            Ambiente Nacional
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar cnpj: CNPJ
        :ivar cpf: CPF
        :ivar ch_nfe: Chave de Acesso da NF-e vinculada ao evento
        :ivar dh_evento: Data e Hora do Evento, formato UTC (AAAA-MM-
            DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)
        :ivar tp_evento: Tipo do Evento
        :ivar n_seq_evento: Seqüencial do evento para o mesmo tipo de
            evento.  Para maioria dos eventos será 1, nos casos em que
            possa existir mais de um evento, como é o caso da carta de
            correção, o autor do evento deve numerar de forma
            seqüencial.
        :ivar ver_evento: Versão do Tipo do Evento
        :ivar det_evento: Schema XML de validação do evento de Ator
            Interessado na NF-e - Transportador (110150)”
        :ivar id: Identificador da TAG a ser assinada, a regra de
            formação do Id é: “ID” + tpEvento +  chave da NF-e +
            nSeqEvento
        """
        c_orgao: Optional[TcorgaoIbge] = field(
            default=None,
            metadata={
                "name": "cOrgao",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        cnpj: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJ",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r"[0-9]{0}|[0-9]{14}",
            }
        )
        cpf: Optional[str] = field(
            default=None,
            metadata={
                "name": "CPF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"[0-9]{11}",
            }
        )
        ch_nfe: Optional[str] = field(
            default=None,
            metadata={
                "name": "chNFe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        dh_evento: Optional[str] = field(
            default=None,
            metadata={
                "name": "dhEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        tp_evento: Optional[InfEventoTpEvento] = field(
            default=None,
            metadata={
                "name": "tpEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[1-9]|[1][0-9]{0,1}|20",
            }
        )
        ver_evento: Optional[InfEventoVerEvento] = field(
            default=None,
            metadata={
                "name": "verEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
            }
        )
        det_evento: Optional["Tevento.InfEvento.DetEvento"] = field(
            default=None,
            metadata={
                "name": "detEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
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
            :ivar desc_evento: Descrição do Evento - "Ator interessado
                na NF-e”"
            :ivar c_orgao_autor:
            :ivar tp_autor: Tipo do Órgão Autor do Evento. Informar uma
                das opções 1=Geração do Evento pelo Emitente; 2=Geração
                do Evento pelo Destinatário; 3=Geração do Evento pelo
                Transportador Outros valores: 1=Empresa Emitente,
                2=Empresa destinatária; 3=Empresa; 5=Fisco; 6=RFB;
                9=Outros Órgãos;
            :ivar ver_aplic: Versão do aplicativo do Autor do Evento.
            :ivar aut_xml: Pessoas autorizadas a acessar o XML da NF-e
            :ivar tp_autorizacao: 0 – Não permite; 1 – Permite o
                transportador autorizado pelo emitente ou destinatário
                autorizar outros transportadores para ter acesso ao
                download da NF-e
            :ivar x_cond_uso: Texto Fixo com as Condição de uso do tipo
                de autorização para o transportador:
            :ivar versao:
            """
            desc_evento: Optional[DetEventoDescEvento] = field(
                default=None,
                metadata={
                    "name": "descEvento",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            c_orgao_autor: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "name": "cOrgaoAutor",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            tp_autor: Optional[DetEventoTpAutor] = field(
                default=None,
                metadata={
                    "name": "tpAutor",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            ver_aplic: Optional[str] = field(
                default=None,
                metadata={
                    "name": "verAplic",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            aut_xml: Optional["Tevento.InfEvento.DetEvento.AutXml"] = field(
                default=None,
                metadata={
                    "name": "autXML",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            tp_autorizacao: Optional[DetEventoTpAutorizacao] = field(
                default=None,
                metadata={
                    "name": "tpAutorizacao",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                }
            )
            x_cond_uso: Optional[DetEventoXCondUso] = field(
                default=None,
                metadata={
                    "name": "xCondUso",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                }
            )
            versao: Optional[DetEventoVersao] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                }
            )

            @dataclass
            class AutXml:
                cnpj: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CNPJ",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{14}",
                    }
                )
                cpf: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CPF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{11}",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "pattern": r"1\.00",
        }
    )

    @dataclass
    class InfEvento:
        """
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar ver_aplic: Versão do Aplicativo que recebeu o Evento
        :ivar c_orgao: Código do órgão de recepção do Evento. Utilizar a
            Tabela do IBGE extendida, utilizar 91 para identificar o
            Ambiente Nacional
        :ivar c_stat: Código do status da registro do Evento
        :ivar x_motivo: Descrição literal do status do registro do
            Evento
        :ivar ch_nfe: Chave de Acesso NF-e vinculada
        :ivar tp_evento: Tipo do Evento vinculado
        :ivar x_evento: Descrição do Evento
        :ivar n_seq_evento: Seqüencial do evento
        :ivar c_orgao_autor: Código do Órgão Autor do Evento. Informar o
            Código da UF para este Evento.
        :ivar dh_reg_evento: Data e Hora de do recebimento do evento ou
            do registro do evento formato UTC AAAA-MM-DDThh:mm:ssTZD.
        :ivar n_prot: Número do protocolo de registro do evento
        :ivar id:
        """
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        ver_aplic: Optional[str] = field(
            default=None,
            metadata={
                "name": "verAplic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        c_stat: Optional[str] = field(
            default=None,
            metadata={
                "name": "cStat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        ch_nfe: Optional[str] = field(
            default=None,
            metadata={
                "name": "chNFe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        tp_evento: Optional[InfEventoTpEvento] = field(
            default=None,
            metadata={
                "name": "tpEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"[0-9]{6}",
            }
        )
        x_evento: Optional[str] = field(
            default=None,
            metadata={
                "name": "xEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "min_length": 5,
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
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"[1-9][0-9]{0,1}",
            }
        )
        c_orgao_autor: Optional[TcodUfIbge] = field(
            default=None,
            metadata={
                "name": "cOrgaoAutor",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        dh_reg_evento: Optional[str] = field(
            default=None,
            metadata={
                "name": "dhRegEvento",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d-0[1-4]:00",
            }
        )
        n_prot: Optional[str] = field(
            default=None,
            metadata={
                "name": "nProt",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
class TenvEvento:
    """
    Tipo Lote de Envio.
    """
    class Meta:
        name = "TEnvEvento"

    id_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "idLote",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,15}",
        }
    )
    evento: List[Tevento] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "min_occurs": 1,
            "max_occurs": 20,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"1\.00",
        }
    )


@dataclass
class TprocEvento:
    """
    Tipo procEvento.
    """
    class Meta:
        name = "TProcEvento"

    evento: Optional[Tevento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    ret_evento: Optional[TretEvento] = field(
        default=None,
        metadata={
            "name": "retEvento",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"1\.00",
        }
    )


@dataclass
class TretEnvEvento:
    """
    Tipo Retorno de Lote de Envio.

    :ivar id_lote:
    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que recebeu o Evento
    :ivar c_orgao: Código do òrgao que registrou o Evento
    :ivar c_stat: Código do status da registro do Evento
    :ivar x_motivo: Descrição literal do status do registro do Evento
    :ivar ret_evento:
    :ivar versao:
    """
    class Meta:
        name = "TRetEnvEvento"

    id_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "idLote",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,15}",
        }
    )
    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    c_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "cStat",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    ret_evento: List[TretEvento] = field(
        default_factory=list,
        metadata={
            "name": "retEvento",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "max_occurs": 20,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"1\.00",
        }
    )
