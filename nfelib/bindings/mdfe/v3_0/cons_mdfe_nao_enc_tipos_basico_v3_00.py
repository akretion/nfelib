from dataclasses import dataclass, field
from typing import List, Optional
from nfelib.bindings.mdfe.v3_0.tipos_geral_mdfe_v3_00 import (
    Tamb,
    TcodUfIbge,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class TconsMdfeNaoEnc:
    """
    Tipo Pedido de Consulta MDF-e Não Encerrados.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar xServ: Serviço Solicitado
    :ivar CNPJ: CNPJ do emitente do MDF-e Informar zeros não
        significativos
    :ivar CPF: CPF do emitente do MDF-e Informar zeros não
        significativos Usar com serie específica 920-969 para emitente
        pessoa física com inscrição estadual
    :ivar versao:
    """
    class Meta:
        name = "TConsMDFeNaoEnc"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    xServ: str = field(
        init=False,
        default="CONSULTAR NÃO ENCERRADOS",
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    CPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
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
class TretConsMdfeNaoEnc:
    """
    Tipo Retorno de Pedido de Consulta MDF-e não Encerrados.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar verAplic: Versão do Aplicativo que processou o MDF-e
    :ivar cStat: Código do status da mensagem enviada.
    :ivar xMotivo: Descrição literal do status do serviço solicitado.
    :ivar cUF: código da UF de atendimento
    :ivar infMDFe:
    :ivar versao:
    """
    class Meta:
        name = "TRetConsMDFeNaoEnc"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cStat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    infMDFe: List["TretConsMdfeNaoEnc.InfMdfe"] = field(
        default_factory=list,
        metadata={
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
    class InfMdfe:
        """
        :ivar chMDFe: Chaves de acesso do MDF-e não encerrado
        :ivar nProt: Número do Protocolo de autorização do MDF-e não
            encerrado
        """
        chMDFe: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        nProt: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
