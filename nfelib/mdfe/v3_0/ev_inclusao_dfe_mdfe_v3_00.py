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

    :ivar desc_evento: Descrição do Evento - “Inclusão DF-e”
    :ivar n_prot: Número do Protocolo de Status do MDF-e. 1 posição tipo
        de autorizador (9 - SEFAZ Nacional ); 2 posições ano; 10
        seqüencial no ano.
    :ivar c_mun_carrega: Código do Município de Carregamento
    :ivar x_mun_carrega: Nome do Município de Carregamento
    :ivar inf_doc: Informações dos Documentos fiscais vinculados ao
        manifesto
    """
    class Meta:
        name = "evIncDFeMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    desc_evento: Optional[EvIncDfeMdfeDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    n_prot: Optional[str] = field(
        default=None,
        metadata={
            "name": "nProt",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    c_mun_carrega: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMunCarrega",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    x_mun_carrega: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMunCarrega",
            "type": "Element",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    inf_doc: List["EvIncDfeMdfe.InfDoc"] = field(
        default_factory=list,
        metadata={
            "name": "infDoc",
            "type": "Element",
            "min_occurs": 1,
        }
    )

    @dataclass
    class InfDoc:
        """
        :ivar c_mun_descarga: Código do Município de Descarregamento
        :ivar x_mun_descarga: Nome do Município de Descarregamento
        :ivar ch_nfe: Nota Fiscal Eletrônica
        """
        c_mun_descarga: Optional[str] = field(
            default=None,
            metadata={
                "name": "cMunDescarga",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{7}",
            }
        )
        x_mun_descarga: Optional[str] = field(
            default=None,
            metadata={
                "name": "xMunDescarga",
                "type": "Element",
                "required": True,
                "min_length": 2,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        ch_nfe: Optional[str] = field(
            default=None,
            metadata={
                "name": "chNFe",
                "type": "Element",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
