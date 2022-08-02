from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bindings.cte.v3_0.evento_cte_tipos_basico_v3_00 import TmodTransp
from nfelib.bindings.cte.v3_0.tipos_geral_cte_v3_00 import (
    Tamb,
    TcodUfIbge,
    TmodCt,
    TmodCtos,
    TmodGtve,
    TmodNf,
    TufSemEx,
    Tuf,
    TtipoUnidCarga,
    TtipoUnidTransp,
)
from nfelib.bindings.cte.v3_0.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class CompTpComp(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class Icms00Cst(Enum):
    VALUE_00 = "00"


class Icms20Cst(Enum):
    VALUE_20 = "20"


class Icms45Cst(Enum):
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_51 = "51"


class Icms60Cst(Enum):
    VALUE_60 = "60"


class Icms90Cst(Enum):
    VALUE_90 = "90"


class IcmsoutraUfCst(Enum):
    VALUE_90 = "90"


class IcmssnCst(Enum):
    VALUE_90 = "90"


class IcmssnIndSn(Enum):
    VALUE_1 = "1"


class TdocAssoc(Enum):
    """
    Tipo Documento Associado.
    """
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"


class TfinCte(Enum):
    """
    Tipo Finalidade da CT-e.
    """
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TfinGtve(Enum):
    """
    Tipo Finalidade da GTV-e.
    """
    VALUE_4 = "4"


class TmodDoc(Enum):
    """
    Tipo Modelo do Documento.
    """
    VALUE_01 = "01"
    VALUE_1_B = "1B"
    VALUE_02 = "02"
    VALUE_2_D = "2D"
    VALUE_2_E = "2E"
    VALUE_04 = "04"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_8_B = "8B"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_55 = "55"


class TmodTranspOs(Enum):
    """
    Tipo Modal transporte Outros Serviços.
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"


class TprocEmi(Enum):
    """
    Tipo processo de emissão do CT-e.
    """
    VALUE_0 = "0"
    VALUE_3 = "3"


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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[^@]+@[^\.]+\..+",
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "pattern": r"[0-9]{3}",
        }
    )
    hash_csrt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "hashCSRT",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "length": 20,
            "format": "base64",
        }
    )


class ComDataTpPer(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class ComHoraTpHor(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class IdeIndGlobalizado(Enum):
    VALUE_1 = "1"


class IdeIndIetoma(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_9 = "9"


class IdeModal(Enum):
    VALUE_01 = "01"
    VALUE_06 = "06"


class IdeRetira(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class IdeTpEmis(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_7 = "7"
    VALUE_8 = "8"


class IdeTpImp(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


class IdeTpServ(Enum):
    VALUE_9 = "9"


class InfCteSubIndAlteraToma(Enum):
    VALUE_1 = "1"


class InfEspecieTpEspecie(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


class InfEspecieTpNumerario(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


class InfOutrosTpDoc(Enum):
    VALUE_00 = "00"
    VALUE_10 = "10"
    VALUE_59 = "59"
    VALUE_65 = "65"
    VALUE_99 = "99"


class InfQCUnid(Enum):
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"


class NoInterTpHor(Enum):
    VALUE_4 = "4"


class NoPeriodoTpPer(Enum):
    VALUE_4 = "4"


class SegRespSeg(Enum):
    VALUE_4 = "4"
    VALUE_5 = "5"


class SemDataTpPer(Enum):
    VALUE_0 = "0"


class SemHoraTpHor(Enum):
    VALUE_0 = "0"


class Toma3Toma(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class Toma4Toma(Enum):
    VALUE_4 = "4"


class TomaTerceiroToma(Enum):
    VALUE_4 = "4"


class TomaToma(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


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
    :ivar x_mun: Nome do município Informar EXTERIOR para operações com
        o exterior.
    :ivar cep: CEP
    :ivar uf: Sigla da UF Informar EX para operações com o exterior.
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    c_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "cPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    x_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "xPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{6,14}",
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
    :ivar c_mun: Código do município (utilizar a tabela do IBGE)
        Informar 9999999 para operações com o exterior.
    :ivar x_mun: Nome do município Informar EXTERIOR para operações com
        o exterior.
    :ivar uf: Sigla da UF Informar EX para operações com o exterior.
    """
    class Meta:
        name = "TEndReEnt"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    x_nome: Optional[str] = field(
        default=None,
        metadata={
            "name": "xNome",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
    :ivar c_mun: Código do município (utilizar a tabela do IBGE)
    :ivar x_mun: Nome do município
    :ivar cep: CEP Informar zeros não significativos
    :ivar uf: Sigla da UF
    :ivar fone: Telefone
    """
    class Meta:
        name = "TEndeEmi"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: Optional[TufSemEx] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{6,14}",
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
    :ivar c_mun: Código do município (utilizar a tabela do IBGE)
        Informar 9999999 para operações com o exterior.
    :ivar x_mun: Nome do município Informar EXTERIOR para operações com
        o exterior.
    :ivar cep: CEP Informar os zeros não significativos
    :ivar uf: Sigla da UF Informar EX para operações com o exterior.
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 2,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    c_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "cPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    x_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "xPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "min_length": 2,
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
    :ivar uf: Sigla da UF Informar EX para operações com o exterior.
    """
    class Meta:
        name = "TEndernac"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )


@dataclass
class Timp:
    """
    Tipo Dados do Imposto CT-e.

    :ivar icms00: Prestação sujeito à tributação normal do ICMS
    :ivar icms20: Prestação sujeito à tributação com redução de BC do
        ICMS
    :ivar icms45: ICMS  Isento, não Tributado ou diferido
    :ivar icms60: Tributação pelo ICMS60 - ICMS cobrado por substituição
        tributária.Responsabilidade do recolhimento do ICMS atribuído ao
        tomador ou 3º por ST
    :ivar icms90: ICMS Outros
    :ivar icmsoutra_uf: ICMS devido à UF de origem da prestação, quando
        diferente da UF do emitente
    :ivar icmssn: Simples Nacional
    """
    class Meta:
        name = "TImp"

    icms00: Optional["Timp.Icms00"] = field(
        default=None,
        metadata={
            "name": "ICMS00",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    icms20: Optional["Timp.Icms20"] = field(
        default=None,
        metadata={
            "name": "ICMS20",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    icms45: Optional["Timp.Icms45"] = field(
        default=None,
        metadata={
            "name": "ICMS45",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    icms60: Optional["Timp.Icms60"] = field(
        default=None,
        metadata={
            "name": "ICMS60",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    icms90: Optional["Timp.Icms90"] = field(
        default=None,
        metadata={
            "name": "ICMS90",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    icmsoutra_uf: Optional["Timp.IcmsoutraUf"] = field(
        default=None,
        metadata={
            "name": "ICMSOutraUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    icmssn: Optional["Timp.Icmssn"] = field(
        default=None,
        metadata={
            "name": "ICMSSN",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )

    @dataclass
    class Icms00:
        """
        :ivar cst: classificação Tributária do Serviço 00 - tributação
            normal ICMS
        :ivar v_bc: Valor da BC do ICMS
        :ivar p_icms: Alíquota do ICMS
        :ivar v_icms: Valor do ICMS
        """
        cst: Optional[Icms00Cst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        v_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "vBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        p_icms: Optional[str] = field(
            default=None,
            metadata={
                "name": "pICMS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_icms: Optional[str] = field(
            default=None,
            metadata={
                "name": "vICMS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass
    class Icms20:
        """
        :ivar cst: Classificação Tributária do serviço 20 - tributação
            com BC reduzida do ICMS
        :ivar p_red_bc: Percentual de redução da BC
        :ivar v_bc: Valor da BC do ICMS
        :ivar p_icms: Alíquota do ICMS
        :ivar v_icms: Valor do ICMS
        """
        cst: Optional[Icms20Cst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        p_red_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "pRedBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "vBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        p_icms: Optional[str] = field(
            default=None,
            metadata={
                "name": "pICMS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_icms: Optional[str] = field(
            default=None,
            metadata={
                "name": "vICMS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass
    class Icms45:
        """
        :ivar cst: Classificação Tributária do Serviço Preencher com: 40
            - ICMS isenção; 41 - ICMS não tributada; 51 - ICMS diferido
        """
        cst: Optional[Icms45Cst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )

    @dataclass
    class Icms60:
        """
        :ivar cst: Classificação Tributária do Serviço 60 - ICMS cobrado
            por substituição tributária
        :ivar v_bcstret: Valor da BC do ICMS ST retido Valor do frete
            sobre o qual será calculado o ICMS a ser substituído na
            Prestação.
        :ivar v_icmsstret: Valor do ICMS ST retido Resultado da
            multiplicação do “vBCSTRet” x “pICMSSTRet” – que será valor
            do ICMS a ser retido pelo Substituto. Podendo o valor do
            ICMS a ser retido efetivamente, sofrer ajustes conforme a
            opção tributaria do transportador substituído.
        :ivar p_icmsstret: Alíquota do ICMS Percentual de Alíquota
            incidente na prestação de serviço de transporte.
        :ivar v_cred: Valor do Crédito outorgado/Presumido Preencher
            somente quando o transportador substituído, for optante pelo
            crédito outorgado previsto no Convênio 106/96 e corresponde
            ao percentual de 20% do valor do ICMS ST retido.
        """
        cst: Optional[Icms60Cst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        v_bcstret: Optional[str] = field(
            default=None,
            metadata={
                "name": "vBCSTRet",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_icmsstret: Optional[str] = field(
            default=None,
            metadata={
                "name": "vICMSSTRet",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        p_icmsstret: Optional[str] = field(
            default=None,
            metadata={
                "name": "pICMSSTRet",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_cred: Optional[str] = field(
            default=None,
            metadata={
                "name": "vCred",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass
    class Icms90:
        """
        :ivar cst: Classificação Tributária do Serviço 90 - ICMS outros
        :ivar p_red_bc: Percentual de redução da BC
        :ivar v_bc: Valor da BC do ICMS
        :ivar p_icms: Alíquota do ICMS
        :ivar v_icms: Valor do ICMS
        :ivar v_cred: Valor do Crédito Outorgado/Presumido
        """
        cst: Optional[Icms90Cst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        p_red_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "pRedBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "vBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        p_icms: Optional[str] = field(
            default=None,
            metadata={
                "name": "pICMS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_icms: Optional[str] = field(
            default=None,
            metadata={
                "name": "vICMS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cred: Optional[str] = field(
            default=None,
            metadata={
                "name": "vCred",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass
    class IcmsoutraUf:
        """
        :ivar cst: Classificação Tributária do Serviço 90 - ICMS Outra
            UF
        :ivar p_red_bcoutra_uf: Percentual de redução da BC
        :ivar v_bcoutra_uf: Valor da BC do ICMS
        :ivar p_icmsoutra_uf: Alíquota do ICMS
        :ivar v_icmsoutra_uf: Valor do ICMS devido outra UF
        """
        cst: Optional[IcmsoutraUfCst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        p_red_bcoutra_uf: Optional[str] = field(
            default=None,
            metadata={
                "name": "pRedBCOutraUF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_bcoutra_uf: Optional[str] = field(
            default=None,
            metadata={
                "name": "vBCOutraUF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        p_icmsoutra_uf: Optional[str] = field(
            default=None,
            metadata={
                "name": "pICMSOutraUF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_icmsoutra_uf: Optional[str] = field(
            default=None,
            metadata={
                "name": "vICMSOutraUF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass
    class Icmssn:
        """
        :ivar cst: Classificação Tributária do Serviço 90 - ICMS Simples
            Nacional
        :ivar ind_sn: Indica se o contribuinte é Simples Nacional
            1=Sim
        """
        cst: Optional[IcmssnCst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        ind_sn: Optional[IcmssnIndSn] = field(
            default=None,
            metadata={
                "name": "indSN",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )


@dataclass
class TimpOs:
    """
    Tipo Dados do Imposto para CT-e OS.

    :ivar icms00: Prestação sujeito à tributação normal do ICMS
    :ivar icms20: Prestação sujeito à tributação com redução de BC do
        ICMS
    :ivar icms45: ICMS  Isento, não Tributado ou diferido
    :ivar icms90: ICMS Outros
    :ivar icmsoutra_uf: ICMS devido à UF de origem da prestação, quando
        diferente da UF do emitente
    :ivar icmssn: Simples Nacional
    """
    class Meta:
        name = "TImpOS"

    icms00: Optional["TimpOs.Icms00"] = field(
        default=None,
        metadata={
            "name": "ICMS00",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    icms20: Optional["TimpOs.Icms20"] = field(
        default=None,
        metadata={
            "name": "ICMS20",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    icms45: Optional["TimpOs.Icms45"] = field(
        default=None,
        metadata={
            "name": "ICMS45",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    icms90: Optional["TimpOs.Icms90"] = field(
        default=None,
        metadata={
            "name": "ICMS90",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    icmsoutra_uf: Optional["TimpOs.IcmsoutraUf"] = field(
        default=None,
        metadata={
            "name": "ICMSOutraUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    icmssn: Optional["TimpOs.Icmssn"] = field(
        default=None,
        metadata={
            "name": "ICMSSN",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )

    @dataclass
    class Icms00:
        """
        :ivar cst: classificação Tributária do Serviço 00 - tributação
            normal ICMS
        :ivar v_bc: Valor da BC do ICMS
        :ivar p_icms: Alíquota do ICMS
        :ivar v_icms: Valor do ICMS
        """
        cst: Optional[Icms00Cst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        v_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "vBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        p_icms: Optional[str] = field(
            default=None,
            metadata={
                "name": "pICMS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_icms: Optional[str] = field(
            default=None,
            metadata={
                "name": "vICMS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass
    class Icms20:
        """
        :ivar cst: Classificação Tributária do serviço 20 - tributação
            com BC reduzida do ICMS
        :ivar p_red_bc: Percentual de redução da BC
        :ivar v_bc: Valor da BC do ICMS
        :ivar p_icms: Alíquota do ICMS
        :ivar v_icms: Valor do ICMS
        """
        cst: Optional[Icms20Cst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        p_red_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "pRedBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "vBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        p_icms: Optional[str] = field(
            default=None,
            metadata={
                "name": "pICMS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_icms: Optional[str] = field(
            default=None,
            metadata={
                "name": "vICMS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass
    class Icms45:
        """
        :ivar cst: Classificação Tributária do Serviço Preencher com: 40
            - ICMS isenção; 41 - ICMS não tributada; 51 - ICMS diferido
        """
        cst: Optional[Icms45Cst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )

    @dataclass
    class Icms90:
        """
        :ivar cst: Classificação Tributária do Serviço 90 - Outros
        :ivar p_red_bc: Percentual de redução da BC
        :ivar v_bc: Valor da BC do ICMS
        :ivar p_icms: Alíquota do ICMS
        :ivar v_icms: Valor do ICMS
        :ivar v_cred: Valor do Crédito Outorgado/Presumido
        """
        cst: Optional[Icms90Cst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        p_red_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "pRedBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "vBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        p_icms: Optional[str] = field(
            default=None,
            metadata={
                "name": "pICMS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_icms: Optional[str] = field(
            default=None,
            metadata={
                "name": "vICMS",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        v_cred: Optional[str] = field(
            default=None,
            metadata={
                "name": "vCred",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass
    class IcmsoutraUf:
        """
        :ivar cst: Classificação Tributária do Serviço 90 - ICMS Outra
            UF
        :ivar p_red_bcoutra_uf: Percentual de redução da BC
        :ivar v_bcoutra_uf: Valor da BC do ICMS
        :ivar p_icmsoutra_uf: Alíquota do ICMS
        :ivar v_icmsoutra_uf: Valor do ICMS devido outra UF
        """
        cst: Optional[IcmsoutraUfCst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        p_red_bcoutra_uf: Optional[str] = field(
            default=None,
            metadata={
                "name": "pRedBCOutraUF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_bcoutra_uf: Optional[str] = field(
            default=None,
            metadata={
                "name": "vBCOutraUF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        p_icmsoutra_uf: Optional[str] = field(
            default=None,
            metadata={
                "name": "pICMSOutraUF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_icmsoutra_uf: Optional[str] = field(
            default=None,
            metadata={
                "name": "vICMSOutraUF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass
    class Icmssn:
        """
        :ivar cst: Classificação Tributária do Serviço 90 - ICMS Simples
            Nacional
        :ivar ind_sn: Indica se o contribuinte é Simples Nacional
            1=Sim
        """
        cst: Optional[IcmssnCst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        ind_sn: Optional[IcmssnIndSn] = field(
            default=None,
            metadata={
                "name": "indSN",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )


@dataclass
class TprotCte:
    """
    Tipo Protocolo de status resultado do processamento da CT-e.

    :ivar inf_prot: Dados do protocolo de status
    :ivar inf_fisco: Mensagem do Fisco
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TProtCTe"

    inf_prot: Optional["TprotCte.InfProt"] = field(
        default=None,
        metadata={
            "name": "infProt",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    inf_fisco: Optional["TprotCte.InfFisco"] = field(
        default=None,
        metadata={
            "name": "infFisco",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
        :ivar ver_aplic: Versão do Aplicativo que processou o CT-e
        :ivar ch_cte: Chaves de acesso da CT-e,
        :ivar dh_recbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS TZD.
        :ivar n_prot: Número do Protocolo de Status do CT-e.
        :ivar dig_val: Digest Value da CT-e processado. Utilizado para
            conferir a integridade do CT-e original.
        :ivar c_stat: Código do status do CT-e.
        :ivar x_motivo: Descrição literal do status do CT-e.
        :ivar id:
        """
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        ver_aplic: Optional[str] = field(
            default=None,
            metadata={
                "name": "verAplic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        ch_cte: Optional[str] = field(
            default=None,
            metadata={
                "name": "chCTe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        dig_val: Optional[bytes] = field(
            default=None,
            metadata={
                "name": "digVal",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "format": "base64",
            }
        )
        c_stat: Optional[str] = field(
            default=None,
            metadata={
                "name": "cStat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )


@dataclass
class TprotCteOs:
    """
    Tipo Protocolo de status resultado do processamento do CT-e OS (Modelo 67)

    :ivar inf_prot: Dados do protocolo de status
    :ivar inf_fisco: Mensagem do Fisco
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TProtCTeOS"

    inf_prot: Optional["TprotCteOs.InfProt"] = field(
        default=None,
        metadata={
            "name": "infProt",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    inf_fisco: Optional["TprotCteOs.InfFisco"] = field(
        default=None,
        metadata={
            "name": "infFisco",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
        :ivar ver_aplic: Versão do Aplicativo que processou o CT-e
        :ivar ch_cte: Chaves de acesso da CT-e
        :ivar dh_recbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS TZD.
        :ivar n_prot: Número do Protocolo de Status do CT-e.
        :ivar dig_val: Digest Value da CT-e processado. Utilizado para
            conferir a integridade do CT-e original.
        :ivar c_stat: Código do status do CT-e.
        :ivar x_motivo: Descrição literal do status do CT-e.
        :ivar id:
        """
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        ver_aplic: Optional[str] = field(
            default=None,
            metadata={
                "name": "verAplic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        ch_cte: Optional[str] = field(
            default=None,
            metadata={
                "name": "chCTe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        dig_val: Optional[bytes] = field(
            default=None,
            metadata={
                "name": "digVal",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "format": "base64",
            }
        )
        c_stat: Optional[str] = field(
            default=None,
            metadata={
                "name": "cStat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )


@dataclass
class TprotGtve:
    """
    Tipo Protocolo de status resultado do processamento da GTV-e (Modelo 64)

    :ivar inf_prot: Dados do protocolo de status
    :ivar inf_fisco: Mensagem do Fisco
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TProtGTVe"

    inf_prot: Optional["TprotGtve.InfProt"] = field(
        default=None,
        metadata={
            "name": "infProt",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    inf_fisco: Optional["TprotGtve.InfFisco"] = field(
        default=None,
        metadata={
            "name": "infFisco",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
        :ivar ver_aplic: Versão do Aplicativo que processou a GTV-e
        :ivar ch_cte: Chaves de acesso da CT-e
        :ivar dh_recbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS TZD.
        :ivar n_prot: Número do Protocolo de Status da GTV-e
        :ivar dig_val: Digest Value da GTV-e processado. Utilizado para
            conferir a integridade da GTV-e original.
        :ivar c_stat: Código do status da GTV-e.
        :ivar x_motivo: Descrição literal do status da GTV-e.
        :ivar id:
        """
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        ver_aplic: Optional[str] = field(
            default=None,
            metadata={
                "name": "verAplic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        ch_cte: Optional[str] = field(
            default=None,
            metadata={
                "name": "chCTe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        dig_val: Optional[bytes] = field(
            default=None,
            metadata={
                "name": "digVal",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "format": "base64",
            }
        )
        c_stat: Optional[str] = field(
            default=None,
            metadata={
                "name": "cStat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )


@dataclass
class TretEnviCte:
    """
    Tipo Retorno do Pedido de Concessão de Autorização da CT-e.

    :ivar tp_amb: Identificação do Ambiente:1 - Produção; 2 -
        Homologação
    :ivar c_uf: Identificação da UF
    :ivar ver_aplic: Versão do Aplicativo que recebeu o Lote.
    :ivar c_stat: Código do status da mensagem enviada.
    :ivar x_motivo: Descrição literal do status do serviço solicitado.
    :ivar inf_rec: Dados do Recibo do Lote
    :ivar versao:
    """
    class Meta:
        name = "TRetEnviCTe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    c_uf: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    inf_rec: Optional["TretEnviCte.InfRec"] = field(
        default=None,
        metadata={
            "name": "infRec",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            DDTHH:MM:SS TZD
        :ivar t_med: Tempo médio de resposta do serviço (em segundos)
            dos últimos 5 minutos
        """
        n_rec: Optional[str] = field(
            default=None,
            metadata={
                "name": "nRec",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        dh_recbto: Optional[str] = field(
            default=None,
            metadata={
                "name": "dhRecbto",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        t_med: Optional[str] = field(
            default=None,
            metadata={
                "name": "tMed",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "pattern": r"[0-9]{1,4}",
            }
        )


@dataclass
class TunidCarga:
    """
    Tipo Dados Unidade de Carga.

    :ivar tp_unid_carga: Tipo da Unidade de Carga 1 - Container 2 - ULD
        3 - Pallet 4 - Outros
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    id_unid_carga: Optional[str] = field(
        default=None,
        metadata={
            "name": "idUnidCarga",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    qtd_rat: Optional[str] = field(
        default=None,
        metadata={
            "name": "qtdRat",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )


@dataclass
class TcteOs:
    """
    Tipo Conhecimento de Transporte Eletrônico Outros Serviços (Modelo 67)

    :ivar inf_cte: Informações do CT-e Outros Serviços
    :ivar inf_cte_supl: Informações suplementares do CT-e
    :ivar signature:
    :ivar versao: Versão do leiaute
    """
    class Meta:
        name = "TCTeOS"

    inf_cte: Optional["TcteOs.InfCte"] = field(
        default=None,
        metadata={
            "name": "infCte",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    inf_cte_supl: Optional["TcteOs.InfCteSupl"] = field(
        default=None,
        metadata={
            "name": "infCTeSupl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "pattern": r"3\.00",
        }
    )

    @dataclass
    class InfCte:
        """
        :ivar ide: Identificação do CT-e Outros Serviços
        :ivar compl: Dados complementares do CT-e para fins operacionais
            ou comerciais
        :ivar emit: Identificação do Emitente do CT-e OS
        :ivar toma: Informações do Tomador/Usuário do Serviço Opcional
            para Excesso de Bagagem
        :ivar v_prest: Valores da Prestação de Serviço
        :ivar imp: Informações relativas aos Impostos
        :ivar inf_cte_norm: Grupo de informações do CT-e OS Normal
        :ivar inf_cte_comp: Detalhamento do CT-e complementado
        :ivar inf_cte_anu: Detalhamento do CT-e do tipo Anulação
        :ivar aut_xml: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar inf_resp_tec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar versao: Versão do leiaute Ex: "3.00"
        :ivar id: Identificador da tag a ser assinada Informar a chave
            de acesso do CT-e OS e precedida do literal "CTe"
        """
        ide: Optional["TcteOs.InfCte.Ide"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        compl: Optional["TcteOs.InfCte.Compl"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        emit: Optional["TcteOs.InfCte.Emit"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        toma: Optional["TcteOs.InfCte.Toma"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        v_prest: Optional["TcteOs.InfCte.VPrest"] = field(
            default=None,
            metadata={
                "name": "vPrest",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        imp: Optional["TcteOs.InfCte.Imp"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        inf_cte_norm: Optional["TcteOs.InfCte.InfCteNorm"] = field(
            default=None,
            metadata={
                "name": "infCTeNorm",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        inf_cte_comp: Optional["TcteOs.InfCte.InfCteComp"] = field(
            default=None,
            metadata={
                "name": "infCteComp",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        inf_cte_anu: Optional["TcteOs.InfCte.InfCteAnu"] = field(
            default=None,
            metadata={
                "name": "infCteAnu",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        aut_xml: List["TcteOs.InfCte.AutXml"] = field(
            default_factory=list,
            metadata={
                "name": "autXML",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "max_occurs": 10,
            }
        )
        inf_resp_tec: Optional[TrespTec] = field(
            default=None,
            metadata={
                "name": "infRespTec",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "pattern": r"CTe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar c_uf: Código da UF do emitente do CT-e. Utilizar a
                Tabela do IBGE.
            :ivar c_ct: Código numérico que compõe a Chave de Acesso.
                Número aleatório gerado pelo emitente para cada CT-e,
                com o objetivo de evitar acessos indevidos ao documento.
            :ivar cfop: Código Fiscal de Operações e Prestações
            :ivar nat_op: Natureza da Operação
            :ivar mod: Modelo do documento fiscal Utilizar o código 67
                para identificação do CT-e Outros Serviços, emitido em
                substituição a Nota Fiscal Modelo 7 para transporte de
                pessoas, valores e excesso de bagagem.
            :ivar serie: Série do CT-e OS Preencher com "0" no caso de
                série única
            :ivar n_ct: Número do CT-e OS
            :ivar dh_emi: Data e hora de emissão do CT-e OS Formato
                AAAA-MM-DDTHH:MM:DD TZD
            :ivar tp_imp: Formato de impressão do DACTE OS Preencher
                com: 1 - Retrato; 2 - Paisagem.
            :ivar tp_emis: Forma de emissão do CT-e Preencher com: 1 -
                Normal; 5 - Contingência FSDA; 7 - Autorização pela SVC-
                RS; 8 - Autorização pela SVC-SP
            :ivar c_dv: Digito Verificador da chave de acesso do CT-e
                Informar o dígito  de controle da chave de acesso do
                CT-e, que deve ser calculado com a aplicação do
                algoritmo módulo 11 (base 2,9) da chave de acesso.
            :ivar tp_amb: Tipo do Ambiente Preencher com:1 - Produção; 2
                - Homologação
            :ivar tp_cte: Tipo do CT-e OS Preencher com: 0 - CT-e
                Normal; 1 - CT-e Complementar; 2 - CT-e de Anulação; 3 -
                CT-e de Substituição.
            :ivar proc_emi: Identificador do processo de emissão do CT-e
                OS Preencher com: 0 - emissão de CT-e com aplicativo do
                contribuinte; 3- emissão CT-e pelo contribuinte com
                aplicativo fornecido pelo Fisco.
            :ivar ver_proc: Versão do processo de emissão Iinformar a
                versão do aplicativo emissor de CT-e.
            :ivar c_mun_env: Código do Município de envio do CT-e (de
                onde o documento foi transmitido) Utilizar a tabela do
                IBGE. Informar 9999999 para as operações com o exterior.
            :ivar x_mun_env: Nome do Município de envio do CT-e (de onde
                o documento foi transmitido) Informar PAIS/Municipio
                para as operações com o exterior.
            :ivar ufenv: Sigla da UF de envio do CT-e (de onde o
                documento foi transmitido) Informar 'EX' para operações
                com o exterior.
            :ivar modal: Modal do CT-e OS Preencher com: 01-Rodoviário;
                02- Aéreo; 03 - Aquaviário; 04 - Ferroviário.
            :ivar tp_serv: Tipo do Serviço Preencher com: 6 - Transporte
                de Pessoas; 7 - Transporte de Valores; 8 - Excesso de
                Bagagem.
            :ivar ind_ietoma: Indicador da IE do tomador: 1 –
                Contribuinte ICMS; 2 – Contribuinte isento de inscrição;
                9 – Não Contribuinte Aplica-se ao tomador que for
                indicado no toma3 ou toma4
            :ivar c_mun_ini: Código do Município de início da prestação
                Utilizar a tabela do IBGE. Informar 9999999 para
                operações com o exterior.
            :ivar x_mun_ini: Nome do Município do início da prestação
                Informar 'EXTERIOR' para operações com o exterior.
            :ivar ufini: UF do início da prestação Informar 'EX' para
                operações com o exterior.
            :ivar c_mun_fim: Código do Município de término da prestação
                Utilizar a tabela do IBGE. Informar 9999999 para
                operações com o exterior.
            :ivar x_mun_fim: Nome do Município do término da prestação
                Informar 'EXTERIOR' para operações com o exterior.
            :ivar uffim: UF do término da prestação Informar 'EX' para
                operações com o exterior.
            :ivar inf_percurso: Informações do Percurso do CT-e Outros
                Serviços
            :ivar dh_cont: Data e Hora da entrada em contingência
                Informar a data e hora no formato AAAA-MM-DDTHH:MM:SS
            :ivar x_just: Justificativa da entrada em contingência
            """
            c_uf: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "name": "cUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            c_ct: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cCT",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            cfop: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CFOP",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[123567][0-9]([0-9][1-9]|[1-9][0-9])",
                }
            )
            nat_op: Optional[str] = field(
                default=None,
                metadata={
                    "name": "natOp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            mod: Optional[TmodCtos] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            serie: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                }
            )
            n_ct: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nCT",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            dh_emi: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tp_imp: Optional[IdeTpImp] = field(
                default=None,
                metadata={
                    "name": "tpImp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tp_emis: Optional[IdeTpEmis] = field(
                default=None,
                metadata={
                    "name": "tpEmis",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            c_dv: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cDV",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
                }
            )
            tp_amb: Optional[Tamb] = field(
                default=None,
                metadata={
                    "name": "tpAmb",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            tp_cte: Optional[TfinCte] = field(
                default=None,
                metadata={
                    "name": "tpCTe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            proc_emi: Optional[TprocEmi] = field(
                default=None,
                metadata={
                    "name": "procEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            ver_proc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "verProc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            c_mun_env: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cMunEnv",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            x_mun_env: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xMunEnv",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ufenv: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UFEnv",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            modal: Optional[TmodTranspOs] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            tp_serv: Optional[IdeTpServ] = field(
                default=None,
                metadata={
                    "name": "tpServ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            ind_ietoma: Optional[IdeIndIetoma] = field(
                default=None,
                metadata={
                    "name": "indIEToma",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            c_mun_ini: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cMunIni",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            x_mun_ini: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xMunIni",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ufini: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UFIni",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            c_mun_fim: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cMunFim",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            x_mun_fim: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xMunFim",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            uffim: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UFFim",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            inf_percurso: List["TcteOs.InfCte.Ide.InfPercurso"] = field(
                default_factory=list,
                metadata={
                    "name": "infPercurso",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_occurs": 25,
                }
            )
            dh_cont: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            x_just: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xJust",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 15,
                    "max_length": 256,
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
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                    }
                )

        @dataclass
        class Compl:
            """
            :ivar x_carac_ad: Característica adicional do transporte
                Texto livre: REENTREGA; DEVOLUÇÃO; REFATURAMENTO; etc
            :ivar x_carac_ser: Característica adicional do serviço Texto
                livre: ENTREGA EXPRESSA; LOGÍSTICA REVERSA;
                CONVENCIONAL; EMERGENCIAL; etc
            :ivar x_emi: Funcionário emissor do CTe
            :ivar x_obs: Observações Gerais
            :ivar obs_cont: Campo de uso livre do contribuinte Informar
                o nome do campo no atributo xCampo e o conteúdo do campo
                no XTexto
            :ivar obs_fisco: Campo de uso livre do contribuinte Informar
                o nome do campo no atributo xCampo e o conteúdo do campo
                no XTexto
            """
            x_carac_ad: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xCaracAd",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_carac_ser: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xCaracSer",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 30,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_emi: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_obs: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xObs",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            obs_cont: List["TcteOs.InfCte.Compl.ObsCont"] = field(
                default_factory=list,
                metadata={
                    "name": "ObsCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_occurs": 10,
                }
            )
            obs_fisco: List["TcteOs.InfCte.Compl.ObsFisco"] = field(
                default_factory=list,
                metadata={
                    "name": "ObsFisco",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_occurs": 10,
                }
            )

            @dataclass
            class ObsCont:
                """
                :ivar x_texto: Conteúdo do campo
                :ivar x_campo: Identificação do campo
                """
                x_texto: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xTexto",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 160,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                x_campo: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xCampo",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )

            @dataclass
            class ObsFisco:
                """
                :ivar x_texto: Conteúdo do campo
                :ivar x_campo: Identificação do campo
                """
                x_texto: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xTexto",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                x_campo: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xCampo",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )

        @dataclass
        class Emit:
            """
            :ivar cnpj: CNPJ do emitente Informar zeros não
                significativos
            :ivar ie: Inscrição Estadual do Emitente
            :ivar iest: Inscrição Estadual do Substituto Tributário
            :ivar x_nome: Razão social ou Nome do emitente
            :ivar x_fant: Nome fantasia
            :ivar ender_emit: Endereço do emitente
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            iest: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IEST",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )

        @dataclass
        class Toma:
            """
            :ivar cnpj: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar cpf: Número do CPF Informar os zeros não
                significativos.
            :ivar ie: Inscrição Estadual Informar a IE do tomador ou
                ISENTO se tomador é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                tomador não seja contribuinte do ICMS não informar o
                conteúdo.
            :ivar x_nome: Razão social ou nome do tomador
            :ivar x_fant: Nome fantasia
            :ivar fone: Telefone
            :ivar ender_toma: Dados do endereço
            :ivar email: Endereço de email
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            fone: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6,14}",
                }
            )
            ender_toma: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "name": "enderToma",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            email: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[^@]+@[^\.]+\..+",
                }
            )

        @dataclass
        class VPrest:
            """
            :ivar v_tprest: Valor Total da Prestação do Serviço Pode
                conter zeros quando o CT-e for de complemento de ICMS
            :ivar v_rec: Valor a Receber
            :ivar comp: Componentes do Valor da Prestação
            """
            v_tprest: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vTPrest",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_rec: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vRec",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            comp: List["TcteOs.InfCte.VPrest.Comp"] = field(
                default_factory=list,
                metadata={
                    "name": "Comp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )

            @dataclass
            class Comp:
                """
                :ivar x_nome: Nome do componente Exxemplos: FRETE PESO,
                    FRETE VALOR, SEC/CAT, ADEME, AGENDAMENTO, etc
                :ivar v_comp: Valor do componente
                """
                x_nome: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xNome",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 15,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                v_comp: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vComp",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

        @dataclass
        class Imp:
            """
            :ivar icms: Informações relativas ao ICMS
            :ivar v_tot_trib: Valor Total dos Tributos
            :ivar inf_ad_fisco: Informações adicionais de interesse do
                Fisco Norma referenciada, informações complementares,
                etc
            :ivar icmsuffim: Informações do ICMS de partilha com a UF de
                término do serviço de transporte na operação
                interestadual Grupo a ser informado nas prestações
                interestaduais para consumidor final, não contribuinte
                do ICMS
            :ivar inf_trib_fed: Informações dos tributos federais Grupo
                a ser informado nas prestações interestaduais para
                consumidor final, não contribuinte do ICMS
            """
            icms: Optional[TimpOs] = field(
                default=None,
                metadata={
                    "name": "ICMS",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            v_tot_trib: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vTotTrib",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            inf_ad_fisco: Optional[str] = field(
                default=None,
                metadata={
                    "name": "infAdFisco",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            icmsuffim: Optional["TcteOs.InfCte.Imp.Icmsuffim"] = field(
                default=None,
                metadata={
                    "name": "ICMSUFFim",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            inf_trib_fed: Optional["TcteOs.InfCte.Imp.InfTribFed"] = field(
                default=None,
                metadata={
                    "name": "infTribFed",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )

            @dataclass
            class Icmsuffim:
                """
                :ivar v_bcuffim: Valor da BC do ICMS na UF de término da
                    prestação do serviço de transporte
                :ivar p_fcpuffim: Percentual do ICMS relativo ao Fundo
                    de Combate à pobreza (FCP) na UF de término da
                    prestação do serviço de transporte Alíquota adotada
                    nas operações internas na UF do destinatário
                :ivar p_icmsuffim: Alíquota interna da UF de término da
                    prestação do serviço de transporte Alíquota adotada
                    nas operações internas na UF do destinatário
                :ivar p_icmsinter: Alíquota interestadual das UF
                    envolvidas Alíquota interestadual das UF envolvidas
                :ivar v_fcpuffim: Valor do ICMS relativo ao Fundo de
                    Combate á Pobreza (FCP) da UF de término da
                    prestação
                :ivar v_icmsuffim: Valor do ICMS de partilha para a UF
                    de término da prestação do serviço de transporte
                :ivar v_icmsufini: Valor do ICMS de partilha para a UF
                    de início da prestação do serviço de transporte
                """
                v_bcuffim: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vBCUFFim",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                p_fcpuffim: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "pFCPUFFim",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                p_icmsuffim: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "pICMSUFFim",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                p_icmsinter: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "pICMSInter",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                v_fcpuffim: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vFCPUFFim",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_icmsuffim: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vICMSUFFim",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_icmsufini: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vICMSUFIni",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

            @dataclass
            class InfTribFed:
                """
                :ivar v_pis: Valor do PIS
                :ivar v_cofins: Valor COFINS
                :ivar v_ir: Valor de Imposto de Renda
                :ivar v_inss: Valor do INSS
                :ivar v_csll: Valor do CSLL
                """
                v_pis: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vPIS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_cofins: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vCOFINS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_ir: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vIR",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_inss: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vINSS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_csll: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vCSLL",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )

        @dataclass
        class InfCteNorm:
            """
            :ivar inf_servico: Informações da Prestação do Serviço
            :ivar inf_doc_ref: Informações dos documentos referenciados
            :ivar seg: Informações de Seguro da Carga
            :ivar inf_modal: Informações do modal Obrigatório para
                Pessoas e Bagagem
            :ivar inf_cte_sub: Informações do CT-e de substituição
            :ivar ref_cte_canc: Chave de acesso do CT-e Cancelado
                Somente para Transporte de Valores
            :ivar cobr: Dados da cobrança do CT-e
            :ivar inf_gtve: Informações das GTV-e relacionadas ao CT-e
                OS
            """
            inf_servico: Optional["TcteOs.InfCte.InfCteNorm.InfServico"] = field(
                default=None,
                metadata={
                    "name": "infServico",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            inf_doc_ref: List["TcteOs.InfCte.InfCteNorm.InfDocRef"] = field(
                default_factory=list,
                metadata={
                    "name": "infDocRef",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            seg: List["TcteOs.InfCte.InfCteNorm.Seg"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            inf_modal: Optional["TcteOs.InfCte.InfCteNorm.InfModal"] = field(
                default=None,
                metadata={
                    "name": "infModal",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            inf_cte_sub: Optional["TcteOs.InfCte.InfCteNorm.InfCteSub"] = field(
                default=None,
                metadata={
                    "name": "infCteSub",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            ref_cte_canc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "refCTeCanc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 44,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{44}",
                }
            )
            cobr: Optional["TcteOs.InfCte.InfCteNorm.Cobr"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            inf_gtve: List["TcteOs.InfCte.InfCteNorm.InfGtve"] = field(
                default_factory=list,
                metadata={
                    "name": "infGTVe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )

            @dataclass
            class InfServico:
                """
                :ivar x_desc_serv: Descrição do Serviço prestado
                :ivar inf_q: Informações de quantidades da Carga do CT-e
                    Para Transporte de Pessoas indicar número de
                    passageiros, para excesso de bagagem e transporte de
                    valores indicar número de Volumes/Malotes
                """
                x_desc_serv: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xDescServ",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 30,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                inf_q: Optional["TcteOs.InfCte.InfCteNorm.InfServico.InfQ"] = field(
                    default=None,
                    metadata={
                        "name": "infQ",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )

                @dataclass
                class InfQ:
                    """
                    :ivar q_carga: Quantidade
                    """
                    q_carga: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "qCarga",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                        }
                    )

            @dataclass
            class InfDocRef:
                """
                :ivar n_doc: Número
                :ivar serie: Série
                :ivar subserie: Subsérie
                :ivar d_emi: Data de Emissão Formato AAAA-MM-DD
                :ivar v_doc: Valor Transportado
                :ivar ch_bpe: Chave de acesso do BP-e que possui eventos
                    excesso de bagagem
                """
                n_doc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nDoc",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                serie: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 3,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                subserie: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 3,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                d_emi: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "dEmi",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                    }
                )
                v_doc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vDoc",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                ch_bpe: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "chBPe",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "max_length": 44,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{44}",
                    }
                )

            @dataclass
            class Seg:
                """
                :ivar resp_seg: Responsável pelo seguro Preencher com: 4
                    - Emitente do CT-e; 5 - Tomador de Serviço.
                :ivar x_seg: Nome da Seguradora
                :ivar n_apol: Número da Apólice Obrigatório pela lei
                    11.442/07 (RCTRC)
                """
                resp_seg: Optional[SegRespSeg] = field(
                    default=None,
                    metadata={
                        "name": "respSeg",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 1,
                        "white_space": "preserve",
                    }
                )
                x_seg: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xSeg",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 30,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                n_apol: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nApol",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )

            @dataclass
            class InfModal:
                """
                :ivar any_element: XML do modal Insira neste local o XML
                    específico do modal O elemento do tipo -any- permite
                    estender o documento XML com elementos não
                    especificados pelo schema. Insira neste local - any-
                    o XML específico do modal (rodoviário). A
                    especificação do schema XML para cada modal pode ser
                    encontrada nos arquivos que acompanham este pacote
                    de liberação: Rodoviário - ver arquivo
                    CTeModalRodoviarioOS_v9.99 Onde v9.99 é a a
                    designação genérica para a versão do arquivo. Por
                    exemplo, o arquivo para o schema do modal Rodoviário
                    na versão 3.00 será denominado
                    "CTeModalRodoviarioOS_v3.00".
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
            class InfCteSub:
                """
                :ivar ch_cte: Chave de acesso do CT-e a ser substituído
                    (original)
                :ivar ref_cte_anu: Chave de acesso do CT-e de Anulação
                :ivar toma_icms: Tomador é contribuinte do ICMS, mas não
                    é emitente de documento fiscal eletrônico
                """
                ch_cte: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "chCte",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "pattern": r"[0-9]{44}",
                    }
                )
                ref_cte_anu: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "refCteAnu",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "max_length": 44,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{44}",
                    }
                )
                toma_icms: Optional["TcteOs.InfCte.InfCteNorm.InfCteSub.TomaIcms"] = field(
                    default=None,
                    metadata={
                        "name": "tomaICMS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )

                @dataclass
                class TomaIcms:
                    """
                    :ivar ref_nfe: Chave de acesso da NF-e emitida pelo
                        Tomador
                    :ivar ref_nf: Informação da NF ou CT emitido pelo
                        Tomador
                    :ivar ref_cte: Chave de acesso do CT-e emitido pelo
                        Tomador
                    """
                    ref_nfe: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "refNFe",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "max_length": 44,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{44}",
                        }
                    )
                    ref_nf: Optional["TcteOs.InfCte.InfCteNorm.InfCteSub.TomaIcms.RefNf"] = field(
                        default=None,
                        metadata={
                            "name": "refNF",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )
                    ref_cte: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "refCte",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "max_length": 44,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{44}",
                        }
                    )

                    @dataclass
                    class RefNf:
                        """
                        :ivar cnpj: CNPJ do Emitente Informar o CNPJ do
                            emitente do Documento Fiscal
                        :ivar cpf: Número do CPF Informar o CPF do
                            emitente do documento fiscal
                        :ivar mod: Modelo do Documento Fiscal
                        :ivar serie: Serie do documento fiscal
                        :ivar subserie: Subserie do documento fiscal
                        :ivar nro: Número do documento fiscal
                        :ivar valor: Valor do documento fiscal.
                        :ivar d_emi: Data de emissão do documento
                            fiscal.
                        """
                        cnpj: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "CNPJ",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "white_space": "preserve",
                                "pattern": r"[0-9]{14}",
                            }
                        )
                        cpf: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "CPF",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "white_space": "preserve",
                                "pattern": r"[0-9]{11}",
                            }
                        )
                        mod: Optional[TmodDoc] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "required": True,
                            }
                        )
                        serie: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                            }
                        )
                        subserie: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "white_space": "preserve",
                                "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                            }
                        )
                        nro: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{1,6}",
                            }
                        )
                        valor: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        d_emi: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "dEmi",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                            }
                        )

            @dataclass
            class Cobr:
                """
                :ivar fat: Dados da fatura
                :ivar dup: Dados das duplicatas
                """
                fat: Optional["TcteOs.InfCte.InfCteNorm.Cobr.Fat"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                dup: List["TcteOs.InfCte.InfCteNorm.Cobr.Dup"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )

                @dataclass
                class Fat:
                    """
                    :ivar n_fat: Número da fatura
                    :ivar v_orig: Valor original da fatura
                    :ivar v_desc: Valor do desconto da fatura
                    :ivar v_liq: Valor líquido da fatura
                    """
                    n_fat: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nFat",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 60,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    v_orig: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vOrig",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_desc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vDesc",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_liq: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vLiq",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )

                @dataclass
                class Dup:
                    """
                    :ivar n_dup: Número da duplicata
                    :ivar d_venc: Data de vencimento da duplicata (AAAA-
                        MM-DD)
                    :ivar v_dup: Valor da duplicata
                    """
                    n_dup: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nDup",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 60,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    d_venc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "dVenc",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    v_dup: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vDup",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )

            @dataclass
            class InfGtve:
                """
                :ivar ch_cte: Chave de acesso da GTV-e
                :ivar comp: Componentes do Valor da GTVe
                """
                ch_cte: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "chCTe",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "pattern": r"[0-9]{44}",
                    }
                )
                comp: List["TcteOs.InfCte.InfCteNorm.InfGtve.Comp"] = field(
                    default_factory=list,
                    metadata={
                        "name": "Comp",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_occurs": 1,
                    }
                )

                @dataclass
                class Comp:
                    """
                    :ivar tp_comp: Tipo do Componente 1-Custodia
                        2-Embarque 3-Tempo de espera 4-Malote 5-Ad
                        Valorem 6-Outros
                    :ivar v_comp: Valor do componente
                    :ivar x_comp: Nome do componente (informar apenas
                        para outros) Exemplos: FRETE PESO, FRETE VALOR,
                        SEC/CAT, ADEME, AGENDAMENTO, etc
                    """
                    tp_comp: Optional[CompTpComp] = field(
                        default=None,
                        metadata={
                            "name": "tpComp",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    v_comp: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vComp",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    x_comp: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "xComp",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 0,
                            "max_length": 15,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )

        @dataclass
        class InfCteComp:
            """
            :ivar ch_cte: Chave do CT-e complementado
            """
            ch_cte: Optional[str] = field(
                default=None,
                metadata={
                    "name": "chCTe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "max_length": 44,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{44}",
                }
            )

        @dataclass
        class InfCteAnu:
            """
            :ivar ch_cte: Chave de acesso do CT-e original a ser anulado
                e substituído
            :ivar d_emi: Data de emissão da declaração do tomador não
                contribuinte do ICMS
            """
            ch_cte: Optional[str] = field(
                default=None,
                metadata={
                    "name": "chCte",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "pattern": r"[0-9]{44}",
                }
            )
            d_emi: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )

    @dataclass
    class InfCteSupl:
        """
        :ivar qr_cod_cte: Texto com o QR-Code impresso no DACTE
        """
        qr_cod_cte: Optional[str] = field(
            default=None,
            metadata={
                "name": "qrCodCTe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 50,
                "max_length": 1000,
                "white_space": "preserve",
                "pattern": r"((HTTPS?|https?)://.*\?chCTe=[0-9]{44}&tpAmb=[1-2](&sign=[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})?)",
            }
        )


@dataclass
class Tgtve:
    """
    Tipo Guia de Transporte de Valores Eletrônica (Modelo 64)

    :ivar inf_cte: Informações do CT-e do tipo GTV-e
    :ivar inf_cte_supl: Informações suplementares da GTV-e
    :ivar signature:
    :ivar versao: Versão do leiaute
    """
    class Meta:
        name = "TGTVe"

    inf_cte: Optional["Tgtve.InfCte"] = field(
        default=None,
        metadata={
            "name": "infCte",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    inf_cte_supl: Optional["Tgtve.InfCteSupl"] = field(
        default=None,
        metadata={
            "name": "infCTeSupl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "pattern": r"3\.00",
        }
    )

    @dataclass
    class InfCte:
        """
        :ivar ide: Identificação da GTV-e
        :ivar compl: Dados complementares da GTV-e para fins
            operacionais ou comerciais
        :ivar emit: Identificação do Emitente da GTV-e
        :ivar rem: Informações do Remetente Poderá não ser informado
            para os CT-e de redespacho intermediário e serviço vinculado
            a multimodal. Nos demais casos deverá sempre ser informado.
        :ivar dest: Informações do Destinatário Poderá não ser informado
            para os CT-e de redespacho intermediário e serviço vinculado
            a multimodal. Nos demais casos deverá sempre ser informado.
        :ivar origem: Informações do endereço da origem do serviço
        :ivar destino: Informações do endereço do destino do serviço
        :ivar det_gtv: Grupo de informações detalhadas da GTV-e
        :ivar aut_xml: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar inf_resp_tec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar versao: Versão do leiaute Ex: "3.00"
        :ivar id: Identificador da tag a ser assinada Informar a chave
            de acesso do CT-e OS e precedida do literal "CTe"
        """
        ide: Optional["Tgtve.InfCte.Ide"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        compl: Optional["Tgtve.InfCte.Compl"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        emit: Optional["Tgtve.InfCte.Emit"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        rem: Optional["Tgtve.InfCte.Rem"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        dest: Optional["Tgtve.InfCte.Dest"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        origem: Optional[TendeEmi] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        destino: Optional[TendeEmi] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        det_gtv: Optional["Tgtve.InfCte.DetGtv"] = field(
            default=None,
            metadata={
                "name": "detGTV",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        aut_xml: List["Tgtve.InfCte.AutXml"] = field(
            default_factory=list,
            metadata={
                "name": "autXML",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "max_occurs": 10,
            }
        )
        inf_resp_tec: Optional[TrespTec] = field(
            default=None,
            metadata={
                "name": "infRespTec",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "pattern": r"CTe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar c_uf: Código da UF do emitente da GTV-e. Utilizar a
                Tabela do IBGE.
            :ivar c_ct: Código numérico que compõe a Chave de Acesso.
                Número aleatório gerado pelo emitente para cada CT-e,
                com o objetivo de evitar acessos indevidos ao documento.
            :ivar cfop: Código Fiscal de Operações e Prestações
            :ivar nat_op: Natureza da Operação
            :ivar mod: Modelo do documento fiscal Utilizar o código 64
                para identificação do CT-e Guia de Transporte de Valores
            :ivar serie: Série da GTV-e Preencher com "0" no caso de
                série única
            :ivar n_ct: Número da GTV-e
            :ivar dh_emi: Data e hora de emissão da GTV-e Formato AAAA-
                MM-DDTHH:MM:DD TZD
            :ivar tp_imp: Formato de impressão do DACTE Preencher com: 1
                - Retrato; 2 - Paisagem.
            :ivar tp_emis: Forma de emissão da GTV-e Preencher com: 1 -
                Normal; 2- Contingencia offline 7 - Autorização pela
                SVC-RS; 8 - Autorização pela SVC-SP
            :ivar c_dv: Digito Verificador da chave de acesso da GTV-e
                Informar o dígito  de controle da chave de acesso do
                CT-e, que deve ser calculado com a aplicação do
                algoritmo módulo 11 (base 2,9) da chave de acesso.
            :ivar tp_amb: Tipo do Ambiente Preencher com:1 - Produção; 2
                - Homologação
            :ivar tp_cte: Tipo da GTV-e Preencher com: 4 - GTV-e
            :ivar ver_proc: Versão do processo de emissão Iinformar a
                versão do aplicativo emissor de CT-e.
            :ivar c_mun_env: Código do Município de envio da GTV-e (de
                onde o documento foi transmitido) Utilizar a tabela do
                IBGE. Informar 9999999 para as operações com o exterior.
            :ivar x_mun_env: Nome do Município de envio da GTV-e (de
                onde o documento foi transmitido) Informar
                PAIS/Municipio para as operações com o exterior.
            :ivar ufenv: Sigla da UF de envio da GTV-e (de onde o
                documento foi transmitido) Informar 'EX' para operações
                com o exterior.
            :ivar modal: Modal da GTV-e Preencher com: 01-Rodoviário
                06-Multimodal
            :ivar tp_serv: Tipo do Serviço Preencher com: 9 - GTV
            :ivar ind_ietoma: Indicador da IE do tomador: 1 –
                Contribuinte ICMS; 2 – Contribuinte isento de inscrição;
                9 – Não Contribuinte Aplica-se ao tomador que for
                indicado no toma3 ou toma4
            :ivar dh_saida_orig: Data e hora de saida da origem Formato
                AAAA-MM-DDTHH:MM:DD TZD
            :ivar dh_chegada_dest: Data e hora de chegada no destino
                Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar toma: Indicador do "papel" do tomador do serviço no
                GT-e
            :ivar toma_terceiro: Indicador do "papel" do tomador do
                serviço no CTV-e
            :ivar dh_cont: Data e Hora da entrada em contingência
                Informar a data e hora no formato AAAA-MM-DDTHH:MM:SS
            :ivar x_just: Justificativa da entrada em contingência
            """
            c_uf: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "name": "cUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            c_ct: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cCT",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            cfop: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CFOP",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[123567][0-9]([0-9][1-9]|[1-9][0-9])",
                }
            )
            nat_op: Optional[str] = field(
                default=None,
                metadata={
                    "name": "natOp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            mod: Optional[TmodGtve] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            serie: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                }
            )
            n_ct: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nCT",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            dh_emi: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tp_imp: Optional[IdeTpImp] = field(
                default=None,
                metadata={
                    "name": "tpImp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tp_emis: Optional[IdeTpEmis] = field(
                default=None,
                metadata={
                    "name": "tpEmis",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            c_dv: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cDV",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
                }
            )
            tp_amb: Optional[Tamb] = field(
                default=None,
                metadata={
                    "name": "tpAmb",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            tp_cte: Optional[TfinGtve] = field(
                default=None,
                metadata={
                    "name": "tpCTe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            ver_proc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "verProc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            c_mun_env: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cMunEnv",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            x_mun_env: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xMunEnv",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ufenv: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UFEnv",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            modal: Optional[IdeModal] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            tp_serv: Optional[IdeTpServ] = field(
                default=None,
                metadata={
                    "name": "tpServ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            ind_ietoma: Optional[IdeIndIetoma] = field(
                default=None,
                metadata={
                    "name": "indIEToma",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            dh_saida_orig: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhSaidaOrig",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            dh_chegada_dest: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhChegadaDest",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            toma: Optional["Tgtve.InfCte.Ide.Toma"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            toma_terceiro: Optional["Tgtve.InfCte.Ide.TomaTerceiro"] = field(
                default=None,
                metadata={
                    "name": "tomaTerceiro",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            dh_cont: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            x_just: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xJust",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 15,
                    "max_length": 256,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )

            @dataclass
            class Toma:
                """
                :ivar toma: Tomador do Serviço Preencher com:
                    0-Remetente; 1-Destinatário
                """
                toma: Optional[TomaToma] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                    }
                )

            @dataclass
            class TomaTerceiro:
                """
                :ivar toma: Tomador do Serviço Preencher com: 4 - Outros
                    Obs: Informar os dados cadastrais do tomador do
                    serviço
                :ivar cnpj: Número do CNPJ Em caso de empresa não
                    estabelecida no Brasil, será informado o CNPJ com
                    zeros. Informar os zeros não significativos.
                :ivar cpf: Número do CPF Informar os zeros não
                    significativos.
                :ivar ie: Inscrição Estadual Informar a IE do tomador ou
                    ISENTO se tomador é contribuinte do ICMS isento de
                    inscrição no cadastro de contribuintes do ICMS. Caso
                    o tomador não seja contribuinte do ICMS não informar
                    o conteúdo.
                :ivar x_nome: Razão Social ou Nome
                :ivar x_fant: Nome Fantasia
                :ivar fone: Telefone
                :ivar ender_toma: Dados do endereço
                :ivar email: Endereço de email
                """
                toma: Optional[TomaTerceiroToma] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                cnpj: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CNPJ",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{0}|[0-9]{14}",
                    }
                )
                cpf: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CPF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{11}",
                    }
                )
                ie: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "IE",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "max_length": 14,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{0,14}|ISENTO",
                    }
                )
                x_nome: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xNome",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
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
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                fone: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{6,14}",
                    }
                )
                ender_toma: Optional[Tendereco] = field(
                    default=None,
                    metadata={
                        "name": "enderToma",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                    }
                )
                email: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[^@]+@[^\.]+\..+",
                    }
                )

        @dataclass
        class Compl:
            """
            :ivar x_carac_ad: Característica adicional do transporte
                Texto livre: REENTREGA; DEVOLUÇÃO; REFATURAMENTO; etc
            :ivar x_carac_ser: Característica adicional do serviço Texto
                livre: ENTREGA EXPRESSA; LOGÍSTICA REVERSA;
                CONVENCIONAL; EMERGENCIAL; etc
            :ivar x_emi: Funcionário emissor da GTV-e
            :ivar x_obs: Observações Gerais
            :ivar obs_cont: Campo de uso livre do contribuinte Informar
                o nome do campo no atributo xCampo e o conteúdo do campo
                no XTexto
            :ivar obs_fisco: Campo de uso livre do contribuinte Informar
                o nome do campo no atributo xCampo e o conteúdo do campo
                no XTexto
            """
            x_carac_ad: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xCaracAd",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_carac_ser: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xCaracSer",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 30,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_emi: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_obs: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xObs",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            obs_cont: List["Tgtve.InfCte.Compl.ObsCont"] = field(
                default_factory=list,
                metadata={
                    "name": "ObsCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_occurs": 10,
                }
            )
            obs_fisco: List["Tgtve.InfCte.Compl.ObsFisco"] = field(
                default_factory=list,
                metadata={
                    "name": "ObsFisco",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_occurs": 10,
                }
            )

            @dataclass
            class ObsCont:
                """
                :ivar x_texto: Conteúdo do campo
                :ivar x_campo: Identificação do campo
                """
                x_texto: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xTexto",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 160,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                x_campo: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xCampo",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )

            @dataclass
            class ObsFisco:
                """
                :ivar x_texto: Conteúdo do campo
                :ivar x_campo: Identificação do campo
                """
                x_texto: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xTexto",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                x_campo: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xCampo",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )

        @dataclass
        class Emit:
            """
            :ivar cnpj: CNPJ do emitente Informar zeros não
                significativos
            :ivar ie: Inscrição Estadual do Emitente
            :ivar iest: Inscrição Estadual do Substituto Tributário
            :ivar x_nome: Razão social ou Nome do emitente
            :ivar x_fant: Nome fantasia
            :ivar ender_emit: Endereço do emitente
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            iest: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IEST",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )

        @dataclass
        class Rem:
            """
            :ivar cnpj: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar cpf: Número do CPF Informar os zeros não
                significativos.
            :ivar ie: Inscrição Estadual Informar a IE do remetente ou
                ISENTO se remetente é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                remetente não seja contribuinte do ICMS não informar a
                tag.
            :ivar x_nome: Razão social ou nome do remetente
            :ivar x_fant: Nome fantasia
            :ivar fone: Telefone
            :ivar ender_reme: Dados do endereço
            :ivar email: Endereço de email
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            fone: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6,14}",
                }
            )
            ender_reme: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "name": "enderReme",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            email: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[^@]+@[^\.]+\..+",
                }
            )

        @dataclass
        class Dest:
            """
            :ivar cnpj: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar cpf: Número do CPF Informar os zeros não
                significativos.
            :ivar ie: Inscrição Estadual Informar a IE do destinatário
                ou ISENTO se destinatário é contribuinte do ICMS isento
                de inscrição no cadastro de contribuintes do ICMS. Caso
                o destinatário não seja contribuinte do ICMS não
                informar o conteúdo.
            :ivar x_nome: Razão Social ou Nome do destinatário
            :ivar fone: Telefone
            :ivar isuf: Inscrição na SUFRAMA (Obrigatório nas operações
                com as áreas com benefícios de incentivos fiscais sob
                controle da SUFRAMA)
            :ivar ender_dest: Dados do endereço
            :ivar email: Endereço de email
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            fone: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6,14}",
                }
            )
            isuf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ISUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8,9}",
                }
            )
            ender_dest: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "name": "enderDest",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            email: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[^@]+@[^\.]+\..+",
                }
            )

        @dataclass
        class DetGtv:
            """
            :ivar inf_especie: Informações das Espécies transportadas
            :ivar q_carga: Quantidade de volumes/malotes
            :ivar inf_veiculo: Grupo de informações dos veículos
                utilizados no transporte de valores
            """
            inf_especie: List["Tgtve.InfCte.DetGtv.InfEspecie"] = field(
                default_factory=list,
                metadata={
                    "name": "infEspecie",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_occurs": 1,
                }
            )
            q_carga: Optional[str] = field(
                default=None,
                metadata={
                    "name": "qCarga",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                }
            )
            inf_veiculo: List["Tgtve.InfCte.DetGtv.InfVeiculo"] = field(
                default_factory=list,
                metadata={
                    "name": "infVeiculo",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class InfEspecie:
                """
                :ivar tp_especie: Tipo da Espécie 1 - Cédula 2 - Cheque
                    3 - Moeda 4 - Outros
                :ivar v_especie: Valor Transportada em Espécie indicada
                :ivar tp_numerario: Nacionalidade do Numerário 1 -
                    Nacional 2 - Estrangeiro
                :ivar x_moeda_estr: Nome da Moeda Informar somente se
                    tipo de numerário for 2 - Estrangeiro
                """
                tp_especie: Optional[InfEspecieTpEspecie] = field(
                    default=None,
                    metadata={
                        "name": "tpEspecie",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                v_especie: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vEspecie",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                tp_numerario: Optional[InfEspecieTpNumerario] = field(
                    default=None,
                    metadata={
                        "name": "tpNumerario",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                x_moeda_estr: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xMoedaEstr",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )

            @dataclass
            class InfVeiculo:
                """
                :ivar placa: Placa do veículo
                :ivar uf: UF em que veículo está licenciado Sigla da UF
                    de licenciamento do veículo.
                :ivar rntrc: RNTRC do transportador
                """
                placa: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[A-Z]{2,3}[0-9]{4}|[A-Z]{3,4}[0-9]{3}|[A-Z0-9]{7}",
                    }
                )
                uf: Optional[Tuf] = field(
                    default=None,
                    metadata={
                        "name": "UF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                rntrc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "RNTRC",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{8}|ISENTO",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )

    @dataclass
    class InfCteSupl:
        """
        :ivar qr_cod_cte: Texto com o QR-Code impresso no DACTE
        """
        qr_cod_cte: Optional[str] = field(
            default=None,
            metadata={
                "name": "qrCodCTe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 50,
                "max_length": 1000,
                "white_space": "preserve",
                "pattern": r"((HTTPS?|https?)://.*\?chCTe=[0-9]{44}&tpAmb=[1-2](&sign=[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})?)",
            }
        )


@dataclass
class TretCte:
    """
    Tipo Retorno do Pedido de Autorização de CT-e (Modelo 57)

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar c_uf: Identificação da UF
    :ivar ver_aplic: Versão do Aplicativo que processou a CT-e
    :ivar c_stat: código do status do retorno da consulta.
    :ivar x_motivo: Descrição literal do status do do retorno da
        consulta.
    :ivar prot_cte: Reposta ao processamento do CT-e
    :ivar versao:
    """
    class Meta:
        name = "TRetCTe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    c_uf: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    prot_cte: Optional[TprotCte] = field(
        default=None,
        metadata={
            "name": "protCTe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
class TretCteOs:
    """
    Tipo Retorno do Pedido de Autorização de CT-e OS (Modelo 67)

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar c_uf: Identificação da UF
    :ivar ver_aplic: Versão do Aplicativo que processou a CT-e
    :ivar c_stat: código do status do retorno da consulta.
    :ivar x_motivo: Descrição literal do status do do retorno da
        consulta.
    :ivar prot_cte: Reposta ao processamento do CT-e
    :ivar versao:
    """
    class Meta:
        name = "TRetCTeOS"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    c_uf: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    prot_cte: Optional[TprotCteOs] = field(
        default=None,
        metadata={
            "name": "protCTe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
class TretGtve:
    """
    Tipo Retorno do Pedido de Autorização de GTV-e (Modelo 64)

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar c_uf: Identificação da UF
    :ivar ver_aplic: Versão do Aplicativo que processou a GTV-e
    :ivar c_stat: código do status do retorno da consulta.
    :ivar x_motivo: Descrição literal do status do do retorno da
        consulta.
    :ivar prot_cte: Reposta ao processamento do CT-e
    :ivar versao:
    """
    class Meta:
        name = "TRetGTVe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    c_uf: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    prot_cte: Optional[TprotGtve] = field(
        default=None,
        metadata={
            "name": "protCTe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
        Tração 2 - Rodoviário Reboque 3 - Navio 4 - Balsa 5 - Aeronave 6
        - Vagão 7 - Outros
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    id_unid_transp: Optional[str] = field(
        default=None,
        metadata={
            "name": "idUnidTransp",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    inf_unid_carga: List[TunidCarga] = field(
        default_factory=list,
        metadata={
            "name": "infUnidCarga",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    qtd_rat: Optional[str] = field(
        default=None,
        metadata={
            "name": "qtdRat",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )


@dataclass
class Tcte:
    """
    Tipo Conhecimento de Transporte Eletrônico (Modelo 57)

    :ivar inf_cte: Informações do CT-e
    :ivar inf_cte_supl: Informações suplementares do CT-e
    :ivar signature:
    """
    class Meta:
        name = "TCTe"

    inf_cte: Optional["Tcte.InfCte"] = field(
        default=None,
        metadata={
            "name": "infCte",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    inf_cte_supl: Optional["Tcte.InfCteSupl"] = field(
        default=None,
        metadata={
            "name": "infCTeSupl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
    class InfCte:
        """
        :ivar ide: Identificação do CT-e
        :ivar compl: Dados complementares do CT-e para fins operacionais
            ou comerciais
        :ivar emit: Identificação do Emitente do CT-e
        :ivar rem: Informações do Remetente das mercadorias
            transportadas pelo CT-e Poderá não ser informado para os
            CT-e de redespacho intermediário e serviço vinculado a
            multimodal. Nos demais casos deverá sempre ser informado.
        :ivar exped: Informações do Expedidor da Carga
        :ivar receb: Informações do Recebedor da Carga
        :ivar dest: Informações do Destinatário do CT-e Poderá não ser
            informado para os CT-e de redespacho intermediário e serviço
            vinculado a multimodal. Nos demais casos deverá sempre ser
            informado.
        :ivar v_prest: Valores da Prestação de Serviço
        :ivar imp: Informações relativas aos Impostos
        :ivar inf_cte_norm: Grupo de informações do CT-e Normal e
            Substituto
        :ivar inf_cte_comp: Detalhamento do CT-e complementado
        :ivar inf_cte_anu: Detalhamento do CT-e do tipo Anulação
        :ivar aut_xml: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar inf_resp_tec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar inf_solic_nff: Grupo de informações do pedido de emissão
            da Nota Fiscal Fácil
        :ivar versao: Versão do leiaute Ex: "3.00"
        :ivar id: Identificador da tag a ser assinada Informar a chave
            de acesso do CT-e e precedida do literal "CTe"
        """
        ide: Optional["Tcte.InfCte.Ide"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        compl: Optional["Tcte.InfCte.Compl"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        emit: Optional["Tcte.InfCte.Emit"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        rem: Optional["Tcte.InfCte.Rem"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        exped: Optional["Tcte.InfCte.Exped"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        receb: Optional["Tcte.InfCte.Receb"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        dest: Optional["Tcte.InfCte.Dest"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        v_prest: Optional["Tcte.InfCte.VPrest"] = field(
            default=None,
            metadata={
                "name": "vPrest",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        imp: Optional["Tcte.InfCte.Imp"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        inf_cte_norm: Optional["Tcte.InfCte.InfCteNorm"] = field(
            default=None,
            metadata={
                "name": "infCTeNorm",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        inf_cte_comp: Optional["Tcte.InfCte.InfCteComp"] = field(
            default=None,
            metadata={
                "name": "infCteComp",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        inf_cte_anu: Optional["Tcte.InfCte.InfCteAnu"] = field(
            default=None,
            metadata={
                "name": "infCteAnu",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        aut_xml: List["Tcte.InfCte.AutXml"] = field(
            default_factory=list,
            metadata={
                "name": "autXML",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "max_occurs": 10,
            }
        )
        inf_resp_tec: Optional[TrespTec] = field(
            default=None,
            metadata={
                "name": "infRespTec",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        inf_solic_nff: Optional["Tcte.InfCte.InfSolicNff"] = field(
            default=None,
            metadata={
                "name": "infSolicNFF",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "pattern": r"CTe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar c_uf: Código da UF do emitente do CT-e. Utilizar a
                Tabela do IBGE.
            :ivar c_ct: Código numérico que compõe a Chave de Acesso.
                Número aleatório gerado pelo emitente para cada CT-e,
                com o objetivo de evitar acessos indevidos ao documento.
            :ivar cfop: Código Fiscal de Operações e Prestações
            :ivar nat_op: Natureza da Operação
            :ivar mod: Modelo do documento fiscal Utilizar o código 57
                para identificação do CT-e, emitido em substituição aos
                modelos de conhecimentos em papel.
            :ivar serie: Série do CT-e Preencher com "0" no caso de
                série única
            :ivar n_ct: Número do CT-e
            :ivar dh_emi: Data e hora de emissão do CT-e Formato AAAA-
                MM-DDTHH:MM:DD TZD
            :ivar tp_imp: Formato de impressão do DACTE Preencher com: 1
                - Retrato; 2 - Paisagem.
            :ivar tp_emis: Forma de emissão do CT-e Preencher com: 1 -
                Normal; 3-Regime Especial NFF;  4-EPEC pela SVC; 5 -
                Contingência FSDA; 7 - Autorização pela SVC-RS; 8 -
                Autorização pela SVC-SP
            :ivar c_dv: Digito Verificador da chave de acesso do CT-e
                Informar o dígito  de controle da chave de acesso do
                CT-e, que deve ser calculado com a aplicação do
                algoritmo módulo 11 (base 2,9) da chave de acesso.
            :ivar tp_amb: Tipo do Ambiente Preencher com:1 - Produção; 2
                - Homologação.
            :ivar tp_cte: Tipo do CT-e Preencher com: 0 - CT-e Normal; 1
                - CT-e de Complemento de Valores;     2 - CT-e de
                Anulação; 3 - CT-e de Substituição
            :ivar proc_emi: Identificador do processo de emissão do CT-e
                Preencher com: 0 - emissão de CT-e com aplicativo do
                contribuinte; 3- emissão CT-e pelo contribuinte com
                aplicativo fornecido pelo SEBRAE.
            :ivar ver_proc: Versão do processo de emissão Iinformar a
                versão do aplicativo emissor de CT-e.
            :ivar ind_globalizado: Indicador de CT-e Globalizado
                Informar valor 1 quando for Globalizado e não informar a
                tag quando não tratar de CT-e Globalizado
            :ivar c_mun_env: Código do Município de envio do CT-e (de
                onde o documento foi transmitido) Utilizar a tabela do
                IBGE. Informar 9999999 para as operações com o exterior.
            :ivar x_mun_env: Nome do Município de envio do CT-e (de onde
                o documento foi transmitido) Informar PAIS/Municipio
                para as operações com o exterior.
            :ivar ufenv: Sigla da UF de envio do CT-e (de onde o
                documento foi transmitido) Informar 'EX' para operações
                com o exterior.
            :ivar modal: Modal Preencher com:01-Rodoviário;
                02-Aéreo;03-Aquaviário;04-Ferroviário;05-Dutoviário;06-Multimodal;
            :ivar tp_serv: Tipo do Serviço Preencher com: 0 - Normal;1 -
                Subcontratação; 2 - Redespacho;3 - Redespacho
                Intermediário; 4 - Serviço Vinculado a Multimodal
            :ivar c_mun_ini: Código do Município de início da prestação
                Utilizar a tabela do IBGE. Informar 9999999 para
                operações com o exterior.
            :ivar x_mun_ini: Nome do Município do início da prestação
                Informar 'EXTERIOR' para operações com o exterior.
            :ivar ufini: UF do início da prestação Informar 'EX' para
                operações com o exterior.
            :ivar c_mun_fim: Código do Município de término da prestação
                Utilizar a tabela do IBGE. Informar 9999999 para
                operações com o exterior.
            :ivar x_mun_fim: Nome do Município do término da prestação
                Informar 'EXTERIOR' para operações com o exterior.
            :ivar uffim: UF do término da prestação Informar 'EX' para
                operações com o exterior.
            :ivar retira: Indicador se o Recebedor retira no Aeroporto,
                Filial, Porto ou Estação de Destino? Preencher com: 0 -
                sim; 1 - não
            :ivar x_det_retira: Detalhes do retira
            :ivar ind_ietoma: Indicador do papel do tomador na prestação
                do serviço: 1 – Contribuinte ICMS; 2 – Contribuinte
                isento de inscrição; 9 – Não Contribuinte Aplica-se ao
                tomador que for indicado no toma3 ou toma4
            :ivar toma3: Indicador do "papel" do tomador do serviço no
                CT-e
            :ivar toma4: Indicador do "papel" do tomador do serviço no
                CT-e
            :ivar dh_cont: Data e Hora da entrada em contingência
                Informar a data e hora no formato AAAA-MM-DDTHH:MM:SS
            :ivar x_just: Justificativa da entrada em contingência
            """
            c_uf: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "name": "cUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            c_ct: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cCT",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            cfop: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CFOP",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[123567][0-9]([0-9][1-9]|[1-9][0-9])",
                }
            )
            nat_op: Optional[str] = field(
                default=None,
                metadata={
                    "name": "natOp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            mod: Optional[TmodCt] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            serie: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                }
            )
            n_ct: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nCT",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            dh_emi: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tp_imp: Optional[IdeTpImp] = field(
                default=None,
                metadata={
                    "name": "tpImp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tp_emis: Optional[IdeTpEmis] = field(
                default=None,
                metadata={
                    "name": "tpEmis",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            c_dv: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cDV",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
                }
            )
            tp_amb: Optional[Tamb] = field(
                default=None,
                metadata={
                    "name": "tpAmb",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            tp_cte: Optional[TfinCte] = field(
                default=None,
                metadata={
                    "name": "tpCTe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            proc_emi: Optional[TprocEmi] = field(
                default=None,
                metadata={
                    "name": "procEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            ver_proc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "verProc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ind_globalizado: Optional[IdeIndGlobalizado] = field(
                default=None,
                metadata={
                    "name": "indGlobalizado",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            c_mun_env: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cMunEnv",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            x_mun_env: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xMunEnv",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ufenv: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UFEnv",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            modal: Optional[TmodTransp] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            tp_serv: Optional[IdeTpServ] = field(
                default=None,
                metadata={
                    "name": "tpServ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            c_mun_ini: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cMunIni",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            x_mun_ini: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xMunIni",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ufini: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UFIni",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            c_mun_fim: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cMunFim",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            x_mun_fim: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xMunFim",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            uffim: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UFFim",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            retira: Optional[IdeRetira] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            x_det_retira: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xDetRetira",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 160,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ind_ietoma: Optional[IdeIndIetoma] = field(
                default=None,
                metadata={
                    "name": "indIEToma",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            toma3: Optional["Tcte.InfCte.Ide.Toma3"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            toma4: Optional["Tcte.InfCte.Ide.Toma4"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            dh_cont: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            x_just: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xJust",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 15,
                    "max_length": 256,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )

            @dataclass
            class Toma3:
                """
                :ivar toma: Tomador do Serviço Preencher com:
                    0-Remetente; 1-Expedidor; 2-Recebedor;
                    3-Destinatário Serão utilizadas as informações
                    contidas no respectivo grupo, conforme indicado pelo
                    conteúdo deste campo
                """
                toma: Optional[Toma3Toma] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                    }
                )

            @dataclass
            class Toma4:
                """
                :ivar toma: Tomador do Serviço Preencher com: 4 - Outros
                    Obs: Informar os dados cadastrais do tomador do
                    serviço
                :ivar cnpj: Número do CNPJ Em caso de empresa não
                    estabelecida no Brasil, será informado o CNPJ com
                    zeros. Informar os zeros não significativos.
                :ivar cpf: Número do CPF Informar os zeros não
                    significativos.
                :ivar ie: Inscrição Estadual Informar a IE do tomador ou
                    ISENTO se tomador é contribuinte do ICMS isento de
                    inscrição no cadastro de contribuintes do ICMS. Caso
                    o tomador não seja contribuinte do ICMS não informar
                    o conteúdo.
                :ivar x_nome: Razão Social ou Nome
                :ivar x_fant: Nome Fantasia
                :ivar fone: Telefone
                :ivar ender_toma: Dados do endereço
                :ivar email: Endereço de email
                """
                toma: Optional[Toma4Toma] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                cnpj: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CNPJ",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{0}|[0-9]{14}",
                    }
                )
                cpf: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CPF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{11}",
                    }
                )
                ie: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "IE",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "max_length": 14,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{0,14}|ISENTO",
                    }
                )
                x_nome: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xNome",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
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
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                fone: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{6,14}",
                    }
                )
                ender_toma: Optional[Tendereco] = field(
                    default=None,
                    metadata={
                        "name": "enderToma",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                    }
                )
                email: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[^@]+@[^\.]+\..+",
                    }
                )

        @dataclass
        class Compl:
            """
            :ivar x_carac_ad: Característica adicional do transporte
                Texto livre: REENTREGA; DEVOLUÇÃO; REFATURAMENTO; etc
            :ivar x_carac_ser: Característica adicional do serviço Texto
                livre: ENTREGA EXPRESSA; LOGÍSTICA REVERSA;
                CONVENCIONAL; EMERGENCIAL; etc
            :ivar x_emi: Funcionário emissor do CTe
            :ivar fluxo: Previsão do fluxo da carga Preenchimento
                obrigatório para o modal aéreo.
            :ivar entrega: Informações ref. a previsão de entrega
            :ivar orig_calc: Município de origem para efeito de cálculo
                do frete
            :ivar dest_calc: Município de destino para efeito de cálculo
                do frete
            :ivar x_obs: Observações Gerais
            :ivar obs_cont: Campo de uso livre do contribuinte Informar
                o nome do campo no atributo xCampo e o conteúdo do campo
                no XTexto
            :ivar obs_fisco: Campo de uso livre do contribuinte Informar
                o nome do campo no atributo xCampo e o conteúdo do campo
                no XTexto
            """
            x_carac_ad: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xCaracAd",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_carac_ser: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xCaracSer",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 30,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_emi: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            fluxo: Optional["Tcte.InfCte.Compl.Fluxo"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            entrega: Optional["Tcte.InfCte.Compl.Entrega"] = field(
                default=None,
                metadata={
                    "name": "Entrega",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            orig_calc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "origCalc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 40,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            dest_calc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "destCalc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 40,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_obs: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xObs",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            obs_cont: List["Tcte.InfCte.Compl.ObsCont"] = field(
                default_factory=list,
                metadata={
                    "name": "ObsCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_occurs": 10,
                }
            )
            obs_fisco: List["Tcte.InfCte.Compl.ObsFisco"] = field(
                default_factory=list,
                metadata={
                    "name": "ObsFisco",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_occurs": 10,
                }
            )

            @dataclass
            class Fluxo:
                """
                :ivar x_orig: Sigla ou código interno da
                    Filial/Porto/Estação/ Aeroporto de Origem
                    Observações para o modal aéreo: - Preenchimento
                    obrigatório para o modal aéreo. - O código de três
                    letras IATA do aeroporto de partida deverá ser
                    incluído como primeira anotação. Quando não for
                    possível, utilizar a sigla OACI.
                :ivar pass_value:
                :ivar x_dest: Sigla ou código interno da
                    Filial/Porto/Estação/Aeroporto de Destino
                    Observações para o modal aéreo: - Preenchimento
                    obrigatório para o modal aéreo. - Deverá ser
                    incluído o código de três letras IATA do aeroporto
                    de destino. Quando não for possível, utilizar a
                    sigla OACI.
                :ivar x_rota: Código da Rota de Entrega
                """
                x_orig: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xOrig",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                pass_value: List["Tcte.InfCte.Compl.Fluxo.Pass"] = field(
                    default_factory=list,
                    metadata={
                        "name": "pass",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                x_dest: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xDest",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                x_rota: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xRota",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 10,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )

                @dataclass
                class Pass:
                    """
                    :ivar x_pass: Sigla ou código interno da
                        Filial/Porto/Estação/Aeroporto de Passagem
                        Observação para o modal aéreo: - O código de
                        três letras IATA, referente ao aeroporto de
                        transferência, deverá ser incluído, quando for o
                        caso. Quando não for possível,  utilizar a sigla
                        OACI. Qualquer solicitação de itinerário deverá
                        ser incluída.
                    """
                    x_pass: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "xPass",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 15,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )

            @dataclass
            class Entrega:
                """
                :ivar sem_data: Entrega sem data definida Esta opção é
                    proibida para o modal aéreo.
                :ivar com_data: Entrega com data definida
                :ivar no_periodo: Entrega no período definido
                :ivar sem_hora: Entrega sem hora definida
                :ivar com_hora: Entrega com hora definida
                :ivar no_inter: Entrega no intervalo de horário definido
                """
                sem_data: Optional["Tcte.InfCte.Compl.Entrega.SemData"] = field(
                    default=None,
                    metadata={
                        "name": "semData",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                com_data: Optional["Tcte.InfCte.Compl.Entrega.ComData"] = field(
                    default=None,
                    metadata={
                        "name": "comData",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                no_periodo: Optional["Tcte.InfCte.Compl.Entrega.NoPeriodo"] = field(
                    default=None,
                    metadata={
                        "name": "noPeriodo",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                sem_hora: Optional["Tcte.InfCte.Compl.Entrega.SemHora"] = field(
                    default=None,
                    metadata={
                        "name": "semHora",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                com_hora: Optional["Tcte.InfCte.Compl.Entrega.ComHora"] = field(
                    default=None,
                    metadata={
                        "name": "comHora",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                no_inter: Optional["Tcte.InfCte.Compl.Entrega.NoInter"] = field(
                    default=None,
                    metadata={
                        "name": "noInter",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )

                @dataclass
                class SemData:
                    """
                    :ivar tp_per: Tipo de data/período programado para
                        entrega 0- Sem data definida
                    """
                    tp_per: Optional[SemDataTpPer] = field(
                        default=None,
                        metadata={
                            "name": "tpPer",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )

                @dataclass
                class ComData:
                    """
                    :ivar tp_per: Tipo de data/período programado para
                        entrega Preencher com: 1-Na data; 2-Até a data;
                        3-A partir da data
                    :ivar d_prog: Data programada Formato AAAA-MM-DD
                    """
                    tp_per: Optional[ComDataTpPer] = field(
                        default=None,
                        metadata={
                            "name": "tpPer",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    d_prog: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "dProg",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )

                @dataclass
                class NoPeriodo:
                    """
                    :ivar tp_per: Tipo período 4-no período
                    :ivar d_ini: Data inicial Formato AAAA-MM-DD
                    :ivar d_fim: Data final Formato AAAA-MM-DD
                    """
                    tp_per: Optional[NoPeriodoTpPer] = field(
                        default=None,
                        metadata={
                            "name": "tpPer",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    d_ini: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "dIni",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    d_fim: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "dFim",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )

                @dataclass
                class SemHora:
                    """
                    :ivar tp_hor: Tipo de hora 0- Sem hora definida
                    """
                    tp_hor: Optional[SemHoraTpHor] = field(
                        default=None,
                        metadata={
                            "name": "tpHor",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )

                @dataclass
                class ComHora:
                    """
                    :ivar tp_hor: Tipo de hora Preencher com: 1 - No
                        horário; 2 - Até o horário; 3 - A partir do
                        horário.
                    :ivar h_prog: Hora programada Formato HH:MM:SS
                    """
                    tp_hor: Optional[ComHoraTpHor] = field(
                        default=None,
                        metadata={
                            "name": "tpHor",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    h_prog: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "hProg",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",
                        }
                    )

                @dataclass
                class NoInter:
                    """
                    :ivar tp_hor: Tipo de hora 4 - No intervalo de tempo
                    :ivar h_ini: Hora inicial Formato HH:MM:SS
                    :ivar h_fim: Hora final Formato HH:MM:SS
                    """
                    tp_hor: Optional[NoInterTpHor] = field(
                        default=None,
                        metadata={
                            "name": "tpHor",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    h_ini: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "hIni",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",
                        }
                    )
                    h_fim: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "hFim",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",
                        }
                    )

            @dataclass
            class ObsCont:
                """
                :ivar x_texto: Conteúdo do campo
                :ivar x_campo: Identificação do campo
                """
                x_texto: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xTexto",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 160,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                x_campo: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xCampo",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )

            @dataclass
            class ObsFisco:
                """
                :ivar x_texto: Conteúdo do campo
                :ivar x_campo: Identificação do campo
                """
                x_texto: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xTexto",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                x_campo: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xCampo",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )

        @dataclass
        class Emit:
            """
            :ivar cnpj: CNPJ do emitente Informar zeros não
                significativos
            :ivar cpf: CPF do emitente Informar zeros não
                significativos. Usar com série específica 920-969 para
                emitente pessoa física com inscrição estadual
            :ivar ie: Inscrição Estadual do Emitente A IE do emitente
                somente ficará sem informação para o caso do Regime
                Especial da NFF (tpEmis=3)
            :ivar iest: Inscrição Estadual do Substituto Tributário
            :ivar x_nome: Razão social ou Nome do emitente
            :ivar x_fant: Nome fantasia
            :ivar ender_emit: Endereço do emitente
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            iest: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IEST",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )

        @dataclass
        class Rem:
            """
            :ivar cnpj: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar cpf: Número do CPF Informar os zeros não
                significativos.
            :ivar ie: Inscrição Estadual Informar a IE do remetente ou
                ISENTO se remetente é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                remetente não seja contribuinte do ICMS não informar a
                tag.
            :ivar x_nome: Razão social ou nome do remetente
            :ivar x_fant: Nome fantasia
            :ivar fone: Telefone
            :ivar ender_reme: Dados do endereço
            :ivar email: Endereço de email
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            fone: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6,14}",
                }
            )
            ender_reme: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "name": "enderReme",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            email: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[^@]+@[^\.]+\..+",
                }
            )

        @dataclass
        class Exped:
            """
            :ivar cnpj: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar cpf: Número do CPF Informar os zeros não
                significativos.
            :ivar ie: Inscrição Estadual Informar a IE do expedidor ou
                ISENTO se expedidor é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                expedidor não seja contribuinte do ICMS não informar a
                tag.
            :ivar x_nome: Razão Social ou Nome
            :ivar fone: Telefone
            :ivar ender_exped: Dados do endereço
            :ivar email: Endereço de email
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            fone: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6,14}",
                }
            )
            ender_exped: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "name": "enderExped",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            email: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[^@]+@[^\.]+\..+",
                }
            )

        @dataclass
        class Receb:
            """
            :ivar cnpj: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar cpf: Número do CPF Informar os zeros não
                significativos.
            :ivar ie: Inscrição Estadual Informar a IE do recebedor ou
                ISENTO se recebedor é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                recebedor não seja contribuinte do ICMS não informar o
                conteúdo.
            :ivar x_nome: Razão Social ou Nome
            :ivar fone: Telefone
            :ivar ender_receb: Dados do endereço
            :ivar email: Endereço de email
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            fone: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6,14}",
                }
            )
            ender_receb: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "name": "enderReceb",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            email: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[^@]+@[^\.]+\..+",
                }
            )

        @dataclass
        class Dest:
            """
            :ivar cnpj: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar cpf: Número do CPF Informar os zeros não
                significativos.
            :ivar ie: Inscrição Estadual Informar a IE do destinatário
                ou ISENTO se destinatário é contribuinte do ICMS isento
                de inscrição no cadastro de contribuintes do ICMS. Caso
                o destinatário não seja contribuinte do ICMS não
                informar o conteúdo.
            :ivar x_nome: Razão Social ou Nome do destinatário
            :ivar fone: Telefone
            :ivar isuf: Inscrição na SUFRAMA (Obrigatório nas operações
                com as áreas com benefícios de incentivos fiscais sob
                controle da SUFRAMA)
            :ivar ender_dest: Dados do endereço
            :ivar email: Endereço de email
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            fone: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6,14}",
                }
            )
            isuf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ISUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8,9}",
                }
            )
            ender_dest: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "name": "enderDest",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            email: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[^@]+@[^\.]+\..+",
                }
            )

        @dataclass
        class VPrest:
            """
            :ivar v_tprest: Valor Total da Prestação do Serviço Pode
                conter zeros quando o CT-e for de complemento de ICMS
            :ivar v_rec: Valor a Receber
            :ivar comp: Componentes do Valor da Prestação
            """
            v_tprest: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vTPrest",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_rec: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vRec",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            comp: List["Tcte.InfCte.VPrest.Comp"] = field(
                default_factory=list,
                metadata={
                    "name": "Comp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )

            @dataclass
            class Comp:
                """
                :ivar x_nome: Nome do componente Exxemplos: FRETE PESO,
                    FRETE VALOR, SEC/CAT, ADEME, AGENDAMENTO, etc
                :ivar v_comp: Valor do componente
                """
                x_nome: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xNome",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 15,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                v_comp: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vComp",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

        @dataclass
        class Imp:
            """
            :ivar icms: Informações relativas ao ICMS
            :ivar v_tot_trib: Valor Total dos Tributos
            :ivar inf_ad_fisco: Informações adicionais de interesse do
                Fisco Norma referenciada, informações complementares,
                etc
            :ivar icmsuffim: Informações do ICMS de partilha com a UF de
                término do serviço de transporte na operação
                interestadual Grupo a ser informado nas prestações
                interestaduais para consumidor final, não contribuinte
                do ICMS
            """
            icms: Optional[Timp] = field(
                default=None,
                metadata={
                    "name": "ICMS",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            v_tot_trib: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vTotTrib",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            inf_ad_fisco: Optional[str] = field(
                default=None,
                metadata={
                    "name": "infAdFisco",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            icmsuffim: Optional["Tcte.InfCte.Imp.Icmsuffim"] = field(
                default=None,
                metadata={
                    "name": "ICMSUFFim",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )

            @dataclass
            class Icmsuffim:
                """
                :ivar v_bcuffim: Valor da BC do ICMS na UF de término da
                    prestação do serviço de transporte
                :ivar p_fcpuffim: Percentual do ICMS relativo ao Fundo
                    de Combate à pobreza (FCP) na UF de término da
                    prestação do serviço de transporte Alíquota adotada
                    nas operações internas na UF do destinatário
                :ivar p_icmsuffim: Alíquota interna da UF de término da
                    prestação do serviço de transporte Alíquota adotada
                    nas operações internas na UF do destinatário
                :ivar p_icmsinter: Alíquota interestadual das UF
                    envolvidas Alíquota interestadual das UF envolvidas
                :ivar v_fcpuffim: Valor do ICMS relativo ao Fundo de
                    Combate á Pobreza (FCP) da UF de término da
                    prestação
                :ivar v_icmsuffim: Valor do ICMS de partilha para a UF
                    de término da prestação do serviço de transporte
                :ivar v_icmsufini: Valor do ICMS de partilha para a UF
                    de início da prestação do serviço de transporte
                """
                v_bcuffim: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vBCUFFim",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                p_fcpuffim: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "pFCPUFFim",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                p_icmsuffim: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "pICMSUFFim",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                p_icmsinter: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "pICMSInter",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                v_fcpuffim: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vFCPUFFim",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_icmsuffim: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vICMSUFFim",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_icmsufini: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vICMSUFIni",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )

        @dataclass
        class InfCteNorm:
            """
            :ivar inf_carga: Informações da Carga do CT-e
            :ivar inf_doc: Informações dos documentos transportados pelo
                CT-e Opcional para Redespacho Intermediario e Serviço
                vinculado a multimodal. Poderá não ser informado para os
                CT-e de redespacho intermediário e serviço vinculado a
                multimodal. Nos demais casos deverá sempre ser
                informado.
            :ivar doc_ant: Documentos de Transporte Anterior
            :ivar inf_modal: Informações do modal
            :ivar veic_novos: informações dos veículos transportados
            :ivar cobr: Dados da cobrança do CT-e
            :ivar inf_cte_sub: Informações do CT-e de substituição
            :ivar inf_globalizado: Informações do CT-e Globalizado
            :ivar inf_serv_vinc: Informações do Serviço Vinculado a
                Multimodal
            """
            inf_carga: Optional["Tcte.InfCte.InfCteNorm.InfCarga"] = field(
                default=None,
                metadata={
                    "name": "infCarga",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            inf_doc: Optional["Tcte.InfCte.InfCteNorm.InfDoc"] = field(
                default=None,
                metadata={
                    "name": "infDoc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            doc_ant: Optional["Tcte.InfCte.InfCteNorm.DocAnt"] = field(
                default=None,
                metadata={
                    "name": "docAnt",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            inf_modal: Optional["Tcte.InfCte.InfCteNorm.InfModal"] = field(
                default=None,
                metadata={
                    "name": "infModal",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            veic_novos: List["Tcte.InfCte.InfCteNorm.VeicNovos"] = field(
                default_factory=list,
                metadata={
                    "name": "veicNovos",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            cobr: Optional["Tcte.InfCte.InfCteNorm.Cobr"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            inf_cte_sub: Optional["Tcte.InfCte.InfCteNorm.InfCteSub"] = field(
                default=None,
                metadata={
                    "name": "infCteSub",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            inf_globalizado: Optional["Tcte.InfCte.InfCteNorm.InfGlobalizado"] = field(
                default=None,
                metadata={
                    "name": "infGlobalizado",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            inf_serv_vinc: Optional["Tcte.InfCte.InfCteNorm.InfServVinc"] = field(
                default=None,
                metadata={
                    "name": "infServVinc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )

            @dataclass
            class InfCarga:
                """
                :ivar v_carga: Valor total da carga Dever ser informado
                    para todos os modais, com exceção para o Dutoviário.
                :ivar pro_pred: Produto predominante Informar a
                    descrição do produto predominante
                :ivar x_out_cat: Outras características da carga "FRIA",
                    "GRANEL", "REFRIGERADA", "Medidas: 12X12X12"
                :ivar inf_q: Informações de quantidades da Carga do CT-e
                    Para o Aéreo é obrigatório o preenchimento desse
                    campo da seguinte forma. 1 - Peso Bruto, sempre em
                    quilogramas (obrigatório); 2 - Peso Cubado; sempre
                    em quilogramas; 3 - Quantidade de volumes, sempre em
                    unidades (obrigatório); 4 - Cubagem, sempre em
                    metros cúbicos (obrigatório apenas quando for
                    impossível preencher as dimensões da(s)
                    embalagem(ens) na tag xDime do leiaute do Aéreo).
                :ivar v_carga_averb: Valor da Carga para efeito de
                    averbação Normalmente igual ao valor declarado da
                    mercadoria, diferente por exemplo, quando a
                    mercadoria transportada é isenta de tributos
                    nacionais para exportação, onde é preciso averbar um
                    valor maior, pois no caso de indenização, o valor a
                    ser pago será maior
                """
                v_carga: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vCarga",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                pro_pred: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "proPred",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                x_out_cat: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xOutCat",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 30,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                inf_q: List["Tcte.InfCte.InfCteNorm.InfCarga.InfQ"] = field(
                    default_factory=list,
                    metadata={
                        "name": "infQ",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_occurs": 1,
                    }
                )
                v_carga_averb: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vCargaAverb",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

                @dataclass
                class InfQ:
                    """
                    :ivar c_unid: Código da Unidade de Medida Preencher
                        com: 00-M3; 01-KG; 02-TON; 03-UNIDADE;
                        04-LITROS; 05-MMBTU
                    :ivar tp_med: Tipo da Medida Exemplos: PESO BRUTO,
                        PESO DECLARADO, PESO CUBADO, PESO AFORADO, PESO
                        AFERIDO, PESO BASE DE CÁLCULO, LITRAGEM, CAIXAS
                        e etc
                    :ivar q_carga: Quantidade
                    """
                    c_unid: Optional[InfQCUnid] = field(
                        default=None,
                        metadata={
                            "name": "cUnid",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    tp_med: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "tpMed",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "min_length": 1,
                            "max_length": 20,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    q_carga: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "qCarga",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                        }
                    )

            @dataclass
            class InfDoc:
                """
                :ivar inf_nf: Informações das NF Este grupo deve ser
                    informado quando o documento originário for NF
                :ivar inf_nfe: Informações das NF-e
                :ivar inf_outros: Informações dos demais documentos
                """
                inf_nf: List["Tcte.InfCte.InfCteNorm.InfDoc.InfNf"] = field(
                    default_factory=list,
                    metadata={
                        "name": "infNF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                inf_nfe: List["Tcte.InfCte.InfCteNorm.InfDoc.InfNfe"] = field(
                    default_factory=list,
                    metadata={
                        "name": "infNFe",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                inf_outros: List["Tcte.InfCte.InfCteNorm.InfDoc.InfOutros"] = field(
                    default_factory=list,
                    metadata={
                        "name": "infOutros",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )

                @dataclass
                class InfNf:
                    """
                    :ivar n_roma: Número do Romaneio da NF
                    :ivar n_ped: Número do Pedido da NF
                    :ivar mod: Modelo da Nota Fiscal Preencher com: 01 -
                        NF Modelo 01/1A e Avulsa; 04 - NF de Produtor
                    :ivar serie: Série
                    :ivar n_doc: Número
                    :ivar d_emi: Data de Emissão Formato AAAA-MM-DD
                    :ivar v_bc: Valor da Base de Cálculo do ICMS
                    :ivar v_icms: Valor Total do ICMS
                    :ivar v_bcst: Valor da Base de Cálculo do ICMS ST
                    :ivar v_st: Valor Total do ICMS ST
                    :ivar v_prod: Valor Total dos Produtos
                    :ivar v_nf: Valor Total da NF
                    :ivar n_cfop: CFOP Predominante CFOP da NF ou, na
                        existência de mais de um, predominância pelo
                        critério de valor econômico.
                    :ivar n_peso: Peso total em Kg
                    :ivar pin: PIN SUFRAMA PIN atribuído pela SUFRAMA
                        para a operação.
                    :ivar d_prev: Data prevista de entrega Formato AAAA-
                        MM-DD
                    :ivar inf_unid_carga: Informações das Unidades de
                        Carga (Containeres/ULD/Outros) Dispositivo de
                        carga utilizada (Unit Load Device - ULD)
                        significa todo tipo de contêiner de carga,
                        vagão, contêiner de avião, palete de aeronave
                        com rede ou palete de aeronave com rede sobre um
                        iglu.
                    :ivar inf_unid_transp: Informações das Unidades de
                        Transporte (Carreta/Reboque/Vagão) Deve ser
                        preenchido com as informações das unidades de
                        transporte utilizadas.
                    """
                    n_roma: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nRoma",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 20,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    n_ped: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nPed",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 20,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    mod: Optional[TmodNf] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                        }
                    )
                    serie: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    n_doc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nDoc",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
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
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    v_bc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vBC",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_icms: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vICMS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_bcst: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vBCST",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_st: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vST",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_prod: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vProd",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_nf: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vNF",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    n_cfop: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nCFOP",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[123567][0-9]([0-9][1-9]|[1-9][0-9])",
                        }
                    )
                    n_peso: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nPeso",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[1-9]{1}[0-9]{2}|0\.[0-9]{2}[1-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?",
                        }
                    )
                    pin: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "PIN",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 2,
                            "max_length": 9,
                            "white_space": "preserve",
                            "pattern": r"[1-9]{1}[0-9]{1,8}",
                        }
                    )
                    d_prev: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "dPrev",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    inf_unid_carga: List[TunidCarga] = field(
                        default_factory=list,
                        metadata={
                            "name": "infUnidCarga",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )
                    inf_unid_transp: List[TunidadeTransp] = field(
                        default_factory=list,
                        metadata={
                            "name": "infUnidTransp",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )

                @dataclass
                class InfNfe:
                    """
                    :ivar chave: Chave de acesso da NF-e
                    :ivar pin: PIN SUFRAMA PIN atribuído pela SUFRAMA
                        para a operação.
                    :ivar d_prev: Data prevista de entrega Formato AAAA-
                        MM-DD
                    :ivar inf_unid_carga: Informações das Unidades de
                        Carga (Containeres/ULD/Outros) Dispositivo de
                        carga utilizada (Unit Load Device - ULD)
                        significa todo tipo de contêiner de carga,
                        vagão, contêiner de avião, palete de aeronave
                        com rede ou palete de aeronave com rede sobre um
                        iglu.
                    :ivar inf_unid_transp: Informações das Unidades de
                        Transporte (Carreta/Reboque/Vagão) Deve ser
                        preenchido com as informações das unidades de
                        transporte utilizadas.
                    """
                    chave: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
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
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 2,
                            "max_length": 9,
                            "white_space": "preserve",
                            "pattern": r"[1-9]{1}[0-9]{1,8}",
                        }
                    )
                    d_prev: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "dPrev",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    inf_unid_carga: List[TunidCarga] = field(
                        default_factory=list,
                        metadata={
                            "name": "infUnidCarga",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )
                    inf_unid_transp: List[TunidadeTransp] = field(
                        default_factory=list,
                        metadata={
                            "name": "infUnidTransp",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )

                @dataclass
                class InfOutros:
                    """
                    :ivar tp_doc: Tipo de documento originário Preencher
                        com: 00 - Declaração; 10 - Dutoviário; 59 - CF-e
                        SAT; 65 - NFC-e; 99 - Outros
                    :ivar desc_outros: Descrição do documento
                    :ivar n_doc: Número
                    :ivar d_emi: Data de Emissão Formato AAAA-MM-DD
                    :ivar v_doc_fisc: Valor do documento
                    :ivar d_prev: Data prevista de entrega Formato AAAA-
                        MM-DD
                    :ivar inf_unid_carga: Informações das Unidades de
                        Carga (Containeres/ULD/Outros) Dispositivo de
                        carga utilizada (Unit Load Device - ULD)
                        significa todo tipo de contêiner de carga,
                        vagão, contêiner de avião, palete de aeronave
                        com rede ou palete de aeronave com rede sobre um
                        iglu.
                    :ivar inf_unid_transp: Informações das Unidades de
                        Transporte (Carreta/Reboque/Vagão) Deve ser
                        preenchido com as informações das unidades de
                        transporte utilizadas.
                    """
                    tp_doc: Optional[InfOutrosTpDoc] = field(
                        default=None,
                        metadata={
                            "name": "tpDoc",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    desc_outros: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "descOutros",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 100,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    n_doc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nDoc",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
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
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    v_doc_fisc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vDocFisc",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    d_prev: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "dPrev",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    inf_unid_carga: List[TunidCarga] = field(
                        default_factory=list,
                        metadata={
                            "name": "infUnidCarga",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )
                    inf_unid_transp: List[TunidadeTransp] = field(
                        default_factory=list,
                        metadata={
                            "name": "infUnidTransp",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )

            @dataclass
            class DocAnt:
                """
                :ivar emi_doc_ant: Emissor do documento anterior
                """
                emi_doc_ant: List["Tcte.InfCte.InfCteNorm.DocAnt.EmiDocAnt"] = field(
                    default_factory=list,
                    metadata={
                        "name": "emiDocAnt",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_occurs": 1,
                    }
                )

                @dataclass
                class EmiDocAnt:
                    """
                    :ivar cnpj: Número do CNPJ Em caso de empresa não
                        estabelecida no Brasil, será informado o CNPJ
                        com zeros. Informar os zeros não significativos.
                    :ivar cpf: Número do CPF Informar os zeros não
                        significativos.
                    :ivar ie: Inscrição Estadual
                    :ivar uf: Sigla da UF Informar EX para operações com
                        o exterior.
                    :ivar x_nome: Razão Social ou Nome do expedidor
                    :ivar id_doc_ant: Informações de identificação dos
                        documentos de Transporte Anterior
                    """
                    cnpj: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "CNPJ",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{0}|[0-9]{14}",
                        }
                    )
                    cpf: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "CPF",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{11}",
                        }
                    )
                    ie: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "IE",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "max_length": 14,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{2,14}",
                        }
                    )
                    uf: Optional[Tuf] = field(
                        default=None,
                        metadata={
                            "name": "UF",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )
                    x_nome: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "xNome",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "min_length": 1,
                            "max_length": 60,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    id_doc_ant: List["Tcte.InfCte.InfCteNorm.DocAnt.EmiDocAnt.IdDocAnt"] = field(
                        default_factory=list,
                        metadata={
                            "name": "idDocAnt",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_occurs": 1,
                            "max_occurs": 2,
                        }
                    )

                    @dataclass
                    class IdDocAnt:
                        """
                        :ivar id_doc_ant_pap: Documentos de transporte
                            anterior em papel
                        :ivar id_doc_ant_ele: Documentos de transporte
                            anterior eletrônicos
                        """
                        id_doc_ant_pap: List["Tcte.InfCte.InfCteNorm.DocAnt.EmiDocAnt.IdDocAnt.IdDocAntPap"] = field(
                            default_factory=list,
                            metadata={
                                "name": "idDocAntPap",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                            }
                        )
                        id_doc_ant_ele: List["Tcte.InfCte.InfCteNorm.DocAnt.EmiDocAnt.IdDocAnt.IdDocAntEle"] = field(
                            default_factory=list,
                            metadata={
                                "name": "idDocAntEle",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                            }
                        )

                        @dataclass
                        class IdDocAntPap:
                            """
                            :ivar tp_doc: Tipo do Documento de
                                Transporte Anterior Preencher com:
                                07-ATRE; 08-DTA (Despacho de Transito
                                Aduaneiro); 09-Conhecimento Aéreo
                                Internacional; 10 – Conhecimento - Carta
                                de Porte Internacional; 11 –
                                Conhecimento Avulso; 12-TIF (Transporte
                                Internacional Ferroviário); 13-BL (Bill
                                of Lading)
                            :ivar serie: Série do Documento Fiscal
                            :ivar subser: Série do Documento Fiscal
                            :ivar n_doc: Número do Documento Fiscal
                            :ivar d_emi: Data de emissão (AAAA-MM-DD)
                            """
                            tp_doc: Optional[TdocAssoc] = field(
                                default=None,
                                metadata={
                                    "name": "tpDoc",
                                    "type": "Element",
                                    "namespace": "http://www.portalfiscal.inf.br/cte",
                                    "required": True,
                                }
                            )
                            serie: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "namespace": "http://www.portalfiscal.inf.br/cte",
                                    "required": True,
                                    "min_length": 1,
                                    "max_length": 3,
                                    "white_space": "preserve",
                                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                                }
                            )
                            subser: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "namespace": "http://www.portalfiscal.inf.br/cte",
                                    "min_length": 1,
                                    "max_length": 2,
                                    "white_space": "preserve",
                                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                                }
                            )
                            n_doc: Optional[str] = field(
                                default=None,
                                metadata={
                                    "name": "nDoc",
                                    "type": "Element",
                                    "namespace": "http://www.portalfiscal.inf.br/cte",
                                    "required": True,
                                    "min_length": 1,
                                    "max_length": 30,
                                    "white_space": "preserve",
                                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                                }
                            )
                            d_emi: Optional[str] = field(
                                default=None,
                                metadata={
                                    "name": "dEmi",
                                    "type": "Element",
                                    "namespace": "http://www.portalfiscal.inf.br/cte",
                                    "required": True,
                                    "white_space": "preserve",
                                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                                }
                            )

                        @dataclass
                        class IdDocAntEle:
                            """
                            :ivar ch_cte: Chave de acesso do CT-e
                            """
                            ch_cte: Optional[str] = field(
                                default=None,
                                metadata={
                                    "name": "chCTe",
                                    "type": "Element",
                                    "namespace": "http://www.portalfiscal.inf.br/cte",
                                    "required": True,
                                    "max_length": 44,
                                    "white_space": "preserve",
                                    "pattern": r"[0-9]{44}",
                                }
                            )

            @dataclass
            class InfModal:
                """
                :ivar any_element: XML do modal Insira neste local o XML
                    específico do modal (rodoviário, aéreo, ferroviário,
                    aquaviário ou dutoviário). O elemento do tipo -any-
                    permite estender o documento XML com elementos não
                    especificados pelo schema. Insira neste local - any-
                    o XML específico do modal (rodoviário, aéreo,
                    ferroviário, aquaviário ou dutoviário). A
                    especificação do schema XML para cada modal pode ser
                    encontrada nos arquivos que acompanham este pacote
                    de liberação: Rodoviário - ver arquivo
                    CTeModalRodoviario_v9.99 Aéreo - ver arquivo
                    CTeModalAereo_v9.99 Aquaviário - arquivo
                    CTeModalAquaviario_v9.99 Ferroviário - arquivo
                    CTeModalFerroviario_v9.99 Dutoviário - arquivo
                    CTeModalDutoviario_v9.99 Onde v9.99 é a a designação
                    genérica para a versão do arquivo. Por exemplo, o
                    arquivo para o schema do modal Rodoviário na versão
                    1.04 será denominado "CTeModalRodoviario_v1.04".
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
            class VeicNovos:
                """
                :ivar chassi: Chassi do veículo
                :ivar c_cor: Cor do veículo Código de cada montadora
                :ivar x_cor: Descrição da cor
                :ivar c_mod: Código Marca Modelo Utilizar tabela RENAVAM
                :ivar v_unit: Valor Unitário do Veículo
                :ivar v_frete: Frete Unitário
                """
                chassi: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "length": 17,
                        "white_space": "preserve",
                        "pattern": r"[A-Z0-9]+",
                    }
                )
                c_cor: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cCor",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 4,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                x_cor: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xCor",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 40,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                c_mod: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cMod",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 6,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                v_unit: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vUnit",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_frete: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vFrete",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

            @dataclass
            class Cobr:
                """
                :ivar fat: Dados da fatura
                :ivar dup: Dados das duplicatas
                """
                fat: Optional["Tcte.InfCte.InfCteNorm.Cobr.Fat"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                dup: List["Tcte.InfCte.InfCteNorm.Cobr.Dup"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )

                @dataclass
                class Fat:
                    """
                    :ivar n_fat: Número da fatura
                    :ivar v_orig: Valor original da fatura
                    :ivar v_desc: Valor do desconto da fatura
                    :ivar v_liq: Valor líquido da fatura
                    """
                    n_fat: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nFat",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 60,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    v_orig: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vOrig",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_desc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vDesc",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_liq: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vLiq",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )

                @dataclass
                class Dup:
                    """
                    :ivar n_dup: Número da duplicata
                    :ivar d_venc: Data de vencimento da duplicata (AAAA-
                        MM-DD)
                    :ivar v_dup: Valor da duplicata
                    """
                    n_dup: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nDup",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 60,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    d_venc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "dVenc",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    v_dup: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vDup",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )

            @dataclass
            class InfCteSub:
                """
                :ivar ch_cte: Chave de acesso do CT-e a ser substituído
                    (original)
                :ivar ref_cte_anu: Chave de acesso do CT-e de Anulação
                :ivar toma_icms: Tomador é contribuinte do ICMS, mas não
                    é emitente de documento fiscal eletrônico
                :ivar ind_altera_toma: Indicador de CT-e Alteração de
                    Tomador
                """
                ch_cte: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "chCte",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "pattern": r"[0-9]{44}",
                    }
                )
                ref_cte_anu: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "refCteAnu",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "max_length": 44,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{44}",
                    }
                )
                toma_icms: Optional["Tcte.InfCte.InfCteNorm.InfCteSub.TomaIcms"] = field(
                    default=None,
                    metadata={
                        "name": "tomaICMS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                ind_altera_toma: Optional[InfCteSubIndAlteraToma] = field(
                    default=None,
                    metadata={
                        "name": "indAlteraToma",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )

                @dataclass
                class TomaIcms:
                    """
                    :ivar ref_nfe: Chave de acesso da NF-e emitida pelo
                        Tomador
                    :ivar ref_nf: Informação da NF ou CT emitido pelo
                        Tomador
                    :ivar ref_cte: Chave de acesso do CT-e emitido pelo
                        Tomador
                    """
                    ref_nfe: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "refNFe",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "max_length": 44,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{44}",
                        }
                    )
                    ref_nf: Optional["Tcte.InfCte.InfCteNorm.InfCteSub.TomaIcms.RefNf"] = field(
                        default=None,
                        metadata={
                            "name": "refNF",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )
                    ref_cte: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "refCte",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "max_length": 44,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{44}",
                        }
                    )

                    @dataclass
                    class RefNf:
                        """
                        :ivar cnpj: CNPJ do Emitente Informar o CNPJ do
                            emitente do Documento Fiscal
                        :ivar cpf: Número do CPF Informar o CPF do
                            emitente do documento fiscal
                        :ivar mod: Modelo do Documento Fiscal
                        :ivar serie: Serie do documento fiscal
                        :ivar subserie: Subserie do documento fiscal
                        :ivar nro: Número do documento fiscal
                        :ivar valor: Valor do documento fiscal.
                        :ivar d_emi: Data de emissão do documento
                            fiscal.
                        """
                        cnpj: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "CNPJ",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "white_space": "preserve",
                                "pattern": r"[0-9]{14}",
                            }
                        )
                        cpf: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "CPF",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "white_space": "preserve",
                                "pattern": r"[0-9]{11}",
                            }
                        )
                        mod: Optional[TmodDoc] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "required": True,
                            }
                        )
                        serie: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                            }
                        )
                        subserie: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "white_space": "preserve",
                                "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                            }
                        )
                        nro: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{1,6}",
                            }
                        )
                        valor: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        d_emi: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "dEmi",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                            }
                        )

            @dataclass
            class InfGlobalizado:
                """
                :ivar x_obs: Preencher com informações adicionais,
                    legislação do regime especial, etc
                """
                x_obs: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xObs",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 15,
                        "max_length": 256,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )

            @dataclass
            class InfServVinc:
                """
                :ivar inf_cte_multimodal: informações do CT-e multimodal
                    vinculado
                """
                inf_cte_multimodal: List["Tcte.InfCte.InfCteNorm.InfServVinc.InfCteMultimodal"] = field(
                    default_factory=list,
                    metadata={
                        "name": "infCTeMultimodal",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_occurs": 1,
                    }
                )

                @dataclass
                class InfCteMultimodal:
                    """
                    :ivar ch_cte_multimodal: Chave de acesso do CT-e
                        Multimodal
                    """
                    ch_cte_multimodal: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "chCTeMultimodal",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "max_length": 44,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{44}",
                        }
                    )

        @dataclass
        class InfCteComp:
            """
            :ivar ch_cte: Chave do CT-e complementado
            """
            ch_cte: Optional[str] = field(
                default=None,
                metadata={
                    "name": "chCTe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "max_length": 44,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{44}",
                }
            )

        @dataclass
        class InfCteAnu:
            """
            :ivar ch_cte: Chave de acesso do CT-e original a ser anulado
                e substituído
            :ivar d_emi: Data de emissão da declaração do tomador não
                contribuinte do ICMS
            """
            ch_cte: Optional[str] = field(
                default=None,
                metadata={
                    "name": "chCte",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "pattern": r"[0-9]{44}",
                }
            )
            d_emi: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )

    @dataclass
    class InfCteSupl:
        """
        :ivar qr_cod_cte: Texto com o QR-Code impresso no DACTE
        """
        qr_cod_cte: Optional[str] = field(
            default=None,
            metadata={
                "name": "qrCodCTe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 50,
                "max_length": 1000,
                "white_space": "preserve",
                "pattern": r"((HTTPS?|https?)://.*\?chCTe=[0-9]{44}&tpAmb=[1-2](&sign=[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})?)",
            }
        )


@dataclass
class TenviCte:
    """
    Tipo Pedido de Concessão de Autorização da CT-e.
    """
    class Meta:
        name = "TEnviCTe"

    id_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "idLote",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,15}",
        }
    )
    cte: List[Tcte] = field(
        default_factory=list,
        metadata={
            "name": "CTe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "min_occurs": 1,
            "max_occurs": 50,
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
