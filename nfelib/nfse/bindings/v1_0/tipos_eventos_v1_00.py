from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.nfse.bindings.v1_0.tipos_simples_v1_00 import (
    TsambGeradorEvt,
    TscodJustAnaliseFiscalCanc,
    TscodJustAnaliseFiscalCancDef,
    TscodJustAnaliseFiscalCancIndef,
    TscodJustCanc,
    TscodJustSubst,
    TscodMotivoRejeicao,
    TscodigoEventoNfse,
    TstipoAmbiente,
)
from nfelib.nfse.bindings.v1_0.xmldsig_core_schema_v1_00 import Signature

__NAMESPACE__ = "http://www.sped.fazenda.gov.br/nfse"


@dataclass
class TcinfoEventoAnulacaoRejeicao:
    """
    :ivar CPFAgTrib: CPF do agente da administração tributária municipal
        que efetuou o anulação da manifestação de rejeição da NFS-e.
    :ivar idEvManifRej: Referência ao Id da "Manifestação de rejeição da
        NFS-e" que originou o presente evento de anulação.
    :ivar xMotivo: Descrição para explicitar o motivo da anluação
    """
    class Meta:
        name = "TCInfoEventoAnulacaoRejeicao"

    CPFAgTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    idEvManifRej: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{59}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


class Te101101XDesc(Enum):
    CANCELAMENTO_DE_NFS_E = "Cancelamento de NFS-e"


class Te101103XDesc(Enum):
    SOLICITACAO_DE_ANALISE_FISCAL_PARA_CANCELAMENTO_DE_NFS_E = "Solicitacao de Analise Fiscal para Cancelamento de NFS-e"


class Te105102XDesc(Enum):
    CANCELAMENTO_DE_NFS_E_POR_SUBSTITUICAO = "Cancelamento de NFS-e por Substituicao"


class Te105104XDesc(Enum):
    CANCELAMENTO_DE_NFS_E_DEFERIDO_POR_AN_LISE_FISCAL = "Cancelamento de NFS-e Deferido por Análise Fiscal"


class Te105105XDesc(Enum):
    CANCELAMENTO_DE_NFS_E_INDEFERIDO_POR_AN_LISE_FISCAL = "Cancelamento de NFS-e Indeferido por Análise Fiscal"


class Te202201XDesc(Enum):
    CONFIRMA_O_DO_PRESTADOR = "Confirmação do Prestador"


class Te202205XDesc(Enum):
    REJEI_O_DO_PRESTADOR = "Rejeição do Prestador"


class Te203202XDesc(Enum):
    CONFIRMA_O_DO_TOMADOR = "Confirmação do Tomador"


class Te203206XDesc(Enum):
    REJEI_O_DO_TOMADOR = "Rejeição do Tomador"


class Te204203XDesc(Enum):
    CONFIRMA_O_DO_INTERMEDI_RIO = "Confirmação do Intermediário"


class Te204207XDesc(Enum):
    REJEI_O_DO_INTERMEDI_RIO = "Rejeição do Intermediário"


class Te205204XDesc(Enum):
    CONFIRMA_O_T_CITA = "Confirmação Tácita"


class Te205208XDesc(Enum):
    ANULA_O_DA_REJEI_O = "Anulação da Rejeição"


class Te305101XDesc(Enum):
    CANCELAMENTO_DE_NFS_E_POR_OF_CIO = "Cancelamento de NFS-e por Ofício"


class Te305102XDesc(Enum):
    BLOQUEIO_DE_NFS_E_POR_OF_CIO = "Bloqueio de NFS-e por Ofício"


class Te305103XDesc(Enum):
    DESBLOQUEIO_DE_NFS_E_POR_OF_CIO = "Desbloqueio de NFS-e por Ofício"


@dataclass
class TcinfoEventoRejeicao:
    """
    :ivar cMotivo: Motivo da Rejeição da NFS-e: 1 - NFS-e em
        duplicidade; 2 - NFS-e já emitida pelo tomador; 3 - Não
        ocorrência do fato gerador; 4 - Erro quanto a responsabilidade
        tributária; 5 - Erro quanto ao valor do serviço, valor das
        deduções ou serviço prestado ou data do fato gerador; 9 -
        Outros;
    :ivar xMotivo: Descrição para explicitar o motivo indicado neste
        evento
    """
    class Meta:
        name = "TCInfoEventoRejeicao"

    cMotivo: Optional[TscodMotivoRejeicao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class TclistaEventos:
    """
    :ivar codEvento: Grupo de informações de documento utilizado para
        Dedução/Redução do valor do serviço
    """
    class Meta:
        name = "TCListaEventos"

    codEvento: List[TscodigoEventoNfse] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_occurs": 1,
            "max_occurs": 9,
        }
    )


