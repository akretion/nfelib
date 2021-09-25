from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from nfelib.nfe_ator_interessado.v1_0.leiaute_evento_ator_interessado_v1_00 import (
    DetEventoDescEvento1,
    DetEventoTpAutor1,
    DetEventoTpAutorizacao1,
    DetEventoVersao1,
    DetEventoXCondUso1,
)
from nfelib.nfe_ator_interessado.v1_0.tipos_basico_v1_03 import TcodUfIbge

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class DetEventoDescEvento2(Enum):
    ATOR_INTERESSADO_NA_NF_E = "Ator interessado na NF-e"


class DetEventoTpAutor2(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class DetEventoTpAutorizacao2(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class DetEventoVersao2(Enum):
    VALUE_1_00 = "1.00"


class DetEventoXCondUso2(Enum):
    O_EMITENTE_OU_DESTINAT_RIO_DA_NF_E_DECLARA_QUE_PERMITE_O_TRANSPORTADOR_DECLARADO_NO_CAMPO_CNPJ_CPF_DESTE_EVENTO_A_AUTORIZAR_OS_TRANSPORTADORES_SUBCONTRATADOS_OU_REDESPACHADOS_A_TEREM_ACESSO_AO_DOWNLOAD_DA_NF_E = "O emitente ou destinatário da NF-e, declara que permite o transportador declarado no campo CNPJ/CPF deste evento a autorizar os transportadores subcontratados ou redespachados a terem acesso ao download da NF-e"


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

    desc_evento: Optional[DetEventoDescEvento1] = field(
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
    tp_autor: Optional[DetEventoTpAutor1] = field(
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
    tp_autorizacao: Optional[DetEventoTpAutorizacao1] = field(
        default=None,
        metadata={
            "name": "tpAutorizacao",
            "type": "Element",
            "white_space": "preserve",
        }
    )
    x_cond_uso: Optional[DetEventoXCondUso1] = field(
        default=None,
        metadata={
            "name": "xCondUso",
            "type": "Element",
            "white_space": "preserve",
        }
    )
    versao: Optional[DetEventoVersao1] = field(
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
