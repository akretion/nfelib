from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional
from xsdata.models.datatype import XmlDateTime
from nfelib.nfe.bindings.v4_0.tipos_basico_v4_00 import (
    Tamb,
    TcorgaoIbge,
    TcodUfIbge,
)
from nfelib.nfe.bindings.v4_0.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class TconsSitNfeXServ(Enum):
    CONSULTAR = "CONSULTAR"


class TverConsSitNfe(Enum):
    """Tipo Versão do Leiaute da Cosulta situação NF-e - 4.00"""
    VALUE_4_00 = "4.00"


@dataclass
class TconsSitNfe:
    """
    Tipo Pedido de Consulta da Situação Atual da Nota Fiscal Eletrônica.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar xServ: Serviço Solicitado
    :ivar chNFe: Chaves de acesso da NF-e, compostas por: UF do
        emitente, AAMM da emissão da NFe, CNPJ do emitente, modelo,
        série e número da NF-e e código numérico + DV.
    :ivar versao:
    """
    class Meta:
        name = "TConsSitNFe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    xServ: Optional[TconsSitNfeXServ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    chNFe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "max_length": 44,
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

    infEvento: Optional["Tevento.InfEvento"] = field(
        default=None,
        metadata={
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
            "pattern": r"[1-9]{1}\.[0-9]{2}",
        }
    )

    @dataclass
    class InfEvento:
        """
        :ivar cOrgao: Código do órgão de recepção do Evento. Utilizar a
            Tabela do IBGE extendida, utilizar 90 para identificar o
            Ambiente Nacional
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar CNPJ: CNPJ
        :ivar CPF: CPF
        :ivar chNFe: Chave de Acesso da NF-e vinculada ao evento
        :ivar dhEvento: Data e Hora do Evento, formato UTC (AAAA-MM-
            DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)
        :ivar tpEvento: Tipo do Evento
        :ivar nSeqEvento: Seqüencial do evento para o mesmo tipo de
            evento.  Para maioria dos eventos será 1, nos casos em que
            possa existir mais de um evento, como é o caso da carta de
            correção, o autor do evento deve numerar de forma
            seqüencial.
        :ivar verEvento: Versão do Tipo do Evento
        :ivar detEvento: Detalhe Específico do Evento
        :ivar Id: Identificador da TAG a ser assinada, a regra de
            formação do Id é: “ID” + tpEvento +  chave da NF-e +
            nSeqEvento
        """
        cOrgao: Optional[TcorgaoIbge] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        tpAmb: Optional[Tamb] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        CNPJ: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r"[0-9]{0}|[0-9]{14}",
            }
        )
        CPF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 11,
                "white_space": "preserve",
                "pattern": r"[0-9]{11}",
            }
        )
        chNFe: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        dhEvento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        tpEvento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{6}",
            }
        )
        nSeqEvento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[1-9][0-9]{0,1}",
            }
        )
        verEvento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
            }
        )
        detEvento: Optional["Tevento.InfEvento.DetEvento"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        Id: Optional[str] = field(
            default=None,
            metadata={
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

    :ivar infProt: Dados do protocolo de status
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TProtNFe"

    infProt: Optional["TprotNfe.InfProt"] = field(
        default=None,
        metadata={
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
            "pattern": r"[1-9]{1}\.[0-9]{2}",
        }
    )

    @dataclass
    class InfProt:
        """
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar verAplic: Versão do Aplicativo que processou a NF-e
        :ivar chNFe: Chaves de acesso da NF-e, compostas por: UF do
            emitente, AAMM da emissão da NFe, CNPJ do emitente, modelo,
            série e número da NF-e e código numérico+DV.
        :ivar dhRecbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS (ou AAAA-MM-DDTHH:MM:SSTZD, de acordo com
            versão). Deve ser preenchida com data e hora da gravação no
            Banco em caso de Confirmação. Em caso de Rejeição, com data
            e hora do recebimento do Lote de NF-e enviado.
        :ivar nProt: Número do Protocolo de Status da NF-e. 1 posição (1
            – Secretaria de Fazenda Estadual 2 – Receita Federal); 2 -
            códiga da UF - 2 posições ano; 10 seqüencial no ano.
        :ivar digVal: Digest Value da NF-e processada. Utilizado para
            conferir a integridade da NF-e original.
        :ivar cStat: Código do status da mensagem enviada.
        :ivar xMotivo: Descrição literal do status do serviço
            solicitado.
        :ivar Id:
        """
        tpAmb: Optional[Tamb] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        verAplic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        chNFe: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        dhRecbto: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        nProt: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 15,
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        digVal: Optional[bytes] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "format": "base64",
            }
        )
        cStat: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "max_length": 3,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMotivo: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        Id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class TretCancNfe:
    """
    Tipo retorno Pedido de Cancelamento da Nota Fiscal Eletrônica.

    :ivar infCanc: Dados do Resultado do Pedido de Cancelamento da Nota
        Fiscal Eletrônica
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TRetCancNFe"

    infCanc: Optional["TretCancNfe.InfCanc"] = field(
        default=None,
        metadata={
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
            "pattern": r"[1-9]{1}\.[0-9]{2}",
        }
    )

    @dataclass
    class InfCanc:
        """
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar verAplic: Versão do Aplicativo que processou o pedido de
            cancelamento
        :ivar cStat: Código do status da mensagem enviada.
        :ivar xMotivo: Descrição literal do status do serviço
            solicitado.
        :ivar cUF: código da UF de atendimento
        :ivar chNFe: Chaves de acesso da NF-e, compostas por: UF do
            emitente, AAMM da emissão da NFe, CNPJ do emitente, modelo,
            série e número da NF-e e código numérico + DV.
        :ivar dhRecbto: Data e hora de recebimento, no formato AAAA-MM-
            DDTHH:MM:SS. Deve ser preenchida com data e hora da gravação
            no Banco em caso de Confirmação.
        :ivar nProt: Número do Protocolo de Status da NF-e. 1 posição (1
            – Secretaria de Fazenda Estadual 2 – Receita Federal); 2 -
            código da UF - 2 posições ano; 10 seqüencial no ano.
        :ivar Id:
        """
        tpAmb: Optional[Tamb] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        verAplic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        cStat: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "max_length": 3,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMotivo: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        cUF: Optional[TcodUfIbge] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        chNFe: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        dhRecbto: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        nProt: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 15,
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        Id: Optional[str] = field(
            default=None,
            metadata={
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

    infEvento: Optional["TretEvento.InfEvento"] = field(
        default=None,
        metadata={
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
            "pattern": r"[1-9]{1}\.[0-9]{2}",
        }
    )

    @dataclass
    class InfEvento:
        """
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar verAplic: Versão do Aplicativo que recebeu o Evento
        :ivar cOrgao: Código do órgão de recepção do Evento. Utilizar a
            Tabela do IBGE extendida, utilizar 90 para identificar o
            Ambiente Nacional
        :ivar cStat: Código do status da registro do Evento
        :ivar xMotivo: Descrição literal do status do registro do Evento
        :ivar chNFe: Chave de Acesso NF-e vinculada
        :ivar tpEvento: Tipo do Evento vinculado
        :ivar xEvento: Descrição do Evento
        :ivar nSeqEvento: Seqüencial do evento
        :ivar CNPJDest: CNPJ Destinatário
        :ivar CPFDest: CPF Destiantário
        :ivar emailDest: email do destinatário
        :ivar dhRegEvento: Data e Hora de registro do evento formato UTC
            AAAA-MM-DDTHH:MM:SSTZD
        :ivar nProt: Número do protocolo de registro do evento
        :ivar Id:
        """
        tpAmb: Optional[Tamb] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        verAplic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        cOrgao: Optional[TcorgaoIbge] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        cStat: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "max_length": 3,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMotivo: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        chNFe: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        tpEvento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"[0-9]{6}",
            }
        )
        xEvento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "min_length": 5,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        nSeqEvento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"[1-9][0-9]{0,1}",
            }
        )
        CNPJDest: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r"[0-9]{0}|[0-9]{14}",
            }
        )
        CPFDest: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 11,
                "white_space": "preserve",
                "pattern": r"[0-9]{11}",
            }
        )
        emailDest: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "min_length": 1,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        dhRegEvento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        nProt: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 15,
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        Id: Optional[str] = field(
            default=None,
            metadata={
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
    retEvento: Optional[TretEvento] = field(
        default=None,
        metadata={
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
            "pattern": r"[1-9]{1}\.[0-9]{2}",
        }
    )


@dataclass
class TretConsSitNfe:
    """
    Tipo Retorno de Pedido de Consulta da Situação Atual da Nota Fiscal Eletrônica.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar verAplic: Versão do Aplicativo que processou a NF-e
    :ivar cStat: Código do status da mensagem enviada.
    :ivar xMotivo: Descrição literal do status do serviço solicitado.
    :ivar cUF: código da UF de atendimento
    :ivar dhRecbto: AAAA-MM-DDTHH:MM:SSTZD
    :ivar chNFe: Chaves de acesso da NF-e consultada
    :ivar protNFe: Protocolo de autorização de uso da NF-e
    :ivar retCancNFe: Protocolo de homologação de cancelamento de uso da
        NF-e
    :ivar procEventoNFe: Protocolo de registro de evento da NF-e
    :ivar versao:
    """
    class Meta:
        name = "TRetConsSitNFe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cStat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "max_length": 3,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    dhRecbto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    chNFe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "max_length": 44,
            "white_space": "preserve",
            "pattern": r"[0-9]{44}",
        }
    )
    protNFe: Optional[TprotNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    retCancNFe: Optional[TretCancNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    procEventoNFe: List[TprocEvento] = field(
        default_factory=list,
        metadata={
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
