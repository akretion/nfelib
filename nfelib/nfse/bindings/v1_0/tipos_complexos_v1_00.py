from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from nfelib.nfse.bindings.v1_0.tipos_simples_v1_00 import (
    TcobjetoLocacao,
    TsambGeradorNfse,
    TscategVeic,
    TscategoriaServico,
    TscodJustSubst,
    TscodNaoNif,
    TsemitenteDps,
    TsenvMdic,
    TsideDedRed,
    TsmecAfcomExPrest,
    TsmecAfcomExToma,
    TsmodoPrestacao,
    TsmovTempBens,
    TsopConsumServ,
    TsopExigSuspensa,
    TsopSimpNac,
    TsopTipoBm,
    TsprocEmissao,
    TsregEspTrib,
    TsregimeApuracaoSimpNac,
    Tsrodagem,
    TstipoAmbiente,
    TstipoCst,
    TstipoEmissao,
    TstipoImunidadeIssqn,
    TstipoIndTotTrib,
    TstipoRetIssqn,
    TstipoRetPiscofins,
    TstribIssqn,
    Tsuf,
    TsvincPrest,
    Tstat,
)
from nfelib.nfse.bindings.v1_0.xmldsig_core_schema_v1_00 import Signature

__NAMESPACE__ = "http://www.sped.fazenda.gov.br/nfse"


@dataclass
class Tccserv:
    """
    :ivar cTribNac: Código de tributação nacional do ISSQN: Regra de
        formação - 6 dígitos numéricos sendo: 2 para Item (LC 116/2003),
        2 para Subitem (LC 116/2003) e 2 para Desdobro Nacional
    :ivar cTribMun: Código de tributação municipal do ISSQN
    :ivar xDescServ: Descrição completa do serviço prestado
    :ivar cNBS: Código NBS (Nomenclatura Brasileira de Serviços,
        Intangíveis e outras Operações que produzam Variações no
        Patrimônio) correspondente ao serviço prestado
    :ivar cIntContrib: Código interno do contribuinte
    """
    class Meta:
        name = "TCCServ"

    cTribNac: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{6}",
        }
    )
    cTribMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xDescServ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 2000,
            "white_space": "preserve",
            "pattern": r"[\s\S!-ÿ]{1}[\s\S -ÿ]{0,}[\s\S!-ÿ]{1}|[\s\S!-ÿ]{1}",
        }
    )
    cNBS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"[0-9]{9}",
        }
    )
    cIntContrib: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r"[a-zA-Z0-9]{1,20}",
        }
    )


@dataclass
class TcdocNfnfs:
    """
    :ivar nNFS: Número da Nota Fiscal NF ou NFS
    :ivar modNFS: Modelo da Nota Fiscal NF ou NFS
    :ivar serieNFS: Série Nota Fiscal NF ou NFS
    """
    class Meta:
        name = "TCDocNFNFS"

    nNFS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 7,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    modNFS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 15,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    serieNFS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 15,
            "white_space": "preserve",
            "pattern": r"[a-zA-Z0-9]{1,15}",
        }
    )


@dataclass
class TcdocOutNfse:
    """
    :ivar cMunNFSeMun: Código Município emissor da nota eletrônica
        municipal (Tabela do IBGE)
    :ivar nNFSeMun: Número da nota eletrônica municipal
    :ivar cVerifNFSeMun: Código de Verificação da nota eletrônica
        municipal
    """
    class Meta:
        name = "TCDocOutNFSe"

    cMunNFSeMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    nNFSeMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 15,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    cVerifNFSeMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 9,
            "white_space": "preserve",
            "pattern": r"[a-zA-Z0-9]{1,9}",
        }
    )


@dataclass
class TcenderExt:
    """
    :ivar cPais: Código do país (Tabela de Países ISO)
    :ivar cEndPost: Código alfanumérico do Endereçamento Postal no
        exterior do prestador do serviço.
    :ivar xCidade: Nome da cidade no exterior do prestador do serviço.
    :ivar xEstProvReg: Estado, província ou região da cidade no exterior
        do prestador do serviço.
    """
    class Meta:
        name = "TCEnderExt"

    cPais: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[A-Z]{2}",
        }
    )
    cEndPost: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 11,
            "white_space": "preserve",
        }
    )
    xCidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
        }
    )
    xEstProvReg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
        }
    )


@dataclass
class TcenderExtSimples:
    """
    :ivar cEndPost: Código alfanumérico do Endereçamento Postal no
        exterior do prestador do serviço.
    :ivar xCidade: Nome da cidade no exterior do prestador do serviço.
    :ivar xEstProvReg: Estado, província ou região da cidade no exterior
        do prestador do serviço.
    """
    class Meta:
        name = "TCEnderExtSimples"

    cEndPost: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 11,
            "white_space": "preserve",
        }
    )
    xCidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
        }
    )
    xEstProvReg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
        }
    )


@dataclass
class TcenderNac:
    """
    :ivar cMun: Código do município, conforme Tabela do IBGE
    :ivar CEP: Número do CEP
    """
    class Meta:
        name = "TCEnderNac"

    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )


@dataclass
class TcenderObraEvento:
    """
    :ivar cEndPost: Código de endereçamento postal
    :ivar xLgr: Tipo e nome do logradouro da localização do imóvel
    :ivar nro: Número do imóvel
    :ivar xCpl: Complemento do endereço
    :ivar xBairro: Bairro
    :ivar xCidade: Cidade
    :ivar xEstProvReg: Estado, província ou região
    """
    class Meta:
        name = "TCEnderObraEvento"

    cEndPost: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 11,
            "white_space": "preserve",
        }
    )
    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 156,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xCidade: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
        }
    )
    xEstProvReg: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
        }
    )


