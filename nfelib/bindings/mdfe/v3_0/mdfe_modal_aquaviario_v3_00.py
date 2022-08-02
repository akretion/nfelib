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
    :ivar tp_emb: Código do tipo de embarcação Preencher com código da
        Tabela de Tipo de Embarcação definida no Ministério dos
        Transportes
    :ivar c_embar: Código da embarcação
    :ivar x_embar: Nome da embarcação
    :ivar n_viag: Número da Viagem
    :ivar c_prt_emb: Código do Porto de Embarque Preencher de acordo com
        Tabela de Portos definida no Ministério dos Transportes
    :ivar c_prt_dest: Código do Porto de Destino Preencher de acordo com
        Tabela de Portos definida no Ministério dos Transportes
    :ivar prt_trans: Porto de Transbordo
    :ivar tp_nav: Tipo de Navegação Preencher com: 0 - Interior; 1 -
        Cabotagem
    :ivar inf_term_carreg: Grupo de informações dos terminais de
        carregamento.
    :ivar inf_term_descarreg: Grupo de informações dos terminais de
        descarregamento.
    :ivar inf_emb_comb: Informações das Embarcações do Comboio
    :ivar inf_unid_carga_vazia: Informações das Undades de Carga vazias
    :ivar inf_unid_transp_vazia: Informações das Undades de Transporte
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
    tp_emb: Optional[str] = field(
        default=None,
        metadata={
            "name": "tpEmb",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{2}",
        }
    )
    c_embar: Optional[str] = field(
        default=None,
        metadata={
            "name": "cEmbar",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_embar: Optional[str] = field(
        default=None,
        metadata={
            "name": "xEmbar",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    n_viag: Optional[str] = field(
        default=None,
        metadata={
            "name": "nViag",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[1-9]{1}[0-9]{0,9}",
        }
    )
    c_prt_emb: Optional[str] = field(
        default=None,
        metadata={
            "name": "cPrtEmb",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_prt_dest: Optional[str] = field(
        default=None,
        metadata={
            "name": "cPrtDest",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    prt_trans: Optional[str] = field(
        default=None,
        metadata={
            "name": "prtTrans",
            "type": "Element",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    tp_nav: Optional[AquavTpNav] = field(
        default=None,
        metadata={
            "name": "tpNav",
            "type": "Element",
            "white_space": "preserve",
        }
    )
    inf_term_carreg: List["Aquav.InfTermCarreg"] = field(
        default_factory=list,
        metadata={
            "name": "infTermCarreg",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    inf_term_descarreg: List["Aquav.InfTermDescarreg"] = field(
        default_factory=list,
        metadata={
            "name": "infTermDescarreg",
            "type": "Element",
            "max_occurs": 5,
        }
    )
    inf_emb_comb: List["Aquav.InfEmbComb"] = field(
        default_factory=list,
        metadata={
            "name": "infEmbComb",
            "type": "Element",
            "max_occurs": 30,
        }
    )
    inf_unid_carga_vazia: List["Aquav.InfUnidCargaVazia"] = field(
        default_factory=list,
        metadata={
            "name": "infUnidCargaVazia",
            "type": "Element",
        }
    )
    inf_unid_transp_vazia: List["Aquav.InfUnidTranspVazia"] = field(
        default_factory=list,
        metadata={
            "name": "infUnidTranspVazia",
            "type": "Element",
        }
    )

    @dataclass
    class InfTermCarreg:
        """
        :ivar c_term_carreg: Código do Terminal de Carregamento
            Preencher de acordo com a Tabela de Terminais de
            Carregamento. O código de cada Porto está definido no
            Ministério de Transportes.
        :ivar x_term_carreg: Nome do Terminal de Carregamento
        """
        c_term_carreg: Optional[str] = field(
            default=None,
            metadata={
                "name": "cTermCarreg",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 8,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        x_term_carreg: Optional[str] = field(
            default=None,
            metadata={
                "name": "xTermCarreg",
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
        :ivar c_term_descarreg: Código do Terminal de Descarregamento
            Preencher de acordo com a Tabela de Terminais de
            Descarregamento. O código de cada Porto está definido no
            Ministério de Transportes.
        :ivar x_term_descarreg: Nome do Terminal de Descarregamento
        """
        c_term_descarreg: Optional[str] = field(
            default=None,
            metadata={
                "name": "cTermDescarreg",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 8,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        x_term_descarreg: Optional[str] = field(
            default=None,
            metadata={
                "name": "xTermDescarreg",
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
        :ivar c_emb_comb: Código da embarcação do comboio
        :ivar x_balsa: Identificador da Balsa
        """
        c_emb_comb: Optional[str] = field(
            default=None,
            metadata={
                "name": "cEmbComb",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 10,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        x_balsa: Optional[str] = field(
            default=None,
            metadata={
                "name": "xBalsa",
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
        :ivar id_unid_carga_vazia: Identificação da unidades de carga
            vazia
        :ivar tp_unid_carga_vazia: Tipo da unidade de carga vazia 1 -
            Container; 2 - ULD;3 - Pallet;4 - Outros;
        """
        id_unid_carga_vazia: Optional[str] = field(
            default=None,
            metadata={
                "name": "idUnidCargaVazia",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[A-Z0-9]+",
            }
        )
        tp_unid_carga_vazia: Optional[InfUnidCargaVaziaTpUnidCargaVazia] = field(
            default=None,
            metadata={
                "name": "tpUnidCargaVazia",
                "type": "Element",
                "required": True,
            }
        )

    @dataclass
    class InfUnidTranspVazia:
        """
        :ivar id_unid_transp_vazia: Identificação da unidades de
            transporte vazia
        :ivar tp_unid_transp_vazia: Tipo da unidade de transporte vazia
            Deve ser preenchido com “1” para Rodoviário Tração do tipo
            caminhão ou “2” para Rodoviário reboque do tipo carreta
        """
        id_unid_transp_vazia: Optional[str] = field(
            default=None,
            metadata={
                "name": "idUnidTranspVazia",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
                "pattern": r"[A-Z0-9]+",
            }
        )
        tp_unid_transp_vazia: Optional[InfUnidTranspVaziaTpUnidTranspVazia] = field(
            default=None,
            metadata={
                "name": "tpUnidTranspVazia",
                "type": "Element",
                "required": True,
            }
        )
