from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from nfelib.bindings.nfe_dist_dfe.v1_0.tipos_dist_dfe_v1_01 import TcorgaoIbge

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class TverResEvento(Enum):
    """
    Tipo Versão do leiate resNFe.
    """
    VALUE_1_01 = "1.01"


@dataclass
class ResEvento:
    """
    Schema da estrutura XML gerada pelo Ambiente Nacional com o conjunto de
    informações resumidas de um evento de NF-e.

    :ivar c_orgao: Código do órgão de recepção do Evento. Utilizar a
        Tabela do IBGE extendida, utilizar 91 para identificar o
        Ambiente Nacional
    :ivar cnpj: CNPJ do Emitente
    :ivar cpf: CPF do Emitente
    :ivar ch_nfe: Chave de acesso da NF-e
    :ivar dh_evento: Data e Hora do Evento, formato UTC (AAAA-MM-
        DDThh:mm:ssTZD, onde TZD = +hh:mm ou -hh:mm)
    :ivar tp_evento: Tipo do Evento
    :ivar n_seq_evento: Seqüencial do evento para o mesmo tipo de
        evento.  Para maioria dos eventos será 1, nos casos em que possa
        existir mais de um evento, como é o caso da carta de correção, o
        autor do evento deve numerar de forma seqüencial
    :ivar x_evento: Descrição do Evento
    :ivar dh_recbto: Data e hora de autorização do evento no formato
        AAAA-MM-DDTHH:MM:SSTZD
    :ivar n_prot: Número do Protocolo do evento. 1 posição (1 –
        Secretaria de Fazenda Estadual 2 – Receita Federal); 2 - códiga
        da UF - 2 posições ano; 10 seqüencial no ano
    :ivar versao:
    """
    class Meta:
        name = "resEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    c_orgao: Optional[TcorgaoIbge] = field(
        default=None,
        metadata={
            "name": "cOrgao",
            "type": "Element",
            "required": True,
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Element",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    ch_nfe: Optional[str] = field(
        default=None,
        metadata={
            "name": "chNFe",
            "type": "Element",
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
            "required": True,
            "white_space": "preserve",
            "pattern": r"[1-9][0-9]{0,1}",
        }
    )
    x_evento: Optional[str] = field(
        default=None,
        metadata={
            "name": "xEvento",
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    dh_recbto: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhRecbto",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    n_prot: Optional[str] = field(
        default=None,
        metadata={
            "name": "nProt",
            "type": "Element",
            "required": True,
            "max_length": 15,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    versao: Optional[TverResEvento] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
