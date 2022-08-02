from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional
from xsdata.models.datatype import XmlDateTime
from nfelib.bindings.nfe_cons.v2_0.tipos_basico_v1_03 import (
    Tamb,
    TcodUfIbge,
)
from nfelib.bindings.nfe_cons.v2_0.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class TcorgaoIbge(Enum):
    """
    Tipo Código de orgão (UF da tabela do IBGE + 91 RFB)
    """
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_31 = "31"
    VALUE_32 = "32"
    VALUE_33 = "33"
    VALUE_35 = "35"
    VALUE_41 = "41"
    VALUE_42 = "42"
    VALUE_43 = "43"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_90 = "90"
    VALUE_91 = "91"


class TconsSitNfeXServ(Enum):
    CONSULTAR = "CONSULTAR"


class TverCancNfeV200107(Enum):
    """Tipo Versão do leiaute de Cancelamento de NF-e - 2.00/1.07"""
    VALUE_2_00 = "2.00"
    VALUE_1_07 = "1.07"


class TverConsSitNfe(Enum):
    """Tipo Versão do Leiaute da Cosulta situação NF-e - 2.01"""
    VALUE_2_01 = "2.01"


class TverEvento(Enum):
    """
    Tipo Versão do Evento 1.00.
    """
    VALUE_1_00 = "1.00"


class TverNfe(Enum):
    """Tipo Versão da NF-e - 2.00/1.10/1.07"""
    VALUE_2_00 = "2.00"
    VALUE_1_10 = "1.10"
    VALUE_1_07 = "1.07"


