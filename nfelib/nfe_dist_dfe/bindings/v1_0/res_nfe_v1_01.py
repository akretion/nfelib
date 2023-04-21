from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class TverResNfe(Enum):
    """
    Tipo Versão do leiate resNFe.
    """
    VALUE_1_01 = "1.01"


class ResNfeCSitNfe(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class ResNfeTpNf(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


@dataclass
class ResNfe:
    """
    Schema da estrutura XML gerada pelo Ambiente Nacional com o conjunto de
    informações resumidas de uma NF-e.

    :ivar chNFe: Chave de acesso da NF-e
    :ivar CNPJ: CNPJ do Emitente
    :ivar CPF: CPF do Emitente
    :ivar xNome: Razão Social ou Nome do emitente
    :ivar IE: Inscrição Estadual do Emitente
    :ivar dhEmi: Data e Hora de emissão do Documento Fiscal (AAAA-MM-
        DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00
    :ivar tpNF: Tipo do Documento Fiscal (0 - entrada; 1 - saída)
    :ivar vNF: Valor Total da NF-e
    :ivar digVal: Digest Value da NF-e processada. Utilizado para
        conferir a integridade da NF-e original
    :ivar dhRecbto: Data e hora de autorização da NF-e, no formato AAAA-
        MM-DDTHH:MM:SSTZD
    :ivar nProt: Número do Protocolo de Status da NF-e. 1 posição (1 –
        Secretaria de Fazenda Estadual 2 – Receita Federal); 2 - códiga
        da UF - 2 posições ano; 10 seqüencial no ano
    :ivar cSitNFe: Situação da NF-e 1-Uso autorizado no momento da
        consulta; 2-Uso denegado;
    :ivar versao:
    """
    class Meta:
        name = "resNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    chNFe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 44,
            "white_space": "preserve",
            "pattern": r"[0-9]{44}",
        }
    )
    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    CPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
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
            "required": True,
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{2,14}|ISENTO",
        }
    )
    dhEmi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    tpNF: Optional[ResNfeTpNf] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    vNF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    digVal: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "format": "base64",
        }
    )
    dhRecbto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    nProt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "max_length": 15,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    cSitNFe: Optional[ResNfeCSitNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    versao: Optional[TverResNfe] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
