from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.nfe.bindings.v4_0.leiaute_cons_sit_nfe_v4_00 import TprotNfe
from nfelib.nfe.bindings.v4_0.tipos_basico_v4_00 import (
    Tamb,
    TcodUfIbge,
    Tmod,
    Tuf,
    TufEmi,
)
from nfelib.nfe.bindings.v4_0.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class CofinsaliqCst(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"


class CofinsntCst(Enum):
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"


class CofinsoutrCst(Enum):
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_54 = "54"
    VALUE_55 = "55"
    VALUE_56 = "56"
    VALUE_60 = "60"
    VALUE_61 = "61"
    VALUE_62 = "62"
    VALUE_63 = "63"
    VALUE_64 = "64"
    VALUE_65 = "65"
    VALUE_66 = "66"
    VALUE_67 = "67"
    VALUE_70 = "70"
    VALUE_71 = "71"
    VALUE_72 = "72"
    VALUE_73 = "73"
    VALUE_74 = "74"
    VALUE_75 = "75"
    VALUE_98 = "98"
    VALUE_99 = "99"


class CofinsqtdeCst(Enum):
    VALUE_03 = "03"


class CofinsstIndSomaCofinsst(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class DiTpIntermedio(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class DiTpViaTransp(Enum):
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
    VALUE_12 = "12"
    VALUE_13 = "13"


class Icms00Cst(Enum):
    VALUE_00 = "00"


class Icms00ModBc(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class Icms10Cst(Enum):
    VALUE_10 = "10"


class Icms10ModBc(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class Icms10ModBcst(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class Icms10MotDesIcmsst(Enum):
    VALUE_3 = "3"
    VALUE_9 = "9"
    VALUE_12 = "12"


class Icms20Cst(Enum):
    VALUE_20 = "20"


class Icms20ModBc(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class Icms20MotDesIcms(Enum):
    VALUE_3 = "3"
    VALUE_9 = "9"
    VALUE_12 = "12"


class Icms30Cst(Enum):
    VALUE_30 = "30"


class Icms30ModBcst(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class Icms30MotDesIcms(Enum):
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_9 = "9"


class Icms40Cst(Enum):
    VALUE_40 = "40"
    VALUE_41 = "41"
    VALUE_50 = "50"


class Icms40MotDesIcms(Enum):
    VALUE_1 = "1"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"
    VALUE_9 = "9"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_16 = "16"
    VALUE_90 = "90"


class Icms51Cst(Enum):
    VALUE_51 = "51"


class Icms51ModBc(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class Icms60Cst(Enum):
    VALUE_60 = "60"


class Icms70Cst(Enum):
    VALUE_70 = "70"


class Icms70ModBc(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class Icms70ModBcst(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class Icms70MotDesIcms(Enum):
    VALUE_3 = "3"
    VALUE_9 = "9"
    VALUE_12 = "12"


class Icms70MotDesIcmsst(Enum):
    VALUE_3 = "3"
    VALUE_9 = "9"
    VALUE_12 = "12"


class Icms90Cst(Enum):
    VALUE_90 = "90"


class Icms90ModBc(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class Icms90ModBcst(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class Icms90MotDesIcms(Enum):
    VALUE_3 = "3"
    VALUE_9 = "9"
    VALUE_12 = "12"


class Icms90MotDesIcmsst(Enum):
    VALUE_3 = "3"
    VALUE_9 = "9"
    VALUE_12 = "12"


class IcmspartCst(Enum):
    VALUE_10 = "10"
    VALUE_90 = "90"


class IcmspartModBc(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class IcmspartModBcst(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class Icmssn101Csosn(Enum):
    VALUE_101 = "101"


class Icmssn102Csosn(Enum):
    VALUE_102 = "102"
    VALUE_103 = "103"
    VALUE_300 = "300"
    VALUE_400 = "400"


class Icmssn201Csosn(Enum):
    VALUE_201 = "201"


class Icmssn201ModBcst(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class Icmssn202Csosn(Enum):
    VALUE_202 = "202"
    VALUE_203 = "203"


class Icmssn202ModBcst(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class Icmssn500Csosn(Enum):
    VALUE_500 = "500"


class Icmssn900Csosn(Enum):
    VALUE_900 = "900"


class Icmssn900ModBc(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class Icmssn900ModBcst(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class IcmsstCst(Enum):
    VALUE_41 = "41"
    VALUE_60 = "60"


class IcmsufdestPIcmsinter(Enum):
    VALUE_4_00 = "4.00"
    VALUE_7_00 = "7.00"
    VALUE_12_00 = "12.00"


class IpintCst(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_54 = "54"
    VALUE_55 = "55"


class IpitribCst(Enum):
    VALUE_00 = "00"
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_99 = "99"


class IssqnIndIss(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"


class IssqnIndIncentivo(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


class IssqntotCRegTrib(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class PisaliqCst(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"


class PisntCst(Enum):
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"


class PisoutrCst(Enum):
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_54 = "54"
    VALUE_55 = "55"
    VALUE_56 = "56"
    VALUE_60 = "60"
    VALUE_61 = "61"
    VALUE_62 = "62"
    VALUE_63 = "63"
    VALUE_64 = "64"
    VALUE_65 = "65"
    VALUE_66 = "66"
    VALUE_67 = "67"
    VALUE_70 = "70"
    VALUE_71 = "71"
    VALUE_72 = "72"
    VALUE_73 = "73"
    VALUE_74 = "74"
    VALUE_75 = "75"
    VALUE_98 = "98"
    VALUE_99 = "99"


class PisqtdeCst(Enum):
    VALUE_03 = "03"


class PisstIndSomaPisst(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class TclistServ(Enum):
    """
    Tipo Código da Lista de Serviços LC 116/2003.
    """
    VALUE_01_01 = "01.01"
    VALUE_01_02 = "01.02"
    VALUE_01_03 = "01.03"
    VALUE_01_04 = "01.04"
    VALUE_01_05 = "01.05"
    VALUE_01_06 = "01.06"
    VALUE_01_07 = "01.07"
    VALUE_01_08 = "01.08"
    VALUE_01_09 = "01.09"
    VALUE_02_01 = "02.01"
    VALUE_03_02 = "03.02"
    VALUE_03_03 = "03.03"
    VALUE_03_04 = "03.04"
    VALUE_03_05 = "03.05"
    VALUE_04_01 = "04.01"
    VALUE_04_02 = "04.02"
    VALUE_04_03 = "04.03"
    VALUE_04_04 = "04.04"
    VALUE_04_05 = "04.05"
    VALUE_04_06 = "04.06"
    VALUE_04_07 = "04.07"
    VALUE_04_08 = "04.08"
    VALUE_04_09 = "04.09"
    VALUE_04_10 = "04.10"
    VALUE_04_11 = "04.11"
    VALUE_04_12 = "04.12"
    VALUE_04_13 = "04.13"
    VALUE_04_14 = "04.14"
    VALUE_04_15 = "04.15"
    VALUE_04_16 = "04.16"
    VALUE_04_17 = "04.17"
    VALUE_04_18 = "04.18"
    VALUE_04_19 = "04.19"
    VALUE_04_20 = "04.20"
    VALUE_04_21 = "04.21"
    VALUE_04_22 = "04.22"
    VALUE_04_23 = "04.23"
    VALUE_05_01 = "05.01"
    VALUE_05_02 = "05.02"
    VALUE_05_03 = "05.03"
    VALUE_05_04 = "05.04"
    VALUE_05_05 = "05.05"
    VALUE_05_06 = "05.06"
    VALUE_05_07 = "05.07"
    VALUE_05_08 = "05.08"
    VALUE_05_09 = "05.09"
    VALUE_06_01 = "06.01"
    VALUE_06_02 = "06.02"
    VALUE_06_03 = "06.03"
    VALUE_06_04 = "06.04"
    VALUE_06_05 = "06.05"
    VALUE_06_06 = "06.06"
    VALUE_07_01 = "07.01"
    VALUE_07_02 = "07.02"
    VALUE_07_03 = "07.03"
    VALUE_07_04 = "07.04"
    VALUE_07_05 = "07.05"
    VALUE_07_06 = "07.06"
    VALUE_07_07 = "07.07"
    VALUE_07_08 = "07.08"
    VALUE_07_09 = "07.09"
    VALUE_07_10 = "07.10"
    VALUE_07_11 = "07.11"
    VALUE_07_12 = "07.12"
    VALUE_07_13 = "07.13"
    VALUE_07_16 = "07.16"
    VALUE_07_17 = "07.17"
    VALUE_07_18 = "07.18"
    VALUE_07_19 = "07.19"
    VALUE_07_20 = "07.20"
    VALUE_07_21 = "07.21"
    VALUE_07_22 = "07.22"
    VALUE_08_01 = "08.01"
    VALUE_08_02 = "08.02"
    VALUE_09_01 = "09.01"
    VALUE_09_02 = "09.02"
    VALUE_09_03 = "09.03"
    VALUE_10_01 = "10.01"
    VALUE_10_02 = "10.02"
    VALUE_10_03 = "10.03"
    VALUE_10_04 = "10.04"
    VALUE_10_05 = "10.05"
    VALUE_10_06 = "10.06"
    VALUE_10_07 = "10.07"
    VALUE_10_08 = "10.08"
    VALUE_10_09 = "10.09"
    VALUE_10_10 = "10.10"
    VALUE_11_01 = "11.01"
    VALUE_11_02 = "11.02"
    VALUE_11_03 = "11.03"
    VALUE_11_04 = "11.04"
    VALUE_12_01 = "12.01"
    VALUE_12_02 = "12.02"
    VALUE_12_03 = "12.03"
    VALUE_12_04 = "12.04"
    VALUE_12_05 = "12.05"
    VALUE_12_06 = "12.06"
    VALUE_12_07 = "12.07"
    VALUE_12_08 = "12.08"
    VALUE_12_09 = "12.09"
    VALUE_12_10 = "12.10"
    VALUE_12_11 = "12.11"
    VALUE_12_12 = "12.12"
    VALUE_12_13 = "12.13"
    VALUE_12_14 = "12.14"
    VALUE_12_15 = "12.15"
    VALUE_12_16 = "12.16"
    VALUE_12_17 = "12.17"
    VALUE_13_02 = "13.02"
    VALUE_13_03 = "13.03"
    VALUE_13_04 = "13.04"
    VALUE_13_05 = "13.05"
    VALUE_14_01 = "14.01"
    VALUE_14_02 = "14.02"
    VALUE_14_03 = "14.03"
    VALUE_14_04 = "14.04"
    VALUE_14_05 = "14.05"
    VALUE_14_06 = "14.06"
    VALUE_14_07 = "14.07"
    VALUE_14_08 = "14.08"
    VALUE_14_09 = "14.09"
    VALUE_14_10 = "14.10"
    VALUE_14_11 = "14.11"
    VALUE_14_12 = "14.12"
    VALUE_14_13 = "14.13"
    VALUE_14_14 = "14.14"
    VALUE_15_01 = "15.01"
    VALUE_15_02 = "15.02"
    VALUE_15_03 = "15.03"
    VALUE_15_04 = "15.04"
    VALUE_15_05 = "15.05"
    VALUE_15_06 = "15.06"
    VALUE_15_07 = "15.07"
    VALUE_15_08 = "15.08"
    VALUE_15_09 = "15.09"
    VALUE_15_10 = "15.10"
    VALUE_15_11 = "15.11"
    VALUE_15_12 = "15.12"
    VALUE_15_13 = "15.13"
    VALUE_15_14 = "15.14"
    VALUE_15_15 = "15.15"
    VALUE_15_16 = "15.16"
    VALUE_15_17 = "15.17"
    VALUE_15_18 = "15.18"
    VALUE_16_01 = "16.01"
    VALUE_16_02 = "16.02"
    VALUE_17_01 = "17.01"
    VALUE_17_02 = "17.02"
    VALUE_17_03 = "17.03"
    VALUE_17_04 = "17.04"
    VALUE_17_05 = "17.05"
    VALUE_17_06 = "17.06"
    VALUE_17_08 = "17.08"
    VALUE_17_09 = "17.09"
    VALUE_17_10 = "17.10"
    VALUE_17_11 = "17.11"
    VALUE_17_12 = "17.12"
    VALUE_17_13 = "17.13"
    VALUE_17_14 = "17.14"
    VALUE_17_15 = "17.15"
    VALUE_17_16 = "17.16"
    VALUE_17_17 = "17.17"
    VALUE_17_18 = "17.18"
    VALUE_17_19 = "17.19"
    VALUE_17_20 = "17.20"
    VALUE_17_21 = "17.21"
    VALUE_17_22 = "17.22"
    VALUE_17_23 = "17.23"
    VALUE_17_24 = "17.24"
    VALUE_17_25 = "17.25"
    VALUE_18_01 = "18.01"
    VALUE_19_01 = "19.01"
    VALUE_20_01 = "20.01"
    VALUE_20_02 = "20.02"
    VALUE_20_03 = "20.03"
    VALUE_21_01 = "21.01"
    VALUE_22_01 = "22.01"
    VALUE_23_01 = "23.01"
    VALUE_24_01 = "24.01"
    VALUE_25_01 = "25.01"
    VALUE_25_02 = "25.02"
    VALUE_25_03 = "25.03"
    VALUE_25_04 = "25.04"
    VALUE_25_05 = "25.05"
    VALUE_26_01 = "26.01"
    VALUE_27_01 = "27.01"
    VALUE_28_01 = "28.01"
    VALUE_29_01 = "29.01"
    VALUE_30_01 = "30.01"
    VALUE_31_01 = "31.01"
    VALUE_32_01 = "32.01"
    VALUE_33_01 = "33.01"
    VALUE_34_01 = "34.01"
    VALUE_35_01 = "35.01"
    VALUE_36_01 = "36.01"
    VALUE_37_01 = "37.01"
    VALUE_38_01 = "38.01"
    VALUE_39_01 = "39.01"
    VALUE_40_01 = "40.01"


class TenderEmiCPais(Enum):
    VALUE_1058 = "1058"


class TenderEmiXPais(Enum):
    BRASIL = "Brasil"
    BRASIL_1 = "BRASIL"


class TenviNfeIndSinc(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class TfinNfe(Enum):
    """
    Tipo Finalidade da NF-e (1=Normal; 2=Complementar; 3=Ajuste;
    4=Devolução/Retorno)
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


@dataclass
class TinfRespTec:
    """
    Grupo de informações do responsável técnico pelo sistema de emissão de
    DF-e.

    :ivar CNPJ: CNPJ
    :ivar xContato: Informar o nome da pessoa a ser contatada na empresa
        desenvolvedora do sistema utilizado na emissão do documento
        fiscal eletrônico.
    :ivar email: Informar o e-mail da pessoa a ser contatada na empresa
        desenvolvedora do sistema.
    :ivar fone: Informar o telefone da pessoa a ser contatada na empresa
        desenvolvedora do sistema. Preencher com o Código DDD + número
        do telefone.
    :ivar idCSRT: Identificador do CSRT utilizado para montar o hash do
        CSRT
    :ivar hashCSRT: O hashCSRT é o resultado da função hash (SHA-1 –
        Base64) do CSRT fornecido pelo fisco mais a Chave de Acesso da
        NFe.
    """
    class Meta:
        name = "TInfRespTec"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{0}|[0-9]{14}",
        }
    )
    xContato: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 6,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{6,14}",
        }
    )
    idCSRT: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{2}",
        }
    )
    hashCSRT: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "length": 20,
            "format": "base64",
        }
    )


class TprocEmi(Enum):
    """
    Tipo processo de emissão da NF-e.
    """
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class Torig(Enum):
    """Tipo Origem da mercadoria CST ICMS  origem da mercadoria: 0-Nacional
    exceto as indicadas nos códigos 3, 4, 5 e 8;

    1-Estrangeira - Importação direta; 2-Estrangeira - Adquirida no mercado interno; 3-Nacional, conteudo superior 40% e inferior ou igual a 70%; 4-Nacional, processos produtivos básicos; 5-Nacional, conteudo inferior 40%; 6-Estrangeira - Importação direta, com similar nacional, lista CAMEX; 7-Estrangeira - mercado interno, sem simular,lista CAMEX;8-Nacional, Conteúdo de Importação superior a 70%.
    """
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"


class ArmaTpArma(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class CardTpIntegra(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


class DestIndIedest(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_9 = "9"


class DetPagIndPag(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class EmitCrt(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class IdeIdDest(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class IdeIndFinal(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class IdeIndIntermed(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class IdeIndPres(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_9 = "9"


class IdeTpEmis(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_9 = "9"


class IdeTpImp(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


class IdeTpNf(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class ProcRefIndProc(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_9 = "9"


class ProdIndEscala(Enum):
    S = "S"
    N = "N"


class ProdIndTot(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class RefEcfMod(Enum):
    VALUE_2_B = "2B"
    VALUE_2_C = "2C"
    VALUE_2_D = "2D"


class RefNfpMod(Enum):
    VALUE_01 = "01"
    VALUE_04 = "04"


class RefNfMod(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"


class TranspModFrete(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_9 = "9"


class VeicProdVin(Enum):
    R = "R"
    N = "N"


class VeicProdCondVeic(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class VeicProdTpOp(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class VeicProdTpRest(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_9 = "9"


@dataclass
class TconsReciNfe:
    """
    Tipo Pedido de Consulta do Recido do Lote de Notas Fiscais Eletrônicas.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar nRec: Número do Recibo
    :ivar versao:
    """
    class Meta:
        name = "TConsReciNFe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    nRec: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "max_length": 15,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[1-9]{1}\.[0-9]{2}",
        }
    )


@dataclass
class TenderEmi:
    """Tipo Dados do Endereço do Emitente  // 24/10/08 - desmembrado / tamanho mínimo

    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município
    :ivar xMun: Nome do município
    :ivar UF: Sigla da UF
    :ivar CEP: CEP - NT 2011/004
    :ivar cPais: Código do país
    :ivar xPais: Nome do país
    :ivar fone: Preencher com Código DDD + número do telefone (v.2.0)
    """
    class Meta:
        name = "TEnderEmi"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    UF: Optional[TufEmi] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    cPais: Optional[TenderEmiCPais] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    xPais: Optional[TenderEmiXPais] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{6,14}",
        }
    )


@dataclass
class Tendereco:
    """Tipo Dados do Endereço  // 24/10/08 - tamanho mínimo

    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar xMun: Nome do município, informar EXTERIOR para operações com
        o exterior.
    :ivar UF: Sigla da UF, informar EX para operações com o exterior.
    :ivar CEP: CEP
    :ivar cPais: Código de Pais
    :ivar xPais: Nome do país
    :ivar fone: Telefone, preencher com Código DDD + número do telefone
        , nas operações com exterior é permtido informar o código do
        país + código da localidade + número do telefone
    """
    class Meta:
        name = "TEndereco"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
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
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    cPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    xPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{6,14}",
        }
    )


@dataclass
class Tipi:
    """Tipo: Dados do IPI

    :ivar CNPJProd: CNPJ do produtor da mercadoria, quando diferente do
        emitente. Somente para os casos de exportação direta ou
        indireta.
    :ivar cSelo: Código do selo de controle do IPI
    :ivar qSelo: Quantidade de selo de controle do IPI
    :ivar cEnq: Código de Enquadramento Legal do IPI (tabela a ser
        criada pela RFB)
    :ivar IPITrib:
    :ivar IPINT:
    """
    class Meta:
        name = "TIpi"

    CNPJProd: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    cSelo: Optional[str] = field(
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
    qSelo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,12}",
        }
    )
    cEnq: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 1,
            "max_length": 3,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    IPITrib: Optional["Tipi.Ipitrib"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    IPINT: Optional["Tipi.Ipint"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )

    @dataclass
    class Ipitrib:
        """
        :ivar CST: Código da Situação Tributária do IPI: 00-Entrada com
            recuperação de crédito 49 - Outras entradas 50-Saída
            tributada 99-Outras saídas
        :ivar vBC: Valor da BC do IPI
        :ivar pIPI: Alíquota do IPI
        :ivar qUnid: Quantidade total na unidade padrão para tributação
        :ivar vUnid: Valor por Unidade Tributável. Informar o valor do
            imposto Pauta por unidade de medida.
        :ivar vIPI: Valor do IPI
        """
        CST: Optional[IpitribCst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
            }
        )
        vBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        pIPI: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
            }
        )
        qUnid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?",
            }
        )
        vUnid: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
            }
        )
        vIPI: Optional[str] = field(
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
    class Ipint:
        """
        :ivar CST: Código da Situação Tributária do IPI: 01-Entrada
            tributada com alíquota zero 02-Entrada isenta 03-Entrada
            não-tributada 04-Entrada imune 05-Entrada com suspensão
            51-Saída tributada com alíquota zero 52-Saída isenta
            53-Saída não-tributada 54-Saída imune 55-Saída com suspensão
        """
        CST: Optional[IpintCst] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
            }
        )


@dataclass
class Tlocal:
    """Tipo Dados do Local de Retirada ou Entrega // 24/10/08 - tamanho mínimo // v2.0

    :ivar CNPJ: CNPJ
    :ivar CPF: CPF (v2.0)
    :ivar xNome: Razão Social ou Nome do Expedidor/Recebedor
    :ivar xLgr: Logradouro
    :ivar nro: Número
    :ivar xCpl: Complemento
    :ivar xBairro: Bairro
    :ivar cMun: Código do município (utilizar a tabela do IBGE)
    :ivar xMun: Nome do município
    :ivar UF: Sigla da UF
    :ivar CEP: CEP
    :ivar cPais: Código de Pais
    :ivar xPais: Nome do país
    :ivar fone: Telefone, preencher com Código DDD + número do telefone
        , nas operações com exterior é permtido informar o código do
        país + código da localidade + número do telefone
    :ivar email: Informar o e-mail do expedidor/Recebedor. O campo pode
        ser utilizado para informar o e-mail de recepção da NF-e
        indicada pelo expedidor
    :ivar IE: Inscrição Estadual (v2.0)
    """
    class Meta:
        name = "TLocal"

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
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    xNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
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
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    cPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    xPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{6,14}",
        }
    )
    email: Optional[str] = field(
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


@dataclass
class TretConsReciNfe:
    """
    Tipo Retorno do Pedido de  Consulta do Recido do Lote de Notas Fiscais
    Eletrônicas.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar verAplic: Versão do Aplicativo que processou a NF-e
    :ivar nRec: Número do Recibo Consultado
    :ivar cStat: Código do status da mensagem enviada.
    :ivar xMotivo: Descrição literal do status do serviço solicitado.
    :ivar cUF: código da UF de atendimento
    :ivar dhRecbto: Data e hora de processamento, no formato AAAA-MM-
        DDTHH:MM:SSTZD. Em caso de Rejeição, com data e hora do
        recebimento do Lote de NF-e enviado.
    :ivar cMsg: Código da Mensagem (v2.0) alterado para tamanho variavel
        1-4. (NT2011/004)
    :ivar xMsg: Mensagem da SEFAZ para o emissor. (v2.0)
    :ivar protNFe: Protocolo de status resultado do processamento da
        NF-e
    :ivar versao:
    """
    class Meta:
        name = "TRetConsReciNFe"

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
    nRec: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "max_length": 15,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
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
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    dhRecbto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    cMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    xMsg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "min_length": 1,
            "max_length": 200,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    protNFe: List[TprotNfe] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "max_occurs": 50,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[1-9]{1}\.[0-9]{2}",
        }
    )


@dataclass
class TretEnviNfe:
    """
    Tipo Retorno do Pedido de Autorização da Nota Fiscal Eletrônica.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar verAplic: Versão do Aplicativo que recebeu o Lote.
    :ivar cStat: Código do status da mensagem enviada.
    :ivar xMotivo: Descrição literal do status do serviço solicitado.
    :ivar cUF: código da UF de atendimento
    :ivar dhRecbto: Data e hora do recebimento, no formato AAAA-MM-
        DDTHH:MM:SSTZD
    :ivar infRec: Dados do Recibo do Lote
    :ivar protNFe: Protocolo de status resultado do processamento
        sincrono da NFC-e
    :ivar versao:
    """
    class Meta:
        name = "TRetEnviNFe"

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
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    dhRecbto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    infRec: Optional["TretEnviNfe.InfRec"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    protNFe: Optional[TprotNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[1-9]{1}\.[0-9]{2}",
        }
    )

    @dataclass
    class InfRec:
        """
        :ivar nRec: Número do Recibo
        :ivar tMed: Tempo médio de resposta do serviço (em segundos) dos
            últimos 5 minutos
        """
        nRec: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "max_length": 15,
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        tMed: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{1,4}",
            }
        )


@dataclass
class Tveiculo:
    """
    Tipo Dados do Veículo.

    :ivar placa: Placa do veículo (NT2011/004)
    :ivar UF: Sigla da UF
    :ivar RNTC: Registro Nacional de Transportador de Carga (ANTT)
    """
    class Meta:
        name = "TVeiculo"

    placa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[A-Z]{2,3}[0-9]{4}|[A-Z]{3,4}[0-9]{3}|[A-Z0-9]{7}",
        }
    )
    UF: Optional[Tuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    RNTC: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class Tnfe:
    """
    Tipo Nota Fiscal Eletrônica.

    :ivar infNFe: Informações da Nota Fiscal eletrônica
    :ivar infNFeSupl: Informações suplementares Nota Fiscal
    :ivar signature:
    """
    class Meta:
        name = "TNFe"

    infNFe: Optional["Tnfe.InfNfe"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    infNFeSupl: Optional["Tnfe.InfNfeSupl"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
    class InfNfe:
        """
        :ivar ide: identificação da NF-e
        :ivar emit: Identificação do emitente
        :ivar avulsa: Emissão de avulsa, informar os dados do Fisco
            emitente
        :ivar dest: Identificação do Destinatário
        :ivar retirada: Identificação do Local de Retirada (informar
            apenas quando for diferente do endereço do remetente)
        :ivar entrega: Identificação do Local de Entrega (informar
            apenas quando for diferente do endereço do destinatário)
        :ivar autXML: Pessoas autorizadas para o download do XML da NF-e
        :ivar det: Dados dos detalhes da NF-e
        :ivar total: Dados dos totais da NF-e
        :ivar transp: Dados dos transportes da NF-e
        :ivar cobr: Dados da cobrança da NF-e
        :ivar pag: Dados de Pagamento. Obrigatório apenas para (NFC-e)
            NT 2012/004
        :ivar infIntermed: Grupo de Informações do Intermediador da
            Transação
        :ivar infAdic: Informações adicionais da NF-e
        :ivar exporta: Informações de exportação
        :ivar compra: Informações de compras  (Nota de Empenho, Pedido e
            Contrato)
        :ivar cana: Informações de registro aquisições de cana
        :ivar infRespTec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar infSolicNFF: Grupo para informações da solicitação da NFF
        :ivar versao: Versão do leiaute (v4.00)
        :ivar Id: PL_005d - 11/08/09 - validação do Id
        """
        ide: Optional["Tnfe.InfNfe.Ide"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        emit: Optional["Tnfe.InfNfe.Emit"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        avulsa: Optional["Tnfe.InfNfe.Avulsa"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        dest: Optional["Tnfe.InfNfe.Dest"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        retirada: Optional[Tlocal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        entrega: Optional[Tlocal] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        autXML: List["Tnfe.InfNfe.AutXml"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_occurs": 10,
            }
        )
        det: List["Tnfe.InfNfe.Det"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "min_occurs": 1,
                "max_occurs": 990,
            }
        )
        total: Optional["Tnfe.InfNfe.Total"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        transp: Optional["Tnfe.InfNfe.Transp"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        cobr: Optional["Tnfe.InfNfe.Cobr"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        pag: Optional["Tnfe.InfNfe.Pag"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        infIntermed: Optional["Tnfe.InfNfe.InfIntermed"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        infAdic: Optional["Tnfe.InfNfe.InfAdic"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        exporta: Optional["Tnfe.InfNfe.Exporta"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        compra: Optional["Tnfe.InfNfe.Compra"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        cana: Optional["Tnfe.InfNfe.Cana"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        infRespTec: Optional[TinfRespTec] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        infSolicNFF: Optional["Tnfe.InfNfe.InfSolicNff"] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        versao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}\.[0-9]{2}",
            }
        )
        Id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"NFe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar cUF: Código da UF do emitente do Documento Fiscal.
                Utilizar a Tabela do IBGE.
            :ivar cNF: Código numérico que compõe a Chave de Acesso.
                Número aleatório gerado pelo emitente para cada NF-e.
            :ivar natOp: Descrição da Natureza da Operação
            :ivar mod: Código do modelo do Documento Fiscal. 55 = NF-e;
                65 = NFC-e.
            :ivar serie: Série do Documento Fiscal série normal 0-889
                Avulsa Fisco 890-899 SCAN 900-999
            :ivar nNF: Número do Documento Fiscal
            :ivar dhEmi: Data e Hora de emissão do Documento Fiscal
                (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00
            :ivar dhSaiEnt: Data e Hora da saída ou de entrada da
                mercadoria / produto (AAAA-MM-DDTHH:mm:ssTZD)
            :ivar tpNF: Tipo do Documento Fiscal (0 - entrada; 1 -
                saída)
            :ivar idDest: Identificador de Local de destino da operação
                (1-Interna;2-Interestadual;3-Exterior)
            :ivar cMunFG: Código do Município de Ocorrência do Fato
                Gerador (utilizar a tabela do IBGE)
            :ivar tpImp: Formato de impressão do DANFE (0-sem
                DANFE;1-DANFe Retrato; 2-DANFe Paisagem;3-DANFe
                Simplificado; 4-DANFe NFC-e;5-DANFe NFC-e em mensagem
                eletrônica)
            :ivar tpEmis: Forma de emissão da NF-e 1 - Normal; 2 -
                Contingência FS 3 - Regime Especial NFF (NT 2021.002) 4
                - Contingência DPEC 5 - Contingência FSDA 6 -
                Contingência SVC - AN 7 - Contingência SVC - RS 9 -
                Contingência off-line NFC-e
            :ivar cDV: Digito Verificador da Chave de Acesso da NF-e
            :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
                Homologação
            :ivar finNFe: Finalidade da emissão da NF-e: 1 - NFe normal
                2 - NFe complementar 3 - NFe de ajuste 4 -
                Devolução/Retorno
            :ivar indFinal: Indica operação com consumidor final
                (0-Não;1-Consumidor Final)
            :ivar indPres: Indicador de presença do comprador no
                estabelecimento comercial no momento da oepração (0-Não
                se aplica (ex.: Nota Fiscal complementar ou de
                ajuste;1-Operação presencial;2-Não presencial,
                internet;3-Não presencial, teleatendimento;4-NFC-e
                entrega em domicílio;5-Operação presencial, fora do
                estabelecimento;9-Não presencial, outros)
            :ivar indIntermed: Indicador de intermediador/marketplace
                0=Operação sem intermediador (em site ou plataforma
                própria) 1=Operação em site ou plataforma de terceiros
                (intermediadores/marketplace)
            :ivar procEmi: Processo de emissão utilizado com a seguinte
                codificação: 0 - emissão de NF-e com aplicativo do
                contribuinte; 1 - emissão de NF-e avulsa pelo Fisco; 2 -
                emissão de NF-e avulsa, pelo contribuinte com seu
                certificado digital, através do site do Fisco; 3-
                emissão de NF-e pelo contribuinte com aplicativo
                fornecido pelo Fisco.
            :ivar verProc: versão do aplicativo utilizado no processo de
                emissão
            :ivar dhCont: Informar a data e hora de entrada em
                contingência contingência no formato  (AAAA-MM-
                DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00.
            :ivar xJust: Informar a Justificativa da entrada
            :ivar NFref: Grupo de infromações da NF referenciada
            """
            cUF: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            cNF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            natOp: Optional[str] = field(
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
            mod: Optional[Tmod] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            serie: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                }
            )
            nNF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,8}",
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
            dhSaiEnt: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tpNF: Optional[IdeTpNf] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            idDest: Optional[IdeIdDest] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            cMunFG: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            tpImp: Optional[IdeTpImp] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tpEmis: Optional[IdeTpEmis] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            cDV: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{1}",
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
            finNFe: Optional[TfinNfe] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            indFinal: Optional[IdeIndFinal] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            indPres: Optional[IdeIndPres] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            indIntermed: Optional[IdeIndIntermed] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                }
            )
            procEmi: Optional[TprocEmi] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            verProc: Optional[str] = field(
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
            dhCont: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            xJust: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 15,
                    "max_length": 256,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            NFref: List["Tnfe.InfNfe.Ide.Nfref"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_occurs": 500,
                }
            )

            @dataclass
            class Nfref:
                """
                :ivar refNFe: Chave de acesso das NF-e referenciadas.
                    Chave de acesso compostas por Código da UF (tabela
                    do IBGE) + AAMM da emissão + CNPJ do Emitente +
                    modelo, série e número da NF-e Referenciada + Código
                    Numérico + DV.
                :ivar refNF: Dados da NF modelo 1/1A referenciada ou NF
                    modelo 2 referenciada
                :ivar refNFP: Grupo com as informações NF de produtor
                    referenciada
                :ivar refCTe: Utilizar esta TAG para referenciar um CT-e
                    emitido anteriormente, vinculada a NF-e atual
                :ivar refECF: Grupo do Cupom Fiscal vinculado à NF-e
                """
                refNFe: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_length": 44,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{44}",
                    }
                )
                refNF: Optional["Tnfe.InfNfe.Ide.Nfref.RefNf"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                refNFP: Optional["Tnfe.InfNfe.Ide.Nfref.RefNfp"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                refCTe: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_length": 44,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{44}",
                    }
                )
                refECF: Optional["Tnfe.InfNfe.Ide.Nfref.RefEcf"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )

                @dataclass
                class RefNf:
                    """
                    :ivar cUF: Código da UF do emitente do Documento
                        Fiscal. Utilizar a Tabela do IBGE.
                    :ivar AAMM: AAMM da emissão
                    :ivar CNPJ: CNPJ do emitente do documento fiscal
                        referenciado
                    :ivar mod: Código do modelo do Documento Fiscal.
                        Utilizar 01 para NF modelo 1/1A e 02 para NF
                        modelo 02
                    :ivar serie: Série do Documento Fiscal, informar
                        zero se inexistente
                    :ivar nNF: Número do Documento Fiscal
                    """
                    cUF: Optional[TcodUfIbge] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                        }
                    )
                    AAMM: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{2}[0]{1}[1-9]{1}|[0-9]{2}[1]{1}[0-2]{1}",
                        }
                    )
                    CNPJ: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "max_length": 14,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{14}",
                        }
                    )
                    mod: Optional[RefNfMod] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    serie: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                        }
                    )
                    nNF: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[1-9]{1}[0-9]{0,8}",
                        }
                    )

                @dataclass
                class RefNfp:
                    """
                    :ivar cUF: Código da UF do emitente do Documento
                        FiscalUtilizar a Tabela do IBGE (Anexo IV -
                        Tabela de UF, Município e País)
                    :ivar AAMM: AAMM da emissão da NF de produtor
                    :ivar CNPJ: CNPJ do emitente da NF de produtor
                    :ivar CPF: CPF do emitente da NF de produtor
                    :ivar IE: IE do emitente da NF de Produtor
                    :ivar mod: Código do modelo do Documento Fiscal -
                        utilizar 04 para NF de produtor  ou 01 para NF
                        Avulsa
                    :ivar serie: Série do Documento Fiscal, informar
                        zero se inexistentesérie
                    :ivar nNF: Número do Documento Fiscal - 1 –
                        999999999
                    """
                    cUF: Optional[TcodUfIbge] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                        }
                    )
                    AAMM: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{2}[0]{1}[1-9]{1}|[0-9]{2}[1]{1}[0-2]{1}",
                        }
                    )
                    CNPJ: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "max_length": 14,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{14}",
                        }
                    )
                    CPF: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "max_length": 11,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{11}",
                        }
                    )
                    IE: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "max_length": 14,
                            "white_space": "preserve",
                            "pattern": r"ISENTO|[0-9]{2,14}",
                        }
                    )
                    mod: Optional[RefNfpMod] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    serie: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|[1-9]{1}[0-9]{0,2}",
                        }
                    )
                    nNF: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[1-9]{1}[0-9]{0,8}",
                        }
                    )

                @dataclass
                class RefEcf:
                    """
                    :ivar mod: Código do modelo do Documento Fiscal
                        Preencher com "2B", quando se tratar de Cupom
                        Fiscal emitido por máquina registradora (não
                        ECF), com "2C", quando se tratar de Cupom Fiscal
                        PDV, ou "2D", quando se tratar de Cupom Fiscal
                        (emitido por ECF)
                    :ivar nECF: Informar o número de ordem seqüencial do
                        ECF que emitiu o Cupom Fiscal vinculado à NF-e
                    :ivar nCOO: Informar o Número do Contador de Ordem
                        de Operação - COO vinculado à NF-e
                    """
                    mod: Optional[RefEcfMod] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    nECF: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,3}",
                        }
                    )
                    nCOO: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,6}",
                        }
                    )

        @dataclass
        class Emit:
            """
            :ivar CNPJ: Número do CNPJ do emitente
            :ivar CPF: Número do CPF do emitente
            :ivar xNome: Razão Social ou Nome do emitente
            :ivar xFant: Nome fantasia
            :ivar enderEmit: Endereço do emitente
            :ivar IE: Inscrição Estadual do Emitente
            :ivar IEST: Inscricao Estadual do Substituto Tributário
            :ivar IM: Inscrição Municipal
            :ivar CNAE: CNAE Fiscal
            :ivar CRT: Código de Regime Tributário. Este campo será
                obrigatoriamente preenchido com: 1 – Simples Nacional; 2
                – Simples Nacional – excesso de sublimite de receita
                bruta; 3 – Regime Normal.
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 11,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            enderEmit: Optional[TenderEmi] = field(
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
                    "required": True,
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}|ISENTO",
                }
            )
            IEST: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            IM: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            CRT: Optional[EmitCrt] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )

        @dataclass
        class Avulsa:
            """
            :ivar CNPJ: CNPJ do Órgão emissor
            :ivar xOrgao: Órgão emitente
            :ivar matr: Matrícula do agente
            :ivar xAgente: Nome do agente
            :ivar fone: Telefone
            :ivar UF: Sigla da Unidade da Federação
            :ivar nDAR: Número do Documento de Arrecadação de Receita
            :ivar dEmi: Data de emissão do DAR (AAAA-MM-DD)
            :ivar vDAR: Valor Total constante no DAR
            :ivar repEmi: Repartição Fiscal emitente
            :ivar dPag: Data de pagamento do DAR (AAAA-MM-DD)
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            xOrgao: Optional[str] = field(
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
            matr: Optional[str] = field(
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
            xAgente: Optional[str] = field(
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
            fone: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6,14}",
                }
            )
            UF: Optional[TufEmi] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            nDAR: Optional[str] = field(
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
            dEmi: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            vDAR: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            repEmi: Optional[str] = field(
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
            dPag: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )

        @dataclass
        class Dest:
            """
            :ivar CNPJ: Número do CNPJ
            :ivar CPF: Número do CPF
            :ivar idEstrangeiro: Identificador do destinatário, em caso
                de comprador estrangeiro
            :ivar xNome: Razão Social ou nome do destinatário
            :ivar enderDest: Dados do endereço
            :ivar indIEDest: Indicador da IE do destinatário: 1 –
                Contribuinte ICMSpagamento à vista; 2 – Contribuinte
                isento de inscrição; 9 – Não Contribuinte
            :ivar IE: Inscrição Estadual (obrigatório nas operações com
                contribuintes do ICMS)
            :ivar ISUF: Inscrição na SUFRAMA (Obrigatório nas operações
                com as áreas com benefícios de incentivos fiscais sob
                controle da SUFRAMA) PL_005d - 11/08/09 - alterado para
                aceitar 8 ou 9 dígitos
            :ivar IM: Inscrição Municipal do tomador do serviço
            :ivar email: Informar o e-mail do destinatário. O campo pode
                ser utilizado para informar o e-mail de recepção da NF-e
                indicada pelo destinatário
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 11,
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
            xNome: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            enderDest: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            indIEDest: Optional[DestIndIedest] = field(
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
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            ISUF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8,9}",
                }
            )
            IM: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 15,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            email: Optional[str] = field(
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

        @dataclass
        class AutXml:
            """
            :ivar CNPJ: CNPJ Autorizado
            :ivar CPF: CPF Autorizado
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            CPF: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 11,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )

        @dataclass
        class Det:
            """
            :ivar prod: Dados dos produtos e serviços da NF-e
            :ivar imposto: Tributos incidentes nos produtos ou serviços
                da NF-e
            :ivar impostoDevol:
            :ivar infAdProd: Informações adicionais do produto (norma
                referenciada, informações complementares, etc)
            :ivar nItem: Número do item do NF
            """
            prod: Optional["Tnfe.InfNfe.Det.Prod"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            imposto: Optional["Tnfe.InfNfe.Det.Imposto"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            impostoDevol: Optional["Tnfe.InfNfe.Det.ImpostoDevol"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            infAdProd: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 500,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            nItem: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,1}|[1-8]{1}[0-9]{2}|[9]{1}[0-8]{1}[0-9]{1}|[9]{1}[9]{1}[0]{1}",
                }
            )

            @dataclass
            class Prod:
                """
                :ivar cProd: Código do produto ou serviço. Preencher com
                    CFOP caso se trate de itens não relacionados com
                    mercadorias/produto e que o contribuinte não possua
                    codificação própria Formato ”CFOP9999”.
                :ivar cEAN: GTIN (Global Trade Item Number) do produto,
                    antigo código EAN ou código de barras
                :ivar cBarra: Codigo de barras diferente do padrão GTIN
                :ivar xProd: Descrição do produto ou serviço
                :ivar NCM: Código NCM (8 posições), será permitida a
                    informação do gênero (posição do capítulo do NCM)
                    quando a operação não for de comércio exterior
                    (importação/exportação) ou o produto não seja
                    tributado pelo IPI. Em caso de item de serviço ou
                    item que não tenham produto (Ex. transferência de
                    crédito, crédito do ativo imobilizado, etc.),
                    informar o código 00 (zeros) (v2.0)
                :ivar NVE: Nomenclatura de Valor aduaneio e Estatístico
                :ivar CEST: Codigo especificador da Substuicao
                    Tributaria - CEST, que identifica a mercadoria
                    sujeita aos regimes de  substituicao tributária e de
                    antecipação do recolhimento  do imposto
                :ivar indEscala:
                :ivar CNPJFab: CNPJ do Fabricante da Mercadoria,
                    obrigatório para produto em escala NÃO relevante.
                :ivar cBenef:
                :ivar EXTIPI: Código EX TIPI (3 posições)
                :ivar CFOP: Cfop
                :ivar uCom: Unidade comercial
                :ivar qCom: Quantidade Comercial  do produto, alterado
                    para aceitar de 0 a 4 casas decimais e 11 inteiros.
                :ivar vUnCom: Valor unitário de comercialização  -
                    alterado para aceitar 0 a 10 casas decimais e 11
                    inteiros
                :ivar vProd: Valor bruto do produto ou serviço.
                :ivar cEANTrib: GTIN (Global Trade Item Number) da
                    unidade tributável, antigo código EAN ou código de
                    barras
                :ivar cBarraTrib: Código de barras da unidade tributável
                    diferente do padrão GTIN
                :ivar uTrib: Unidade Tributável
                :ivar qTrib: Quantidade Tributável - alterado para
                    aceitar de 0 a 4 casas decimais e 11 inteiros
                :ivar vUnTrib: Valor unitário de tributação - - alterado
                    para aceitar 0 a 10 casas decimais e 11 inteiros
                :ivar vFrete: Valor Total do Frete
                :ivar vSeg: Valor Total do Seguro
                :ivar vDesc: Valor do Desconto
                :ivar vOutro: Outras despesas acessórias
                :ivar indTot: Este campo deverá ser preenchido com: 0 –
                    o valor do item (vProd) não compõe o valor total da
                    NF-e (vProd) 1  – o valor do item (vProd) compõe o
                    valor total da NF-e (vProd)
                :ivar DI: Delcaração de Importação (NT 2011/004)
                :ivar detExport: Detalhe da exportação
                :ivar xPed: pedido de compra - Informação de interesse
                    do emissor para controle do B2B.
                :ivar nItemPed: Número do Item do Pedido de Compra -
                    Identificação do número do item do pedido de Compra
                :ivar nFCI: Número de controle da FCI - Ficha de
                    Conteúdo de Importação.
                :ivar rastro:
                :ivar infProdNFF: Informações mais detalhadas do produto
                    (usada na NFF)
                :ivar infProdEmb: Informações mais detalhadas do produto
                    (usada na NFF)
                :ivar veicProd: Veículos novos
                :ivar med: grupo do detalhamento de Medicamentos e de
                    matérias-primas farmacêuticas
                :ivar arma: Armamentos
                :ivar comb: Informar apenas para operações com
                    combustíveis líquidos
                :ivar nRECOPI: Número do RECOPI
                """
                cProd: Optional[str] = field(
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
                cEAN: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"SEM GTIN|[0-9]{0}|[0-9]{8}|[0-9]{12,14}",
                    }
                )
                cBarra: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "min_length": 3,
                        "max_length": 30,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                xProd: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 120,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                NCM: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{2}|[0-9]{8}",
                    }
                )
                NVE: List[str] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_occurs": 8,
                        "white_space": "preserve",
                        "pattern": r"[A-Z]{2}[0-9]{4}",
                    }
                )
                CEST: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7}",
                    }
                )
                indEscala: Optional[ProdIndEscala] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                CNPJFab: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_length": 14,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{14}",
                    }
                )
                cBenef: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"([!-ÿ]{8}|[!-ÿ]{10}|SEM CBENEF)?",
                    }
                )
                EXTIPI: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{2,3}",
                    }
                )
                CFOP: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[1,2,3,5,6,7]{1}[0-9]{3}",
                    }
                )
                uCom: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 6,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                qCom: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?",
                    }
                )
                vUnCom: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?",
                    }
                )
                vProd: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                cEANTrib: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"SEM GTIN|[0-9]{0}|[0-9]{8}|[0-9]{12,14}",
                    }
                )
                cBarraTrib: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "min_length": 3,
                        "max_length": 30,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                uTrib: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 6,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                qTrib: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?",
                    }
                )
                vUnTrib: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?",
                    }
                )
                vFrete: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vSeg: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vDesc: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vOutro: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                indTot: Optional[ProdIndTot] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                DI: List["Tnfe.InfNfe.Det.Prod.Di"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_occurs": 100,
                    }
                )
                detExport: List["Tnfe.InfNfe.Det.Prod.DetExport"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_occurs": 500,
                    }
                )
                xPed: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "min_length": 1,
                        "max_length": 15,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                nItemPed: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,6}",
                    }
                )
                nFCI: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"[A-F0-9]{8}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{4}-[A-F0-9]{12}",
                    }
                )
                rastro: List["Tnfe.InfNfe.Det.Prod.Rastro"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_occurs": 500,
                    }
                )
                infProdNFF: Optional["Tnfe.InfNfe.Det.Prod.InfProdNff"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                infProdEmb: Optional["Tnfe.InfNfe.Det.Prod.InfProdEmb"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                veicProd: Optional["Tnfe.InfNfe.Det.Prod.VeicProd"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                med: Optional["Tnfe.InfNfe.Det.Prod.Med"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                arma: List["Tnfe.InfNfe.Det.Prod.Arma"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_occurs": 500,
                    }
                )
                comb: Optional["Tnfe.InfNfe.Det.Prod.Comb"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                nRECOPI: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_length": 20,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{20}",
                    }
                )

                @dataclass
                class Di:
                    """
                    :ivar nDI: Numero do Documento de Importação
                        DI/DSI/DA/DRI-E (DI/DSI/DA/DRI-E) (NT2011/004)
                    :ivar dDI: Data de registro da DI/DSI/DA (AAAA-MM-
                        DD)
                    :ivar xLocDesemb: Local do desembaraço aduaneiro
                    :ivar UFDesemb: UF onde ocorreu o desembaraço
                        aduaneiro
                    :ivar dDesemb: Data do desembaraço aduaneiro (AAAA-
                        MM-DD)
                    :ivar tpViaTransp: Via de transporte internacional
                        informada na DI
                        1-Maritima;2-Fluvial;3-Lacustre;4-Aerea;5-Postal;6-Ferroviaria;7-Rodoviaria;8-Conduto;9-Meios
                        Proprios;10-Entrada/Saida Ficta;
                        11-Courier;12-Em maos;13-Por reboque.
                    :ivar vAFRMM: Valor Adicional ao frete para
                        renovação de marinha mercante
                    :ivar tpIntermedio: Forma de Importação quanto a
                        intermediação 1-por conta propria;2-por conta e
                        ordem;3-encomenda
                    :ivar CNPJ: CNPJ do adquirente ou do encomendante
                    :ivar UFTerceiro: Sigla da UF do adquirente ou do
                        encomendante
                    :ivar cExportador: Código do exportador (usado nos
                        sistemas internos de informação do emitente da
                        NF-e)
                    :ivar adi: Adições (NT 2011/004)
                    """
                    nDI: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 15,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    dDI: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    xLocDesemb: Optional[str] = field(
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
                    UFDesemb: Optional[TufEmi] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                        }
                    )
                    dDesemb: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    tpViaTransp: Optional[DiTpViaTransp] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    vAFRMM: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    tpIntermedio: Optional[DiTpIntermedio] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    CNPJ: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "max_length": 14,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{14}",
                        }
                    )
                    UFTerceiro: Optional[TufEmi] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    cExportador: Optional[str] = field(
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
                    adi: List["Tnfe.InfNfe.Det.Prod.Di.Adi"] = field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "min_occurs": 1,
                            "max_occurs": 999,
                        }
                    )

                    @dataclass
                    class Adi:
                        """
                        :ivar nAdicao: Número da Adição
                        :ivar nSeqAdic: Número seqüencial do item dentro
                            da Adição
                        :ivar cFabricante: Código do fabricante
                            estrangeiro (usado nos sistemas internos de
                            informação do emitente da NF-e)
                        :ivar vDescDI: Valor do desconto do item da DI –
                            adição
                        :ivar nDraw: Número do ato concessório de
                            Drawback
                        """
                        nAdicao: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"[1-9]{1}[0-9]{0,2}",
                            }
                        )
                        nSeqAdic: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[1-9]{1}[0-9]{0,4}",
                            }
                        )
                        cFabricante: Optional[str] = field(
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
                        vDescDI: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        nDraw: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "min_length": 1,
                                "max_length": 20,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )

                @dataclass
                class DetExport:
                    """
                    :ivar nDraw: Número do ato concessório de Drawback
                    :ivar exportInd: Exportação indireta
                    """
                    nDraw: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "min_length": 1,
                            "max_length": 20,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    exportInd: Optional["Tnfe.InfNfe.Det.Prod.DetExport.ExportInd"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )

                    @dataclass
                    class ExportInd:
                        """
                        :ivar nRE: Registro de exportação
                        :ivar chNFe: Chave de acesso da NF-e recebida
                            para exportação
                        :ivar qExport: Quantidade do item efetivamente
                            exportado
                        """
                        nRE: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{0,12}",
                            }
                        )
                        chNFe: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "max_length": 44,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{44}",
                            }
                        )
                        qExport: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?",
                            }
                        )

                @dataclass
                class Rastro:
                    """
                    :ivar nLote: Número do lote do produto.
                    :ivar qLote: Quantidade de produto no lote.
                    :ivar dFab: Data de fabricação/produção. Formato
                        "AAAA-MM-DD".
                    :ivar dVal: Data de validade. Informar o último dia
                        do mês caso a validade não especifique o dia.
                        Formato "AAAA-MM-DD".
                    :ivar cAgreg:
                    """
                    nLote: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 20,
                        }
                    )
                    qLote: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,7}(\.[0-9]{1,3})?",
                        }
                    )
                    dFab: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    dVal: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    cAgreg: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "min_length": 1,
                            "max_length": 20,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )

                @dataclass
                class InfProdNff:
                    """
                    :ivar cProdFisco: Código Fiscal do Produto
                    :ivar cOperNFF: Código da operação selecionada na
                        NFF e relacionada ao item
                    """
                    cProdFisco: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "length": 14,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    cOperNFF: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,5}",
                        }
                    )

                @dataclass
                class InfProdEmb:
                    """
                    :ivar xEmb: Embalagem do produto
                    :ivar qVolEmb: Volume do produto na embalagem
                    :ivar uEmb: Unidade de Medida da Embalagem
                    """
                    xEmb: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 8,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    qVolEmb: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,7}(\.[0-9]{1,3})?",
                        }
                    )
                    uEmb: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 8,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )

                @dataclass
                class VeicProd:
                    """
                    :ivar tpOp: Tipo da Operação (1 - Venda
                        concessionária; 2 - Faturamento direto; 3 -
                        Venda direta; 0 - Outros)
                    :ivar chassi: Chassi do veículo - VIN (código-
                        identificação-veículo)
                    :ivar cCor: Cor do veículo (código de cada
                        montadora)
                    :ivar xCor: Descrição da cor
                    :ivar pot: Potência máxima do motor do veículo em
                        cavalo vapor (CV). (potência-veículo)
                    :ivar cilin: Capacidade voluntária do motor expressa
                        em centímetros cúbicos (CC). (cilindradas)
                    :ivar pesoL: Peso líquido
                    :ivar pesoB: Peso bruto
                    :ivar nSerie: Serial (série)
                    :ivar tpComb: Tipo de combustível-Tabela RENAVAM:
                        01-Álcool; 02-Gasolina; 03-Diesel;
                        16-Álcool/Gas.; 17-Gas./Álcool/GNV;
                        18-Gasolina/Elétrico
                    :ivar nMotor: Número do motor
                    :ivar CMT: CMT-Capacidade Máxima de Tração - em
                        Toneladas 4 casas decimais
                    :ivar dist: Distância entre eixos
                    :ivar anoMod: Ano Modelo de Fabricação
                    :ivar anoFab: Ano de Fabricação
                    :ivar tpPint: Tipo de pintura
                    :ivar tpVeic: Tipo de veículo (utilizar tabela
                        RENAVAM)
                    :ivar espVeic: Espécie de veículo (utilizar tabela
                        RENAVAM)
                    :ivar VIN: Informa-se o veículo tem VIN (chassi)
                        remarcado. R-Remarcado N-NormalVIN
                    :ivar condVeic: Condição do veículo (1 - acabado; 2
                        - inacabado; 3 - semi-acabado)
                    :ivar cMod: Código Marca Modelo (utilizar tabela
                        RENAVAM)
                    :ivar cCorDENATRAN: Código da Cor Segundo as regras
                        de pré-cadastro do DENATRAN:
                        01-AMARELO;02-AZUL;03-BEGE;04-BRANCA;05-CINZA;06-DOURADA;07-GRENA
                        08-LARANJA;09-MARROM;10-PRATA;11-PRETA;12-ROSA;13-ROXA;14-VERDE;15-VERMELHA;16-FANTASIA
                    :ivar lota: Quantidade máxima de permitida de
                        passageiros sentados, inclusive motorista.
                    :ivar tpRest: Restrição 0 - Não há; 1 - Alienação
                        Fiduciária; 2 - Arrendamento Mercantil; 3 -
                        Reserva de Domínio; 4 - Penhor de Veículos; 9 -
                        outras.
                    """
                    tpOp: Optional[VeicProdTpOp] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    chassi: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 40,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    pot: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 4,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    cilin: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 4,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    pesoL: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 9,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    pesoB: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 9,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    nSerie: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 9,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    tpComb: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 2,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    nMotor: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 21,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    CMT: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 9,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    dist: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 4,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    anoMod: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{4}",
                        }
                    )
                    anoFab: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{4}",
                        }
                    )
                    tpPint: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "length": 1,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    tpVeic: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,2}",
                        }
                    )
                    espVeic: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1}",
                        }
                    )
                    VIN: Optional[VeicProdVin] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "length": 1,
                        }
                    )
                    condVeic: Optional[VeicProdCondVeic] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    cMod: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,6}",
                        }
                    )
                    cCorDENATRAN: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 2,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,2}",
                        }
                    )
                    lota: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 3,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,3}",
                        }
                    )
                    tpRest: Optional[VeicProdTpRest] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )

                @dataclass
                class Med:
                    """
                    :ivar cProdANVISA: Utilizar o número do registro
                        ANVISA  ou preencher com o literal “ISENTO”, no
                        caso de medicamento isento de registro na
                        ANVISA.
                    :ivar xMotivoIsencao: Obs.: Para medicamento isento
                        de registro na ANVISA, informar o número da
                        decisão que o isenta, como por exemplo o número
                        da Resolução da Diretoria Colegiada da ANVISA
                        (RDC).
                    :ivar vPMC: Preço Máximo ao Consumidor.
                    """
                    cProdANVISA: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{13}|ISENTO",
                        }
                    )
                    xMotivoIsencao: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "min_length": 1,
                            "max_length": 255,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    vPMC: Optional[str] = field(
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
                class Arma:
                    """
                    :ivar tpArma: Indicador do tipo de arma de fogo (0 -
                        Uso permitido; 1 - Uso restrito)
                    :ivar nSerie: Número de série da arma
                    :ivar nCano: Número de série do cano
                    :ivar descr: Descrição completa da arma,
                        compreendendo: calibre, marca, capacidade, tipo
                        de funcionamento, comprimento e demais elementos
                        que permitam a sua perfeita identificação.
                    """
                    tpArma: Optional[ArmaTpArma] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    nSerie: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 15,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    nCano: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 15,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    descr: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 256,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )

                @dataclass
                class Comb:
                    """
                    :ivar cProdANP: Código de produto da ANP.
                        codificação de produtos do SIMP
                        (http://www.anp.gov.br)
                    :ivar descANP: Descrição do Produto conforme ANP.
                        Utilizar a descrição de produtos do Sistema de
                        Informações de Movimentação de Produtos - SIMP
                        (http://www.anp.gov.br/simp/).
                    :ivar pGLP: Percentual do GLP derivado do petróleo
                        no produto GLP (cProdANP=210203001). Informar em
                        número decimal o percentual do GLP derivado de
                        petróleo no produto GLP. Valores 0 a 100.
                    :ivar pGNn: Percentual de gás natural nacional -
                        GLGNn para o produto GLP (cProdANP=210203001).
                        Informar em número decimal o percentual do Gás
                        Natural Nacional - GLGNn para o produto GLP.
                        Valores de 0 a 100.
                    :ivar pGNi: Percentual de gás natural importado
                        GLGNi para o produto GLP (cProdANP=210203001).
                        Informar em número deciaml o percentual do Gás
                        Natural Importado - GLGNi para o produto GLP.
                        Valores de 0 a 100.
                    :ivar vPart: Valor de partida (cProdANP=210203001).
                        Deve ser informado neste campo o valor por
                        quilograma sem ICMS.
                    :ivar CODIF: Código de autorização / registro do
                        CODIF. Informar apenas quando a UF utilizar o
                        CODIF (Sistema de Controle do
                        Diferimento do Imposto nas Operações com AEAC -
                        Álcool Etílico Anidro Combustível).
                    :ivar qTemp: Quantidade de combustível faturada à
                        temperatura ambiente. Informar quando a
                        quantidade faturada informada no campo qCom
                        (I10) tiver sido ajustada para uma temperatura
                        diferente da ambiente.
                    :ivar UFCons: Sigla da UF de Consumo
                    :ivar CIDE: CIDE Combustíveis
                    :ivar encerrante: Informações do grupo de
                        "encerrante"
                    """
                    cProdANP: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{9}",
                        }
                    )
                    descANP: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 2,
                            "max_length": 95,
                        }
                    )
                    pGLP: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0(\.[0-9]{2,4})?|[1-9]{1}[0-9]{0,1}(\.[0-9]{2,4})?|100(\.0{2,4})?",
                        }
                    )
                    pGNn: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0(\.[0-9]{2,4})?|[1-9]{1}[0-9]{0,1}(\.[0-9]{2,4})?|100(\.0{2,4})?",
                        }
                    )
                    pGNi: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0(\.[0-9]{2,4})?|[1-9]{1}[0-9]{0,1}(\.[0-9]{2,4})?|100(\.0{2,4})?",
                        }
                    )
                    vPart: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    CODIF: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,21}",
                        }
                    )
                    qTemp: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}|0\.[0-9]{2}[1-9]{1}[0-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{2}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?",
                        }
                    )
                    UFCons: Optional[Tuf] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                        }
                    )
                    CIDE: Optional["Tnfe.InfNfe.Det.Prod.Comb.Cide"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    encerrante: Optional["Tnfe.InfNfe.Det.Prod.Comb.Encerrante"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )

                    @dataclass
                    class Cide:
                        """
                        :ivar qBCProd: BC do CIDE ( Quantidade
                            comercializada)
                        :ivar vAliqProd: Alíquota do CIDE  (em reais)
                        :ivar vCIDE: Valor do CIDE
                        """
                        qBCProd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?",
                            }
                        )
                        vAliqProd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                            }
                        )
                        vCIDE: Optional[str] = field(
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
                    class Encerrante:
                        """
                        :ivar nBico: Numero de identificação do Bico
                            utilizado no abastecimento
                        :ivar nBomba: Numero de identificação da bomba
                            ao qual o bico está interligado
                        :ivar nTanque: Numero de identificação do tanque
                            ao qual o bico está interligado
                        :ivar vEncIni: Valor do Encerrante no ínicio do
                            abastecimento
                        :ivar vEncFin: Valor do Encerrante no final do
                            abastecimento
                        """
                        nBico: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{1,3}",
                            }
                        )
                        nBomba: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"[0-9]{1,3}",
                            }
                        )
                        nTanque: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{1,3}",
                            }
                        )
                        vEncIni: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?",
                            }
                        )
                        vEncFin: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?",
                            }
                        )

            @dataclass
            class Imposto:
                """
                :ivar vTotTrib: Valor estimado total de impostos
                    federais, estaduais e municipais
                :ivar ICMS: Dados do ICMS Normal e ST
                :ivar IPI:
                :ivar II: Dados do Imposto de Importação
                :ivar ISSQN: ISSQN
                :ivar PIS: Dados do PIS
                :ivar PISST: Dados do PIS Substituição Tributária
                :ivar COFINS: Dados do COFINS
                :ivar COFINSST: Dados do COFINS da Substituição
                    Tributaria;
                :ivar ICMSUFDest: Grupo a ser informado nas vendas
                    interestarduais para consumidor final, não
                    contribuinte de ICMS
                """
                vTotTrib: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                ICMS: Optional["Tnfe.InfNfe.Det.Imposto.Icms"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                IPI: List[Tipi] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_occurs": 2,
                    }
                )
                II: Optional["Tnfe.InfNfe.Det.Imposto.Ii"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                ISSQN: Optional["Tnfe.InfNfe.Det.Imposto.Issqn"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                PIS: Optional["Tnfe.InfNfe.Det.Imposto.Pis"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                PISST: Optional["Tnfe.InfNfe.Det.Imposto.Pisst"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                COFINS: Optional["Tnfe.InfNfe.Det.Imposto.Cofins"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                COFINSST: Optional["Tnfe.InfNfe.Det.Imposto.Cofinsst"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                ICMSUFDest: Optional["Tnfe.InfNfe.Det.Imposto.Icmsufdest"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )

                @dataclass
                class Pis:
                    """
                    :ivar PISAliq: Código de Situação Tributária do PIS.
                        01 – Operação Tributável - Base de Cálculo =
                        Valor da Operação Alíquota Normal
                        (Cumulativo/Não Cumulativo); 02 - Operação
                        Tributável - Base de Calculo = Valor da Operação
                        (Alíquota Diferenciada);
                    :ivar PISQtde: Código de Situação Tributária do PIS.
                        03 - Operação Tributável - Base de Calculo =
                        Quantidade Vendida x Alíquota por Unidade de
                        Produto;
                    :ivar PISNT: Código de Situação Tributária do PIS.
                        04 - Operação Tributável - Tributação Monofásica
                        - (Alíquota Zero); 06 - Operação Tributável -
                        Alíquota Zero; 07 - Operação Isenta da
                        contribuição; 08 - Operação Sem Incidência da
                        contribuição; 09 - Operação com suspensão da
                        contribuição;
                    :ivar PISOutr: Código de Situação Tributária do PIS.
                        99 - Outras Operações.
                    """
                    PISAliq: Optional["Tnfe.InfNfe.Det.Imposto.Pis.Pisaliq"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    PISQtde: Optional["Tnfe.InfNfe.Det.Imposto.Pis.Pisqtde"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    PISNT: Optional["Tnfe.InfNfe.Det.Imposto.Pis.Pisnt"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    PISOutr: Optional["Tnfe.InfNfe.Det.Imposto.Pis.Pisoutr"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )

                    @dataclass
                    class Pisaliq:
                        """
                        :ivar CST: Código de Situação Tributária do PIS.
                            01 – Operação Tributável - Base de Cálculo =
                            Valor da Operação Alíquota Normal
                            (Cumulativo/Não Cumulativo); 02 - Operação
                            Tributável - Base de Calculo = Valor da
                            Operação (Alíquota Diferenciada);
                        :ivar vBC: Valor da BC do PIS
                        :ivar pPIS: Alíquota do PIS (em percentual)
                        :ivar vPIS: Valor do PIS
                        """
                        CST: Optional[PisaliqCst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        vBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pPIS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vPIS: Optional[str] = field(
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
                    class Pisqtde:
                        """
                        :ivar CST: Código de Situação Tributária do PIS.
                            03 - Operação Tributável - Base de Calculo =
                            Quantidade Vendida x Alíquota por Unidade de
                            Produto;
                        :ivar qBCProd: Quantidade Vendida  (NT2011/004)
                        :ivar vAliqProd: Alíquota do PIS (em reais)
                            (NT2011/004)
                        :ivar vPIS: Valor do PIS
                        """
                        CST: Optional[PisqtdeCst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        qBCProd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?",
                            }
                        )
                        vAliqProd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?",
                            }
                        )
                        vPIS: Optional[str] = field(
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
                    class Pisnt:
                        """
                        :ivar CST: Código de Situação Tributária do PIS.
                            04 - Operação Tributável - Tributação
                            Monofásica - (Alíquota Zero); 05 - Operação
                            Tributável (ST); 06 - Operação Tributável -
                            Alíquota Zero; 07 - Operação Isenta da
                            contribuição; 08 - Operação Sem Incidência
                            da contribuição; 09 - Operação com suspensão
                            da contribuição;
                        """
                        CST: Optional[PisntCst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )

                    @dataclass
                    class Pisoutr:
                        """
                        :ivar CST: Código de Situação Tributária do PIS.
                            99 - Outras Operações.
                        :ivar vBC: Valor da BC do PIS
                        :ivar pPIS: Alíquota do PIS (em percentual)
                        :ivar qBCProd: Quantidade Vendida (NT2011/004)
                        :ivar vAliqProd: Alíquota do PIS (em reais)
                            (NT2011/004)
                        :ivar vPIS: Valor do PIS
                        """
                        CST: Optional[PisoutrCst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        vBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pPIS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        qBCProd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?",
                            }
                        )
                        vAliqProd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?",
                            }
                        )
                        vPIS: Optional[str] = field(
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
                class Pisst:
                    """
                    :ivar vBC: Valor da BC do PIS ST
                    :ivar pPIS: Alíquota do PIS ST (em percentual)
                    :ivar qBCProd: Quantidade Vendida
                    :ivar vAliqProd: Alíquota do PIS ST (em reais)
                    :ivar vPIS: Valor do PIS ST
                    :ivar indSomaPISST: Indica se o valor do PISST
                        compõe o valor total da NF-e
                    """
                    vBC: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    pPIS: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    qBCProd: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?",
                        }
                    )
                    vAliqProd: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                        }
                    )
                    vPIS: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    indSomaPISST: Optional[PisstIndSomaPisst] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                        }
                    )

                @dataclass
                class Cofins:
                    """
                    :ivar COFINSAliq: Código de Situação Tributária do
                        COFINS. 01 – Operação Tributável - Base de
                        Cálculo = Valor da Operação Alíquota Normal
                        (Cumulativo/Não Cumulativo); 02 - Operação
                        Tributável - Base de Calculo = Valor da Operação
                        (Alíquota Diferenciada);
                    :ivar COFINSQtde: Código de Situação Tributária do
                        COFINS. 03 - Operação Tributável - Base de
                        Calculo = Quantidade Vendida x Alíquota por
                        Unidade de Produto;
                    :ivar COFINSNT: Código de Situação Tributária do
                        COFINS: 04 - Operação Tributável - Tributação
                        Monofásica - (Alíquota Zero); 06 - Operação
                        Tributável - Alíquota Zero; 07 - Operação Isenta
                        da contribuição; 08 - Operação Sem Incidência da
                        contribuição; 09 - Operação com suspensão da
                        contribuição;
                    :ivar COFINSOutr: Código de Situação Tributária do
                        COFINS: 49 - Outras Operações de Saída 50 -
                        Operação com Direito a Crédito - Vinculada
                        Exclusivamente a Receita Tributada no Mercado
                        Interno 51 - Operação com Direito a Crédito –
                        Vinculada Exclusivamente a Receita Não Tributada
                        no Mercado Interno 52 - Operação com Direito a
                        Crédito - Vinculada Exclusivamente a Receita de
                        Exportação 53 - Operação com Direito a Crédito -
                        Vinculada a Receitas Tributadas e Não-Tributadas
                        no Mercado Interno 54 - Operação com Direito a
                        Crédito - Vinculada a Receitas Tributadas no
                        Mercado Interno e de Exportação 55 - Operação
                        com Direito a Crédito - Vinculada a Receitas
                        Não-Tributadas no Mercado Interno e de
                        Exportação 56 - Operação com Direito a Crédito -
                        Vinculada a Receitas Tributadas e Não-Tributadas
                        no Mercado Interno, e de Exportação 60 - Crédito
                        Presumido - Operação de Aquisição Vinculada
                        Exclusivamente a Receita Tributada no Mercado
                        Interno 61 - Crédito Presumido - Operação de
                        Aquisição Vinculada Exclusivamente a Receita
                        Não-Tributada no Mercado Interno 62 - Crédito
                        Presumido - Operação de Aquisição Vinculada
                        Exclusivamente a Receita de Exportação 63 -
                        Crédito Presumido - Operação de Aquisição
                        Vinculada a Receitas Tributadas e Não-Tributadas
                        no Mercado Interno 64 - Crédito Presumido -
                        Operação de Aquisição Vinculada a Receitas
                        Tributadas no Mercado Interno e de Exportação 65
                        - Crédito Presumido - Operação de Aquisição
                        Vinculada a Receitas Não-Tributadas no Mercado
                        Interno e de Exportação 66 - Crédito Presumido -
                        Operação de Aquisição Vinculada a Receitas
                        Tributadas e Não-Tributadas no Mercado Interno,
                        e de Exportação 67 - Crédito Presumido - Outras
                        Operações 70 - Operação de Aquisição sem Direito
                        a Crédito 71 - Operação de Aquisição com Isenção
                        72 - Operação de Aquisição com Suspensão 73 -
                        Operação de Aquisição a Alíquota Zero 74 -
                        Operação de Aquisição sem Incidência da
                        Contribuição 75 - Operação de Aquisição por
                        Substituição Tributária 98 - Outras Operações de
                        Entrada 99 - Outras Operações.
                    """
                    COFINSAliq: Optional["Tnfe.InfNfe.Det.Imposto.Cofins.Cofinsaliq"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    COFINSQtde: Optional["Tnfe.InfNfe.Det.Imposto.Cofins.Cofinsqtde"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    COFINSNT: Optional["Tnfe.InfNfe.Det.Imposto.Cofins.Cofinsnt"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    COFINSOutr: Optional["Tnfe.InfNfe.Det.Imposto.Cofins.Cofinsoutr"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )

                    @dataclass
                    class Cofinsaliq:
                        """
                        :ivar CST: Código de Situação Tributária do
                            COFINS. 01 – Operação Tributável - Base de
                            Cálculo = Valor da Operação Alíquota Normal
                            (Cumulativo/Não Cumulativo); 02 - Operação
                            Tributável - Base de Calculo = Valor da
                            Operação (Alíquota Diferenciada);
                        :ivar vBC: Valor da BC do COFINS
                        :ivar pCOFINS: Alíquota do COFINS (em
                            percentual)
                        :ivar vCOFINS: Valor do COFINS
                        """
                        CST: Optional[CofinsaliqCst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        vBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pCOFINS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vCOFINS: Optional[str] = field(
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
                    class Cofinsqtde:
                        """
                        :ivar CST: Código de Situação Tributária do
                            COFINS. 03 - Operação Tributável - Base de
                            Calculo = Quantidade Vendida x Alíquota por
                            Unidade de Produto;
                        :ivar qBCProd: Quantidade Vendida (NT2011/004)
                        :ivar vAliqProd: Alíquota do COFINS (em reais)
                            (NT2011/004)
                        :ivar vCOFINS: Valor do COFINS
                        """
                        CST: Optional[CofinsqtdeCst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        qBCProd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?",
                            }
                        )
                        vAliqProd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?",
                            }
                        )
                        vCOFINS: Optional[str] = field(
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
                    class Cofinsnt:
                        """
                        :ivar CST: Código de Situação Tributária do
                            COFINS: 04 - Operação Tributável -
                            Tributação Monofásica - (Alíquota Zero); 05
                            - Operação Tributável (ST); 06 - Operação
                            Tributável - Alíquota Zero; 07 - Operação
                            Isenta da contribuição; 08 - Operação Sem
                            Incidência da contribuição; 09 - Operação
                            com suspensão da contribuição;
                        """
                        CST: Optional[CofinsntCst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )

                    @dataclass
                    class Cofinsoutr:
                        """
                        :ivar CST: Código de Situação Tributária do
                            COFINS: 49 - Outras Operações de Saída 50 -
                            Operação com Direito a Crédito - Vinculada
                            Exclusivamente a Receita Tributada no
                            Mercado Interno 51 - Operação com Direito a
                            Crédito – Vinculada Exclusivamente a Receita
                            Não Tributada no Mercado Interno 52 -
                            Operação com Direito a Crédito - Vinculada
                            Exclusivamente a Receita de Exportação 53 -
                            Operação com Direito a Crédito - Vinculada a
                            Receitas Tributadas e Não-Tributadas no
                            Mercado Interno 54 - Operação com Direito a
                            Crédito - Vinculada a Receitas Tributadas no
                            Mercado Interno e de Exportação 55 -
                            Operação com Direito a Crédito - Vinculada a
                            Receitas Não-Tributadas no Mercado Interno e
                            de Exportação 56 - Operação com Direito a
                            Crédito - Vinculada a Receitas Tributadas e
                            Não-Tributadas no Mercado Interno, e de
                            Exportação 60 - Crédito Presumido - Operação
                            de Aquisição Vinculada Exclusivamente a
                            Receita Tributada no Mercado Interno 61 -
                            Crédito Presumido - Operação de Aquisição
                            Vinculada Exclusivamente a Receita Não-
                            Tributada no Mercado Interno 62 - Crédito
                            Presumido - Operação de Aquisição Vinculada
                            Exclusivamente a Receita de Exportação 63 -
                            Crédito Presumido - Operação de Aquisição
                            Vinculada a Receitas Tributadas e Não-
                            Tributadas no Mercado Interno 64 - Crédito
                            Presumido - Operação de Aquisição Vinculada
                            a Receitas Tributadas no Mercado Interno e
                            de Exportação 65 - Crédito Presumido -
                            Operação de Aquisição Vinculada a Receitas
                            Não-Tributadas no Mercado Interno e de
                            Exportação 66 - Crédito Presumido - Operação
                            de Aquisição Vinculada a Receitas Tributadas
                            e Não-Tributadas no Mercado Interno, e de
                            Exportação 67 - Crédito Presumido - Outras
                            Operações 70 - Operação de Aquisição sem
                            Direito a Crédito 71 - Operação de Aquisição
                            com Isenção 72 - Operação de Aquisição com
                            Suspensão 73 - Operação de Aquisição a
                            Alíquota Zero 74 - Operação de Aquisição sem
                            Incidência da Contribuição 75 - Operação de
                            Aquisição por Substituição Tributária 98 -
                            Outras Operações de Entrada 99 - Outras
                            Operações.
                        :ivar vBC: Valor da BC do COFINS
                        :ivar pCOFINS: Alíquota do COFINS (em
                            percentual)
                        :ivar qBCProd: Quantidade Vendida (NT2011/004)
                        :ivar vAliqProd: Alíquota do COFINS (em reais)
                            (NT2011/004)
                        :ivar vCOFINS: Valor do COFINS
                        """
                        CST: Optional[CofinsoutrCst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        vBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pCOFINS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        qBCProd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?",
                            }
                        )
                        vAliqProd: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?",
                            }
                        )
                        vCOFINS: Optional[str] = field(
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
                class Cofinsst:
                    """
                    :ivar vBC: Valor da BC do COFINS ST
                    :ivar pCOFINS: Alíquota do COFINS ST(em percentual)
                    :ivar qBCProd: Quantidade Vendida
                    :ivar vAliqProd: Alíquota do COFINS ST(em reais)
                    :ivar vCOFINS: Valor do COFINS ST
                    :ivar indSomaCOFINSST: Indica se o valor da COFINS
                        ST compõe o valor total da NFe
                    """
                    vBC: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    pCOFINS: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    qBCProd: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?",
                        }
                    )
                    vAliqProd: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                        }
                    )
                    vCOFINS: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    indSomaCOFINSST: Optional[CofinsstIndSomaCofinsst] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                        }
                    )

                @dataclass
                class Icmsufdest:
                    """
                    :ivar vBCUFDest: Valor da Base de Cálculo do ICMS na
                        UF do destinatário.
                    :ivar vBCFCPUFDest: Valor da Base de Cálculo do FCP
                        na UF do destinatário.
                    :ivar pFCPUFDest: Percentual adicional inserido na
                        alíquota interna da UF de destino, relativo ao
                        Fundo de Combate à Pobreza (FCP) naquela UF.
                    :ivar pICMSUFDest: Alíquota adotada nas operações
                        internas na UF do destinatário para o produto /
                        mercadoria.
                    :ivar pICMSInter: Alíquota interestadual das UF
                        envolvidas: - 4% alíquota interestadual para
                        produtos importados; - 7% para os Estados de
                        origem do Sul e Sudeste (exceto ES), destinado
                        para os Estados do Norte e Nordeste  ou ES; -
                        12% para os demais casos.
                    :ivar pICMSInterPart: Percentual de partilha para a
                        UF do destinatário: - 40% em 2016; - 60% em
                        2017; - 80% em 2018; - 100% a partir de 2019.
                    :ivar vFCPUFDest: Valor do ICMS relativo ao Fundo de
                        Combate à Pobreza (FCP) da UF de destino.
                    :ivar vICMSUFDest: Valor do ICMS de partilha para a
                        UF do destinatário.
                    :ivar vICMSUFRemet: Valor do ICMS de partilha para a
                        UF do remetente. Nota: A partir de 2019, este
                        valor será zero.
                    """
                    vBCUFDest: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vBCFCPUFDest: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    pFCPUFDest: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    pICMSUFDest: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    pICMSInter: Optional[IcmsufdestPIcmsinter] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    pICMSInterPart: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    vFCPUFDest: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vICMSUFDest: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vICMSUFRemet: Optional[str] = field(
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
                class Icms:
                    """
                    :ivar ICMS00: Tributação pelo ICMS 00 - Tributada
                        integralmente
                    :ivar ICMS10: Tributação pelo ICMS 10 - Tributada e
                        com cobrança do ICMS por substituição tributária
                    :ivar ICMS20: Tributção pelo ICMS 20 - Com redução
                        de base de cálculo
                    :ivar ICMS30: Tributação pelo ICMS 30 - Isenta ou
                        não tributada e com cobrança do ICMS por
                        substituição tributária
                    :ivar ICMS40: Tributação pelo ICMS 40 - Isenta 41 -
                        Não tributada 50 - Suspensão
                    :ivar ICMS51: Tributção pelo ICMS 51 - Diferimento A
                        exigência do preenchimento das informações do
                        ICMS diferido fica à critério de cada UF.
                    :ivar ICMS60: Tributação pelo ICMS 60 - ICMS cobrado
                        anteriormente por substituição tributária
                    :ivar ICMS70: Tributação pelo ICMS 70 - Com redução
                        de base de cálculo e cobrança do ICMS por
                        substituição tributária
                    :ivar ICMS90: Tributação pelo ICMS 90 - Outras
                    :ivar ICMSPart: Partilha do ICMS entre a UF de
                        origem e UF de destino ou a UF definida na
                        legislação Operação interestadual para
                        consumidor final com partilha do ICMS  devido na
                        operação entre a UF de origem e a UF do
                        destinatário ou ou a UF definida na legislação.
                        (Ex. UF da concessionária de entrega do
                        veículos)
                    :ivar ICMSST: Grupo de informação do ICMSST devido
                        para a UF de destino, nas operações
                        interestaduais de produtos que tiveram retenção
                        antecipada de ICMS por ST na UF do remetente.
                        Repasse via Substituto Tributário.
                    :ivar ICMSSN101: Tributação do ICMS pelo SIMPLES
                        NACIONAL e CSOSN=101 (v.2.0)
                    :ivar ICMSSN102: Tributação do ICMS pelo SIMPLES
                        NACIONAL e CSOSN=102, 103, 300 ou 400 (v.2.0))
                    :ivar ICMSSN201: Tributação do ICMS pelo SIMPLES
                        NACIONAL e CSOSN=201 (v.2.0)
                    :ivar ICMSSN202: Tributação do ICMS pelo SIMPLES
                        NACIONAL e CSOSN=202 ou 203 (v.2.0)
                    :ivar ICMSSN500: Tributação do ICMS pelo SIMPLES
                        NACIONAL,CRT=1 – Simples Nacional e CSOSN=500
                        (v.2.0)
                    :ivar ICMSSN900: Tributação do ICMS pelo SIMPLES
                        NACIONAL, CRT=1 – Simples Nacional e CSOSN=900
                        (v2.0)
                    """
                    ICMS00: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms00"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMS10: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms10"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMS20: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms20"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMS30: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms30"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMS40: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms40"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMS51: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms51"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMS60: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms60"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMS70: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms70"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMS90: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms90"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMSPart: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmspart"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMSST: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmsst"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMSSN101: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmssn101"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMSSN102: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmssn102"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMSSN201: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmssn201"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMSSN202: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmssn202"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMSSN500: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmssn500"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    ICMSSN900: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmssn900"] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )

                    @dataclass
                    class Icms00:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                        :ivar CST: Tributção pelo ICMS 00 - Tributada
                            integralmente
                        :ivar modBC: Modalidade de determinação da BC do
                            ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar vBC: Valor da BC do ICMS
                        :ivar pICMS: Alíquota do ICMS
                        :ivar vICMS: Valor do ICMS
                        :ivar pFCP: Percentual de ICMS relativo ao Fundo
                            de Combate à Pobreza (FCP).
                        :ivar vFCP: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CST: Optional[Icms00Cst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        modBC: Optional[Icms00ModBc] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        vBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
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
                        pFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )

                    @dataclass
                    class Icms10:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                        :ivar CST: 10 - Tributada e com cobrança do ICMS
                            por substituição tributária
                        :ivar modBC: Modalidade de determinação da BC do
                            ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar vBC: Valor da BC do ICMS
                        :ivar pICMS: Alíquota do ICMS
                        :ivar vICMS: Valor do ICMS
                        :ivar vBCFCP: Valor da Base de cálculo do FCP.
                        :ivar pFCP: Percentual de ICMS relativo ao Fundo
                            de Combate à Pobreza (FCP).
                        :ivar vFCP: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        :ivar modBCST: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor) 6-Valor da Operação;
                        :ivar pMVAST: Percentual da Margem de Valor
                            Adicionado ICMS ST
                        :ivar pRedBCST: Percentual de redução da BC ICMS
                            ST
                        :ivar vBCST: Valor da BC do ICMS ST
                        :ivar pICMSST: Alíquota do ICMS ST
                        :ivar vICMSST: Valor do ICMS ST
                        :ivar vBCFCPST: Valor da Base de cálculo do FCP
                            retido por substituicao tributaria.
                        :ivar pFCPST: Percentual de FCP retido por
                            substituição tributária.
                        :ivar vFCPST: Valor do FCP retido por
                            substituição tributária.
                        :ivar vICMSSTDeson: Valor do ICMS-ST desonerado.
                        :ivar motDesICMSST: Motivo da desoneração do
                            ICMS-ST: 3-Uso na agropecuária; 9-Outros;
                            12-Fomento agropecuário.
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CST: Optional[Icms10Cst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        modBC: Optional[Icms10ModBc] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        vBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
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
                        vBCFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        modBCST: Optional[Icms10ModBcst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        pMVAST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        pRedBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vBCFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vICMSSTDeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        motDesICMSST: Optional[Icms10MotDesIcmsst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )

                    @dataclass
                    class Icms20:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                        :ivar CST: Tributção pelo ICMS 20 - Com redução
                            de base de cálculo
                        :ivar modBC: Modalidade de determinação da BC do
                            ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar pRedBC: Percentual de redução da BC
                        :ivar vBC: Valor da BC do ICMS
                        :ivar pICMS: Alíquota do ICMS
                        :ivar vICMS: Valor do ICMS
                        :ivar vBCFCP: Valor da Base de cálculo do FCP.
                        :ivar pFCP: Percentual de ICMS relativo ao Fundo
                            de Combate à Pobreza (FCP).
                        :ivar vFCP: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        :ivar vICMSDeson: Valor do ICMS de desoneração
                        :ivar motDesICMS: Motivo da desoneração do
                            ICMS:3-Uso na
                            agropecuária;9-Outros;12-Fomento
                            agropecuário
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CST: Optional[Icms20Cst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        modBC: Optional[Icms20ModBc] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        pRedBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
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
                        vBCFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vICMSDeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        motDesICMS: Optional[Icms20MotDesIcms] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )

                    @dataclass
                    class Icms30:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                        :ivar CST: Tributção pelo ICMS 30 - Isenta ou
                            não tributada e com cobrança do ICMS por
                            substituição tributária
                        :ivar modBCST: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor). 6 - Valor da Operação
                        :ivar pMVAST: Percentual da Margem de Valor
                            Adicionado ICMS ST
                        :ivar pRedBCST: Percentual de redução da BC ICMS
                            ST
                        :ivar vBCST: Valor da BC do ICMS ST
                        :ivar pICMSST: Alíquota do ICMS ST
                        :ivar vICMSST: Valor do ICMS ST
                        :ivar vBCFCPST: Valor da Base de cálculo do FCP.
                        :ivar pFCPST: Percentual de FCP retido por
                            substituição tributária.
                        :ivar vFCPST: Valor do FCP retido por
                            substituição tributária.
                        :ivar vICMSDeson: Valor do ICMS de desoneração
                        :ivar motDesICMS: Motivo da desoneração do
                            ICMS:6-Utilitários Motocicleta AÁrea
                            Livre;7-SUFRAMA;9-Outros
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CST: Optional[Icms30Cst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        modBCST: Optional[Icms30ModBcst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        pMVAST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        pRedBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vBCFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vICMSDeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        motDesICMS: Optional[Icms30MotDesIcms] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )

                    @dataclass
                    class Icms40:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                        :ivar CST: Tributação pelo ICMS 40 - Isenta 41 -
                            Não tributada 50 - Suspensão 51 -
                            Diferimento
                        :ivar vICMSDeson: O valor do ICMS será informado
                            apenas nas operações com veículos
                            beneficiados com a desoneração condicional
                            do ICMS.
                        :ivar motDesICMS: Este campo será preenchido
                            quando o campo anterior estiver preenchido.
                            Informar o motivo da desoneração: 1 – Táxi;
                            3 – Produtor Agropecuário; 4 –
                            Frotista/Locadora; 5 – Diplomático/Consular;
                            6 – Utilitários e Motocicletas da Amazônia
                            Ocidental e Áreas de Livre Comércio
                            (Resolução 714/88 e 790/94 – CONTRAN e suas
                            alterações); 7 – SUFRAMA; 8 - Venda a órgão
                            Público; 9 – Outros 10- Deficiente Condutor
                            11- Deficiente não condutor 16 - Olimpíadas
                            Rio 2016 90 - Solicitado pelo Fisco
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CST: Optional[Icms40Cst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        vICMSDeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        motDesICMS: Optional[Icms40MotDesIcms] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )

                    @dataclass
                    class Icms51:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                        :ivar CST: Tributção pelo ICMS 20 - Com redução
                            de base de cálculo
                        :ivar modBC: Modalidade de determinação da BC do
                            ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar pRedBC: Percentual de redução da BC
                        :ivar vBC: Valor da BC do ICMS
                        :ivar pICMS: Alíquota do imposto
                        :ivar vICMSOp: Valor do ICMS da Operação
                        :ivar pDif: Percentual do diferemento
                        :ivar vICMSDif: Valor do ICMS da diferido
                        :ivar vICMS: Valor do ICMS
                        :ivar vBCFCP: Valor da Base de cálculo do FCP.
                        :ivar pFCP: Percentual de ICMS relativo ao Fundo
                            de Combate à Pobreza (FCP).
                        :ivar vFCP: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        :ivar pFCPDif: Percentual do diferimento do ICMS
                            relativo ao Fundo de Combate à Pobreza
                            (FCP).
                        :ivar vFCPDif: Valor do ICMS relativo ao Fundo
                            de Combate à Pobreza (FCP) diferido.
                        :ivar vFCPEfet: Valor efetivo do ICMS relativo
                            ao Fundo de Combate à Pobreza (FCP).
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CST: Optional[Icms51Cst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        modBC: Optional[Icms51ModBc] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        pRedBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSOp: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pDif: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0(\.[0-9]{2,4})?|[1-9]{1}[0-9]{0,1}(\.[0-9]{2,4})?|100(\.0{2,4})?",
                            }
                        )
                        vICMSDif: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vICMS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vBCFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCPDif: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCPDif: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vFCPEfet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )

                    @dataclass
                    class Icms60:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                        :ivar CST: Tributação pelo ICMS 60 - ICMS
                            cobrado anteriormente por substituição
                            tributária
                        :ivar vBCSTRet: Valor da BC do ICMS ST retido
                            anteriormente
                        :ivar pST: Aliquota suportada pelo consumidor
                            final.
                        :ivar vICMSSubstituto: Valor do ICMS Próprio do
                            Substituto cobrado em operação anterior
                        :ivar vICMSSTRet: Valor do ICMS ST retido
                            anteriormente
                        :ivar vBCFCPSTRet: Valor da Base de cálculo do
                            FCP retido anteriormente por ST.
                        :ivar pFCPSTRet: Percentual de FCP retido
                            anteriormente por substituição tributária.
                        :ivar vFCPSTRet: Valor do FCP retido por
                            substituição tributária.
                        :ivar pRedBCEfet: Percentual de redução da base
                            de cálculo efetiva.
                        :ivar vBCEfet: Valor da base de cálculo efetiva.
                        :ivar pICMSEfet: Alíquota do ICMS efetiva.
                        :ivar vICMSEfet: Valor do ICMS efetivo.
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CST: Optional[Icms60Cst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        vBCSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSSubstituto: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vICMSSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vBCFCPSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCPSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCPSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pRedBCEfet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBCEfet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMSEfet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSEfet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )

                    @dataclass
                    class Icms70:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                        :ivar CST: Tributção pelo ICMS 70 - Com redução
                            de base de cálculo e cobrança do ICMS por
                            substituição tributária
                        :ivar modBC: Modalidade de determinação da BC do
                            ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar pRedBC: Percentual de redução da BC
                        :ivar vBC: Valor da BC do ICMS
                        :ivar pICMS: Alíquota do ICMS
                        :ivar vICMS: Valor do ICMS
                        :ivar vBCFCP: Valor da Base de cálculo do FCP.
                        :ivar pFCP: Percentual de ICMS relativo ao Fundo
                            de Combate à Pobreza (FCP).
                        :ivar vFCP: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        :ivar modBCST: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor); 6 - Valor da Operação.
                        :ivar pMVAST: Percentual da Margem de Valor
                            Adicionado ICMS ST
                        :ivar pRedBCST: Percentual de redução da BC ICMS
                            ST
                        :ivar vBCST: Valor da BC do ICMS ST
                        :ivar pICMSST: Alíquota do ICMS ST
                        :ivar vICMSST: Valor do ICMS ST
                        :ivar vBCFCPST: Valor da Base de cálculo do FCP
                            retido por substituição tributária.
                        :ivar pFCPST: Percentual de FCP retido por
                            substituição tributária.
                        :ivar vFCPST: Valor do FCP retido por
                            substituição tributária.
                        :ivar vICMSDeson: Valor do ICMS de desoneração
                        :ivar motDesICMS: Motivo da desoneração do
                            ICMS:3-Uso na
                            agropecuária;9-Outros;12-Fomento
                            agropecuário
                        :ivar vICMSSTDeson: Valor do ICMS-ST desonerado.
                        :ivar motDesICMSST: Motivo da desoneração do
                            ICMS-ST: 3-Uso na agropecuária; 9-Outros;
                            12-Fomento agropecuário.
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CST: Optional[Icms70Cst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        modBC: Optional[Icms70ModBc] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        pRedBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
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
                        vBCFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        modBCST: Optional[Icms70ModBcst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        pMVAST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        pRedBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vBCFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vICMSDeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        motDesICMS: Optional[Icms70MotDesIcms] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        vICMSSTDeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        motDesICMSST: Optional[Icms70MotDesIcmsst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )

                    @dataclass
                    class Icms90:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                        :ivar CST: Tributção pelo ICMS 90 - Outras
                        :ivar modBC: Modalidade de determinação da BC do
                            ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar vBC: Valor da BC do ICMS
                        :ivar pRedBC: Percentual de redução da BC
                        :ivar pICMS: Alíquota do ICMS
                        :ivar vICMS: Valor do ICMS
                        :ivar vBCFCP: Valor da Base de cálculo do FCP.
                        :ivar pFCP: Percentual de ICMS relativo ao Fundo
                            de Combate à Pobreza (FCP).
                        :ivar vFCP: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        :ivar modBCST: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor); 6 - Valor da Operação.
                        :ivar pMVAST: Percentual da Margem de Valor
                            Adicionado ICMS ST
                        :ivar pRedBCST: Percentual de redução da BC ICMS
                            ST
                        :ivar vBCST: Valor da BC do ICMS ST
                        :ivar pICMSST: Alíquota do ICMS ST
                        :ivar vICMSST: Valor do ICMS ST
                        :ivar vBCFCPST: Valor da Base de cálculo do FCP.
                        :ivar pFCPST: Percentual de FCP retido por
                            substituição tributária.
                        :ivar vFCPST: Valor do FCP retido por
                            substituição tributária.
                        :ivar vICMSDeson: Valor do ICMS de desoneração
                        :ivar motDesICMS: Motivo da desoneração do
                            ICMS:3-Uso na
                            agropecuária;9-Outros;12-Fomento
                            agropecuário
                        :ivar vICMSSTDeson: Valor do ICMS-ST desonerado.
                        :ivar motDesICMSST: Motivo da desoneração do
                            ICMS-ST: 3-Uso na agropecuária; 9-Outros;
                            12-Fomento agropecuário.
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CST: Optional[Icms90Cst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        modBC: Optional[Icms90ModBc] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        vBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pRedBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        pICMS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vBCFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCP: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        modBCST: Optional[Icms90ModBcst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        pMVAST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        pRedBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vBCFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vICMSDeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        motDesICMS: Optional[Icms90MotDesIcms] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        vICMSSTDeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        motDesICMSST: Optional[Icms90MotDesIcmsst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )

                    @dataclass
                    class Icmspart:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                        :ivar CST: Tributação pelo ICMS 10 - Tributada e
                            com cobrança do ICMS por substituição
                            tributária; 90 – Outros.
                        :ivar modBC: Modalidade de determinação da BC do
                            ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar vBC: Valor da BC do ICMS
                        :ivar pRedBC: Percentual de redução da BC
                        :ivar pICMS: Alíquota do ICMS
                        :ivar vICMS: Valor do ICMS
                        :ivar modBCST: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor). 6 - Valor da Operação
                        :ivar pMVAST: Percentual da Margem de Valor
                            Adicionado ICMS ST
                        :ivar pRedBCST: Percentual de redução da BC ICMS
                            ST
                        :ivar vBCST: Valor da BC do ICMS ST
                        :ivar pICMSST: Alíquota do ICMS ST
                        :ivar vICMSST: Valor do ICMS ST
                        :ivar pBCOp: Percentual para determinação do
                            valor  da Base de Cálculo da operação
                            própria.
                        :ivar UFST: Sigla da UF para qual é devido o
                            ICMS ST da operação.
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CST: Optional[IcmspartCst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        modBC: Optional[IcmspartModBc] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        vBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pRedBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        pICMS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
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
                        modBCST: Optional[IcmspartModBcst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        pMVAST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        pRedBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pBCOp: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        UFST: Optional[Tuf] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )

                    @dataclass
                    class Icmsst:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                        :ivar CST: Tributção pelo ICMS 41-Não Tributado.
                            60-Cobrado anteriormente por substituição
                            tributária.
                        :ivar vBCSTRet: Informar o valor da BC do ICMS
                            ST retido na UF remetente
                        :ivar pST: Aliquota suportada pelo consumidor
                            final.
                        :ivar vICMSSubstituto: Valor do ICMS Próprio do
                            Substituto cobrado em operação anterior
                        :ivar vICMSSTRet: Informar o valor do ICMS ST
                            retido na UF remetente (iv2.0))
                        :ivar vBCFCPSTRet: Informar o valor da Base de
                            Cálculo do FCP retido anteriormente por ST.
                        :ivar pFCPSTRet: Percentual relativo ao Fundo de
                            Combate à Pobreza (FCP) retido por
                            substituição tributária.
                        :ivar vFCPSTRet: Valor do ICMS relativo ao Fundo
                            de Combate à Pobreza (FCP) retido por
                            substituição tributária.
                        :ivar vBCSTDest: Informar o valor da BC do ICMS
                            ST da UF destino
                        :ivar vICMSSTDest: Informar o valor da BC do
                            ICMS ST da UF destino (v2.0)
                        :ivar pRedBCEfet: Percentual de redução da base
                            de cálculo efetiva.
                        :ivar vBCEfet: Valor da base de cálculo efetiva.
                        :ivar pICMSEfet: Alíquota do ICMS efetivo.
                        :ivar vICMSEfet: Valor do ICMS efetivo.
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CST: Optional[IcmsstCst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        vBCSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSSubstituto: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vICMSSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vBCFCPSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCPSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCPSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vBCSTDest: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vICMSSTDest: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pRedBCEfet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBCEfet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMSEfet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSEfet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )

                    @dataclass
                    class Icmssn101:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                            (v2.0)
                        :ivar CSOSN: 101- Tributada pelo Simples
                            Nacional com permissão de crédito. (v.2.0)
                        :ivar pCredSN: Alíquota aplicável de cálculo do
                            crédito (Simples Nacional). (v2.0)
                        :ivar vCredICMSSN: Valor crédito do ICMS que
                            pode ser aproveitado nos termos do art. 23
                            da LC 123 (Simples Nacional) (v2.0)
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CSOSN: Optional[Icmssn101Csosn] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        pCredSN: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vCredICMSSN: Optional[str] = field(
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
                    class Icmssn102:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                            (v2.0)
                        :ivar CSOSN: 102- Tributada pelo Simples
                            Nacional sem permissão de crédito. 103 –
                            Isenção do ICMS  no Simples Nacional para
                            faixa de receita bruta. 300 – Imune. 400 –
                            Não tributda pelo Simples Nacional (v.2.0)
                            (v.2.0)
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CSOSN: Optional[Icmssn102Csosn] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )

                    @dataclass
                    class Icmssn201:
                        """
                        :ivar orig: Origem da mercadoria: 0 – Nacional;
                            1 – Estrangeira – Importação direta; 2 –
                            Estrangeira – Adquirida no mercado interno.
                            (v2.0)
                        :ivar CSOSN: 201- Tributada pelo Simples
                            Nacional com permissão de crédito e com
                            cobrança do ICMS por Substituição Tributária
                            (v.2.0)
                        :ivar modBCST: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor). (v2.0) 6 - Valor da Operação
                        :ivar pMVAST: Percentual da Margem de Valor
                            Adicionado ICMS ST (v2.0)
                        :ivar pRedBCST: Percentual de redução da BC ICMS
                            ST  (v2.0)
                        :ivar vBCST: Valor da BC do ICMS ST (v2.0)
                        :ivar pICMSST: Alíquota do ICMS ST (v2.0)
                        :ivar vICMSST: Valor do ICMS ST (v2.0)
                        :ivar vBCFCPST: Valor da Base de cálculo do FCP.
                        :ivar pFCPST: Percentual de FCP retido por
                            substituição tributária.
                        :ivar vFCPST: Valor do FCP retido por
                            substituição tributária.
                        :ivar pCredSN: Alíquota aplicável de cálculo do
                            crédito (Simples Nacional). (v2.0)
                        :ivar vCredICMSSN: Valor crédito do ICMS que
                            pode ser aproveitado nos termos do art. 23
                            da LC 123 (Simples Nacional) (v2.0)
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CSOSN: Optional[Icmssn201Csosn] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        modBCST: Optional[Icmssn201ModBcst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        pMVAST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        pRedBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vBCFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pCredSN: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vCredICMSSN: Optional[str] = field(
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
                    class Icmssn202:
                        """
                        :ivar orig: Origem da mercadoria: 0 – Nacional;
                            1 – Estrangeira – Importação direta; 2 –
                            Estrangeira – Adquirida no mercado interno.
                            (v2.0)
                        :ivar CSOSN: 202- Tributada pelo Simples
                            Nacional sem permissão de crédito e com
                            cobrança do ICMS por Substituição
                            Tributária; 203-  Isenção do ICMS nos
                            Simples Nacional para faixa de receita bruta
                            e com cobrança do ICMS por Substituição
                            Tributária (v.2.0)
                        :ivar modBCST: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor). (v2.0) 6 - Valor da Operação
                        :ivar pMVAST: Percentual da Margem de Valor
                            Adicionado ICMS ST (v2.0)
                        :ivar pRedBCST: Percentual de redução da BC ICMS
                            ST  (v2.0)
                        :ivar vBCST: Valor da BC do ICMS ST (v2.0)
                        :ivar pICMSST: Alíquota do ICMS ST (v2.0)
                        :ivar vICMSST: Valor do ICMS ST (v2.0)
                        :ivar vBCFCPST: Valor da Base de cálculo do FCP.
                        :ivar pFCPST: Percentual de FCP retido por
                            substituição tributária.
                        :ivar vFCPST: Valor do FCP retido por
                            substituição tributária.
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CSOSN: Optional[Icmssn202Csosn] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        modBCST: Optional[Icmssn202ModBcst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        pMVAST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        pRedBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vBCFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )

                    @dataclass
                    class Icmssn500:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                        :ivar CSOSN: 500 – ICMS cobrado anterirmente por
                            substituição tributária (substituído) ou por
                            antecipação (v.2.0)
                        :ivar vBCSTRet: Valor da BC do ICMS ST retido
                            anteriormente (v2.0)
                        :ivar pST: Aliquota suportada pelo consumidor
                            final.
                        :ivar vICMSSubstituto: Valor do ICMS próprio do
                            substituto
                        :ivar vICMSSTRet: Valor do ICMS ST retido
                            anteriormente  (v2.0)
                        :ivar vBCFCPSTRet: Valor da Base de cálculo do
                            FCP retido anteriormente.
                        :ivar pFCPSTRet: Percentual de FCP retido
                            anteriormente por substituição tributária.
                        :ivar vFCPSTRet: Valor do FCP retido por
                            substituição tributária.
                        :ivar pRedBCEfet: Percentual de redução da base
                            de cálculo efetiva.
                        :ivar vBCEfet: Valor da base de cálculo efetiva.
                        :ivar pICMSEfet: Alíquota do ICMS efetiva.
                        :ivar vICMSEfet: Valor do ICMS efetivo.
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CSOSN: Optional[Icmssn500Csosn] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        vBCSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSSubstituto: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vICMSSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vBCFCPSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCPSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCPSTRet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pRedBCEfet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBCEfet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMSEfet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSEfet: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )

                    @dataclass
                    class Icmssn900:
                        """
                        :ivar orig: origem da mercadoria: 0 - Nacional 1
                            - Estrangeira - Importação direta 2 -
                            Estrangeira - Adquirida no mercado interno
                        :ivar CSOSN: Tributação pelo ICMS 900 -
                            Outros(v2.0)
                        :ivar modBC: Modalidade de determinação da BC do
                            ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar vBC: Valor da BC do ICMS
                        :ivar pRedBC: Percentual de redução da BC
                        :ivar pICMS: Alíquota do ICMS
                        :ivar vICMS: Valor do ICMS
                        :ivar modBCST: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor). 6 - Valor da Operação
                        :ivar pMVAST: Percentual da Margem de Valor
                            Adicionado ICMS ST
                        :ivar pRedBCST: Percentual de redução da BC ICMS
                            ST
                        :ivar vBCST: Valor da BC do ICMS ST
                        :ivar pICMSST: Alíquota do ICMS ST
                        :ivar vICMSST: Valor do ICMS ST
                        :ivar vBCFCPST: Valor da Base de cálculo do FCP.
                        :ivar pFCPST: Percentual de FCP retido por
                            substituição tributária.
                        :ivar vFCPST: Valor do FCP retido por
                            substituição tributária.
                        :ivar pCredSN: Alíquota aplicável de cálculo do
                            crédito (Simples Nacional). (v2.0)
                        :ivar vCredICMSSN: Valor crédito do ICMS que
                            pode ser aproveitado nos termos do art. 23
                            da LC 123 (Simples Nacional) (v2.0)
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        CSOSN: Optional[Icmssn900Csosn] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        modBC: Optional[Icmssn900ModBc] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        vBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pRedBC: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        pICMS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMS: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        modBCST: Optional[Icmssn900ModBcst] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        pMVAST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        pRedBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vBCST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vICMSST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        vBCFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vFCPST: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        pCredSN: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        vCredICMSSN: Optional[str] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )

                @dataclass
                class Ii:
                    """
                    :ivar vBC: Base da BC do Imposto de Importação
                    :ivar vDespAdu: Valor das despesas aduaneiras
                    :ivar vII: Valor do Imposto de Importação
                    :ivar vIOF: Valor do Imposto sobre Operações
                        Financeiras
                    """
                    vBC: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vDespAdu: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vII: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vIOF: Optional[str] = field(
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
                class Issqn:
                    """
                    :ivar vBC: Valor da BC do ISSQN
                    :ivar vAliq: Alíquota do ISSQN
                    :ivar vISSQN: Valor da do ISSQN
                    :ivar cMunFG: Informar o município de ocorrência do
                        fato gerador do ISSQN. Utilizar a Tabela do IBGE
                        (Anexo VII - Tabela de UF, Município e País).
                        “Atenção, não vincular com os campos B12, C10 ou
                        E10” v2.0
                    :ivar cListServ: Informar o Item da lista de
                        serviços da LC 116/03 em que se classifica o
                        serviço.
                    :ivar vDeducao: Valor dedução para redução da base
                        de cálculo
                    :ivar vOutro: Valor outras retenções
                    :ivar vDescIncond: Valor desconto incondicionado
                    :ivar vDescCond: Valor desconto condicionado
                    :ivar vISSRet: Valor Retenção ISS
                    :ivar indISS: Exibilidade do ISS:1-Exigível;2-Não
                        incidente;3-Isenção;4-Exportação;5-Imunidade;6-Exig.Susp.
                        Judicial;7-Exig.Susp. ADM
                    :ivar cServico: Código do serviço prestado dentro do
                        município
                    :ivar cMun: Código do Município de Incidência do
                        Imposto
                    :ivar cPais: Código de Pais
                    :ivar nProcesso: Número do Processo administrativo
                        ou judicial de suspenção do processo
                    :ivar indIncentivo: Indicador de Incentivo Fiscal.
                        1=Sim; 2=Não
                    """
                    vBC: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vAliq: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    vISSQN: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    cMunFG: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{7}",
                        }
                    )
                    cListServ: Optional[TclistServ] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                        }
                    )
                    vDeducao: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vOutro: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vDescIncond: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vDescCond: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    vISSRet: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    indISS: Optional[IssqnIndIss] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    cServico: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "min_length": 1,
                            "max_length": 20,
                            "white_space": "preserve",
                        }
                    )
                    cMun: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{7}",
                        }
                    )
                    cPais: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,4}",
                        }
                    )
                    nProcesso: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "min_length": 1,
                            "max_length": 30,
                            "white_space": "preserve",
                        }
                    )
                    indIncentivo: Optional[IssqnIndIncentivo] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )

            @dataclass
            class ImpostoDevol:
                """
                :ivar pDevol: Percentual de mercadoria devolvida
                :ivar IPI: Informação de IPI devolvido
                """
                pDevol: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0(\.[0-9]{2})?|100(\.00)?|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})?",
                    }
                )
                IPI: Optional["Tnfe.InfNfe.Det.ImpostoDevol.Ipi"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                    }
                )

                @dataclass
                class Ipi:
                    """
                    :ivar vIPIDevol: Valor do IPI devolvido
                    """
                    vIPIDevol: Optional[str] = field(
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
        class Total:
            """
            :ivar ICMSTot: Totais referentes ao ICMS
            :ivar ISSQNtot: Totais referentes ao ISSQN
            :ivar retTrib: Retenção de Tributos Federais
            """
            ICMSTot: Optional["Tnfe.InfNfe.Total.Icmstot"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            ISSQNtot: Optional["Tnfe.InfNfe.Total.Issqntot"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            retTrib: Optional["Tnfe.InfNfe.Total.RetTrib"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )

            @dataclass
            class Icmstot:
                """
                :ivar vBC: BC do ICMS
                :ivar vICMS: Valor Total do ICMS
                :ivar vICMSDeson: Valor Total do ICMS desonerado
                :ivar vFCPUFDest: Valor total do ICMS relativo ao Fundo
                    de Combate à Pobreza (FCP) para a UF de destino.
                :ivar vICMSUFDest: Valor total do ICMS de partilha para
                    a UF do destinatário
                :ivar vICMSUFRemet: Valor total do ICMS de partilha para
                    a UF do remetente
                :ivar vFCP: Valor Total do FCP (Fundo de Combate à
                    Pobreza).
                :ivar vBCST: BC do ICMS ST
                :ivar vST: Valor Total do ICMS ST
                :ivar vFCPST: Valor Total do FCP (Fundo de Combate à
                    Pobreza) retido por substituição tributária.
                :ivar vFCPSTRet: Valor Total do FCP (Fundo de Combate à
                    Pobreza) retido anteriormente por substituição
                    tributária.
                :ivar vProd: Valor Total dos produtos e serviços
                :ivar vFrete: Valor Total do Frete
                :ivar vSeg: Valor Total do Seguro
                :ivar vDesc: Valor Total do Desconto
                :ivar vII: Valor Total do II
                :ivar vIPI: Valor Total do IPI
                :ivar vIPIDevol: Valor Total do IPI devolvido. Deve ser
                    informado quando preenchido o Grupo Tributos
                    Devolvidos na emissão de nota finNFe=4 (devolução)
                    nas operações com não contribuintes do IPI.
                    Corresponde ao total da soma dos campos id: UA04.
                :ivar vPIS: Valor do PIS
                :ivar vCOFINS: Valor do COFINS
                :ivar vOutro: Outras Despesas acessórias
                :ivar vNF: Valor Total da NF-e
                :ivar vTotTrib: Valor estimado total de impostos
                    federais, estaduais e municipais
                """
                vBC: Optional[str] = field(
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
                vICMSDeson: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vFCPUFDest: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vICMSUFDest: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vICMSUFRemet: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vFCP: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vBCST: Optional[str] = field(
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
                vFCPST: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vFCPSTRet: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vProd: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vFrete: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vSeg: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vDesc: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vII: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vIPI: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vIPIDevol: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vPIS: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vCOFINS: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vOutro: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
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
                vTotTrib: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

            @dataclass
            class Issqntot:
                """
                :ivar vServ: Valor Total dos Serviços sob não-incidência
                    ou não tributados pelo ICMS
                :ivar vBC: Base de Cálculo do ISS
                :ivar vISS: Valor Total do ISS
                :ivar vPIS: Valor do PIS sobre serviços
                :ivar vCOFINS: Valor do COFINS sobre serviços
                :ivar dCompet: Data da prestação do serviço  (AAAA-MM-
                    DD)
                :ivar vDeducao: Valor dedução para redução da base de
                    cálculo
                :ivar vOutro: Valor outras retenções
                :ivar vDescIncond: Valor desconto incondicionado
                :ivar vDescCond: Valor desconto condicionado
                :ivar vISSRet: Valor Total Retenção ISS
                :ivar cRegTrib: Código do regime especial de tributação
                """
                vServ: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vBC: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vISS: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vPIS: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vCOFINS: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                dCompet: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                    }
                )
                vDeducao: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vOutro: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vDescIncond: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vDescCond: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vISSRet: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                cRegTrib: Optional[IssqntotCRegTrib] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                    }
                )

            @dataclass
            class RetTrib:
                """
                :ivar vRetPIS: Valor Retido de PIS
                :ivar vRetCOFINS: Valor Retido de COFINS
                :ivar vRetCSLL: Valor Retido de CSLL
                :ivar vBCIRRF: Base de Cálculo do IRRF
                :ivar vIRRF: Valor Retido de IRRF
                :ivar vBCRetPrev: Base de Cálculo da Retenção da
                    Previdêncica Social
                :ivar vRetPrev: Valor da Retenção da Previdêncica Social
                """
                vRetPIS: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vRetCOFINS: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vRetCSLL: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vBCIRRF: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vIRRF: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vBCRetPrev: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vRetPrev: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

        @dataclass
        class Transp:
            """
            :ivar modFrete: Modalidade do frete 0- Contratação do Frete
                por conta do Remetente (CIF); 1- Contratação do Frete
                por conta do destinatário/remetente (FOB); 2-
                Contratação do Frete por conta de terceiros; 3-
                Transporte próprio por conta do remetente; 4- Transporte
                próprio por conta do destinatário; 9- Sem Ocorrência de
                transporte.
            :ivar transporta: Dados do transportador
            :ivar retTransp: Dados da retenção  ICMS do Transporte
            :ivar veicTransp: Dados do veículo
            :ivar reboque: Dados do reboque/Dolly (v2.0)
            :ivar vagao: Identificação do vagão (v2.0)
            :ivar balsa: Identificação da balsa (v2.0)
            :ivar vol: Dados dos volumes
            """
            modFrete: Optional[TranspModFrete] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            transporta: Optional["Tnfe.InfNfe.Transp.Transporta"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            retTransp: Optional["Tnfe.InfNfe.Transp.RetTransp"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            veicTransp: Optional[Tveiculo] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            reboque: List[Tveiculo] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_occurs": 5,
                }
            )
            vagao: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            balsa: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            vol: List["Tnfe.InfNfe.Transp.Vol"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_occurs": 5000,
                }
            )

            @dataclass
            class Transporta:
                """
                :ivar CNPJ: CNPJ do transportador
                :ivar CPF: CPF do transportador
                :ivar xNome: Razão Social ou nome do transportador
                :ivar IE: Inscrição Estadual (v2.0)
                :ivar xEnder: Endereço completo
                :ivar xMun: Nome do munícipio
                :ivar UF: Sigla da UF
                """
                CNPJ: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_length": 14,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{14}",
                    }
                )
                CPF: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_length": 11,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{11}",
                    }
                )
                xNome: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                IE: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_length": 14,
                        "white_space": "preserve",
                        "pattern": r"ISENTO|[0-9]{2,14}",
                    }
                )
                xEnder: Optional[str] = field(
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
                xMun: Optional[str] = field(
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
                UF: Optional[Tuf] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )

            @dataclass
            class RetTransp:
                """
                :ivar vServ: Valor do Serviço
                :ivar vBCRet: BC da Retenção do ICMS
                :ivar pICMSRet: Alíquota da Retenção
                :ivar vICMSRet: Valor do ICMS Retido
                :ivar CFOP: Código Fiscal de Operações e Prestações
                :ivar cMunFG: Código do Município de Ocorrência do Fato
                    Gerador (utilizar a tabela do IBGE)
                """
                vServ: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vBCRet: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                pICMSRet: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                    }
                )
                vICMSRet: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                CFOP: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[1,2,3,5,6,7]{1}[0-9]{3}",
                    }
                )
                cMunFG: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7}",
                    }
                )

            @dataclass
            class Vol:
                """
                :ivar qVol: Quantidade de volumes transportados
                :ivar esp: Espécie dos volumes transportados
                :ivar marca: Marca dos volumes transportados
                :ivar nVol: Numeração dos volumes transportados
                :ivar pesoL: Peso líquido (em kg)
                :ivar pesoB: Peso bruto (em kg)
                :ivar lacres:
                """
                qVol: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,15}",
                    }
                )
                esp: Optional[str] = field(
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
                marca: Optional[str] = field(
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
                nVol: Optional[str] = field(
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
                pesoL: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?",
                    }
                )
                pesoB: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?",
                    }
                )
                lacres: List["Tnfe.InfNfe.Transp.Vol.Lacres"] = field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_occurs": 5000,
                    }
                )

                @dataclass
                class Lacres:
                    """
                    :ivar nLacre: Número dos Lacres
                    """
                    nLacre: Optional[str] = field(
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

        @dataclass
        class Cobr:
            """
            :ivar fat: Dados da fatura
            :ivar dup: Dados das duplicatas NT 2011/004
            """
            fat: Optional["Tnfe.InfNfe.Cobr.Fat"] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            dup: List["Tnfe.InfNfe.Cobr.Dup"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_occurs": 120,
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
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vDesc: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                vLiq: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

            @dataclass
            class Dup:
                """
                :ivar nDup: Número da duplicata
                :ivar dVenc: Data de vencimento da duplicata (AAAA-MM-
                    DD)
                :ivar vDup: Valor da duplicata
                """
                nDup: Optional[str] = field(
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
                dVenc: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                    }
                )
                vDup: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

        @dataclass
        class Pag:
            """
            :ivar detPag: Grupo de detalhamento da forma de pagamento.
            :ivar vTroco: Valor do Troco.
            """
            detPag: List["Tnfe.InfNfe.Pag.DetPag"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_occurs": 1,
                    "max_occurs": 100,
                }
            )
            vTroco: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )

            @dataclass
            class DetPag:
                """
                :ivar indPag: Indicador da Forma de
                    Pagamento:0-Pagamento à Vista;1-Pagamento à Prazo;
                :ivar tPag: Forma de Pagamento:
                :ivar xPag: Descrição do Meio de Pagamento
                :ivar vPag: Valor do Pagamento. Esta tag poderá ser
                    omitida quando a tag tPag=90 (Sem Pagamento), caso
                    contrário deverá ser preenchida.
                :ivar card: Grupo de Cartões
                """
                indPag: Optional[DetPagIndPag] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                    }
                )
                tPag: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{2}",
                    }
                )
                xPag: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                vPag: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                card: Optional["Tnfe.InfNfe.Pag.DetPag.Card"] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )

                @dataclass
                class Card:
                    """
                    :ivar tpIntegra: Tipo de Integração do processo de
                        pagamento com o sistema de automação da empresa/
                        1=Pagamento integrado com o sistema de automação
                        da empresa Ex. equipamento TEF , Comercio
                        Eletronico 2=Pagamento não integrado com o
                        sistema de automação da empresa Ex: equipamento
                        POS
                    :ivar CNPJ: CNPJ da instituição de pagamento
                    :ivar tBand: Bandeira da operadora de cartão
                    :ivar cAut: Número de autorização da operação cartão
                        de crédito/débito
                    """
                    tpIntegra: Optional[CardTpIntegra] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    CNPJ: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "max_length": 14,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{14}",
                        }
                    )
                    tBand: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{2}",
                        }
                    )
                    cAut: Optional[str] = field(
                        default=None,
                        metadata={
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "min_length": 1,
                            "max_length": 20,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )

        @dataclass
        class InfIntermed:
            """
            :ivar CNPJ: CNPJ do Intermediador da Transação (agenciador,
                plataforma de delivery, marketplace e similar) de
                serviços e de negócios.
            :ivar idCadIntTran: Identificador cadastrado no
                intermediador
            """
            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            idCadIntTran: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )

        @dataclass
        class InfAdic:
            """
            :ivar infAdFisco: Informações adicionais de interesse do
                Fisco (v2.0)
            :ivar infCpl: Informações complementares de interesse do
                Contribuinte
            :ivar obsCont: Campo de uso livre do contribuinte informar o
                nome do campo no atributo xCampo e o conteúdo do campo
                no xTexto
            :ivar obsFisco: Campo de uso exclusivo do Fisco informar o
                nome do campo no atributo xCampo e o conteúdo do campo
                no xTexto
            :ivar procRef: Grupo de informações do  processo
                referenciado
            """
            infAdFisco: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 5000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            obsCont: List["Tnfe.InfNfe.InfAdic.ObsCont"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_occurs": 10,
                }
            )
            obsFisco: List["Tnfe.InfNfe.InfAdic.ObsFisco"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_occurs": 10,
                }
            )
            procRef: List["Tnfe.InfNfe.InfAdic.ProcRef"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_occurs": 100,
                }
            )

            @dataclass
            class ObsCont:
                xTexto: Optional[str] = field(
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
                xTexto: Optional[str] = field(
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
            class ProcRef:
                """
                :ivar nProc: Indentificador do processo ou ato
                    concessório
                :ivar indProc: Origem do processo, informar com: 0 -
                    SEFAZ; 1 - Justiça Federal; 2 - Justiça Estadual; 3
                    - Secex/RFB; 9 - Outros
                """
                nProc: Optional[str] = field(
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
                indProc: Optional[ProcRefIndProc] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                    }
                )

        @dataclass
        class Exporta:
            """
            :ivar UFSaidaPais: Sigla da UF de Embarque ou de
                transposição de fronteira
            :ivar xLocExporta: Local de Embarque ou de transposição de
                fronteira
            :ivar xLocDespacho: Descrição do local de despacho
            """
            UFSaidaPais: Optional[TufEmi] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            xLocExporta: Optional[str] = field(
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
            xLocDespacho: Optional[str] = field(
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

        @dataclass
        class Compra:
            """
            :ivar xNEmp: Informação da Nota de Empenho de compras
                públicas (NT2011/004)
            :ivar xPed: Informação do pedido
            :ivar xCont: Informação do contrato
            """
            xNEmp: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 22,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            xPed: Optional[str] = field(
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
            xCont: Optional[str] = field(
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

        @dataclass
        class Cana:
            """
            :ivar safra: Identificação da safra
            :ivar ref: Mês e Ano de Referência, formato: MM/AAAA
            :ivar forDia: Fornecimentos diários
            :ivar qTotMes: Total do mês
            :ivar qTotAnt: Total Anterior
            :ivar qTotGer: Total Geral
            :ivar deduc: Deduções - Taxas e Contribuições
            :ivar vFor: Valor  dos fornecimentos
            :ivar vTotDed: Valor Total das Deduções
            :ivar vLiqFor: Valor Líquido dos fornecimentos
            """
            safra: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "min_length": 4,
                    "max_length": 9,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ref: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(0[1-9]|1[0-2])([/][2][0-9][0-9][0-9])",
                }
            )
            forDia: List["Tnfe.InfNfe.Cana.ForDia"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_occurs": 1,
                    "max_occurs": 31,
                }
            )
            qTotMes: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?",
                }
            )
            qTotAnt: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?",
                }
            )
            qTotGer: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?",
                }
            )
            deduc: List["Tnfe.InfNfe.Cana.Deduc"] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_occurs": 10,
                }
            )
            vFor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            vTotDed: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            vLiqFor: Optional[str] = field(
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
            class ForDia:
                """
                :ivar qtde: Quantidade em quilogramas - peso líquido
                :ivar dia: Número do dia
                """
                qtde: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?",
                    }
                )
                dia: Optional[str] = field(
                    default=None,
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[1-9]|[1][0-9]|[2][0-9]|[3][0-1]",
                    }
                )

            @dataclass
            class Deduc:
                """
                :ivar xDed: Descrição da Dedução
                :ivar vDed: valor da dedução
                """
                xDed: Optional[str] = field(
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
                vDed: Optional[str] = field(
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
        class InfSolicNff:
            """
            :ivar xSolic: Solicitação do pedido de emissão da NFF
            """
            xSolic: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "min_length": 2,
                    "max_length": 2000,
                }
            )

    @dataclass
    class InfNfeSupl:
        """
        :ivar qrCode: Texto com o QR-Code impresso no DANFE NFC-e
        :ivar urlChave: Informar a URL da "Consulta por chave de acesso
            da NFC-e". A mesma URL que deve estar informada no DANFE
            NFC-e para consulta por chave de acesso.
        """
        qrCode: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 100,
                "max_length": 600,
                "white_space": "preserve",
                "pattern": r"(((HTTPS?|https?)://.*\?chNFe=[0-9]{44}&nVersao=100&tpAmb=[1-2](&cDest=([A-Za-z0-9.:+-/)(]{0}|[A-Za-z0-9.:+-/)(]{5,20})?)?&dhEmi=[A-Fa-f0-9]{50}&vNF=(0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?)&vICMS=(0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?)&digVal=[A-Fa-f0-9]{56}&cIdToken=[0-9]{6}&cHashQRCode=[A-Fa-f0-9]{40})|((HTTPS?|https?)://.*\?p=([0-9]{34}(1|4)[0-9]{9})\|[2]\|[1-2]\|(0|[1-9]{1}([0-9]{1,5})?)\|[A-Fa-f0-9]{40})|((HTTPS?|https?)://.*\?p=([0-9]{34}9[0-9]{9})\|[2]\|[1-2]\|([0]{1}[1-9]{1}|[1-2]{1}[0-9]{1}|[3]{1}[0-1]{1})\|(0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?)\|[A-Fa-f0-9]{56}\|(0|[1-9]{1}([0-9]{1,5})?)\|[A-Fa-f0-9]{40}))",
            }
        )
        urlChave: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 21,
                "max_length": 85,
            }
        )


@dataclass
class TenviNfe:
    """
    Tipo Pedido de Concessão de Autorização da Nota Fiscal Eletrônica.

    :ivar idLote:
    :ivar indSinc: Indicador de processamento síncrono. 0=NÃO;
        1=SIM=Síncrono
    :ivar NFe:
    :ivar versao:
    """
    class Meta:
        name = "TEnviNFe"

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
    indSinc: Optional[TenviNfeIndSinc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
        }
    )
    NFe: List[Tnfe] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "pattern": r"[1-9]{1}\.[0-9]{2}",
        }
    )


@dataclass
class TnfeProc:
    """
    Tipo da NF-e processada.
    """
    class Meta:
        name = "TNfeProc"

    NFe: Optional[Tnfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    protNFe: Optional[TprotNfe] = field(
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
            "pattern": r"[1-9]{1}\.[0-9]{2}",
        }
    )