@dataclass
class TconsSitNfe:
    """
    Tipo Pedido de Consulta da Situação Atual da Nota Fiscal Eletrônica.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar x_serv: Serviço Solicitado
    :ivar ch_nfe: Chaves de acesso da NF-e, compostas por: UF do
        emitente, AAMM da emissão da NFe, CNPJ do emitente, modelo,
        série e número da NF-e e código numérico + DV.
    :ivar versao:
    """
    class Meta:
        name = "TConsSitNFe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    x_serv: Optional[TconsSitNfeXServ] = field(
        default=None,
        metadata={
            "name": "xServ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
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
    versao: Optional[TverConsSitNfe] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


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
    versao: Optional[TverEvento] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class InfEvento:
        """
        :ivar c_orgao: Código do órgão de recepção do Evento. Utilizar a
            Tabela do IBGE extendida, utilizar 90 para identificar o
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
        :ivar det_evento: Detalhe Específico do Evento
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
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d-0[1-4]:00",
            }
        )
        tp_evento: Optional[str] = field(
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
                "pattern": r"[1-9][0-9]{0,1}",
            }
        )
        ver_evento: Optional[str] = field(
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
            any_element: List[object] = field(
                default_factory=list,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                }
            )
            any_attributes: Dict[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                }
            )


@dataclass
class TprotNfe:
    """
    Tipo Protocolo de status resultado do processamento da NF-e.

    :ivar inf_prot: Dados do protocolo de status
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TProtNFe"

    inf_prot: Optional["TprotNfe.InfProt"] = field(
        default=None,
        metadata={
            "name": "infProt",
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
    versao: Optional[TverNfe] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class InfProt:
        """
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar ver_aplic: Versão do Aplicativo que processou a NF-e
        :ivar ch_nfe: Chaves de acesso da NF-e, compostas por: UF do
            emitente, AAMM da emissão da NFe, CNPJ do emitente, modelo,
            série e número da NF-e e código numérico+DV.
        :ivar dh_recbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS. Deve ser preenchida com data e hora da
            gravação no Banco em caso de Confirmação. Em caso de
            Rejeição, com data e hora do recebimento do Lote de NF-e
            enviado.
        :ivar n_prot: Número do Protocolo de Status da NF-e. 1 posição
            (1 – Secretaria de Fazenda Estadual 2 – Receita Federal); 2
            - códiga da UF - 2 posições ano; 10 seqüencial no ano.
        :ivar dig_val: Digest Value da NF-e processada. Utilizado para
            conferir a integridade da NF-e original.
        :ivar c_stat: Código do status da mensagem enviada.
        :ivar x_motivo: Descrição literal do status do serviço
            solicitado.
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
        dh_recbto: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "dhRecbto",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
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
        dig_val: Optional[bytes] = field(
            default=None,
            metadata={
                "name": "digVal",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "format": "base64",
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
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
            }
        )


@dataclass
class TretCancNfeV200107:
    """
    Tipo retorno Pedido de Cancelamento da Nota Fiscal Eletrônica.

    :ivar inf_canc: Dados do Resultado do Pedido de Cancelamento da Nota
        Fiscal Eletrônica
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TRetCancNFe_v200107"

    inf_canc: Optional["TretCancNfeV200107.InfCanc"] = field(
        default=None,
        metadata={
            "name": "infCanc",
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
    versao: Optional[TverCancNfeV200107] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class InfCanc:
        """
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar ver_aplic: Versão do Aplicativo que processou o pedido de
            cancelamento
        :ivar c_stat: Código do status da mensagem enviada.
        :ivar x_motivo: Descrição literal do status do serviço
            solicitado.
        :ivar c_uf: código da UF de atendimento
        :ivar ch_nfe: Chaves de acesso da NF-e, compostas por: UF do
            emitente, AAMM da emissão da NFe, CNPJ do emitente, modelo,
            série e número da NF-e e código numérico + DV.
        :ivar dh_recbto: Data e hora de recebimento, no formato AAAA-MM-
            DDTHH:MM:SS. Deve ser preenchida com data e hora da gravação
            no Banco em caso de Confirmação.
        :ivar n_prot: Número do Protocolo de Status da NF-e. 1 posição
            (1 – Secretaria de Fazenda Estadual 2 – Receita Federal); 2
            - código da UF - 2 posições ano; 10 seqüencial no ano.
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
        c_uf: Optional[TcodUfIbge] = field(
            default=None,
            metadata={
                "name": "cUF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
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
        dh_recbto: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "dhRecbto",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
    versao: Optional[TverEvento] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class InfEvento:
        """
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar ver_aplic: Versão do Aplicativo que recebeu o Evento
        :ivar c_orgao: Código do órgão de recepção do Evento. Utilizar a
            Tabela do IBGE extendida, utilizar 90 para identificar o
            Ambiente Nacional
        :ivar c_stat: Código do status da registro do Evento
        :ivar x_motivo: Descrição literal do status do registro do
            Evento
        :ivar ch_nfe: Chave de Acesso NF-e vinculada
        :ivar tp_evento: Tipo do Evento vinculado
        :ivar x_evento: Descrição do Evento
        :ivar n_seq_evento: Seqüencial do evento
        :ivar cnpjdest: CNPJ Destinatário
        :ivar cpfdest: CPF Destiantário
        :ivar email_dest: email do destinatário
        :ivar dh_reg_evento: Data e Hora de registro do evento formato
            UTC AAAA-MM-DDTHH:MM:SSTZD
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
        tp_evento: Optional[str] = field(
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
        cnpjdest: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJDest",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r"[0-9]{0}|[0-9]{14}",
            }
        )
        cpfdest: Optional[str] = field(
            default=None,
            metadata={
                "name": "CPFDest",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"[0-9]{11}",
            }
        )
        email_dest: Optional[str] = field(
            default=None,
            metadata={
                "name": "emailDest",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "min_length": 1,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
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
    versao: Optional[TverEvento] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TretConsSitNfe:
    """
    Tipo Retorno de Pedido de Consulta da Situação Atual da Nota Fiscal
    Eletrônica.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que processou a NF-e
    :ivar c_stat: Código do status da mensagem enviada.
    :ivar x_motivo: Descrição literal do status do serviço solicitado.
    :ivar c_uf: código da UF de atendimento
    :ivar ch_nfe: Chaves de acesso da NF-e consultada
    :ivar prot_nfe: Protocolo de autorização de uso da NF-e
    :ivar ret_canc_nfe: Protocolo de homologação de cancelamento de uso
        da NF-e
    :ivar proc_evento_nfe: Protocolo de registro de evento da NF-e
    :ivar versao:
    """
    class Meta:
        name = "TRetConsSitNFe"

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
    c_uf: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
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
    prot_nfe: Optional[TprotNfe] = field(
        default=None,
        metadata={
            "name": "protNFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    ret_canc_nfe: Optional[TretCancNfeV200107] = field(
        default=None,
        metadata={
            "name": "retCancNFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    proc_evento_nfe: List[TprocEvento] = field(
        default_factory=list,
        metadata={
            "name": "procEventoNFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    versao: Optional[TverConsSitNfe] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
