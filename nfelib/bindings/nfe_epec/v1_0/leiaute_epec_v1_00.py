from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


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


class Tamb(Enum):
    """
    Tipo Ambiente.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"


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
    VALUE_91 = "91"


class TcodUfIbge(Enum):
    """
    Tipo Código da UF da tabela do IBGE.
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


class Tuf(Enum):
    """
    Tipo Sigla da UF.
    """
    AC = "AC"
    AL = "AL"
    AM = "AM"
    AP = "AP"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MG = "MG"
    MS = "MS"
    MT = "MT"
    PA = "PA"
    PB = "PB"
    PE = "PE"
    PI = "PI"
    PR = "PR"
    RJ = "RJ"
    RN = "RN"
    RO = "RO"
    RR = "RR"
    RS = "RS"
    SC = "SC"
    SE = "SE"
    SP = "SP"
    TO = "TO"
    EX = "EX"


class DescEventoValue(Enum):
    EPEC = "EPEC"


class DetEventoVersao(Enum):
    VALUE_1_00 = "1.00"


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


class InfEventoTpEvento(Enum):
    VALUE_110140 = "110140"


class InfEventoVerEvento(Enum):
    VALUE_1_00 = "1.00"


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
class SignatureValueType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        }
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class TtransformUri(Enum):
    HTTP_WWW_W3_ORG_2000_09_XMLDSIG_ENVELOPED_SIGNATURE = "http://www.w3.org/2000/09/xmldsig#enveloped-signature"
    HTTP_WWW_W3_ORG_TR_2001_REC_XML_C14N_20010315 = "http://www.w3.org/TR/2001/REC-xml-c14n-20010315"


@dataclass
class X509DataType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    X509Certificate: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
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


@dataclass
class KeyInfoType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    X509Data: Optional[X509DataType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class TransformType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    XPath: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    Algorithm: Optional[TtransformUri] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TransformsType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    transform: List[TransformType] = field(
        default_factory=list,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 2,
            "max_occurs": 2,
        }
    )


@dataclass
class ReferenceType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    transforms: Optional[TransformsType] = field(
        default=None,
        metadata={
            "name": "Transforms",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    digestMethod: Optional["ReferenceType.DigestMethod"] = field(
        default=None,
        metadata={
            "name": "DigestMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    digestValue: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "DigestValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
            "format": "base64",
        }
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    URI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "min_length": 2,
        }
    )
    Type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )

    @dataclass
    class DigestMethod:
        Algorithm: str = field(
            init=False,
            default="http://www.w3.org/2000/09/xmldsig#sha1",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class SignedInfoType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    canonicalizationMethod: Optional["SignedInfoType.CanonicalizationMethod"] = field(
        default=None,
        metadata={
            "name": "CanonicalizationMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    signatureMethod: Optional["SignedInfoType.SignatureMethod"] = field(
        default=None,
        metadata={
            "name": "SignatureMethod",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    reference: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class CanonicalizationMethod:
        Algorithm: str = field(
            init=False,
            default="http://www.w3.org/TR/2001/REC-xml-c14n-20010315",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SignatureMethod:
        Algorithm: str = field(
            init=False,
            default="http://www.w3.org/2000/09/xmldsig#rsa-sha1",
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass
class SignatureType:
    class Meta:
        target_namespace = "http://www.w3.org/2000/09/xmldsig#"

    signedInfo: Optional[SignedInfoType] = field(
        default=None,
        metadata={
            "name": "SignedInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    signatureValue: Optional[SignatureValueType] = field(
        default=None,
        metadata={
            "name": "SignatureValue",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    keyInfo: Optional[KeyInfoType] = field(
        default=None,
        metadata={
            "name": "KeyInfo",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Signature(SignatureType):
    class Meta:
        namespace = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class Tevento:
    """
    Tipo Evento.
    """
    class Meta:
        name = "TEvento"
        target_namespace = "http://www.portalfiscal.inf.br/nfe"

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
            evento.
        :ivar verEvento: Versão do Tipo do Evento
        :ivar detEvento: Schema XML de validação do evento de emissão
            prévia em contingência - 110140
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
            descEvento: Optional[DescEventoValue] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            cOrgaoAutor: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            tpAutor: Optional[TpAutorValue] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
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
            dhEmi: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tpNF: Optional[TpNfValue] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            dest: Optional["Tevento.InfEvento.DetEvento.Dest"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                :ivar idEstrangeiro: Identificador do destinatário, em
                    caso de comprador estrangeiro
                :ivar IE:
                :ivar vNF:
                :ivar vICMS:
                :ivar vST:
                """
                UF: Optional[Tuf] = field(
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
                        "white_space": "preserve",
                        "pattern": r"[0-9]{14}",
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
                idEstrangeiro: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"([!-ÿ]{0}|[!-ÿ]{5,20})?",
                    }
                )
                IE: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{2,14}",
                    }
                )
                vNF: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vICMS: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vST: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )


@dataclass
class TretEvento:
    """
    Tipo retorno do Evento.
    """
    class Meta:
        name = "TRetEvento"
        target_namespace = "http://www.portalfiscal.inf.br/nfe"

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
        :ivar cOrgaoAutor:
        :ivar dhRegEvento: Data e Hora de do recebimento do evento ou do
            registro do evento formato UTC AAAA-MM-DDThh:mm:ssTZD.
        :ivar nProt: Número do protocolo de registro do evento
        :ivar chNFePend: Relação de Chaves de Acesso de EPEC não
            conciliados (pendentes de conciliação) existentes no AN.
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
        cOrgaoAutor: Optional[TcodUfIbge] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        dhRegEvento: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d[\-,\+](0[0-9]|10|11|12):00",
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
        chNFePend: List[str] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_occurs": 50,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
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
        target_namespace = "http://www.portalfiscal.inf.br/nfe"

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
        target_namespace = "http://www.portalfiscal.inf.br/nfe"

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
        target_namespace = "http://www.portalfiscal.inf.br/nfe"

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
