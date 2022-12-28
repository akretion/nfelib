from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class Aereo:
    """
    Informações do modal Aéreo.

    :ivar nac: Marca da Nacionalidade da aeronave
    :ivar matr: Marca de Matrícula da aeronave
    :ivar nVoo: Número do Voo Formato = AB1234, sendo AB a designação da
        empresa e 1234 o número do voo. Quando não for possível incluir
        as marcas de nacionalidade e matrícula sem hífen.
    :ivar cAerEmb: Aeródromo de Embarque O código de três letras IATA do
        aeroporto de partida deverá ser incluído como primeira anotação.
        Quando não for possível, utilizar a sigla OACI.
    :ivar cAerDes: Aeródromo de Destino O código de três letras IATA do
        aeroporto de destino deverá ser incluído como primeira anotação.
        Quando não for possível, utilizar a sigla OACI.
    :ivar dVoo: Data do Voo Formato AAAA-MM-DD
    """
    class Meta:
        name = "aereo"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    nac: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 4,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    matr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 6,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nVoo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 5,
            "max_length": 9,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cAerEmb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 3,
            "max_length": 4,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cAerDes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 3,
            "max_length": 4,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    dVoo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
        }
    )
