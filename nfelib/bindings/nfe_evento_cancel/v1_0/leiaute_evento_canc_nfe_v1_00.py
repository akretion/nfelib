from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bindings.nfe_evento_cancel.v1_0.tipos_basico_v1_03 import (
    Tamb,
    TcorgaoIbge,
)
from nfelib.bindings.nfe_evento_cancel.v1_0.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class DetEventoDescEvento(Enum):
    CANCELAMENTO = "Cancelamento"


class DetEventoVersao(Enum):
    VALUE_1_00 = "1.00"


class InfEventoTpEvento(Enum):
    VALUE_110111 = "110111"


class InfEventoVerEvento(Enum):
    VALUE_1_00 = "1.00"


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
            "pattern": r"1\.00",
        }
    )

    @dataclass
    class InfEvento:
        """
        :ivar cOrgao: Código do órgão de recepção do Evento. Utilizar a
            Tabela do IBGE extendida, utilizar 91 para identificar o
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
        :ivar detEvento: Schema XML de validação do evento do
            cancelamento 1101111
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
                "white_space": "preserve",
                "pattern": r"(1[1-7]|2[1-9]|3[1,2,3,5]|4[1-3]|5[0-3])(0[6-9]|[1-9][\d])(0[1-9]|1[0-2])([\d]{14})([\d]{5})([\d]{9})([\d]{10})",
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
        tpEvento: Optional[InfEventoTpEvento] = field(
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
                "pattern": r"[1-9]|[1][0-9]{0,1}|20",
            }
        )
        verEvento: Optional[InfEventoVerEvento] = field(
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
            """
            :ivar descEvento: Descrição do Evento - “Cancelamento”
            :ivar nProt: Número do Protocolo de Status da NF-e. 1
                posição (1 – Secretaria de Fazenda Estadual 2 – Receita
                Federal); 2 posições ano; 10 seqüencial no ano.
            :ivar xJust: Justificativa do cancelamento
            :ivar versao:
            """
            descEvento: Optional[DetEventoDescEvento] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            nProt: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{15}",
                }
            )
            xJust: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "min_length": 15,
                    "max_length": 255,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
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
            "pattern": r"1\.00",
        }
    )

    @dataclass
    class InfEvento:
        """
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar verAplic: Versão do Aplicativo que recebeu o Evento
        :ivar cOrgao: Código do órgão de recepção do Evento. Utilizar a
            Tabela do IBGE extendida, utilizar 91 para identificar o
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
        :ivar dhRegEvento: Data e Hora de do recebimento do evento ou do
            registro do evento formato UTC AAAA-MM-DDThh:mm:ssTZD.
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
                "white_space": "preserve",
                "pattern": r"(1[1-7]|2[1-9]|3[1,2,3,5]|4[1-3]|5[0-3])(0[6-9]|[1-9][\d])(0[1-9]|1[0-2])([\d]{14})([\d]{5})([\d]{9})([\d]{10})",
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
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d-0[1-4]:00",
            }
        )
        nProt: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
class TenvEvento:
    """
    Tipo Lote de Envio.
    """
    class Meta:
        name = "TEnvEvento"

    idLote: Optional[str] = field(
        default=None,
        metadata={
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
            "pattern": r"1\.00",
        }
    )


@dataclass
class TretEnvEvento:
    """
    Tipo Retorno de Lote de Envio.

    :ivar idLote:
    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar verAplic: Versão do Aplicativo que recebeu o Evento
    :ivar cOrgao: Código do òrgao que registrou o Evento
    :ivar cStat: Código do status da registro do Evento
    :ivar xMotivo: Descrição literal do status do registro do Evento
    :ivar retEvento:
    :ivar versao:
    """
    class Meta:
        name = "TRetEnvEvento"

    idLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,15}",
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
    retEvento: List[TretEvento] = field(
        default_factory=list,
        metadata={
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
