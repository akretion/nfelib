from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bindings.bpe.v1_0.tipos_geral_bpe_v1_00 import (
    Tamb,
    TcodUfIbge,
    TmodBpe,
    Tuf,
    TufSemEx,
)
from nfelib.bindings.bpe.v1_0.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/bpe"


class CompTpComp(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_99 = "99"


class Icms00Cst(Enum):
    VALUE_00 = "00"


class Icms20Cst(Enum):
    VALUE_20 = "20"


class Icms45Cst(Enum):
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_51 = "51"


class Icms90Cst(Enum):
    VALUE_90 = "90"


class IcmssnCst(Enum):
    VALUE_90 = "90"


class IcmssnIndSn(Enum):
    VALUE_1 = "1"


class Tdoc(Enum):
    """
    Tipo de Documento de Identificação.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


class TindPres(Enum):
    """
    Tipo de Indicador de Presença.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_9 = "9"


class Tmodal(Enum):
    """
    Tipo Modal do BP-e.
    """
    VALUE_1 = "1"
    VALUE_3 = "3"
    VALUE_4 = "4"


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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "pattern": r"[0-9]{3}",
        }
    )
    hash_csrt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "hashCSRT",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "length": 20,
            "format": "base64",
        }
    )


class TtipoBpe(Enum):
    """
    Tipo de BP-e.
    """
    VALUE_0 = "0"
    VALUE_3 = "3"


class TtipoBpeTm(Enum):
    """
    Tipo de BP-e Transporte Metropolitano.
    """
    VALUE_4 = "4"


