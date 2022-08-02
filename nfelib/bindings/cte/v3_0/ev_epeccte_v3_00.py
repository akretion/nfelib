from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from nfelib.bindings.cte.v3_0.cte_tipos_basico_v3_00 import Toma4Toma
from nfelib.bindings.cte.v3_0.evento_cte_tipos_basico_v3_00 import TmodTransp
from nfelib.bindings.cte.v3_0.tipos_geral_cte_v3_00 import Tuf

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class EvEpeccteDescEvento(Enum):
    EPEC = "EPEC"


class EvEpeccteTpCte(Enum):
    VALUE_0 = "0"


@dataclass
class EvEpeccte:
    """
    Schema XML de validação do evento de emissão prévia de emissão em
    contingência 110113.

    :ivar desc_evento: Descrição do Evento - “EPEC”
    :ivar x_just: Justificativa da Entrada em Contingencia
    :ivar v_icms: Valor do ICMS
    :ivar v_icmsst: Valor do ICMS ST
    :ivar v_tprest: Valor Total da Prestação do Serviço Pode conter
        zeros quando o CT-e for de complemento de ICMS
    :ivar v_carga: Valor total da carga Dever ser informado para todos
        os modais, com exceção para o Dutoviário.
    :ivar toma4: Indicador do "papel" do tomador do serviço no CT-e
    :ivar modal: Modal Preencher com: 01-Rodoviário; 02-Aéreo;
        03-Aquaviário; 04-Ferroviário; 05-Dutoviário; 06-Multimodal;
    :ivar ufini: UF do início da prestação Informar 'EX' para operações
        com o exterior.
    :ivar uffim: UF do término da prestação Informar 'EX' para operações
        com o exterior.
    :ivar tp_cte: Tipo do CT-e - Aceitar apenas Tipo Normal = 0
        Preencher com: 0 - CT-e Normal; 1 - CT-e de Complemento de
        Valores;     2 - CT-e de Anulação; 3 - CT-e Substituto
    :ivar dh_emi: Data e hora de emissão do CT-e Formato AAAA-MM-
        DDTHH:MM:DD TZD
    """
    class Meta:
        name = "evEPECCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"

    desc_evento: Optional[EvEpeccteDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    x_just: Optional[str] = field(
        default=None,
        metadata={
            "name": "xJust",
            "type": "Element",
            "required": True,
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    v_icms: Optional[str] = field(
        default=None,
        metadata={
            "name": "vICMS",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_icmsst: Optional[str] = field(
        default=None,
        metadata={
            "name": "vICMSST",
            "type": "Element",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_tprest: Optional[str] = field(
        default=None,
        metadata={
            "name": "vTPrest",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    v_carga: Optional[str] = field(
        default=None,
        metadata={
            "name": "vCarga",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
        }
    )
    toma4: Optional["EvEpeccte.Toma4"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    modal: Optional[TmodTransp] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ufini: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UFIni",
            "type": "Element",
            "required": True,
        }
    )
    uffim: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UFFim",
            "type": "Element",
            "required": True,
        }
    )
    tp_cte: Optional[EvEpeccteTpCte] = field(
        default=None,
        metadata={
            "name": "tpCTe",
            "type": "Element",
            "required": True,
            "length": 1,
            "white_space": "preserve",
        }
    )
    dh_emi: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhEmi",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )

    @dataclass
    class Toma4:
        """
        :ivar toma: Tomador do Serviço Preencher com: 0-Remetente;
            1-Expedidor;2-Recebedor;3-Destinatário ;4 - Outros
        :ivar uf: UF do tomador do serviço Informar 'EX' para operações
            com o exterior.
        :ivar cnpj: Número do CNPJ Em caso de empresa não estabelecida
            no Brasil, será informado o CNPJ com zeros. Informar os
            zeros não significativos.
        :ivar cpf: Número do CPF Informar os zeros não significativos.
        :ivar ie: Inscrição Estadual Informar a IE do tomador ou ISENTO
            se tomador é contribuinte do ICMS isento de inscrição no
            cadastro de contribuintes do ICMS. Caso o tomador não seja
            contribuinte do ICMS não informar o conteúdo.
        """
        toma: Optional[Toma4Toma] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
            }
        )
        uf: Optional[Tuf] = field(
            default=None,
            metadata={
                "name": "UF",
                "type": "Element",
                "required": True,
            }
        )
        cnpj: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJ",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{0}|[0-9]{14}",
            }
        )
        cpf: Optional[str] = field(
            default=None,
            metadata={
                "name": "CPF",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{11}",
            }
        )
        ie: Optional[str] = field(
            default=None,
            metadata={
                "name": "IE",
                "type": "Element",
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r"[0-9]{0,14}|ISENTO",
            }
        )