@dataclass
class TcinfoCompl:
    """
    :ivar idDocTec: Identificador de Documento de Responsabilidade
        Técnica: ART, RRT, DRT, Outros.
    :ivar docRef: Chave da nota, número identificador da nota, número do
        contrato ou outro identificador de documento emitido pelo
        prestador de serviços, que subsidia a emissão dessa nota pelo
        tomador do serviço ou intermediário (preenchimento obrigatório
        caso a nota esteja sendo emitida pelo Tomador ou intermediário
        do serviço).
    :ivar xInfComp: Informações complementares
    """
    class Meta:
        name = "TCInfoCompl"

    idDocTec: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 40,
            "white_space": "preserve",
        }
    )
    docRef: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xInfComp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 2000,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class TctribTotalMonet:
    """
    :ivar vTotTribFed: Valor monetário total aproximado dos tributos
        federais (R$).
    :ivar vTotTribEst: Valor monetário total aproximado dos tributos
        estaduais (R$).
    :ivar vTotTribMun: Valor monetário total aproximado dos tributos
        municipais (R$).
    """
    class Meta:
        name = "TCTribTotalMonet"

    vTotTribFed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    vTotTribEst: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    vTotTribMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )


@dataclass
class TctribTotalPercent:
    """
    :ivar pTotTribFed: Valor percentual total aproximado dos tributos
        federais (%).
    :ivar pTotTribEst: Valor percentual total aproximado dos tributos
        estaduais (%).
    :ivar pTotTribMun: Valor percentual total aproximado dos tributos
        municipais (%).
    """
    class Meta:
        name = "TCTribTotalPercent"

    pTotTribFed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    pTotTribEst: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    pTotTribMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )


@dataclass
class TcvdescCondIncond:
    """
    :ivar vDescIncond: Valor monetário do desconto incondicionado (R$)
    :ivar vDescCond: Valor monetário do desconto condicionado (R$)
    """
    class Meta:
        name = "TCVDescCondIncond"

    vDescIncond: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    vDescCond: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )


@dataclass
class TcvservPrest:
    """
    :ivar vReceb: Valor monetário recebido pelo intermediário do serviço
        (R$)
    :ivar vServ: Valor dos serviços em R$
    """
    class Meta:
        name = "TCVServPrest"

    vReceb: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    vServ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )


@dataclass
class TcvaloresNfse:
    """
    :ivar vCalcDR: Valor monetário (R$) de dedução/redução da base de
        cálculo (BC) do ISSQN.
    :ivar tpBM: Tipo de Benefício Municipal (BM)
    :ivar vCalcBM: Valor monetário (R$) do percentual de redução da base
        de cálculo (BC) do ISSQN devido a um benefício municipal (BM).
    :ivar vBC: Valor monetário (R$) do percentual de redução da base de
        cálculo (BC) do ISSQN devido a um benefício municipal (BM).
    :ivar pAliqAplic: Alíquota aplicada sobre a base de cálculo para
        apuração do ISSQN.
    :ivar vISSQN: Valor do ISSQN (R$) = Valor da Base de Cálculo x
        Alíquota ISSQN = vBC x pAliqAplic
    :ivar vTotalRet: Valor total de retenções = Σ(CP + IRRF + CSLL  +
        ISSQN* +  (PIS + COFINS)**) vTotalRet (R$) = (vRetCP + vRetIRRF
        + vRetCSLL) + vISSQN* + (vPIS + vCOFINS)**
    :ivar vLiq: Valor líquido = Valor do serviço - Desconto condicionado
        - Desconto incondicionado - Valores retidos (CP, IRRF, CSLL)* -
        Valores, se retidos (ISSQN, PIS, COFINS)** Valor Líquido (R$) =
        vServ – vDescIncond – vDescCond – (vRetCP + vRetIRRF +
        vRetCSLL)* – (vISSQN - vPIS + vCOFINS)**
    :ivar xOutInf: Uso da Administração Tributária Municipal.
    """
    class Meta:
        name = "TCValoresNFSe"

    vCalcDR: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    tpBM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 40,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    vCalcBM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    vBC: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    pAliqAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|[0-9]{1}(\.[0-9]{2})?",
        }
    )
    vISSQN: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    vTotalRet: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    vLiq: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    xOutInf: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 2000,
            "white_space": "preserve",
            "pattern": r"[\s\S!-ÿ]{1}[\s\S -ÿ]{0,}[\s\S!-ÿ]{1}|[\s\S!-ÿ]{1}",
        }
    )


@dataclass
class TcbeneficioMunicipal:
    """
    :ivar tpBM: Identificação da Lei parametrizada pelo município que
        define o benefício. Trata-se de um identificador único que foi
        gerado pelo Sistema Nacional no momento em que o município de
        incidência do ISSQN incluiu o benefício no sistema. Tem a
        seguinte regra de formação: 7 dígitos com o código IBGE do
        município + 4 dígitos com número sequencial. Deve ser obtido da
        parametrização do município de incidência do ISSQN.
    :ivar nBM: Identificador do benefício municipal parametrizado pelo
        município.
    :ivar vRedBCBM: Valor monetário informado pelo emitente para redução
        da base de cálculo (BC) do ISSQN devido a um Benefício Municipal
        (BM).
    :ivar pRedBCBM: Valor percentual informado pelo emitente para
        redução da base de cálculo (BC) do ISSQN devido a um Benefício
        Municipal (BM).
    """
    class Meta:
        name = "TCBeneficioMunicipal"

    tpBM: Optional[TsopTipoBm] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    nBM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "pattern": r"[0-9]{14}",
        }
    )
    vRedBCBM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    pRedBCBM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )


