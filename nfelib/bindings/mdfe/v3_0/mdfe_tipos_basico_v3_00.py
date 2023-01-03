from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from nfelib.bindings.mdfe.v3_0.tipos_geral_mdfe_v3_00 import (
    Tamb,
    TcodUfIbge,
    Temit,
    TmodMd,
    Ttransp,
    Tuf,
    TtipoUnidCarga,
    TtipoUnidTransp,
)
from nfelib.bindings.mdfe.v3_0.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class TmodalMd(Enum):
    """
    Tipo Modal Manifesto.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


class TprocEmi(Enum):
    """
    Tipo processo de emissão do MDF-e.
    """
    VALUE_0 = "0"


@dataclass
class TrespTec:
    """
    Tipo Dados da Responsável Técnico.

    :ivar CNPJ: CNPJ da pessoa jurídica responsável técnica pelo sistema
        utilizado na emissão do documento fiscal eletrônico Informar o
        CNPJ da pessoa jurídica desenvolvedora do sistema utilizado na
        emissão do documento fiscal eletrônico.
    :ivar xContato: Nome da pessoa a ser contatada Informar o nome da
        pessoa a ser contatada na empresa desenvolvedora do sistema
        utilizado na emissão do documento fiscal eletrônico. No caso de
        pessoa física, informar o respectivo nome.
    :ivar email: Email da pessoa jurídica a ser contatada
    :ivar fone: Telefone da pessoa jurídica a ser contatada Preencher
        com o Código DDD + número do telefone.
    :ivar idCSRT: Identificador do código de segurança do responsável
        técnico Identificador do CSRT utilizado para geração do hash
    :ivar hashCSRT: Hash do token do código de segurança do responsável
        técnico O hashCSRT é o resultado das funções SHA-1 e base64 do
        token CSRT fornecido pelo fisco + chave de acesso do DF-e.
        (Implementação em futura NT) Observação: 28 caracteres são
        representados no schema como 20 bytes do tipo base64Binary
    """
    class Meta:
        name = "TRespTec"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    xContato: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 6,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[^@]+@[^\.]+\..+",
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7,12}",
        }
    )
    idCSRT: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "pattern": r"[0-9]{3}",
        }
    )
    hashCSRT: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "length": 20,
            "format": "base64",
        }
    )


class IdeIndCanalVerde(Enum):
    VALUE_1 = "1"


class IdeIndCarregaPosterior(Enum):
    VALUE_1 = "1"


class IdeTpEmis(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class InfCteIndReentrega(Enum):
    VALUE_1 = "1"


class InfMdfeTranspIndReentrega(Enum):
    VALUE_1 = "1"


class InfNfeIndReentrega(Enum):
    VALUE_1 = "1"


class InfRespRespSeg(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


class ProdPredTpCarga(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"


class TotCUnid(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"


@dataclass
class TendOrg:
    """
    Tipo Dados do Endereço.

    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar xMun: Nome do município, , informar EXTERIOR para operações
        com o exterior.
    :ivar CEP: CEP
    :ivar UF: Sigla da UF, , informar EX para operações com o exterior.
    :ivar cPais: Código do país
    :ivar xPais: Nome do país
    :ivar fone: Telefone
    """
    class Meta:
        name = "TEndOrg"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    cPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    xPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{7,10}",
        }
    )


@dataclass
class TendReEnt:
    """
    Tipo Dados do Local de Retirada ou Entrega.

    :ivar CNPJ: Número do CNPJ
    :ivar CPF: Número do CPF
    :ivar xNome: Razão Social ou Nome
    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar xMun: Nome do município, , informar EXTERIOR para operações
        com o exterior.
    :ivar UF: Sigla da UF, , informar EX para operações com o exterior.
    """
    class Meta:
        name = "TEndReEnt"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    CPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    xNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )


@dataclass
class TendeEmi:
    """
    Tipo Dados do Endereço.

    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar xMun: Nome do município, , informar EXTERIOR para operações
        com o exterior.
    :ivar CEP: CEP Informar zeros não significativos
    :ivar UF: Sigla da UF, , informar EX para operações com o exterior.
    :ivar fone: Telefone
    :ivar email: Endereço de E-mail
    """
    class Meta:
        name = "TEndeEmi"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{7,12}",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 6,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[^@]+@[^\.]+\..+",
        }
    )


@dataclass
class TenderFer:
    """
    Tipo Dados do Endereço.

    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar xMun: Nome do município, , informar EXTERIOR para operações
        com o exterior.
    :ivar CEP: CEP
    :ivar UF: Sigla da UF, , informar EX para operações com o exterior.
    """
    class Meta:
        name = "TEnderFer"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )


@dataclass
class Tendereco:
    """
    Tipo Dados do Endereço.

    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar xMun: Nome do município, informar EXTERIOR para operações com
        o exterior.
    :ivar CEP: CEP Informar os zeros não significativos
    :ivar UF: Sigla da UF, informar EX para operações com o exterior.
    :ivar cPais: Código do país Utilizar a tabela do BACEN
    :ivar xPais: Nome do país
    """
    class Meta:
        name = "TEndereco"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    cPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    xPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class Tendernac:
    """
    Tipo Dados do Endereço.

    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar xMun: Nome do município, , informar EXTERIOR para operações
        com o exterior.
    :ivar CEP: CEP
    :ivar UF: Sigla da UF, , informar EX para operações com o exterior.
    """
    class Meta:
        name = "TEndernac"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )


@dataclass
class Tlocal:
    """
    Tipo Dados do Local de Origem ou Destino.

    :ivar cMun: Código do município (utilizar a tabela do IBGE)
    :ivar xMun: Nome do município
    :ivar UF: Sigla da UF
    """
    class Meta:
        name = "TLocal"

    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )


@dataclass
class TnfeNf:
    """
    Tipo  de Dados das Notas Fiscais Papel e Eletrônica.

    :ivar infNFe: Informações da NF-e
    :ivar infNF: Informações da NF mod 1 e 1A
    """
    class Meta:
        name = "TNFeNF"

    infNFe: Optional["TnfeNf.InfNfe"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    infNF: Optional["TnfeNf.InfNf"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )

    @dataclass
    class InfNfe:
        """
        :ivar chNFe: Chave de acesso da NF-e
        :ivar PIN: PIN SUFRAMA PIN atribuído pela SUFRAMA para a
            operação.
        """
        chNFe: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        PIN: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "min_length": 2,
                "max_length": 9,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{1,8}",
            }
        )

    @dataclass
    class InfNf:
        """
        :ivar emi: Informações do Emitente da NF
        :ivar dest: Informações do Destinatário da NF
        :ivar serie: Série
        :ivar nNF: Número
        :ivar dEmi: Data de Emissão Formato AAAA-MM-DD
        :ivar vNF: Valor Total da NF
        :ivar PIN: PIN SUFRAMA PIN atribuído pela SUFRAMA para a
            operação.
        """
        emi: Optional["TnfeNf.InfNf.Emi"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
            }
        )
        dest: Optional["TnfeNf.InfNf.Dest"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
            }
        )
        serie: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "min_length": 1,
                "max_length": 3,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        nNF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        dEmi: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
            }
        )
        vNF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        PIN: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "min_length": 2,
                "max_length": 9,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{1,8}",
            }
        )

        @dataclass
        class Emi:
            """
            :ivar CNPJ: CNPJ do emitente
            :ivar xNome: Razão Social ou Nome
            :ivar UF: UF do Emitente Informar 'EX' para operações com o
                exterior.
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            UF: Optional[Tuf] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )

        @dataclass
        class Dest:
            """
            :ivar CNPJ: CNPJ do Destinatário Informar o CNPJ ou o CPF do
                destinatário, preenchendo os zeros não significativos.
                Não informar o conteúdo da TAG se a operação for
                realizada com o Exterior.
            :ivar CPF: CPF do Destinatário Informar os zeros não
                significativos.
            :ivar xNome: Razão Social ou Nome
            :ivar UF: UF do Destinatário Informar 'EX' para operações
                com o exterior.
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            UF: Optional[Tuf] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )


@dataclass
class TprotMdfe:
    """
    Tipo Protocolo de status resultado do processamento do MDF-e.

    :ivar infProt: Dados do protocolo de status
    :ivar infFisco: Mensagem do Fisco
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TProtMDFe"

    infProt: Optional["TprotMdfe.InfProt"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    infFisco: Optional["TprotMdfe.InfFisco"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
    class InfProt:
        """
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar verAplic: Versão do Aplicativo que processou a NF-3e
        :ivar chMDFe: Chave de acesso do MDF-e
        :ivar dhRecbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS TZD.
        :ivar nProt: Número do Protocolo de Status do MDF-e
        :ivar digVal: Digest Value do MDF-e processado. Utilizado para
            conferir a integridade do MDF-e original.
        :ivar cStat: Código do status do MDF-e
        :ivar xMotivo: Descrição literal do status do MDF-e.
        :ivar Id:
        """
        tpAmb: Optional[Tamb] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
            }
        )
        verAplic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        chMDFe: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        dhRecbto: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        nProt: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        digVal: Optional[bytes] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "format": "base64",
            }
        )
        cStat: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMotivo: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
    class InfFisco:
        """
        :ivar cMsg: Código do status da mensagem do fisco
        :ivar xMsg: Mensagem do Fisco
        """
        cMsg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMsg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )


@dataclass
class TretEnviMdfe:
    """
    Tipo Retorno do Recibo do Pedido de Autorização do MDF-e.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar cUF: Identificação da UF
    :ivar verAplic: Versão do Aplicativo que recebeu o Arquivo.
    :ivar cStat: Código do status da mensagem enviada.
    :ivar xMotivo: Descrição literal do status do serviço solicitado.
    :ivar infRec: Dados do Recibo do Arquivo
    :ivar versao:
    """
    class Meta:
        name = "TRetEnviMDFe"

    tpAmb: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    infRec: Optional["TretEnviMdfe.InfRec"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
    class InfRec:
        """
        :ivar nRec: Número do Recibo
        :ivar dhRecbto: Data e hora do recebimento, no formato AAAA-MM-
            DDTHH:MM:SS
        :ivar tMed: Tempo médio de resposta do serviço (em segundos) dos
            últimos 5 minutos
        """
        nRec: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        dhRecbto: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
            }
        )
        tMed: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "pattern": r"[0-9]{1,4}",
            }
        )


@dataclass
class TunidCarga:
    """
    Tipo Dados Unidade de Carga.

    :ivar tpUnidCarga: Tipo da Unidade de Carga 1 - Container; 2 - ULD;
        3 - Pallet; 4 - Outros;
    :ivar idUnidCarga: Identificação da Unidade de Carga Informar a
        identificação da unidade de carga, por exemplo: número do
        container.
    :ivar lacUnidCarga: Lacres das Unidades de Carga
    :ivar qtdRat: Quantidade rateada (Peso,Volume)
    """
    class Meta:
        name = "TUnidCarga"

    tpUnidCarga: Optional[TtipoUnidCarga] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    idUnidCarga: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[A-Z0-9]+",
        }
    )
    lacUnidCarga: List["TunidCarga.LacUnidCarga"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    qtdRat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,3}(\.[0-9]{2,3})?",
        }
    )

    @dataclass
    class LacUnidCarga:
        """
        :ivar nLacre: Número do lacre
        """
        nLacre: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )


@dataclass
class TretMdfe:
    """
    Tipo Retorno do Pedido de Autorização do MDF-e.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar cUF: Identificação da UF
    :ivar verAplic: Versão do Aplicativo que recebeu o Arquivo.
    :ivar cStat: Código do status da mensagem enviada.
    :ivar xMotivo: Descrição literal do status do serviço solicitado.
    :ivar protMDFe: Dados do Recibo do Arquivo
    :ivar versao:
    """
    class Meta:
        name = "TRetMDFe"

    tpAmb: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    protMDFe: Optional[TprotMdfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
class TunidadeTransp:
    """
    Tipo Dados Unidade de Transporte.

    :ivar tpUnidTransp: Tipo da Unidade de Transporte 1 - Rodoviário
        Tração; 2 - Rodoviário Reboque; 3 - Navio; 4 - Balsa; 5 -
        Aeronave; 6 - Vagão; 7 - Outros
    :ivar idUnidTransp: Identificação da Unidade de Transporte Informar
        a identificação conforme o tipo de unidade de transporte. Por
        exemplo: para rodoviário tração ou reboque deverá preencher com
        a placa do veículo.
    :ivar lacUnidTransp: Lacres das Unidades de Transporte
    :ivar infUnidCarga: Informações das Unidades de Carga
        (Containeres/ULD/Outros) Dispositivo de carga utilizada (Unit
        Load Device - ULD) significa todo tipo de contêiner de carga,
        vagão, contêiner de avião, palete de aeronave com rede ou palete
        de aeronave com rede sobre um iglu.
    :ivar qtdRat: Quantidade rateada (Peso,Volume)
    """
    class Meta:
        name = "TUnidadeTransp"

    tpUnidTransp: Optional[TtipoUnidTransp] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    idUnidTransp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[A-Z0-9]+",
        }
    )
    lacUnidTransp: List["TunidadeTransp.LacUnidTransp"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    infUnidCarga: List[TunidCarga] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    qtdRat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,3}(\.[0-9]{2,3})?",
        }
    )

    @dataclass
    class LacUnidTransp:
        """
        :ivar nLacre: Número do lacre
        """
        nLacre: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )


