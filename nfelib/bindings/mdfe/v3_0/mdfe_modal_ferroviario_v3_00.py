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
        :ivar xPref: Prefixo do Trem
        :ivar dhTrem: Data e hora de liberação do trem na origem
        :ivar xOri: Origem do Trem Sigla da estação de origem
        :ivar xDest: Destino do Trem Sigla da estação de destino
        :ivar qVag: Quantidade de vagões carregados
        """
        xPref: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 10,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        dhTrem: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        xOri: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 3,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        xDest: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 3,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        qVag: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "pattern": r"[1-9]{1}[0-9]{0,2}",
            }
        )

    @dataclass
    class Vag:
        """
        :ivar pesoBC: Peso Base de Cálculo de Frete em Toneladas
        :ivar pesoR: Peso Real em Toneladas
        :ivar tpVag: Tipo de Vagão
        :ivar serie: Serie de Identificação do vagão
        :ivar nVag: Número de Identificação do vagão
        :ivar nSeq: Sequencia do vagão na composição
        :ivar TU: Tonelada Útil Unidade de peso referente à carga útil
            (apenas o peso da carga transportada), expressa em
            toneladas.
        """
        pesoBC: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{3})?",
            }
        )
        pesoR: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{3})?",
            }
        )
        tpVag: Optional[str] = field(
            default=None,
            metadata={
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
        nVag: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 8,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,7}",
            }
        )
        nSeq: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,2}",
            }
        )
        TU: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{1,3}(\.[0-9]{2,3})?",
            }
        )
