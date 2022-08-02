from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bindings.nfe.v4_0.tipos_basico_v4_00 import (
    Tamb,
    TcodUfIbge,
    Tmod,
    Tuf,
    TufEmi,
)
from nfelib.bindings.nfe.v4_0.xmldsig_core_schema_v1_01 import Signature

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

    :ivar cnpj: CNPJ
    :ivar x_contato: Informar o nome da pessoa a ser contatada na
        empresa desenvolvedora do sistema utilizado na emissão do
        documento fiscal eletrônico.
    :ivar email: Informar o e-mail da pessoa a ser contatada na empresa
        desenvolvedora do sistema.
    :ivar fone: Informar o telefone da pessoa a ser contatada na empresa
        desenvolvedora do sistema. Preencher com o Código DDD + número
        do telefone.
    :ivar id_csrt: Identificador do CSRT utilizado para montar o hash do
        CSRT
    :ivar hash_csrt: O hashCSRT é o resultado da função hash (SHA-1 –
        Base64) do CSRT fornecido pelo fisco mais a Chave de Acesso da
        NFe.
    """
    class Meta:
        name = "TInfRespTec"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{0}|[0-9]{14}",
        }
    )
    x_contato: Optional[str] = field(
        default=None,
        metadata={
            "name": "xContato",
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
    id_csrt: Optional[str] = field(
        default=None,
        metadata={
            "name": "idCSRT",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{2}",
        }
    )
    hash_csrt: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "hashCSRT",
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

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar n_rec: Número do Recibo
    :ivar versao:
    """
    class Meta:
        name = "TConsReciNFe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    n_rec: Optional[str] = field(
        default=None,
        metadata={
            "name": "nRec",
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
            "pattern": r"4\.00",
        }
    )


