from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from nfelib.bindings.nfe_epec.v1_0.leiaute_epec_v1_00 import DetEventoVersao
from nfelib.bindings.nfe_epec.v1_0.tipos_basico_v1_03 import (
    TcodUfIbge,
    Tuf,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class Ie:
    """Informar a IE.

    Para IE do destinatário somente quando o contribuinte possuir uma
    inscrição estadual
    """
    class Meta:
        name = "IE"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    value: str = field(
        default="",
        metadata={
            "white_space": "preserve",
            "pattern": r"[0-9]{2,14}",
        }
    )


class DescEventoValue(Enum):
    EPEC = "EPEC"


@dataclass
class DhEmi:
    """Data de emissão no formato UTC.

    AAAA-MM-DDThh:mm:ssTZD
    """
    class Meta:
        name = "dhEmi"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )


class TpAutorValue(Enum):
    VALUE_1 = "1"


class TpNfValue(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


@dataclass
class VIcms:
    """
    Valor total do ICMS.
    """
    class Meta:
        name = "vICMS"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass
class VNf:
    """
    Valor total da NF-e.
    """
    class Meta:
        name = "vNF"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass
class VSt:
    """
    Valor total do ICMS de Substituição Tributária.
    """
    class Meta:
        name = "vST"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )


@dataclass
class VerAplic:
    """
    Versão do Aplicativo do Autor do Evento.
    """
    class Meta:
        name = "verAplic"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class Uf:
    """Sigla UF do destinatário.

    Informar "EX" no caso de operação com o exterior
    """
    class Meta:
        name = "UF"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    value: Optional[Tuf] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class COrgaoAutor:
    class Meta:
        name = "cOrgaoAutor"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    value: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class DescEvento:
    class Meta:
        name = "descEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    value: Optional[DescEventoValue] = field(
        default=None,
        metadata={
            "white_space": "preserve",
        }
    )


@dataclass
class DetEvento:
    class Meta:
        name = "detEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    descEvento: Optional[DescEventoValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    cOrgaoAutor: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tpAutor: Optional[TpAutorValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    verAplic: Optional[str] = field(
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
    dhEmi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    tpNF: Optional[TpNfValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    IE: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{2,14}",
        }
    )
    dest: Optional["DetEvento.Dest"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
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
    class Dest:
        """
        :ivar UF:
        :ivar CNPJ:
        :ivar CPF:
        :ivar idEstrangeiro: Identificador do destinatário, em caso de
            comprador estrangeiro
        :ivar IE:
        :ivar vNF:
        :ivar vICMS:
        :ivar vST:
        """
        UF: Optional[Tuf] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
        CNPJ: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{14}",
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
        idEstrangeiro: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"([!-ÿ]{0}|[!-ÿ]{5,20})?",
            }
        )
        IE: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{2,14}",
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
        vICMS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        vST: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )


@dataclass
class TpAutor:
    """Neste evento, aceitar apenas 1.

    1=Empresa Emitente; 2=Empresa Destinatária; 3=Empresa; 5=Fisco;
    6=RFB; 9=Outros Órgãos
    """
    class Meta:
        name = "tpAutor"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    value: Optional[TpAutorValue] = field(
        default=None,
        metadata={
            "white_space": "preserve",
        }
    )


@dataclass
class TpNf:
    """Tipo do Documento Fiscal (0 - entrada; 1 - saída)"""
    class Meta:
        name = "tpNF"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    value: Optional[TpNfValue] = field(
        default=None,
        metadata={
            "white_space": "preserve",
        }
    )
