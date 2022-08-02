from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bindings.mdfe.v3_0.tipos_geral_mdfe_v3_00 import Tamb

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


class TdistDfeIndCompRet(Enum):
    VALUE_0 = 0
    VALUE_1 = 1


class TdistDfeIndDfe(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_8 = 8
    VALUE_9 = 9


@dataclass
class TloteDistDfe:
    """
    Schema XML de validação da área de dados descompactada.
    """
    class Meta:
        name = "TLoteDistDFe"

    proc: List["TloteDistDfe.Proc"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "min_occurs": 1,
            "max_occurs": 50,
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
    class Proc:
        """
        :ivar any_element: informação do proc
        :ivar schema: Identificação do Schema XML de validação do proc,
            Ex. procMDFe_v1.00.xsd.
        :ivar nsu: número sequencial único do Ambiente Autorizador
        :ivar ip_transmissor:
        """
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            }
        )
        schema: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        nsu: Optional[str] = field(
            default=None,
            metadata={
                "name": "NSU",
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9]{15}",
            }
        )
        ip_transmissor: Optional[str] = field(
            default=None,
            metadata={
                "name": "ipTransmissor",
                "type": "Attribute",
                "white_space": "preserve",
                "pattern": r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])",
            }
        )


@dataclass
class TdistDfe:
    """
    Schema XML de validação da área de dados da mensagem da solicitação de
    distribuição de DF-e.

    :ivar tp_amb: Identificação do Ambiente:  1 - Produção  2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que solicitou a distribuição
        de DF-e
    :ivar ind_dfe: Indicador de DF-e solicitados: 0 - DF-e autorizados
        pela UF; 1 - DF-e com carregamento na UF; 2 – DF-e com
        descarregamento na UF; 3 – DF-e com percurso pela UF; 8 – DF-e
        carregados  (1), descarregados (2)  e que tiveram percurso na UF
        (3); 9 - Todos DF-e que fazem referência a UF.
    :ivar ind_comp_ret: Indicador de Compactação da Mensagem de retorno:
        0 - sem compactação;  1 - compactação padrão gZip
    :ivar ult_nsu: último NSU recebido, caso seja informado com zero, o
        Ambiente Autorizador tentará localizar o primeiro DF-e
        existente.
    :ivar versao:
    """
    class Meta:
        name = "TDistDFe"

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
    ind_dfe: Optional[TdistDfeIndDfe] = field(
        default=None,
        metadata={
            "name": "indDFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    ind_comp_ret: Optional[TdistDfeIndCompRet] = field(
        default=None,
        metadata={
            "name": "indCompRet",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    ult_nsu: Optional[str] = field(
        default=None,
        metadata={
            "name": "ultNSU",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
            "pattern": r"[0-9]{15}",
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
class TretDistDfe:
    """
    Schema XML de validação do lote de retorno de documentos ficais
    eletronicos.

    :ivar tp_amb: Identificação do Ambiente:  1 - Produção  2 -
        Homologação
    :ivar ver_aplic: Versão do Aplicativo que atendeu a pedido de
        distribuição de DF-e
    :ivar c_stat: código do status de resultado da pesquisa
    :ivar x_motivo: descrição do resultado do pesquisa
    :ivar ult_nsu: último NSU
    :ivar lote_dist_mdfe_comp:
    :ivar lote_dist_mdfe:
    :ivar versao:
    """
    class Meta:
        name = "TRetDistDFe"

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
    ult_nsu: Optional[str] = field(
        default=None,
        metadata={
            "name": "ultNSU",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "pattern": r"[0-9]{15}",
        }
    )
    lote_dist_mdfe_comp: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "loteDistMDFeComp",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "format": "base64",
        }
    )
    lote_dist_mdfe: Optional[TloteDistDfe] = field(
        default=None,
        metadata={
            "name": "loteDistMDFe",
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
