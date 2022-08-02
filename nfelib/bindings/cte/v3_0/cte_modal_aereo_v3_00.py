from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class InfTotApUniAp(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


class NatCargaCInfManu(Enum):
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
    VALUE_99 = "99"


@dataclass
class Aereo:
    """
    Informações do modal Aéreo.

    :ivar n_minu: Número da Minuta Documento que precede o CT-e,
        assinado pelo expedidor, espécie de pedido de serviço
    :ivar n_oca: Número Operacional do Conhecimento Aéreo Representa o
        número de controle comumente utilizado pelo conhecimento aéreo
        composto por uma sequência numérica de onze dígitos. Os três
        primeiros dígitos representam um código que os operadores de
        transporte aéreo associados à IATA possuem. Em seguida um número
        de série de sete dígitos determinados pelo operador de
        transporte aéreo. Para finalizar, um dígito verificador, que é
        um sistema de módulo sete imponderado o qual divide o número de
        série do conhecimento aéreo por sete e usa o resto como dígito
        de verificação.
    :ivar d_prev_aereo: Data prevista da entrega Formato AAAA-MM-DD
    :ivar nat_carga: Natureza da carga
    :ivar tarifa: Informações de tarifa
    :ivar peri: Preenchido quando for  transporte de produtos
        classificados pela ONU como perigosos. O preenchimento desses
        campos não desobriga a empresa aérea de emitir os demais
        documentos que constam na legislação vigente.
    """
    class Meta:
        name = "aereo"
        namespace = "http://www.portalfiscal.inf.br/cte"

    n_minu: Optional[str] = field(
        default=None,
        metadata={
            "name": "nMinu",
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"[0-9]{9}",
        }
    )
    n_oca: Optional[str] = field(
        default=None,
        metadata={
            "name": "nOCA",
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    d_prev_aereo: Optional[str] = field(
        default=None,
        metadata={
            "name": "dPrevAereo",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
        }
    )
    nat_carga: Optional["Aereo.NatCarga"] = field(
        default=None,
        metadata={
            "name": "natCarga",
            "type": "Element",
            "required": True,
        }
    )
    tarifa: Optional["Aereo.Tarifa"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    peri: List["Aereo.Peri"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class NatCarga:
        """
        :ivar x_dime: Dimensão Formato:1234X1234X1234 (cm). Esse campo
            deve sempre que possível ser preenchido. Entretanto, quando
            for impossível o preenchimento das dimensões, fica
            obrigatório o preenchimento da cubagem em metro cúbico do
            leiaute do CT-e da estrutura genérica (infQ).
        :ivar c_inf_manu: Informações de manuseio 01 - certificado do
            expedidor para embarque de animal vivo; 02 - artigo perigoso
            conforme Declaração do Expedidor anexa; 03 - somente em
            aeronave cargueira; 04 - artigo perigoso - declaração do
            expedidor não requerida; 05 - artigo perigoso em quantidade
            isenta; 06 - gelo seco para refrigeração (especificar no
            campo observações a quantidade); 07 - não restrito
            (especificar a Disposição Especial no campo observações); 08
            - artigo perigoso em carga consolidada (especificar a
            quantidade no campo observações) ; 09 - autorização da
            autoridade governamental anexa (especificar no campo
            observações); 10 – baterias de íons de lítio em conformidade
            com a Seção II da PI965 – CAO ; 11 - baterias de íons de
            lítio em conformidade com a Seção II da PI966 ; 12 -
            baterias de íons de lítio em conformidade com a Seção II da
            PI967 ; 13 – baterias de metal lítio em conformidade com a
            Seção II da PI968 — CAO; 14 - baterias de metal lítio em
            conformidade com a Seção II da PI969; 15 - baterias de metal
            lítio em conformidade com a Seção II da PI970 ; 99 - outro
            (especificar no campo observações) .
        """
        x_dime: Optional[str] = field(
            default=None,
            metadata={
                "name": "xDime",
                "type": "Element",
                "min_length": 5,
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        c_inf_manu: List[NatCargaCInfManu] = field(
            default_factory=list,
            metadata={
                "name": "cInfManu",
                "type": "Element",
                "white_space": "preserve",
            }
        )

    @dataclass
    class Tarifa:
        """
        :ivar cl: Classe Preencher com: M - Tarifa Mínima; G - Tarifa
            Geral; E - Tarifa Específica
        :ivar c_tar: Código da Tarifa Deverão ser incluídos os códigos
            de três dígitos, correspondentes à tarifa.
        :ivar v_tar: Valor da Tarifa Valor da tarifa por kg quando for o
            caso.
        """
        cl: Optional[str] = field(
            default=None,
            metadata={
                "name": "CL",
                "type": "Element",
                "required": True,
                "length": 1,
                "white_space": "preserve",
                "pattern": r"M|G|E",
            }
        )
        c_tar: Optional[str] = field(
            default=None,
            metadata={
                "name": "cTar",
                "type": "Element",
                "min_length": 1,
                "max_length": 4,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        v_tar: Optional[str] = field(
            default=None,
            metadata={
                "name": "vTar",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )

    @dataclass
    class Peri:
        """
        :ivar n_onu: Número ONU/UN Ver a legislação de transporte de
            produtos perigosos aplicadas ao modal
        :ivar q_tot_emb: Quantidade total de volumes contendo artigos
            perigosos Preencher com o número de volumes (unidades) de
            artigos perigosos, ou seja, cada embalagem devidamente
            marcada e etiquetada (por ex.: número de caixas, de
            tambores, de bombonas, dentre outros). Não deve ser
            preenchido com o número de ULD, pallets ou containers.
        :ivar inf_tot_ap: Grupo de informações das quantidades totais de
            artigos perigosos Preencher conforme a legislação de
            transporte de produtos perigosos aplicada ao modal
        """
        n_onu: Optional[str] = field(
            default=None,
            metadata={
                "name": "nONU",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{4}|ND",
            }
        )
        q_tot_emb: Optional[str] = field(
            default=None,
            metadata={
                "name": "qTotEmb",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        inf_tot_ap: Optional["Aereo.Peri.InfTotAp"] = field(
            default=None,
            metadata={
                "name": "infTotAP",
                "type": "Element",
                "required": True,
            }
        )

        @dataclass
        class InfTotAp:
            """
            :ivar q_tot_prod: Quantidade total de artigos perigosos 15
                posições, sendo 11 inteiras e 4 decimais. Deve indicar a
                quantidade total do artigo perigoso, tendo como base a
                unidade referenciada na Tabela 3-1 do Doc 9284, por
                exemplo: litros; quilogramas; quilograma bruto etc. O
                preenchimento não deve, entretanto, incluir a unidade de
                medida. No caso de transporte de material radioativo,
                deve-se indicar o somatório dos Índices de Transporte
                (TI). Não indicar a quantidade do artigo perigoso por
                embalagem.
            :ivar uni_ap: Unidade de medida 1 – KG; 2 – KG G (quilograma
                bruto); 3 – LITROS; 4 – TI (índice de transporte para
                radioativos); 5- Unidades (apenas para artigos perigosos
                medidos em unidades que não se enquadram nos itens
                acima. Exemplo: baterias, celulares, equipamentos,
                veículos, dentre outros)
            """
            q_tot_prod: Optional[str] = field(
                default=None,
                metadata={
                    "name": "qTotProd",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"0|0\.[0-9]{4}|[1-9]{1}[0-9]{0,10}(\.[0-9]{4})?",
                }
            )
            uni_ap: Optional[InfTotApUniAp] = field(
                default=None,
                metadata={
                    "name": "uniAP",
                    "type": "Element",
                    "required": True,
                    "min_length": 1,
                    "max_length": 1,
                }
            )
