from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlDateTime
from nfelib.nfe.bindings.v4_0.leiaute_nfe_v4_00 import Tendereco
from nfelib.nfe.bindings.v4_0.tipos_basico_v4_00 import (
    TcodUfIbge,
    Tuf,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class TufCons(Enum):
    """
    Tipo Sigla da UF consultada.
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
    SU = "SU"


class InfCadCSit(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class InfCadIndCredCte(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


class InfCadIndCredNfe(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


class InfConsXServ(Enum):
    CONS_CAD = "CONS-CAD"


@dataclass
class TconsCad:
    """
    Tipo Pedido de Consulta de cadastro de contribuintes.

    :ivar infCons: Dados do Pedido de Consulta de cadastro de
        contribuintes
    :ivar versao:
    """
    class Meta:
        name = "TConsCad"

    infCons: Optional["TconsCad.InfCons"] = field(
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
            "pattern": r"2\.00",
        }
    )

    @dataclass
    class InfCons:
        """
        :ivar xServ: Serviço Solicitado
        :ivar UF: sigla da UF consultada, utilizar SU para SUFRAMA
        :ivar IE: Inscrição Estadual do contribuinte
        :ivar CNPJ: CNPJ do contribuinte
        :ivar CPF: CPF do contribuinte
        """
        xServ: Optional[InfConsXServ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        UF: Optional[TufCons] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        IE: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r"[0-9]{2,14}|ISENTO",
            }
        )
        CNPJ: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r"[0-9]{3,14}",
            }
        )
        CPF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 11,
                "white_space": "preserve",
                "pattern": r"[0-9]{3,11}",
            }
        )


@dataclass
class TretConsCad:
    """
    Tipo Retorno Pedido de Consulta de cadastro de contribuintes.

    :ivar infCons: Dados do Resultado doDados do Pedido de Consulta de
        cadastro de contribuintes
    :ivar versao:
    """
    class Meta:
        name = "TRetConsCad"

    infCons: Optional["TretConsCad.InfCons"] = field(
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
            "pattern": r"2\.00",
        }
    )

    @dataclass
    class InfCons:
        """
        :ivar verAplic: Versão do Aplicativo que processou o pedido de
            consulta de cadastro
        :ivar cStat: Código do status da mensagem enviada.
        :ivar xMotivo: Descrição literal do status do serviço
            solicitado.
        :ivar UF: sigla da UF consultada, utilizar SU para SUFRAMA
        :ivar IE: Inscrição Estadual do contribuinte
        :ivar CNPJ: CNPJ do contribuinte
        :ivar CPF: CPF do contribuinte
        :ivar dhCons: Data da Consulta
        :ivar cUF: código da UF de atendimento
        :ivar infCad: Informações cadastrais do contribuinte consultado
        """
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
        cStat: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "max_length": 3,
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
        UF: Optional[TufCons] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        IE: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r"[0-9]{2,14}|ISENTO",
            }
        )
        CNPJ: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r"[0-9]{3,14}",
            }
        )
        CPF: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 11,
                "white_space": "preserve",
                "pattern": r"[0-9]{3,11}",
            }
        )
        dhCons: Optional[XmlDateTime] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        cUF: Optional[TcodUfIbge] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        infCad: List["TretConsCad.InfCons.InfCad"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )

        @dataclass
        class InfCad:
            """
            :ivar IE: Número da Inscrição Estadual do contribuinte
            :ivar CNPJ: Número do CNPJ  do contribuinte
            :ivar CPF: Número do CPF do contribuinte
            :ivar UF: Sigla da UF de localização do contribuinte. Em
                algumas situações, a UF de localização pode ser
                diferente da UF consultada. Ex. IE de Substituto
                Tributário.
            :ivar cSit: Situação cadastral do contribuinte: 0 - não
                habilitado 1 - habilitado
            :ivar indCredNFe: Indicador de contribuinte credenciado a
                emitir NF-e. 0 - Não credenciado para emissão da NF-e; 1
                - Credenciado; 2 - Credenciado com obrigatoriedade para
                todas operações; 3 - Credenciado com obrigatoriedade
                parcial; 4 – a SEFAZ não fornece a informação. Este
                indicador significa apenas que o contribuinte é
                credenciado para emitir NF-e na SEFAZ consultada.
            :ivar indCredCTe: Indicador de contribuinte credenciado a
                emitir CT-e. 0 - Não credenciado para emissão da CT-e; 1
                - Credenciado; 2 - Credenciado com obrigatoriedade para
                todas operações; 3 - Credenciado com obrigatoriedade
                parcial; 4 – a SEFAZ não fornece a informação. Este
                indicador significa apenas que o contribuinte é
                credenciado para emitir CT-e na SEFAZ consultada.
            :ivar xNome: Razão Social ou nome do contribuinte
            :ivar xFant: Razão Social ou nome do contribuinte
            :ivar xRegApur: Regime de Apuração do ICMS
            :ivar CNAE: CNAE Fiscal do contribuinte
            :ivar dIniAtiv: Data de início de atividades do contribuinte
            :ivar dUltSit: Data da última modificação da situação
                cadastral do contribuinte.
            :ivar dBaixa: Data de ocorrência da baixa do contribuinte.
            :ivar IEUnica: Inscrição Estadual Única
            :ivar IEAtual: Inscrição Estadual atual
            :ivar ender: Endereço
            """
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}|ISENTO",
                }
            )
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{3,14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 11,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{3,11}",
                }
            )
            UF: Optional[Tuf] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            cSit: Optional[InfCadCSit] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            indCredNFe: Optional[InfCadIndCredNfe] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            indCredCTe: Optional[InfCadIndCredCte] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            xFant: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            xRegApur: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 60,
                }
            )
            CNAE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "pattern": r"[0-9]{6,7}",
                }
            )
            dIniAtiv: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            dUltSit: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            dBaixa: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            IEUnica: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}|ISENTO",
                }
            )
            IEAtual: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}|ISENTO",
                }
            )
            ender: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
