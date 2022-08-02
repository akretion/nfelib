from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class EvIncCondutorMdfeDescEvento(Enum):
    INCLUSAO_CONDUTOR = "Inclusao Condutor"


@dataclass
class EvIncCondutorMdfe:
    """
    Schema XML de validação do evento de inclusao de condutor 110114.

    :ivar desc_evento: Descrição do Evento - “Inclusao Condutor”
    :ivar condutor: Informações do(s) Condutor(s) do veículo
    """
    class Meta:
        name = "evIncCondutorMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    desc_evento: Optional[EvIncCondutorMdfeDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    condutor: Optional["EvIncCondutorMdfe.Condutor"] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )

    @dataclass
    class Condutor:
        """
        :ivar x_nome: Nome do Condutor
        :ivar cpf: CPF do Condutor
        """
        x_nome: Optional[str] = field(
            default=None,
            metadata={
                "name": "xNome",
                "type": "Element",
                "required": True,
                "min_length": 2,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        cpf: Optional[str] = field(
            default=None,
            metadata={
                "name": "CPF",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{11}",
            }
        )
