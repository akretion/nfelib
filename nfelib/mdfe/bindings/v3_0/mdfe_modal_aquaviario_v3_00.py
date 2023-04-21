from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class AquavTpNav(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class InfUnidCargaVaziaTpUnidCargaVazia(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


class InfUnidTranspVaziaTpUnidTranspVazia(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


@dataclass
class Aquav:
    """
    Informações do modal Aquaviário.

    :ivar irin: Irin do navio sempre deverá ser informado
    :ivar tpEmb: Código do tipo de embarcação Preencher com código da
        Tabela de Tipo de Embarcação definida no Ministério dos
        Transportes
    :ivar cEmbar: Código da embarcação
    :ivar xEmbar: Nome da embarcação
    :ivar nViag: Número da Viagem
    :ivar cPrtEmb: Código do Porto de Embarque Preencher de acordo com
        Tabela de Portos definida no Ministério dos Transportes
    :ivar cPrtDest: Código do Porto de Destino Preencher de acordo com
        Tabela de Portos definida no Ministério dos Transportes
    :ivar prtTrans: Porto de Transbordo
    :ivar tpNav: Tipo de Navegação Preencher com: 0 - Interior; 1 -
        Cabotagem
    :ivar infTermCarreg: Grupo de informações dos terminais de
        carregamento.
    :ivar infTermDescarreg: Grupo de informações dos terminais de
        descarregamento.
    :ivar infEmbComb: Informações das Embarcações do Comboio
    :ivar infUnidCargaVazia: Informações das Undades de Carga vazias
    :ivar infUnidTranspVazia: Informações das Undades de Transporte
        vazias
    """
    class Meta:
        name = "aquav"
        namespace = "http://www.portalfiscal.inf.br/mdfe"

    irin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "white_space": "preserve",
        }
    )
    tpEmb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{2}",
        }
    )
    cEmbar: Optional[str] = field(
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
    xEmbar: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nViag: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[1-9]{1}[0-9]{0,9}",
        }
    )
    cPrtEmb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cPrtDest: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    prtTrans: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    tpNav: Optional[AquavTpNav] = field(
        default=None,
        metadata={
            "type": "Element",
            "white_space": "preserve",
        }
    )
    infTermCarreg: List["Aquav.InfTermCarreg"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        }
    )
    infTermDescarreg: List["Aquav.InfTermDescarreg"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 5,
        }
    )
    infEmbComb: List["Aquav.InfEmbComb"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 30,
        }
    )
    infUnidCargaVazia: List["Aquav.InfUnidCargaVazia"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    infUnidTranspVazia: List["Aquav.InfUnidTranspVazia"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )

    @dataclass
    class InfTermCarreg:
        """
        :ivar cTermCarreg: Código do Terminal de Carregamento Preencher
            de acordo com a Tabela de Terminais de Carregamento. O
            código de cada Porto está definido no Ministério de
            Transportes.
        :ivar xTermCarreg: Nome do Terminal de Carregamento
        """
        cTermCarreg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 8,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        xTermCarreg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )

    @dataclass
    class InfTermDescarreg:
        """
        :ivar cTermDescarreg: Código do Terminal de Descarregamento
            Preencher de acordo com a Tabela de Terminais de
            Descarregamento. O código de cada Porto está definido no
            Ministério de Transportes.
        :ivar xTermDescarreg: Nome do Terminal de Descarregamento
        """
        cTermDescarreg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 8,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        xTermDescarreg: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )

    @dataclass
    class InfEmbComb:
        """
        :ivar cEmbComb: Código da embarcação do comboio
        :ivar xBalsa: Identificador da Balsa
        """
        cEmbComb: Optional[str] = field(
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
        xBalsa: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 60,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )

    @dataclass
    class InfUnidCargaVazia:
        """
        :ivar idUnidCargaVazia: Identificação da unidades de carga vazia
        :ivar tpUnidCargaVazia: Tipo da unidade de carga vazia 1 -
            Container; 2 - ULD;3 - Pallet;4 - Outros;
        """
        idUnidCargaVazia: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[A-Z0-9]+",
            }
        )
        tpUnidCargaVazia: Optional[InfUnidCargaVaziaTpUnidCargaVazia] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )

    @dataclass
    class InfUnidTranspVazia:
        """
        :ivar idUnidTranspVazia: Identificação da unidades de transporte
            vazia
        :ivar tpUnidTranspVazia: Tipo da unidade de transporte vazia
            Deve ser preenchido com “1” para Rodoviário Tração do tipo
            caminhão ou “2” para Rodoviário reboque do tipo carreta
        """
        idUnidTranspVazia: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[A-Z0-9]+",
            }
        )
        tpUnidTranspVazia: Optional[InfUnidTranspVaziaTpUnidTranspVazia] = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            }
        )
