from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bindings.mdfe.v3_0.tipos_geral_mdfe_v3_00 import (
    Tamb,
    TcodUfIbge,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class ProcEventoMdfeVersao(Enum):
    VALUE_1_00 = "1.00"
    VALUE_3_00 = "3.00"


class ProtMdfeVersao(Enum):
    VALUE_1_00 = "1.00"
    VALUE_3_00 = "3.00"


@dataclass
class TconsSitMdfe:
    """
    Tipo Pedido de Consulta da Situação Atual do MDF-e.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar x_serv: Serviço Solicitado
    :ivar ch_mdfe: Chaves de acesso do MDF-e, compostas por: UF do
        emitente, AAMM da emissão do MDF-e, CNPJ do emitente, modelo,
        série, tipo de emissão e número do MDF-e e código numérico + DV.
    :ivar versao:
    """
    class Meta:
        name = "TConsSitMDFe"

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
class TretConsSitMdfe:
    """
    Tipo Retorno de Pedido de Consulta da Situação Atual do MDF-e.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que processou o MDF-e
    :ivar c_stat: Código do status da mensagem enviada.
    :ivar x_motivo: Descrição literal do status do serviço solicitado.
    :ivar c_uf: código da UF de atendimento
    :ivar prot_mdfe:
    :ivar proc_evento_mdfe:
    :ivar versao:
    """
    class Meta:
        name = "TRetConsSitMDFe"

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
    c_uf: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cUF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    prot_mdfe: Optional["TretConsSitMdfe.ProtMdfe"] = field(
        default=None,
        metadata={
            "name": "protMDFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
        }
    )
    proc_evento_mdfe: List["TretConsSitMdfe.ProcEventoMdfe"] = field(
        default_factory=list,
        metadata={
            "name": "procEventoMDFe",
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

    @dataclass
    class ProtMdfe:
        """
        :ivar any_element: Retornar protMDFe da versão correspondente do
            MDF-e autorizado
        :ivar versao:
        """
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            }
        )
        versao: Optional[ProtMdfeVersao] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
            }
        )

    @dataclass
    class ProcEventoMdfe:
        """
        :ivar any_element: Retornar procEventoMDFe da versão
            correspondente do evento MDF-e autorizado
        :ivar versao:
        """
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            }
        )
        versao: Optional[ProcEventoMdfeVersao] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "white_space": "preserve",
            }
        )
