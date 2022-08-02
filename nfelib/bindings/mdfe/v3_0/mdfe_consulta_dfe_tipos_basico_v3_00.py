from dataclasses import dataclass, field
from typing import List, Optional
from nfelib.bindings.mdfe.v3_0.tipos_geral_mdfe_v3_00 import Tamb

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class TmdfeDfe:
    """
    Tipo Documento Fiscal Eletrônico MDF-e.
    """
    class Meta:
        name = "TMDFeDFe"

    proc_mdfe: Optional["TmdfeDfe.ProcMdfe"] = field(
        default=None,
        metadata={
            "name": "procMDFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    proc_evento_mdfe: List["TmdfeDfe.ProcEventoMdfe"] = field(
        default_factory=list,
        metadata={
            "name": "procEventoMDFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )

    @dataclass
    class ProcMdfe:
        """
        :ivar any_element: Autorização de Uso do MDF-e
        :ivar versao:
        """
        any_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "min_occurs": 2,
                "max_occurs": 2,
            }
        )
        versao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"3\.00",
            }
        )

    @dataclass
    class ProcEventoMdfe:
        """
        :ivar any_element: Demais eventos vinculados ao MDF-e
        :ivar versao:
        """
        any_element: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
                "min_occurs": 2,
                "max_occurs": 2,
            }
        )
        versao: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"3\.00",
            }
        )


@dataclass
class TmdfeConsultaDfe:
    """
    Tipo Pedido de Consulta do Manifesto Eletrônico de Documentos Fiscais.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar x_serv: Serviço Solicitado
    :ivar ch_mdfe: Chaves de acesso do MDF-e, compostas por: UF do
        emitente, AAMM da emissão do MDF-e, CNPJ do emitente, modelo,
        série e número do MDF-e e código numérico + DV.
    :ivar versao:
    """
    class Meta:
        name = "TMDFeConsultaDFe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    x_serv: str = field(
        init=False,
        default="CONSULTAR",
        metadata={
            "name": "xServ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    ch_mdfe: Optional[str] = field(
        default=None,
        metadata={
            "name": "chMDFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "max_length": 44,
            "white_space": "preserve",
            "pattern": r"[0-9]{44}",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"3\.00",
        }
    )


@dataclass
class TretMdfeConsultaDfe:
    """
    Tipo Retorno de Pedido de Consulta do Manifesto Eletrônico de Documentos
    Fiscais.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que processou a consulta do
        MDF-e
    :ivar c_stat: Código do status da consulta do MDF-e
    :ivar x_motivo: Descrição literal do status da consulta do MDF-e
    :ivar mdfe_dfe:
    :ivar versao:
    """
    class Meta:
        name = "TRetMDFeConsultaDFe"

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
    mdfe_dfe: Optional[TmdfeDfe] = field(
        default=None,
        metadata={
            "name": "MDFeDFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"3\.00",
        }
    )
