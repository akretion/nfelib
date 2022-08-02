from dataclasses import dataclass, field
from typing import List, Optional
from nfelib.bindings.cte.v3_0.tipos_geral_cte_v3_00 import Tuf

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class Rodo:
    """
    Informações do modal Rodoviário.

    :ivar rntrc: Registro Nacional de Transportadores Rodoviários de
        Carga Registro obrigatório do emitente do CT-e junto à ANTT para
        exercer a atividade de transportador rodoviário de cargas por
        conta de terceiros e mediante remuneração.
    :ivar occ: Ordens de Coleta associados
    """
    class Meta:
        name = "rodo"
        namespace = "http://www.portalfiscal.inf.br/cte"

    rntrc: Optional[str] = field(
        default=None,
        metadata={
            "name": "RNTRC",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{8}|ISENTO",
        }
    )
    occ: List["Rodo.Occ"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 10,
        }
    )

    @dataclass
    class Occ:
        """
        :ivar serie: Série da OCC
        :ivar n_occ: Número da Ordem de coleta
        :ivar d_emi: Data de emissão da ordem de coleta Formato AAAA-MM-
            DD
        :ivar emi_occ:
        """
        serie: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "min_length": 1,
                "max_length": 3,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        n_occ: Optional[str] = field(
            default=None,
            metadata={
                "name": "nOcc",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,5}",
            }
        )
        d_emi: Optional[str] = field(
            default=None,
            metadata={
                "name": "dEmi",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
            }
        )
        emi_occ: Optional["Rodo.Occ.EmiOcc"] = field(
            default=None,
            metadata={
                "name": "emiOcc",
                "type": "Element",
                "required": True,
            }
        )

        @dataclass
        class EmiOcc:
            """
            :ivar cnpj: Número do CNPJ Informar os zeros não
                significativos.
            :ivar c_int: Código interno de uso da transportadora Uso
                intermo das transportadoras.
            :ivar ie: Inscrição Estadual
            :ivar uf: Sigla da UF Informar EX para operações com o
                exterior.
            :ivar fone: Telefone
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            c_int: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cInt",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 10,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "required": True,
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
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
            fone: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "white_space": "preserve",
                    "pattern": r"[0-9]{6,14}",
                }
            )
