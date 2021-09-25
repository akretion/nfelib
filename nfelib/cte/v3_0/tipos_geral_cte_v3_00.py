from enum import Enum

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class Tamb(Enum):
    """
    Tipo Ambiente.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"


class TcorgaoIbge(Enum):
    """Tipo Código de orgão (UF da tabela do IBGE + 90 SUFRAMA + 91 RFB +  94
    SVC-RS + 95 SVC-SP + 96  Sinc.

    Chaves do RS para SVSP
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
    VALUE_90 = "90"
    VALUE_91 = "91"
    VALUE_93 = "93"
    VALUE_94 = "94"
    VALUE_95 = "95"
    VALUE_96 = "96"


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


class TmodCt(Enum):
    """
    Tipo Modelo Documento Fiscal.
    """
    VALUE_57 = "57"


class TmodCtos(Enum):
    """
    Tipo Modelo Documento Fiscal.
    """
    VALUE_67 = "67"


class TmodCtCargaOs(Enum):
    """
    Tipo Modelo Documento Fiscal.
    """
    VALUE_57 = "57"
    VALUE_67 = "67"


class TmodGtve(Enum):
    """
    Tipo Modelo Documento Fiscal.
    """
    VALUE_64 = "64"


class TmodNf(Enum):
    """Tipo Modelo Documento Fiscal - NF Remetente"""
    VALUE_01 = "01"
    VALUE_04 = "04"


class TufSemEx(Enum):
    """
    Tipo Sigla da UF, sem Exterior.
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


class TtipoUnidCarga(Enum):
    """
    Tipo da Unidade de Carga.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


class TtipoUnidTransp(Enum):
    """
    Tipo da Unidade de Transporte.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