@dataclass
class Te101101:
    """
    :ivar xDesc: Descrição do Evento: Descrição do evento: "Cancelamento
        de NFS-e".
    :ivar cMotivo: Código de justificativa de cancelamento
    :ivar xMotivo: Descrição para explicitar o motivo indicado neste
        evento
    """
    class Meta:
        name = "TE101101"

    xDesc: Optional[Te101101XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )
    cMotivo: Optional[TscodJustCanc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class Te101103:
    """
    :ivar xDesc: Descrição do evento: "Solicitação de Análise Fiscal
        para Cancelamento de NFS-e"
    :ivar cMotivo: Código do motivo da solicitação de análise fiscal
        para cancelamento de NFS-e:
    :ivar xMotivo: Descrição para explicitar o motivo indicado neste
        evento
    """
    class Meta:
        name = "TE101103"

    xDesc: Optional[Te101103XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )
    cMotivo: Optional[TscodJustAnaliseFiscalCanc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class Te105102:
    """
    :ivar xDesc: Descrição do Evento: Descrição do evento: "Cancelamento
        de NFS-e por Substituição".
    :ivar cMotivo: Código de justificativa de cancelamento substituição
    :ivar xMotivo: Descrição para explicitar o motivo indicado neste
        evento
    :ivar chSubstituta: Chave de Acesso da NFS-e substituta.
    """
    class Meta:
        name = "TE105102"

    xDesc: Optional[Te105102XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )
    cMotivo: Optional[TscodJustSubst] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    chSubstituta: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 50,
            "white_space": "preserve",
            "pattern": r"[0-9]{50}",
        }
    )


@dataclass
class Te105104:
    """
    :ivar xDesc: Descrição do evento: "Cancelamento de NFS-e Deferido
        por Análise Fiscal"
    :ivar CPFAgTrib: CPF do agente da administração tributária municipal
        que efetuou o deferimento da  solicitação de análise fiscal para
        cancelamento de NFS-e.
    :ivar nProcAdm: Número do processo administrativo municipal
        vinculado à solicitação de análise fiscal para cancelamento de
        NFS-e.
    :ivar cMotivo: Resposta da solicitação de análise fiscal para
        cancelamento de NFS-e: 1 - Cancelamento de NFS-e Deferido.
    :ivar xMotivo: Descrição para explicitar o motivo indicado neste
        evento
    """
    class Meta:
        name = "TE105104"

    xDesc: Optional[Te105104XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )
    CPFAgTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    nProcAdm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,30}",
        }
    )
    cMotivo: Optional[TscodJustAnaliseFiscalCancDef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class Te105105:
    """
    :ivar xDesc: Descrição do evento: "Cancelamento de NFS-e Indeferido
        por Análise Fiscal".
    :ivar CPFAgTrib: CPF do agente da administração tributária municipal
        que efetuou o indeferimento da solicitação de análise fiscal
        para cancelamento de NFS-e.
    :ivar nProcAdm: Número do processo administrativo municipal
        vinculado à solicitação de análise fiscal para cancelamento de
        NFS-e.
    :ivar cMotivo: Resposta da solicitação de análise fiscal para
        cancelamento de NFS-e: 1 - Cancelamento de NFS-e Indeferido; 2 -
        Cancelamento de NFS-e Indeferido Sem Análise de Mérito.
    :ivar xMotivo: Descrição para explicitar o motivo indicado neste
        evento
    """
    class Meta:
        name = "TE105105"

    xDesc: Optional[Te105105XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )
    CPFAgTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    nProcAdm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,30}",
        }
    )
    cMotivo: Optional[TscodJustAnaliseFiscalCancIndef] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class Te202201:
    """
    :ivar xDesc: Descrição do evento: "Confirmação do Prestador".
    """
    class Meta:
        name = "TE202201"

    xDesc: Optional[Te202201XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )


@dataclass
class Te203202:
    """
    :ivar xDesc: Descrição do evento: "Confirmação do Tomador".
    """
    class Meta:
        name = "TE203202"

    xDesc: Optional[Te203202XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )


@dataclass
class Te204203:
    """
    :ivar xDesc: Descrição do evento: "Confirmação do Intermediário".
    """
    class Meta:
        name = "TE204203"

    xDesc: Optional[Te204203XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )


@dataclass
class Te205204:
    """
    :ivar xDesc: Descrição do evento: "Confirmação Tácita".
    """
    class Meta:
        name = "TE205204"

    xDesc: Optional[Te205204XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )


@dataclass
class Te205208:
    """
    :ivar xDesc: Descrição do evento: "Anulação da Rejeição".
    :ivar infAnRej:
    """
    class Meta:
        name = "TE205208"

    xDesc: Optional[Te205208XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )
    infAnRej: Optional[TcinfoEventoAnulacaoRejeicao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )


@dataclass
class Te305101:
    """
    :ivar xDesc: Descrição do evento: "Cancelamento de NFS-e por
        Ofício".
    :ivar CPFAgTrib: CPF do agente da administração tributária municipal
        que efetuou o cancelamento por ofício de NFS-e.
    :ivar nProcAdm: Número do processo administrativo municipal
        vinculado ao cancelamento de NFS-e por ofício.
    :ivar xProcAdm: Descrição para explicitar o motivo indicado neste
        evento.
    """
    class Meta:
        name = "TE305101"

    xDesc: Optional[Te305101XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )
    CPFAgTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    nProcAdm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,30}",
        }
    )
    xProcAdm: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class Te305102:
    """
    :ivar xDesc: Descrição do evento: "Bloqueio de NFS-e por Ofício".
    :ivar CPFAgTrib: CPF do agente da administração tributária municipal
        que efetuou o cancelamento por ofício de NFS-e.
    :ivar xMotivo: Descrição para explicitar o motivo indicado neste
        evento
    :ivar codEvento: Descrição para explicitar o motivo indicado neste
        evento
    """
    class Meta:
        name = "TE305102"

    xDesc: Optional[Te305102XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )
    CPFAgTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 15,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    codEvento: Optional[TscodigoEventoNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )


@dataclass
class Te305103:
    """
    :ivar xDesc: Descrição do evento: "Desbloqueio de NFS-e por Ofício".
    :ivar CPFAgTrib: CPF do agente da administração tributária municipal
        que efetuou o cancelamento por ofício de NFS-e.
    :ivar idBloqOfic: Referência ao Id da "Manifestação de rejeição da
        NFS-e" que originou o presente evento de anulação.
    """
    class Meta:
        name = "TE305103"

    xDesc: Optional[Te305103XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )
    CPFAgTrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    idBloqOfic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{59}",
        }
    )


@dataclass
class Te202205:
    """
    :ivar xDesc: Descrição do evento: "Rejeição do Prestador".
    :ivar infRej:
    """
    class Meta:
        name = "TE202205"

    xDesc: Optional[Te202205XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )
    infRej: Optional[TcinfoEventoRejeicao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )


@dataclass
class Te203206:
    """
    :ivar xDesc: Descrição do evento: "Rejeição do Tomador".
    :ivar infRej:
    """
    class Meta:
        name = "TE203206"

    xDesc: Optional[Te203206XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )
    infRej: Optional[TcinfoEventoRejeicao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )


@dataclass
class Te204207:
    """
    :ivar xDesc: Descrição do evento: "Rejeição do Intermediário".
    :ivar infRej:
    """
    class Meta:
        name = "TE204207"

    xDesc: Optional[Te204207XDesc] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
        }
    )
    infRej: Optional[TcinfoEventoRejeicao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )


@dataclass
class TcinfPedReg:
    """
    :ivar tpAmb: Identificação do Ambiente: 1 - Produção; 2 -
        Homologação
    :ivar verAplic: Versão do aplicativo que gerou o pedido de registro
        de evento.
    :ivar dhEvento: Data e hora do evento no formato AAAA-MM-
        DDThh:mm:ssTZD (UTC - Universal Coordinated Time, onde TZD pode
        ser -02:00 (Fernando de Noronha), -03:00 (Brasília) ou -04:00
        (Manaus), no horário de verão serão -01:00, -02:00 e -03:00.
        Ex.: 2010-08-19T13:00:15-03:00.
    :ivar CNPJAutor: CNPJ do autor do evento.
    :ivar CPFAutor: CPF do autor do evento.
    :ivar chNFSe: Chave de Acesso da NFS-e vinculada ao Evento
    :ivar nPedRegEvento: Número do pedido do registro de evento para o
        mesmo tipo de evento. Para os eventos que ocorrem somente uma
        vez, como é o caso do cancelamento, o nPedRegEvento deve ser
        igual a 1. Os eventos que podem ocorrer mais de uma vez devem
        ter o nPedRegEvento único.
    :ivar e101101: Evento de cancelamento
    :ivar e105102: Evento de cancelamento por substituição
    :ivar e101103: Solicitação de Análise Fiscal para Cancelamento de
        NFS-e
    :ivar e105104: Cancelamento de NFS-e Deferido por Análise Fiscal
    :ivar e105105: Cancelamento de NFS-e Indeferido por Análise Fiscal
    :ivar e202201: Confirmação do Prestador
    :ivar e203202: Confirmação do Tomador
    :ivar e204203: Confirmação do Intermediário
    :ivar e205204: Confirmação Tácita
    :ivar e202205: Rejeição do Prestador
    :ivar e203206: Rejeição do Tomador
    :ivar e204207: Rejeição do Intermediário
    :ivar e205208: Anulação da Rejeição
    :ivar e305101: Cancelamento de NFS-e por Ofício
    :ivar e305102: Bloqueio de NFS-e por Ofício
    :ivar e305103: Desbloqueio de NFS-e por Ofício
    :ivar Id:
    """
    class Meta:
        name = "TCInfPedReg"

    tpAmb: Optional[TstipoAmbiente] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    dhEvento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    CNPJAutor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    CPFAutor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    chNFSe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 50,
            "white_space": "preserve",
            "pattern": r"[0-9]{50}",
        }
    )
    nPedRegEvento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 3,
            "white_space": "preserve",
            "pattern": r"[0-9]{1}[0-9]{0,2}",
        }
    )
    e101101: Optional[Te101101] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e105102: Optional[Te105102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e101103: Optional[Te101103] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e105104: Optional[Te105104] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e105105: Optional[Te105105] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e202201: Optional[Te202201] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e203202: Optional[Te203202] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e204203: Optional[Te204203] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e205204: Optional[Te205204] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e202205: Optional[Te202205] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e203206: Optional[Te203206] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e204207: Optional[Te204207] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e205208: Optional[Te205208] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e305101: Optional[Te305101] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e305102: Optional[Te305102] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    e305103: Optional[Te305103] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 62,
            "white_space": "preserve",
            "pattern": r"PRE[0-9]{59}",
        }
    )


@dataclass
class TcpedRegEvt:
    class Meta:
        name = "TCPedRegEvt"

    infPedReg: Optional[TcinfPedReg] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"1\.00",
        }
    )


@dataclass
class TcinfEvento:
    """
    :ivar verAplic: Versão do aplicativo que gerou o pedido do evento.
    :ivar ambGer: Ambiente gerador do evento
    :ivar nSeqEvento: Sequencial do evento para o mesmo tipo de evento.
        Para maioria dos eventos nSeqEvento=1. Nos casos em que possa
        existir mais de um evento do mesmo tipo o ambiente gerador
        deverá numerar de forma sequencial.
    :ivar dhProc: Data/Hora do registro do evento. Data e hora no
        formato UTC (Universal Coordinated Time): AAAA-MM-
        DDThh:mm:ssTZD"
    :ivar nDFe: Ambiente gerador do evento
    :ivar pedRegEvento: Leiaute do pedido de registro do evento gerado
        pelo autor do evento
    :ivar Id:
    """
    class Meta:
        name = "TCInfEvento"

    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    ambGer: Optional[TsambGeradorEvt] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    nSeqEvento: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 3,
            "white_space": "preserve",
            "pattern": r"[0-9]{1}[0-9]{0,2}",
        }
    )
    dhProc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    nDFe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,13}",
        }
    )
    pedRegEvento: Optional[TcpedRegEvt] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    Id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 62,
            "white_space": "preserve",
            "pattern": r"EVT[0-9]{59}",
        }
    )


@dataclass
class Tcevento:
    class Meta:
        name = "TCEvento"

    infEvento: Optional[TcinfEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "required": True,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
            "pattern": r"1\.00",
        }
    )
