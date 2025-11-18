from dataclasses import dataclass, field
from typing import Optional

from nfelib import CommonMixin
from nfelib.cte.bindings.v4_0.tipos_geral_cte_v4_00 import Tuf

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class Rodo(CommonMixin):
    """
    Informações do modal Rodoviário.

    :ivar RNTRC: Registro Nacional de Transportadores Rodoviários de
        Carga Registro obrigatório do emitente do CT-e junto à ANTT para
        exercer a atividade de transportador rodoviário de cargas por
        conta de terceiros e mediante remuneração.
    :ivar occ: Ordens de Coleta associados
    """

    class Meta:
        name = "rodo"
        namespace = "http://www.portalfiscal.inf.br/cte"

    RNTRC: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{8}|ISENTO",
        },
    )
    occ: list["Rodo.Occ"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        },
    )

    @dataclass
    class Occ(CommonMixin):
        """
        :ivar serie: Série da OCC
        :ivar nOcc: Número da Ordem de coleta
        :ivar dEmi: Data de emissão da ordem de coleta Formato AAAA-MM-
            DD
        :ivar emiOcc:
        """

        serie: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "min_length": 1,
                "max_length": 3,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            },
        )
        nOcc: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,5}",
            },
        )
        dEmi: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
            },
        )
        emiOcc: Optional["Rodo.Occ.EmiOcc"] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )

        @dataclass
        class EmiOcc(CommonMixin):
            """
            :ivar CNPJ: Número do CNPJ Informar os zeros não
                significativos.
            :ivar cInt: Código interno de uso da transportadora Uso
                intermo das transportadoras.
            :ivar IE: Inscrição Estadual
            :ivar UF: Sigla da UF Informar EX para operações com o
                exterior.
            :ivar fone: Telefone
            """

            CNPJ: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[A-Z0-9]{12}[0-9]{2}",
                },
            )
            cInt: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 10,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                },
            )
            IE: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                },
            )
            UF: Optional[Tuf] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "required": True,
                },
            )
            fone: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6,14}",
                },
            )