@dataclass
class TenderEmi:
    """Tipo Dados do Endereço do Emitente  // 24/10/08 - desmembrado / tamanho mínimo

    :ivar x_lgr: Logradouro
    :ivar nro: Número
    :ivar x_cpl: Complemento
    :ivar x_bairro: Bairro
    :ivar c_mun: Código do município
    :ivar x_mun: Nome do município
    :ivar uf: Sigla da UF
    :ivar cep: CEP - NT 2011/004
    :ivar c_pais: Código do país
    :ivar x_pais: Nome do país
    :ivar fone: Preencher com Código DDD + número do telefone (v.2.0)
    """
    class Meta:
        name = "TEnderEmi"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
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
    x_cpl: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    uf: Optional[TufEmi] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    c_pais: Optional[TenderEmiCPais] = field(
        default=None,
        metadata={
            "name": "cPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    x_pais: Optional[TenderEmiXPais] = field(
        default=None,
        metadata={
            "name": "xPais",
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

    :ivar x_lgr: Logradouro
    :ivar nro: Número
    :ivar x_cpl: Complemento
    :ivar x_bairro: Bairro
    :ivar c_mun: Código do município (utilizar a tabela do IBGE),
        informar 9999999 para operações com o exterior.
    :ivar x_mun: Nome do município, informar EXTERIOR para operações com
        o exterior.
    :ivar uf: Sigla da UF, informar EX para operações com o exterior.
    :ivar cep: CEP
    :ivar c_pais: Código de Pais
    :ivar x_pais: Nome do país
    :ivar fone: Telefone, preencher com Código DDD + número do telefone
        , nas operações com exterior é permtido informar o código do
        país + código da localidade + número do telefone
    """
    class Meta:
        name = "TEndereco"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
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
    x_cpl: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 2,
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    c_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "cPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    x_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "xPais",
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

    :ivar cnpjprod: CNPJ do produtor da mercadoria, quando diferente do
        emitente. Somente para os casos de exportação direta ou
        indireta.
    :ivar c_selo: Código do selo de controle do IPI
    :ivar q_selo: Quantidade de selo de controle do IPI
    :ivar c_enq: Código de Enquadramento Legal do IPI (tabela a ser
        criada pela RFB)
    :ivar ipitrib:
    :ivar ipint:
    """
    class Meta:
        name = "TIpi"

    cnpjprod: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJProd",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    c_selo: Optional[str] = field(
        default=None,
        metadata={
            "name": "cSelo",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    q_selo: Optional[str] = field(
        default=None,
        metadata={
            "name": "qSelo",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,12}",
        }
    )
    c_enq: Optional[str] = field(
        default=None,
        metadata={
            "name": "cEnq",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 1,
            "max_length": 3,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    ipitrib: Optional["Tipi.Ipitrib"] = field(
        default=None,
        metadata={
            "name": "IPITrib",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    ipint: Optional["Tipi.Ipint"] = field(
        default=None,
        metadata={
            "name": "IPINT",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )

    @dataclass
    class Ipitrib:
        """
        :ivar cst: Código da Situação Tributária do IPI: 00-Entrada com
            recuperação de crédito 49 - Outras entradas 50-Saída
            tributada 99-Outras saídas
        :ivar v_bc: Valor da BC do IPI
        :ivar p_ipi: Alíquota do IPI
        :ivar q_unid: Quantidade total na unidade padrão para tributação
        :ivar v_unid: Valor por Unidade Tributável. Informar o valor do
            imposto Pauta por unidade de medida.
        :ivar v_ipi: Valor do IPI
        """
        cst: Optional[IpitribCst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
            }
        )
        v_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "vBC",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        p_ipi: Optional[str] = field(
            default=None,
            metadata={
                "name": "pIPI",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
            }
        )
        q_unid: Optional[str] = field(
            default=None,
            metadata={
                "name": "qUnid",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?",
            }
        )
        v_unid: Optional[str] = field(
            default=None,
            metadata={
                "name": "vUnid",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
            }
        )
        v_ipi: Optional[str] = field(
            default=None,
            metadata={
                "name": "vIPI",
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
        :ivar cst: Código da Situação Tributária do IPI: 01-Entrada
            tributada com alíquota zero 02-Entrada isenta 03-Entrada
            não-tributada 04-Entrada imune 05-Entrada com suspensão
            51-Saída tributada com alíquota zero 52-Saída isenta
            53-Saída não-tributada 54-Saída imune 55-Saída com suspensão
        """
        cst: Optional[IpintCst] = field(
            default=None,
            metadata={
                "name": "CST",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
            }
        )


@dataclass
class Tlocal:
    """Tipo Dados do Local de Retirada ou Entrega // 24/10/08 - tamanho mínimo // v2.0

    :ivar cnpj: CNPJ
    :ivar cpf: CPF (v2.0)
    :ivar x_nome: Razão Social ou Nome do Expedidor/Recebedor
    :ivar x_lgr: Logradouro
    :ivar nro: Número
    :ivar x_cpl: Complemento
    :ivar x_bairro: Bairro
    :ivar c_mun: Código do município (utilizar a tabela do IBGE)
    :ivar x_mun: Nome do município
    :ivar uf: Sigla da UF
    :ivar cep: CEP
    :ivar c_pais: Código de Pais
    :ivar x_pais: Nome do país
    :ivar fone: Telefone, preencher com Código DDD + número do telefone
        , nas operações com exterior é permtido informar o código do
        país + código da localidade + número do telefone
    :ivar email: Informar o e-mail do expedidor/Recebedor. O campo pode
        ser utilizado para informar o e-mail de recepção da NF-e
        indicada pelo expedidor
    :ivar ie: Inscrição Estadual (v2.0)
    """
    class Meta:
        name = "TLocal"

    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{0}|[0-9]{14}",
        }
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    x_nome: Optional[str] = field(
        default=None,
        metadata={
            "name": "xNome",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "min_length": 2,
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
    x_cpl: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 2,
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    c_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "cPais",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    x_pais: Optional[str] = field(
        default=None,
        metadata={
            "name": "xPais",
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
    ie: Optional[str] = field(
        default=None,
        metadata={
            "name": "IE",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{2,14}|ISENTO",
        }
    )


@dataclass
class TprotNfe:
    """
    Tipo Protocolo de status resultado do processamento da NF-e.

    :ivar inf_prot: Dados do protocolo de status
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TProtNFe"

    inf_prot: Optional["TprotNfe.InfProt"] = field(
        default=None,
        metadata={
            "name": "infProt",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
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
            "pattern": r"4\.00",
        }
    )

    @dataclass
    class InfProt:
        """
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar ver_aplic: Versão do Aplicativo que processou a NF-e
        :ivar ch_nfe: Chaves de acesso da NF-e, compostas por: UF do
            emitente, AAMM da emissão da NFe, CNPJ do emitente, modelo,
            série e número da NF-e e código numérico+DV.
        :ivar dh_recbto: Data e hora de processamento, no formato AAAA-
            MM-DDTHH:MM:SSTZD. Deve ser preenchida com data e hora da
            gravação no Banco em caso de Confirmação. Em caso de
            Rejeição, com data e hora do recebimento do Lote de NF-e
            enviado.
        :ivar n_prot: Número do Protocolo de Status da NF-e. 1 posição
            (1 – Secretaria de Fazenda Estadual 2 – Receita Federal); 2
            - códiga da UF - 2 posições ano; 10 seqüencial no ano.
        :ivar dig_val: Digest Value da NF-e processada. Utilizado para
            conferir a integridade da NF-e original.
        :ivar c_stat: Código do status da mensagem enviada.
        :ivar x_motivo: Descrição literal do status do serviço
            solicitado.
        :ivar c_msg: Código da Mensagem.
        :ivar x_msg: Mensagem da SEFAZ para o emissor.
        :ivar id:
        """
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        ver_aplic: Optional[str] = field(
            default=None,
            metadata={
                "name": "verAplic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        ch_nfe: Optional[str] = field(
            default=None,
            metadata={
                "name": "chNFe",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 15,
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        dig_val: Optional[bytes] = field(
            default=None,
            metadata={
                "name": "digVal",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "format": "base64",
            }
        )
        c_stat: Optional[str] = field(
            default=None,
            metadata={
                "name": "cStat",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "max_length": 3,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        x_motivo: Optional[str] = field(
            default=None,
            metadata={
                "name": "xMotivo",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        c_msg: Optional[str] = field(
            default=None,
            metadata={
                "name": "cMsg",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"[0-9]{1,4}",
            }
        )
        x_msg: Optional[str] = field(
            default=None,
            metadata={
                "name": "xMsg",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "min_length": 1,
                "max_length": 200,
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
class Tveiculo:
    """
    Tipo Dados do Veículo.

    :ivar placa: Placa do veículo (NT2011/004)
    :ivar uf: Sigla da UF
    :ivar rntc: Registro Nacional de Transportador de Carga (ANTT)
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
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    rntc: Optional[str] = field(
        default=None,
        metadata={
            "name": "RNTC",
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

    :ivar inf_nfe: Informações da Nota Fiscal eletrônica
    :ivar inf_nfe_supl: Informações suplementares Nota Fiscal
    :ivar signature:
    """
    class Meta:
        name = "TNFe"

    inf_nfe: Optional["Tnfe.InfNfe"] = field(
        default=None,
        metadata={
            "name": "infNFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    inf_nfe_supl: Optional["Tnfe.InfNfeSupl"] = field(
        default=None,
        metadata={
            "name": "infNFeSupl",
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
        :ivar aut_xml: Pessoas autorizadas para o download do XML da
            NF-e
        :ivar det: Dados dos detalhes da NF-e
        :ivar total: Dados dos totais da NF-e
        :ivar transp: Dados dos transportes da NF-e
        :ivar cobr: Dados da cobrança da NF-e
        :ivar pag: Dados de Pagamento. Obrigatório apenas para (NFC-e)
            NT 2012/004
        :ivar inf_intermed: Grupo de Informações do Intermediador da
            Transação
        :ivar inf_adic: Informações adicionais da NF-e
        :ivar exporta: Informações de exportação
        :ivar compra: Informações de compras  (Nota de Empenho, Pedido e
            Contrato)
        :ivar cana: Informações de registro aquisições de cana
        :ivar inf_resp_tec: Informações do Responsável Técnico pela
            emissão do DF-e
        :ivar inf_solic_nff: Grupo para informações da solicitação da
            NFF
        :ivar versao: Versão do leiaute (v4.00)
        :ivar id: PL_005d - 11/08/09 - validação do Id
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
        aut_xml: List["Tnfe.InfNfe.AutXml"] = field(
            default_factory=list,
            metadata={
                "name": "autXML",
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
        inf_intermed: Optional["Tnfe.InfNfe.InfIntermed"] = field(
            default=None,
            metadata={
                "name": "infIntermed",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        inf_adic: Optional["Tnfe.InfNfe.InfAdic"] = field(
            default=None,
            metadata={
                "name": "infAdic",
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
        inf_resp_tec: Optional[TinfRespTec] = field(
            default=None,
            metadata={
                "name": "infRespTec",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        inf_solic_nff: Optional["Tnfe.InfNfe.InfSolicNff"] = field(
            default=None,
            metadata={
                "name": "infSolicNFF",
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
                "pattern": r"4\.00",
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "required": True,
                "pattern": r"NFe[0-9]{44}",
            }
        )

        @dataclass
        class Ide:
            """
            :ivar c_uf: Código da UF do emitente do Documento Fiscal.
                Utilizar a Tabela do IBGE.
            :ivar c_nf: Código numérico que compõe a Chave de Acesso.
                Número aleatório gerado pelo emitente para cada NF-e.
            :ivar nat_op: Descrição da Natureza da Operação
            :ivar mod: Código do modelo do Documento Fiscal. 55 = NF-e;
                65 = NFC-e.
            :ivar serie: Série do Documento Fiscal série normal 0-889
                Avulsa Fisco 890-899 SCAN 900-999
            :ivar n_nf: Número do Documento Fiscal
            :ivar dh_emi: Data e Hora de emissão do Documento Fiscal
                (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00
            :ivar dh_sai_ent: Data e Hora da saída ou de entrada da
                mercadoria / produto (AAAA-MM-DDTHH:mm:ssTZD)
            :ivar tp_nf: Tipo do Documento Fiscal (0 - entrada; 1 -
                saída)
            :ivar id_dest: Identificador de Local de destino da operação
                (1-Interna;2-Interestadual;3-Exterior)
            :ivar c_mun_fg: Código do Município de Ocorrência do Fato
                Gerador (utilizar a tabela do IBGE)
            :ivar tp_imp: Formato de impressão do DANFE (0-sem
                DANFE;1-DANFe Retrato; 2-DANFe Paisagem;3-DANFe
                Simplificado; 4-DANFe NFC-e;5-DANFe NFC-e em mensagem
                eletrônica)
            :ivar tp_emis: Forma de emissão da NF-e 1 - Normal; 2 -
                Contingência FS 3 - Regime Especial NFF (NT 2021.002) 4
                - Contingência DPEC 5 - Contingência FSDA 6 -
                Contingência SVC - AN 7 - Contingência SVC - RS 9 -
                Contingência off-line NFC-e
            :ivar c_dv: Digito Verificador da Chave de Acesso da NF-e
            :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
                Homologação
            :ivar fin_nfe: Finalidade da emissão da NF-e: 1 - NFe normal
                2 - NFe complementar 3 - NFe de ajuste 4 -
                Devolução/Retorno
            :ivar ind_final: Indica operação com consumidor final
                (0-Não;1-Consumidor Final)
            :ivar ind_pres: Indicador de presença do comprador no
                estabelecimento comercial no momento da oepração (0-Não
                se aplica (ex.: Nota Fiscal complementar ou de
                ajuste;1-Operação presencial;2-Não presencial,
                internet;3-Não presencial, teleatendimento;4-NFC-e
                entrega em domicílio;5-Operação presencial, fora do
                estabelecimento;9-Não presencial, outros)
            :ivar ind_intermed: Indicador de intermediador/marketplace
                0=Operação sem intermediador (em site ou plataforma
                própria) 1=Operação em site ou plataforma de terceiros
                (intermediadores/marketplace)
            :ivar proc_emi: Processo de emissão utilizado com a seguinte
                codificação: 0 - emissão de NF-e com aplicativo do
                contribuinte; 1 - emissão de NF-e avulsa pelo Fisco; 2 -
                emissão de NF-e avulsa, pelo contribuinte com seu
                certificado digital, através do site do Fisco; 3-
                emissão de NF-e pelo contribuinte com aplicativo
                fornecido pelo Fisco.
            :ivar ver_proc: versão do aplicativo utilizado no processo
                de emissão
            :ivar dh_cont: Informar a data e hora de entrada em
                contingência contingência no formato  (AAAA-MM-
                DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00.
            :ivar x_just: Informar a Justificativa da entrada
            :ivar nfref: Grupo de infromações da NF referenciada
            """
            c_uf: Optional[TcodUfIbge] = field(
                default=None,
                metadata={
                    "name": "cUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            c_nf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cNF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8}",
                }
            )
            nat_op: Optional[str] = field(
                default=None,
                metadata={
                    "name": "natOp",
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
            n_nf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nNF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            dh_sai_ent: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhSaiEnt",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            tp_nf: Optional[IdeTpNf] = field(
                default=None,
                metadata={
                    "name": "tpNF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            id_dest: Optional[IdeIdDest] = field(
                default=None,
                metadata={
                    "name": "idDest",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            c_mun_fg: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cMunFG",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            tp_imp: Optional[IdeTpImp] = field(
                default=None,
                metadata={
                    "name": "tpImp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            tp_emis: Optional[IdeTpEmis] = field(
                default=None,
                metadata={
                    "name": "tpEmis",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            c_dv: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cDV",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            fin_nfe: Optional[TfinNfe] = field(
                default=None,
                metadata={
                    "name": "finNFe",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            ind_final: Optional[IdeIndFinal] = field(
                default=None,
                metadata={
                    "name": "indFinal",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            ind_pres: Optional[IdeIndPres] = field(
                default=None,
                metadata={
                    "name": "indPres",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            ind_intermed: Optional[IdeIndIntermed] = field(
                default=None,
                metadata={
                    "name": "indIntermed",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                }
            )
            proc_emi: Optional[TprocEmi] = field(
                default=None,
                metadata={
                    "name": "procEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            ver_proc: Optional[str] = field(
                default=None,
                metadata={
                    "name": "verProc",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            dh_cont: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dhCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
                }
            )
            x_just: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xJust",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 15,
                    "max_length": 256,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            nfref: List["Tnfe.InfNfe.Ide.Nfref"] = field(
                default_factory=list,
                metadata={
                    "name": "NFref",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_occurs": 500,
                }
            )

            @dataclass
            class Nfref:
                """
                :ivar ref_nfe: Chave de acesso das NF-e referenciadas.
                    Chave de acesso compostas por Código da UF (tabela
                    do IBGE) + AAMM da emissão + CNPJ do Emitente +
                    modelo, série e número da NF-e Referenciada + Código
                    Numérico + DV.
                :ivar ref_nf: Dados da NF modelo 1/1A referenciada ou NF
                    modelo 2 referenciada
                :ivar ref_nfp: Grupo com as informações NF de produtor
                    referenciada
                :ivar ref_cte: Utilizar esta TAG para referenciar um
                    CT-e emitido anteriormente, vinculada a NF-e atual
                :ivar ref_ecf: Grupo do Cupom Fiscal vinculado à NF-e
                """
                ref_nfe: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "refNFe",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_length": 44,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{44}",
                    }
                )
                ref_nf: Optional["Tnfe.InfNfe.Ide.Nfref.RefNf"] = field(
                    default=None,
                    metadata={
                        "name": "refNF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                ref_nfp: Optional["Tnfe.InfNfe.Ide.Nfref.RefNfp"] = field(
                    default=None,
                    metadata={
                        "name": "refNFP",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                ref_cte: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "refCTe",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_length": 44,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{44}",
                    }
                )
                ref_ecf: Optional["Tnfe.InfNfe.Ide.Nfref.RefEcf"] = field(
                    default=None,
                    metadata={
                        "name": "refECF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )

                @dataclass
                class RefNf:
                    """
                    :ivar c_uf: Código da UF do emitente do Documento
                        Fiscal. Utilizar a Tabela do IBGE.
                    :ivar aamm: AAMM da emissão
                    :ivar cnpj: CNPJ do emitente do documento fiscal
                        referenciado
                    :ivar mod: Código do modelo do Documento Fiscal.
                        Utilizar 01 para NF modelo 1/1A e 02 para NF
                        modelo 02
                    :ivar serie: Série do Documento Fiscal, informar
                        zero se inexistente
                    :ivar n_nf: Número do Documento Fiscal
                    """
                    c_uf: Optional[TcodUfIbge] = field(
                        default=None,
                        metadata={
                            "name": "cUF",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                        }
                    )
                    aamm: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "AAMM",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{2}[0]{1}[1-9]{1}|[0-9]{2}[1]{1}[0-2]{1}",
                        }
                    )
                    cnpj: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "CNPJ",
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
                    n_nf: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nNF",
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
                    :ivar c_uf: Código da UF do emitente do Documento
                        FiscalUtilizar a Tabela do IBGE (Anexo IV -
                        Tabela de UF, Município e País)
                    :ivar aamm: AAMM da emissão da NF de produtor
                    :ivar cnpj: CNPJ do emitente da NF de produtor
                    :ivar cpf: CPF do emitente da NF de produtor
                    :ivar ie: IE do emitente da NF de Produtor
                    :ivar mod: Código do modelo do Documento Fiscal -
                        utilizar 04 para NF de produtor  ou 01 para NF
                        Avulsa
                    :ivar serie: Série do Documento Fiscal, informar
                        zero se inexistentesérie
                    :ivar n_nf: Número do Documento Fiscal - 1 –
                        999999999
                    """
                    c_uf: Optional[TcodUfIbge] = field(
                        default=None,
                        metadata={
                            "name": "cUF",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                        }
                    )
                    aamm: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "AAMM",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{2}[0]{1}[1-9]{1}|[0-9]{2}[1]{1}[0-2]{1}",
                        }
                    )
                    cnpj: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "CNPJ",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "max_length": 14,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{14}",
                        }
                    )
                    cpf: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "CPF",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "max_length": 11,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{11}",
                        }
                    )
                    ie: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "IE",
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
                    n_nf: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nNF",
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
                    :ivar n_ecf: Informar o número de ordem seqüencial
                        do ECF que emitiu o Cupom Fiscal vinculado à
                        NF-e
                    :ivar n_coo: Informar o Número do Contador de Ordem
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
                    n_ecf: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nECF",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,3}",
                        }
                    )
                    n_coo: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nCOO",
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
            :ivar cnpj: Número do CNPJ do emitente
            :ivar cpf: Número do CPF do emitente
            :ivar x_nome: Razão Social ou Nome do emitente
            :ivar x_fant: Nome fantasia
            :ivar ender_emit: Endereço do emitente
            :ivar ie: Inscrição Estadual do Emitente
            :ivar iest: Inscricao Estadual do Substituto Tributário
            :ivar im: Inscrição Municipal
            :ivar cnae: CNAE Fiscal
            :ivar crt: Código de Regime Tributário. Este campo será
                obrigatoriamente preenchido com: 1 – Simples Nacional; 2
                – Simples Nacional – excesso de sublimite de receita
                bruta; 3 – Regime Normal.
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 11,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ender_emit: Optional[TenderEmi] = field(
                default=None,
                metadata={
                    "name": "enderEmit",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}|ISENTO",
                }
            )
            iest: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IEST",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            im: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IM",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{7}",
                }
            )
            crt: Optional[EmitCrt] = field(
                default=None,
                metadata={
                    "name": "CRT",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )

        @dataclass
        class Avulsa:
            """
            :ivar cnpj: CNPJ do Órgão emissor
            :ivar x_orgao: Órgão emitente
            :ivar matr: Matrícula do agente
            :ivar x_agente: Nome do agente
            :ivar fone: Telefone
            :ivar uf: Sigla da Unidade da Federação
            :ivar n_dar: Número do Documento de Arrecadação de Receita
            :ivar d_emi: Data de emissão do DAR (AAAA-MM-DD)
            :ivar v_dar: Valor Total constante no DAR
            :ivar rep_emi: Repartição Fiscal emitente
            :ivar d_pag: Data de pagamento do DAR (AAAA-MM-DD)
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            x_orgao: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xOrgao",
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
            x_agente: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xAgente",
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
            uf: Optional[TufEmi] = field(
                default=None,
                metadata={
                    "name": "UF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            n_dar: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nDAR",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            d_emi: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )
            v_dar: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vDAR",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            rep_emi: Optional[str] = field(
                default=None,
                metadata={
                    "name": "repEmi",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            d_pag: Optional[str] = field(
                default=None,
                metadata={
                    "name": "dPag",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                }
            )

        @dataclass
        class Dest:
            """
            :ivar cnpj: Número do CNPJ
            :ivar cpf: Número do CPF
            :ivar id_estrangeiro: Identificador do destinatário, em caso
                de comprador estrangeiro
            :ivar x_nome: Razão Social ou nome do destinatário
            :ivar ender_dest: Dados do endereço
            :ivar ind_iedest: Indicador da IE do destinatário: 1 –
                Contribuinte ICMSpagamento à vista; 2 – Contribuinte
                isento de inscrição; 9 – Não Contribuinte
            :ivar ie: Inscrição Estadual (obrigatório nas operações com
                contribuintes do ICMS)
            :ivar isuf: Inscrição na SUFRAMA (Obrigatório nas operações
                com as áreas com benefícios de incentivos fiscais sob
                controle da SUFRAMA) PL_005d - 11/08/09 - alterado para
                aceitar 8 ou 9 dígitos
            :ivar im: Inscrição Municipal do tomador do serviço
            :ivar email: Informar o e-mail do destinatário. O campo pode
                ser utilizado para informar o e-mail de recepção da NF-e
                indicada pelo destinatário
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 11,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{11}",
                }
            )
            id_estrangeiro: Optional[str] = field(
                default=None,
                metadata={
                    "name": "idEstrangeiro",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"([!-ÿ]{0}|[!-ÿ]{5,20})?",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ender_dest: Optional[Tendereco] = field(
                default=None,
                metadata={
                    "name": "enderDest",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            ind_iedest: Optional[DestIndIedest] = field(
                default=None,
                metadata={
                    "name": "indIEDest",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            isuf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ISUF",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{8,9}",
                }
            )
            im: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IM",
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
            :ivar cnpj: CNPJ Autorizado
            :ivar cpf: CPF Autorizado
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            cpf: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CPF",
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
            :ivar imposto_devol:
            :ivar inf_ad_prod: Informações adicionais do produto (norma
                referenciada, informações complementares, etc)
            :ivar n_item: Número do item do NF
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
            imposto_devol: Optional["Tnfe.InfNfe.Det.ImpostoDevol"] = field(
                default=None,
                metadata={
                    "name": "impostoDevol",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            inf_ad_prod: Optional[str] = field(
                default=None,
                metadata={
                    "name": "infAdProd",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 500,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            n_item: Optional[str] = field(
                default=None,
                metadata={
                    "name": "nItem",
                    "type": "Attribute",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[1-9]{1}[0-9]{0,1}|[1-8]{1}[0-9]{2}|[9]{1}[0-8]{1}[0-9]{1}|[9]{1}[9]{1}[0]{1}",
                }
            )

            @dataclass
            class Prod:
                """
                :ivar c_prod: Código do produto ou serviço. Preencher
                    com CFOP caso se trate de itens não relacionados com
                    mercadorias/produto e que o contribuinte não possua
                    codificação própria Formato ”CFOP9999”.
                :ivar c_ean: GTIN (Global Trade Item Number) do produto,
                    antigo código EAN ou código de barras
                :ivar c_barra: Codigo de barras diferente do padrão GTIN
                :ivar x_prod: Descrição do produto ou serviço
                :ivar ncm: Código NCM (8 posições), será permitida a
                    informação do gênero (posição do capítulo do NCM)
                    quando a operação não for de comércio exterior
                    (importação/exportação) ou o produto não seja
                    tributado pelo IPI. Em caso de item de serviço ou
                    item que não tenham produto (Ex. transferência de
                    crédito, crédito do ativo imobilizado, etc.),
                    informar o código 00 (zeros) (v2.0)
                :ivar nve: Nomenclatura de Valor aduaneio e Estatístico
                :ivar cest: Codigo especificador da Substuicao
                    Tributaria - CEST, que identifica a mercadoria
                    sujeita aos regimes de  substituicao tributária e de
                    antecipação do recolhimento  do imposto
                :ivar ind_escala:
                :ivar cnpjfab: CNPJ do Fabricante da Mercadoria,
                    obrigatório para produto em escala NÃO relevante.
                :ivar c_benef:
                :ivar extipi: Código EX TIPI (3 posições)
                :ivar cfop: Cfop
                :ivar u_com: Unidade comercial
                :ivar q_com: Quantidade Comercial  do produto, alterado
                    para aceitar de 0 a 4 casas decimais e 11 inteiros.
                :ivar v_un_com: Valor unitário de comercialização  -
                    alterado para aceitar 0 a 10 casas decimais e 11
                    inteiros
                :ivar v_prod: Valor bruto do produto ou serviço.
                :ivar c_eantrib: GTIN (Global Trade Item Number) da
                    unidade tributável, antigo código EAN ou código de
                    barras
                :ivar c_barra_trib: Código de barras da unidade
                    tributável diferente do padrão GTIN
                :ivar u_trib: Unidade Tributável
                :ivar q_trib: Quantidade Tributável - alterado para
                    aceitar de 0 a 4 casas decimais e 11 inteiros
                :ivar v_un_trib: Valor unitário de tributação - -
                    alterado para aceitar 0 a 10 casas decimais e 11
                    inteiros
                :ivar v_frete: Valor Total do Frete
                :ivar v_seg: Valor Total do Seguro
                :ivar v_desc: Valor do Desconto
                :ivar v_outro: Outras despesas acessórias
                :ivar ind_tot: Este campo deverá ser preenchido com: 0 –
                    o valor do item (vProd) não compõe o valor total da
                    NF-e (vProd) 1  – o valor do item (vProd) compõe o
                    valor total da NF-e (vProd)
                :ivar di: Delcaração de Importação (NT 2011/004)
                :ivar det_export: Detalhe da exportação
                :ivar x_ped: pedido de compra - Informação de interesse
                    do emissor para controle do B2B.
                :ivar n_item_ped: Número do Item do Pedido de Compra -
                    Identificação do número do item do pedido de Compra
                :ivar n_fci: Número de controle da FCI - Ficha de
                    Conteúdo de Importação.
                :ivar rastro:
                :ivar inf_prod_nff: Informações mais detalhadas do
                    produto (usada na NFF)
                :ivar inf_prod_emb: Informações mais detalhadas do
                    produto (usada na NFF)
                :ivar veic_prod: Veículos novos
                :ivar med: grupo do detalhamento de Medicamentos e de
                    matérias-primas farmacêuticas
                :ivar arma: Armamentos
                :ivar comb: Informar apenas para operações com
                    combustíveis líquidos
                :ivar n_recopi: Número do RECOPI
                """
                c_prod: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cProd",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                c_ean: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cEAN",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"SEM GTIN|[0-9]{0}|[0-9]{8}|[0-9]{12,14}",
                    }
                )
                c_barra: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cBarra",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "min_length": 3,
                        "max_length": 30,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                x_prod: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xProd",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 120,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                ncm: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "NCM",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{2}|[0-9]{8}",
                    }
                )
                nve: List[str] = field(
                    default_factory=list,
                    metadata={
                        "name": "NVE",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_occurs": 8,
                        "white_space": "preserve",
                        "pattern": r"[A-Z]{2}[0-9]{4}",
                    }
                )
                cest: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CEST",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{7}",
                    }
                )
                ind_escala: Optional[ProdIndEscala] = field(
                    default=None,
                    metadata={
                        "name": "indEscala",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                cnpjfab: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CNPJFab",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_length": 14,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{14}",
                    }
                )
                c_benef: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cBenef",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"([!-ÿ]{8}|[!-ÿ]{10}|SEM CBENEF)?",
                    }
                )
                extipi: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "EXTIPI",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{2,3}",
                    }
                )
                cfop: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CFOP",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[1,2,3,5,6,7]{1}[0-9]{3}",
                    }
                )
                u_com: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "uCom",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 6,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                q_com: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "qCom",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?",
                    }
                )
                v_un_com: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vUnCom",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?",
                    }
                )
                v_prod: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vProd",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                c_eantrib: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cEANTrib",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"SEM GTIN|[0-9]{0}|[0-9]{8}|[0-9]{12,14}",
                    }
                )
                c_barra_trib: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cBarraTrib",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "min_length": 3,
                        "max_length": 30,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                u_trib: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "uTrib",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 6,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                q_trib: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "qTrib",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?",
                    }
                )
                v_un_trib: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vUnTrib",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?",
                    }
                )
                v_frete: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vFrete",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_seg: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vSeg",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_desc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vDesc",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_outro: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vOutro",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                ind_tot: Optional[ProdIndTot] = field(
                    default=None,
                    metadata={
                        "name": "indTot",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                    }
                )
                di: List["Tnfe.InfNfe.Det.Prod.Di"] = field(
                    default_factory=list,
                    metadata={
                        "name": "DI",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_occurs": 100,
                    }
                )
                det_export: List["Tnfe.InfNfe.Det.Prod.DetExport"] = field(
                    default_factory=list,
                    metadata={
                        "name": "detExport",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_occurs": 500,
                    }
                )
                x_ped: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xPed",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "min_length": 1,
                        "max_length": 15,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                n_item_ped: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nItemPed",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"[0-9]{1,6}",
                    }
                )
                n_fci: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nFCI",
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
                inf_prod_nff: Optional["Tnfe.InfNfe.Det.Prod.InfProdNff"] = field(
                    default=None,
                    metadata={
                        "name": "infProdNFF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                inf_prod_emb: Optional["Tnfe.InfNfe.Det.Prod.InfProdEmb"] = field(
                    default=None,
                    metadata={
                        "name": "infProdEmb",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                veic_prod: Optional["Tnfe.InfNfe.Det.Prod.VeicProd"] = field(
                    default=None,
                    metadata={
                        "name": "veicProd",
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
                n_recopi: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nRECOPI",
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
                    :ivar n_di: Numero do Documento de Importação
                        DI/DSI/DA/DRI-E (DI/DSI/DA/DRI-E) (NT2011/004)
                    :ivar d_di: Data de registro da DI/DSI/DA (AAAA-MM-
                        DD)
                    :ivar x_loc_desemb: Local do desembaraço aduaneiro
                    :ivar ufdesemb: UF onde ocorreu o desembaraço
                        aduaneiro
                    :ivar d_desemb: Data do desembaraço aduaneiro (AAAA-
                        MM-DD)
                    :ivar tp_via_transp: Via de transporte internacional
                        informada na DI
                        1-Maritima;2-Fluvial;3-Lacustre;4-Aerea;5-Postal;6-Ferroviaria;7-Rodoviaria;8-Conduto;9-Meios
                        Proprios;10-Entrada/Saida Ficta;
                        11-Courier;12-Em maos;13-Por reboque.
                    :ivar v_afrmm: Valor Adicional ao frete para
                        renovação de marinha mercante
                    :ivar tp_intermedio: Forma de Importação quanto a
                        intermediação 1-por conta propria;2-por conta e
                        ordem;3-encomenda
                    :ivar cnpj: CNPJ do adquirente ou do encomendante
                    :ivar ufterceiro: Sigla da UF do adquirente ou do
                        encomendante
                    :ivar c_exportador: Código do exportador (usado nos
                        sistemas internos de informação do emitente da
                        NF-e)
                    :ivar adi: Adições (NT 2011/004)
                    """
                    n_di: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nDI",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 15,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    d_di: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "dDI",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    x_loc_desemb: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "xLocDesemb",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 60,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    ufdesemb: Optional[TufEmi] = field(
                        default=None,
                        metadata={
                            "name": "UFDesemb",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                        }
                    )
                    d_desemb: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "dDesemb",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    tp_via_transp: Optional[DiTpViaTransp] = field(
                        default=None,
                        metadata={
                            "name": "tpViaTransp",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    v_afrmm: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vAFRMM",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    tp_intermedio: Optional[DiTpIntermedio] = field(
                        default=None,
                        metadata={
                            "name": "tpIntermedio",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    cnpj: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "CNPJ",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "max_length": 14,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{14}",
                        }
                    )
                    ufterceiro: Optional[TufEmi] = field(
                        default=None,
                        metadata={
                            "name": "UFTerceiro",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    c_exportador: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cExportador",
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
                        :ivar n_adicao: Número da Adição
                        :ivar n_seq_adic: Número seqüencial do item
                            dentro da Adição
                        :ivar c_fabricante: Código do fabricante
                            estrangeiro (usado nos sistemas internos de
                            informação do emitente da NF-e)
                        :ivar v_desc_di: Valor do desconto do item da DI
                            – adição
                        :ivar n_draw: Número do ato concessório de
                            Drawback
                        """
                        n_adicao: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "nAdicao",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"[1-9]{1}[0-9]{0,2}",
                            }
                        )
                        n_seq_adic: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "nSeqAdic",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[1-9]{1}[0-9]{0,4}",
                            }
                        )
                        c_fabricante: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "cFabricante",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "min_length": 1,
                                "max_length": 60,
                                "white_space": "preserve",
                                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                            }
                        )
                        v_desc_di: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vDescDI",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        n_draw: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "nDraw",
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
                    :ivar n_draw: Número do ato concessório de Drawback
                    :ivar export_ind: Exportação indireta
                    """
                    n_draw: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nDraw",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "min_length": 1,
                            "max_length": 20,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    export_ind: Optional["Tnfe.InfNfe.Det.Prod.DetExport.ExportInd"] = field(
                        default=None,
                        metadata={
                            "name": "exportInd",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )

                    @dataclass
                    class ExportInd:
                        """
                        :ivar n_re: Registro de exportação
                        :ivar ch_nfe: Chave de acesso da NF-e recebida
                            para exportação
                        :ivar q_export: Quantidade do item efetivamente
                            exportado
                        """
                        n_re: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "nRE",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{0,12}",
                            }
                        )
                        ch_nfe: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "chNFe",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "max_length": 44,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{44}",
                            }
                        )
                        q_export: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qExport",
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
                    :ivar n_lote: Número do lote do produto.
                    :ivar q_lote: Quantidade de produto no lote.
                    :ivar d_fab: Data de fabricação/produção. Formato
                        "AAAA-MM-DD".
                    :ivar d_val: Data de validade. Informar o último dia
                        do mês caso a validade não especifique o dia.
                        Formato "AAAA-MM-DD".
                    :ivar c_agreg:
                    """
                    n_lote: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nLote",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 20,
                        }
                    )
                    q_lote: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "qLote",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,7}(\.[0-9]{1,3})?",
                        }
                    )
                    d_fab: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "dFab",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    d_val: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "dVal",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                        }
                    )
                    c_agreg: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cAgreg",
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
                    :ivar c_prod_fisco: Código Fiscal do Produto
                    :ivar c_oper_nff: Código da operação selecionada na
                        NFF e relacionada ao item
                    """
                    c_prod_fisco: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cProdFisco",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "length": 14,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    c_oper_nff: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cOperNFF",
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
                    :ivar x_emb: Embalagem do produto
                    :ivar q_vol_emb: Volume do produto na embalagem
                    :ivar u_emb: Unidade de Medida da Embalagem
                    """
                    x_emb: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "xEmb",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 8,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    q_vol_emb: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "qVolEmb",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,7}(\.[0-9]{1,3})?",
                        }
                    )
                    u_emb: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "uEmb",
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
                    :ivar tp_op: Tipo da Operação (1 - Venda
                        concessionária; 2 - Faturamento direto; 3 -
                        Venda direta; 0 - Outros)
                    :ivar chassi: Chassi do veículo - VIN (código-
                        identificação-veículo)
                    :ivar c_cor: Cor do veículo (código de cada
                        montadora)
                    :ivar x_cor: Descrição da cor
                    :ivar pot: Potência máxima do motor do veículo em
                        cavalo vapor (CV). (potência-veículo)
                    :ivar cilin: Capacidade voluntária do motor expressa
                        em centímetros cúbicos (CC). (cilindradas)
                    :ivar peso_l: Peso líquido
                    :ivar peso_b: Peso bruto
                    :ivar n_serie: Serial (série)
                    :ivar tp_comb: Tipo de combustível-Tabela RENAVAM:
                        01-Álcool; 02-Gasolina; 03-Diesel;
                        16-Álcool/Gas.; 17-Gas./Álcool/GNV;
                        18-Gasolina/Elétrico
                    :ivar n_motor: Número do motor
                    :ivar cmt: CMT-Capacidade Máxima de Tração - em
                        Toneladas 4 casas decimais
                    :ivar dist: Distância entre eixos
                    :ivar ano_mod: Ano Modelo de Fabricação
                    :ivar ano_fab: Ano de Fabricação
                    :ivar tp_pint: Tipo de pintura
                    :ivar tp_veic: Tipo de veículo (utilizar tabela
                        RENAVAM)
                    :ivar esp_veic: Espécie de veículo (utilizar tabela
                        RENAVAM)
                    :ivar vin: Informa-se o veículo tem VIN (chassi)
                        remarcado. R-Remarcado N-NormalVIN
                    :ivar cond_veic: Condição do veículo (1 - acabado; 2
                        - inacabado; 3 - semi-acabado)
                    :ivar c_mod: Código Marca Modelo (utilizar tabela
                        RENAVAM)
                    :ivar c_cor_denatran: Código da Cor Segundo as
                        regras de pré-cadastro do DENATRAN:
                        01-AMARELO;02-AZUL;03-BEGE;04-BRANCA;05-CINZA;06-DOURADA;07-GRENA
                        08-LARANJA;09-MARROM;10-PRATA;11-PRETA;12-ROSA;13-ROXA;14-VERDE;15-VERMELHA;16-FANTASIA
                    :ivar lota: Quantidade máxima de permitida de
                        passageiros sentados, inclusive motorista.
                    :ivar tp_rest: Restrição 0 - Não há; 1 - Alienação
                        Fiduciária; 2 - Arrendamento Mercantil; 3 -
                        Reserva de Domínio; 4 - Penhor de Veículos; 9 -
                        outras.
                    """
                    tp_op: Optional[VeicProdTpOp] = field(
                        default=None,
                        metadata={
                            "name": "tpOp",
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
                    c_cor: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cCor",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                    peso_l: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "pesoL",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 9,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    peso_b: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "pesoB",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 9,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    n_serie: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nSerie",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 9,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    tp_comb: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "tpComb",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 2,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    n_motor: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nMotor",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 21,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    cmt: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "CMT",
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
                    ano_mod: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "anoMod",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{4}",
                        }
                    )
                    ano_fab: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "anoFab",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{4}",
                        }
                    )
                    tp_pint: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "tpPint",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "length": 1,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    tp_veic: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "tpVeic",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,2}",
                        }
                    )
                    esp_veic: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "espVeic",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1}",
                        }
                    )
                    vin: Optional[VeicProdVin] = field(
                        default=None,
                        metadata={
                            "name": "VIN",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "length": 1,
                        }
                    )
                    cond_veic: Optional[VeicProdCondVeic] = field(
                        default=None,
                        metadata={
                            "name": "condVeic",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    c_mod: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cMod",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,6}",
                        }
                    )
                    c_cor_denatran: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cCorDENATRAN",
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
                    tp_rest: Optional[VeicProdTpRest] = field(
                        default=None,
                        metadata={
                            "name": "tpRest",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )

                @dataclass
                class Med:
                    """
                    :ivar c_prod_anvisa: Utilizar o número do registro
                        ANVISA  ou preencher com o literal “ISENTO”, no
                        caso de medicamento isento de registro na
                        ANVISA.
                    :ivar x_motivo_isencao: Obs.: Para medicamento
                        isento de registro na ANVISA, informar o número
                        da decisão que o isenta, como por exemplo o
                        número da Resolução da Diretoria Colegiada da
                        ANVISA (RDC).
                    :ivar v_pmc: Preço Máximo ao Consumidor.
                    """
                    c_prod_anvisa: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cProdANVISA",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{13}|ISENTO",
                        }
                    )
                    x_motivo_isencao: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "xMotivoIsencao",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "min_length": 1,
                            "max_length": 255,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    v_pmc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vPMC",
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
                    :ivar tp_arma: Indicador do tipo de arma de fogo (0
                        - Uso permitido; 1 - Uso restrito)
                    :ivar n_serie: Número de série da arma
                    :ivar n_cano: Número de série do cano
                    :ivar descr: Descrição completa da arma,
                        compreendendo: calibre, marca, capacidade, tipo
                        de funcionamento, comprimento e demais elementos
                        que permitam a sua perfeita identificação.
                    """
                    tp_arma: Optional[ArmaTpArma] = field(
                        default=None,
                        metadata={
                            "name": "tpArma",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    n_serie: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nSerie",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 1,
                            "max_length": 15,
                            "white_space": "preserve",
                            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                        }
                    )
                    n_cano: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nCano",
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
                    :ivar c_prod_anp: Código de produto da ANP.
                        codificação de produtos do SIMP
                        (http://www.anp.gov.br)
                    :ivar desc_anp: Descrição do Produto conforme ANP.
                        Utilizar a descrição de produtos do Sistema de
                        Informações de Movimentação de Produtos - SIMP
                        (http://www.anp.gov.br/simp/).
                    :ivar p_glp: Percentual do GLP derivado do petróleo
                        no produto GLP (cProdANP=210203001). Informar em
                        número decimal o percentual do GLP derivado de
                        petróleo no produto GLP. Valores 0 a 100.
                    :ivar p_gnn: Percentual de gás natural nacional -
                        GLGNn para o produto GLP (cProdANP=210203001).
                        Informar em número decimal o percentual do Gás
                        Natural Nacional - GLGNn para o produto GLP.
                        Valores de 0 a 100.
                    :ivar p_gni: Percentual de gás natural importado
                        GLGNi para o produto GLP (cProdANP=210203001).
                        Informar em número deciaml o percentual do Gás
                        Natural Importado - GLGNi para o produto GLP.
                        Valores de 0 a 100.
                    :ivar v_part: Valor de partida (cProdANP=210203001).
                        Deve ser informado neste campo o valor por
                        quilograma sem ICMS.
                    :ivar codif: Código de autorização / registro do
                        CODIF. Informar apenas quando a UF utilizar o
                        CODIF (Sistema de Controle do
                        Diferimento do Imposto nas Operações com AEAC -
                        Álcool Etílico Anidro Combustível).
                    :ivar q_temp: Quantidade de combustível faturada à
                        temperatura ambiente. Informar quando a
                        quantidade faturada informada no campo qCom
                        (I10) tiver sido ajustada para uma temperatura
                        diferente da ambiente.
                    :ivar ufcons: Sigla da UF de Consumo
                    :ivar cide: CIDE Combustíveis
                    :ivar encerrante: Informações do grupo de
                        "encerrante"
                    """
                    c_prod_anp: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cProdANP",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{9}",
                        }
                    )
                    desc_anp: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "descANP",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "min_length": 2,
                            "max_length": 95,
                        }
                    )
                    p_glp: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "pGLP",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0(\.[0-9]{2,4})?|[1-9]{1}[0-9]{0,1}(\.[0-9]{2,4})?|100(\.0{2,4})?",
                        }
                    )
                    p_gnn: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "pGNn",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0(\.[0-9]{2,4})?|[1-9]{1}[0-9]{0,1}(\.[0-9]{2,4})?|100(\.0{2,4})?",
                        }
                    )
                    p_gni: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "pGNi",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0(\.[0-9]{2,4})?|[1-9]{1}[0-9]{0,1}(\.[0-9]{2,4})?|100(\.0{2,4})?",
                        }
                    )
                    v_part: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vPart",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    codif: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "CODIF",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,21}",
                        }
                    )
                    q_temp: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "qTemp",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[1-9]{1}[0-9]{3}|0\.[0-9]{3}[1-9]{1}|0\.[0-9]{2}[1-9]{1}[0-9]{1}|0\.[0-9]{1}[1-9]{1}[0-9]{2}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?",
                        }
                    )
                    ufcons: Optional[Tuf] = field(
                        default=None,
                        metadata={
                            "name": "UFCons",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                        }
                    )
                    cide: Optional["Tnfe.InfNfe.Det.Prod.Comb.Cide"] = field(
                        default=None,
                        metadata={
                            "name": "CIDE",
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
                        :ivar q_bcprod: BC do CIDE ( Quantidade
                            comercializada)
                        :ivar v_aliq_prod: Alíquota do CIDE  (em reais)
                        :ivar v_cide: Valor do CIDE
                        """
                        q_bcprod: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qBCProd",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?",
                            }
                        )
                        v_aliq_prod: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vAliqProd",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                            }
                        )
                        v_cide: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vCIDE",
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
                        :ivar n_bico: Numero de identificação do Bico
                            utilizado no abastecimento
                        :ivar n_bomba: Numero de identificação da bomba
                            ao qual o bico está interligado
                        :ivar n_tanque: Numero de identificação do
                            tanque ao qual o bico está interligado
                        :ivar v_enc_ini: Valor do Encerrante no ínicio
                            do abastecimento
                        :ivar v_enc_fin: Valor do Encerrante no final do
                            abastecimento
                        """
                        n_bico: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "nBico",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{1,3}",
                            }
                        )
                        n_bomba: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "nBomba",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"[0-9]{1,3}",
                            }
                        )
                        n_tanque: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "nTanque",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"[0-9]{1,3}",
                            }
                        )
                        v_enc_ini: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vEncIni",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?",
                            }
                        )
                        v_enc_fin: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vEncFin",
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
                :ivar v_tot_trib: Valor estimado total de impostos
                    federais, estaduais e municipais
                :ivar icms: Dados do ICMS Normal e ST
                :ivar ipi:
                :ivar ii: Dados do Imposto de Importação
                :ivar issqn: ISSQN
                :ivar pis: Dados do PIS
                :ivar pisst: Dados do PIS Substituição Tributária
                :ivar cofins: Dados do COFINS
                :ivar cofinsst: Dados do COFINS da Substituição
                    Tributaria;
                :ivar icmsufdest: Grupo a ser informado nas vendas
                    interestarduais para consumidor final, não
                    contribuinte de ICMS
                """
                v_tot_trib: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vTotTrib",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                icms: Optional["Tnfe.InfNfe.Det.Imposto.Icms"] = field(
                    default=None,
                    metadata={
                        "name": "ICMS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                ipi: Optional[Tipi] = field(
                    default=None,
                    metadata={
                        "name": "IPI",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                ii: Optional["Tnfe.InfNfe.Det.Imposto.Ii"] = field(
                    default=None,
                    metadata={
                        "name": "II",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                issqn: Optional["Tnfe.InfNfe.Det.Imposto.Issqn"] = field(
                    default=None,
                    metadata={
                        "name": "ISSQN",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                pis: Optional["Tnfe.InfNfe.Det.Imposto.Pis"] = field(
                    default=None,
                    metadata={
                        "name": "PIS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                pisst: Optional["Tnfe.InfNfe.Det.Imposto.Pisst"] = field(
                    default=None,
                    metadata={
                        "name": "PISST",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                cofins: Optional["Tnfe.InfNfe.Det.Imposto.Cofins"] = field(
                    default=None,
                    metadata={
                        "name": "COFINS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                cofinsst: Optional["Tnfe.InfNfe.Det.Imposto.Cofinsst"] = field(
                    default=None,
                    metadata={
                        "name": "COFINSST",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )
                icmsufdest: Optional["Tnfe.InfNfe.Det.Imposto.Icmsufdest"] = field(
                    default=None,
                    metadata={
                        "name": "ICMSUFDest",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )

                @dataclass
                class Pis:
                    """
                    :ivar pisaliq: Código de Situação Tributária do PIS.
                        01 – Operação Tributável - Base de Cálculo =
                        Valor da Operação Alíquota Normal
                        (Cumulativo/Não Cumulativo); 02 - Operação
                        Tributável - Base de Calculo = Valor da Operação
                        (Alíquota Diferenciada);
                    :ivar pisqtde: Código de Situação Tributária do PIS.
                        03 - Operação Tributável - Base de Calculo =
                        Quantidade Vendida x Alíquota por Unidade de
                        Produto;
                    :ivar pisnt: Código de Situação Tributária do PIS.
                        04 - Operação Tributável - Tributação Monofásica
                        - (Alíquota Zero); 06 - Operação Tributável -
                        Alíquota Zero; 07 - Operação Isenta da
                        contribuição; 08 - Operação Sem Incidência da
                        contribuição; 09 - Operação com suspensão da
                        contribuição;
                    :ivar pisoutr: Código de Situação Tributária do PIS.
                        99 - Outras Operações.
                    """
                    pisaliq: Optional["Tnfe.InfNfe.Det.Imposto.Pis.Pisaliq"] = field(
                        default=None,
                        metadata={
                            "name": "PISAliq",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    pisqtde: Optional["Tnfe.InfNfe.Det.Imposto.Pis.Pisqtde"] = field(
                        default=None,
                        metadata={
                            "name": "PISQtde",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    pisnt: Optional["Tnfe.InfNfe.Det.Imposto.Pis.Pisnt"] = field(
                        default=None,
                        metadata={
                            "name": "PISNT",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    pisoutr: Optional["Tnfe.InfNfe.Det.Imposto.Pis.Pisoutr"] = field(
                        default=None,
                        metadata={
                            "name": "PISOutr",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )

                    @dataclass
                    class Pisaliq:
                        """
                        :ivar cst: Código de Situação Tributária do PIS.
                            01 – Operação Tributável - Base de Cálculo =
                            Valor da Operação Alíquota Normal
                            (Cumulativo/Não Cumulativo); 02 - Operação
                            Tributável - Base de Calculo = Valor da
                            Operação (Alíquota Diferenciada);
                        :ivar v_bc: Valor da BC do PIS
                        :ivar p_pis: Alíquota do PIS (em percentual)
                        :ivar v_pis: Valor do PIS
                        """
                        cst: Optional[PisaliqCst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        v_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_pis: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pPIS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_pis: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vPIS",
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
                        :ivar cst: Código de Situação Tributária do PIS.
                            03 - Operação Tributável - Base de Calculo =
                            Quantidade Vendida x Alíquota por Unidade de
                            Produto;
                        :ivar q_bcprod: Quantidade Vendida  (NT2011/004)
                        :ivar v_aliq_prod: Alíquota do PIS (em reais)
                            (NT2011/004)
                        :ivar v_pis: Valor do PIS
                        """
                        cst: Optional[PisqtdeCst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        q_bcprod: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qBCProd",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?",
                            }
                        )
                        v_aliq_prod: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vAliqProd",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?",
                            }
                        )
                        v_pis: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vPIS",
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
                        :ivar cst: Código de Situação Tributária do PIS.
                            04 - Operação Tributável - Tributação
                            Monofásica - (Alíquota Zero); 05 - Operação
                            Tributável (ST); 06 - Operação Tributável -
                            Alíquota Zero; 07 - Operação Isenta da
                            contribuição; 08 - Operação Sem Incidência
                            da contribuição; 09 - Operação com suspensão
                            da contribuição;
                        """
                        cst: Optional[PisntCst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )

                    @dataclass
                    class Pisoutr:
                        """
                        :ivar cst: Código de Situação Tributária do PIS.
                            99 - Outras Operações.
                        :ivar v_bc: Valor da BC do PIS
                        :ivar p_pis: Alíquota do PIS (em percentual)
                        :ivar q_bcprod: Quantidade Vendida (NT2011/004)
                        :ivar v_aliq_prod: Alíquota do PIS (em reais)
                            (NT2011/004)
                        :ivar v_pis: Valor do PIS
                        """
                        cst: Optional[PisoutrCst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        v_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_pis: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pPIS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        q_bcprod: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qBCProd",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?",
                            }
                        )
                        v_aliq_prod: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vAliqProd",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?",
                            }
                        )
                        v_pis: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vPIS",
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
                    :ivar v_bc: Valor da BC do PIS ST
                    :ivar p_pis: Alíquota do PIS ST (em percentual)
                    :ivar q_bcprod: Quantidade Vendida
                    :ivar v_aliq_prod: Alíquota do PIS ST (em reais)
                    :ivar v_pis: Valor do PIS ST
                    :ivar ind_soma_pisst: Indica se o valor do PISST
                        compõe o valor total da NF-e
                    """
                    v_bc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vBC",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    p_pis: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "pPIS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    q_bcprod: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "qBCProd",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?",
                        }
                    )
                    v_aliq_prod: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vAliqProd",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                        }
                    )
                    v_pis: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vPIS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    ind_soma_pisst: Optional[PisstIndSomaPisst] = field(
                        default=None,
                        metadata={
                            "name": "indSomaPISST",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                        }
                    )

                @dataclass
                class Cofins:
                    """
                    :ivar cofinsaliq: Código de Situação Tributária do
                        COFINS. 01 – Operação Tributável - Base de
                        Cálculo = Valor da Operação Alíquota Normal
                        (Cumulativo/Não Cumulativo); 02 - Operação
                        Tributável - Base de Calculo = Valor da Operação
                        (Alíquota Diferenciada);
                    :ivar cofinsqtde: Código de Situação Tributária do
                        COFINS. 03 - Operação Tributável - Base de
                        Calculo = Quantidade Vendida x Alíquota por
                        Unidade de Produto;
                    :ivar cofinsnt: Código de Situação Tributária do
                        COFINS: 04 - Operação Tributável - Tributação
                        Monofásica - (Alíquota Zero); 06 - Operação
                        Tributável - Alíquota Zero; 07 - Operação Isenta
                        da contribuição; 08 - Operação Sem Incidência da
                        contribuição; 09 - Operação com suspensão da
                        contribuição;
                    :ivar cofinsoutr: Código de Situação Tributária do
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
                    cofinsaliq: Optional["Tnfe.InfNfe.Det.Imposto.Cofins.Cofinsaliq"] = field(
                        default=None,
                        metadata={
                            "name": "COFINSAliq",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    cofinsqtde: Optional["Tnfe.InfNfe.Det.Imposto.Cofins.Cofinsqtde"] = field(
                        default=None,
                        metadata={
                            "name": "COFINSQtde",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    cofinsnt: Optional["Tnfe.InfNfe.Det.Imposto.Cofins.Cofinsnt"] = field(
                        default=None,
                        metadata={
                            "name": "COFINSNT",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    cofinsoutr: Optional["Tnfe.InfNfe.Det.Imposto.Cofins.Cofinsoutr"] = field(
                        default=None,
                        metadata={
                            "name": "COFINSOutr",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )

                    @dataclass
                    class Cofinsaliq:
                        """
                        :ivar cst: Código de Situação Tributária do
                            COFINS. 01 – Operação Tributável - Base de
                            Cálculo = Valor da Operação Alíquota Normal
                            (Cumulativo/Não Cumulativo); 02 - Operação
                            Tributável - Base de Calculo = Valor da
                            Operação (Alíquota Diferenciada);
                        :ivar v_bc: Valor da BC do COFINS
                        :ivar p_cofins: Alíquota do COFINS (em
                            percentual)
                        :ivar v_cofins: Valor do COFINS
                        """
                        cst: Optional[CofinsaliqCst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        v_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_cofins: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pCOFINS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_cofins: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vCOFINS",
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
                        :ivar cst: Código de Situação Tributária do
                            COFINS. 03 - Operação Tributável - Base de
                            Calculo = Quantidade Vendida x Alíquota por
                            Unidade de Produto;
                        :ivar q_bcprod: Quantidade Vendida (NT2011/004)
                        :ivar v_aliq_prod: Alíquota do COFINS (em reais)
                            (NT2011/004)
                        :ivar v_cofins: Valor do COFINS
                        """
                        cst: Optional[CofinsqtdeCst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        q_bcprod: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qBCProd",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?",
                            }
                        )
                        v_aliq_prod: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vAliqProd",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?",
                            }
                        )
                        v_cofins: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vCOFINS",
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
                        :ivar cst: Código de Situação Tributária do
                            COFINS: 04 - Operação Tributável -
                            Tributação Monofásica - (Alíquota Zero); 05
                            - Operação Tributável (ST); 06 - Operação
                            Tributável - Alíquota Zero; 07 - Operação
                            Isenta da contribuição; 08 - Operação Sem
                            Incidência da contribuição; 09 - Operação
                            com suspensão da contribuição;
                        """
                        cst: Optional[CofinsntCst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )

                    @dataclass
                    class Cofinsoutr:
                        """
                        :ivar cst: Código de Situação Tributária do
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
                        :ivar v_bc: Valor da BC do COFINS
                        :ivar p_cofins: Alíquota do COFINS (em
                            percentual)
                        :ivar q_bcprod: Quantidade Vendida (NT2011/004)
                        :ivar v_aliq_prod: Alíquota do COFINS (em reais)
                            (NT2011/004)
                        :ivar v_cofins: Valor do COFINS
                        """
                        cst: Optional[CofinsoutrCst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        v_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_cofins: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pCOFINS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        q_bcprod: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "qBCProd",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{1,4})?",
                            }
                        )
                        v_aliq_prod: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vAliqProd",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,4})?",
                            }
                        )
                        v_cofins: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vCOFINS",
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
                    :ivar v_bc: Valor da BC do COFINS ST
                    :ivar p_cofins: Alíquota do COFINS ST(em percentual)
                    :ivar q_bcprod: Quantidade Vendida
                    :ivar v_aliq_prod: Alíquota do COFINS ST(em reais)
                    :ivar v_cofins: Valor do COFINS ST
                    :ivar ind_soma_cofinsst: Indica se o valor da COFINS
                        ST compõe o valor total da NFe
                    """
                    v_bc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vBC",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    p_cofins: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "pCOFINS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    q_bcprod: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "qBCProd",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{1,4}|[1-9]{1}[0-9]{0,11}|[1-9]{1}[0-9]{0,11}(\.[0-9]{4})?",
                        }
                    )
                    v_aliq_prod: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vAliqProd",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                        }
                    )
                    v_cofins: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vCOFINS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    ind_soma_cofinsst: Optional[CofinsstIndSomaCofinsst] = field(
                        default=None,
                        metadata={
                            "name": "indSomaCOFINSST",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                        }
                    )

                @dataclass
                class Icmsufdest:
                    """
                    :ivar v_bcufdest: Valor da Base de Cálculo do ICMS
                        na UF do destinatário.
                    :ivar v_bcfcpufdest: Valor da Base de Cálculo do FCP
                        na UF do destinatário.
                    :ivar p_fcpufdest: Percentual adicional inserido na
                        alíquota interna da UF de destino, relativo ao
                        Fundo de Combate à Pobreza (FCP) naquela UF.
                    :ivar p_icmsufdest: Alíquota adotada nas operações
                        internas na UF do destinatário para o produto /
                        mercadoria.
                    :ivar p_icmsinter: Alíquota interestadual das UF
                        envolvidas: - 4% alíquota interestadual para
                        produtos importados; - 7% para os Estados de
                        origem do Sul e Sudeste (exceto ES), destinado
                        para os Estados do Norte e Nordeste  ou ES; -
                        12% para os demais casos.
                    :ivar p_icmsinter_part: Percentual de partilha para
                        a UF do destinatário: - 40% em 2016; - 60% em
                        2017; - 80% em 2018; - 100% a partir de 2019.
                    :ivar v_fcpufdest: Valor do ICMS relativo ao Fundo
                        de Combate à Pobreza (FCP) da UF de destino.
                    :ivar v_icmsufdest: Valor do ICMS de partilha para a
                        UF do destinatário.
                    :ivar v_icmsufremet: Valor do ICMS de partilha para
                        a UF do remetente. Nota: A partir de 2019, este
                        valor será zero.
                    """
                    v_bcufdest: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vBCUFDest",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_bcfcpufdest: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vBCFCPUFDest",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    p_fcpufdest: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "pFCPUFDest",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    p_icmsufdest: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "pICMSUFDest",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    p_icmsinter: Optional[IcmsufdestPIcmsinter] = field(
                        default=None,
                        metadata={
                            "name": "pICMSInter",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    p_icmsinter_part: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "pICMSInterPart",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    v_fcpufdest: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vFCPUFDest",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_icmsufdest: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vICMSUFDest",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_icmsufremet: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vICMSUFRemet",
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
                    :ivar icms00: Tributação pelo ICMS 00 - Tributada
                        integralmente
                    :ivar icms10: Tributação pelo ICMS 10 - Tributada e
                        com cobrança do ICMS por substituição tributária
                    :ivar icms20: Tributção pelo ICMS 20 - Com redução
                        de base de cálculo
                    :ivar icms30: Tributação pelo ICMS 30 - Isenta ou
                        não tributada e com cobrança do ICMS por
                        substituição tributária
                    :ivar icms40: Tributação pelo ICMS 40 - Isenta 41 -
                        Não tributada 50 - Suspensão
                    :ivar icms51: Tributção pelo ICMS 51 - Diferimento A
                        exigência do preenchimento das informações do
                        ICMS diferido fica à critério de cada UF.
                    :ivar icms60: Tributação pelo ICMS 60 - ICMS cobrado
                        anteriormente por substituição tributária
                    :ivar icms70: Tributação pelo ICMS 70 - Com redução
                        de base de cálculo e cobrança do ICMS por
                        substituição tributária
                    :ivar icms90: Tributação pelo ICMS 90 - Outras
                    :ivar icmspart: Partilha do ICMS entre a UF de
                        origem e UF de destino ou a UF definida na
                        legislação Operação interestadual para
                        consumidor final com partilha do ICMS  devido na
                        operação entre a UF de origem e a UF do
                        destinatário ou ou a UF definida na legislação.
                        (Ex. UF da concessionária de entrega do
                        veículos)
                    :ivar icmsst: Grupo de informação do ICMSST devido
                        para a UF de destino, nas operações
                        interestaduais de produtos que tiveram retenção
                        antecipada de ICMS por ST na UF do remetente.
                        Repasse via Substituto Tributário.
                    :ivar icmssn101: Tributação do ICMS pelo SIMPLES
                        NACIONAL e CSOSN=101 (v.2.0)
                    :ivar icmssn102: Tributação do ICMS pelo SIMPLES
                        NACIONAL e CSOSN=102, 103, 300 ou 400 (v.2.0))
                    :ivar icmssn201: Tributação do ICMS pelo SIMPLES
                        NACIONAL e CSOSN=201 (v.2.0)
                    :ivar icmssn202: Tributação do ICMS pelo SIMPLES
                        NACIONAL e CSOSN=202 ou 203 (v.2.0)
                    :ivar icmssn500: Tributação do ICMS pelo SIMPLES
                        NACIONAL,CRT=1 – Simples Nacional e CSOSN=500
                        (v.2.0)
                    :ivar icmssn900: Tributação do ICMS pelo SIMPLES
                        NACIONAL, CRT=1 – Simples Nacional e CSOSN=900
                        (v2.0)
                    """
                    icms00: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms00"] = field(
                        default=None,
                        metadata={
                            "name": "ICMS00",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icms10: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms10"] = field(
                        default=None,
                        metadata={
                            "name": "ICMS10",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icms20: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms20"] = field(
                        default=None,
                        metadata={
                            "name": "ICMS20",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icms30: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms30"] = field(
                        default=None,
                        metadata={
                            "name": "ICMS30",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icms40: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms40"] = field(
                        default=None,
                        metadata={
                            "name": "ICMS40",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icms51: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms51"] = field(
                        default=None,
                        metadata={
                            "name": "ICMS51",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icms60: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms60"] = field(
                        default=None,
                        metadata={
                            "name": "ICMS60",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icms70: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms70"] = field(
                        default=None,
                        metadata={
                            "name": "ICMS70",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icms90: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icms90"] = field(
                        default=None,
                        metadata={
                            "name": "ICMS90",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icmspart: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmspart"] = field(
                        default=None,
                        metadata={
                            "name": "ICMSPart",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icmsst: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmsst"] = field(
                        default=None,
                        metadata={
                            "name": "ICMSST",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icmssn101: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmssn101"] = field(
                        default=None,
                        metadata={
                            "name": "ICMSSN101",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icmssn102: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmssn102"] = field(
                        default=None,
                        metadata={
                            "name": "ICMSSN102",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icmssn201: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmssn201"] = field(
                        default=None,
                        metadata={
                            "name": "ICMSSN201",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icmssn202: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmssn202"] = field(
                        default=None,
                        metadata={
                            "name": "ICMSSN202",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icmssn500: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmssn500"] = field(
                        default=None,
                        metadata={
                            "name": "ICMSSN500",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                        }
                    )
                    icmssn900: Optional["Tnfe.InfNfe.Det.Imposto.Icms.Icmssn900"] = field(
                        default=None,
                        metadata={
                            "name": "ICMSSN900",
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
                        :ivar cst: Tributção pelo ICMS 00 - Tributada
                            integralmente
                        :ivar mod_bc: Modalidade de determinação da BC
                            do ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar v_bc: Valor da BC do ICMS
                        :ivar p_icms: Alíquota do ICMS
                        :ivar v_icms: Valor do ICMS
                        :ivar p_fcp: Percentual de ICMS relativo ao
                            Fundo de Combate à Pobreza (FCP).
                        :ivar v_fcp: Valor do ICMS relativo ao Fundo de
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
                        cst: Optional[Icms00Cst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        mod_bc: Optional[Icms00ModBc] = field(
                            default=None,
                            metadata={
                                "name": "modBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        v_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icms: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCP",
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
                        :ivar cst: 10 - Tributada e com cobrança do ICMS
                            por substituição tributária
                        :ivar mod_bc: Modalidade de determinação da BC
                            do ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar v_bc: Valor da BC do ICMS
                        :ivar p_icms: Alíquota do ICMS
                        :ivar v_icms: Valor do ICMS
                        :ivar v_bcfcp: Valor da Base de cálculo do FCP.
                        :ivar p_fcp: Percentual de ICMS relativo ao
                            Fundo de Combate à Pobreza (FCP).
                        :ivar v_fcp: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        :ivar mod_bcst: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor) 6-Valor da Operação;
                        :ivar p_mvast: Percentual da Margem de Valor
                            Adicionado ICMS ST
                        :ivar p_red_bcst: Percentual de redução da BC
                            ICMS ST
                        :ivar v_bcst: Valor da BC do ICMS ST
                        :ivar p_icmsst: Alíquota do ICMS ST
                        :ivar v_icmsst: Valor do ICMS ST
                        :ivar v_bcfcpst: Valor da Base de cálculo do FCP
                            retido por substituicao tributaria.
                        :ivar p_fcpst: Percentual de FCP retido por
                            substituição tributária.
                        :ivar v_fcpst: Valor do FCP retido por
                            substituição tributária.
                        :ivar v_icmsstdeson: Valor do ICMS-ST
                            desonerado.
                        :ivar mot_des_icmsst: Motivo da desoneração do
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
                        cst: Optional[Icms10Cst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        mod_bc: Optional[Icms10ModBc] = field(
                            default=None,
                            metadata={
                                "name": "modBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        v_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icms: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        mod_bcst: Optional[Icms10ModBcst] = field(
                            default=None,
                            metadata={
                                "name": "modBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        p_mvast: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pMVAST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        p_red_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_icmsstdeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSSTDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        mot_des_icmsst: Optional[Icms10MotDesIcmsst] = field(
                            default=None,
                            metadata={
                                "name": "motDesICMSST",
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
                        :ivar cst: Tributção pelo ICMS 20 - Com redução
                            de base de cálculo
                        :ivar mod_bc: Modalidade de determinação da BC
                            do ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar p_red_bc: Percentual de redução da BC
                        :ivar v_bc: Valor da BC do ICMS
                        :ivar p_icms: Alíquota do ICMS
                        :ivar v_icms: Valor do ICMS
                        :ivar v_bcfcp: Valor da Base de cálculo do FCP.
                        :ivar p_fcp: Percentual de ICMS relativo ao
                            Fundo de Combate à Pobreza (FCP).
                        :ivar v_fcp: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        :ivar v_icmsdeson: Valor do ICMS de desoneração
                        :ivar mot_des_icms: Motivo da desoneração do
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
                        cst: Optional[Icms20Cst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        mod_bc: Optional[Icms20ModBc] = field(
                            default=None,
                            metadata={
                                "name": "modBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        p_red_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icms: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_icmsdeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        mot_des_icms: Optional[Icms20MotDesIcms] = field(
                            default=None,
                            metadata={
                                "name": "motDesICMS",
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
                        :ivar cst: Tributção pelo ICMS 30 - Isenta ou
                            não tributada e com cobrança do ICMS por
                            substituição tributária
                        :ivar mod_bcst: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor). 6 - Valor da Operação
                        :ivar p_mvast: Percentual da Margem de Valor
                            Adicionado ICMS ST
                        :ivar p_red_bcst: Percentual de redução da BC
                            ICMS ST
                        :ivar v_bcst: Valor da BC do ICMS ST
                        :ivar p_icmsst: Alíquota do ICMS ST
                        :ivar v_icmsst: Valor do ICMS ST
                        :ivar v_bcfcpst: Valor da Base de cálculo do
                            FCP.
                        :ivar p_fcpst: Percentual de FCP retido por
                            substituição tributária.
                        :ivar v_fcpst: Valor do FCP retido por
                            substituição tributária.
                        :ivar v_icmsdeson: Valor do ICMS de desoneração
                        :ivar mot_des_icms: Motivo da desoneração do
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
                        cst: Optional[Icms30Cst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        mod_bcst: Optional[Icms30ModBcst] = field(
                            default=None,
                            metadata={
                                "name": "modBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        p_mvast: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pMVAST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        p_red_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_icmsdeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        mot_des_icms: Optional[Icms30MotDesIcms] = field(
                            default=None,
                            metadata={
                                "name": "motDesICMS",
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
                        :ivar cst: Tributação pelo ICMS 40 - Isenta 41 -
                            Não tributada 50 - Suspensão 51 -
                            Diferimento
                        :ivar v_icmsdeson: O valor do ICMS será
                            informado apenas nas operações com veículos
                            beneficiados com a desoneração condicional
                            do ICMS.
                        :ivar mot_des_icms: Este campo será preenchido
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
                        cst: Optional[Icms40Cst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        v_icmsdeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        mot_des_icms: Optional[Icms40MotDesIcms] = field(
                            default=None,
                            metadata={
                                "name": "motDesICMS",
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
                        :ivar cst: Tributção pelo ICMS 20 - Com redução
                            de base de cálculo
                        :ivar mod_bc: Modalidade de determinação da BC
                            do ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar p_red_bc: Percentual de redução da BC
                        :ivar v_bc: Valor da BC do ICMS
                        :ivar p_icms: Alíquota do imposto
                        :ivar v_icmsop: Valor do ICMS da Operação
                        :ivar p_dif: Percentual do diferemento
                        :ivar v_icmsdif: Valor do ICMS da diferido
                        :ivar v_icms: Valor do ICMS
                        :ivar v_bcfcp: Valor da Base de cálculo do FCP.
                        :ivar p_fcp: Percentual de ICMS relativo ao
                            Fundo de Combate à Pobreza (FCP).
                        :ivar v_fcp: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        :ivar p_fcpdif: Percentual do diferimento do
                            ICMS relativo ao Fundo de Combate à Pobreza
                            (FCP).
                        :ivar v_fcpdif: Valor do ICMS relativo ao Fundo
                            de Combate à Pobreza (FCP) diferido.
                        :ivar v_fcpefet: Valor efetivo do ICMS relativo
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
                        cst: Optional[Icms51Cst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        mod_bc: Optional[Icms51ModBc] = field(
                            default=None,
                            metadata={
                                "name": "modBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        p_red_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icms: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmsop: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSOp",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_dif: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pDif",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0(\.[0-9]{2,4})?|[1-9]{1}[0-9]{0,1}(\.[0-9]{2,4})?|100(\.0{2,4})?",
                            }
                        )
                        v_icmsdif: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSDif",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_icms: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcpdif: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCPDif",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcpdif: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCPDif",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_fcpefet: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCPEfet",
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
                        :ivar cst: Tributação pelo ICMS 60 - ICMS
                            cobrado anteriormente por substituição
                            tributária
                        :ivar v_bcstret: Valor da BC do ICMS ST retido
                            anteriormente
                        :ivar p_st: Aliquota suportada pelo consumidor
                            final.
                        :ivar v_icmssubstituto: Valor do ICMS Próprio do
                            Substituto cobrado em operação anterior
                        :ivar v_icmsstret: Valor do ICMS ST retido
                            anteriormente
                        :ivar v_bcfcpstret: Valor da Base de cálculo do
                            FCP retido anteriormente por ST.
                        :ivar p_fcpstret: Percentual de FCP retido
                            anteriormente por substituição tributária.
                        :ivar v_fcpstret: Valor do FCP retido por
                            substituição tributária.
                        :ivar p_red_bcefet: Percentual de redução da
                            base de cálculo efetiva.
                        :ivar v_bcefet: Valor da base de cálculo
                            efetiva.
                        :ivar p_icmsefet: Alíquota do ICMS efetiva.
                        :ivar v_icmsefet: Valor do ICMS efetivo.
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        cst: Optional[Icms60Cst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        v_bcstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_st: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmssubstituto: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSSubstituto",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_icmsstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcpstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCPSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcpstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCPSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcpstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCPSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_red_bcefet: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBCEfet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bcefet: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCEfet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icmsefet: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMSEfet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmsefet: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSEfet",
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
                        :ivar cst: Tributção pelo ICMS 70 - Com redução
                            de base de cálculo e cobrança do ICMS por
                            substituição tributária
                        :ivar mod_bc: Modalidade de determinação da BC
                            do ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar p_red_bc: Percentual de redução da BC
                        :ivar v_bc: Valor da BC do ICMS
                        :ivar p_icms: Alíquota do ICMS
                        :ivar v_icms: Valor do ICMS
                        :ivar v_bcfcp: Valor da Base de cálculo do FCP.
                        :ivar p_fcp: Percentual de ICMS relativo ao
                            Fundo de Combate à Pobreza (FCP).
                        :ivar v_fcp: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        :ivar mod_bcst: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor); 6 - Valor da Operação.
                        :ivar p_mvast: Percentual da Margem de Valor
                            Adicionado ICMS ST
                        :ivar p_red_bcst: Percentual de redução da BC
                            ICMS ST
                        :ivar v_bcst: Valor da BC do ICMS ST
                        :ivar p_icmsst: Alíquota do ICMS ST
                        :ivar v_icmsst: Valor do ICMS ST
                        :ivar v_bcfcpst: Valor da Base de cálculo do FCP
                            retido por substituição tributária.
                        :ivar p_fcpst: Percentual de FCP retido por
                            substituição tributária.
                        :ivar v_fcpst: Valor do FCP retido por
                            substituição tributária.
                        :ivar v_icmsdeson: Valor do ICMS de desoneração
                        :ivar mot_des_icms: Motivo da desoneração do
                            ICMS:3-Uso na
                            agropecuária;9-Outros;12-Fomento
                            agropecuário
                        :ivar v_icmsstdeson: Valor do ICMS-ST
                            desonerado.
                        :ivar mot_des_icmsst: Motivo da desoneração do
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
                        cst: Optional[Icms70Cst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        mod_bc: Optional[Icms70ModBc] = field(
                            default=None,
                            metadata={
                                "name": "modBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        p_red_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icms: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        mod_bcst: Optional[Icms70ModBcst] = field(
                            default=None,
                            metadata={
                                "name": "modBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        p_mvast: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pMVAST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        p_red_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_icmsdeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        mot_des_icms: Optional[Icms70MotDesIcms] = field(
                            default=None,
                            metadata={
                                "name": "motDesICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        v_icmsstdeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSSTDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        mot_des_icmsst: Optional[Icms70MotDesIcmsst] = field(
                            default=None,
                            metadata={
                                "name": "motDesICMSST",
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
                        :ivar cst: Tributção pelo ICMS 90 - Outras
                        :ivar mod_bc: Modalidade de determinação da BC
                            do ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar v_bc: Valor da BC do ICMS
                        :ivar p_red_bc: Percentual de redução da BC
                        :ivar p_icms: Alíquota do ICMS
                        :ivar v_icms: Valor do ICMS
                        :ivar v_bcfcp: Valor da Base de cálculo do FCP.
                        :ivar p_fcp: Percentual de ICMS relativo ao
                            Fundo de Combate à Pobreza (FCP).
                        :ivar v_fcp: Valor do ICMS relativo ao Fundo de
                            Combate à Pobreza (FCP).
                        :ivar mod_bcst: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor); 6 - Valor da Operação.
                        :ivar p_mvast: Percentual da Margem de Valor
                            Adicionado ICMS ST
                        :ivar p_red_bcst: Percentual de redução da BC
                            ICMS ST
                        :ivar v_bcst: Valor da BC do ICMS ST
                        :ivar p_icmsst: Alíquota do ICMS ST
                        :ivar v_icmsst: Valor do ICMS ST
                        :ivar v_bcfcpst: Valor da Base de cálculo do
                            FCP.
                        :ivar p_fcpst: Percentual de FCP retido por
                            substituição tributária.
                        :ivar v_fcpst: Valor do FCP retido por
                            substituição tributária.
                        :ivar v_icmsdeson: Valor do ICMS de desoneração
                        :ivar mot_des_icms: Motivo da desoneração do
                            ICMS:3-Uso na
                            agropecuária;9-Outros;12-Fomento
                            agropecuário
                        :ivar v_icmsstdeson: Valor do ICMS-ST
                            desonerado.
                        :ivar mot_des_icmsst: Motivo da desoneração do
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
                        cst: Optional[Icms90Cst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        mod_bc: Optional[Icms90ModBc] = field(
                            default=None,
                            metadata={
                                "name": "modBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        v_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_red_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        p_icms: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icms: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcp: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCP",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        mod_bcst: Optional[Icms90ModBcst] = field(
                            default=None,
                            metadata={
                                "name": "modBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        p_mvast: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pMVAST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        p_red_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_icmsdeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        mot_des_icms: Optional[Icms90MotDesIcms] = field(
                            default=None,
                            metadata={
                                "name": "motDesICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        v_icmsstdeson: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSSTDeson",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        mot_des_icmsst: Optional[Icms90MotDesIcmsst] = field(
                            default=None,
                            metadata={
                                "name": "motDesICMSST",
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
                        :ivar cst: Tributação pelo ICMS 10 - Tributada e
                            com cobrança do ICMS por substituição
                            tributária; 90 – Outros.
                        :ivar mod_bc: Modalidade de determinação da BC
                            do ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar v_bc: Valor da BC do ICMS
                        :ivar p_red_bc: Percentual de redução da BC
                        :ivar p_icms: Alíquota do ICMS
                        :ivar v_icms: Valor do ICMS
                        :ivar mod_bcst: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor). 6 - Valor da Operação
                        :ivar p_mvast: Percentual da Margem de Valor
                            Adicionado ICMS ST
                        :ivar p_red_bcst: Percentual de redução da BC
                            ICMS ST
                        :ivar v_bcst: Valor da BC do ICMS ST
                        :ivar p_icmsst: Alíquota do ICMS ST
                        :ivar v_icmsst: Valor do ICMS ST
                        :ivar p_bcop: Percentual para determinação do
                            valor  da Base de Cálculo da operação
                            própria.
                        :ivar ufst: Sigla da UF para qual é devido o
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
                        cst: Optional[IcmspartCst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        mod_bc: Optional[IcmspartModBc] = field(
                            default=None,
                            metadata={
                                "name": "modBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        v_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_red_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        p_icms: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icms: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        mod_bcst: Optional[IcmspartModBcst] = field(
                            default=None,
                            metadata={
                                "name": "modBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        p_mvast: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pMVAST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        p_red_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_bcop: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pBCOp",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        ufst: Optional[Tuf] = field(
                            default=None,
                            metadata={
                                "name": "UFST",
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
                        :ivar cst: Tributção pelo ICMS 41-Não Tributado.
                            60-Cobrado anteriormente por substituição
                            tributária.
                        :ivar v_bcstret: Informar o valor da BC do ICMS
                            ST retido na UF remetente
                        :ivar p_st: Aliquota suportada pelo consumidor
                            final.
                        :ivar v_icmssubstituto: Valor do ICMS Próprio do
                            Substituto cobrado em operação anterior
                        :ivar v_icmsstret: Informar o valor do ICMS ST
                            retido na UF remetente (iv2.0))
                        :ivar v_bcfcpstret: Informar o valor da Base de
                            Cálculo do FCP retido anteriormente por ST.
                        :ivar p_fcpstret: Percentual relativo ao Fundo
                            de Combate à Pobreza (FCP) retido por
                            substituição tributária.
                        :ivar v_fcpstret: Valor do ICMS relativo ao
                            Fundo de Combate à Pobreza (FCP) retido por
                            substituição tributária.
                        :ivar v_bcstdest: Informar o valor da BC do ICMS
                            ST da UF destino
                        :ivar v_icmsstdest: Informar o valor da BC do
                            ICMS ST da UF destino (v2.0)
                        :ivar p_red_bcefet: Percentual de redução da
                            base de cálculo efetiva.
                        :ivar v_bcefet: Valor da base de cálculo
                            efetiva.
                        :ivar p_icmsefet: Alíquota do ICMS efetivo.
                        :ivar v_icmsefet: Valor do ICMS efetivo.
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        cst: Optional[IcmsstCst] = field(
                            default=None,
                            metadata={
                                "name": "CST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        v_bcstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_st: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmssubstituto: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSSubstituto",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_icmsstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcpstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCPSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcpstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCPSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcpstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCPSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcstdest: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCSTDest",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_icmsstdest: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSSTDest",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_red_bcefet: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBCEfet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bcefet: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCEfet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icmsefet: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMSEfet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmsefet: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSEfet",
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
                        :ivar csosn: 101- Tributada pelo Simples
                            Nacional com permissão de crédito. (v.2.0)
                        :ivar p_cred_sn: Alíquota aplicável de cálculo
                            do crédito (Simples Nacional). (v2.0)
                        :ivar v_cred_icmssn: Valor crédito do ICMS que
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
                        csosn: Optional[Icmssn101Csosn] = field(
                            default=None,
                            metadata={
                                "name": "CSOSN",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        p_cred_sn: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pCredSN",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_cred_icmssn: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vCredICMSSN",
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
                        :ivar csosn: 102- Tributada pelo Simples
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
                        csosn: Optional[Icmssn102Csosn] = field(
                            default=None,
                            metadata={
                                "name": "CSOSN",
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
                        :ivar csosn: 201- Tributada pelo Simples
                            Nacional com permissão de crédito e com
                            cobrança do ICMS por Substituição Tributária
                            (v.2.0)
                        :ivar mod_bcst: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor). (v2.0) 6 - Valor da Operação
                        :ivar p_mvast: Percentual da Margem de Valor
                            Adicionado ICMS ST (v2.0)
                        :ivar p_red_bcst: Percentual de redução da BC
                            ICMS ST  (v2.0)
                        :ivar v_bcst: Valor da BC do ICMS ST (v2.0)
                        :ivar p_icmsst: Alíquota do ICMS ST (v2.0)
                        :ivar v_icmsst: Valor do ICMS ST (v2.0)
                        :ivar v_bcfcpst: Valor da Base de cálculo do
                            FCP.
                        :ivar p_fcpst: Percentual de FCP retido por
                            substituição tributária.
                        :ivar v_fcpst: Valor do FCP retido por
                            substituição tributária.
                        :ivar p_cred_sn: Alíquota aplicável de cálculo
                            do crédito (Simples Nacional). (v2.0)
                        :ivar v_cred_icmssn: Valor crédito do ICMS que
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
                        csosn: Optional[Icmssn201Csosn] = field(
                            default=None,
                            metadata={
                                "name": "CSOSN",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        mod_bcst: Optional[Icmssn201ModBcst] = field(
                            default=None,
                            metadata={
                                "name": "modBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        p_mvast: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pMVAST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        p_red_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_cred_sn: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pCredSN",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_cred_icmssn: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vCredICMSSN",
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
                        :ivar csosn: 202- Tributada pelo Simples
                            Nacional sem permissão de crédito e com
                            cobrança do ICMS por Substituição
                            Tributária; 203-  Isenção do ICMS nos
                            Simples Nacional para faixa de receita bruta
                            e com cobrança do ICMS por Substituição
                            Tributária (v.2.0)
                        :ivar mod_bcst: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor). (v2.0) 6 - Valor da Operação
                        :ivar p_mvast: Percentual da Margem de Valor
                            Adicionado ICMS ST (v2.0)
                        :ivar p_red_bcst: Percentual de redução da BC
                            ICMS ST  (v2.0)
                        :ivar v_bcst: Valor da BC do ICMS ST (v2.0)
                        :ivar p_icmsst: Alíquota do ICMS ST (v2.0)
                        :ivar v_icmsst: Valor do ICMS ST (v2.0)
                        :ivar v_bcfcpst: Valor da Base de cálculo do
                            FCP.
                        :ivar p_fcpst: Percentual de FCP retido por
                            substituição tributária.
                        :ivar v_fcpst: Valor do FCP retido por
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
                        csosn: Optional[Icmssn202Csosn] = field(
                            default=None,
                            metadata={
                                "name": "CSOSN",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        mod_bcst: Optional[Icmssn202ModBcst] = field(
                            default=None,
                            metadata={
                                "name": "modBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        p_mvast: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pMVAST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        p_red_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCPST",
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
                        :ivar csosn: 500 – ICMS cobrado anterirmente por
                            substituição tributária (substituído) ou por
                            antecipação (v.2.0)
                        :ivar v_bcstret: Valor da BC do ICMS ST retido
                            anteriormente (v2.0)
                        :ivar p_st: Aliquota suportada pelo consumidor
                            final.
                        :ivar v_icmssubstituto: Valor do ICMS próprio do
                            substituto
                        :ivar v_icmsstret: Valor do ICMS ST retido
                            anteriormente  (v2.0)
                        :ivar v_bcfcpstret: Valor da Base de cálculo do
                            FCP retido anteriormente.
                        :ivar p_fcpstret: Percentual de FCP retido
                            anteriormente por substituição tributária.
                        :ivar v_fcpstret: Valor do FCP retido por
                            substituição tributária.
                        :ivar p_red_bcefet: Percentual de redução da
                            base de cálculo efetiva.
                        :ivar v_bcefet: Valor da base de cálculo
                            efetiva.
                        :ivar p_icmsefet: Alíquota do ICMS efetiva.
                        :ivar v_icmsefet: Valor do ICMS efetivo.
                        """
                        orig: Optional[Torig] = field(
                            default=None,
                            metadata={
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                            }
                        )
                        csosn: Optional[Icmssn500Csosn] = field(
                            default=None,
                            metadata={
                                "name": "CSOSN",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        v_bcstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_st: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmssubstituto: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSSubstituto",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_icmsstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcpstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCPSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcpstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCPSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcpstret: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCPSTRet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_red_bcefet: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBCEfet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bcefet: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCEfet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icmsefet: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMSEfet",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmsefet: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSEfet",
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
                        :ivar csosn: Tributação pelo ICMS 900 -
                            Outros(v2.0)
                        :ivar mod_bc: Modalidade de determinação da BC
                            do ICMS: 0 - Margem Valor Agregado (%); 1 -
                            Pauta (valor); 2 - Preço Tabelado Máximo
                            (valor); 3 - Valor da Operação.
                        :ivar v_bc: Valor da BC do ICMS
                        :ivar p_red_bc: Percentual de redução da BC
                        :ivar p_icms: Alíquota do ICMS
                        :ivar v_icms: Valor do ICMS
                        :ivar mod_bcst: Modalidade de determinação da BC
                            do ICMS ST: 0 – Preço tabelado ou máximo
                            sugerido; 1 - Lista Negativa (valor); 2 -
                            Lista Positiva (valor); 3 - Lista Neutra
                            (valor); 4 - Margem Valor Agregado (%); 5 -
                            Pauta (valor). 6 - Valor da Operação
                        :ivar p_mvast: Percentual da Margem de Valor
                            Adicionado ICMS ST
                        :ivar p_red_bcst: Percentual de redução da BC
                            ICMS ST
                        :ivar v_bcst: Valor da BC do ICMS ST
                        :ivar p_icmsst: Alíquota do ICMS ST
                        :ivar v_icmsst: Valor do ICMS ST
                        :ivar v_bcfcpst: Valor da Base de cálculo do
                            FCP.
                        :ivar p_fcpst: Percentual de FCP retido por
                            substituição tributária.
                        :ivar v_fcpst: Valor do FCP retido por
                            substituição tributária.
                        :ivar p_cred_sn: Alíquota aplicável de cálculo
                            do crédito (Simples Nacional). (v2.0)
                        :ivar v_cred_icmssn: Valor crédito do ICMS que
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
                        csosn: Optional[Icmssn900Csosn] = field(
                            default=None,
                            metadata={
                                "name": "CSOSN",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "required": True,
                                "white_space": "preserve",
                            }
                        )
                        mod_bc: Optional[Icmssn900ModBc] = field(
                            default=None,
                            metadata={
                                "name": "modBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        v_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_red_bc: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBC",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        p_icms: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icms: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMS",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        mod_bcst: Optional[Icmssn900ModBcst] = field(
                            default=None,
                            metadata={
                                "name": "modBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                            }
                        )
                        p_mvast: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pMVAST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        p_red_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pRedBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_bcst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_icmsst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vICMSST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        v_bcfcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vBCFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_fcpst: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vFCPST",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )
                        p_cred_sn: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "pCredSN",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                            }
                        )
                        v_cred_icmssn: Optional[str] = field(
                            default=None,
                            metadata={
                                "name": "vCredICMSSN",
                                "type": "Element",
                                "namespace": "http://www.portalfiscal.inf.br/nfe",
                                "white_space": "preserve",
                                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                            }
                        )

                @dataclass
                class Ii:
                    """
                    :ivar v_bc: Base da BC do Imposto de Importação
                    :ivar v_desp_adu: Valor das despesas aduaneiras
                    :ivar v_ii: Valor do Imposto de Importação
                    :ivar v_iof: Valor do Imposto sobre Operações
                        Financeiras
                    """
                    v_bc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vBC",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_desp_adu: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vDespAdu",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_ii: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vII",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_iof: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vIOF",
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
                    :ivar v_bc: Valor da BC do ISSQN
                    :ivar v_aliq: Alíquota do ISSQN
                    :ivar v_issqn: Valor da do ISSQN
                    :ivar c_mun_fg: Informar o município de ocorrência
                        do fato gerador do ISSQN. Utilizar a Tabela do
                        IBGE (Anexo VII - Tabela de UF, Município e
                        País). “Atenção, não vincular com os campos B12,
                        C10 ou E10” v2.0
                    :ivar c_list_serv: Informar o Item da lista de
                        serviços da LC 116/03 em que se classifica o
                        serviço.
                    :ivar v_deducao: Valor dedução para redução da base
                        de cálculo
                    :ivar v_outro: Valor outras retenções
                    :ivar v_desc_incond: Valor desconto incondicionado
                    :ivar v_desc_cond: Valor desconto condicionado
                    :ivar v_issret: Valor Retenção ISS
                    :ivar ind_iss: Exibilidade do ISS:1-Exigível;2-Não
                        incidente;3-Isenção;4-Exportação;5-Imunidade;6-Exig.Susp.
                        Judicial;7-Exig.Susp. ADM
                    :ivar c_servico: Código do serviço prestado dentro
                        do município
                    :ivar c_mun: Código do Município de Incidência do
                        Imposto
                    :ivar c_pais: Código de Pais
                    :ivar n_processo: Número do Processo administrativo
                        ou judicial de suspenção do processo
                    :ivar ind_incentivo: Indicador de Incentivo Fiscal.
                        1=Sim; 2=Não
                    """
                    v_bc: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vBC",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_aliq: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vAliq",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                        }
                    )
                    v_issqn: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vISSQN",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    c_mun_fg: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cMunFG",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{7}",
                        }
                    )
                    c_list_serv: Optional[TclistServ] = field(
                        default=None,
                        metadata={
                            "name": "cListServ",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                        }
                    )
                    v_deducao: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vDeducao",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_outro: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vOutro",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_desc_incond: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vDescIncond",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_desc_cond: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vDescCond",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    v_issret: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vISSRet",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                        }
                    )
                    ind_iss: Optional[IssqnIndIss] = field(
                        default=None,
                        metadata={
                            "name": "indISS",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    c_servico: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cServico",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "min_length": 1,
                            "max_length": 20,
                            "white_space": "preserve",
                        }
                    )
                    c_mun: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cMun",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{7}",
                        }
                    )
                    c_pais: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cPais",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{1,4}",
                        }
                    )
                    n_processo: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nProcesso",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "min_length": 1,
                            "max_length": 30,
                            "white_space": "preserve",
                        }
                    )
                    ind_incentivo: Optional[IssqnIndIncentivo] = field(
                        default=None,
                        metadata={
                            "name": "indIncentivo",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )

            @dataclass
            class ImpostoDevol:
                """
                :ivar p_devol: Percentual de mercadoria devolvida
                :ivar ipi: Informação de IPI devolvido
                """
                p_devol: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "pDevol",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0(\.[0-9]{2})?|100(\.00)?|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})?",
                    }
                )
                ipi: Optional["Tnfe.InfNfe.Det.ImpostoDevol.Ipi"] = field(
                    default=None,
                    metadata={
                        "name": "IPI",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                    }
                )

                @dataclass
                class Ipi:
                    """
                    :ivar v_ipidevol: Valor do IPI devolvido
                    """
                    v_ipidevol: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "vIPIDevol",
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
            :ivar icmstot: Totais referentes ao ICMS
            :ivar issqntot: Totais referentes ao ISSQN
            :ivar ret_trib: Retenção de Tributos Federais
            """
            icmstot: Optional["Tnfe.InfNfe.Total.Icmstot"] = field(
                default=None,
                metadata={
                    "name": "ICMSTot",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            issqntot: Optional["Tnfe.InfNfe.Total.Issqntot"] = field(
                default=None,
                metadata={
                    "name": "ISSQNtot",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            ret_trib: Optional["Tnfe.InfNfe.Total.RetTrib"] = field(
                default=None,
                metadata={
                    "name": "retTrib",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )

            @dataclass
            class Icmstot:
                """
                :ivar v_bc: BC do ICMS
                :ivar v_icms: Valor Total do ICMS
                :ivar v_icmsdeson: Valor Total do ICMS desonerado
                :ivar v_fcpufdest: Valor total do ICMS relativo ao Fundo
                    de Combate à Pobreza (FCP) para a UF de destino.
                :ivar v_icmsufdest: Valor total do ICMS de partilha para
                    a UF do destinatário
                :ivar v_icmsufremet: Valor total do ICMS de partilha
                    para a UF do remetente
                :ivar v_fcp: Valor Total do FCP (Fundo de Combate à
                    Pobreza).
                :ivar v_bcst: BC do ICMS ST
                :ivar v_st: Valor Total do ICMS ST
                :ivar v_fcpst: Valor Total do FCP (Fundo de Combate à
                    Pobreza) retido por substituição tributária.
                :ivar v_fcpstret: Valor Total do FCP (Fundo de Combate à
                    Pobreza) retido anteriormente por substituição
                    tributária.
                :ivar v_prod: Valor Total dos produtos e serviços
                :ivar v_frete: Valor Total do Frete
                :ivar v_seg: Valor Total do Seguro
                :ivar v_desc: Valor Total do Desconto
                :ivar v_ii: Valor Total do II
                :ivar v_ipi: Valor Total do IPI
                :ivar v_ipidevol: Valor Total do IPI devolvido. Deve ser
                    informado quando preenchido o Grupo Tributos
                    Devolvidos na emissão de nota finNFe=4 (devolução)
                    nas operações com não contribuintes do IPI.
                    Corresponde ao total da soma dos campos id: UA04.
                :ivar v_pis: Valor do PIS
                :ivar v_cofins: Valor do COFINS
                :ivar v_outro: Outras Despesas acessórias
                :ivar v_nf: Valor Total da NF-e
                :ivar v_tot_trib: Valor estimado total de impostos
                    federais, estaduais e municipais
                """
                v_bc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vBC",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_icmsdeson: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vICMSDeson",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_fcpufdest: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vFCPUFDest",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_icmsufdest: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vICMSUFDest",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_icmsufremet: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vICMSUFRemet",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_fcp: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vFCP",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_fcpst: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vFCPST",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_fcpstret: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vFCPSTRet",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_seg: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vSeg",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_desc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vDesc",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_ii: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vII",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_ipi: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vIPI",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_ipidevol: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vIPIDevol",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_pis: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vPIS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_cofins: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vCOFINS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_outro: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vOutro",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_tot_trib: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vTotTrib",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

            @dataclass
            class Issqntot:
                """
                :ivar v_serv: Valor Total dos Serviços sob não-
                    incidência ou não tributados pelo ICMS
                :ivar v_bc: Base de Cálculo do ISS
                :ivar v_iss: Valor Total do ISS
                :ivar v_pis: Valor do PIS sobre serviços
                :ivar v_cofins: Valor do COFINS sobre serviços
                :ivar d_compet: Data da prestação do serviço  (AAAA-MM-
                    DD)
                :ivar v_deducao: Valor dedução para redução da base de
                    cálculo
                :ivar v_outro: Valor outras retenções
                :ivar v_desc_incond: Valor desconto incondicionado
                :ivar v_desc_cond: Valor desconto condicionado
                :ivar v_issret: Valor Total Retenção ISS
                :ivar c_reg_trib: Código do regime especial de
                    tributação
                """
                v_serv: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vServ",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_bc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vBC",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_iss: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vISS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_pis: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vPIS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_cofins: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vCOFINS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                d_compet: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "dCompet",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                    }
                )
                v_deducao: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vDeducao",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_outro: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vOutro",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_desc_incond: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vDescIncond",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_desc_cond: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vDescCond",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_issret: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vISSRet",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                c_reg_trib: Optional[IssqntotCRegTrib] = field(
                    default=None,
                    metadata={
                        "name": "cRegTrib",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                    }
                )

            @dataclass
            class RetTrib:
                """
                :ivar v_ret_pis: Valor Retido de PIS
                :ivar v_ret_cofins: Valor Retido de COFINS
                :ivar v_ret_csll: Valor Retido de CSLL
                :ivar v_bcirrf: Base de Cálculo do IRRF
                :ivar v_irrf: Valor Retido de IRRF
                :ivar v_bcret_prev: Base de Cálculo da Retenção da
                    Previdêncica Social
                :ivar v_ret_prev: Valor da Retenção da Previdêncica
                    Social
                """
                v_ret_pis: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vRetPIS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_ret_cofins: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vRetCOFINS",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_ret_csll: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vRetCSLL",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_bcirrf: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vBCIRRF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_irrf: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vIRRF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_bcret_prev: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vBCRetPrev",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_ret_prev: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vRetPrev",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0\.[0-9]{1}[1-9]{1}|0\.[1-9]{1}[0-9]{1}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

        @dataclass
        class Transp:
            """
            :ivar mod_frete: Modalidade do frete 0- Contratação do Frete
                por conta do Remetente (CIF); 1- Contratação do Frete
                por conta do destinatário/remetente (FOB); 2-
                Contratação do Frete por conta de terceiros; 3-
                Transporte próprio por conta do remetente; 4- Transporte
                próprio por conta do destinatário; 9- Sem Ocorrência de
                transporte.
            :ivar transporta: Dados do transportador
            :ivar ret_transp: Dados da retenção  ICMS do Transporte
            :ivar veic_transp: Dados do veículo
            :ivar reboque: Dados do reboque/Dolly (v2.0)
            :ivar vagao: Identificação do vagão (v2.0)
            :ivar balsa: Identificação da balsa (v2.0)
            :ivar vol: Dados dos volumes
            """
            mod_frete: Optional[TranspModFrete] = field(
                default=None,
                metadata={
                    "name": "modFrete",
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
            ret_transp: Optional["Tnfe.InfNfe.Transp.RetTransp"] = field(
                default=None,
                metadata={
                    "name": "retTransp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                }
            )
            veic_transp: Optional[Tveiculo] = field(
                default=None,
                metadata={
                    "name": "veicTransp",
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
                :ivar cnpj: CNPJ do transportador
                :ivar cpf: CPF do transportador
                :ivar x_nome: Razão Social ou nome do transportador
                :ivar ie: Inscrição Estadual (v2.0)
                :ivar x_ender: Endereço completo
                :ivar x_mun: Nome do munícipio
                :ivar uf: Sigla da UF
                """
                cnpj: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CNPJ",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_length": 14,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{14}",
                    }
                )
                cpf: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CPF",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_length": 11,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{11}",
                    }
                )
                x_nome: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xNome",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                ie: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "IE",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "max_length": 14,
                        "white_space": "preserve",
                        "pattern": r"ISENTO|[0-9]{2,14}",
                    }
                )
                x_ender: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xEnder",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                x_mun: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xMun",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                    }
                )

            @dataclass
            class RetTransp:
                """
                :ivar v_serv: Valor do Serviço
                :ivar v_bcret: BC da Retenção do ICMS
                :ivar p_icmsret: Alíquota da Retenção
                :ivar v_icmsret: Valor do ICMS Retido
                :ivar cfop: Código Fiscal de Operações e Prestações
                :ivar c_mun_fg: Código do Município de Ocorrência do
                    Fato Gerador (utilizar a tabela do IBGE)
                """
                v_serv: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vServ",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_bcret: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vBCRet",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                p_icmsret: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "pICMSRet",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2,4}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2,4})?",
                    }
                )
                v_icmsret: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vICMSRet",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                cfop: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CFOP",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[1,2,3,5,6,7]{1}[0-9]{3}",
                    }
                )
                c_mun_fg: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "cMunFG",
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
                :ivar q_vol: Quantidade de volumes transportados
                :ivar esp: Espécie dos volumes transportados
                :ivar marca: Marca dos volumes transportados
                :ivar n_vol: Numeração dos volumes transportados
                :ivar peso_l: Peso líquido (em kg)
                :ivar peso_b: Peso bruto (em kg)
                :ivar lacres:
                """
                q_vol: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "qVol",
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
                n_vol: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nVol",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                peso_l: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "pesoL",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{3}|[1-9]{1}[0-9]{0,11}(\.[0-9]{3})?",
                    }
                )
                peso_b: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "pesoB",
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
                    :ivar n_lacre: Número dos Lacres
                    """
                    n_lacre: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "nLacre",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_desc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vDesc",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )
                v_liq: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vLiq",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                    }
                )

            @dataclass
            class Dup:
                """
                :ivar n_dup: Número da duplicata
                :ivar d_venc: Data de vencimento da duplicata (AAAA-MM-
                    DD)
                :ivar v_dup: Valor da duplicata
                """
                n_dup: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nDup",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                        "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
                    }
                )
                v_dup: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vDup",
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
            :ivar det_pag: Grupo de detalhamento da forma de pagamento.
            :ivar v_troco: Valor do Troco.
            """
            det_pag: List["Tnfe.InfNfe.Pag.DetPag"] = field(
                default_factory=list,
                metadata={
                    "name": "detPag",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_occurs": 1,
                    "max_occurs": 100,
                }
            )
            v_troco: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vTroco",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )

            @dataclass
            class DetPag:
                """
                :ivar ind_pag: Indicador da Forma de
                    Pagamento:0-Pagamento à Vista;1-Pagamento à Prazo;
                :ivar t_pag: Forma de Pagamento:
                :ivar x_pag: Descrição do Meio de Pagamento
                :ivar v_pag: Valor do Pagamento. Esta tag poderá ser
                    omitida quando a tag tPag=90 (Sem Pagamento), caso
                    contrário deverá ser preenchida.
                :ivar card: Grupo de Cartões
                """
                ind_pag: Optional[DetPagIndPag] = field(
                    default=None,
                    metadata={
                        "name": "indPag",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "white_space": "preserve",
                    }
                )
                t_pag: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "tPag",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                        "pattern": r"[0-9]{2}",
                    }
                )
                x_pag: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xPag",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "min_length": 2,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                v_pag: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vPag",
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
                    :ivar tp_integra: Tipo de Integração do processo de
                        pagamento com o sistema de automação da empresa/
                        1=Pagamento integrado com o sistema de automação
                        da empresa Ex. equipamento TEF , Comercio
                        Eletronico 2=Pagamento não integrado com o
                        sistema de automação da empresa Ex: equipamento
                        POS
                    :ivar cnpj: CNPJ da instituição de pagamento
                    :ivar t_band: Bandeira da operadora de cartão
                    :ivar c_aut: Número de autorização da operação
                        cartão de crédito/débito
                    """
                    tp_integra: Optional[CardTpIntegra] = field(
                        default=None,
                        metadata={
                            "name": "tpIntegra",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "required": True,
                            "white_space": "preserve",
                        }
                    )
                    cnpj: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "CNPJ",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "max_length": 14,
                            "white_space": "preserve",
                            "pattern": r"[0-9]{14}",
                        }
                    )
                    t_band: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "tBand",
                            "type": "Element",
                            "namespace": "http://www.portalfiscal.inf.br/nfe",
                            "white_space": "preserve",
                            "pattern": r"[0-9]{2}",
                        }
                    )
                    c_aut: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "cAut",
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
            :ivar cnpj: CNPJ do Intermediador da Transação (agenciador,
                plataforma de delivery, marketplace e similar) de
                serviços e de negócios.
            :ivar id_cad_int_tran: Identificador cadastrado no
                intermediador
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            id_cad_int_tran: Optional[str] = field(
                default=None,
                metadata={
                    "name": "idCadIntTran",
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
            :ivar inf_ad_fisco: Informações adicionais de interesse do
                Fisco (v2.0)
            :ivar inf_cpl: Informações complementares de interesse do
                Contribuinte
            :ivar obs_cont: Campo de uso livre do contribuinte informar
                o nome do campo no atributo xCampo e o conteúdo do campo
                no xTexto
            :ivar obs_fisco: Campo de uso exclusivo do Fisco informar o
                nome do campo no atributo xCampo e o conteúdo do campo
                no xTexto
            :ivar proc_ref: Grupo de informações do  processo
                referenciado
            """
            inf_ad_fisco: Optional[str] = field(
                default=None,
                metadata={
                    "name": "infAdFisco",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 5000,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            obs_cont: List["Tnfe.InfNfe.InfAdic.ObsCont"] = field(
                default_factory=list,
                metadata={
                    "name": "obsCont",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_occurs": 10,
                }
            )
            obs_fisco: List["Tnfe.InfNfe.InfAdic.ObsFisco"] = field(
                default_factory=list,
                metadata={
                    "name": "obsFisco",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_occurs": 10,
                }
            )
            proc_ref: List["Tnfe.InfNfe.InfAdic.ProcRef"] = field(
                default_factory=list,
                metadata={
                    "name": "procRef",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "max_occurs": 100,
                }
            )

            @dataclass
            class ObsCont:
                x_texto: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xTexto",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            class ObsFisco:
                x_texto: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xTexto",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            class ProcRef:
                """
                :ivar n_proc: Indentificador do processo ou ato
                    concessório
                :ivar ind_proc: Origem do processo, informar com: 0 -
                    SEFAZ; 1 - Justiça Federal; 2 - Justiça Estadual; 3
                    - Secex/RFB; 9 - Outros
                """
                n_proc: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "nProc",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                ind_proc: Optional[ProcRefIndProc] = field(
                    default=None,
                    metadata={
                        "name": "indProc",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "white_space": "preserve",
                    }
                )

        @dataclass
        class Exporta:
            """
            :ivar ufsaida_pais: Sigla da UF de Embarque ou de
                transposição de fronteira
            :ivar x_loc_exporta: Local de Embarque ou de transposição de
                fronteira
            :ivar x_loc_despacho: Descrição do local de despacho
            """
            ufsaida_pais: Optional[TufEmi] = field(
                default=None,
                metadata={
                    "name": "UFSaidaPais",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                }
            )
            x_loc_exporta: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xLocExporta",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_loc_despacho: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xLocDespacho",
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
            :ivar x_nemp: Informação da Nota de Empenho de compras
                públicas (NT2011/004)
            :ivar x_ped: Informação do pedido
            :ivar x_cont: Informação do contrato
            """
            x_nemp: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNEmp",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 22,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_ped: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xPed",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_length": 1,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            x_cont: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xCont",
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
            :ivar for_dia: Fornecimentos diários
            :ivar q_tot_mes: Total do mês
            :ivar q_tot_ant: Total Anterior
            :ivar q_tot_ger: Total Geral
            :ivar deduc: Deduções - Taxas e Contribuições
            :ivar v_for: Valor  dos fornecimentos
            :ivar v_tot_ded: Valor Total das Deduções
            :ivar v_liq_for: Valor Líquido dos fornecimentos
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
            for_dia: List["Tnfe.InfNfe.Cana.ForDia"] = field(
                default_factory=list,
                metadata={
                    "name": "forDia",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "min_occurs": 1,
                    "max_occurs": 31,
                }
            )
            q_tot_mes: Optional[str] = field(
                default=None,
                metadata={
                    "name": "qTotMes",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?",
                }
            )
            q_tot_ant: Optional[str] = field(
                default=None,
                metadata={
                    "name": "qTotAnt",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{1,10}|[1-9]{1}[0-9]{0,10}|[1-9]{1}[0-9]{0,10}(\.[0-9]{1,10})?",
                }
            )
            q_tot_ger: Optional[str] = field(
                default=None,
                metadata={
                    "name": "qTotGer",
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
            v_for: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vFor",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_tot_ded: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vTotDed",
                    "type": "Element",
                    "namespace": "http://www.portalfiscal.inf.br/nfe",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
                }
            )
            v_liq_for: Optional[str] = field(
                default=None,
                metadata={
                    "name": "vLiqFor",
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
                :ivar x_ded: Descrição da Dedução
                :ivar v_ded: valor da dedução
                """
                x_ded: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "xDed",
                        "type": "Element",
                        "namespace": "http://www.portalfiscal.inf.br/nfe",
                        "required": True,
                        "min_length": 1,
                        "max_length": 60,
                        "white_space": "preserve",
                        "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                    }
                )
                v_ded: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "vDed",
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
            :ivar x_solic: Solicitação do pedido de emissão da NFF
            """
            x_solic: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xSolic",
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
        :ivar qr_code: Texto com o QR-Code impresso no DANFE NFC-e
        :ivar url_chave: Informar a URL da "Consulta por chave de acesso
            da NFC-e". A mesma URL que deve estar informada no DANFE
            NFC-e para consulta por chave de acesso.
        """
        qr_code: Optional[str] = field(
            default=None,
            metadata={
                "name": "qrCode",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 100,
                "max_length": 600,
                "white_space": "preserve",
                "pattern": r"(((HTTPS?|https?)://.*\?chNFe=[0-9]{44}&nVersao=100&tpAmb=[1-2](&cDest=([A-Za-z0-9.:+-/)(]{0}|[A-Za-z0-9.:+-/)(]{5,20})?)?&dhEmi=[A-Fa-f0-9]{50}&vNF=(0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?)&vICMS=(0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?)&digVal=[A-Fa-f0-9]{56}&cIdToken=[0-9]{6}&cHashQRCode=[A-Fa-f0-9]{40})|((HTTPS?|https?)://.*\?p=([0-9]{34}(1|4)[0-9]{9})\|[2]\|[1-2]\|(0|[1-9]{1}([0-9]{1,5})?)\|[A-Fa-f0-9]{40})|((HTTPS?|https?)://.*\?p=([0-9]{34}9[0-9]{9})\|[2]\|[1-2]\|([0]{1}[1-9]{1}|[1-2]{1}[0-9]{1}|[3]{1}[0-1]{1})\|(0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?)\|[A-Fa-f0-9]{56}\|(0|[1-9]{1}([0-9]{1,5})?)\|[A-Fa-f0-9]{40}))",
            }
        )
        url_chave: Optional[str] = field(
            default=None,
            metadata={
                "name": "urlChave",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 21,
                "max_length": 85,
            }
        )


@dataclass
class TretConsReciNfe:
    """
    Tipo Retorno do Pedido de  Consulta do Recido do Lote de Notas Fiscais
    Eletrônicas.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que processou a NF-e
    :ivar n_rec: Número do Recibo Consultado
    :ivar c_stat: Código do status da mensagem enviada.
    :ivar x_motivo: Descrição literal do status do serviço solicitado.
    :ivar c_uf: código da UF de atendimento
    :ivar dh_recbto: Data e hora de processamento, no formato AAAA-MM-
        DDTHH:MM:SSTZD. Em caso de Rejeição, com data e hora do
        recebimento do Lote de NF-e enviado.
    :ivar c_msg: Código da Mensagem (v2.0) alterado para tamanho
        variavel 1-4. (NT2011/004)
    :ivar x_msg: Mensagem da SEFAZ para o emissor. (v2.0)
    :ivar prot_nfe: Protocolo de status resultado do processamento da
        NF-e
    :ivar versao:
    """
    class Meta:
        name = "TRetConsReciNFe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    n_rec: Optional[str] = field(
        default=None,
        metadata={
            "name": "nRec",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "max_length": 15,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    c_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "cStat",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "max_length": 3,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    x_motivo: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMotivo",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_uf: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    dh_recbto: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhRecbto",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    c_msg: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMsg",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{1,4}",
        }
    )
    x_msg: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMsg",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "min_length": 1,
            "max_length": 200,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    prot_nfe: List[TprotNfe] = field(
        default_factory=list,
        metadata={
            "name": "protNFe",
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
            "pattern": r"4\.00",
        }
    )


@dataclass
class TretEnviNfe:
    """
    Tipo Retorno do Pedido de Autorização da Nota Fiscal Eletrônica.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que recebeu o Lote.
    :ivar c_stat: Código do status da mensagem enviada.
    :ivar x_motivo: Descrição literal do status do serviço solicitado.
    :ivar c_uf: código da UF de atendimento
    :ivar dh_recbto: Data e hora do recebimento, no formato AAAA-MM-
        DDTHH:MM:SSTZD
    :ivar inf_rec: Dados do Recibo do Lote
    :ivar prot_nfe: Protocolo de status resultado do processamento
        sincrono da NFC-e
    :ivar versao:
    """
    class Meta:
        name = "TRetEnviNFe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "max_length": 3,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    x_motivo: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMotivo",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_uf: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    dh_recbto: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhRecbto",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    inf_rec: Optional["TretEnviNfe.InfRec"] = field(
        default=None,
        metadata={
            "name": "infRec",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
        }
    )
    prot_nfe: Optional[TprotNfe] = field(
        default=None,
        metadata={
            "name": "protNFe",
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
            "pattern": r"4\.00",
        }
    )

    @dataclass
    class InfRec:
        """
        :ivar n_rec: Número do Recibo
        :ivar t_med: Tempo médio de resposta do serviço (em segundos)
            dos últimos 5 minutos
        """
        n_rec: Optional[str] = field(
            default=None,
            metadata={
                "name": "nRec",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "max_length": 15,
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        t_med: Optional[str] = field(
            default=None,
            metadata={
                "name": "tMed",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{1,4}",
            }
        )


@dataclass
class TenviNfe:
    """
    Tipo Pedido de Concessão de Autorização da Nota Fiscal Eletrônica.

    :ivar id_lote:
    :ivar ind_sinc: Indicador de processamento síncrono. 0=NÃO;
        1=SIM=Síncrono
    :ivar nfe:
    :ivar versao:
    """
    class Meta:
        name = "TEnviNFe"

    id_lote: Optional[str] = field(
        default=None,
        metadata={
            "name": "idLote",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,15}",
        }
    )
    ind_sinc: Optional[TenviNfeIndSinc] = field(
        default=None,
        metadata={
            "name": "indSinc",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
            "white_space": "preserve",
        }
    )
    nfe: List[Tnfe] = field(
        default_factory=list,
        metadata={
            "name": "NFe",
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
            "pattern": r"4\.00",
        }
    )


@dataclass
class TnfeProc:
    """
    Tipo da NF-e processada.
    """
    class Meta:
        name = "TNfeProc"

    nfe: Optional[Tnfe] = field(
        default=None,
        metadata={
            "name": "NFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    prot_nfe: Optional[TprotNfe] = field(
        default=None,
        metadata={
            "name": "protNFe",
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
            "pattern": r"4\.00",
        }
    )