@dataclass
class TccomExterior:
    """
    :ivar mdPrestacao: Modo de Prestação: 0 - Desconhecido (tipo não
        informado na nota de origem); 1 - Transfronteiriço; 2 - Consumo
        no Brasil; 3 - Presença Comercial no Exterior; 4 - Movimento
        Temporário de Pessoas Físicas;
    :ivar vincPrest: Vínculo entre as partes no negócio: 0 - Sem vínculo
        com o tomador/ Prestador 1 - Controlada; 2 - Controladora; 3 -
        Coligada; 4 - Matriz; 5 - Filial ou sucursal; 6 - Outro vínculo;
    :ivar tpMoeda: Identifica a moeda da transação comercial
    :ivar vServMoeda: Valor do serviço prestado expresso em moeda
        estrangeira especificada em tpmoeda
    :ivar mecAFComexP: Mecanismo de apoio/fomento ao Comércio Exterior
        utilizado pelo prestador do serviço: 00 - Desconhecido (tipo não
        informado na nota de origem); 01 - Nenhum; 02 - ACC -
        Adiantamento sobre Contrato de Câmbio – Redução a Zero do IR e
        do IOF; 03 - ACE – Adiantamento sobre Cambiais Entregues -
        Redução a Zero do IR e do IOF; 04 - BNDES-Exim Pós-Embarque –
        Serviços; 05 - BNDES-Exim Pré-Embarque - Serviços; 06 - FGE -
        Fundo de Garantia à Exportação; 07 - PROEX - EQUALIZAÇÃO 08 -
        PROEX - Financiamento;
    :ivar mecAFComexT: Mecanismo de apoio/fomento ao Comércio Exterior
        utilizado pelo tomador do serviço: 00 - Desconhecido (tipo não
        informado na nota de origem); 01 - Nenhum; 02 - Adm. Pública e
        Repr. Internacional; 03 - Alugueis e Arrend. Mercantil de
        maquinas, equip., embarc. e aeronaves; 04 - Arrendamento
        Mercantil de aeronave para empresa de transporte aéreo público;
        05 - Comissão a agentes externos na exportação; 06 - Despesas de
        armazenagem, mov. e transporte de carga no exterior; 07 -
        Eventos FIFA (subsidiária); 08 - Eventos FIFA; 09 - Fretes,
        arrendamentos de embarcações ou aeronaves e outros; 10 -
        Material Aeronáutico; 11 - Promoção de Bens no Exterior; 12 -
        Promoção de Dest. Turísticos Brasileiros; 13 - Promoção do
        Brasil no Exterior; 14 - Promoção Serviços no Exterior; 15 -
        RECINE; 16 - RECOPA; 17 - Registro e Manutenção de marcas,
        patentes e cultivares; 18 - REICOMP; 19 - REIDI; 20 - REPENEC;
        21 - REPES; 22 - RETAERO; 23 - RETID; 24 - Royalties,
        Assistência Técnica, Científica e Assemelhados; 25 - Serviços de
        avaliação da conformidade vinculados aos Acordos da OMC; 26 -
        ZPE;
    :ivar movTempBens: Operação está vinculada à Movimentação Temporária
        de Bens: 0 - Desconhecido (tipo não informado na nota de
        origem); 1 - Não 2 - Vinculada - Declaração de Importação 3 -
        Vinculada - Declaração de Exportação
    :ivar nDI: Número da Declaração de Importação (DI/DSI/DA/DRI-E)
        averbado
    :ivar nRE: Número do Registro de Exportação (RE) averbado
    :ivar mdic: Compartilhar as informações da NFS-e gerada a partir
        desta DPS com a Secretaria de Comércio Exterior: 0 - Não enviar
        para o MDIC; 1 - Enviar para o MDIC;
    """
    class Meta:
        name = "TCComExterior"

    mdPrestacao: Optional[TsmodoPrestacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    vincPrest: Optional[TsvincPrest] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    tpMoeda: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 3,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    vServMoeda: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    mecAFComexP: Optional[TsmecAfcomExPrest] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    mecAFComexT: Optional[TsmecAfcomExToma] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    movTempBens: Optional[TsmovTempBens] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    nDI: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 12,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nRE: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 12,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    mdic: Optional[TsenvMdic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )


@dataclass
class Tcendereco:
    """
    :ivar endNac: Grupo de informações específicas de endereço nacional
    :ivar endExt: Grupo de informações específicas de endereço no
        exterior
    :ivar xLgr: Tipo e nome do logradouro da localização do imóvel
    :ivar nro: Número do imóvel
    :ivar xCpl: Complemento do endereço
    :ivar xBairro: Bairro
    """
    class Meta:
        name = "TCEndereco"

    endNac: Optional[TcenderNac] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    endExt: Optional[TcenderExt] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 156,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class TcenderecoEmitente:
    """
    :ivar xLgr: Tipo e nome do logradouro da localização do imóvel
    :ivar nro: Número do imóvel
    :ivar xCpl: Complemento do endereço
    :ivar xBairro: Bairro
    :ivar cMun: Código do município, conforme Tabela do IBGE
    :ivar UF: Sigla da unidade da federação do município do endereço do
        emitente.
    :ivar CEP: Número do CEP
    """
    class Meta:
        name = "TCEnderecoEmitente"

    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 156,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    UF: Optional[Tsuf] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )


@dataclass
class TcenderecoSimples:
    """
    :ivar CEP: Número do CEP
    :ivar endExt: Grupo de informações específicas de endereço no
        exterior
    :ivar xLgr: Tipo e nome do logradouro da localização do imóvel
    :ivar nro: Número do imóvel
    :ivar xCpl: Complemento do endereço
    :ivar xBairro: Bairro
    """
    class Meta:
        name = "TCEnderecoSimples"

    CEP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    endExt: Optional[TcenderExtSimples] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    xLgr: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xCpl: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 156,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xBairro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class TcexigSuspensa:
    """
    :ivar tpSusp: Opção para Exigibilidade Suspensa: 1 - Exigibilidade
        Suspensa por Decisão Judicial; 2 - Exigibilidade Suspensa por
        Processo Administrativo;
    :ivar nProcesso: Número do processo judicial ou administrativo de
        suspensão da exigibilidade
    """
    class Meta:
        name = "TCExigSuspensa"

    tpSusp: Optional[TsopExigSuspensa] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    nProcesso: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "pattern": r"[0-9]{30}",
        }
    )