class TtipoSubstituicao(Enum):
    """
    Tipo de Substituição.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class CardTBand(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_99 = "99"


class CardTpIntegra(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


class EmitCrt(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class IdeTpEmis(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


class InfTravessiaSitVeiculo(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class InfTravessiaTpVeiculo(Enum):
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
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"
    VALUE_27 = "27"
    VALUE_28 = "28"
    VALUE_29 = "29"
    VALUE_99 = "99"


class InfValorBpeTpDesconto(Enum):
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
    VALUE_99 = "99"


class InfViagemTpAcomodacao(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


class InfViagemTpServ(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"
    VALUE_9 = "9"
    VALUE_10 = "10"
    VALUE_11 = "11"


class InfViagemTpTrecho(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class InfViagemTpViagem(Enum):
    VALUE_00 = "00"
    VALUE_01 = "01"


class PagTPag(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_99 = "99"


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
    :ivar email: Endereço de E-mail
    """
    class Meta:
        name = "TEndeEmi"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: Optional[TufSemEx] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "white_space": "preserve",
            "pattern": r"[0-9]{7,12}",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[^@]+@[^\.]+\..+",
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
    :ivar fone: Telefone
    :ivar email: Endereço de E-mail
    """
    class Meta:
        name = "TEndereco"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    c_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "cPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    x_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "xPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "white_space": "preserve",
            "pattern": r"[0-9]{7,12}",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[^@]+@[^\.]+\..+",
        }
    )


@dataclass
class Timp:
    """
    Tipo Dados do Imposto BP-e.

    :ivar icms00: Prestação sujeito à tributação normal do ICMS
    :ivar icms20: Prestação sujeito à tributação com redução de BC do
        ICMS
    :ivar icms45: ICMS  Isento, não Tributado ou diferido
    :ivar icms90: ICMS Outros
    :ivar icmssn: Simples Nacional
    """
    class Meta:
        name = "TImp"

    icms00: Optional["Timp.Icms00"] = field(
        default=None,
        metadata={
            "name": "ICMS00",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
        }
    )
    icms20: Optional["Timp.Icms20"] = field(
        default=None,
        metadata={
            "name": "ICMS20",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
        }
    )
    icms45: Optional["Timp.Icms45"] = field(
        default=None,
        metadata={
            "name": "ICMS45",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
        }
    )
    icms90: Optional["Timp.Icms90"] = field(
        default=None,
        metadata={
            "name": "ICMS90",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
        }
    )
    icmssn: Optional["Timp.Icmssn"] = field(
        default=None,
        metadata={
            "name": "ICMSSN",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
            }
        )
        v_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "vBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
            }
        )
        p_red_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "pRedBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
            }
        )
        p_red_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "pRedBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        v_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "vBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
            }
        )
        ind_sn: Optional[IcmssnIndSn] = field(
            default=None,
            metadata={
                "name": "indSN",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
            }
        )


@dataclass
class TprotBpe:
    """
    Tipo Protocolo de status resultado do processamento do BP-e (Modelo 63)

    :ivar inf_prot: Dados do protocolo de status
    :ivar inf_fisco: Mensagem do Fisco
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TProtBPe"

    inf_prot: Optional["TprotBpe.InfProt"] = field(
        default=None,
        metadata={
            "name": "infProt",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    inf_fisco: Optional["TprotBpe.InfFisco"] = field(
        default=None,
        metadata={
            "name": "infFisco",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
    class InfProt:
        """
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar ver_aplic: Versão do Aplicativo que processou o BP-e
        :ivar ch_bpe: Chave de acesso do BP-e
        :ivar dh_recbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS TZD.
        :ivar n_prot: Número do Protocolo de Status do BP-e.
        :ivar dig_val: Digest Value do BP-e processado. Utilizado para
            conferir a integridade do BP-e original.
        :ivar c_stat: Código do status do BP-e.
        :ivar x_motivo: Descrição literal do status do BP-e.
        :ivar id:
        """
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
            }
        )
        ver_aplic: Optional[str] = field(
            default=None,
            metadata={
                "name": "verAplic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        ch_bpe: Optional[str] = field(
            default=None,
            metadata={
                "name": "chBPe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        dig_val: Optional[bytes] = field(
            default=None,
            metadata={
                "name": "digVal",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "format": "base64",
            }
        )
        c_stat: Optional[str] = field(
            default=None,
            metadata={
                "name": "cStat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )


@dataclass
class Tbpe:
    """
    Tipo Bilhete de Passagem Eletrônico.

    :ivar inf_bpe: Informações do BP-e
    :ivar inf_bpe_supl: Informações suplementares do BP-e
    :ivar signature:
    """
    class Meta:
        name = "TBPe"

    inf_bpe: Optional["Tbpe.InfBpe"] = field(
        default=None,
        metadata={
            "name": "infBPe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    inf_bpe_supl: Optional["Tbpe.InfBpeSupl"] = field(
        default=None,
        metadata={
            "name": "infBPeSupl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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

    @dataclass
    class InfBpe:
        """
        :ivar ide: Identificação do BP-e
        :ivar emit: Identificação do Emitente do BP-e
        :ivar comp: Identificação do Comprador do BP-e
        :ivar agencia: Identificação da agência/preposto/terceiro que
            comercializou o BP-e
        :ivar inf_bpe_sub: Informações dos BP-e de Substituição para
            remarcação e/ou transferência
        :ivar inf_passagem: Informações do detalhamento da Passagem
        :ivar inf_viagem: Grupo de informações da viagem do BP-e
        :ivar inf_valor_bpe: Informações dos valores do Bilhete de
            Passagem
        :ivar imp: Informações relativas aos Impostos
        :ivar pag: Dados de Pagamento.
        :ivar aut_xml: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar inf_adic: Informações Adicionais
        :ivar inf_resp_tec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar versao: Versão do leiaute Ex: "3.00"
        :ivar id: Identificador da tag a ser assinada Informar a chave
            de acesso do BP-e e precedida do literal "BPe"
        """
        ide: Optional["Tbpe.InfBpe.Ide"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
            }
        )
        emit: Optional["Tbpe.InfBpe.Emit"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
            }
        )
        comp: Optional["Tbpe.InfBpe.Comp"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
            }
        )
        agencia: Optional["Tbpe.InfBpe.Agencia"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
            }
        )
        inf_bpe_sub: Optional["Tbpe.InfBpe.InfBpeSub"] = field(
            default=None,
            metadata={
                "name": "infBPeSub",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
            }
        )
        inf_passagem: Optional["Tbpe.InfBpe.InfPassagem"] = field(
            default=None,
            metadata={
                "name": "infPassagem",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
            }
        )
        inf_viagem: List["Tbpe.InfBpe.InfViagem"] = field(
            default_factory=list,
            metadata={
                "name": "infViagem",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "min_occurs": 1,
            }
        )
        inf_valor_bpe: Optional["Tbpe.InfBpe.InfValorBpe"] = field(
            default=None,
            metadata={
                "name": "infValorBPe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
            }
        )
        imp: Optional["Tbpe.InfBpe.Imp"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
            }
        )
        pag: List["Tbpe.InfBpe.Pag"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "min_occurs": 1,
                "max_occurs": 10,
            }
        )
        aut_xml: List["Tbpe.InfBpe.AutXml"] = field(
            default_factory=list,
            metadata={
                "name": "autXML",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "max_occurs": 10,
            }
        )
        inf_adic: Optional["Tbpe.InfBpe.InfAdic"] = field(
            default=None,
            metadata={
                "name": "infAdic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
            }
        )
        inf_resp_tec: Optional[TrespTec] = field(
            default=None,
            metadata={
                "name": "infRespTec",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "required": True,
                "pattern": r"BPe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar c_uf: Código da UF do emitente do BP-e Código da UF do
                emitente do Documento Fiscal. Utilizar a Tabela do IBGE
                de código de unidades da federação.
            :ivar tp_amb: Tipo do Ambiente 1 - Produção 2 - Homologação
            :ivar mod: Modelo do Bilhete de Passagem Utilizar o código
                63 para identificação do BP-e
            :ivar serie: Série do documento fiscal Informar a série do
                documento fiscal (informar zero se inexistente).
            :ivar n_bp: Número do bilhete de passagem Número que
                identifica o bilhete 1 a 999999999.
            :ivar c_bp: Código numérico que compõe a Chave de Acesso.
                Código aleatório gerado pelo emitente, com o objetivo de
                evitar acessos indevidos ao documento.
            :ivar c_dv: Digito verificador da chave de acesso Informar o
                dígito  de controle da chave de acesso do BP-e, que deve
                ser calculado com a aplicação do algoritmo módulo 11
                (base 2,9) da chave de acesso.
            :ivar modal: Modalidade de transporte 1 - Rodoviário; 3 -
                Aquaviário; 4 - Ferroviário.
            :ivar dh_emi: Data e hora de emissão do Bilhete de Passagem
                Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar tp_emis: Forma de emissão do Bilhete (Normal ou
                Contingência Off-Line) 1 - Normal ; 2 - Contingência
                Off-Line
            :ivar ver_proc: Versão do processo de emissão Informar a
                versão do aplicativo emissor de BP-e.
            :ivar tp_bpe: Tipo do BP-e 0 - BP-e normal 3 - BP-e
                substituição
            :ivar ind_pres: Indicador de presença do comprador no
                estabelecimento comercial no momento da operação
                1=Operação presencial não embarcado; 2=Operação não
                presencial, pela Internet; 3=Operação não presencial,
                Teleatendimento; 4=BP-e em operação com entrega a
                domicílio; 5=Operação presencial embarcada; 9=Operação
                não presencial, outros.
            :ivar ufini: Sigla da UF Início da Viagem Utilizar a Tabela
                do IBGE de código de unidades da federação
            :ivar c_mun_ini: Código do município do início da viagem
            :ivar uffim: Sigla da UF do Fim da Viagem Utilizar a Tabela
                do IBGE de código de unidades da federação. Informar
                'EX' para operações com o exterior.
            :ivar c_mun_fim: Código do município do fim da viagem
            :ivar dh_cont: Data e Hora da entrada em contingência
                Informar a data e hora no formato AAAA-MM-DDTHH:MM:SS
            :ivar x_just: Justificativa da entrada em contingência
            """
            c_uf: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "name": "cUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            tp_amb: Optional[Tamb] = field(
                default=None,
                metadata={
                    "name": "tpAmb",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            mod: Optional[TmodBpe] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            serie: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                }
            )
            n_bp: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nBP",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            c_bp: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cBP",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
                }
            )
            modal: Optional[Tmodal] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            dh_emi: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            ver_proc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "verProc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            tp_bpe: Optional[TtipoBpe] = field(
                default=None,
                metadata={
                    "name": "tpBPe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            ind_pres: Optional[TindPres] = field(
                default=None,
                metadata={
                    "name": "indPres",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            ufini: Optional[TufSemEx] = field(
                default=None,
                metadata={
                    "name": "UFIni",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            c_mun_ini: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cMunIni",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            uffim: Optional[Tuf] = field(
                default=None,
                metadata={
                    "name": "UFFim",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            c_mun_fim: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cMunFim",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            dh_cont: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            x_just: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xJust",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 15,
                    "max_length": 256,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )

        @dataclass
        class Emit:
            """
            :ivar cnpj: CNPJ do emitente Informar zeros não
                significativos
            :ivar ie: Inscrição Estadual do emitente
            :ivar iest: Inscrição Estadual do Substituto Tributário
            :ivar x_nome: Razão social ou Nome do emitente
            :ivar x_fant: Nome fantasia do emitente
            :ivar im: Inscrição Municipal
            :ivar cnae: CNAE Fiscal
            :ivar crt: Código de Regime Tributário. Este campo será
                obrigatoriamente preenchido com: 1 – Simples Nacional; 2
                – Simples Nacional – excesso de sublimite de receita
                bruta; 3 – Regime Normal.
            :ivar ender_emit: Endereço do emitente
            :ivar tar: Termo de Autorização de Serviço Regular Registro
                obrigatório do emitente do BP-e junto à ANTT para
                exercer a atividade
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            iest: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IEST",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            im: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IM",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            cnae: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNAE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            crt: Optional[EmitCrt] = field(
                default=None,
                metadata={
                    "name": "CRT",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            ender_emit: Optional[TendeEmi] = field(
                default=None,
                metadata={
                    "name": "enderEmit",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            tar: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TAR",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                }
            )

        @dataclass
        class Comp:
            """
            :ivar x_nome: Razão social ou Nome do comprador
            :ivar cnpj: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar cpf: Número do CPF Informar os zeros não
                significativos.
            :ivar id_estrangeiro: Identificador do comprador em caso de
                comprador estrangeiro
            :ivar ie: Inscrição Estadual Informar a IE do remetente ou
                ISENTO se remetente é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                remetente não seja contribuinte do ICMS não informar a
                tag.
            :ivar ender_comp: Endereço do comprador
            """
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            id_estrangeiro: Optional[str] = field(
                default=None,
                metadata={
                    "name": "idEstrangeiro",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"([!-ÿ]{0}|[!-ÿ]{5,20})?",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO|PR[0-9]{4,8}",
                }
            )
            ender_comp: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "name": "enderComp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )

        @dataclass
        class Agencia:
            """
            :ivar x_nome: Razão social ou Nome da Agência
            :ivar cnpj: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar ender_agencia: Endereço da agência
            """
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            ender_agencia: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "name": "enderAgencia",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )

        @dataclass
        class InfBpeSub:
            """
            :ivar ch_bpe: Chave do Bilhete de Passagem Substituido
                Informar os zeros não significativos.
            :ivar tp_sub: Tipo de Substituição 1 - Remarcação 2 -
                Transferência 3 - Transferência e Remarcação
            """
            ch_bpe: Optional[str] = field(
                default=None,
                metadata={
                    "name": "chBPe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "max_length": 44,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{44}",
                }
            )
            tp_sub: Optional[TtipoSubstituicao] = field(
                default=None,
                metadata={
                    "name": "tpSub",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )

        @dataclass
        class InfPassagem:
            """
            :ivar c_loc_orig: Código da Localidade de Origem
            :ivar x_loc_orig: Descrição da Localidade de Origem
            :ivar c_loc_dest:
            :ivar x_loc_dest: Descrição da Localidade de Destino
            :ivar dh_emb: Data e hora de embarque Formato AAAA-MM-
                DDTHH:MM:DD TZD
            :ivar dh_validade: Data e hora de validade do bilhete
                Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar inf_passageiro: Informações do passageiro
            """
            c_loc_orig: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cLocOrig",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 7,
                    "white_space": "preserve",
                }
            )
            x_loc_orig: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xLocOrig",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            c_loc_dest: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cLocDest",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 7,
                    "white_space": "preserve",
                }
            )
            x_loc_dest: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xLocDest",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            dh_emb: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhEmb",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            dh_validade: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhValidade",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            inf_passageiro: Optional["Tbpe.InfBpe.InfPassagem.InfPassageiro"] = field(
                default=None,
                metadata={
                    "name": "infPassageiro",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                }
            )

            @dataclass
            class InfPassageiro:
                """
                :ivar x_nome: Nome do Passageiro
                :ivar cpf: Número do CPF Informar os zeros não
                    significativos.
                :ivar tp_doc: Tipo do Documento de identificação 1-RG
                    2-Título de Eleitor 3-Passaporte 4-CNH 5-Outros
                :ivar n_doc: Número do Documento do passageiro
                :ivar x_doc: Descrição do tipo de documento "outros"
                :ivar d_nasc: Data de Nascimento Formato AAAA-MM-DD
                :ivar fone: Telefone
                :ivar email: Endereço de E-mail
                """
                x_nome: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xNome",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                cpf: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CPF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{11}",
                    }
                )
                tp_doc: Optional[Tdoc] = field(
                    default=None,
                    metadata={
                        "name": "tpDoc",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                    }
                )
                n_doc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nDoc",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "min_length": 2,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                x_doc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xDoc",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 2,
                        "max_length": 100,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                d_nasc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "dNasc",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "white_space": "preserve",
                        "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                    }
                )
                fone: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7,12}",
                    }
                )
                email: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[^@]+@[^\.]+\..+",
                    }
                )

        @dataclass
        class InfViagem:
            """
            :ivar c_percurso: Código do percurso da viagem
            :ivar x_percurso: Descrição do Percurso da viagem
            :ivar tp_viagem: Tipo de Viagem Informa o código do tipo da
                viagem (00-regular, 01-extra)
            :ivar tp_serv: Tipo de Serviço Informar o código do tipo de
                serviço (1-Convencional com sanitário, 2-Convencional
                sem sanitário, 3-Semileito, 4-Leito com ar condicionado,
                5-Leito sem ar condicionado, 6-Executivo, 7-Semiurbano,
                8-Longitudinal, 9-Travessia, 10-Cama, 11-Micro-onibus)
            :ivar tp_acomodacao: Tipo de Acomodação Informar o código do
                tipo de acomodação (1-Assento/poltrona, 2-Rede, 3-Rede
                com ar-condicionado, 4-Cabine, 5-Outros)
            :ivar tp_trecho: Tipo de trecho da viagem Informar do tipo
                de trecho (1-Normal, 2-Trecho Inicial, 3-Conexão)
            :ivar dh_viagem: Data e hora de referencia para a viagem
                Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar dh_conexao: Data e hora da conexão Informar se
                tpTrecho = 3 Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar prefixo: Prefixo da linha
            :ivar poltrona: Número da Poltrona / assento / cabine
            :ivar plataforma: Plataforma/carro/barco de Embarque
            :ivar inf_travessia: Informações do transporte aquaviário de
                travessia
            """
            c_percurso: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cPercurso",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                }
            )
            x_percurso: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xPercurso",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 100,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            tp_viagem: Optional[InfViagemTpViagem] = field(
                default=None,
                metadata={
                    "name": "tpViagem",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tp_serv: Optional[InfViagemTpServ] = field(
                default=None,
                metadata={
                    "name": "tpServ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tp_acomodacao: Optional[InfViagemTpAcomodacao] = field(
                default=None,
                metadata={
                    "name": "tpAcomodacao",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tp_trecho: Optional[InfViagemTpTrecho] = field(
                default=None,
                metadata={
                    "name": "tpTrecho",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            dh_viagem: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhViagem",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            dh_conexao: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhConexao",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            prefixo: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                }
            )
            poltrona: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 3,
                    "white_space": "preserve",
                    "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                }
            )
            plataforma: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 10,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            inf_travessia: Optional["Tbpe.InfBpe.InfViagem.InfTravessia"] = field(
                default=None,
                metadata={
                    "name": "infTravessia",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                }
            )

            @dataclass
            class InfTravessia:
                """
                :ivar tp_veiculo: Tipo do veículo transportado
                    01-Motocicleta 02-Automóvel 03-Automóvel com reboque
                    04-Caminhonete 05-Caminhonete com reboque 06-Micro-
                    onibus 07-Van 08-Ônibus - 2 ou 3 eixos 09-Ônibus 4
                    eixos 10-Caminhão 3/4 11-Caminhão toco 12-Caminhão
                    Truck 13-Carreta 14-Bi-Trem 15-Rodo-Trem - 9 eixos
                    16-Romeu e Julieta - 7 eixos 17-Jamanta - 6 eixos
                    18-Jamanta - 5 eixos 19-Jamanta - 4 eixos 20-Trator
                    de esteira 21-Pá mecânica 22-Patrol 23-Trator de
                    Pneu Grande 24-Trator de Pneu com reboque 25-Trator
                    de Pneu sem reboque 26-Carroça 27-Mobilete
                    28-Bicicleta 29-Passageiro 99-Outros
                :ivar sit_veiculo: Situação do veículo transportado 01 -
                    Vazio; 02 - Carregado; 03 - Não se aplica
                """
                tp_veiculo: Optional[InfTravessiaTpVeiculo] = field(
                    default=None,
                    metadata={
                        "name": "tpVeiculo",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                sit_veiculo: Optional[InfTravessiaSitVeiculo] = field(
                    default=None,
                    metadata={
                        "name": "sitVeiculo",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                    }
                )

        @dataclass
        class InfValorBpe:
            """
            :ivar v_bp: Valor do Bilhete de Passagem Pode conter zeros
                quando o BP-e for de complemento de ICMS
            :ivar v_desconto: Valor do desconto concedido ao comprador
                Indicar o valor total concedido em função dos benefícios
                concedidos ou política de desconto da empresa Informar
                0.00 em caso de passagem comercializada sem nenhum
                desconto
            :ivar v_pgto: Valor pago pelo BP-e (vBP - vDesconto)
            :ivar v_troco: Valor do troco
            :ivar tp_desconto: Tipo de desconto/benefício para o BP-e 01
                - Tarifa promocional 02 - Idoso 03 - Criança 04 -
                Deficiente 05 - Estudante 06 - Animal Doméstico 07 -
                Acordo Coletivo 08 - Profissional em Deslocamento 09 -
                Profissional da Empresa 10 - Jovem 99 - Outros
            :ivar x_desconto: Descrição do tipo de desconto/benefício
                concedido
            :ivar c_desconto: Código do desconto quando informado com
                tipo 99 - Outros
            :ivar comp: Componentes do Valor do Bilhete
            """
            v_bp: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vBP",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_desconto: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vDesconto",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_pgto: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vPgto",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_troco: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vTroco",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            tp_desconto: Optional[InfValorBpeTpDesconto] = field(
                default=None,
                metadata={
                    "name": "tpDesconto",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                }
            )
            x_desconto: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xDesconto",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 2,
                    "max_length": 100,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            c_desconto: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cDesconto",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 2,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            comp: List["Tbpe.InfBpe.InfValorBpe.Comp"] = field(
                default_factory=list,
                metadata={
                    "name": "Comp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_occurs": 1,
                }
            )

            @dataclass
            class Comp:
                """
                :ivar tp_comp: Tipo do Componente 01 - TARIFA; 02 -
                    PEDÁGIO; 03 - TAXA EMBARQUE; 04 - SEGURO; 05-TAXA DE
                    MANUTENÇÃO RODOVIA (TMR); 06 - SERVIÇO DE VENDA
                    INTEGRADA (SVI); 99 - OUTROS
                :ivar v_comp: Valor do componente
                """
                tp_comp: Optional[CompTpComp] = field(
                    default=None,
                    metadata={
                        "name": "tpComp",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                v_comp: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vComp",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            v_tot_trib: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vTotTrib",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            inf_ad_fisco: Optional[str] = field(
                default=None,
                metadata={
                    "name": "infAdFisco",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            icmsuffim: Optional["Tbpe.InfBpe.Imp.Icmsuffim"] = field(
                default=None,
                metadata={
                    "name": "ICMSUFFim",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                }
            )

            @dataclass
            class Icmsuffim:
                """
                :ivar v_bcuffim: Valor da BC do ICMS na UF fim da viagem
                :ivar p_fcpuffim: Percentual do ICMS relativo ao Fundo
                    de Combate à pobreza (FCP) na UF fim da viagem
                    Alíquota adotada nas operações internas na UF do
                    destinatário
                :ivar p_icmsuffim: Alíquota interna da UF fim da viagem
                    Alíquota adotada nas operações internas na UF do
                    destinatário
                :ivar p_icmsinter: Alíquota interestadual das UF
                    envolvidas Alíquota interestadual das UF envolvidas
                :ivar v_fcpuffim: Valor do ICMS relativo ao Fundo de
                    Combate á Pobreza (FCP) da UF fim da viagem
                :ivar v_icmsuffim: Valor do ICMS de partilha para a UF
                    fim da viagem
                :ivar v_icmsufini: Valor do ICMS de partilha para a UF
                    início da viagem
                """
                v_bcuffim: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vBCUFFim",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

        @dataclass
        class Pag:
            """
            :ivar t_pag: Forma de
                Pagamento:01-Dinheiro;02-Cheque;03-Cartão de
                Crédito;04-Cartão de Débito;05-Vale Transportel;06 -
                PIX; 99 - Outros
            :ivar x_pag: Descrição da forma de pagamento 99 - Outros
            :ivar n_doc_pag: Número do documento ou carteira apresentada
                nas formas de pagamento diferentes de 03 e 04
            :ivar v_pag: Valor do Pagamento
            :ivar card: Grupo de Cartões
            """
            t_pag: Optional[PagTPag] = field(
                default=None,
                metadata={
                    "name": "tPag",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            x_pag: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xPag",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 2,
                    "max_length": 100,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            n_doc_pag: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nDocPag",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 2,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            v_pag: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vPag",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            card: Optional["Tbpe.InfBpe.Pag.Card"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                }
            )

            @dataclass
            class Card:
                """
                :ivar tp_integra: Tipo de Integração do processo de
                    pagamento com o sistema de automação da empresa
                    1=Pagamento integrado com o sistema de automação da
                    empresa Ex. equipamento TEF , Comercio Eletronico
                    2=Pagamento não integrado com o sistema de automação
                    da empresa Ex: equipamento POS
                :ivar cnpj: CNPJ da credenciadora de cartão de
                    crédito/débito
                :ivar t_band: Bandeira da operadora de cartão de
                    crédito/débito 01–Visa; 02–Mastercard; 03–American
                    Express; 04–Sorocred; 05 - Elo; 06 - Diners;
                    99–Outros
                :ivar x_band: Descrição da operador de cartão para 99 -
                    Outros
                :ivar c_aut: Número de autorização da operação cartão de
                    crédito/débito
                :ivar nsu_trans: Número sequencial único da transação
                :ivar nsu_host: Número sequencial único do Host
                :ivar n_parcelas: Número de parcelas
                :ivar inf_ad_card: Informações adicionais operacionais
                    para integração do cartão de crédito Norma
                    referenciada, informações complementares, etc
                """
                tp_integra: Optional[CardTpIntegra] = field(
                    default=None,
                    metadata={
                        "name": "tpIntegra",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                cnpj: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CNPJ",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{14}",
                    }
                )
                t_band: Optional[CardTBand] = field(
                    default=None,
                    metadata={
                        "name": "tBand",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "white_space": "preserve",
                    }
                )
                x_band: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xBand",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 2,
                        "max_length": 100,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                c_aut: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cAut",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                nsu_trans: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nsuTrans",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                nsu_host: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nsuHost",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                n_parcelas: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nParcelas",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 3,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{3}",
                    }
                )
                inf_ad_card: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "infAdCard",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 2000,
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 5000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )

    @dataclass
    class InfBpeSupl:
        """
        :ivar qr_cod_bpe: Texto com o QR-Code impresso no DABPE
        :ivar board_pass_bpe: Texto contendo o boarding Pass impresso no
            DABPE (padrão PDF417) O boarding Pass poderá ser gerado no
            padrão PDF417 e impresso no DABPE opcionalmente pelo
            emitente para colocar informações operacionais do bilhete
            e/ou prestar informações para a agência reguladora do setor
        """
        qr_cod_bpe: Optional[str] = field(
            default=None,
            metadata={
                "name": "qrCodBPe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "min_length": 50,
                "max_length": 1000,
                "white_space": "preserve",
                "pattern": r"((HTTPS?|https?)://.*\?chBPe=[0-9]{44}&tpAmb=[1-2](&sign=[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})?)",
            }
        )
        board_pass_bpe: Optional[str] = field(
            default=None,
            metadata={
                "name": "boardPassBPe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "min_length": 50,
                "max_length": 1000,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )


@dataclass
class TbpeTm:
    """
    Tipo Bilhete de Passagem Eletrônico Transporte Metropolitano.

    :ivar inf_bpe: Informações do BPeTM
    :ivar signature:
    """
    class Meta:
        name = "TBPeTM"

    inf_bpe: Optional["TbpeTm.InfBpe"] = field(
        default=None,
        metadata={
            "name": "infBPe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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

    @dataclass
    class InfBpe:
        """
        :ivar ide: Identificação do BPe TM
        :ivar emit: Identificação do Emitente do BPe TM
        :ivar det_bpe_tm: Grupo de informações detalhadas do BPe TM
        :ivar total: Informações dos totais do BPe TM
        :ivar aut_xml: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar inf_adic: Informações Adicionais
        :ivar inf_resp_tec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar versao: Versão do leiaute Ex: "3.00"
        :ivar id: Identificador da tag a ser assinada Informar a chave
            de acesso do BP-e e precedida do literal "BPe"
        """
        ide: Optional["TbpeTm.InfBpe.Ide"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
            }
        )
        emit: Optional["TbpeTm.InfBpe.Emit"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
            }
        )
        det_bpe_tm: List["TbpeTm.InfBpe.DetBpeTm"] = field(
            default_factory=list,
            metadata={
                "name": "detBPeTM",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "min_occurs": 1,
                "max_occurs": 99,
            }
        )
        total: Optional["TbpeTm.InfBpe.Total"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
            }
        )
        aut_xml: List["TbpeTm.InfBpe.AutXml"] = field(
            default_factory=list,
            metadata={
                "name": "autXML",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "max_occurs": 10,
            }
        )
        inf_adic: Optional["TbpeTm.InfBpe.InfAdic"] = field(
            default=None,
            metadata={
                "name": "infAdic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
            }
        )
        inf_resp_tec: Optional[TrespTec] = field(
            default=None,
            metadata={
                "name": "infRespTec",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "required": True,
                "pattern": r"BPe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar c_uf: Código da UF do emitente do BP-e Código da UF do
                emitente do Documento Fiscal. Utilizar a Tabela do IBGE
                de código de unidades da federação.
            :ivar tp_amb: Tipo do Ambiente 1 - Produção 2 - Homologação
            :ivar mod: Modelo do Bilhete de Passagem Utilizar o código
                63 para identificação do BP-e
            :ivar serie: Série do documento fiscal Informar a série do
                documento fiscal (informar zero se inexistente).
            :ivar n_bp: Número do bilhete de passagem Número que
                identifica o bilhete 1 a 999999999.
            :ivar c_bp: Código numérico que compõe a Chave de Acesso.
                Código aleatório gerado pelo emitente, com o objetivo de
                evitar acessos indevidos ao documento.
            :ivar c_dv: Digito verificador da chave de acesso Informar o
                dígito  de controle da chave de acesso do BP-e, que deve
                ser calculado com a aplicação do algoritmo módulo 11
                (base 2,9) da chave de acesso.
            :ivar modal: Modalidade de transporte 1 - Rodoviário; 3 -
                Aquaviário; 4 - Ferroviário.
            :ivar dh_emi: Data e hora de emissão do Bilhete de Passagem
                Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar d_compet: Data da Competência a que se refere o
                Transporte Metropolitano Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar tp_emis: Forma de emissão do Bilhete (Normal ou
                Contingência Off-Line) 1 - Normal ; 2 - Contingência
                Off-Line
            :ivar ver_proc: Versão do processo de emissão Informar a
                versão do aplicativo emissor de BP-e.
            :ivar tp_bpe: Tipo do BP-e 4 - BP-e Transporte Metropolitano
            :ivar cfop: Código Fiscal de Operações e Prestações
            :ivar dh_cont: Data e Hora da entrada em contingência
                Informar a data e hora no formato AAAA-MM-DDTHH:MM:SS
            :ivar x_just: Justificativa da entrada em contingência
            """
            c_uf: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "name": "cUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            tp_amb: Optional[Tamb] = field(
                default=None,
                metadata={
                    "name": "tpAmb",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            mod: Optional[TmodBpe] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            serie: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                }
            )
            n_bp: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nBP",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            c_bp: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cBP",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
                }
            )
            modal: Optional[Tmodal] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            dh_emi: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            d_compet: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dCompet",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            tp_emis: Optional[IdeTpEmis] = field(
                default=None,
                metadata={
                    "name": "tpEmis",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            ver_proc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "verProc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            tp_bpe: Optional[TtipoBpeTm] = field(
                default=None,
                metadata={
                    "name": "tpBPe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            cfop: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CFOP",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[123567][0-9]([0-9][1-9]|[1-9][0-9])",
                }
            )
            dh_cont: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            x_just: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xJust",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 15,
                    "max_length": 256,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )

        @dataclass
        class Emit:
            """
            :ivar cnpj: CNPJ do emitente Informar zeros não
                significativos
            :ivar ie: Inscrição Estadual do emitente
            :ivar iest: Inscrição Estadual do Substituto Tributário
            :ivar x_nome: Razão social ou Nome do emitente
            :ivar x_fant: Nome fantasia do emitente
            :ivar im: Inscrição Municipal
            :ivar cnae: CNAE Fiscal
            :ivar crt: Código de Regime Tributário. Este campo será
                obrigatoriamente preenchido com: 1 – Simples Nacional; 2
                – Simples Nacional – excesso de sublimite de receita
                bruta; 3 – Regime Normal.
            :ivar ender_emit: Endereço do emitente
            :ivar tar: Termo de Autorização de Serviço Regular Registro
                obrigatório do emitente do BP-e junto à ANTT para
                exercer a atividade
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            iest: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IEST",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            im: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IM",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            cnae: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNAE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            crt: Optional[EmitCrt] = field(
                default=None,
                metadata={
                    "name": "CRT",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            ender_emit: Optional[TendeEmi] = field(
                default=None,
                metadata={
                    "name": "enderEmit",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            tar: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TAR",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                }
            )

        @dataclass
        class DetBpeTm:
            """
            :ivar ufini_viagem: Sigla da UF início da Viagem Utilizar a
                Tabela do IBGE de código de unidades da federação
            :ivar uffim_viagem: Sigla da UF fim da Viagem Utilizar a
                Tabela do IBGE de código de unidades da federação
            :ivar placa: Placa do coletivo
            :ivar prefixo: Prefixo da linha
            :ivar det: Datalhamento da viagem por trechos do BPeTM
            :ivar id_eqp_cont: Identificador do equipamento contador
            """
            ufini_viagem: Optional[TufSemEx] = field(
                default=None,
                metadata={
                    "name": "UFIniViagem",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            uffim_viagem: Optional[TufSemEx] = field(
                default=None,
                metadata={
                    "name": "UFFimViagem",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                }
            )
            placa: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[A-Z]{2,3}[0-9]{4}|[A-Z]{3,4}[0-9]{3}|[A-Z0-9]{7}",
                }
            )
            prefixo: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                }
            )
            det: List["TbpeTm.InfBpe.DetBpeTm.Det"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_occurs": 1,
                    "max_occurs": 990,
                }
            )
            id_eqp_cont: Optional[str] = field(
                default=None,
                metadata={
                    "name": "idEqpCont",
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,1}|[1-8]{1}[0-9]{2}|[9]{1}[0-8]{1}[0-9]{1}|[9]{1}[9]{1}[0]{1}",
                }
            )

            @dataclass
            class Det:
                """
                :ivar c_mun_ini: Código do município do início da viagem
                :ivar c_mun_fim: Código do município do fim da viagem
                :ivar n_cont_inicio: Contador início da viagem
                :ivar n_cont_fim: Contador fim da viagem
                :ivar q_pass: Quantidade de Passagens da viagem
                :ivar v_bp: Valor da soma dos Bilhetes de Passagem da
                    viagem Pode conter zeros quando o BP-e for de
                    complemento de ICMS
                :ivar imp: Informações relativas aos Impostos
                :ivar comp: Componentes da viagem
                :ivar n_viagem:
                """
                c_mun_ini: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cMunIni",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7}",
                    }
                )
                c_mun_fim: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cMunFim",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7}",
                    }
                )
                n_cont_inicio: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nContInicio",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                    }
                )
                n_cont_fim: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nContFim",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                    }
                )
                q_pass: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "qPass",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                    }
                )
                v_bp: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vBP",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                imp: Optional["TbpeTm.InfBpe.DetBpeTm.Det.Imp"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                    }
                )
                comp: List["TbpeTm.InfBpe.DetBpeTm.Det.Comp"] = field(
                    default_factory=list,
                    metadata={
                        "name": "Comp",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_occurs": 1,
                    }
                )
                n_viagem: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nViagem",
                        "type": "Attribute",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[1-9]{1}[0-9]{0,1}|[1-8]{1}[0-9]{2}|[9]{1}[0-8]{1}[0-9]{1}|[9]{1}[9]{1}[0]{1}",
                    }
                )

                @dataclass
                class Imp:
                    """
                    :ivar icms: Informações relativas ao ICMS
                    :ivar inf_ad_fisco: Informações adicionais de
                        interesse do Fisco Norma referenciada,
                        informações complementares, etc
                    """
                    icms: Optional[Timp] = field(
                        default=None,
                        metadata={
                            "name": "ICMS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/bpe",
                            "required": True,
                        }
                    )
                    inf_ad_fisco: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "infAdFisco",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/bpe",
                            "min_length": 1,
                            "max_length": 2000,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )

                @dataclass
                class Comp:
                    """
                    :ivar x_nome: Nome do componente Exxemplos: ISENTOS,
                        VT, CARTAO PRE-PAGO, IDOSOS
                    :ivar q_comp: Quantidade do componente
                    """
                    x_nome: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "xNome",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/bpe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 15,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    q_comp: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "qComp",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/bpe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{5}",
                        }
                    )

        @dataclass
        class Total:
            """
            :ivar q_pass: Quantidade total de passagens
            :ivar v_bp: Valor Total do Bilhete de Passagem Transporte
                Metropolitano Pode conter zeros quando o BP-e for de
                complemento de ICMS
            :ivar icmstot: Totais referentes ao ICMS
            """
            q_pass: Optional[str] = field(
                default=None,
                metadata={
                    "name": "qPass",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1,6}",
                }
            )
            v_bp: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vBP",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            icmstot: Optional["TbpeTm.InfBpe.Total.Icmstot"] = field(
                default=None,
                metadata={
                    "name": "ICMSTot",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )

            @dataclass
            class Icmstot:
                """
                :ivar v_bc: BC do ICMS
                :ivar v_icms: Valor Total do ICMS
                """
                v_bc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vBC",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 5000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )


@dataclass
class TretBpe:
    """
    Tipo Retorno do Pedido de Autorização de BP-e (Modelo 63)

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar c_uf: Identificação da UF
    :ivar ver_aplic: Versão do Aplicativo que processou o BP-e
    :ivar c_stat: código do status do retorno da consulta.
    :ivar x_motivo: Descrição literal do status do do retorno da
        consulta.
    :ivar prot_bpe: Reposta ao processamento do BP-e
    :ivar versao:
    """
    class Meta:
        name = "TRetBPe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    c_uf: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    prot_bpe: Optional[TprotBpe] = field(
        default=None,
        metadata={
            "name": "protBPe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
class TenviBpe:
    """
    Tipo Pedido de Concessão de Autorização de BP-e.
    """
    class Meta:
        name = "TEnviBPe"

    id_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "idLote",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,15}",
        }
    )
    bpe: Optional[Tbpe] = field(
        default=None,
        metadata={
            "name": "BPe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
