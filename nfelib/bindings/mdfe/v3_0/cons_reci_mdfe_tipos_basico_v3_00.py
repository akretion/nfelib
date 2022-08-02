from dataclasses import dataclass, field
from typing import Optional
from nfelib.bindings.mdfe.v3_0.mdfe_tipos_basico_v3_00 import TprotMdfe
from nfelib.bindings.mdfe.v3_0.tipos_geral_mdfe_v3_00 import (
    Tamb,
    TcodUfIbge,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class TconsReciMdfe:
    """
    Tipo Pedido de Consulta do Recibo do MDF-e.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar n_rec: Número do Recibo do arquivo a ser consultado
    :ivar versao:
    """
    class Meta:
        name = "TConsReciMDFe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    n_rec: Optional[str] = field(
        default=None,
        metadata={
            "name": "nRec",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
class TretConsReciMdfe:
    """
    Tipo Retorno do Pedido de  Consulta do Recibo do MDF-e.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que processou o MDF-e
    :ivar n_rec: Número do Recibo Consultado
    :ivar c_stat: código do status do retorno da consulta.
    :ivar x_motivo: Descrição literal do status do do retorno da
        consulta.
    :ivar c_uf: Idntificação da UF
    :ivar prot_mdfe: Resultado do processamento do MDF-e
    :ivar versao:
    """
    class Meta:
        name = "TRetConsReciMDFe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    prot_mdfe: Optional[TprotMdfe] = field(
        default=None,
        metadata={
            "name": "protMDFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
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
