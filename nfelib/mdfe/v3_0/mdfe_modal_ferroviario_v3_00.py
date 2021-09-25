from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class Ferrov:
    """
    Informações do modal Ferroviário.

    :ivar trem: Informações da composição do trem
    :ivar vag: informações dos Vagões
    """
    class Meta:
        name = "ferrov"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    trem: Optional["Ferrov.Trem"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    vag: List["Ferrov.Vag"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class Trem:
        """
        :ivar x_pref: Prefixo do Trem
        :ivar dh_trem: Data e hora de liberação do trem na origem
        :ivar x_ori: Origem do Trem Sigla da estação de origem
        :ivar x_dest: Destino do Trem Sigla da estação de destino
        :ivar q_vag: Quantidade de vagões carregados
        """
        x_pref: Optional[str] = field(
            default=None,
            metadata={
                "name": "xPref",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 10,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        dh_trem: Optional[str] = field(
            default=None,
            metadata={
                "name": "dhTrem",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        x_ori: Optional[str] = field(
            default=None,
            metadata={
                "name": "xOri",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 3,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        x_dest: Optional[str] = field(
            default=None,
            metadata={
                "name": "xDest",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 3,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        q_vag: Optional[str] = field(
            default=None,
            metadata={
                "name": "qVag",
                "type": "Element",
                "required": True,
                "pattern": r"[1-9]{1}[0-9]{0,2}",
            }
        )

    @dataclass
    class Vag:
        """
        :ivar peso_bc: Peso Base de Cálculo de Frete em Toneladas
        :ivar peso_r: Peso Real em Toneladas
        :ivar tp_vag: Tipo de Vagão
        :ivar serie: Serie de Identificação do vagão
        :ivar n_vag: Número de Identificação do vagão
        :ivar n_seq: Sequencia do vagão na composição
        :ivar tu: Tonelada Útil Unidade de peso referente à carga útil
            (apenas o peso da carga transportada), expressa em
            toneladas.
        """
        peso_bc: Optional[str] = field(
            default=None,
            metadata={
                "name": "pesoBC",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{3})?",
            }
        )
        peso_r: Optional[str] = field(
            default=None,
            metadata={
                "name": "pesoR",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{3})?",
            }
        )
        tp_vag: Optional[str] = field(
            default=None,
            metadata={
                "name": "tpVag",
                "type": "Element",
                "length": 3,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        serie: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "length": 3,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        n_vag: Optional[str] = field(
            default=None,
            metadata={
                "name": "nVag",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 8,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,7}",
            }
        )
        n_seq: Optional[str] = field(
            default=None,
            metadata={
                "name": "nSeq",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,2}",
            }
        )
        tu: Optional[str] = field(
            default=None,
            metadata={
                "name": "TU",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{1,3}(\.[0-9]{2,3})?",
            }
        )