@dataclass
class TcexploracaoRodoviaria:
    """
    :ivar categVeic: Categorias de veículos para cobrança: 00 -
        Categoria de Veículos (tipo não informado na nota de origem); 01
        - Automóvel, caminhonete e furgão; 02 - Caminhão leve, ônibus,
        caminhão trator e furgão; 03 - Automóvel e caminhonete com
        semireboque; 04 - Caminhão, caminhão-trator, caminhão-trator com
        semi-reboque e ônibus; 05 - Automóvel e caminhonete com reboque;
        06 - Caminhão com reboque e caminhãotrator com semi-reboque; 07
        - Caminhão com reboque e caminhãotrator com semi-reboque; 08 -
        Caminhão com reboque e caminhãotrator com semi-reboque; 09 -
        Motocicletas, motonetas e bicicletas motorizadas; 10 - Veículo
        especial; 11 - Veículo Isento;
    :ivar nEixos: Número de eixos para fins de cobrança
    :ivar rodagem: Tipo de rodagem
    :ivar sentido: Placa do veículo
    :ivar placa: Placa do veículo
    :ivar codAcessoPed: Código de acesso gerado automaticamente pelo
        sistema emissor da concessionária.
    :ivar codContrato: Código de contrato gerado automaticamente pelo
        sistema nacional no cadastro da concessionária.
    """
    class Meta:
        name = "TCExploracaoRodoviaria"

    categVeic: Optional[TscategVeic] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    nEixos: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,2}",
        }
    )
    rodagem: Optional[Tsrodagem] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    sentido: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,3}",
        }
    )
    placa: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[A-Z]{2,3}[0-9]{4}|[A-Z]{3,4}[0-9]{3}",
        }
    )
    codAcessoPed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[a-zA-Z0-9]{10}",
        }
    )
    codContrato: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[a-zA-Z0-9]{4}",
        }
    )


@dataclass
class TclocPrest:
    """
    :ivar cLocPrestacao: Código do município onde o serviço foi prestado
        (tabela do IBGE)
    :ivar cPaisPrestacao: Código do país onde o serviço foi prestado
        (Tabela de Países ISO)
    :ivar opConsumServ: Opção para que o emitente informe onde ocorreu o
        consumo do serviço prestado. 0 - Consumo do serviço prestado
        ocorrido no município do local da prestação; 1 - Consumo do
        serviço prestado ocorrido ocorrido no exterior ;
    """
    class Meta:
        name = "TCLocPrest"

    cLocPrestacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    cPaisPrestacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"[A-Z]{2}",
        }
    )
    opConsumServ: Optional[TsopConsumServ] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )


@dataclass
class TclocacaoSublocacao:
    """
    :ivar categ: Categoria do serviço
    :ivar objeto: Tipo de objetos da locação, sublocação, arrendamento,
        direito de passagem ou permissão de uso
    :ivar extensao: Extensão total da ferrovia, rodovia, cabos, dutos ou
        condutos
    :ivar nPostes: Número total de postes
    """
    class Meta:
        name = "TCLocacaoSublocacao"

    categ: Optional[TscategoriaServico] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    objeto: Optional[TcobjetoLocacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    extensao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,5}",
        }
    )
    nPostes: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 6,
            "white_space": "preserve",
            "pattern": r"[0-9]{1,6}",
        }
    )


@dataclass
class TcregTrib:
    """
    :ivar opSimpNac: Situação perante o Simples Nacional: 1 - Não
        Optante; 2 - Optante - Microempreendedor Individual (MEI); 3 -
        Optante - Microempresa ou Empresa de Pequeno Porte (ME/EPP);
    :ivar regApTribSN: Opção para que o contribuinte optante pelo
        Simples Nacional ME/EPP (opSimpNac = 3) possa indicar, ao emitir
        o documento fiscal, em qual regime de apuração os tributos
        federais e municipal estão inseridos, caso tenha ultrapassado
        algum sublimite ou limite definido para o Simples Nacional. 1 –
        Regime de apuração dos tributos federais e municipal pelo SN; 2
        – Regime de apuração dos tributos federais pelo SN e ISSQN  por
        fora do SN conforme respectiva legislação municipal do tributo;
        3 – Regime de apuração dos tributos federais e municipal por
        fora do SN conforme respectivas legilações federal e municipal
        de cada tributo;
    :ivar regEspTrib: Tipos de Regimes Especiais de Tributação: 0 -
        Nenhum; 1 - Ato Cooperado (Cooperativa); 2 - Estimativa; 3 -
        Microempresa Municipal; 4 - Notário ou Registrador; 5 -
        Profissional Autônomo; 6 - Sociedade de Profissionais;
    """
    class Meta:
        name = "TCRegTrib"

    opSimpNac: Optional[TsopSimpNac] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    regApTribSN: Optional[TsregimeApuracaoSimpNac] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    regEspTrib: Optional[TsregEspTrib] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )


@dataclass
class Tcsubstituicao:
    """
    :ivar chSubstda: Chave de acesso da NFS-e a ser substituída
    :ivar cMotivo: Código de justificativa para substituição de NFS-e:
        01 - Desenquadramento de NFS-e do Simples Nacional; 02 -
        Enquadramento de NFS-e no Simples Nacional; 03 - Inclusão
        Retroativa de Imunidade/Isenção para NFS-e; 04 - Exclusão
        Retroativa de Imunidade/Isenção para NFS-e; 05 - Rejeição de
        NFS-e pelo tomador ou pelo intermediário se responsável pelo
        recolhimento do tributo; 99 - Outros;
    :ivar xMotivo: Descrição do motivo da substituição da NFS-e
    """
    class Meta:
        name = "TCSubstituicao"

    chSubstda: Optional[str] = field(
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


@dataclass
class TctribOutrosPisCofins:
    """
    :ivar CST: Código de Situação Tributária do PIS/COFINS (CST): 00 -
        Nenhum; 01 - Operação Tributável com Alíquota Básica; 02 -
        Operação Tributável com Alíquota Diferenciada; 03 - Operação
        Tributável com Alíquota por Unidade de Medida de Produto; 04 -
        Operação Tributável monofásica - Revenda a Alíquota Zero; 05 -
        Operação Tributável por Substituição Tributária; 06 - Operação
        Tributável a Alíquota Zero; 07 - Operação Tributável da
        Contribuição; 08 - Operação sem Incidência da Contribuição; 09 -
        Operação com Suspensão da Contribuição;
    :ivar vBCPisCofins: Valor da Base de Cálculo do PIS/COFINS (R$).
    :ivar pAliqPis: Valor da Alíquota do PIS (%).
    :ivar pAliqCofins: Valor da Alíquota da COFINS (%).
    :ivar vPis: Valor monetário do PIS (R$).
    :ivar vCofins: Valor monetário do COFINS (R$).
    :ivar tpRetPisCofins: Tipo de retencao do Pis/Cofins: 1 - Retido; 2
        - Não Retido;
    """
    class Meta:
        name = "TCTribOutrosPisCofins"

    CST: Optional[TstipoCst] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    vBCPisCofins: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    pAliqPis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})?",
        }
    )
    pAliqCofins: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})?",
        }
    )
    vPis: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    vCofins: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    tpRetPisCofins: Optional[TstipoRetPiscofins] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )


@dataclass
class TctribTotal:
    """
    :ivar vTotTrib: Valor monetário total aproximado dos tributos, em
        conformidade com o artigo 1o da Lei no 12.741/2012
    :ivar pTotTrib: Valor percentual total aproximado dos tributos, em
        conformidade com o artigo 1o da Lei no 12.741/2012
    :ivar indTotTrib: Indicador de informação de valor total de
        tributos. Possui valor fixo igual a zero (indTotTrib=0). Não
        informar nenhum valor estimado para os Tributos (Decreto
        8.264/2014). 0 - Não;
    :ivar pTotTribSN: Valor percentual aproximado do total dos tributos
        da alíquota do Simples Nacional (%)
    """
    class Meta:
        name = "TCTribTotal"

    vTotTrib: Optional[TctribTotalMonet] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    pTotTrib: Optional[TctribTotalPercent] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    indTotTrib: Optional[TstipoIndTotTrib] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    pTotTribSN: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,1}(\.[0-9]{2})?",
        }
    )


@dataclass
class TcatvEvento:
    """
    :ivar desc: Descrição do evento Artístico, Cultural, Esportivo, etc
    :ivar dtIni: Data de início da atividade de evento. Ano, Mês e Dia
        (AAAA-MM-DD)
    :ivar dtFim: Data de fim da atividade de evento. Ano, Mês e Dia
        (AAAA-MM-DD)
    :ivar id: Identificação da Atividade de Evento (código identificador
        de evento determinado pela Administração Tributária Municipal)
    :ivar end: Grupo de informações relativas ao endereço da atividade,
        evento ou local do serviço prestado
    """
    class Meta:
        name = "TCAtvEvento"

    desc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    dtIni: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    dtFim: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
        }
    )
    end: Optional[TcenderecoSimples] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )


@dataclass
class Tcemitente:
    """
    :ivar CNPJ: Número do CNPJ do emitente da NFS-e.
    :ivar CPF: Número do CPF do emitente da NFS-e.
    :ivar IM: Número da inscrição municipal
    :ivar xNome: Nome / Razão Social do emitente.
    :ivar xFant: Nome / Fantasia do emitente.
    :ivar enderNac: Grupo de informações do endereço nacional do
        Emitente da NFS-e
    :ivar fone: Número do telefone do emitente. (Preencher com o Código
        DDD + número do telefone. Nas operações com exterior é permitido
        informar o código do país + código da localidade + número do
        telefone)
    :ivar email: E-mail do emitente.
    """
    class Meta:
        name = "TCEmitente"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    CPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    IM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 15,
            "white_space": "preserve",
        }
    )
    xNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "preserve",
        }
    )
    xFant: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
        }
    )
    enderNac: Optional[TcenderecoEmitente] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"[0-9]{6,20}",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 80,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class TcinfoObra:
    """
    :ivar cObra: Número de identificação da obra. Cadastro Nacional de
        Obras (CNO) ou Cadastro Específico do INSS (CEI).
    :ivar inscImobFisc: Inscrição imobiliária fiscal (código fornecido
        pela Prefeitura Municipal para a identificação da obra ou para
        fins de recolhimento do IPTU)
    :ivar end: Grupo de informações do endereço da obra do serviço
        prestado
    """
    class Meta:
        name = "TCInfoObra"

    cObra: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
        }
    )
    inscImobFisc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
        }
    )
    end: Optional[TcenderecoSimples] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )


@dataclass
class TcinfoPessoa:
    """Informações das pessoas envolvidas na NFS-e.

    Pode ser o tomador, o intermediário ou o fornecedor
    (dedução/redução)

    :ivar CNPJ: Número do CNPJ
    :ivar CPF: Número do CPF
    :ivar NIF: Número de Identificação Fiscal fornecido por órgão de
        administração tributária no exterior
    :ivar cNaoNIF: Motivo para não informação do NIF: 0 - Não informado
        na nota de origem; 1 - Dispensado do NIF; 2 - Não exigência do
        NIF;
    :ivar CAEPF: Número do Cadastro de Atividade Econômica da Pessoa
        Física (CAEPF)
    :ivar IM: Número da inscrição municipal
    :ivar xNome: Nome/Nome Empresarial
    :ivar end: Dados de endereço
    :ivar fone: Número do telefone do prestador: Preencher com o Código
        DDD + número do telefone. Nas operações com exterior é permitido
        informar o código do país + código da localidade + número do
        telefone)
    :ivar email: E-mail
    """
    class Meta:
        name = "TCInfoPessoa"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    CPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    NIF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 40,
            "white_space": "preserve",
        }
    )
    cNaoNIF: Optional[TscodNaoNif] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    CAEPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    IM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 15,
            "white_space": "preserve",
        }
    )
    xNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 300,
            "white_space": "preserve",
        }
    )
    end: Optional[Tcendereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"[0-9]{6,20}",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 80,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass
class TcinfoPrestador:
    """Informações do prestador da NFS-e.

    Difere das demais pessoas por causa das informações de regimes de
    tributação

    :ivar CNPJ: Número do CNPJ
    :ivar CPF: Número do CPF
    :ivar NIF: Número de Identificação Fiscal fornecido por órgão de
        administração tributária no exterior
    :ivar cNaoNIF: Motivo para não informação do NIF: 1 - Dispensado do
        NIF; 2 - Não exigência do NIF;
    :ivar CAEPF: Número do Cadastro de Atividade Econômica da Pessoa
        Física (CAEPF) do prestador do serviço.
    :ivar IM: Número da inscrição municipal
    :ivar xNome: Nome/Nome Empresarial do prestador
    :ivar end: Dados de endereço do prestador
    :ivar fone: Número do telefone do prestador: Preencher com o Código
        DDD + número do telefone. Nas operações com exterior é permitido
        informar o código do país + código da localidade + número do
        telefone)
    :ivar email: E-mail
    :ivar regTrib: Grupo de informações relativas aos regimes de
        tributação do prestador de serviços
    """
    class Meta:
        name = "TCInfoPrestador"

    CNPJ: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    CPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        }
    )
    NIF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 40,
            "white_space": "preserve",
        }
    )
    cNaoNIF: Optional[TscodNaoNif] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    CAEPF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9]{14}",
        }
    )
    IM: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 15,
            "white_space": "preserve",
        }
    )
    xNome: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 300,
            "white_space": "preserve",
        }
    )
    end: Optional[Tcendereco] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    fone: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"[0-9]{6,20}",
        }
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 80,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    regTrib: Optional[TcregTrib] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )


@dataclass
class TctribMunicipal:
    """
    :ivar tribISSQN: Tributação do ISSQN sobre o serviço prestado: 1 -
        Operação tributável; 2 - Exportação de serviço; 3 - Não
        Incidência; 4 - Imunidade;
    :ivar cPaisResult: Código do país onde se verficou o resultado da
        prestação do serviço para o caso de Exportação de
        Serviço.(Tabela de Países ISO)
    :ivar BM: Tributação do ISSQN sobre o serviço prestado: 1 - Operação
        tributável; 2 - Exportação de serviço; 3 - Não Incidência; 4 -
        Imunidade;
    :ivar exigSusp: Informações para a suspensão da Exigibilidade do
        ISSQN
    :ivar tpImunidade: Identificação da Imunidade do ISSQN – somente
        para o caso de Imunidade: 0 - Imunidade (tipo não informado na
        nota de origem); 1 - Patrimônio, renda ou serviços, uns dos
        outros (CF88, Art 150, VI, a); 2 - Templos de qualquer culto
        (CF88, Art 150, VI, b); 3 - Patrimônio, renda ou serviços dos
        partidos políticos, inclusive suas fundações, das entidades
        sindicais dos trabalhadores, das instituições de educação e de
        assistência social, sem fins lucrativos, atendidos os requisitos
        da lei (CF88, Art 150, VI, c); 4 - Livros, jornais, periódicos e
        o papel destinado a sua impressão (CF88, Art 150, VI, d);
    :ivar pAliq: Valor da alíquota (%) do serviço prestado relativo ao
        município sujeito ativo (município de incidência) do ISSQN. Se o
        município de incidência pertence ao Sistema Nacional NFS-e a
        alíquota estará parametrizada e, portanto, será fornecida pelo
        sistema. Se o município de incidência não pertence ao Sistema
        Nacional NFS-e a alíquota não estará parametrizada e, por isso,
        deverá ser fornecida pelo emitente.
    :ivar tpRetISSQN: Tipo de retencao do ISSQN: 1 - Não Retido; 2 -
        Retido pelo Tomador; 3 - Retido pelo Intermediario;
    """
    class Meta:
        name = "TCTribMunicipal"

    tribISSQN: Optional[TstribIssqn] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    cPaisResult: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"[A-Z]{2}",
        }
    )
    BM: Optional[TcbeneficioMunicipal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    exigSusp: Optional[TcexigSuspensa] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    tpImunidade: Optional[TstipoImunidadeIssqn] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    pAliq: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|[0-9]{1}(\.[0-9]{2})?",
        }
    )
    tpRetISSQN: Optional[TstipoRetIssqn] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )


@dataclass
class TctribNacional:
    """
    :ivar piscofins: Grupo de informações dos tributos PIS/COFINS
    :ivar vRetCP: Valor monetário do CP(R$).
    :ivar vRetIRRF: Valor monetário do IRRF (R$).
    :ivar vRetCSLL: Valor monetário do CSLL (R$).
    """
    class Meta:
        name = "TCTribNacional"

    piscofins: Optional[TctribOutrosPisCofins] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    vRetCP: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    vRetIRRF: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    vRetCSLL: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )


@dataclass
class TcdocDedRed:
    """
    :ivar chNFSe: Chave de Acesso da NFS-e (Padrão Nacional)
    :ivar chNFe: Chave de Acesso da NF-e
    :ivar NFSeMun: Grupo de informações de Outras NFS-e (Padrão anterior
        de NFS-e)
    :ivar NFNFS: Grupo de informações de NF ou NFS (Modelo não
        eletrônico)
    :ivar nDocFisc: Número de documento fiscal
    :ivar nDoc: Número de documento não fiscal
    :ivar tpDedRed: Identificação da Dedução/Redução: 1 – Alimentação e
        bebidas/frigobar; 2 – Materiais; 3 – Produção externa; 4 –
        Reembolso de despesas; 5 – Repasse consorciado; 6 – Repasse
        plano de saúde; 7 – Serviços; 8 – Subempreitada de mão de obra;
        99 – Outras deduções;
    :ivar xDescOutDed: Descrição da Dedução/Redução quando a opção é "99
        – Outras Deduções"
    :ivar dtEmiDoc: Data da emissão do documento dedutível. Ano, mês e
        dia (AAAA-MM-DD)
    :ivar vDedutivelRedutivel: Valor monetário total dedutível/redutível
        no documento informado (R$). Este é o valor total no documento
        informado que é passível de dedução/redução.
    :ivar vDeducaoReducao: Valor monetário utilizado para
        dedução/redução do valor do serviço da NFS-e que está sendo
        emitida (R$). Deve ser menor ou igual ao valor
        deduzível/redutível (vDedutivelRedutivel).
    :ivar fornec: Grupo de informações do Fornecedor em Deduções de
        Serviços
    """
    class Meta:
        name = "TCDocDedRed"

    chNFSe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "max_length": 50,
            "white_space": "preserve",
            "pattern": r"[0-9]{50}",
        }
    )
    chNFe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "max_length": 44,
            "white_space": "preserve",
            "pattern": r"[0-9]{44}",
        }
    )
    NFSeMun: Optional[TcdocOutNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    NFNFS: Optional[TcdocNfnfs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    nDocFisc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nDoc: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    tpDedRed: Optional[TsideDedRed] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    xDescOutDed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    dtEmiDoc: Optional[XmlDate] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    vDedutivelRedutivel: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    vDeducaoReducao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    fornec: Optional[TcinfoPessoa] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )


@dataclass
class TcinfoTributacao:
    """
    :ivar tribMun: Grupo de informações relacionados ao Imposto Sobre
        Serviços de Qualquer Natureza - ISSQN
    :ivar tribNac: Grupo de informações de outros tributos relacionados
        ao serviço prestado
    :ivar totTrib: Grupo de informações para totais aproximados dos
        tributos relacionados ao serviço prestado
    """
    class Meta:
        name = "TCInfoTributacao"

    tribMun: Optional[TctribMunicipal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    tribNac: Optional[TctribNacional] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    totTrib: Optional[TctribTotal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )


@dataclass
class Tcserv:
    """
    :ivar locPrest: Grupo de informações relativas ao local da prestação
        do serviço
    :ivar cServ: Grupo de informações relativas ao código do serviço
        prestado
    :ivar comExt: Grupo de informações relativas à exportação/importação
        de serviço prestado
    :ivar lsadppu: Grupo de informações relativas a atividades de
        Locação, sublocação, arrendamento, direito de passagem ou
        permissão de uso, compartilhado ou não, de ferrovia, rodovia,
        postes, cabos, dutos e condutos de qualquer natureza
    :ivar obra: Grupo de informações do DPS relativas à serviço de obra
    :ivar atvEvento: Grupo de informações do DPS relativas à Evento
    :ivar explRod: Grupo de informações relativas a pedágio
    :ivar infoCompl: Grupo de informações complementares disponível para
        todos os serviços prestados
    """
    class Meta:
        name = "TCServ"

    locPrest: Optional[TclocPrest] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    cServ: Optional[Tccserv] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    comExt: Optional[TccomExterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    lsadppu: Optional[TclocacaoSublocacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    obra: Optional[TcinfoObra] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    atvEvento: Optional[TcatvEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    explRod: Optional[TcexploracaoRodoviaria] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    infoCompl: Optional[TcinfoCompl] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )


@dataclass
class TclistaDocDedRed:
    """
    :ivar docDedRed: Grupo de informações de documento utilizado para
        Dedução/Redução do valor do serviço
    """
    class Meta:
        name = "TCListaDocDedRed"

    docDedRed: List[TcdocDedRed] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_occurs": 1,
            "max_occurs": 1000,
        }
    )


@dataclass
class TcinfoDedRed:
    """
    :ivar pDR: Valor percentual padrão para dedução/redução do valor do
        serviço
    :ivar vDR: Valor monetário padrão para dedução/redução do valor do
        serviço
    :ivar documentos: Grupo de informações de documento utilizado para
        Dedução/Redução do valor do serviço
    """
    class Meta:
        name = "TCInfoDedRed"

    pDR: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,2}(\.[0-9]{2})?",
        }
    )
    vDR: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,14}(\.[0-9]{2})?",
        }
    )
    documentos: Optional[TclistaDocDedRed] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )


@dataclass
class TcinfoValores:
    """
    :ivar vServPrest: Grupo de informações relativas aos valores do
        serviço prestado
    :ivar vDescCondIncond: Grupo de informações relativas aos descontos
        condicionados e incondicionados
    :ivar vDedRed: Grupo de informações relativas ao valores para
        dedução/redução do valor da base de cálculo (valor do serviço)
    :ivar trib: Grupo de informações relacionados aos tributos
        relacionados ao serviço prestado
    """
    class Meta:
        name = "TCInfoValores"

    vServPrest: Optional[TcvservPrest] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    vDescCondIncond: Optional[TcvdescCondIncond] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    vDedRed: Optional[TcinfoDedRed] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    trib: Optional[TcinfoTributacao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )


@dataclass
class TcinfDps:
    """
    :ivar tpAmb: Identificação do Ambiente: 1 - Produção; 2 -
        Homologação
    :ivar dhEmi: Data e hora da emissão do DPS. Data e hora no formato
        UTC (Universal Coordinated Time): AAAA-MM-DDThh:mm:ssTZD
    :ivar verAplic: Versão do aplicativo que gerou o DPS
    :ivar serie: Número do equipamento emissor do DPS ou série do DPS
    :ivar nDPS: Número do DPS
    :ivar dCompet: Data em que se iniciou a prestação do serviço: Dia,
        mês e ano (AAAAMMDD)
    :ivar tpEmit: Emitente da DPS: 1 - Prestador; 2 - Tomador; 3 -
        Intermediário
    :ivar cLocEmi: O código de município utilizado pelo Sistema Nacional
        NFS-e é o código definido para cada município pertencente ao
        ""Anexo V – Tabela de Código de Municípios do IBGE"", que consta
        ao final do Manual de Orientação ao Contribuinte do ISSQN para a
        Sefin Nacional NFS-e. O município emissor da NFS-e é aquele
        município em que o emitente da DPS está cadastrado e autorizado
        a "emitir uma NFS-e", ou seja, emitir uma DPS para que o sistema
        nacional valide as informações nela prestadas e gere a NFS-e
        correspondente para o emitente. Para que o sistema nacional
        emita a NFS-e o município emissor deve ser conveniado e estar
        ativo no sistema nacional. Além disso o convênio do município
        deve permitir que os contribuintes do município utilize os
        emissores públicos do Sistema Nacional NFS-e
    :ivar subst: Dados da NFS-e a ser substituída
    :ivar prest: Grupo de informações do DPS relativas ao Prestador de
        Serviços
    :ivar toma: Grupo de informações do DPS relativas ao Tomador de
        Serviços
    :ivar interm: Grupo de informações do DPS relativas ao Intermediário
        de Serviços
    :ivar serv: Grupo de informações do DPS relativas ao Serviço
        Prestado
    :ivar valores: Grupo de informações relativas à valores do serviço
        prestado
    :ivar Id:
    """
    class Meta:
        name = "TCInfDPS"

    tpAmb: Optional[TstipoAmbiente] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    dhEmi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
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
    serie: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 5,
            "white_space": "preserve",
        }
    )
    nDPS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 15,
            "white_space": "preserve",
            "pattern": r"[1-9]{1}[0-9]{0,14}",
        }
    )
    dCompet: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
        }
    )
    tpEmit: Optional[TsemitenteDps] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    cLocEmi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    subst: Optional[Tcsubstituicao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    prest: Optional[TcinfoPrestador] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    toma: Optional[TcinfoPessoa] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    interm: Optional[TcinfoPessoa] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
        }
    )
    serv: Optional[Tcserv] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    valores: Optional[TcinfoValores] = field(
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
            "max_length": 45,
            "white_space": "preserve",
            "pattern": r"DPS[0-9]{42}",
        }
    )


@dataclass
class Tcdps:
    class Meta:
        name = "TCDPS"

    infDPS: Optional[TcinfDps] = field(
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
class TcinfNfse:
    """
    :ivar xLocEmi: Descrição do código do IBGE do município emissor da
        NFS-e.
    :ivar xLocPrestacao: Descrição do local da prestação do serviço.
    :ivar nNFSe: Número sequencial por tipo de emitente da NFS-e. A
        Sefin Nacional NFS-e irá gerar o número da NFS-e de forma
        sequencial por emitente. Por se tratar de um ambiente altamente
        transacional, a Sefin Nacional NFS-e não irá reutilizar números
        inutilizados durante a geração da NFS-e.
    :ivar cLocIncid: O código de município utilizado pelo Sistema
        Nacional NFS-e é o código definido para cada município
        pertencente ao ""Anexo V – Tabela de Código de Municípios do
        IBGE"", que consta ao final do Manual de Orientação ao
        Contribuinte do ISSQN para a Sefin Nacional NFS-e. O município
        de incidência do ISSQN é determinado automaticamente pelo
        sistema, conforme regras do aspecto espacial da lei complementar
        federal (LC 116/03) que são válidas para todos  os municípios.
        http://www.planalto.gov.br/ccivil_03/Leis/LCP/Lcp116.htm
    :ivar xLocIncid: A descrição do código de município utilizado pelo
        Sistema Nacional NFS-e é o nome de cada município pertencente ao
        "Anexo V – Tabela de Código de Municípios do IBGE", que consta
        ao final do Manual de Orientação ao Contribuinte do ISSQN para a
        Sefin Nacional NFS-e.
    :ivar xTribNac: Descrição do código de tributação nacional do ISSQN.
    :ivar xTribMun: Descrição do código de tributação municipal do
        ISSQN.
    :ivar xNBS: Descrição do código da NBS.
    :ivar verAplic: Versão do aplicativo que gerou a NFS-e
    :ivar ambGer: Ambiente gerador da NFS-e
    :ivar tpEmis: Processo de Emissão da DPS: 1 - Emissão com aplicativo
        do contribuinte (via Web Service); 2 - Emissão com aplicativo
        disponibilizado pelo fisco (Web); 3 - Emissão com aplicativo
        disponibilizado pelo fisco (App);
    :ivar procEmi: Processo de Emissão da DPS: 1 - Emissão com
        aplicativo do contribuinte (via Web Service); 2 - Emissão com
        aplicativo disponibilizado pelo fisco (Web); 3 - Emissão com
        aplicativo disponibilizado pelo fisco (App);
    :ivar cStat: Código do Status da mensagem
    :ivar dhProc: Data/Hora da validação da DPS e geração da NFS-e. Data
        e hora no formato UTC (Universal Coordinated Time):AAAA-MM-
        DDThh:mm:ssTZD
    :ivar nDFSe: Número sequencial do documento gerado por ambiente
        gerador de DFSe do múnicípio.
    :ivar emit: Grupo de informações da DPS relativas ao emitente da
        NFS-e
    :ivar valores: Grupo de valores referentes ao Serviço Prestado
    :ivar DPS: Grupo de informações da DPS relativas ao serviço prestado
    :ivar Id:
    """
    class Meta:
        name = "TCInfNFSe"

    xLocEmi: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xLocPrestacao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nNFSe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 13,
            "white_space": "preserve",
            "pattern": r"[1-9]{1}[0-9]{0,12}",
        }
    )
    cLocIncid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    xLocIncid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xTribNac: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "min_length": 1,
            "max_length": 600,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xTribMun: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 600,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    xNBS: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "min_length": 1,
            "max_length": 600,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
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
    ambGer: Optional[TsambGeradorNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    tpEmis: Optional[TstipoEmissao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    procEmi: Optional[TsprocEmissao] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    cStat: Optional[Tstat] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
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
    nDFSe: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
            "max_length": 13,
            "white_space": "preserve",
            "pattern": r"[1-9]{1}[0-9]{0,12}",
        }
    )
    emit: Optional[Tcemitente] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    valores: Optional[TcvaloresNfse] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.sped.fazenda.gov.br/nfse",
            "required": True,
        }
    )
    DPS: Optional[Tcdps] = field(
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
            "max_length": 53,
            "white_space": "preserve",
            "pattern": r"NFS[0-9]{50}",
        }
    )


@dataclass
class Tcnfse:
    class Meta:
        name = "TCNFSe"

    infNFSe: Optional[TcinfNfse] = field(
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