@dataclass
class Tmdfe:
    """
    Tipo Manifesto de Documentos Fiscais Eletrônicos.

    :ivar infMDFe: Informações do MDF-e
    :ivar infMDFeSupl: Informações suplementares do MDF-e
    :ivar signature:
    """
    class Meta:
        name = "TMDFe"

    infMDFe: Optional["Tmdfe.InfMdfe"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    infMDFeSupl: Optional["Tmdfe.InfMdfeSupl"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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

    @dataclass
    class InfMdfe:
        """
        :ivar ide: Identificação do MDF-e
        :ivar emit: Identificação do Emitente do Manifesto
        :ivar infModal: Informações do modal
        :ivar infDoc: Informações dos Documentos fiscais vinculados ao
            manifesto
        :ivar seg: Informações de Seguro da Carga
        :ivar prodPred: Produto predominante Informar a descrição do
            produto predominante
        :ivar tot: Totalizadores da carga transportada e seus documentos
            fiscais
        :ivar lacres: Lacres do MDF-e Preechimento opcional para os
            modais Rodoviário e Ferroviário
        :ivar autXML: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar infAdic: Informações Adicionais
        :ivar infRespTec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar infSolicNFF: Grupo de informações do pedido de emissão da
            Nota Fiscal Fácil
        :ivar versao: Versão do leiaute Ex: "3.00"
        :ivar Id: Identificador da tag a ser assinada Informar a chave
            de acesso do MDF-e e precedida do literal "MDFe"
        """
        ide: Optional["Tmdfe.InfMdfe.Ide"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
            }
        )
        emit: Optional["Tmdfe.InfMdfe.Emit"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
            }
        )
        infModal: Optional["Tmdfe.InfMdfe.InfModal"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
            }
        )
        infDoc: Optional["Tmdfe.InfMdfe.InfDoc"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
            }
        )
        seg: List["Tmdfe.InfMdfe.Seg"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
            }
        )
        prodPred: Optional["Tmdfe.InfMdfe.ProdPred"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
            }
        )
        tot: Optional["Tmdfe.InfMdfe.Tot"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
            }
        )
        lacres: List["Tmdfe.InfMdfe.Lacres"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
            }
        )
        autXML: List["Tmdfe.InfMdfe.AutXml"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "max_occurs": 10,
            }
        )
        infAdic: Optional["Tmdfe.InfMdfe.InfAdic"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
            }
        )
        infRespTec: Optional[TrespTec] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
            }
        )
        infSolicNFF: Optional["Tmdfe.InfMdfe.InfSolicNff"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
        Id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"MDFe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar cUF: Código da UF do emitente do MDF-e Código da UF do
                emitente do Documento Fiscal. Utilizar a Tabela do IBGE
                de código de unidades da federação.
            :ivar tpAmb: Tipo do Ambiente 1 - Produção 2 - Homologação
            :ivar tpEmit: Tipo do Emitente 1 - Prestador de serviço de
                transporte 2 - Transportador de Carga Própria 3 -
                Prestador de serviço de transporte que emitirá CT-e
                Globalizado OBS: Deve ser preenchido com 2 para
                emitentes de NF-e e pelas transportadoras quando
                estiverem fazendo transporte de carga própria. Deve ser
                preenchido com 3 para transportador de carga que emitirá
                à posteriori CT-e Globalizado relacionando as NF-e.
            :ivar tpTransp: Tipo do Transportador 1 - ETC 2 - TAC 3 -
                CTC
            :ivar mod: Modelo do Manifesto Eletrônico Utilizar o código
                58 para identificação do MDF-e
            :ivar serie: Série do Manifesto Informar a série do
                documento fiscal (informar zero se inexistente). Série
                na faixa [920-969]: Reservada para emissão por
                contribuinte pessoa física com inscrição estadual.
            :ivar nMDF: Número do Manifesto Número que identifica o
                Manifesto. 1 a 999999999.
            :ivar cMDF: Código numérico que compõe a Chave de Acesso.
                Código aleatório gerado pelo emitente, com o objetivo de
                evitar acessos indevidos ao documento.
            :ivar cDV: Digito verificador da chave de acesso do
                Manifesto Informar o dígito  de controle da chave de
                acesso do MDF-e, que deve ser calculado com a aplicação
                do algoritmo módulo 11 (base 2,9) da chave de acesso.
            :ivar modal: Modalidade de transporte 1 - Rodoviário; 2 -
                Aéreo; 3 - Aquaviário; 4 - Ferroviário.
            :ivar dhEmi: Data e hora de emissão do Manifesto Formato
                AAAA-MM-DDTHH:MM:DD TZD
            :ivar tpEmis: Forma de emissão do Manifesto 1 - Normal ; 2 -
                Contingência; 3-Regime Especial NFF
            :ivar procEmi: Identificação do processo de emissão do
                Manifesto 0 - emissão de MDF-e com aplicativo do
                contribuinte
            :ivar verProc: Versão do processo de emissão Informar a
                versão do aplicativo emissor de MDF-e.
            :ivar UFIni: Sigla da UF do Carregamento Utilizar a Tabela
                do IBGE de código de unidades da federação. Informar
                'EX' para operações com o exterior.
            :ivar UFFim: Sigla da UF do Descarregamento Utilizar a
                Tabela do IBGE de código de unidades da federação.
                Informar 'EX' para operações com o exterior.
            :ivar infMunCarrega: Informações dos Municípios de
                Carregamento
            :ivar infPercurso: Informações do Percurso do MDF-e
            :ivar dhIniViagem: Data e hora previstos de inicio da viagem
                Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar indCanalVerde: Indicador de participação do Canal
                Verde
            :ivar indCarregaPosterior: Indicador de MDF-e com inclusão
                da Carga posterior a emissão por evento de inclusão de
                DF-e
            """
            cUF: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            tpAmb: Optional[Tamb] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            tpEmit: Optional[Temit] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            tpTransp: Optional[Ttransp] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                }
            )
            mod: Optional[TmodMd] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            serie: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                }
            )
            nMDF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            cMDF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            cDV: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
                }
            )
            modal: Optional[TmodalMd] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            dhEmi: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tpEmis: Optional[IdeTpEmis] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            procEmi: Optional[TprocEmi] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            verProc: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            UFIni: Optional[Tuf] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            UFFim: Optional[Tuf] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            infMunCarrega: List["Tmdfe.InfMdfe.Ide.InfMunCarrega"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "min_occurs": 1,
                    "max_occurs": 50,
                }
            )
            infPercurso: List["Tmdfe.InfMdfe.Ide.InfPercurso"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "max_occurs": 25,
                }
            )
            dhIniViagem: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            indCanalVerde: Optional[IdeIndCanalVerde] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                }
            )
            indCarregaPosterior: Optional[IdeIndCarregaPosterior] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                }
            )

            @dataclass
            class InfMunCarrega:
                """
                :ivar cMunCarrega: Código do Município de Carregamento
                :ivar xMunCarrega: Nome do Município de Carregamento
                """
                cMunCarrega: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7}",
                    }
                )
                xMunCarrega: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )

            @dataclass
            class InfPercurso:
                """
                :ivar UFPer: Sigla das Unidades da Federação do percurso
                    do veículo. Não é necessário repetir as UF de Início
                    e Fim
                """
                UFPer: Optional[Tuf] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                    }
                )

        @dataclass
        class Emit:
            """
            :ivar CNPJ: CNPJ do emitente Informar zeros não
                significativos
            :ivar CPF: CPF do emitente Informar zeros não
                significativos. Usar com série específica 920-969 para
                emitente pessoa física com inscrição estadual. Poderá
                ser usado também para emissão do Regime Especial da Nota
                Fiscal Fácil
            :ivar IE: Inscrição Estadual do emitemte
            :ivar xNome: Razão social ou Nome do emitente
            :ivar xFant: Nome fantasia do emitente
            :ivar enderEmit: Endereço do emitente
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            xFant: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            enderEmit: Optional[TendeEmi] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )

        @dataclass
        class InfModal:
            """
            :ivar any_element: XML do modal Insira neste local o XML
                específico do modal (rodoviário, aéreo, ferroviário ou
                aquaviário). O elemento do tipo -any- permite estender o
                documento XML com elementos não especificados pelo
                schema. Insira neste local - any- o XML específico do
                modal (rodoviário, aéreo, ferroviário ou aquaviário). A
                especificação do schema XML para cada modal pode ser
                encontrada nos arquivos que acompanham este pacote de
                liberação: Rodoviário - ver arquivo
                MDFeModalRodoviario_v9.99 Aéreo - ver arquivo
                MDFeModalAereo_v9.99 Aquaviário - arquivo
                MDFeModalAquaviario_v9.99 Ferroviário - arquivo
                MDFeModalFerroviario_v9.99 Onde v9.99 é a a designação
                genérica para a versão do arquivo. Por exemplo, o
                arquivo para o schema do modal Rodoviário na versão 1.00
                será denominado "MDFeModalRodoviario_v1.00".
            :ivar versaoModal: Versão do leiaute específico para o Modal
            """
            any_element: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                }
            )
            versaoModal: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"3\.(0[0-9]|[1-9][0-9])",
                }
            )

        @dataclass
        class InfDoc:
            """
            :ivar infMunDescarga: Informações dos Municípios de
                descarregamento
            """
            infMunDescarga: List["Tmdfe.InfMdfe.InfDoc.InfMunDescarga"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "min_occurs": 1,
                    "max_occurs": 1000,
                }
            )

            @dataclass
            class InfMunDescarga:
                """
                :ivar cMunDescarga: Código do Município de
                    Descarregamento
                :ivar xMunDescarga: Nome do Município de Descarregamento
                :ivar infCTe: Conhecimentos de Tranporte - usar este
                    grupo quando for prestador de serviço de transporte
                :ivar infNFe: Nota Fiscal Eletronica
                :ivar infMDFeTransp: Manifesto Eletrônico de Documentos
                    Fiscais. Somente para modal Aquaviário (vide regras
                    MOC)
                """
                cMunDescarga: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7}",
                    }
                )
                xMunDescarga: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                infCTe: List["Tmdfe.InfMdfe.InfDoc.InfMunDescarga.InfCte"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "max_occurs": 10000,
                    }
                )
                infNFe: List["Tmdfe.InfMdfe.InfDoc.InfMunDescarga.InfNfe"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "max_occurs": 10000,
                    }
                )
                infMDFeTransp: List["Tmdfe.InfMdfe.InfDoc.InfMunDescarga.InfMdfeTransp"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "max_occurs": 10000,
                    }
                )

                @dataclass
                class InfCte:
                    """
                    :ivar chCTe: Conhecimento Eletrônico - Chave de
                        Acesso
                    :ivar SegCodBarra: Segundo código de barras
                    :ivar indReentrega: Indicador de Reentrega
                    :ivar infUnidTransp: Informações das Unidades de
                        Transporte (Carreta/Reboque/Vagão) Deve ser
                        preenchido com as informações das unidades de
                        transporte utilizadas.
                    :ivar peri: Preenchido quando for  transporte de
                        produtos classificados pela ONU como perigosos.
                    :ivar infEntregaParcial: Grupo de informações da
                        Entrega Parcial (Corte de Voo)
                    """
                    chCTe: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "required": True,
                            "max_length": 44,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{44}",
                        }
                    )
                    SegCodBarra: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "pattern": r"[0-9]{36}",
                        }
                    )
                    indReentrega: Optional[InfCteIndReentrega] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )
                    infUnidTransp: List[TunidadeTransp] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )
                    peri: List["Tmdfe.InfMdfe.InfDoc.InfMunDescarga.InfCte.Peri"] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )
                    infEntregaParcial: Optional["Tmdfe.InfMdfe.InfDoc.InfMunDescarga.InfCte.InfEntregaParcial"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )

                    @dataclass
                    class Peri:
                        """
                        :ivar nONU: Número ONU/UN Ver a legislação de
                            transporte de produtos perigosos aplicadas
                            ao modal
                        :ivar xNomeAE: Nome apropriado para embarque do
                            produto Ver a legislação de transporte de
                            produtos perigosos aplicada ao modo de
                            transporte
                        :ivar xClaRisco: Classe ou subclasse/divisão, e
                            risco subsidiário/risco secundário Ver a
                            legislação de transporte de produtos
                            perigosos aplicadas ao modal
                        :ivar grEmb: Grupo de Embalagem Ver a legislação
                            de transporte de produtos perigosos
                            aplicadas ao modal Preenchimento obrigatório
                            para o modal aéreo. A legislação para o
                            modal rodoviário e ferroviário não atribui
                            grupo de embalagem para todos os produtos,
                            portanto haverá casos de não preenchimento
                            desse campo.
                        :ivar qTotProd: Quantidade total por produto
                            Preencher conforme a legislação de
                            transporte de produtos perigosos aplicada ao
                            modal
                        :ivar qVolTipo: Quantidade e Tipo de volumes
                            Preencher conforme a legislação de
                            transporte de produtos perigosos aplicada ao
                            modal
                        """
                        nONU: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{4}|ND",
                            }
                        )
                        xNomeAE: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 150,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        xClaRisco: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 40,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        grEmb: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 6,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        qTotProd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "min_length": 1,
                                "max_length": 20,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        qVolTipo: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 60,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )

                    @dataclass
                    class InfEntregaParcial:
                        """
                        :ivar qtdTotal: Quantidade total de volumes
                        :ivar qtdParcial: Quantidade de volumes enviados
                            no MDF-e
                        """
                        qtdTotal: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                            }
                        )
                        qtdParcial: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                            }
                        )

                @dataclass
                class InfNfe:
                    """
                    :ivar chNFe: Nota Fiscal Eletrônica
                    :ivar SegCodBarra: Segundo código de barras
                    :ivar indReentrega: Indicador de Reentrega
                    :ivar infUnidTransp: Informações das Unidades de
                        Transporte (Carreta/Reboque/Vagão) Deve ser
                        preenchido com as informações das unidades de
                        transporte utilizadas.
                    :ivar peri: Preenchido quando for  transporte de
                        produtos classificados pela ONU como perigosos.
                    """
                    chNFe: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "required": True,
                            "max_length": 44,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{44}",
                        }
                    )
                    SegCodBarra: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "pattern": r"[0-9]{36}",
                        }
                    )
                    indReentrega: Optional[InfNfeIndReentrega] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )
                    infUnidTransp: List[TunidadeTransp] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )
                    peri: List["Tmdfe.InfMdfe.InfDoc.InfMunDescarga.InfNfe.Peri"] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )

                    @dataclass
                    class Peri:
                        """
                        :ivar nONU: Número ONU/UN Ver a legislação de
                            transporte de produtos perigosos aplicadas
                            ao modal
                        :ivar xNomeAE: Nome apropriado para embarque do
                            produto Ver a legislação de transporte de
                            produtos perigosos aplicada ao modo de
                            transporte
                        :ivar xClaRisco: Classe ou subclasse/divisão, e
                            risco subsidiário/risco secundário Ver a
                            legislação de transporte de produtos
                            perigosos aplicadas ao modal
                        :ivar grEmb: Grupo de Embalagem Ver a legislação
                            de transporte de produtos perigosos
                            aplicadas ao modal Preenchimento obrigatório
                            para o modal aéreo. A legislação para o
                            modal rodoviário e ferroviário não atribui
                            grupo de embalagem para todos os produtos,
                            portanto haverá casos de não preenchimento
                            desse campo.
                        :ivar qTotProd: Quantidade total por produto
                            Preencher conforme a legislação de
                            transporte de produtos perigosos aplicada ao
                            modal
                        :ivar qVolTipo: Quantidade e Tipo de volumes
                            Preencher conforme a legislação de
                            transporte de produtos perigosos aplicada ao
                            modal
                        """
                        nONU: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{4}|ND",
                            }
                        )
                        xNomeAE: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 150,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        xClaRisco: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 40,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        grEmb: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 6,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        qTotProd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "min_length": 1,
                                "max_length": 20,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        qVolTipo: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 60,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )

                @dataclass
                class InfMdfeTransp:
                    """
                    :ivar chMDFe: Manifesto Eletrônico de Documentos
                        Fiscais
                    :ivar indReentrega: Indicador de Reentrega
                    :ivar infUnidTransp: Informações das Unidades de
                        Transporte (Carreta/Reboque/Vagão) Dispositivo
                        de carga utilizada (Unit Load Device - ULD)
                        significa todo tipo de contêiner de carga,
                        vagão, contêiner de avião, palete de aeronave
                        com rede ou palete de aeronave com rede sobre um
                        iglu.
                    :ivar peri: Preenchido quando for  transporte de
                        produtos classificados pela ONU como perigosos.
                    """
                    chMDFe: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "required": True,
                            "max_length": 44,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{44}",
                        }
                    )
                    indReentrega: Optional[InfMdfeTranspIndReentrega] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )
                    infUnidTransp: List[TunidadeTransp] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )
                    peri: List["Tmdfe.InfMdfe.InfDoc.InfMunDescarga.InfMdfeTransp.Peri"] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )

                    @dataclass
                    class Peri:
                        """
                        :ivar nONU: Número ONU/UN Ver a legislação de
                            transporte de produtos perigosos aplicadas
                            ao modal
                        :ivar xNomeAE: Nome apropriado para embarque do
                            produto Ver a legislação de transporte de
                            produtos perigosos aplicada ao modo de
                            transporte
                        :ivar xClaRisco: Classe ou subclasse/divisão, e
                            risco subsidiário/risco secundário Ver a
                            legislação de transporte de produtos
                            perigosos aplicadas ao modal
                        :ivar grEmb: Grupo de Embalagem Ver a legislação
                            de transporte de produtos perigosos
                            aplicadas ao modal Preenchimento obrigatório
                            para o modal aéreo. A legislação para o
                            modal rodoviário e ferroviário não atribui
                            grupo de embalagem para todos os produtos,
                            portanto haverá casos de não preenchimento
                            desse campo.
                        :ivar qTotProd: Quantidade total por produto
                            Preencher conforme a legislação de
                            transporte de produtos perigosos aplicada ao
                            modal
                        :ivar qVolTipo: Quantidade e Tipo de volumes
                            Preencher conforme a legislação de
                            transporte de produtos perigosos aplicada ao
                            modal
                        """
                        nONU: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{4}|ND",
                            }
                        )
                        xNomeAE: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 150,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        xClaRisco: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 40,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        grEmb: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 6,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        qTotProd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "min_length": 1,
                                "max_length": 20,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        qVolTipo: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 60,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )

        @dataclass
        class Seg:
            """
            :ivar infResp: Informações do responsável pelo seguro da
                carga
            :ivar infSeg: Informações da seguradora
            :ivar nApol: Número da Apólice Obrigatório pela lei
                11.442/07 (RCTRC)
            :ivar nAver: Número da Averbação Informar as averbações do
                seguro
            """
            infResp: Optional["Tmdfe.InfMdfe.Seg.InfResp"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            infSeg: Optional["Tmdfe.InfMdfe.Seg.InfSeg"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                }
            )
            nApol: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            nAver: List[str] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "min_length": 1,
                    "max_length": 40,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )

            @dataclass
            class InfResp:
                """
                :ivar respSeg: Responsável pelo seguro Preencher com: 1-
                    Emitente do MDF-e; 22 - Responsável pela contratação
                    do serviço de transporte (contratante) Dados
                    obrigatórios apenas no modal Rodoviário, depois da
                    lei 11.442/07. Para os demais modais esta informação
                    é opcional.
                :ivar CNPJ: Número do CNPJ do responsável pelo seguro
                    Obrigatório apenas se responsável pelo seguro for
                    (2) responsável pela contratação do transporte -
                    pessoa jurídica
                :ivar CPF: Número do CPF do responsável pelo seguro
                    Obrigatório apenas se responsável pelo seguro for
                    (2) responsável pela contratação do transporte -
                    pessoa física
                """
                respSeg: Optional[InfRespRespSeg] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                CNPJ: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{14}",
                    }
                )
                CPF: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{11}",
                    }
                )

            @dataclass
            class InfSeg:
                """
                :ivar xSeg: Nome da Seguradora
                :ivar CNPJ: Número do CNPJ da seguradora Obrigatório
                    apenas se responsável pelo seguro for (2)
                    responsável pela contratação do transporte - pessoa
                    jurídica
                """
                xSeg: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 30,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                CNPJ: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{0}|[0-9]{14}",
                    }
                )

        @dataclass
        class ProdPred:
            """
            :ivar tpCarga: Tipo de Carga Conforme Resolução ANTT nº.
                5.849/2019. 01-Granel sólido; 02-Granel líquido;
                03-Frigorificada; 04-Conteinerizada; 05-Carga Geral;
                06-Neogranel; 07-Perigosa (granel sólido); 08-Perigosa
                (granel líquido); 09-Perigosa (carga frigorificada);
                10-Perigosa (conteinerizada); 11-Perigosa (carga geral).
            :ivar xProd: Descrição do produto
            :ivar cEAN: GTIN (Global Trade Item Number) do produto,
                antigo código EAN ou código de barras
            :ivar NCM: Código NCM
            :ivar infLotacao: Informações da carga lotação. Informar
                somente quando MDF-e for de carga lotação
            """
            tpCarga: Optional[ProdPredTpCarga] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            xProd: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 120,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            cEAN: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"SEM GTIN|[0-9]{0}|[0-9]{8}|[0-9]{12,14}",
                }
            )
            NCM: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2}|[0-9]{8}",
                }
            )
            infLotacao: Optional["Tmdfe.InfMdfe.ProdPred.InfLotacao"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                }
            )

            @dataclass
            class InfLotacao:
                """
                :ivar infLocalCarrega: Informações da localização de
                    carregamento do MDF-e de carga lotação
                :ivar infLocalDescarrega: Informações da localização de
                    descarregamento do MDF-e de carga lotação
                """
                infLocalCarrega: Optional["Tmdfe.InfMdfe.ProdPred.InfLotacao.InfLocalCarrega"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                    }
                )
                infLocalDescarrega: Optional["Tmdfe.InfMdfe.ProdPred.InfLotacao.InfLocalDescarrega"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                    }
                )

                @dataclass
                class InfLocalCarrega:
                    """
                    :ivar CEP: CEP onde foi carregado o MDF-e Informar
                        zeros não significativos
                    :ivar latitude: Latitude do ponto geográfico onde
                        foi carregado o MDF-e
                    :ivar longitude: Latitude do ponto geográfico onde
                        foi carregado o MDF-e
                    """
                    CEP: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{8}",
                        }
                    )
                    latitude: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]\.[0-9]{6}|[1-8][0-9]\.[0-9]{6}|90\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-8][0-9]\.[0-9]{6}|-90\.[0-9]{6}",
                        }
                    )
                    longitude: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]\.[0-9]{6}|[1-9][0-9]\.[0-9]{6}|1[0-7][0-9]\.[0-9]{6}|180\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-9][0-9]\.[0-9]{6}|-1[0-7][0-9]\.[0-9]{6}|-180\.[0-9]{6}",
                        }
                    )

                @dataclass
                class InfLocalDescarrega:
                    """
                    :ivar CEP: CEP onde foi descarregado o MDF-e
                        Informar zeros não significativos
                    :ivar latitude: Latitude do ponto geográfico onde
                        foi descarregado o MDF-e
                    :ivar longitude: Latitude do ponto geográfico onde
                        foi descarregado o MDF-e
                    """
                    CEP: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{8}",
                        }
                    )
                    latitude: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]\.[0-9]{6}|[1-8][0-9]\.[0-9]{6}|90\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-8][0-9]\.[0-9]{6}|-90\.[0-9]{6}",
                        }
                    )
                    longitude: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]\.[0-9]{6}|[1-9][0-9]\.[0-9]{6}|1[0-7][0-9]\.[0-9]{6}|180\.[0-9]{6}|-[0-9]\.[0-9]{6}|-[1-9][0-9]\.[0-9]{6}|-1[0-7][0-9]\.[0-9]{6}|-180\.[0-9]{6}",
                        }
                    )

        @dataclass
        class Tot:
            """
            :ivar qCTe: Quantidade total de CT-e relacionados no
                Manifesto
            :ivar qNFe: Quantidade total de NF-e relacionadas no
                Manifesto
            :ivar qMDFe: Quantidade total de MDF-e relacionados no
                Manifesto Aquaviário
            :ivar vCarga: Valor total da carga / mercadorias
                transportadas
            :ivar cUnid: Código da unidade de medida do Peso Bruto da
                Carga / Mercadorias transportadas 01 – KG;  02 - TON
            :ivar qCarga: Peso Bruto Total da Carga / Mercadorias
                transportadas
            """
            qCTe: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1,6}",
                }
            )
            qNFe: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "pattern": r"[0-9]{1,6}",
                }
            )
            qMDFe: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "pattern": r"[0-9]{1,6}",
                }
            )
            vCarga: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            cUnid: Optional[TotCUnid] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            qCarga: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                }
            )

        @dataclass
        class Lacres:
            """
            :ivar nLacre: número do lacre
            """
            nLacre: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )

        @dataclass
        class AutXml:
            """
            :ivar CNPJ: CNPJ do autorizado Informar zeros não
                significativos
            :ivar CPF: CPF do autorizado Informar zeros não
                significativos
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )

        @dataclass
        class InfAdic:
            """
            :ivar infAdFisco: Informações adicionais de interesse do
                Fisco Norma referenciada, informações complementares,
                etc
            :ivar infCpl: Informações complementares de interesse do
                Contribuinte
            """
            infAdFisco: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            infCpl: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "min_length": 1,
                    "max_length": 5000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )

        @dataclass
        class InfSolicNff:
            """
            :ivar xSolic: Solicitação do pedido de emissão da NFF. Será
                preenchido com a totalidade de campos informados no
                aplicativo emissor serializado.
            """
            xSolic: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )

    @dataclass
    class InfMdfeSupl:
        """
        :ivar qrCodMDFe: Texto com o QR-Code para consulta do MDF-e
        """
        qrCodMDFe: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "min_length": 50,
                "max_length": 1000,
                "white_space": "preserve",
                "pattern": r"((HTTPS?|https?)://.*\?chMDFe=[0-9]{44}&tpAmb=[1-2](&sign=[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})?)",
            }
        )


@dataclass
class TenviMdfe:
    """
    Tipo Pedido de Autorização Assíncrona de MDF-e.
    """
    class Meta:
        name = "TEnviMDFe"

    idLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,15}",
        }
    )
    MDFe: Optional[Tmdfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
