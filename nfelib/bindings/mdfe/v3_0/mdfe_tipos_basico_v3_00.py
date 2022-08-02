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

    :ivar cnpj: CNPJ da pessoa jurídica responsável técnica pelo sistema
        utilizado na emissão do documento fiscal eletrônico Informar o
        CNPJ da pessoa jurídica desenvolvedora do sistema utilizado na
        emissão do documento fiscal eletrônico.
    :ivar x_contato: Nome da pessoa a ser contatada Informar o nome da
        pessoa a ser contatada na empresa desenvolvedora do sistema
        utilizado na emissão do documento fiscal eletrônico. No caso de
        pessoa física, informar o respectivo nome.
    :ivar email: Email da pessoa jurídica a ser contatada
    :ivar fone: Telefone da pessoa jurídica a ser contatada Preencher
        com o Código DDD + número do telefone.
    :ivar id_csrt: Identificador do código de segurança do responsável
        técnico Identificador do CSRT utilizado para geração do hash
    :ivar hash_csrt: Hash do token do código de segurança do responsável
        técnico O hashCSRT é o resultado das funções SHA-1 e base64 do
        token CSRT fornecido pelo fisco + chave de acesso do DF-e.
        (Implementação em futura NT) Observação: 28 caracteres são
        representados no schema como 20 bytes do tipo base64Binary
    """
    class Meta:
        name = "TRespTec"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    x_contato: Optional[str] = field(
        default=None,
        metadata={
            "name": "xContato",
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
    id_csrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "idCSRT",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "pattern": r"[0-9]{3}",
        }
    )
    hash_csrt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "hashCSRT",
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

    :ivar x_lgr: Logradouro
    :ivar nro: Número
    :ivar x_cpl: Complemento
    :ivar x_bairro: Bairro
    :ivar c_mun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar x_mun: Nome do município, , informar EXTERIOR para operações
        com o exterior.
    :ivar cep: CEP
    :ivar uf: Sigla da UF, , informar EX para operações com o exterior.
    :ivar c_pais: Código do país
    :ivar x_pais: Nome do país
    :ivar fone: Telefone
    """
    class Meta:
        name = "TEndOrg"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
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
    x_cpl: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "xBairro",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    x_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    c_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "cPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    x_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "xPais",
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

    :ivar cnpj: Número do CNPJ
    :ivar cpf: Número do CPF
    :ivar x_nome: Razão Social ou Nome
    :ivar x_lgr: Logradouro
    :ivar nro: Número
    :ivar x_cpl: Complemento
    :ivar x_bairro: Bairro
    :ivar c_mun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar x_mun: Nome do município, , informar EXTERIOR para operações
        com o exterior.
    :ivar uf: Sigla da UF, , informar EX para operações com o exterior.
    """
    class Meta:
        name = "TEndReEnt"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    x_nome: Optional[str] = field(
        default=None,
        metadata={
            "name": "xNome",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
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
    x_cpl: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "xBairro",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    x_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )


@dataclass
class TendeEmi:
    """
    Tipo Dados do Endereço.

    :ivar x_lgr: Logradouro
    :ivar nro: Número
    :ivar x_cpl: Complemento
    :ivar x_bairro: Bairro
    :ivar c_mun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar x_mun: Nome do município, , informar EXTERIOR para operações
        com o exterior.
    :ivar cep: CEP Informar zeros não significativos
    :ivar uf: Sigla da UF, , informar EX para operações com o exterior.
    :ivar fone: Telefone
    :ivar email: Endereço de E-mail
    """
    class Meta:
        name = "TEndeEmi"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
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
    x_cpl: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "xBairro",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    x_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
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

    :ivar x_lgr: Logradouro
    :ivar nro: Número
    :ivar x_cpl: Complemento
    :ivar x_bairro: Bairro
    :ivar c_mun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar x_mun: Nome do município, , informar EXTERIOR para operações
        com o exterior.
    :ivar cep: CEP
    :ivar uf: Sigla da UF, , informar EX para operações com o exterior.
    """
    class Meta:
        name = "TEnderFer"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
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
    x_cpl: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "xBairro",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    x_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )


@dataclass
class Tendereco:
    """
    Tipo Dados do Endereço.

    :ivar x_lgr: Logradouro
    :ivar nro: Número
    :ivar x_cpl: Complemento
    :ivar x_bairro: Bairro
    :ivar c_mun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar x_mun: Nome do município, informar EXTERIOR para operações com
        o exterior.
    :ivar cep: CEP Informar os zeros não significativos
    :ivar uf: Sigla da UF, informar EX para operações com o exterior.
    :ivar c_pais: Código do país Utilizar a tabela do BACEN
    :ivar x_pais: Nome do país
    """
    class Meta:
        name = "TEndereco"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
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
    x_cpl: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "xBairro",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    x_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    c_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "cPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    x_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "xPais",
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

    :ivar x_lgr: Logradouro
    :ivar nro: Número
    :ivar x_cpl: Complemento
    :ivar x_bairro: Bairro
    :ivar c_mun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar x_mun: Nome do município, , informar EXTERIOR para operações
        com o exterior.
    :ivar cep: CEP
    :ivar uf: Sigla da UF, , informar EX para operações com o exterior.
    """
    class Meta:
        name = "TEndernac"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
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
    x_cpl: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "xBairro",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    x_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )


@dataclass
class Tlocal:
    """
    Tipo Dados do Local de Origem ou Destino.

    :ivar c_mun: Código do município (utilizar a tabela do IBGE)
    :ivar x_mun: Nome do município
    :ivar uf: Sigla da UF
    """
    class Meta:
        name = "TLocal"

    c_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    x_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )


@dataclass
class TnfeNf:
    """
    Tipo  de Dados das Notas Fiscais Papel e Eletrônica.

    :ivar inf_nfe: Informações da NF-e
    :ivar inf_nf: Informações da NF mod 1 e 1A
    """
    class Meta:
        name = "TNFeNF"

    inf_nfe: Optional["TnfeNf.InfNfe"] = field(
        default=None,
        metadata={
            "name": "infNFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    inf_nf: Optional["TnfeNf.InfNf"] = field(
        default=None,
        metadata={
            "name": "infNF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )

    @dataclass
    class InfNfe:
        """
        :ivar ch_nfe: Chave de acesso da NF-e
        :ivar pin: PIN SUFRAMA PIN atribuído pela SUFRAMA para a
            operação.
        """
        ch_nfe: Optional[str] = field(
            default=None,
            metadata={
                "name": "chNFe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        pin: Optional[str] = field(
            default=None,
            metadata={
                "name": "PIN",
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
        :ivar n_nf: Número
        :ivar d_emi: Data de Emissão Formato AAAA-MM-DD
        :ivar v_nf: Valor Total da NF
        :ivar pin: PIN SUFRAMA PIN atribuído pela SUFRAMA para a
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
        n_nf: Optional[str] = field(
            default=None,
            metadata={
                "name": "nNF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        d_emi: Optional[str] = field(
            default=None,
            metadata={
                "name": "dEmi",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
            }
        )
        v_nf: Optional[str] = field(
            default=None,
            metadata={
                "name": "vNF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pin: Optional[str] = field(
            default=None,
            metadata={
                "name": "PIN",
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
            :ivar cnpj: CNPJ do emitente
            :ivar x_nome: Razão Social ou Nome
            :ivar uf: UF do Emitente Informar 'EX' para operações com o
                exterior.
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            uf: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )

        @dataclass
        class Dest:
            """
            :ivar cnpj: CNPJ do Destinatário Informar o CNPJ ou o CPF do
                destinatário, preenchendo os zeros não significativos.
                Não informar o conteúdo da TAG se a operação for
                realizada com o Exterior.
            :ivar cpf: CPF do Destinatário Informar os zeros não
                significativos.
            :ivar x_nome: Razão Social ou Nome
            :ivar uf: UF do Destinatário Informar 'EX' para operações
                com o exterior.
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            uf: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )


@dataclass
class TprotMdfe:
    """
    Tipo Protocolo de status resultado do processamento do MDF-e.

    :ivar inf_prot: Dados do protocolo de status
    :ivar inf_fisco: Mensagem do Fisco
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TProtMDFe"

    inf_prot: Optional["TprotMdfe.InfProt"] = field(
        default=None,
        metadata={
            "name": "infProt",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    inf_fisco: Optional["TprotMdfe.InfFisco"] = field(
        default=None,
        metadata={
            "name": "infFisco",
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
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar ver_aplic: Versão do Aplicativo que processou a NF-3e
        :ivar ch_mdfe: Chave de acesso do MDF-e
        :ivar dh_recbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS TZD.
        :ivar n_prot: Número do Protocolo de Status do MDF-e
        :ivar dig_val: Digest Value do MDF-e processado. Utilizado para
            conferir a integridade do MDF-e original.
        :ivar c_stat: Código do status do MDF-e
        :ivar x_motivo: Descrição literal do status do MDF-e.
        :ivar id:
        """
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
            }
        )
        ver_aplic: Optional[str] = field(
            default=None,
            metadata={
                "name": "verAplic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        ch_mdfe: Optional[str] = field(
            default=None,
            metadata={
                "name": "chMDFe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        dh_recbto: Optional[str] = field(
            default=None,
            metadata={
                "name": "dhRecbto",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        dig_val: Optional[bytes] = field(
            default=None,
            metadata={
                "name": "digVal",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "format": "base64",
            }
        )
        c_stat: Optional[str] = field(
            default=None,
            metadata={
                "name": "cStat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
    class InfFisco:
        """
        :ivar c_msg: Código do status da mensagem do fisco
        :ivar x_msg: Mensagem do Fisco
        """
        c_msg: Optional[str] = field(
            default=None,
            metadata={
                "name": "cMsg",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        x_msg: Optional[str] = field(
            default=None,
            metadata={
                "name": "xMsg",
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

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar c_uf: Identificação da UF
    :ivar ver_aplic: Versão do Aplicativo que recebeu o Arquivo.
    :ivar c_stat: Código do status da mensagem enviada.
    :ivar x_motivo: Descrição literal do status do serviço solicitado.
    :ivar inf_rec: Dados do Recibo do Arquivo
    :ivar versao:
    """
    class Meta:
        name = "TRetEnviMDFe"

    tp_amb: Optional[object] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    c_uf: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    inf_rec: Optional["TretEnviMdfe.InfRec"] = field(
        default=None,
        metadata={
            "name": "infRec",
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
        :ivar n_rec: Número do Recibo
        :ivar dh_recbto: Data e hora do recebimento, no formato AAAA-MM-
            DDTHH:MM:SS
        :ivar t_med: Tempo médio de resposta do serviço (em segundos)
            dos últimos 5 minutos
        """
        n_rec: Optional[str] = field(
            default=None,
            metadata={
                "name": "nRec",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        dh_recbto: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "name": "dhRecbto",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
            }
        )
        t_med: Optional[str] = field(
            default=None,
            metadata={
                "name": "tMed",
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

    :ivar tp_unid_carga: Tipo da Unidade de Carga 1 - Container; 2 -
        ULD; 3 - Pallet; 4 - Outros;
    :ivar id_unid_carga: Identificação da Unidade de Carga Informar a
        identificação da unidade de carga, por exemplo: número do
        container.
    :ivar lac_unid_carga: Lacres das Unidades de Carga
    :ivar qtd_rat: Quantidade rateada (Peso,Volume)
    """
    class Meta:
        name = "TUnidCarga"

    tp_unid_carga: Optional[TtipoUnidCarga] = field(
        default=None,
        metadata={
            "name": "tpUnidCarga",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    id_unid_carga: Optional[str] = field(
        default=None,
        metadata={
            "name": "idUnidCarga",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[A-Z0-9]+",
        }
    )
    lac_unid_carga: List["TunidCarga.LacUnidCarga"] = field(
        default_factory=list,
        metadata={
            "name": "lacUnidCarga",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    qtd_rat: Optional[str] = field(
        default=None,
        metadata={
            "name": "qtdRat",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,3}(\.[0-9]{2,3})?",
        }
    )

    @dataclass
    class LacUnidCarga:
        """
        :ivar n_lacre: Número do lacre
        """
        n_lacre: Optional[str] = field(
            default=None,
            metadata={
                "name": "nLacre",
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

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar c_uf: Identificação da UF
    :ivar ver_aplic: Versão do Aplicativo que recebeu o Arquivo.
    :ivar c_stat: Código do status da mensagem enviada.
    :ivar x_motivo: Descrição literal do status do serviço solicitado.
    :ivar prot_mdfe: Dados do Recibo do Arquivo
    :ivar versao:
    """
    class Meta:
        name = "TRetMDFe"

    tp_amb: Optional[object] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    c_uf: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    prot_mdfe: Optional[TprotMdfe] = field(
        default=None,
        metadata={
            "name": "protMDFe",
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

    :ivar tp_unid_transp: Tipo da Unidade de Transporte 1 - Rodoviário
        Tração; 2 - Rodoviário Reboque; 3 - Navio; 4 - Balsa; 5 -
        Aeronave; 6 - Vagão; 7 - Outros
    :ivar id_unid_transp: Identificação da Unidade de Transporte
        Informar a identificação conforme o tipo de unidade de
        transporte. Por exemplo: para rodoviário tração ou reboque
        deverá preencher com a placa do veículo.
    :ivar lac_unid_transp: Lacres das Unidades de Transporte
    :ivar inf_unid_carga: Informações das Unidades de Carga
        (Containeres/ULD/Outros) Dispositivo de carga utilizada (Unit
        Load Device - ULD) significa todo tipo de contêiner de carga,
        vagão, contêiner de avião, palete de aeronave com rede ou palete
        de aeronave com rede sobre um iglu.
    :ivar qtd_rat: Quantidade rateada (Peso,Volume)
    """
    class Meta:
        name = "TUnidadeTransp"

    tp_unid_transp: Optional[TtipoUnidTransp] = field(
        default=None,
        metadata={
            "name": "tpUnidTransp",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    id_unid_transp: Optional[str] = field(
        default=None,
        metadata={
            "name": "idUnidTransp",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[A-Z0-9]+",
        }
    )
    lac_unid_transp: List["TunidadeTransp.LacUnidTransp"] = field(
        default_factory=list,
        metadata={
            "name": "lacUnidTransp",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    inf_unid_carga: List[TunidCarga] = field(
        default_factory=list,
        metadata={
            "name": "infUnidCarga",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    qtd_rat: Optional[str] = field(
        default=None,
        metadata={
            "name": "qtdRat",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,3}(\.[0-9]{2,3})?",
        }
    )

    @dataclass
    class LacUnidTransp:
        """
        :ivar n_lacre: Número do lacre
        """
        n_lacre: Optional[str] = field(
            default=None,
            metadata={
                "name": "nLacre",
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

    :ivar inf_mdfe: Informações do MDF-e
    :ivar inf_mdfe_supl: Informações suplementares do MDF-e
    :ivar signature:
    """
    class Meta:
        name = "TMDFe"

    inf_mdfe: Optional["Tmdfe.InfMdfe"] = field(
        default=None,
        metadata={
            "name": "infMDFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    inf_mdfe_supl: Optional["Tmdfe.InfMdfeSupl"] = field(
        default=None,
        metadata={
            "name": "infMDFeSupl",
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
        :ivar inf_modal: Informações do modal
        :ivar inf_doc: Informações dos Documentos fiscais vinculados ao
            manifesto
        :ivar seg: Informações de Seguro da Carga
        :ivar prod_pred: Produto predominante Informar a descrição do
            produto predominante
        :ivar tot: Totalizadores da carga transportada e seus documentos
            fiscais
        :ivar lacres: Lacres do MDF-e Preechimento opcional para os
            modais Rodoviário e Ferroviário
        :ivar aut_xml: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar inf_adic: Informações Adicionais
        :ivar inf_resp_tec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar inf_solic_nff: Grupo de informações do pedido de emissão
            da Nota Fiscal Fácil
        :ivar versao: Versão do leiaute Ex: "3.00"
        :ivar id: Identificador da tag a ser assinada Informar a chave
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
        inf_modal: Optional["Tmdfe.InfMdfe.InfModal"] = field(
            default=None,
            metadata={
                "name": "infModal",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
            }
        )
        inf_doc: Optional["Tmdfe.InfMdfe.InfDoc"] = field(
            default=None,
            metadata={
                "name": "infDoc",
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
        prod_pred: Optional["Tmdfe.InfMdfe.ProdPred"] = field(
            default=None,
            metadata={
                "name": "prodPred",
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
        aut_xml: List["Tmdfe.InfMdfe.AutXml"] = field(
            default_factory=list,
            metadata={
                "name": "autXML",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "max_occurs": 10,
            }
        )
        inf_adic: Optional["Tmdfe.InfMdfe.InfAdic"] = field(
            default=None,
            metadata={
                "name": "infAdic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
            }
        )
        inf_resp_tec: Optional[TrespTec] = field(
            default=None,
            metadata={
                "name": "infRespTec",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
            }
        )
        inf_solic_nff: Optional["Tmdfe.InfMdfe.InfSolicNff"] = field(
            default=None,
            metadata={
                "name": "infSolicNFF",
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
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "required": True,
                "pattern": r"MDFe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar c_uf: Código da UF do emitente do MDF-e Código da UF
                do emitente do Documento Fiscal. Utilizar a Tabela do
                IBGE de código de unidades da federação.
            :ivar tp_amb: Tipo do Ambiente 1 - Produção 2 - Homologação
            :ivar tp_emit: Tipo do Emitente 1 - Prestador de serviço de
                transporte 2 - Transportador de Carga Própria 3 -
                Prestador de serviço de transporte que emitirá CT-e
                Globalizado OBS: Deve ser preenchido com 2 para
                emitentes de NF-e e pelas transportadoras quando
                estiverem fazendo transporte de carga própria. Deve ser
                preenchido com 3 para transportador de carga que emitirá
                à posteriori CT-e Globalizado relacionando as NF-e.
            :ivar tp_transp: Tipo do Transportador 1 - ETC 2 - TAC 3 -
                CTC
            :ivar mod: Modelo do Manifesto Eletrônico Utilizar o código
                58 para identificação do MDF-e
            :ivar serie: Série do Manifesto Informar a série do
                documento fiscal (informar zero se inexistente). Série
                na faixa [920-969]: Reservada para emissão por
                contribuinte pessoa física com inscrição estadual.
            :ivar n_mdf: Número do Manifesto Número que identifica o
                Manifesto. 1 a 999999999.
            :ivar c_mdf: Código numérico que compõe a Chave de Acesso.
                Código aleatório gerado pelo emitente, com o objetivo de
                evitar acessos indevidos ao documento.
            :ivar c_dv: Digito verificador da chave de acesso do
                Manifesto Informar o dígito  de controle da chave de
                acesso do MDF-e, que deve ser calculado com a aplicação
                do algoritmo módulo 11 (base 2,9) da chave de acesso.
            :ivar modal: Modalidade de transporte 1 - Rodoviário; 2 -
                Aéreo; 3 - Aquaviário; 4 - Ferroviário.
            :ivar dh_emi: Data e hora de emissão do Manifesto Formato
                AAAA-MM-DDTHH:MM:DD TZD
            :ivar tp_emis: Forma de emissão do Manifesto 1 - Normal ; 2
                - Contingência; 3-Regime Especial NFF
            :ivar proc_emi: Identificação do processo de emissão do
                Manifesto 0 - emissão de MDF-e com aplicativo do
                contribuinte
            :ivar ver_proc: Versão do processo de emissão Informar a
                versão do aplicativo emissor de MDF-e.
            :ivar ufini: Sigla da UF do Carregamento Utilizar a Tabela
                do IBGE de código de unidades da federação. Informar
                'EX' para operações com o exterior.
            :ivar uffim: Sigla da UF do Descarregamento Utilizar a
                Tabela do IBGE de código de unidades da federação.
                Informar 'EX' para operações com o exterior.
            :ivar inf_mun_carrega: Informações dos Municípios de
                Carregamento
            :ivar inf_percurso: Informações do Percurso do MDF-e
            :ivar dh_ini_viagem: Data e hora previstos de inicio da
                viagem Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar ind_canal_verde: Indicador de participação do Canal
                Verde
            :ivar ind_carrega_posterior: Indicador de MDF-e com inclusão
                da Carga posterior a emissão por evento de inclusão de
                DF-e
            """
            c_uf: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "name": "cUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            tp_amb: Optional[Tamb] = field(
                default=None,
                metadata={
                    "name": "tpAmb",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            tp_emit: Optional[Temit] = field(
                default=None,
                metadata={
                    "name": "tpEmit",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            tp_transp: Optional[Ttransp] = field(
                default=None,
                metadata={
                    "name": "tpTransp",
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
            n_mdf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nMDF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            c_mdf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cMDF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            c_dv: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cDV",
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
            dh_emi: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tp_emis: Optional[IdeTpEmis] = field(
                default=None,
                metadata={
                    "name": "tpEmis",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            proc_emi: Optional[TprocEmi] = field(
                default=None,
                metadata={
                    "name": "procEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            ver_proc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "verProc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ufini: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UFIni",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            uffim: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UFFim",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            inf_mun_carrega: List["Tmdfe.InfMdfe.Ide.InfMunCarrega"] = field(
                default_factory=list,
                metadata={
                    "name": "infMunCarrega",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "min_occurs": 1,
                    "max_occurs": 50,
                }
            )
            inf_percurso: List["Tmdfe.InfMdfe.Ide.InfPercurso"] = field(
                default_factory=list,
                metadata={
                    "name": "infPercurso",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "max_occurs": 25,
                }
            )
            dh_ini_viagem: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhIniViagem",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            ind_canal_verde: Optional[IdeIndCanalVerde] = field(
                default=None,
                metadata={
                    "name": "indCanalVerde",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                }
            )
            ind_carrega_posterior: Optional[IdeIndCarregaPosterior] = field(
                default=None,
                metadata={
                    "name": "indCarregaPosterior",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                }
            )

            @dataclass
            class InfMunCarrega:
                """
                :ivar c_mun_carrega: Código do Município de Carregamento
                :ivar x_mun_carrega: Nome do Município de Carregamento
                """
                c_mun_carrega: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cMunCarrega",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7}",
                    }
                )
                x_mun_carrega: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xMunCarrega",
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
                :ivar ufper: Sigla das Unidades da Federação do percurso
                    do veículo. Não é necessário repetir as UF de Início
                    e Fim
                """
                ufper: Optional[Tuf] = field(
                    default=None,
                    metadata={
                        "name": "UFPer",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                    }
                )

        @dataclass
        class Emit:
            """
            :ivar cnpj: CNPJ do emitente Informar zeros não
                significativos
            :ivar cpf: CPF do emitente Informar zeros não
                significativos. Usar com série específica 920-969 para
                emitente pessoa física com inscrição estadual. Poderá
                ser usado também para emissão do Regime Especial da Nota
                Fiscal Fácil
            :ivar ie: Inscrição Estadual do emitemte
            :ivar x_nome: Razão social ou Nome do emitente
            :ivar x_fant: Nome fantasia do emitente
            :ivar ender_emit: Endereço do emitente
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_fant: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xFant",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ender_emit: Optional[TendeEmi] = field(
                default=None,
                metadata={
                    "name": "enderEmit",
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
            :ivar versao_modal: Versão do leiaute específico para o
                Modal
            """
            any_element: Optional[object] = field(
                default=None,
                metadata={
                    "type": "Wildcard",
                    "namespace": "##any",
                }
            )
            versao_modal: Optional[str] = field(
                default=None,
                metadata={
                    "name": "versaoModal",
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"3\.(0[0-9]|[1-9][0-9])",
                }
            )

        @dataclass
        class InfDoc:
            """
            :ivar inf_mun_descarga: Informações dos Municípios de
                descarregamento
            """
            inf_mun_descarga: List["Tmdfe.InfMdfe.InfDoc.InfMunDescarga"] = field(
                default_factory=list,
                metadata={
                    "name": "infMunDescarga",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "min_occurs": 1,
                    "max_occurs": 1000,
                }
            )

            @dataclass
            class InfMunDescarga:
                """
                :ivar c_mun_descarga: Código do Município de
                    Descarregamento
                :ivar x_mun_descarga: Nome do Município de
                    Descarregamento
                :ivar inf_cte: Conhecimentos de Tranporte - usar este
                    grupo quando for prestador de serviço de transporte
                :ivar inf_nfe: Nota Fiscal Eletronica
                :ivar inf_mdfe_transp: Manifesto Eletrônico de
                    Documentos Fiscais. Somente para modal Aquaviário
                    (vide regras MOC)
                """
                c_mun_descarga: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cMunDescarga",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7}",
                    }
                )
                x_mun_descarga: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xMunDescarga",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                inf_cte: List["Tmdfe.InfMdfe.InfDoc.InfMunDescarga.InfCte"] = field(
                    default_factory=list,
                    metadata={
                        "name": "infCTe",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "max_occurs": 10000,
                    }
                )
                inf_nfe: List["Tmdfe.InfMdfe.InfDoc.InfMunDescarga.InfNfe"] = field(
                    default_factory=list,
                    metadata={
                        "name": "infNFe",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "max_occurs": 10000,
                    }
                )
                inf_mdfe_transp: List["Tmdfe.InfMdfe.InfDoc.InfMunDescarga.InfMdfeTransp"] = field(
                    default_factory=list,
                    metadata={
                        "name": "infMDFeTransp",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "max_occurs": 10000,
                    }
                )

                @dataclass
                class InfCte:
                    """
                    :ivar ch_cte: Conhecimento Eletrônico - Chave de
                        Acesso
                    :ivar seg_cod_barra: Segundo código de barras
                    :ivar ind_reentrega: Indicador de Reentrega
                    :ivar inf_unid_transp: Informações das Unidades de
                        Transporte (Carreta/Reboque/Vagão) Deve ser
                        preenchido com as informações das unidades de
                        transporte utilizadas.
                    :ivar peri: Preenchido quando for  transporte de
                        produtos classificados pela ONU como perigosos.
                    :ivar inf_entrega_parcial: Grupo de informações da
                        Entrega Parcial (Corte de Voo)
                    """
                    ch_cte: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "chCTe",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "required": True,
                            "max_length": 44,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{44}",
                        }
                    )
                    seg_cod_barra: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "SegCodBarra",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "pattern": r"[0-9]{36}",
                        }
                    )
                    ind_reentrega: Optional[InfCteIndReentrega] = field(
                        default=None,
                        metadata={
                            "name": "indReentrega",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )
                    inf_unid_transp: List[TunidadeTransp] = field(
                        default_factory=list,
                        metadata={
                            "name": "infUnidTransp",
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
                    inf_entrega_parcial: Optional["Tmdfe.InfMdfe.InfDoc.InfMunDescarga.InfCte.InfEntregaParcial"] = field(
                        default=None,
                        metadata={
                            "name": "infEntregaParcial",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )

                    @dataclass
                    class Peri:
                        """
                        :ivar n_onu: Número ONU/UN Ver a legislação de
                            transporte de produtos perigosos aplicadas
                            ao modal
                        :ivar x_nome_ae: Nome apropriado para embarque
                            do produto Ver a legislação de transporte de
                            produtos perigosos aplicada ao modo de
                            transporte
                        :ivar x_cla_risco: Classe ou subclasse/divisão,
                            e risco subsidiário/risco secundário Ver a
                            legislação de transporte de produtos
                            perigosos aplicadas ao modal
                        :ivar gr_emb: Grupo de Embalagem Ver a
                            legislação de transporte de produtos
                            perigosos aplicadas ao modal Preenchimento
                            obrigatório para o modal aéreo. A legislação
                            para o modal rodoviário e ferroviário não
                            atribui grupo de embalagem para todos os
                            produtos, portanto haverá casos de não
                            preenchimento desse campo.
                        :ivar q_tot_prod: Quantidade total por produto
                            Preencher conforme a legislação de
                            transporte de produtos perigosos aplicada ao
                            modal
                        :ivar q_vol_tipo: Quantidade e Tipo de volumes
                            Preencher conforme a legislação de
                            transporte de produtos perigosos aplicada ao
                            modal
                        """
                        n_onu: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "nONU",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{4}|ND",
                            }
                        )
                        x_nome_ae: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "xNomeAE",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 150,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        x_cla_risco: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "xClaRisco",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 40,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        gr_emb: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "grEmb",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 6,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        q_tot_prod: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qTotProd",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "min_length": 1,
                                "max_length": 20,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        q_vol_tipo: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qVolTipo",
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
                        :ivar qtd_total: Quantidade total de volumes
                        :ivar qtd_parcial: Quantidade de volumes
                            enviados no MDF-e
                        """
                        qtd_total: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qtdTotal",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                            }
                        )
                        qtd_parcial: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qtdParcial",
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
                    :ivar ch_nfe: Nota Fiscal Eletrônica
                    :ivar seg_cod_barra: Segundo código de barras
                    :ivar ind_reentrega: Indicador de Reentrega
                    :ivar inf_unid_transp: Informações das Unidades de
                        Transporte (Carreta/Reboque/Vagão) Deve ser
                        preenchido com as informações das unidades de
                        transporte utilizadas.
                    :ivar peri: Preenchido quando for  transporte de
                        produtos classificados pela ONU como perigosos.
                    """
                    ch_nfe: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "chNFe",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "required": True,
                            "max_length": 44,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{44}",
                        }
                    )
                    seg_cod_barra: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "SegCodBarra",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "pattern": r"[0-9]{36}",
                        }
                    )
                    ind_reentrega: Optional[InfNfeIndReentrega] = field(
                        default=None,
                        metadata={
                            "name": "indReentrega",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )
                    inf_unid_transp: List[TunidadeTransp] = field(
                        default_factory=list,
                        metadata={
                            "name": "infUnidTransp",
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
                        :ivar n_onu: Número ONU/UN Ver a legislação de
                            transporte de produtos perigosos aplicadas
                            ao modal
                        :ivar x_nome_ae: Nome apropriado para embarque
                            do produto Ver a legislação de transporte de
                            produtos perigosos aplicada ao modo de
                            transporte
                        :ivar x_cla_risco: Classe ou subclasse/divisão,
                            e risco subsidiário/risco secundário Ver a
                            legislação de transporte de produtos
                            perigosos aplicadas ao modal
                        :ivar gr_emb: Grupo de Embalagem Ver a
                            legislação de transporte de produtos
                            perigosos aplicadas ao modal Preenchimento
                            obrigatório para o modal aéreo. A legislação
                            para o modal rodoviário e ferroviário não
                            atribui grupo de embalagem para todos os
                            produtos, portanto haverá casos de não
                            preenchimento desse campo.
                        :ivar q_tot_prod: Quantidade total por produto
                            Preencher conforme a legislação de
                            transporte de produtos perigosos aplicada ao
                            modal
                        :ivar q_vol_tipo: Quantidade e Tipo de volumes
                            Preencher conforme a legislação de
                            transporte de produtos perigosos aplicada ao
                            modal
                        """
                        n_onu: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "nONU",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{4}|ND",
                            }
                        )
                        x_nome_ae: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "xNomeAE",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 150,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        x_cla_risco: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "xClaRisco",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 40,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        gr_emb: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "grEmb",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 6,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        q_tot_prod: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qTotProd",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "min_length": 1,
                                "max_length": 20,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        q_vol_tipo: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qVolTipo",
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
                    :ivar ch_mdfe: Manifesto Eletrônico de Documentos
                        Fiscais
                    :ivar ind_reentrega: Indicador de Reentrega
                    :ivar inf_unid_transp: Informações das Unidades de
                        Transporte (Carreta/Reboque/Vagão) Dispositivo
                        de carga utilizada (Unit Load Device - ULD)
                        significa todo tipo de contêiner de carga,
                        vagão, contêiner de avião, palete de aeronave
                        com rede ou palete de aeronave com rede sobre um
                        iglu.
                    :ivar peri: Preenchido quando for  transporte de
                        produtos classificados pela ONU como perigosos.
                    """
                    ch_mdfe: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "chMDFe",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                            "required": True,
                            "max_length": 44,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{44}",
                        }
                    )
                    ind_reentrega: Optional[InfMdfeTranspIndReentrega] = field(
                        default=None,
                        metadata={
                            "name": "indReentrega",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        }
                    )
                    inf_unid_transp: List[TunidadeTransp] = field(
                        default_factory=list,
                        metadata={
                            "name": "infUnidTransp",
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
                        :ivar n_onu: Número ONU/UN Ver a legislação de
                            transporte de produtos perigosos aplicadas
                            ao modal
                        :ivar x_nome_ae: Nome apropriado para embarque
                            do produto Ver a legislação de transporte de
                            produtos perigosos aplicada ao modo de
                            transporte
                        :ivar x_cla_risco: Classe ou subclasse/divisão,
                            e risco subsidiário/risco secundário Ver a
                            legislação de transporte de produtos
                            perigosos aplicadas ao modal
                        :ivar gr_emb: Grupo de Embalagem Ver a
                            legislação de transporte de produtos
                            perigosos aplicadas ao modal Preenchimento
                            obrigatório para o modal aéreo. A legislação
                            para o modal rodoviário e ferroviário não
                            atribui grupo de embalagem para todos os
                            produtos, portanto haverá casos de não
                            preenchimento desse campo.
                        :ivar q_tot_prod: Quantidade total por produto
                            Preencher conforme a legislação de
                            transporte de produtos perigosos aplicada ao
                            modal
                        :ivar q_vol_tipo: Quantidade e Tipo de volumes
                            Preencher conforme a legislação de
                            transporte de produtos perigosos aplicada ao
                            modal
                        """
                        n_onu: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "nONU",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{4}|ND",
                            }
                        )
                        x_nome_ae: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "xNomeAE",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 150,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        x_cla_risco: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "xClaRisco",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 40,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        gr_emb: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "grEmb",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "min_length": 1,
                                "max_length": 6,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        q_tot_prod: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qTotProd",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                                "required": True,
                                "min_length": 1,
                                "max_length": 20,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        q_vol_tipo: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qVolTipo",
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
            :ivar inf_resp: Informações do responsável pelo seguro da
                carga
            :ivar inf_seg: Informações da seguradora
            :ivar n_apol: Número da Apólice Obrigatório pela lei
                11.442/07 (RCTRC)
            :ivar n_aver: Número da Averbação Informar as averbações do
                seguro
            """
            inf_resp: Optional["Tmdfe.InfMdfe.Seg.InfResp"] = field(
                default=None,
                metadata={
                    "name": "infResp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            inf_seg: Optional["Tmdfe.InfMdfe.Seg.InfSeg"] = field(
                default=None,
                metadata={
                    "name": "infSeg",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                }
            )
            n_apol: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nApol",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            n_aver: List[str] = field(
                default_factory=list,
                metadata={
                    "name": "nAver",
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
                :ivar resp_seg: Responsável pelo seguro Preencher com:
                    1- Emitente do MDF-e; 22 - Responsável pela
                    contratação do serviço de transporte (contratante)
                    Dados obrigatórios apenas no modal Rodoviário,
                    depois da lei 11.442/07. Para os demais modais esta
                    informação é opcional.
                :ivar cnpj: Número do CNPJ do responsável pelo seguro
                    Obrigatório apenas se responsável pelo seguro for
                    (2) responsável pela contratação do transporte -
                    pessoa jurídica
                :ivar cpf: Número do CPF do responsável pelo seguro
                    Obrigatório apenas se responsável pelo seguro for
                    (2) responsável pela contratação do transporte -
                    pessoa física
                """
                resp_seg: Optional[InfRespRespSeg] = field(
                    default=None,
                    metadata={
                        "name": "respSeg",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 1,
                        "white_space": "preserve",
                    }
                )
                cnpj: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CNPJ",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{14}",
                    }
                )
                cpf: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CPF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{11}",
                    }
                )

            @dataclass
            class InfSeg:
                """
                :ivar x_seg: Nome da Seguradora
                :ivar cnpj: Número do CNPJ da seguradora Obrigatório
                    apenas se responsável pelo seguro for (2)
                    responsável pela contratação do transporte - pessoa
                    jurídica
                """
                x_seg: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xSeg",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 30,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                cnpj: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CNPJ",
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
            :ivar tp_carga: Tipo de Carga Conforme Resolução ANTT nº.
                5.849/2019. 01-Granel sólido; 02-Granel líquido;
                03-Frigorificada; 04-Conteinerizada; 05-Carga Geral;
                06-Neogranel; 07-Perigosa (granel sólido); 08-Perigosa
                (granel líquido); 09-Perigosa (carga frigorificada);
                10-Perigosa (conteinerizada); 11-Perigosa (carga geral).
            :ivar x_prod: Descrição do produto
            :ivar c_ean: GTIN (Global Trade Item Number) do produto,
                antigo código EAN ou código de barras
            :ivar ncm: Código NCM
            :ivar inf_lotacao: Informações da carga lotação. Informar
                somente quando MDF-e for de carga lotação
            """
            tp_carga: Optional[ProdPredTpCarga] = field(
                default=None,
                metadata={
                    "name": "tpCarga",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            x_prod: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xProd",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 120,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            c_ean: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cEAN",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"SEM GTIN|[0-9]{0}|[0-9]{8}|[0-9]{12,14}",
                }
            )
            ncm: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NCM",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2}|[0-9]{8}",
                }
            )
            inf_lotacao: Optional["Tmdfe.InfMdfe.ProdPred.InfLotacao"] = field(
                default=None,
                metadata={
                    "name": "infLotacao",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                }
            )

            @dataclass
            class InfLotacao:
                """
                :ivar inf_local_carrega: Informações da localização de
                    carregamento do MDF-e de carga lotação
                :ivar inf_local_descarrega: Informações da localização
                    de descarregamento do MDF-e de carga lotação
                """
                inf_local_carrega: Optional["Tmdfe.InfMdfe.ProdPred.InfLotacao.InfLocalCarrega"] = field(
                    default=None,
                    metadata={
                        "name": "infLocalCarrega",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                    }
                )
                inf_local_descarrega: Optional["Tmdfe.InfMdfe.ProdPred.InfLotacao.InfLocalDescarrega"] = field(
                    default=None,
                    metadata={
                        "name": "infLocalDescarrega",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/mdfe",
                        "required": True,
                    }
                )

                @dataclass
                class InfLocalCarrega:
                    """
                    :ivar cep: CEP onde foi carregado o MDF-e Informar
                        zeros não significativos
                    :ivar latitude: Latitude do ponto geográfico onde
                        foi carregado o MDF-e
                    :ivar longitude: Latitude do ponto geográfico onde
                        foi carregado o MDF-e
                    """
                    cep: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "CEP",
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
                    :ivar cep: CEP onde foi descarregado o MDF-e
                        Informar zeros não significativos
                    :ivar latitude: Latitude do ponto geográfico onde
                        foi descarregado o MDF-e
                    :ivar longitude: Latitude do ponto geográfico onde
                        foi descarregado o MDF-e
                    """
                    cep: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "CEP",
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
            :ivar q_cte: Quantidade total de CT-e relacionados no
                Manifesto
            :ivar q_nfe: Quantidade total de NF-e relacionadas no
                Manifesto
            :ivar q_mdfe: Quantidade total de MDF-e relacionados no
                Manifesto Aquaviário
            :ivar v_carga: Valor total da carga / mercadorias
                transportadas
            :ivar c_unid: Código da unidade de medida do Peso Bruto da
                Carga / Mercadorias transportadas 01 – KG;  02 - TON
            :ivar q_carga: Peso Bruto Total da Carga / Mercadorias
                transportadas
            """
            q_cte: Optional[str] = field(
                default=None,
                metadata={
                    "name": "qCTe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1,6}",
                }
            )
            q_nfe: Optional[str] = field(
                default=None,
                metadata={
                    "name": "qNFe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "pattern": r"[0-9]{1,6}",
                }
            )
            q_mdfe: Optional[str] = field(
                default=None,
                metadata={
                    "name": "qMDFe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "pattern": r"[0-9]{1,6}",
                }
            )
            v_carga: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vCarga",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            c_unid: Optional[TotCUnid] = field(
                default=None,
                metadata={
                    "name": "cUnid",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "required": True,
                }
            )
            q_carga: Optional[str] = field(
                default=None,
                metadata={
                    "name": "qCarga",
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
            :ivar n_lacre: número do lacre
            """
            n_lacre: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nLacre",
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
            :ivar cnpj: CNPJ do autorizado Informar zeros não
                significativos
            :ivar cpf: CPF do autorizado Informar zeros não
                significativos
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )

        @dataclass
        class InfAdic:
            """
            :ivar inf_ad_fisco: Informações adicionais de interesse do
                Fisco Norma referenciada, informações complementares,
                etc
            :ivar inf_cpl: Informações complementares de interesse do
                Contribuinte
            """
            inf_ad_fisco: Optional[str] = field(
                default=None,
                metadata={
                    "name": "infAdFisco",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/mdfe",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            inf_cpl: Optional[str] = field(
                default=None,
                metadata={
                    "name": "infCpl",
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
            :ivar x_solic: Solicitação do pedido de emissão da NFF. Será
                preenchido com a totalidade de campos informados no
                aplicativo emissor serializado.
            """
            x_solic: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xSolic",
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
        :ivar qr_cod_mdfe: Texto com o QR-Code para consulta do MDF-e
        """
        qr_cod_mdfe: Optional[str] = field(
            default=None,
            metadata={
                "name": "qrCodMDFe",
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

    id_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "idLote",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,15}",
        }
    )
    mdfe: Optional[Tmdfe] = field(
        default=None,
        metadata={
            "name": "MDFe",
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
