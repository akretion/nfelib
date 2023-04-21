from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class EvIncDfeMdfeDescEvento(Enum):
    INCLUS_O_DF_E = "Inclusão DF-e"
    INCLUSAO_DF_E = "Inclusao DF-e"


@dataclass
class EvIncDfeMdfe:
    """
    Schema XML de validação do evento de inclusão de DFe 110115.

    :ivar descEvento: Descrição do Evento - “Inclusão DF-e”
    :ivar nProt: Número do Protocolo de Status do MDF-e. 1 posição tipo
        de autorizador (9 - SEFAZ Nacional ); 2 posições ano; 10
        seqüencial no ano.
    :ivar cMunCarrega: Código do Município de Carregamento
    :ivar xMunCarrega: Nome do Município de Carregamento
    :ivar infDoc: Informações dos Documentos fiscais vinculados ao
        manifesto
    """
    class Meta:
        name = "evIncDFeMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    descEvento: Optional[EvIncDfeMdfeDescEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    nProt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    cMunCarrega: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xMunCarrega: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    infDoc: List["EvIncDfeMdfe.InfDoc"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class InfDoc:
        """
        :ivar cMunDescarga: Código do Município de Descarregamento
        :ivar xMunDescarga: Nome do Município de Descarregamento
        :ivar chNFe: Nota Fiscal Eletrônica
        """
        cMunDescarga: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{7}",
            }
        )
        xMunDescarga: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 2,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        chNFe: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
