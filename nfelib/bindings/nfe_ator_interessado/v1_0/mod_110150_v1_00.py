from dataclasses import dataclass, field
from typing import Optional
from nfelib.bindings.nfe_ator_interessado.v1_0.leiaute_evento_ator_interessado_v1_00 import (
    DetEventoDescEvento,
    DetEventoTpAutor,
    DetEventoTpAutorizacao,
    DetEventoVersao,
    DetEventoXCondUso,
)
from nfelib.bindings.nfe_ator_interessado.v1_0.tipos_basico_v1_03 import TcodUfIbge

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class DetEvento:
    """Schema XML de validação do evento de Ator Interessado na NF-e - Transportador (110150)”

    :ivar desc_evento: Descrição do Evento - "Ator interessado na NF-e”"
    :ivar c_orgao_autor:
    :ivar tp_autor: Tipo do Órgão Autor do Evento. Informar uma das
        opções 1=Geração do Evento pelo Emitente; 2=Geração do Evento
        pelo Destinatário; 3=Geração do Evento pelo Transportador Outros
        valores: 1=Empresa Emitente, 2=Empresa destinatária; 3=Empresa;
        5=Fisco; 6=RFB; 9=Outros Órgãos;
    :ivar ver_aplic: Versão do aplicativo do Autor do Evento.
    :ivar aut_xml: Pessoas autorizadas a acessar o XML da NF-e
    :ivar tp_autorizacao: 0 – Não permite; 1 – Permite o transportador
        autorizado pelo emitente ou destinatário autorizar outros
        transportadores para ter acesso ao download da NF-e
    :ivar x_cond_uso: Texto Fixo com as Condição de uso do tipo de
        autorização para o transportador:
    :ivar versao:
    """
    class Meta:
        name = "detEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    desc_evento: Optional[DetEventoDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    c_orgao_autor: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "name": "cOrgaoAutor",
            "type": "Element",
            "required": True,
        }
    )
    tp_autor: Optional[DetEventoTpAutor] = field(
        default=None,
        metadata={
            "name": "tpAutor",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    ver_aplic: Optional[str] = field(
        default=None,
        metadata={
            "name": "verAplic",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    aut_xml: Optional["DetEvento.AutXml"] = field(
        default=None,
        metadata={
            "name": "autXML",
            "type": "Element",
            "required": True,
        }
    )
    tp_autorizacao: Optional[DetEventoTpAutorizacao] = field(
        default=None,
        metadata={
            "name": "tpAutorizacao",
            "type": "Element",
            "white_space": "preserve",
        }
    )
    x_cond_uso: Optional[DetEventoXCondUso] = field(
        default=None,
        metadata={
            "name": "xCondUso",
            "type": "Element",
            "white_space": "preserve",
        }
    )
    versao: Optional[DetEventoVersao] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
        }
    )

    @dataclass
    class AutXml:
        cnpj: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJ",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{14}",
            }
        )
        cpf: Optional[str] = field(
            default=None,
            metadata={
                "name": "CPF",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[0-9]{11}",
            }
        )
