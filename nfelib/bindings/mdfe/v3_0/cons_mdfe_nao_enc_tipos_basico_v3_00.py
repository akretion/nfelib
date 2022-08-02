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

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar x_serv: Serviço Solicitado
    :ivar cnpj: CNPJ do emitente do MDF-e Informar zeros não
        significativos
    :ivar cpf: CPF do emitente do MDF-e Informar zeros não
        significativos Usar com serie específica 920-969 para emitente
        pessoa física com inscrição estadual
    :ivar versao:
    """
    class Meta:
        name = "TConsMDFeNaoEnc"

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
        default="CONSULTAR NÃO ENCERRADOS",
        metadata={
            "name": "xServ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cnpj: Optional[str] = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    cpf: Optional[str] = field(
        default=None,
        metadata={
            "name": "CPF",
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

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que processou o MDF-e
    :ivar c_stat: Código do status da mensagem enviada.
    :ivar x_motivo: Descrição literal do status do serviço solicitado.
    :ivar c_uf: código da UF de atendimento
    :ivar inf_mdfe:
    :ivar versao:
    """
    class Meta:
        name = "TRetConsMDFeNaoEnc"

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
    inf_mdfe: List["TretConsMdfeNaoEnc.InfMdfe"] = field(
        default_factory=list,
        metadata={
            "name": "infMDFe",
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
        :ivar ch_mdfe: Chaves de acesso do MDF-e não encerrado
        :ivar n_prot: Número do Protocolo de autorização do MDF-e não
            encerrado
        """
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
        n_prot: Optional[str] = field(
            default=None,
            metadata={
                "name": "nProt",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/mdfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
