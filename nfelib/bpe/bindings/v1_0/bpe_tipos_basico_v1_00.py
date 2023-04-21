from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bpe.bindings.v1_0.tipos_geral_bpe_v1_00 import (
    Tamb,
    TcodUfIbge,
    TmodBpe,
    Tuf,
    TufSemEx,
)
from nfelib.bpe.bindings.v1_0.xmldsig_core_schema_v1_01 import Signature

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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    xContato: Optional[str] = field(
        default=None,
        metadata={
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
    idCSRT: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "pattern": r"[0-9]{3}",
        }
    )
    hashCSRT: Optional[bytes] = field(
        default=None,
        metadata={
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

    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município (utilizar a tabela do IBGE)
    :ivar xMun: Nome do município
    :ivar CEP: CEP Informar zeros não significativos
    :ivar UF: Sigla da UF
    :ivar fone: Telefone
    :ivar email: Endereço de E-mail
    """
    class Meta:
        name = "TEndeEmi"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
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
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    UF: Optional[TufSemEx] = field(
        default=None,
        metadata={
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
    :ivar fone: Telefone
    :ivar email: Endereço de E-mail
    """
    class Meta:
        name = "TEndereco"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
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
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
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
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    cPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    xPais: Optional[str] = field(
        default=None,
        metadata={
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

    :ivar ICMS00: Prestação sujeito à tributação normal do ICMS
    :ivar ICMS20: Prestação sujeito à tributação com redução de BC do
        ICMS
    :ivar ICMS45: ICMS  Isento, não Tributado ou diferido
    :ivar ICMS90: ICMS Outros
    :ivar ICMSSN: Simples Nacional
    """
    class Meta:
        name = "TImp"

    ICMS00: Optional["Timp.Icms00"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
        }
    )
    ICMS20: Optional["Timp.Icms20"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
        }
    )
    ICMS45: Optional["Timp.Icms45"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
        }
    )
    ICMS90: Optional["Timp.Icms90"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
        }
    )
    ICMSSN: Optional["Timp.Icmssn"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
            }
        )
        vBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pICMS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vICMS: Optional[str] = field(
            default=None,
            metadata={
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
            }
        )
        pRedBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pICMS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vICMS: Optional[str] = field(
            default=None,
            metadata={
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
        :ivar CST: Classificação Tributária do Serviço Preencher com: 40
            - ICMS isenção; 41 - ICMS não tributada; 51 - ICMS diferido
        """
        CST: Optional[Icms45Cst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
            }
        )
        pRedBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "white_space": "preserve",
                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pICMS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
            }
        )
        vICMS: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        vCred: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
            }
        )
        indSN: Optional[IcmssnIndSn] = field(
            default=None,
            metadata={
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

    :ivar infProt: Dados do protocolo de status
    :ivar infFisco: Mensagem do Fisco
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TProtBPe"

    infProt: Optional["TprotBpe.InfProt"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    infFisco: Optional["TprotBpe.InfFisco"] = field(
        default=None,
        metadata={
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
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar verAplic: Versão do Aplicativo que processou o BP-e
        :ivar chBPe: Chave de acesso do BP-e
        :ivar dhRecbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SS TZD.
        :ivar nProt: Número do Protocolo de Status do BP-e.
        :ivar digVal: Digest Value do BP-e processado. Utilizado para
            conferir a integridade do BP-e original.
        :ivar cStat: Código do status do BP-e.
        :ivar xMotivo: Descrição literal do status do BP-e.
        :ivar Id:
        """
        tpAmb: Optional[Tamb] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
            }
        )
        verAplic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        chBPe: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        nProt: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        digVal: Optional[bytes] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "format": "base64",
            }
        )
        cStat: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMotivo: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMsg: Optional[str] = field(
            default=None,
            metadata={
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

    :ivar infBPe: Informações do BP-e
    :ivar infBPeSupl: Informações suplementares do BP-e
    :ivar signature:
    """
    class Meta:
        name = "TBPe"

    infBPe: Optional["Tbpe.InfBpe"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    infBPeSupl: Optional["Tbpe.InfBpeSupl"] = field(
        default=None,
        metadata={
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
        :ivar infBPeSub: Informações dos BP-e de Substituição para
            remarcação e/ou transferência
        :ivar infPassagem: Informações do detalhamento da Passagem
        :ivar infViagem: Grupo de informações da viagem do BP-e
        :ivar infValorBPe: Informações dos valores do Bilhete de
            Passagem
        :ivar imp: Informações relativas aos Impostos
        :ivar pag: Dados de Pagamento.
        :ivar autXML: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar infAdic: Informações Adicionais
        :ivar infRespTec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar versao: Versão do leiaute Ex: "3.00"
        :ivar Id: Identificador da tag a ser assinada Informar a chave
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
        infBPeSub: Optional["Tbpe.InfBpe.InfBpeSub"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
            }
        )
        infPassagem: Optional["Tbpe.InfBpe.InfPassagem"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
            }
        )
        infViagem: List["Tbpe.InfBpe.InfViagem"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "min_occurs": 1,
            }
        )
        infValorBPe: Optional["Tbpe.InfBpe.InfValorBpe"] = field(
            default=None,
            metadata={
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
        autXML: List["Tbpe.InfBpe.AutXml"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "max_occurs": 10,
            }
        )
        infAdic: Optional["Tbpe.InfBpe.InfAdic"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
            }
        )
        infRespTec: Optional[TrespTec] = field(
            default=None,
            metadata={
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
        Id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"BPe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar cUF: Código da UF do emitente do BP-e Código da UF do
                emitente do Documento Fiscal. Utilizar a Tabela do IBGE
                de código de unidades da federação.
            :ivar tpAmb: Tipo do Ambiente 1 - Produção 2 - Homologação
            :ivar mod: Modelo do Bilhete de Passagem Utilizar o código
                63 para identificação do BP-e
            :ivar serie: Série do documento fiscal Informar a série do
                documento fiscal (informar zero se inexistente).
            :ivar nBP: Número do bilhete de passagem Número que
                identifica o bilhete 1 a 999999999.
            :ivar cBP: Código numérico que compõe a Chave de Acesso.
                Código aleatório gerado pelo emitente, com o objetivo de
                evitar acessos indevidos ao documento.
            :ivar cDV: Digito verificador da chave de acesso Informar o
                dígito  de controle da chave de acesso do BP-e, que deve
                ser calculado com a aplicação do algoritmo módulo 11
                (base 2,9) da chave de acesso.
            :ivar modal: Modalidade de transporte 1 - Rodoviário; 3 -
                Aquaviário; 4 - Ferroviário.
            :ivar dhEmi: Data e hora de emissão do Bilhete de Passagem
                Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar tpEmis: Forma de emissão do Bilhete (Normal ou
                Contingência Off-Line) 1 - Normal ; 2 - Contingência
                Off-Line
            :ivar verProc: Versão do processo de emissão Informar a
                versão do aplicativo emissor de BP-e.
            :ivar tpBPe: Tipo do BP-e 0 - BP-e normal 3 - BP-e
                substituição
            :ivar indPres: Indicador de presença do comprador no
                estabelecimento comercial no momento da operação
                1=Operação presencial não embarcado; 2=Operação não
                presencial, pela Internet; 3=Operação não presencial,
                Teleatendimento; 4=BP-e em operação com entrega a
                domicílio; 5=Operação presencial embarcada; 9=Operação
                não presencial, outros.
            :ivar UFIni: Sigla da UF Início da Viagem Utilizar a Tabela
                do IBGE de código de unidades da federação
            :ivar cMunIni: Código do município do início da viagem
            :ivar UFFim: Sigla da UF do Fim da Viagem Utilizar a Tabela
                do IBGE de código de unidades da federação. Informar
                'EX' para operações com o exterior.
            :ivar cMunFim: Código do município do fim da viagem
            :ivar dhCont: Data e Hora da entrada em contingência
                Informar a data e hora no formato AAAA-MM-DDTHH:MM:SS
            :ivar xJust: Justificativa da entrada em contingência
            """
            cUF: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            tpAmb: Optional[Tamb] = field(
                default=None,
                metadata={
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
            nBP: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            cBP: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            cDV: Optional[str] = field(
                default=None,
                metadata={
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
            dhEmi: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tpEmis: Optional[IdeTpEmis] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            verProc: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            tpBPe: Optional[TtipoBpe] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            indPres: Optional[TindPres] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            UFIni: Optional[TufSemEx] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            cMunIni: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            UFFim: Optional[Tuf] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            cMunFim: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            dhCont: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            xJust: Optional[str] = field(
                default=None,
                metadata={
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
            :ivar CNPJ: CNPJ do emitente Informar zeros não
                significativos
            :ivar IE: Inscrição Estadual do emitente
            :ivar IEST: Inscrição Estadual do Substituto Tributário
            :ivar xNome: Razão social ou Nome do emitente
            :ivar xFant: Nome fantasia do emitente
            :ivar IM: Inscrição Municipal
            :ivar CNAE: CNAE Fiscal
            :ivar CRT: Código de Regime Tributário. Este campo será
                obrigatoriamente preenchido com: 1 – Simples Nacional; 2
                – Simples Nacional – excesso de sublimite de receita
                bruta; 3 – Regime Normal.
            :ivar enderEmit: Endereço do emitente
            :ivar TAR: Termo de Autorização de Serviço Regular Registro
                obrigatório do emitente do BP-e junto à ANTT para
                exercer a atividade
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            IEST: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            IM: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            CNAE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            CRT: Optional[EmitCrt] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            enderEmit: Optional[TendeEmi] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            TAR: Optional[str] = field(
                default=None,
                metadata={
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
            :ivar xNome: Razão social ou Nome do comprador
            :ivar CNPJ: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar CPF: Número do CPF Informar os zeros não
                significativos.
            :ivar idEstrangeiro: Identificador do comprador em caso de
                comprador estrangeiro
            :ivar IE: Inscrição Estadual Informar a IE do remetente ou
                ISENTO se remetente é contribuinte do ICMS isento de
                inscrição no cadastro de contribuintes do ICMS. Caso o
                remetente não seja contribuinte do ICMS não informar a
                tag.
            :ivar enderComp: Endereço do comprador
            """
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            idEstrangeiro: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"([!-ÿ]{0}|[!-ÿ]{5,20})?",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0,14}|ISENTO|PR[0-9]{4,8}",
                }
            )
            enderComp: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )

        @dataclass
        class Agencia:
            """
            :ivar xNome: Razão social ou Nome da Agência
            :ivar CNPJ: Número do CNPJ Em caso de empresa não
                estabelecida no Brasil, será informado o CNPJ com zeros.
                Informar os zeros não significativos.
            :ivar enderAgencia: Endereço da agência
            """
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{0}|[0-9]{14}",
                }
            )
            enderAgencia: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )

        @dataclass
        class InfBpeSub:
            """
            :ivar chBPe: Chave do Bilhete de Passagem Substituido
                Informar os zeros não significativos.
            :ivar tpSub: Tipo de Substituição 1 - Remarcação 2 -
                Transferência 3 - Transferência e Remarcação
            """
            chBPe: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "max_length": 44,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{44}",
                }
            )
            tpSub: Optional[TtipoSubstituicao] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )

        @dataclass
        class InfPassagem:
            """
            :ivar cLocOrig: Código da Localidade de Origem
            :ivar xLocOrig: Descrição da Localidade de Origem
            :ivar cLocDest:
            :ivar xLocDest: Descrição da Localidade de Destino
            :ivar dhEmb: Data e hora de embarque Formato AAAA-MM-
                DDTHH:MM:DD TZD
            :ivar dhValidade: Data e hora de validade do bilhete Formato
                AAAA-MM-DDTHH:MM:DD TZD
            :ivar infPassageiro: Informações do passageiro
            """
            cLocOrig: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 7,
                    "white_space": "preserve",
                }
            )
            xLocOrig: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            cLocDest: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 7,
                    "white_space": "preserve",
                }
            )
            xLocDest: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            dhEmb: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            dhValidade: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            infPassageiro: Optional["Tbpe.InfBpe.InfPassagem.InfPassageiro"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                }
            )

            @dataclass
            class InfPassageiro:
                """
                :ivar xNome: Nome do Passageiro
                :ivar CPF: Número do CPF Informar os zeros não
                    significativos.
                :ivar tpDoc: Tipo do Documento de identificação 1-RG
                    2-Título de Eleitor 3-Passaporte 4-CNH 5-Outros
                :ivar nDoc: Número do Documento do passageiro
                :ivar xDoc: Descrição do tipo de documento "outros"
                :ivar dNasc: Data de Nascimento Formato AAAA-MM-DD
                :ivar fone: Telefone
                :ivar email: Endereço de E-mail
                """
                xNome: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                CPF: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{11}",
                    }
                )
                tpDoc: Optional[Tdoc] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                    }
                )
                nDoc: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "min_length": 2,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                xDoc: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 2,
                        "max_length": 100,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                dNasc: Optional[str] = field(
                    default=None,
                    metadata={
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
            :ivar cPercurso: Código do percurso da viagem
            :ivar xPercurso: Descrição do Percurso da viagem
            :ivar tpViagem: Tipo de Viagem Informa o código do tipo da
                viagem (00-regular, 01-extra)
            :ivar tpServ: Tipo de Serviço Informar o código do tipo de
                serviço (1-Convencional com sanitário, 2-Convencional
                sem sanitário, 3-Semileito, 4-Leito com ar condicionado,
                5-Leito sem ar condicionado, 6-Executivo, 7-Semiurbano,
                8-Longitudinal, 9-Travessia, 10-Cama, 11-Micro-onibus)
            :ivar tpAcomodacao: Tipo de Acomodação Informar o código do
                tipo de acomodação (1-Assento/poltrona, 2-Rede, 3-Rede
                com ar-condicionado, 4-Cabine, 5-Outros)
            :ivar tpTrecho: Tipo de trecho da viagem Informar do tipo de
                trecho (1-Normal, 2-Trecho Inicial, 3-Conexão)
            :ivar dhViagem: Data e hora de referencia para a viagem
                Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar dhConexao: Data e hora da conexão Informar se tpTrecho
                = 3 Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar prefixo: Prefixo da linha
            :ivar poltrona: Número da Poltrona / assento / cabine
            :ivar plataforma: Plataforma/carro/barco de Embarque
            :ivar infTravessia: Informações do transporte aquaviário de
                travessia
            """
            cPercurso: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                }
            )
            xPercurso: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 100,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            tpViagem: Optional[InfViagemTpViagem] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tpServ: Optional[InfViagemTpServ] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tpAcomodacao: Optional[InfViagemTpAcomodacao] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tpTrecho: Optional[InfViagemTpTrecho] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            dhViagem: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            dhConexao: Optional[str] = field(
                default=None,
                metadata={
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
            infTravessia: Optional["Tbpe.InfBpe.InfViagem.InfTravessia"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                }
            )

            @dataclass
            class InfTravessia:
                """
                :ivar tpVeiculo: Tipo do veículo transportado
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
                :ivar sitVeiculo: Situação do veículo transportado 01 -
                    Vazio; 02 - Carregado; 03 - Não se aplica
                """
                tpVeiculo: Optional[InfTravessiaTpVeiculo] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                sitVeiculo: Optional[InfTravessiaSitVeiculo] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                    }
                )

        @dataclass
        class InfValorBpe:
            """
            :ivar vBP: Valor do Bilhete de Passagem Pode conter zeros
                quando o BP-e for de complemento de ICMS
            :ivar vDesconto: Valor do desconto concedido ao comprador
                Indicar o valor total concedido em função dos benefícios
                concedidos ou política de desconto da empresa Informar
                0.00 em caso de passagem comercializada sem nenhum
                desconto
            :ivar vPgto: Valor pago pelo BP-e (vBP - vDesconto)
            :ivar vTroco: Valor do troco
            :ivar tpDesconto: Tipo de desconto/benefício para o BP-e 01
                - Tarifa promocional 02 - Idoso 03 - Criança 04 -
                Deficiente 05 - Estudante 06 - Animal Doméstico 07 -
                Acordo Coletivo 08 - Profissional em Deslocamento 09 -
                Profissional da Empresa 10 - Jovem 99 - Outros
            :ivar xDesconto: Descrição do tipo de desconto/benefício
                concedido
            :ivar cDesconto: Código do desconto quando informado com
                tipo 99 - Outros
            :ivar comp: Componentes do Valor do Bilhete
            """
            vBP: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            vDesconto: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            vPgto: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            vTroco: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            tpDesconto: Optional[InfValorBpeTpDesconto] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                }
            )
            xDesconto: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 2,
                    "max_length": 100,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            cDesconto: Optional[str] = field(
                default=None,
                metadata={
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
                :ivar tpComp: Tipo do Componente 01 - TARIFA; 02 -
                    PEDÁGIO; 03 - TAXA EMBARQUE; 04 - SEGURO; 05-TAXA DE
                    MANUTENÇÃO RODOVIA (TMR); 06 - SERVIÇO DE VENDA
                    INTEGRADA (SVI); 99 - OUTROS
                :ivar vComp: Valor do componente
                """
                tpComp: Optional[CompTpComp] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                vComp: Optional[str] = field(
                    default=None,
                    metadata={
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            vTotTrib: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            infAdFisco: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 2000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ICMSUFFim: Optional["Tbpe.InfBpe.Imp.Icmsuffim"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                }
            )

            @dataclass
            class Icmsuffim:
                """
                :ivar vBCUFFim: Valor da BC do ICMS na UF fim da viagem
                :ivar pFCPUFFim: Percentual do ICMS relativo ao Fundo de
                    Combate à pobreza (FCP) na UF fim da viagem Alíquota
                    adotada nas operações internas na UF do destinatário
                :ivar pICMSUFFim: Alíquota interna da UF fim da viagem
                    Alíquota adotada nas operações internas na UF do
                    destinatário
                :ivar pICMSInter: Alíquota interestadual das UF
                    envolvidas Alíquota interestadual das UF envolvidas
                :ivar vFCPUFFim: Valor do ICMS relativo ao Fundo de
                    Combate á Pobreza (FCP) da UF fim da viagem
                :ivar vICMSUFFim: Valor do ICMS de partilha para a UF
                    fim da viagem
                :ivar vICMSUFIni: Valor do ICMS de partilha para a UF
                    início da viagem
                """
                vBCUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                pFCPUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                pICMSUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                pICMSInter: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
                    }
                )
                vFCPUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vICMSUFFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vICMSUFIni: Optional[str] = field(
                    default=None,
                    metadata={
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
            :ivar tPag: Forma de
                Pagamento:01-Dinheiro;02-Cheque;03-Cartão de
                Crédito;04-Cartão de Débito;05-Vale Transportel;06 -
                PIX; 99 - Outros
            :ivar xPag: Descrição da forma de pagamento 99 - Outros
            :ivar nDocPag: Número do documento ou carteira apresentada
                nas formas de pagamento diferentes de 03 e 04
            :ivar vPag: Valor do Pagamento
            :ivar card: Grupo de Cartões
            """
            tPag: Optional[PagTPag] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            xPag: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 2,
                    "max_length": 100,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            nDocPag: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 2,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            vPag: Optional[str] = field(
                default=None,
                metadata={
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
                :ivar tpIntegra: Tipo de Integração do processo de
                    pagamento com o sistema de automação da empresa
                    1=Pagamento integrado com o sistema de automação da
                    empresa Ex. equipamento TEF , Comercio Eletronico
                    2=Pagamento não integrado com o sistema de automação
                    da empresa Ex: equipamento POS
                :ivar CNPJ: CNPJ da credenciadora de cartão de
                    crédito/débito
                :ivar tBand: Bandeira da operadora de cartão de
                    crédito/débito 01–Visa; 02–Mastercard; 03–American
                    Express; 04–Sorocred; 05 - Elo; 06 - Diners;
                    99–Outros
                :ivar xBand: Descrição da operador de cartão para 99 -
                    Outros
                :ivar cAut: Número de autorização da operação cartão de
                    crédito/débito
                :ivar nsuTrans: Número sequencial único da transação
                :ivar nsuHost: Número sequencial único do Host
                :ivar nParcelas: Número de parcelas
                :ivar infAdCard: Informações adicionais operacionais
                    para integração do cartão de crédito Norma
                    referenciada, informações complementares, etc
                """
                tpIntegra: Optional[CardTpIntegra] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                CNPJ: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{14}",
                    }
                )
                tBand: Optional[CardTBand] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "white_space": "preserve",
                    }
                )
                xBand: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 2,
                        "max_length": 100,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                cAut: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                nsuTrans: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                nsuHost: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                nParcelas: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 3,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{3}",
                    }
                )
                infAdCard: Optional[str] = field(
                    default=None,
                    metadata={
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
            :ivar CNPJ: CNPJ do autorizado Informar zeros não
                significativos
            :ivar CPF: CPF do autorizado Informar zeros não
                significativos
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
        :ivar qrCodBPe: Texto com o QR-Code impresso no DABPE
        :ivar boardPassBPe: Texto contendo o boarding Pass impresso no
            DABPE (padrão PDF417) O boarding Pass poderá ser gerado no
            padrão PDF417 e impresso no DABPE opcionalmente pelo
            emitente para colocar informações operacionais do bilhete
            e/ou prestar informações para a agência reguladora do setor
        """
        qrCodBPe: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "required": True,
                "min_length": 50,
                "max_length": 1000,
                "white_space": "preserve",
                "pattern": r"((HTTPS?|https?)://.*\?chBPe=[0-9]{44}&tpAmb=[1-2](&sign=[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})?)",
            }
        )
        boardPassBPe: Optional[str] = field(
            default=None,
            metadata={
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

    :ivar infBPe: Informações do BPeTM
    :ivar signature:
    """
    class Meta:
        name = "TBPeTM"

    infBPe: Optional["TbpeTm.InfBpe"] = field(
        default=None,
        metadata={
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
        :ivar detBPeTM: Grupo de informações detalhadas do BPe TM
        :ivar total: Informações dos totais do BPe TM
        :ivar autXML: Autorizados para download do XML do DF-e Informar
            CNPJ ou CPF. Preencher os zeros não significativos.
        :ivar infAdic: Informações Adicionais
        :ivar infRespTec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar versao: Versão do leiaute Ex: "3.00"
        :ivar Id: Identificador da tag a ser assinada Informar a chave
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
        detBPeTM: List["TbpeTm.InfBpe.DetBpeTm"] = field(
            default_factory=list,
            metadata={
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
        autXML: List["TbpeTm.InfBpe.AutXml"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
                "max_occurs": 10,
            }
        )
        infAdic: Optional["TbpeTm.InfBpe.InfAdic"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/bpe",
            }
        )
        infRespTec: Optional[TrespTec] = field(
            default=None,
            metadata={
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
        Id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"BPe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar cUF: Código da UF do emitente do BP-e Código da UF do
                emitente do Documento Fiscal. Utilizar a Tabela do IBGE
                de código de unidades da federação.
            :ivar tpAmb: Tipo do Ambiente 1 - Produção 2 - Homologação
            :ivar mod: Modelo do Bilhete de Passagem Utilizar o código
                63 para identificação do BP-e
            :ivar serie: Série do documento fiscal Informar a série do
                documento fiscal (informar zero se inexistente).
            :ivar nBP: Número do bilhete de passagem Número que
                identifica o bilhete 1 a 999999999.
            :ivar cBP: Código numérico que compõe a Chave de Acesso.
                Código aleatório gerado pelo emitente, com o objetivo de
                evitar acessos indevidos ao documento.
            :ivar cDV: Digito verificador da chave de acesso Informar o
                dígito  de controle da chave de acesso do BP-e, que deve
                ser calculado com a aplicação do algoritmo módulo 11
                (base 2,9) da chave de acesso.
            :ivar modal: Modalidade de transporte 1 - Rodoviário; 3 -
                Aquaviário; 4 - Ferroviário.
            :ivar dhEmi: Data e hora de emissão do Bilhete de Passagem
                Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar dCompet: Data da Competência a que se refere o
                Transporte Metropolitano Formato AAAA-MM-DDTHH:MM:DD TZD
            :ivar tpEmis: Forma de emissão do Bilhete (Normal ou
                Contingência Off-Line) 1 - Normal ; 2 - Contingência
                Off-Line
            :ivar verProc: Versão do processo de emissão Informar a
                versão do aplicativo emissor de BP-e.
            :ivar tpBPe: Tipo do BP-e 4 - BP-e Transporte Metropolitano
            :ivar CFOP: Código Fiscal de Operações e Prestações
            :ivar dhCont: Data e Hora da entrada em contingência
                Informar a data e hora no formato AAAA-MM-DDTHH:MM:SS
            :ivar xJust: Justificativa da entrada em contingência
            """
            cUF: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            tpAmb: Optional[Tamb] = field(
                default=None,
                metadata={
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
            nBP: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
                }
            )
            cBP: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            cDV: Optional[str] = field(
                default=None,
                metadata={
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
            dhEmi: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            dCompet: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"((((20|19|18)(([02468][048])|([13579][26]))-02-29))|((20|19|18)[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            tpEmis: Optional[IdeTpEmis] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            verProc: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            tpBPe: Optional[TtipoBpeTm] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            CFOP: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[123567][0-9]([0-9][1-9]|[1-9][0-9])",
                }
            )
            dhCont: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            xJust: Optional[str] = field(
                default=None,
                metadata={
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
            :ivar CNPJ: CNPJ do emitente Informar zeros não
                significativos
            :ivar IE: Inscrição Estadual do emitente
            :ivar IEST: Inscrição Estadual do Substituto Tributário
            :ivar xNome: Razão social ou Nome do emitente
            :ivar xFant: Nome fantasia do emitente
            :ivar IM: Inscrição Municipal
            :ivar CNAE: CNAE Fiscal
            :ivar CRT: Código de Regime Tributário. Este campo será
                obrigatoriamente preenchido com: 1 – Simples Nacional; 2
                – Simples Nacional – excesso de sublimite de receita
                bruta; 3 – Regime Normal.
            :ivar enderEmit: Endereço do emitente
            :ivar TAR: Termo de Autorização de Serviço Regular Registro
                obrigatório do emitente do BP-e junto à ANTT para
                exercer a atividade
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            IEST: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            IM: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            CNAE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            CRT: Optional[EmitCrt] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            enderEmit: Optional[TendeEmi] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            TAR: Optional[str] = field(
                default=None,
                metadata={
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
            :ivar UFIniViagem: Sigla da UF início da Viagem Utilizar a
                Tabela do IBGE de código de unidades da federação
            :ivar UFFimViagem: Sigla da UF fim da Viagem Utilizar a
                Tabela do IBGE de código de unidades da federação
            :ivar placa: Placa do coletivo
            :ivar prefixo: Prefixo da linha
            :ivar det: Datalhamento da viagem por trechos do BPeTM
            :ivar idEqpCont: Identificador do equipamento contador
            """
            UFIniViagem: Optional[TufSemEx] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )
            UFFimViagem: Optional[TufSemEx] = field(
                default=None,
                metadata={
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
            idEqpCont: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,1}|[1-8]{1}[0-9]{2}|[9]{1}[0-8]{1}[0-9]{1}|[9]{1}[9]{1}[0]{1}",
                }
            )

            @dataclass
            class Det:
                """
                :ivar cMunIni: Código do município do início da viagem
                :ivar cMunFim: Código do município do fim da viagem
                :ivar nContInicio: Contador início da viagem
                :ivar nContFim: Contador fim da viagem
                :ivar qPass: Quantidade de Passagens da viagem
                :ivar vBP: Valor da soma dos Bilhetes de Passagem da
                    viagem Pode conter zeros quando o BP-e for de
                    complemento de ICMS
                :ivar imp: Informações relativas aos Impostos
                :ivar comp: Componentes da viagem
                :ivar nViagem:
                """
                cMunIni: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7}",
                    }
                )
                cMunFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7}",
                    }
                )
                nContInicio: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                    }
                )
                nContFim: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                    }
                )
                qPass: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 20,
                        "white_space": "preserve",
                    }
                )
                vBP: Optional[str] = field(
                    default=None,
                    metadata={
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
                nViagem: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[1-9]{1}[0-9]{0,1}|[1-8]{1}[0-9]{2}|[9]{1}[0-8]{1}[0-9]{1}|[9]{1}[9]{1}[0]{1}",
                    }
                )

                @dataclass
                class Imp:
                    """
                    :ivar ICMS: Informações relativas ao ICMS
                    :ivar infAdFisco: Informações adicionais de
                        interesse do Fisco Norma referenciada,
                        informações complementares, etc
                    """
                    ICMS: Optional[Timp] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/bpe",
                            "required": True,
                        }
                    )
                    infAdFisco: Optional[str] = field(
                        default=None,
                        metadata={
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
                    :ivar xNome: Nome do componente Exxemplos: ISENTOS,
                        VT, CARTAO PRE-PAGO, IDOSOS
                    :ivar qComp: Quantidade do componente
                    """
                    xNome: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/bpe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 15,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    qComp: Optional[str] = field(
                        default=None,
                        metadata={
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
            :ivar qPass: Quantidade total de passagens
            :ivar vBP: Valor Total do Bilhete de Passagem Transporte
                Metropolitano Pode conter zeros quando o BP-e for de
                complemento de ICMS
            :ivar ICMSTot: Totais referentes ao ICMS
            """
            qPass: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1,6}",
                }
            )
            vBP: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            ICMSTot: Optional["TbpeTm.InfBpe.Total.Icmstot"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "required": True,
                }
            )

            @dataclass
            class Icmstot:
                """
                :ivar vBC: BC do ICMS
                :ivar vICMS: Valor Total do ICMS
                """
                vBC: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/bpe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vICMS: Optional[str] = field(
                    default=None,
                    metadata={
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
            :ivar CNPJ: CNPJ do autorizado Informar zeros não
                significativos
            :ivar CPF: CPF do autorizado Informar zeros não
                significativos
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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
                    "namespace": "http://www.portalfiscal.inf.br/bpe",
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

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar cUF: Identificação da UF
    :ivar verAplic: Versão do Aplicativo que processou o BP-e
    :ivar cStat: código do status do retorno da consulta.
    :ivar xMotivo: Descrição literal do status do do retorno da
        consulta.
    :ivar protBPe: Reposta ao processamento do BP-e
    :ivar versao:
    """
    class Meta:
        name = "TRetBPe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
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
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    protBPe: Optional[TprotBpe] = field(
        default=None,
        metadata={
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

    idLote: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/bpe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,15}",
        }
    )
    BPe: Optional[Tbpe] = field(
        default=None,
        metadata={
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
