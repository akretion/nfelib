from dataclasses import dataclass, field
from typing import List, Optional
from nfelib.bindings.cte.v3_0.cte_tipos_basico_v3_00 import TprotCte
from nfelib.bindings.cte.v3_0.tipos_geral_cte_v3_00 import (
    Tamb,
    TcodUfIbge,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class TconsReciCte:
    """
    Tipo Pedido de Consulta do Recibo do Lote de CT-e.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar n_rec: Número do Recibo do lote a ser consultado
    :ivar versao:
    """
    class Meta:
        name = "TConsReciCTe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    n_rec: Optional[str] = field(
        default=None,
        metadata={
            "name": "nRec",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"3\.00",
        }
    )


@dataclass
class TretConsReciCte:
    """
    Tipo Retorno do Pedido de  Consulta do Recibo do Lote de CT-e.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que processou a CT-e
    :ivar n_rec: Número do Recibo Consultado
    :ivar c_stat: código do status do retorno da consulta.
    :ivar x_motivo: Descrição literal do status do do retorno da
        consulta.
    :ivar c_uf: Idntificação da UF
    :ivar prot_cte: Conjunto de CT-es processados, só existe nos casos
        em que o lote consultado se encontra processado
    :ivar versao:
    """
    class Meta:
        name = "TRetConsReciCTe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    n_rec: Optional[str] = field(
        default=None,
        metadata={
            "name": "nRec",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    c_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "cStat",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    x_motivo: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMotivo",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_uf: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    prot_cte: List[TprotCte] = field(
        default_factory=list,
        metadata={
            "name": "protCTe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "max_occurs": 50,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"3\.00",
        }
    )
