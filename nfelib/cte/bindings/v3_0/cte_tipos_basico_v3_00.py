from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.cte.bindings.v3_0.evento_cte_tipos_basico_v3_00 import TmodTransp
from nfelib.cte.bindings.v3_0.tipos_geral_cte_v3_00 import (
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
from nfelib.cte.bindings.v3_0.xmldsig_core_schema_v1_01 import Signature

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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    xContato: Optional[str] = field(
        default=None,
        metadata={
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
    idCSRT: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "pattern": r"[0-9]{3}",
        }
    )
    hashCSRT: Optional[bytes] = field(
        default=None,
        metadata={
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

    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar xMun: Nome do município Informar EXTERIOR para operações com o
        exterior.
    :ivar CEP: CEP
    :ivar UF: Sigla da UF Informar EX para operações com o exterior.
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
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
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
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    cPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    xPais: Optional[str] = field(
        default=None,
        metadata={
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

    :ivar CNPJ: Número do CNPJ
    :ivar CPF: Número do CPF
    :ivar xNome: Razão Social ou Nome
    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município (utilizar a tabela do IBGE) Informar
        9999999 para operações com o exterior.
    :ivar xMun: Nome do município Informar EXTERIOR para operações com o
        exterior.
    :ivar UF: Sigla da UF Informar EX para operações com o exterior.
    """
    class Meta:
        name = "TEndReEnt"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    CPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    xNome: Optional[str] = field(
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
    xLgr: Optional[str] = field(
        default=None,
        metadata={
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
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
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
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
    :ivar cMun: Código do município (utilizar a tabela do IBGE)
    :ivar xMun: Nome do município
    :ivar CEP: CEP Informar zeros não significativos
    :ivar UF: Sigla da UF
    :ivar fone: Telefone
    """
    class Meta:
        name = "TEndeEmi"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
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
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    UF: Optional[TufSemEx] = field(
        default=None,
        metadata={
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

    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município (utilizar a tabela do IBGE) Informar
        9999999 para operações com o exterior.
    :ivar xMun: Nome do município Informar EXTERIOR para operações com o
        exterior.
    :ivar CEP: CEP Informar os zeros não significativos
    :ivar UF: Sigla da UF Informar EX para operações com o exterior.
    :ivar cPais: Código do país Utilizar a tabela do BACEN
    :ivar xPais: Nome do país
    """
    class Meta:
        name = "TEndereco"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
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
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    cPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    xPais: Optional[str] = field(
        default=None,
        metadata={
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

    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar xMun: Nome do município, , informar EXTERIOR para operações
        com o exterior.
    :ivar CEP: CEP
    :ivar UF: Sigla da UF Informar EX para operações com o exterior.
    """
    class Meta:
        name = "TEndernac"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
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
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
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
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )


@dataclass
class Timp:
    """
    Tipo Dados do Imposto CT-e.

    :ivar ICMS00: Prestação sujeito à tributação normal do ICMS
    :ivar ICMS20: Prestação sujeito à tributação com redução de BC do
        ICMS
    :ivar ICMS45: ICMS  Isento, não Tributado ou diferido
    :ivar ICMS60: Tributação pelo ICMS60 - ICMS cobrado por substituição
        tributária.Responsabilidade do recolhimento do ICMS atribuído ao
        tomador ou 3º por ST
    :ivar ICMS90: ICMS Outros
    :ivar ICMSOutraUF: ICMS devido à UF de origem da prestação, quando
        diferente da UF do emitente
    :ivar ICMSSN: Simples Nacional
    """
    class Meta:
        name = "TImp"

    ICMS00: Optional["Timp.Icms00"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    ICMS20: Optional["Timp.Icms20"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    ICMS45: Optional["Timp.Icms45"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    ICMS60: Optional["Timp.Icms60"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    ICMS90: Optional["Timp.Icms90"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    ICMSOutraUF: Optional["Timp.IcmsoutraUf"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    ICMSSN: Optional["Timp.Icmssn"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )

    @dataclass
    class Icms00:
        """
        :ivar CST: classificação Tributária do Serviço 00 - tributação
            normal ICMS
        :ivar vBC: Valor da BC do ICMS
        :ivar pICMS: Alíquota do ICMS
        :ivar vICMS: Valor do ICMS
        """
        CST: Optional[Icms00Cst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        vBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pICMS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vICMS: Optional[str] = field(
            default=None,
            metadata={
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
        :ivar CST: Classificação Tributária do serviço 20 - tributação
            com BC reduzida do ICMS
        :ivar pRedBC: Percentual de redução da BC
        :ivar vBC: Valor da BC do ICMS
        :ivar pICMS: Alíquota do ICMS
        :ivar vICMS: Valor do ICMS
        """
        CST: Optional[Icms20Cst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        pRedBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pICMS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vICMS: Optional[str] = field(
            default=None,
            metadata={
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
        :ivar CST: Classificação Tributária do Serviço Preencher com: 40
            - ICMS isenção; 41 - ICMS não tributada; 51 - ICMS diferido
        """
        CST: Optional[Icms45Cst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )

    @dataclass
    class Icms60:
        """
        :ivar CST: Classificação Tributária do Serviço 60 - ICMS cobrado
            por substituição tributária
        :ivar vBCSTRet: Valor da BC do ICMS ST retido Valor do frete
            sobre o qual será calculado o ICMS a ser substituído na
            Prestação.
        :ivar vICMSSTRet: Valor do ICMS ST retido Resultado da
            multiplicação do “vBCSTRet” x “pICMSSTRet” – que será valor
            do ICMS a ser retido pelo Substituto. Podendo o valor do
            ICMS a ser retido efetivamente, sofrer ajustes conforme a
            opção tributaria do transportador substituído.
        :ivar pICMSSTRet: Alíquota do ICMS Percentual de Alíquota
            incidente na prestação de serviço de transporte.
        :ivar vCred: Valor do Crédito outorgado/Presumido Preencher
            somente quando o transportador substituído, for optante pelo
            crédito outorgado previsto no Convênio 106/96 e corresponde
            ao percentual de 20% do valor do ICMS ST retido.
        """
        CST: Optional[Icms60Cst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        vBCSTRet: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        vICMSSTRet: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pICMSSTRet: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vCred: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass
    class Icms90:
        """
        :ivar CST: Classificação Tributária do Serviço 90 - ICMS outros
        :ivar pRedBC: Percentual de redução da BC
        :ivar vBC: Valor da BC do ICMS
        :ivar pICMS: Alíquota do ICMS
        :ivar vICMS: Valor do ICMS
        :ivar vCred: Valor do Crédito Outorgado/Presumido
        """
        CST: Optional[Icms90Cst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        pRedBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pICMS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vICMS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        vCred: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass
    class IcmsoutraUf:
        """
        :ivar CST: Classificação Tributária do Serviço 90 - ICMS Outra
            UF
        :ivar pRedBCOutraUF: Percentual de redução da BC
        :ivar vBCOutraUF: Valor da BC do ICMS
        :ivar pICMSOutraUF: Alíquota do ICMS
        :ivar vICMSOutraUF: Valor do ICMS devido outra UF
        """
        CST: Optional[IcmsoutraUfCst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        pRedBCOutraUF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vBCOutraUF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pICMSOutraUF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vICMSOutraUF: Optional[str] = field(
            default=None,
            metadata={
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
        :ivar CST: Classificação Tributária do Serviço 90 - ICMS Simples
            Nacional
        :ivar indSN: Indica se o contribuinte é Simples Nacional
            1=Sim
        """
        CST: Optional[IcmssnCst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        indSN: Optional[IcmssnIndSn] = field(
            default=None,
            metadata={
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

    :ivar ICMS00: Prestação sujeito à tributação normal do ICMS
    :ivar ICMS20: Prestação sujeito à tributação com redução de BC do
        ICMS
    :ivar ICMS45: ICMS  Isento, não Tributado ou diferido
    :ivar ICMS90: ICMS Outros
    :ivar ICMSOutraUF: ICMS devido à UF de origem da prestação, quando
        diferente da UF do emitente
    :ivar ICMSSN: Simples Nacional
    """
    class Meta:
        name = "TImpOS"

    ICMS00: Optional["TimpOs.Icms00"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    ICMS20: Optional["TimpOs.Icms20"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    ICMS45: Optional["TimpOs.Icms45"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    ICMS90: Optional["TimpOs.Icms90"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    ICMSOutraUF: Optional["TimpOs.IcmsoutraUf"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    ICMSSN: Optional["TimpOs.Icmssn"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )

    @dataclass
    class Icms00:
        """
        :ivar CST: classificação Tributária do Serviço 00 - tributação
            normal ICMS
        :ivar vBC: Valor da BC do ICMS
        :ivar pICMS: Alíquota do ICMS
        :ivar vICMS: Valor do ICMS
        """
        CST: Optional[Icms00Cst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        vBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pICMS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vICMS: Optional[str] = field(
            default=None,
            metadata={
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
        :ivar CST: Classificação Tributária do serviço 20 - tributação
            com BC reduzida do ICMS
        :ivar pRedBC: Percentual de redução da BC
        :ivar vBC: Valor da BC do ICMS
        :ivar pICMS: Alíquota do ICMS
        :ivar vICMS: Valor do ICMS
        """
        CST: Optional[Icms20Cst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        pRedBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pICMS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vICMS: Optional[str] = field(
            default=None,
            metadata={
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
        :ivar CST: Classificação Tributária do Serviço Preencher com: 40
            - ICMS isenção; 41 - ICMS não tributada; 51 - ICMS diferido
        """
        CST: Optional[Icms45Cst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )

    @dataclass
    class Icms90:
        """
        :ivar CST: Classificação Tributária do Serviço 90 - Outros
        :ivar pRedBC: Percentual de redução da BC
        :ivar vBC: Valor da BC do ICMS
        :ivar pICMS: Alíquota do ICMS
        :ivar vICMS: Valor do ICMS
        :ivar vCred: Valor do Crédito Outorgado/Presumido
        """
        CST: Optional[Icms90Cst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        pRedBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pICMS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vICMS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        vCred: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass
    class IcmsoutraUf:
        """
        :ivar CST: Classificação Tributária do Serviço 90 - ICMS Outra
            UF
        :ivar pRedBCOutraUF: Percentual de redução da BC
        :ivar vBCOutraUF: Valor da BC do ICMS
        :ivar pICMSOutraUF: Alíquota do ICMS
        :ivar vICMSOutraUF: Valor do ICMS devido outra UF
        """
        CST: Optional[IcmsoutraUfCst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        pRedBCOutraUF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vBCOutraUF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pICMSOutraUF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vICMSOutraUF: Optional[str] = field(
            default=None,
            metadata={
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
        :ivar CST: Classificação Tributária do Serviço 90 - ICMS Simples
            Nacional
        :ivar indSN: Indica se o contribuinte é Simples Nacional
            1=Sim
        """
        CST: Optional[IcmssnCst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
            }
        )
        indSN: Optional[IcmssnIndSn] = field(
            default=None,
            metadata={
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
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
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )


@dataclass
class TprotCte:
    """
    Tipo Protocolo de status resultado do processamento da CT-e.

    :ivar infProt: Dados do protocolo de status
    :ivar infFisco: Mensagem do Fisco
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TProtCTe"

    infProt: Optional["TprotCte.InfProt"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    infFisco: Optional["TprotCte.InfFisco"] = field(
        default=None,
        metadata={
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
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar verAplic: Versão do Aplicativo que processou o CT-e
        :ivar chCTe: Chaves de acesso da CT-e,
        :ivar dhRecbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS TZD.
        :ivar nProt: Número do Protocolo de Status do CT-e.
        :ivar digVal: Digest Value da CT-e processado. Utilizado para
            conferir a integridade do CT-e original.
        :ivar cStat: Código do status do CT-e.
        :ivar xMotivo: Descrição literal do status do CT-e.
        :ivar Id:
        """
        tpAmb: Optional[Tamb] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        verAplic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        chCTe: Optional[str] = field(
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
        dhRecbto: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        nProt: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        digVal: Optional[bytes] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "format": "base64",
            }
        )
        cStat: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMotivo: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMsg: Optional[str] = field(
            default=None,
            metadata={
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

    :ivar infProt: Dados do protocolo de status
    :ivar infFisco: Mensagem do Fisco
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TProtCTeOS"

    infProt: Optional["TprotCteOs.InfProt"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    infFisco: Optional["TprotCteOs.InfFisco"] = field(
        default=None,
        metadata={
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
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar verAplic: Versão do Aplicativo que processou o CT-e
        :ivar chCTe: Chaves de acesso da CT-e
        :ivar dhRecbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS TZD.
        :ivar nProt: Número do Protocolo de Status do CT-e.
        :ivar digVal: Digest Value da CT-e processado. Utilizado para
            conferir a integridade do CT-e original.
        :ivar cStat: Código do status do CT-e.
        :ivar xMotivo: Descrição literal do status do CT-e.
        :ivar Id:
        """
        tpAmb: Optional[Tamb] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        verAplic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        chCTe: Optional[str] = field(
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
        dhRecbto: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        nProt: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        digVal: Optional[bytes] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "format": "base64",
            }
        )
        cStat: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMotivo: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMsg: Optional[str] = field(
            default=None,
            metadata={
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

    :ivar infProt: Dados do protocolo de status
    :ivar infFisco: Mensagem do Fisco
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TProtGTVe"

    infProt: Optional["TprotGtve.InfProt"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    infFisco: Optional["TprotGtve.InfFisco"] = field(
        default=None,
        metadata={
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
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar verAplic: Versão do Aplicativo que processou a GTV-e
        :ivar chCTe: Chaves de acesso da CT-e
        :ivar dhRecbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS TZD.
        :ivar nProt: Número do Protocolo de Status da GTV-e
        :ivar digVal: Digest Value da GTV-e processado. Utilizado para
            conferir a integridade da GTV-e original.
        :ivar cStat: Código do status da GTV-e.
        :ivar xMotivo: Descrição literal do status da GTV-e.
        :ivar Id:
        """
        tpAmb: Optional[Tamb] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        verAplic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        chCTe: Optional[str] = field(
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
        dhRecbto: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        nProt: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        digVal: Optional[bytes] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "format": "base64",
            }
        )
        cStat: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMotivo: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMsg: Optional[str] = field(
            default=None,
            metadata={
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

    :ivar tpAmb: Identificação do Ambiente:1 - Produção; 2 - Homologação
    :ivar cUF: Identificação da UF
    :ivar verAplic: Versão do Aplicativo que recebeu o Lote.
    :ivar cStat: Código do status da mensagem enviada.
    :ivar xMotivo: Descrição literal do status do serviço solicitado.
    :ivar infRec: Dados do Recibo do Lote
    :ivar versao:
    """
    class Meta:
        name = "TRetEnviCTe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    infRec: Optional["TretEnviCte.InfRec"] = field(
        default=None,
        metadata={
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
        :ivar nRec: Número do Recibo
        :ivar dhRecbto: Data e hora do recebimento, no formato AAAA-MM-
            DDTHH:MM:SS TZD
        :ivar tMed: Tempo médio de resposta do serviço (em segundos) dos
            últimos 5 minutos
        """
        nRec: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        dhRecbto: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        tMed: Optional[str] = field(
            default=None,
            metadata={
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

    :ivar tpUnidCarga: Tipo da Unidade de Carga 1 - Container 2 - ULD 3
        - Pallet 4 - Outros
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    idUnidCarga: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    qtdRat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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

    :ivar infCte: Informações do CT-e Outros Serviços
    :ivar infCTeSupl: Informações suplementares do CT-e
    :ivar signature:
    :ivar versao: Versão do leiaute
    """
    class Meta:
        name = "TCTeOS"

    infCte: Optional["TcteOs.InfCte"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    infCTeSupl: Optional["TcteOs.InfCteSupl"] = field(
        default=None,
        metadata={
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
        :ivar vPrest: Valores da Prestação de Serviço
        :ivar imp: Informações relativas aos Impostos
        :ivar infCTeNorm: Grupo de informações do CT-e OS Normal
        :ivar infCteComp: Detalhamento do CT-e complementado
        :ivar infCteAnu: Detalhamento do CT-e do tipo Anulação
        :ivar autXML: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar infRespTec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar versao: Versão do leiaute Ex: "3.00"
        :ivar Id: Identificador da tag a ser assinada Informar a chave
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
        vPrest: Optional["TcteOs.InfCte.VPrest"] = field(
            default=None,
            metadata={
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
        infCTeNorm: Optional["TcteOs.InfCte.InfCteNorm"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        infCteComp: Optional["TcteOs.InfCte.InfCteComp"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        infCteAnu: Optional["TcteOs.InfCte.InfCteAnu"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        autXML: List["TcteOs.InfCte.AutXml"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "max_occurs": 10,
            }
        )
        infRespTec: Optional[TrespTec] = field(
            default=None,
            metadata={
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
        Id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"CTe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar cUF: Código da UF do emitente do CT-e. Utilizar a
                Tabela do IBGE.
            :ivar cCT: Código numérico que compõe a Chave de Acesso.
                Número aleatório gerado pelo emitente para cada CT-e,
                com o objetivo de evitar acessos indevidos ao documento.
            :ivar CFOP: Código Fiscal de Operações e Prestações
            :ivar natOp: Natureza da Operação
            :ivar mod: Modelo do documento fiscal Utilizar o código 67
                para identificação do CT-e Outros Serviços, emitido em
                substituição a Nota Fiscal Modelo 7 para transporte de
                pessoas, valores e excesso de bagagem.
            :ivar serie: Série do CT-e OS Preencher com "0" no caso de
                série única
            :ivar nCT: Número do CT-e OS
            :ivar dhEmi: Data e hora de emissão do CT-e OS Formato AAAA-
                MM-DDTHH:MM:DD TZD
            :ivar tpImp: Formato de impressão do DACTE OS Preencher com:
                1 - Retrato; 2 - Paisagem.
            :ivar tpEmis: Forma de emissão do CT-e Preencher com: 1 -
                Normal; 5 - Contingência FSDA; 7 - Autorização pela SVC-
                RS; 8 - Autorização pela SVC-SP
            :ivar cDV: Digito Verificador da chave de acesso do CT-e
                Informar o dígito  de controle da chave de acesso do
                CT-e, que deve ser calculado com a aplicação do
                algoritmo módulo 11 (base 2,9) da chave de acesso.
            :ivar tpAmb: Tipo do Ambiente Preencher com:1 - Produção; 2
                - Homologação
            :ivar tpCTe: Tipo do CT-e OS Preencher com: 0 - CT-e Normal;
                1 - CT-e Complementar; 2 - CT-e de Anulação; 3 - CT-e de
                Substituição.
            :ivar procEmi: Identificador do processo de emissão do CT-e
                OS Preencher com: 0 - emissão de CT-e com aplicativo do
                contribuinte; 3- emissão CT-e pelo contribuinte com
                aplicativo fornecido pelo Fisco.
            :ivar verProc: Versão do processo de emissão Iinformar a
                versão do aplicativo emissor de CT-e.
            :ivar cMunEnv: Código do Município de envio do CT-e (de onde
                o documento foi transmitido) Utilizar a tabela do IBGE.
                Informar 9999999 para as operações com o exterior.
            :ivar xMunEnv: Nome do Município de envio do CT-e (de onde o
                documento foi transmitido) Informar PAIS/Municipio para
                as operações com o exterior.
            :ivar UFEnv: Sigla da UF de envio do CT-e (de onde o
                documento foi transmitido) Informar 'EX' para operações
                com o exterior.
            :ivar modal: Modal do CT-e OS Preencher com: 01-Rodoviário;
                02- Aéreo; 03 - Aquaviário; 04 - Ferroviário.
            :ivar tpServ: Tipo do Serviço Preencher com: 6 - Transporte
                de Pessoas; 7 - Transporte de Valores; 8 - Excesso de
                Bagagem.
            :ivar indIEToma: Indicador da IE do tomador: 1 –
                Contribuinte ICMS; 2 – Contribuinte isento de inscrição;
                9 – Não Contribuinte Aplica-se ao tomador que for
                indicado no toma3 ou toma4
            :ivar cMunIni: Código do Município de início da prestação
                Utilizar a tabela do IBGE. Informar 9999999 para
                operações com o exterior.
            :ivar xMunIni: Nome do Município do início da prestação
                Informar 'EXTERIOR' para operações com o exterior.
            :ivar UFIni: UF do início da prestação Informar 'EX' para
                operações com o exterior.
            :ivar cMunFim: Código do Município de término da prestação
                Utilizar a tabela do IBGE. Informar 9999999 para
                operações com o exterior.
            :ivar xMunFim: Nome do Município do término da prestação
                Informar 'EXTERIOR' para operações com o exterior.
            :ivar UFFim: UF do término da prestação Informar 'EX' para
                operações com o exterior.
            :ivar infPercurso: Informações do Percurso do CT-e Outros
                Serviços
            :ivar dhCont: Data e Hora da entrada em contingência
                Informar a data e hora no formato AAAA-MM-DDTHH:MM:SS
            :ivar xJust: Justificativa da entrada em contingência
            """
            cUF: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            cCT: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            CFOP: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[123567][0-9]([0-9][1-9]|[1-9][0-9])",
                }
            )
            natOp: Optional[str] = field(
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
            nCT: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            dhEmi: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tpImp: Optional[IdeTpImp] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tpEmis: Optional[IdeTpEmis] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            cDV: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
                }
            )
            tpAmb: Optional[Tamb] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            tpCTe: Optional[TfinCte] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            procEmi: Optional[TprocEmi] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            verProc: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            cMunEnv: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            xMunEnv: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            UFEnv: Optional[Tuf] = field(
                default=None,
                metadata={
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
            tpServ: Optional[IdeTpServ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            indIEToma: Optional[IdeIndIetoma] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            cMunIni: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            xMunIni: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            UFIni: Optional[Tuf] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            cMunFim: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            xMunFim: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            UFFim: Optional[Tuf] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            infPercurso: List["TcteOs.InfCte.Ide.InfPercurso"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_occurs": 25,
                }
            )
            dhCont: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            xJust: Optional[str] = field(
                default=None,
                metadata={
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
                :ivar UFPer: Sigla das Unidades da Federação do percurso
                    do veículo. Não é necessário repetir as UF de Início
                    e Fim
                """
                UFPer: Optional[Tuf] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                    }
                )

        @dataclass
        class Compl:
            """
            :ivar xCaracAd: Característica adicional do transporte Texto
                livre: REENTREGA; DEVOLUÇÃO; REFATURAMENTO; etc
            :ivar xCaracSer: Característica adicional do serviço Texto
                livre: ENTREGA EXPRESSA; LOGÍSTICA REVERSA;
                CONVENCIONAL; EMERGENCIAL; etc
            :ivar xEmi: Funcionário emissor do CTe
            :ivar xObs: Observações Gerais
            :ivar obsCont: Campo de uso livre do contribuinte Informar o
                nome do campo no atributo xCampo e o conteúdo do campo
                no XTexto
            :ivar obsFisco: Campo de uso livre do contribuinte Informar
                o nome do campo no atributo xCampo e o conteúdo do campo
                no XTexto
            """
            xCaracAd: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            xCaracSer: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 30,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            xEmi: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            xObs: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            obsCont: List["TcteOs.InfCte.Compl.ObsCont"] = field(
                default_factory=list,
                metadata={
                    "name": "ObsCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_occurs": 10,
                }
            )
            obsFisco: List["TcteOs.InfCte.Compl.ObsFisco"] = field(
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
                :ivar xTexto: Conteúdo do campo
                :ivar xCampo: Identificação do campo
                """
                xTexto: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 160,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                xCampo: Optional[str] = field(
                    default=None,
                    metadata={
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
                :ivar xTexto: Conteúdo do campo
                :ivar xCampo: Identificação do campo
                """
                xTexto: Optional[str] = field(
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
                xCampo: Optional[str] = field(
                    default=None,
                    metadata={
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
            :ivar CNPJ: CNPJ do emitente Informar zeros não
                significativos
            :ivar IE: Inscrição Estadual do Emitente
            :ivar IEST: Inscrição Estadual do Substituto Tributário
            :ivar xNome: Razão social ou Nome do emitente
            :ivar xFant: Nome fantasia
            :ivar enderEmit: Endereço do emitente
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            IEST: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            enderEmit: Optional[TendeEmi] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )

        @dataclass
        class Toma:
            """
            :ivar CNPJ: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar CPF: Número do CPF Informar os zeros não
                significativos.
            :ivar IE: Inscrição Estadual Informar a IE do tomador ou
                ISENTO se tomador é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                tomador não seja contribuinte do ICMS não informar o
                conteúdo.
            :ivar xNome: Razão social ou nome do tomador
            :ivar xFant: Nome fantasia
            :ivar fone: Telefone
            :ivar enderToma: Dados do endereço
            :ivar email: Endereço de email
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
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
            enderToma: Optional[Tendereco] = field(
                default=None,
                metadata={
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
            :ivar vTPrest: Valor Total da Prestação do Serviço Pode
                conter zeros quando o CT-e for de complemento de ICMS
            :ivar vRec: Valor a Receber
            :ivar comp: Componentes do Valor da Prestação
            """
            vTPrest: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            vRec: Optional[str] = field(
                default=None,
                metadata={
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
                :ivar xNome: Nome do componente Exxemplos: FRETE PESO,
                    FRETE VALOR, SEC/CAT, ADEME, AGENDAMENTO, etc
                :ivar vComp: Valor do componente
                """
                xNome: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 15,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                vComp: Optional[str] = field(
                    default=None,
                    metadata={
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
            :ivar ICMS: Informações relativas ao ICMS
            :ivar vTotTrib: Valor Total dos Tributos
            :ivar infAdFisco: Informações adicionais de interesse do
                Fisco Norma referenciada, informações complementares,
                etc
            :ivar ICMSUFFim: Informações do ICMS de partilha com a UF de
                término do serviço de transporte na operação
                interestadual Grupo a ser informado nas prestações
                interestaduais para consumidor final, não contribuinte
                do ICMS
            :ivar infTribFed: Informações dos tributos federais Grupo a
                ser informado nas prestações interestaduais para
                consumidor final, não contribuinte do ICMS
            """
            ICMS: Optional[TimpOs] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            vTotTrib: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            infAdFisco: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ICMSUFFim: Optional["TcteOs.InfCte.Imp.Icmsuffim"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            infTribFed: Optional["TcteOs.InfCte.Imp.InfTribFed"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )

            @dataclass
            class Icmsuffim:
                """
                :ivar vBCUFFim: Valor da BC do ICMS na UF de término da
                    prestação do serviço de transporte
                :ivar pFCPUFFim: Percentual do ICMS relativo ao Fundo de
                    Combate à pobreza (FCP) na UF de término da
                    prestação do serviço de transporte Alíquota adotada
                    nas operações internas na UF do destinatário
                :ivar pICMSUFFim: Alíquota interna da UF de término da
                    prestação do serviço de transporte Alíquota adotada
                    nas operações internas na UF do destinatário
                :ivar pICMSInter: Alíquota interestadual das UF
                    envolvidas Alíquota interestadual das UF envolvidas
                :ivar vFCPUFFim: Valor do ICMS relativo ao Fundo de
                    Combate á Pobreza (FCP) da UF de término da
                    prestação
                :ivar vICMSUFFim: Valor do ICMS de partilha para a UF de
                    término da prestação do serviço de transporte
                :ivar vICMSUFIni: Valor do ICMS de partilha para a UF de
                    início da prestação do serviço de transporte
                """
                vBCUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                pFCPUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                pICMSUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                pICMSInter: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                vFCPUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vICMSUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vICMSUFIni: Optional[str] = field(
                    default=None,
                    metadata={
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
                :ivar vPIS: Valor do PIS
                :ivar vCOFINS: Valor COFINS
                :ivar vIR: Valor de Imposto de Renda
                :ivar vINSS: Valor do INSS
                :ivar vCSLL: Valor do CSLL
                """
                vPIS: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vCOFINS: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vIR: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vINSS: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vCSLL: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )

        @dataclass
        class InfCteNorm:
            """
            :ivar infServico: Informações da Prestação do Serviço
            :ivar infDocRef: Informações dos documentos referenciados
            :ivar seg: Informações de Seguro da Carga
            :ivar infModal: Informações do modal Obrigatório para
                Pessoas e Bagagem
            :ivar infCteSub: Informações do CT-e de substituição
            :ivar refCTeCanc: Chave de acesso do CT-e Cancelado Somente
                para Transporte de Valores
            :ivar cobr: Dados da cobrança do CT-e
            :ivar infGTVe: Informações das GTV-e relacionadas ao CT-e OS
            """
            infServico: Optional["TcteOs.InfCte.InfCteNorm.InfServico"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            infDocRef: List["TcteOs.InfCte.InfCteNorm.InfDocRef"] = field(
                default_factory=list,
                metadata={
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
            infModal: Optional["TcteOs.InfCte.InfCteNorm.InfModal"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            infCteSub: Optional["TcteOs.InfCte.InfCteNorm.InfCteSub"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            refCTeCanc: Optional[str] = field(
                default=None,
                metadata={
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
            infGTVe: List["TcteOs.InfCte.InfCteNorm.InfGtve"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )

            @dataclass
            class InfServico:
                """
                :ivar xDescServ: Descrição do Serviço prestado
                :ivar infQ: Informações de quantidades da Carga do CT-e
                    Para Transporte de Pessoas indicar número de
                    passageiros, para excesso de bagagem e transporte de
                    valores indicar número de Volumes/Malotes
                """
                xDescServ: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 30,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                infQ: Optional["TcteOs.InfCte.InfCteNorm.InfServico.InfQ"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )

                @dataclass
                class InfQ:
                    """
                    :ivar qCarga: Quantidade
                    """
                    qCarga: Optional[str] = field(
                        default=None,
                        metadata={
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
                :ivar nDoc: Número
                :ivar serie: Série
                :ivar subserie: Subsérie
                :ivar dEmi: Data de Emissão Formato AAAA-MM-DD
                :ivar vDoc: Valor Transportado
                :ivar chBPe: Chave de acesso do BP-e que possui eventos
                    excesso de bagagem
                """
                nDoc: Optional[str] = field(
                    default=None,
                    metadata={
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
                dEmi: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                    }
                )
                vDoc: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                chBPe: Optional[str] = field(
                    default=None,
                    metadata={
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
                :ivar respSeg: Responsável pelo seguro Preencher com: 4
                    - Emitente do CT-e; 5 - Tomador de Serviço.
                :ivar xSeg: Nome da Seguradora
                :ivar nApol: Número da Apólice Obrigatório pela lei
                    11.442/07 (RCTRC)
                """
                respSeg: Optional[SegRespSeg] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                xSeg: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 30,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                nApol: Optional[str] = field(
                    default=None,
                    metadata={
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
                :ivar versaoModal: Versão do leiaute específico para o
                    Modal
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
            class InfCteSub:
                """
                :ivar chCte: Chave de acesso do CT-e a ser substituído
                    (original)
                :ivar refCteAnu: Chave de acesso do CT-e de Anulação
                :ivar tomaICMS: Tomador é contribuinte do ICMS, mas não
                    é emitente de documento fiscal eletrônico
                """
                chCte: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "pattern": r"[0-9]{44}",
                    }
                )
                refCteAnu: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "max_length": 44,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{44}",
                    }
                )
                tomaICMS: Optional["TcteOs.InfCte.InfCteNorm.InfCteSub.TomaIcms"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )

                @dataclass
                class TomaIcms:
                    """
                    :ivar refNFe: Chave de acesso da NF-e emitida pelo
                        Tomador
                    :ivar refNF: Informação da NF ou CT emitido pelo
                        Tomador
                    :ivar refCte: Chave de acesso do CT-e emitido pelo
                        Tomador
                    """
                    refNFe: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "max_length": 44,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{44}",
                        }
                    )
                    refNF: Optional["TcteOs.InfCte.InfCteNorm.InfCteSub.TomaIcms.RefNf"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )
                    refCte: Optional[str] = field(
                        default=None,
                        metadata={
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
                        :ivar CNPJ: CNPJ do Emitente Informar o CNPJ do
                            emitente do Documento Fiscal
                        :ivar CPF: Número do CPF Informar o CPF do
                            emitente do documento fiscal
                        :ivar mod: Modelo do Documento Fiscal
                        :ivar serie: Serie do documento fiscal
                        :ivar subserie: Subserie do documento fiscal
                        :ivar nro: Número do documento fiscal
                        :ivar valor: Valor do documento fiscal.
                        :ivar dEmi: Data de emissão do documento fiscal.
                        """
                        CNPJ: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "white_space": "preserve",
                                "pattern": r"[0-9]{14}",
                            }
                        )
                        CPF: Optional[str] = field(
                            default=None,
                            metadata={
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
                        dEmi: Optional[str] = field(
                            default=None,
                            metadata={
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
                    :ivar nFat: Número da fatura
                    :ivar vOrig: Valor original da fatura
                    :ivar vDesc: Valor do desconto da fatura
                    :ivar vLiq: Valor líquido da fatura
                    """
                    nFat: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 60,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    vOrig: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vDesc: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vLiq: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )

                @dataclass
                class Dup:
                    """
                    :ivar nDup: Número da duplicata
                    :ivar dVenc: Data de vencimento da duplicata (AAAA-
                        MM-DD)
                    :ivar vDup: Valor da duplicata
                    """
                    nDup: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 60,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    dVenc: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    vDup: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )

            @dataclass
            class InfGtve:
                """
                :ivar chCTe: Chave de acesso da GTV-e
                :ivar comp: Componentes do Valor da GTVe
                """
                chCTe: Optional[str] = field(
                    default=None,
                    metadata={
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
                    :ivar tpComp: Tipo do Componente 1-Custodia
                        2-Embarque 3-Tempo de espera 4-Malote 5-Ad
                        Valorem 6-Outros
                    :ivar vComp: Valor do componente
                    :ivar xComp: Nome do componente (informar apenas
                        para outros) Exemplos: FRETE PESO, FRETE VALOR,
                        SEC/CAT, ADEME, AGENDAMENTO, etc
                    """
                    tpComp: Optional[CompTpComp] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    vComp: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    xComp: Optional[str] = field(
                        default=None,
                        metadata={
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
            :ivar chCTe: Chave do CT-e complementado
            """
            chCTe: Optional[str] = field(
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

        @dataclass
        class InfCteAnu:
            """
            :ivar chCte: Chave de acesso do CT-e original a ser anulado
                e substituído
            :ivar dEmi: Data de emissão da declaração do tomador não
                contribuinte do ICMS
            """
            chCte: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "pattern": r"[0-9]{44}",
                }
            )
            dEmi: Optional[str] = field(
                default=None,
                metadata={
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
        :ivar qrCodCTe: Texto com o QR-Code impresso no DACTE
        """
        qrCodCTe: Optional[str] = field(
            default=None,
            metadata={
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

    :ivar infCte: Informações do CT-e do tipo GTV-e
    :ivar infCTeSupl: Informações suplementares da GTV-e
    :ivar signature:
    :ivar versao: Versão do leiaute
    """
    class Meta:
        name = "TGTVe"

    infCte: Optional["Tgtve.InfCte"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    infCTeSupl: Optional["Tgtve.InfCteSupl"] = field(
        default=None,
        metadata={
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
        :ivar detGTV: Grupo de informações detalhadas da GTV-e
        :ivar autXML: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar infRespTec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar versao: Versão do leiaute Ex: "3.00"
        :ivar Id: Identificador da tag a ser assinada Informar a chave
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
        detGTV: Optional["Tgtve.InfCte.DetGtv"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        autXML: List["Tgtve.InfCte.AutXml"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "max_occurs": 10,
            }
        )
        infRespTec: Optional[TrespTec] = field(
            default=None,
            metadata={
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
        Id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"CTe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar cUF: Código da UF do emitente da GTV-e. Utilizar a
                Tabela do IBGE.
            :ivar cCT: Código numérico que compõe a Chave de Acesso.
                Número aleatório gerado pelo emitente para cada CT-e,
                com o objetivo de evitar acessos indevidos ao documento.
            :ivar CFOP: Código Fiscal de Operações e Prestações
            :ivar natOp: Natureza da Operação
            :ivar mod: Modelo do documento fiscal Utilizar o código 64
                para identificação do CT-e Guia de Transporte de Valores
            :ivar serie: Série da GTV-e Preencher com "0" no caso de
                série única
            :ivar nCT: Número da GTV-e
            :ivar dhEmi: Data e hora de emissão da GTV-e Formato AAAA-
                MM-DDTHH:MM:DD TZD
            :ivar tpImp: Formato de impressão do DACTE Preencher com: 1
                - Retrato; 2 - Paisagem.
            :ivar tpEmis: Forma de emissão da GTV-e Preencher com: 1 -
                Normal; 2- Contingencia offline 7 - Autorização pela
                SVC-RS; 8 - Autorização pela SVC-SP
            :ivar cDV: Digito Verificador da chave de acesso da GTV-e
                Informar o dígito  de controle da chave de acesso do
                CT-e, que deve ser calculado com a aplicação do
                algoritmo módulo 11 (base 2,9) da chave de acesso.
            :ivar tpAmb: Tipo do Ambiente Preencher com:1 - Produção; 2
                - Homologação
            :ivar tpCTe: Tipo da GTV-e Preencher com: 4 - GTV-e
            :ivar verProc: Versão do processo de emissão Iinformar a
                versão do aplicativo emissor de CT-e.
            :ivar cMunEnv: Código do Município de envio da GTV-e (de
                onde o documento foi transmitido) Utilizar a tabela do
                IBGE. Informar 9999999 para as operações com o exterior.
            :ivar xMunEnv: Nome do Município de envio da GTV-e (de onde
                o documento foi transmitido) Informar PAIS/Municipio
                para as operações com o exterior.
            :ivar UFEnv: Sigla da UF de envio da GTV-e (de onde o
                documento foi transmitido) Informar 'EX' para operações
                com o exterior.
            :ivar modal: Modal da GTV-e Preencher com: 01-Rodoviário
                06-Multimodal
            :ivar tpServ: Tipo do Serviço Preencher com: 9 - GTV
            :ivar indIEToma: Indicador da IE do tomador: 1 –
                Contribuinte ICMS; 2 – Contribuinte isento de inscrição;
                9 – Não Contribuinte Aplica-se ao tomador que for
                indicado no toma3 ou toma4
            :ivar dhSaidaOrig: Data e hora de saida da origem Formato
                AAAA-MM-DDTHH:MM:DD TZD
            :ivar dhChegadaDest: Data e hora de chegada no destino
                Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar toma: Indicador do "papel" do tomador do serviço no
                GT-e
            :ivar tomaTerceiro: Indicador do "papel" do tomador do
                serviço no CTV-e
            :ivar dhCont: Data e Hora da entrada em contingência
                Informar a data e hora no formato AAAA-MM-DDTHH:MM:SS
            :ivar xJust: Justificativa da entrada em contingência
            """
            cUF: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            cCT: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            CFOP: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[123567][0-9]([0-9][1-9]|[1-9][0-9])",
                }
            )
            natOp: Optional[str] = field(
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
            nCT: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            dhEmi: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tpImp: Optional[IdeTpImp] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tpEmis: Optional[IdeTpEmis] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            cDV: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
                }
            )
            tpAmb: Optional[Tamb] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            tpCTe: Optional[TfinGtve] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            verProc: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            cMunEnv: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            xMunEnv: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            UFEnv: Optional[Tuf] = field(
                default=None,
                metadata={
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
            tpServ: Optional[IdeTpServ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            indIEToma: Optional[IdeIndIetoma] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            dhSaidaOrig: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            dhChegadaDest: Optional[str] = field(
                default=None,
                metadata={
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
            tomaTerceiro: Optional["Tgtve.InfCte.Ide.TomaTerceiro"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            dhCont: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            xJust: Optional[str] = field(
                default=None,
                metadata={
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
                :ivar CNPJ: Número do CNPJ Em caso de empresa não
                    estabelecida no Brasil, será informado o CNPJ com
                    zeros. Informar os zeros não significativos.
                :ivar CPF: Número do CPF Informar os zeros não
                    significativos.
                :ivar IE: Inscrição Estadual Informar a IE do tomador ou
                    ISENTO se tomador é contribuinte do ICMS isento de
                    inscrição no cadastro de contribuintes do ICMS. Caso
                    o tomador não seja contribuinte do ICMS não informar
                    o conteúdo.
                :ivar xNome: Razão Social ou Nome
                :ivar xFant: Nome Fantasia
                :ivar fone: Telefone
                :ivar enderToma: Dados do endereço
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
                CNPJ: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{0}|[0-9]{14}",
                    }
                )
                CPF: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{11}",
                    }
                )
                IE: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "max_length": 14,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{0,14}|ISENTO",
                    }
                )
                xNome: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
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
                enderToma: Optional[Tendereco] = field(
                    default=None,
                    metadata={
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
            :ivar xCaracAd: Característica adicional do transporte Texto
                livre: REENTREGA; DEVOLUÇÃO; REFATURAMENTO; etc
            :ivar xCaracSer: Característica adicional do serviço Texto
                livre: ENTREGA EXPRESSA; LOGÍSTICA REVERSA;
                CONVENCIONAL; EMERGENCIAL; etc
            :ivar xEmi: Funcionário emissor da GTV-e
            :ivar xObs: Observações Gerais
            :ivar obsCont: Campo de uso livre do contribuinte Informar o
                nome do campo no atributo xCampo e o conteúdo do campo
                no XTexto
            :ivar obsFisco: Campo de uso livre do contribuinte Informar
                o nome do campo no atributo xCampo e o conteúdo do campo
                no XTexto
            """
            xCaracAd: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            xCaracSer: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 30,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            xEmi: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            xObs: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            obsCont: List["Tgtve.InfCte.Compl.ObsCont"] = field(
                default_factory=list,
                metadata={
                    "name": "ObsCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_occurs": 10,
                }
            )
            obsFisco: List["Tgtve.InfCte.Compl.ObsFisco"] = field(
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
                :ivar xTexto: Conteúdo do campo
                :ivar xCampo: Identificação do campo
                """
                xTexto: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 160,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                xCampo: Optional[str] = field(
                    default=None,
                    metadata={
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
                :ivar xTexto: Conteúdo do campo
                :ivar xCampo: Identificação do campo
                """
                xTexto: Optional[str] = field(
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
                xCampo: Optional[str] = field(
                    default=None,
                    metadata={
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
            :ivar CNPJ: CNPJ do emitente Informar zeros não
                significativos
            :ivar IE: Inscrição Estadual do Emitente
            :ivar IEST: Inscrição Estadual do Substituto Tributário
            :ivar xNome: Razão social ou Nome do emitente
            :ivar xFant: Nome fantasia
            :ivar enderEmit: Endereço do emitente
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            IEST: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            enderEmit: Optional[TendeEmi] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )

        @dataclass
        class Rem:
            """
            :ivar CNPJ: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar CPF: Número do CPF Informar os zeros não
                significativos.
            :ivar IE: Inscrição Estadual Informar a IE do remetente ou
                ISENTO se remetente é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                remetente não seja contribuinte do ICMS não informar a
                tag.
            :ivar xNome: Razão social ou nome do remetente
            :ivar xFant: Nome fantasia
            :ivar fone: Telefone
            :ivar enderReme: Dados do endereço
            :ivar email: Endereço de email
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
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
            enderReme: Optional[Tendereco] = field(
                default=None,
                metadata={
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
            :ivar CNPJ: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar CPF: Número do CPF Informar os zeros não
                significativos.
            :ivar IE: Inscrição Estadual Informar a IE do destinatário
                ou ISENTO se destinatário é contribuinte do ICMS isento
                de inscrição no cadastro de contribuintes do ICMS. Caso
                o destinatário não seja contribuinte do ICMS não
                informar o conteúdo.
            :ivar xNome: Razão Social ou Nome do destinatário
            :ivar fone: Telefone
            :ivar ISUF: Inscrição na SUFRAMA (Obrigatório nas operações
                com as áreas com benefícios de incentivos fiscais sob
                controle da SUFRAMA)
            :ivar enderDest: Dados do endereço
            :ivar email: Endereço de email
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
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
            ISUF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8,9}",
                }
            )
            enderDest: Optional[Tendereco] = field(
                default=None,
                metadata={
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
            :ivar infEspecie: Informações das Espécies transportadas
            :ivar qCarga: Quantidade de volumes/malotes
            :ivar infVeiculo: Grupo de informações dos veículos
                utilizados no transporte de valores
            """
            infEspecie: List["Tgtve.InfCte.DetGtv.InfEspecie"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_occurs": 1,
                }
            )
            qCarga: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                }
            )
            infVeiculo: List["Tgtve.InfCte.DetGtv.InfVeiculo"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class InfEspecie:
                """
                :ivar tpEspecie: Tipo da Espécie 1 - Cédula 2 - Cheque 3
                    - Moeda 4 - Outros
                :ivar vEspecie: Valor Transportada em Espécie indicada
                :ivar tpNumerario: Nacionalidade do Numerário 1 -
                    Nacional 2 - Estrangeiro
                :ivar xMoedaEstr: Nome da Moeda Informar somente se tipo
                    de numerário for 2 - Estrangeiro
                """
                tpEspecie: Optional[InfEspecieTpEspecie] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                vEspecie: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                tpNumerario: Optional[InfEspecieTpNumerario] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                xMoedaEstr: Optional[str] = field(
                    default=None,
                    metadata={
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
                :ivar UF: UF em que veículo está licenciado Sigla da UF
                    de licenciamento do veículo.
                :ivar RNTRC: RNTRC do transportador
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
                UF: Optional[Tuf] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                RNTRC: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{8}|ISENTO",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )

    @dataclass
    class InfCteSupl:
        """
        :ivar qrCodCTe: Texto com o QR-Code impresso no DACTE
        """
        qrCodCTe: Optional[str] = field(
            default=None,
            metadata={
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

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar cUF: Identificação da UF
    :ivar verAplic: Versão do Aplicativo que processou a CT-e
    :ivar cStat: código do status do retorno da consulta.
    :ivar xMotivo: Descrição literal do status do do retorno da
        consulta.
    :ivar protCTe: Reposta ao processamento do CT-e
    :ivar versao:
    """
    class Meta:
        name = "TRetCTe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    protCTe: Optional[TprotCte] = field(
        default=None,
        metadata={
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

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar cUF: Identificação da UF
    :ivar verAplic: Versão do Aplicativo que processou a CT-e
    :ivar cStat: código do status do retorno da consulta.
    :ivar xMotivo: Descrição literal do status do do retorno da
        consulta.
    :ivar protCTe: Reposta ao processamento do CT-e
    :ivar versao:
    """
    class Meta:
        name = "TRetCTeOS"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    protCTe: Optional[TprotCteOs] = field(
        default=None,
        metadata={
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

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar cUF: Identificação da UF
    :ivar verAplic: Versão do Aplicativo que processou a GTV-e
    :ivar cStat: código do status do retorno da consulta.
    :ivar xMotivo: Descrição literal do status do do retorno da
        consulta.
    :ivar protCTe: Reposta ao processamento do CT-e
    :ivar versao:
    """
    class Meta:
        name = "TRetGTVe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    protCTe: Optional[TprotGtve] = field(
        default=None,
        metadata={
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

    :ivar tpUnidTransp: Tipo da Unidade de Transporte 1 - Rodoviário
        Tração 2 - Rodoviário Reboque 3 - Navio 4 - Balsa 5 - Aeronave 6
        - Vagão 7 - Outros
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    idUnidTransp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    infUnidCarga: List[TunidCarga] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
        }
    )
    qtdRat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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

    :ivar infCte: Informações do CT-e
    :ivar infCTeSupl: Informações suplementares do CT-e
    :ivar signature:
    """
    class Meta:
        name = "TCTe"

    infCte: Optional["Tcte.InfCte"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    infCTeSupl: Optional["Tcte.InfCteSupl"] = field(
        default=None,
        metadata={
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
        :ivar vPrest: Valores da Prestação de Serviço
        :ivar imp: Informações relativas aos Impostos
        :ivar infCTeNorm: Grupo de informações do CT-e Normal e
            Substituto
        :ivar infCteComp: Detalhamento do CT-e complementado
        :ivar infCteAnu: Detalhamento do CT-e do tipo Anulação
        :ivar autXML: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar infRespTec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar infSolicNFF: Grupo de informações do pedido de emissão da
            Nota Fiscal Fácil
        :ivar versao: Versão do leiaute Ex: "3.00"
        :ivar Id: Identificador da tag a ser assinada Informar a chave
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
        vPrest: Optional["Tcte.InfCte.VPrest"] = field(
            default=None,
            metadata={
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
        infCTeNorm: Optional["Tcte.InfCte.InfCteNorm"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        infCteComp: Optional["Tcte.InfCte.InfCteComp"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        infCteAnu: Optional["Tcte.InfCte.InfCteAnu"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        autXML: List["Tcte.InfCte.AutXml"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "max_occurs": 10,
            }
        )
        infRespTec: Optional[TrespTec] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        infSolicNFF: Optional["Tcte.InfCte.InfSolicNff"] = field(
            default=None,
            metadata={
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
        Id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"CTe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar cUF: Código da UF do emitente do CT-e. Utilizar a
                Tabela do IBGE.
            :ivar cCT: Código numérico que compõe a Chave de Acesso.
                Número aleatório gerado pelo emitente para cada CT-e,
                com o objetivo de evitar acessos indevidos ao documento.
            :ivar CFOP: Código Fiscal de Operações e Prestações
            :ivar natOp: Natureza da Operação
            :ivar mod: Modelo do documento fiscal Utilizar o código 57
                para identificação do CT-e, emitido em substituição aos
                modelos de conhecimentos em papel.
            :ivar serie: Série do CT-e Preencher com "0" no caso de
                série única
            :ivar nCT: Número do CT-e
            :ivar dhEmi: Data e hora de emissão do CT-e Formato AAAA-MM-
                DDTHH:MM:DD TZD
            :ivar tpImp: Formato de impressão do DACTE Preencher com: 1
                - Retrato; 2 - Paisagem.
            :ivar tpEmis: Forma de emissão do CT-e Preencher com: 1 -
                Normal; 3-Regime Especial NFF;  4-EPEC pela SVC; 5 -
                Contingência FSDA; 7 - Autorização pela SVC-RS; 8 -
                Autorização pela SVC-SP
            :ivar cDV: Digito Verificador da chave de acesso do CT-e
                Informar o dígito  de controle da chave de acesso do
                CT-e, que deve ser calculado com a aplicação do
                algoritmo módulo 11 (base 2,9) da chave de acesso.
            :ivar tpAmb: Tipo do Ambiente Preencher com:1 - Produção; 2
                - Homologação.
            :ivar tpCTe: Tipo do CT-e Preencher com: 0 - CT-e Normal; 1
                - CT-e de Complemento de Valores;     2 - CT-e de
                Anulação; 3 - CT-e de Substituição
            :ivar procEmi: Identificador do processo de emissão do CT-e
                Preencher com: 0 - emissão de CT-e com aplicativo do
                contribuinte; 3- emissão CT-e pelo contribuinte com
                aplicativo fornecido pelo SEBRAE.
            :ivar verProc: Versão do processo de emissão Iinformar a
                versão do aplicativo emissor de CT-e.
            :ivar indGlobalizado: Indicador de CT-e Globalizado Informar
                valor 1 quando for Globalizado e não informar a tag
                quando não tratar de CT-e Globalizado
            :ivar cMunEnv: Código do Município de envio do CT-e (de onde
                o documento foi transmitido) Utilizar a tabela do IBGE.
                Informar 9999999 para as operações com o exterior.
            :ivar xMunEnv: Nome do Município de envio do CT-e (de onde o
                documento foi transmitido) Informar PAIS/Municipio para
                as operações com o exterior.
            :ivar UFEnv: Sigla da UF de envio do CT-e (de onde o
                documento foi transmitido) Informar 'EX' para operações
                com o exterior.
            :ivar modal: Modal Preencher com:01-Rodoviário;
                02-Aéreo;03-Aquaviário;04-Ferroviário;05-Dutoviário;06-Multimodal;
            :ivar tpServ: Tipo do Serviço Preencher com: 0 - Normal;1 -
                Subcontratação; 2 - Redespacho;3 - Redespacho
                Intermediário; 4 - Serviço Vinculado a Multimodal
            :ivar cMunIni: Código do Município de início da prestação
                Utilizar a tabela do IBGE. Informar 9999999 para
                operações com o exterior.
            :ivar xMunIni: Nome do Município do início da prestação
                Informar 'EXTERIOR' para operações com o exterior.
            :ivar UFIni: UF do início da prestação Informar 'EX' para
                operações com o exterior.
            :ivar cMunFim: Código do Município de término da prestação
                Utilizar a tabela do IBGE. Informar 9999999 para
                operações com o exterior.
            :ivar xMunFim: Nome do Município do término da prestação
                Informar 'EXTERIOR' para operações com o exterior.
            :ivar UFFim: UF do término da prestação Informar 'EX' para
                operações com o exterior.
            :ivar retira: Indicador se o Recebedor retira no Aeroporto,
                Filial, Porto ou Estação de Destino? Preencher com: 0 -
                sim; 1 - não
            :ivar xDetRetira: Detalhes do retira
            :ivar indIEToma: Indicador do papel do tomador na prestação
                do serviço: 1 – Contribuinte ICMS; 2 – Contribuinte
                isento de inscrição; 9 – Não Contribuinte Aplica-se ao
                tomador que for indicado no toma3 ou toma4
            :ivar toma3: Indicador do "papel" do tomador do serviço no
                CT-e
            :ivar toma4: Indicador do "papel" do tomador do serviço no
                CT-e
            :ivar dhCont: Data e Hora da entrada em contingência
                Informar a data e hora no formato AAAA-MM-DDTHH:MM:SS
            :ivar xJust: Justificativa da entrada em contingência
            """
            cUF: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            cCT: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            CFOP: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[123567][0-9]([0-9][1-9]|[1-9][0-9])",
                }
            )
            natOp: Optional[str] = field(
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
            nCT: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            dhEmi: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tpImp: Optional[IdeTpImp] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tpEmis: Optional[IdeTpEmis] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            cDV: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
                }
            )
            tpAmb: Optional[Tamb] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            tpCTe: Optional[TfinCte] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            procEmi: Optional[TprocEmi] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            verProc: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            indGlobalizado: Optional[IdeIndGlobalizado] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            cMunEnv: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            xMunEnv: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            UFEnv: Optional[Tuf] = field(
                default=None,
                metadata={
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
            tpServ: Optional[IdeTpServ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            cMunIni: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            xMunIni: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            UFIni: Optional[Tuf] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            cMunFim: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            xMunFim: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            UFFim: Optional[Tuf] = field(
                default=None,
                metadata={
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
            xDetRetira: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 160,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            indIEToma: Optional[IdeIndIetoma] = field(
                default=None,
                metadata={
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
            dhCont: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            xJust: Optional[str] = field(
                default=None,
                metadata={
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
                :ivar CNPJ: Número do CNPJ Em caso de empresa não
                    estabelecida no Brasil, será informado o CNPJ com
                    zeros. Informar os zeros não significativos.
                :ivar CPF: Número do CPF Informar os zeros não
                    significativos.
                :ivar IE: Inscrição Estadual Informar a IE do tomador ou
                    ISENTO se tomador é contribuinte do ICMS isento de
                    inscrição no cadastro de contribuintes do ICMS. Caso
                    o tomador não seja contribuinte do ICMS não informar
                    o conteúdo.
                :ivar xNome: Razão Social ou Nome
                :ivar xFant: Nome Fantasia
                :ivar fone: Telefone
                :ivar enderToma: Dados do endereço
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
                CNPJ: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{0}|[0-9]{14}",
                    }
                )
                CPF: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{11}",
                    }
                )
                IE: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "max_length": 14,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{0,14}|ISENTO",
                    }
                )
                xNome: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
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
                enderToma: Optional[Tendereco] = field(
                    default=None,
                    metadata={
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
            :ivar xCaracAd: Característica adicional do transporte Texto
                livre: REENTREGA; DEVOLUÇÃO; REFATURAMENTO; etc
            :ivar xCaracSer: Característica adicional do serviço Texto
                livre: ENTREGA EXPRESSA; LOGÍSTICA REVERSA;
                CONVENCIONAL; EMERGENCIAL; etc
            :ivar xEmi: Funcionário emissor do CTe
            :ivar fluxo: Previsão do fluxo da carga Preenchimento
                obrigatório para o modal aéreo.
            :ivar entrega: Informações ref. a previsão de entrega
            :ivar origCalc: Município de origem para efeito de cálculo
                do frete
            :ivar destCalc: Município de destino para efeito de cálculo
                do frete
            :ivar xObs: Observações Gerais
            :ivar obsCont: Campo de uso livre do contribuinte Informar o
                nome do campo no atributo xCampo e o conteúdo do campo
                no XTexto
            :ivar obsFisco: Campo de uso livre do contribuinte Informar
                o nome do campo no atributo xCampo e o conteúdo do campo
                no XTexto
            """
            xCaracAd: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            xCaracSer: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 30,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            xEmi: Optional[str] = field(
                default=None,
                metadata={
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
            origCalc: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 40,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            destCalc: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 40,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            xObs: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            obsCont: List["Tcte.InfCte.Compl.ObsCont"] = field(
                default_factory=list,
                metadata={
                    "name": "ObsCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_occurs": 10,
                }
            )
            obsFisco: List["Tcte.InfCte.Compl.ObsFisco"] = field(
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
                :ivar xOrig: Sigla ou código interno da
                    Filial/Porto/Estação/ Aeroporto de Origem
                    Observações para o modal aéreo: - Preenchimento
                    obrigatório para o modal aéreo. - O código de três
                    letras IATA do aeroporto de partida deverá ser
                    incluído como primeira anotação. Quando não for
                    possível, utilizar a sigla OACI.
                :ivar pass_value:
                :ivar xDest: Sigla ou código interno da
                    Filial/Porto/Estação/Aeroporto de Destino
                    Observações para o modal aéreo: - Preenchimento
                    obrigatório para o modal aéreo. - Deverá ser
                    incluído o código de três letras IATA do aeroporto
                    de destino. Quando não for possível, utilizar a
                    sigla OACI.
                :ivar xRota: Código da Rota de Entrega
                """
                xOrig: Optional[str] = field(
                    default=None,
                    metadata={
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
                xDest: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                xRota: Optional[str] = field(
                    default=None,
                    metadata={
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
                    :ivar xPass: Sigla ou código interno da
                        Filial/Porto/Estação/Aeroporto de Passagem
                        Observação para o modal aéreo: - O código de
                        três letras IATA, referente ao aeroporto de
                        transferência, deverá ser incluído, quando for o
                        caso. Quando não for possível,  utilizar a sigla
                        OACI. Qualquer solicitação de itinerário deverá
                        ser incluída.
                    """
                    xPass: Optional[str] = field(
                        default=None,
                        metadata={
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
                :ivar semData: Entrega sem data definida Esta opção é
                    proibida para o modal aéreo.
                :ivar comData: Entrega com data definida
                :ivar noPeriodo: Entrega no período definido
                :ivar semHora: Entrega sem hora definida
                :ivar comHora: Entrega com hora definida
                :ivar noInter: Entrega no intervalo de horário definido
                """
                semData: Optional["Tcte.InfCte.Compl.Entrega.SemData"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                comData: Optional["Tcte.InfCte.Compl.Entrega.ComData"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                noPeriodo: Optional["Tcte.InfCte.Compl.Entrega.NoPeriodo"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                semHora: Optional["Tcte.InfCte.Compl.Entrega.SemHora"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                comHora: Optional["Tcte.InfCte.Compl.Entrega.ComHora"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                noInter: Optional["Tcte.InfCte.Compl.Entrega.NoInter"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )

                @dataclass
                class SemData:
                    """
                    :ivar tpPer: Tipo de data/período programado para
                        entrega 0- Sem data definida
                    """
                    tpPer: Optional[SemDataTpPer] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )

                @dataclass
                class ComData:
                    """
                    :ivar tpPer: Tipo de data/período programado para
                        entrega Preencher com: 1-Na data; 2-Até a data;
                        3-A partir da data
                    :ivar dProg: Data programada Formato AAAA-MM-DD
                    """
                    tpPer: Optional[ComDataTpPer] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    dProg: Optional[str] = field(
                        default=None,
                        metadata={
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
                    :ivar tpPer: Tipo período 4-no período
                    :ivar dIni: Data inicial Formato AAAA-MM-DD
                    :ivar dFim: Data final Formato AAAA-MM-DD
                    """
                    tpPer: Optional[NoPeriodoTpPer] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    dIni: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    dFim: Optional[str] = field(
                        default=None,
                        metadata={
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
                    :ivar tpHor: Tipo de hora 0- Sem hora definida
                    """
                    tpHor: Optional[SemHoraTpHor] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )

                @dataclass
                class ComHora:
                    """
                    :ivar tpHor: Tipo de hora Preencher com: 1 - No
                        horário; 2 - Até o horário; 3 - A partir do
                        horário.
                    :ivar hProg: Hora programada Formato HH:MM:SS
                    """
                    tpHor: Optional[ComHoraTpHor] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    hProg: Optional[str] = field(
                        default=None,
                        metadata={
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
                    :ivar tpHor: Tipo de hora 4 - No intervalo de tempo
                    :ivar hIni: Hora inicial Formato HH:MM:SS
                    :ivar hFim: Hora final Formato HH:MM:SS
                    """
                    tpHor: Optional[NoInterTpHor] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    hIni: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])",
                        }
                    )
                    hFim: Optional[str] = field(
                        default=None,
                        metadata={
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
                :ivar xTexto: Conteúdo do campo
                :ivar xCampo: Identificação do campo
                """
                xTexto: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 160,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                xCampo: Optional[str] = field(
                    default=None,
                    metadata={
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
                :ivar xTexto: Conteúdo do campo
                :ivar xCampo: Identificação do campo
                """
                xTexto: Optional[str] = field(
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
                xCampo: Optional[str] = field(
                    default=None,
                    metadata={
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
            :ivar CNPJ: CNPJ do emitente Informar zeros não
                significativos
            :ivar CPF: CPF do emitente Informar zeros não
                significativos. Usar com série específica 920-969 para
                emitente pessoa física com inscrição estadual
            :ivar IE: Inscrição Estadual do Emitente A IE do emitente
                somente ficará sem informação para o caso do Regime
                Especial da NFF (tpEmis=3)
            :ivar IEST: Inscrição Estadual do Substituto Tributário
            :ivar xNome: Razão social ou Nome do emitente
            :ivar xFant: Nome fantasia
            :ivar enderEmit: Endereço do emitente
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            IEST: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
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
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            enderEmit: Optional[TendeEmi] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )

        @dataclass
        class Rem:
            """
            :ivar CNPJ: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar CPF: Número do CPF Informar os zeros não
                significativos.
            :ivar IE: Inscrição Estadual Informar a IE do remetente ou
                ISENTO se remetente é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                remetente não seja contribuinte do ICMS não informar a
                tag.
            :ivar xNome: Razão social ou nome do remetente
            :ivar xFant: Nome fantasia
            :ivar fone: Telefone
            :ivar enderReme: Dados do endereço
            :ivar email: Endereço de email
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
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
            enderReme: Optional[Tendereco] = field(
                default=None,
                metadata={
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
            :ivar CNPJ: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar CPF: Número do CPF Informar os zeros não
                significativos.
            :ivar IE: Inscrição Estadual Informar a IE do expedidor ou
                ISENTO se expedidor é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                expedidor não seja contribuinte do ICMS não informar a
                tag.
            :ivar xNome: Razão Social ou Nome
            :ivar fone: Telefone
            :ivar enderExped: Dados do endereço
            :ivar email: Endereço de email
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
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
            enderExped: Optional[Tendereco] = field(
                default=None,
                metadata={
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
            :ivar CNPJ: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar CPF: Número do CPF Informar os zeros não
                significativos.
            :ivar IE: Inscrição Estadual Informar a IE do recebedor ou
                ISENTO se recebedor é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                recebedor não seja contribuinte do ICMS não informar o
                conteúdo.
            :ivar xNome: Razão Social ou Nome
            :ivar fone: Telefone
            :ivar enderReceb: Dados do endereço
            :ivar email: Endereço de email
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
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
            enderReceb: Optional[Tendereco] = field(
                default=None,
                metadata={
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
            :ivar CNPJ: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar CPF: Número do CPF Informar os zeros não
                significativos.
            :ivar IE: Inscrição Estadual Informar a IE do destinatário
                ou ISENTO se destinatário é contribuinte do ICMS isento
                de inscrição no cadastro de contribuintes do ICMS. Caso
                o destinatário não seja contribuinte do ICMS não
                informar o conteúdo.
            :ivar xNome: Razão Social ou Nome do destinatário
            :ivar fone: Telefone
            :ivar ISUF: Inscrição na SUFRAMA (Obrigatório nas operações
                com as áreas com benefícios de incentivos fiscais sob
                controle da SUFRAMA)
            :ivar enderDest: Dados do endereço
            :ivar email: Endereço de email
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
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
            ISUF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8,9}",
                }
            )
            enderDest: Optional[Tendereco] = field(
                default=None,
                metadata={
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
            :ivar vTPrest: Valor Total da Prestação do Serviço Pode
                conter zeros quando o CT-e for de complemento de ICMS
            :ivar vRec: Valor a Receber
            :ivar comp: Componentes do Valor da Prestação
            """
            vTPrest: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            vRec: Optional[str] = field(
                default=None,
                metadata={
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
                :ivar xNome: Nome do componente Exxemplos: FRETE PESO,
                    FRETE VALOR, SEC/CAT, ADEME, AGENDAMENTO, etc
                :ivar vComp: Valor do componente
                """
                xNome: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 15,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                vComp: Optional[str] = field(
                    default=None,
                    metadata={
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
            :ivar ICMS: Informações relativas ao ICMS
            :ivar vTotTrib: Valor Total dos Tributos
            :ivar infAdFisco: Informações adicionais de interesse do
                Fisco Norma referenciada, informações complementares,
                etc
            :ivar ICMSUFFim: Informações do ICMS de partilha com a UF de
                término do serviço de transporte na operação
                interestadual Grupo a ser informado nas prestações
                interestaduais para consumidor final, não contribuinte
                do ICMS
            """
            ICMS: Optional[Timp] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            vTotTrib: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            infAdFisco: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ICMSUFFim: Optional["Tcte.InfCte.Imp.Icmsuffim"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )

            @dataclass
            class Icmsuffim:
                """
                :ivar vBCUFFim: Valor da BC do ICMS na UF de término da
                    prestação do serviço de transporte
                :ivar pFCPUFFim: Percentual do ICMS relativo ao Fundo de
                    Combate à pobreza (FCP) na UF de término da
                    prestação do serviço de transporte Alíquota adotada
                    nas operações internas na UF do destinatário
                :ivar pICMSUFFim: Alíquota interna da UF de término da
                    prestação do serviço de transporte Alíquota adotada
                    nas operações internas na UF do destinatário
                :ivar pICMSInter: Alíquota interestadual das UF
                    envolvidas Alíquota interestadual das UF envolvidas
                :ivar vFCPUFFim: Valor do ICMS relativo ao Fundo de
                    Combate á Pobreza (FCP) da UF de término da
                    prestação
                :ivar vICMSUFFim: Valor do ICMS de partilha para a UF de
                    término da prestação do serviço de transporte
                :ivar vICMSUFIni: Valor do ICMS de partilha para a UF de
                    início da prestação do serviço de transporte
                """
                vBCUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                pFCPUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                pICMSUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                pICMSInter: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                vFCPUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vICMSUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vICMSUFIni: Optional[str] = field(
                    default=None,
                    metadata={
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
            :ivar CNPJ: CNPJ do autorizado Informar zeros não
                significativos
            :ivar CPF: CPF do autorizado Informar zeros não
                significativos
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
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
            :ivar infCarga: Informações da Carga do CT-e
            :ivar infDoc: Informações dos documentos transportados pelo
                CT-e Opcional para Redespacho Intermediario e Serviço
                vinculado a multimodal. Poderá não ser informado para os
                CT-e de redespacho intermediário e serviço vinculado a
                multimodal. Nos demais casos deverá sempre ser
                informado.
            :ivar docAnt: Documentos de Transporte Anterior
            :ivar infModal: Informações do modal
            :ivar veicNovos: informações dos veículos transportados
            :ivar cobr: Dados da cobrança do CT-e
            :ivar infCteSub: Informações do CT-e de substituição
            :ivar infGlobalizado: Informações do CT-e Globalizado
            :ivar infServVinc: Informações do Serviço Vinculado a
                Multimodal
            """
            infCarga: Optional["Tcte.InfCte.InfCteNorm.InfCarga"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            infDoc: Optional["Tcte.InfCte.InfCteNorm.InfDoc"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            docAnt: Optional["Tcte.InfCte.InfCteNorm.DocAnt"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            infModal: Optional["Tcte.InfCte.InfCteNorm.InfModal"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                }
            )
            veicNovos: List["Tcte.InfCte.InfCteNorm.VeicNovos"] = field(
                default_factory=list,
                metadata={
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
            infCteSub: Optional["Tcte.InfCte.InfCteNorm.InfCteSub"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            infGlobalizado: Optional["Tcte.InfCte.InfCteNorm.InfGlobalizado"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )
            infServVinc: Optional["Tcte.InfCte.InfCteNorm.InfServVinc"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                }
            )

            @dataclass
            class InfCarga:
                """
                :ivar vCarga: Valor total da carga Dever ser informado
                    para todos os modais, com exceção para o Dutoviário.
                :ivar proPred: Produto predominante Informar a descrição
                    do produto predominante
                :ivar xOutCat: Outras características da carga "FRIA",
                    "GRANEL", "REFRIGERADA", "Medidas: 12X12X12"
                :ivar infQ: Informações de quantidades da Carga do CT-e
                    Para o Aéreo é obrigatório o preenchimento desse
                    campo da seguinte forma. 1 - Peso Bruto, sempre em
                    quilogramas (obrigatório); 2 - Peso Cubado; sempre
                    em quilogramas; 3 - Quantidade de volumes, sempre em
                    unidades (obrigatório); 4 - Cubagem, sempre em
                    metros cúbicos (obrigatório apenas quando for
                    impossível preencher as dimensões da(s)
                    embalagem(ens) na tag xDime do leiaute do Aéreo).
                :ivar vCargaAverb: Valor da Carga para efeito de
                    averbação Normalmente igual ao valor declarado da
                    mercadoria, diferente por exemplo, quando a
                    mercadoria transportada é isenta de tributos
                    nacionais para exportação, onde é preciso averbar um
                    valor maior, pois no caso de indenização, o valor a
                    ser pago será maior
                """
                vCarga: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                proPred: Optional[str] = field(
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
                xOutCat: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_length": 1,
                        "max_length": 30,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                infQ: List["Tcte.InfCte.InfCteNorm.InfCarga.InfQ"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_occurs": 1,
                    }
                )
                vCargaAverb: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

                @dataclass
                class InfQ:
                    """
                    :ivar cUnid: Código da Unidade de Medida Preencher
                        com: 00-M3; 01-KG; 02-TON; 03-UNIDADE;
                        04-LITROS; 05-MMBTU
                    :ivar tpMed: Tipo da Medida Exemplos: PESO BRUTO,
                        PESO DECLARADO, PESO CUBADO, PESO AFORADO, PESO
                        AFERIDO, PESO BASE DE CÁLCULO, LITRAGEM, CAIXAS
                        e etc
                    :ivar qCarga: Quantidade
                    """
                    cUnid: Optional[InfQCUnid] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    tpMed: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "min_length": 1,
                            "max_length": 20,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    qCarga: Optional[str] = field(
                        default=None,
                        metadata={
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
                :ivar infNF: Informações das NF Este grupo deve ser
                    informado quando o documento originário for NF
                :ivar infNFe: Informações das NF-e
                :ivar infOutros: Informações dos demais documentos
                """
                infNF: List["Tcte.InfCte.InfCteNorm.InfDoc.InfNf"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                infNFe: List["Tcte.InfCte.InfCteNorm.InfDoc.InfNfe"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                infOutros: List["Tcte.InfCte.InfCteNorm.InfDoc.InfOutros"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )

                @dataclass
                class InfNf:
                    """
                    :ivar nRoma: Número do Romaneio da NF
                    :ivar nPed: Número do Pedido da NF
                    :ivar mod: Modelo da Nota Fiscal Preencher com: 01 -
                        NF Modelo 01/1A e Avulsa; 04 - NF de Produtor
                    :ivar serie: Série
                    :ivar nDoc: Número
                    :ivar dEmi: Data de Emissão Formato AAAA-MM-DD
                    :ivar vBC: Valor da Base de Cálculo do ICMS
                    :ivar vICMS: Valor Total do ICMS
                    :ivar vBCST: Valor da Base de Cálculo do ICMS ST
                    :ivar vST: Valor Total do ICMS ST
                    :ivar vProd: Valor Total dos Produtos
                    :ivar vNF: Valor Total da NF
                    :ivar nCFOP: CFOP Predominante CFOP da NF ou, na
                        existência de mais de um, predominância pelo
                        critério de valor econômico.
                    :ivar nPeso: Peso total em Kg
                    :ivar PIN: PIN SUFRAMA PIN atribuído pela SUFRAMA
                        para a operação.
                    :ivar dPrev: Data prevista de entrega Formato AAAA-
                        MM-DD
                    :ivar infUnidCarga: Informações das Unidades de
                        Carga (Containeres/ULD/Outros) Dispositivo de
                        carga utilizada (Unit Load Device - ULD)
                        significa todo tipo de contêiner de carga,
                        vagão, contêiner de avião, palete de aeronave
                        com rede ou palete de aeronave com rede sobre um
                        iglu.
                    :ivar infUnidTransp: Informações das Unidades de
                        Transporte (Carreta/Reboque/Vagão) Deve ser
                        preenchido com as informações das unidades de
                        transporte utilizadas.
                    """
                    nRoma: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 20,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    nPed: Optional[str] = field(
                        default=None,
                        metadata={
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
                    nDoc: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
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
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    vBC: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vICMS: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vBCST: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vST: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vProd: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vNF: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    nCFOP: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[123567][0-9]([0-9][1-9]|[1-9][0-9])",
                        }
                    )
                    nPeso: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[1-9]{1}[0-9]{2}|0\.[0-9]{2}[1-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?",
                        }
                    )
                    PIN: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 2,
                            "max_length": 9,
                            "white_space": "preserve",
                            "pattern": r"[1-9]{1}[0-9]{1,8}",
                        }
                    )
                    dPrev: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    infUnidCarga: List[TunidCarga] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )
                    infUnidTransp: List[TunidadeTransp] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )

                @dataclass
                class InfNfe:
                    """
                    :ivar chave: Chave de acesso da NF-e
                    :ivar PIN: PIN SUFRAMA PIN atribuído pela SUFRAMA
                        para a operação.
                    :ivar dPrev: Data prevista de entrega Formato AAAA-
                        MM-DD
                    :ivar infUnidCarga: Informações das Unidades de
                        Carga (Containeres/ULD/Outros) Dispositivo de
                        carga utilizada (Unit Load Device - ULD)
                        significa todo tipo de contêiner de carga,
                        vagão, contêiner de avião, palete de aeronave
                        com rede ou palete de aeronave com rede sobre um
                        iglu.
                    :ivar infUnidTransp: Informações das Unidades de
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
                    PIN: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 2,
                            "max_length": 9,
                            "white_space": "preserve",
                            "pattern": r"[1-9]{1}[0-9]{1,8}",
                        }
                    )
                    dPrev: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    infUnidCarga: List[TunidCarga] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )
                    infUnidTransp: List[TunidadeTransp] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )

                @dataclass
                class InfOutros:
                    """
                    :ivar tpDoc: Tipo de documento originário Preencher
                        com: 00 - Declaração; 10 - Dutoviário; 59 - CF-e
                        SAT; 65 - NFC-e; 99 - Outros
                    :ivar descOutros: Descrição do documento
                    :ivar nDoc: Número
                    :ivar dEmi: Data de Emissão Formato AAAA-MM-DD
                    :ivar vDocFisc: Valor do documento
                    :ivar dPrev: Data prevista de entrega Formato AAAA-
                        MM-DD
                    :ivar infUnidCarga: Informações das Unidades de
                        Carga (Containeres/ULD/Outros) Dispositivo de
                        carga utilizada (Unit Load Device - ULD)
                        significa todo tipo de contêiner de carga,
                        vagão, contêiner de avião, palete de aeronave
                        com rede ou palete de aeronave com rede sobre um
                        iglu.
                    :ivar infUnidTransp: Informações das Unidades de
                        Transporte (Carreta/Reboque/Vagão) Deve ser
                        preenchido com as informações das unidades de
                        transporte utilizadas.
                    """
                    tpDoc: Optional[InfOutrosTpDoc] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    descOutros: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 100,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    nDoc: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
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
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    vDocFisc: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    dPrev: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    infUnidCarga: List[TunidCarga] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )
                    infUnidTransp: List[TunidadeTransp] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )

            @dataclass
            class DocAnt:
                """
                :ivar emiDocAnt: Emissor do documento anterior
                """
                emiDocAnt: List["Tcte.InfCte.InfCteNorm.DocAnt.EmiDocAnt"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_occurs": 1,
                    }
                )

                @dataclass
                class EmiDocAnt:
                    """
                    :ivar CNPJ: Número do CNPJ Em caso de empresa não
                        estabelecida no Brasil, será informado o CNPJ
                        com zeros. Informar os zeros não significativos.
                    :ivar CPF: Número do CPF Informar os zeros não
                        significativos.
                    :ivar IE: Inscrição Estadual
                    :ivar UF: Sigla da UF Informar EX para operações com
                        o exterior.
                    :ivar xNome: Razão Social ou Nome do expedidor
                    :ivar idDocAnt: Informações de identificação dos
                        documentos de Transporte Anterior
                    """
                    CNPJ: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{0}|[0-9]{14}",
                        }
                    )
                    CPF: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{11}",
                        }
                    )
                    IE: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "max_length": 14,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{2,14}",
                        }
                    )
                    UF: Optional[Tuf] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )
                    xNome: Optional[str] = field(
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
                    idDocAnt: List["Tcte.InfCte.InfCteNorm.DocAnt.EmiDocAnt.IdDocAnt"] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_occurs": 1,
                            "max_occurs": 2,
                        }
                    )

                    @dataclass
                    class IdDocAnt:
                        """
                        :ivar idDocAntPap: Documentos de transporte
                            anterior em papel
                        :ivar idDocAntEle: Documentos de transporte
                            anterior eletrônicos
                        """
                        idDocAntPap: List["Tcte.InfCte.InfCteNorm.DocAnt.EmiDocAnt.IdDocAnt.IdDocAntPap"] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                            }
                        )
                        idDocAntEle: List["Tcte.InfCte.InfCteNorm.DocAnt.EmiDocAnt.IdDocAnt.IdDocAntEle"] = field(
                            default_factory=list,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                            }
                        )

                        @dataclass
                        class IdDocAntPap:
                            """
                            :ivar tpDoc: Tipo do Documento de Transporte
                                Anterior Preencher com: 07-ATRE; 08-DTA
                                (Despacho de Transito Aduaneiro);
                                09-Conhecimento Aéreo Internacional; 10
                                – Conhecimento - Carta de Porte
                                Internacional; 11 – Conhecimento Avulso;
                                12-TIF (Transporte Internacional
                                Ferroviário); 13-BL (Bill of Lading)
                            :ivar serie: Série do Documento Fiscal
                            :ivar subser: Série do Documento Fiscal
                            :ivar nDoc: Número do Documento Fiscal
                            :ivar dEmi: Data de emissão (AAAA-MM-DD)
                            """
                            tpDoc: Optional[TdocAssoc] = field(
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
                            nDoc: Optional[str] = field(
                                default=None,
                                metadata={
                                    "type": "Element",
                                    "namespace": "http://www.portalfiscal.inf.br/cte",
                                    "required": True,
                                    "min_length": 1,
                                    "max_length": 30,
                                    "white_space": "preserve",
                                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                                }
                            )
                            dEmi: Optional[str] = field(
                                default=None,
                                metadata={
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
                            :ivar chCTe: Chave de acesso do CT-e
                            """
                            chCTe: Optional[str] = field(
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
                :ivar versaoModal: Versão do leiaute específico para o
                    Modal
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
            class VeicNovos:
                """
                :ivar chassi: Chassi do veículo
                :ivar cCor: Cor do veículo Código de cada montadora
                :ivar xCor: Descrição da cor
                :ivar cMod: Código Marca Modelo Utilizar tabela RENAVAM
                :ivar vUnit: Valor Unitário do Veículo
                :ivar vFrete: Frete Unitário
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
                cCor: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 4,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                xCor: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 40,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                cMod: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "min_length": 1,
                        "max_length": 6,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                vUnit: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vFrete: Optional[str] = field(
                    default=None,
                    metadata={
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
                    :ivar nFat: Número da fatura
                    :ivar vOrig: Valor original da fatura
                    :ivar vDesc: Valor do desconto da fatura
                    :ivar vLiq: Valor líquido da fatura
                    """
                    nFat: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 60,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    vOrig: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vDesc: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vLiq: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )

                @dataclass
                class Dup:
                    """
                    :ivar nDup: Número da duplicata
                    :ivar dVenc: Data de vencimento da duplicata (AAAA-
                        MM-DD)
                    :ivar vDup: Valor da duplicata
                    """
                    nDup: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "min_length": 1,
                            "max_length": 60,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    dVenc: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    vDup: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )

            @dataclass
            class InfCteSub:
                """
                :ivar chCte: Chave de acesso do CT-e a ser substituído
                    (original)
                :ivar refCteAnu: Chave de acesso do CT-e de Anulação
                :ivar tomaICMS: Tomador é contribuinte do ICMS, mas não
                    é emitente de documento fiscal eletrônico
                :ivar indAlteraToma: Indicador de CT-e Alteração de
                    Tomador
                """
                chCte: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "required": True,
                        "pattern": r"[0-9]{44}",
                    }
                )
                refCteAnu: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "max_length": 44,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{44}",
                    }
                )
                tomaICMS: Optional["Tcte.InfCte.InfCteNorm.InfCteSub.TomaIcms"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )
                indAlteraToma: Optional[InfCteSubIndAlteraToma] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                    }
                )

                @dataclass
                class TomaIcms:
                    """
                    :ivar refNFe: Chave de acesso da NF-e emitida pelo
                        Tomador
                    :ivar refNF: Informação da NF ou CT emitido pelo
                        Tomador
                    :ivar refCte: Chave de acesso do CT-e emitido pelo
                        Tomador
                    """
                    refNFe: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                            "max_length": 44,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{44}",
                        }
                    )
                    refNF: Optional["Tcte.InfCte.InfCteNorm.InfCteSub.TomaIcms.RefNf"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/cte",
                        }
                    )
                    refCte: Optional[str] = field(
                        default=None,
                        metadata={
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
                        :ivar CNPJ: CNPJ do Emitente Informar o CNPJ do
                            emitente do Documento Fiscal
                        :ivar CPF: Número do CPF Informar o CPF do
                            emitente do documento fiscal
                        :ivar mod: Modelo do Documento Fiscal
                        :ivar serie: Serie do documento fiscal
                        :ivar subserie: Subserie do documento fiscal
                        :ivar nro: Número do documento fiscal
                        :ivar valor: Valor do documento fiscal.
                        :ivar dEmi: Data de emissão do documento fiscal.
                        """
                        CNPJ: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/cte",
                                "white_space": "preserve",
                                "pattern": r"[0-9]{14}",
                            }
                        )
                        CPF: Optional[str] = field(
                            default=None,
                            metadata={
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
                        dEmi: Optional[str] = field(
                            default=None,
                            metadata={
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
                :ivar xObs: Preencher com informações adicionais,
                    legislação do regime especial, etc
                """
                xObs: Optional[str] = field(
                    default=None,
                    metadata={
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
                :ivar infCTeMultimodal: informações do CT-e multimodal
                    vinculado
                """
                infCTeMultimodal: List["Tcte.InfCte.InfCteNorm.InfServVinc.InfCteMultimodal"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/cte",
                        "min_occurs": 1,
                    }
                )

                @dataclass
                class InfCteMultimodal:
                    """
                    :ivar chCTeMultimodal: Chave de acesso do CT-e
                        Multimodal
                    """
                    chCTeMultimodal: Optional[str] = field(
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

        @dataclass
        class InfCteComp:
            """
            :ivar chCTe: Chave do CT-e complementado
            """
            chCTe: Optional[str] = field(
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

        @dataclass
        class InfCteAnu:
            """
            :ivar chCte: Chave de acesso do CT-e original a ser anulado
                e substituído
            :ivar dEmi: Data de emissão da declaração do tomador não
                contribuinte do ICMS
            """
            chCte: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/cte",
                    "required": True,
                    "pattern": r"[0-9]{44}",
                }
            )
            dEmi: Optional[str] = field(
                default=None,
                metadata={
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
        :ivar qrCodCTe: Texto com o QR-Code impresso no DACTE
        """
        qrCodCTe: Optional[str] = field(
            default=None,
            metadata={
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

    idLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,15}",
        }
    )
    CTe: List[Tcte] = field(
        default_factory=list,
        metadata={
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
