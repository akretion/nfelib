from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.w3.org/2000/09/xmldsig#"


@dataclass
class SignatureValueType:
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
class KeyInfoType:
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
