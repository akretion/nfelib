from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.mdfe.bindings.v3_0.tipos_geral_mdfe_v3_00 import Tamb

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
        :ivar schema_value: Identificação do Schema XML de validação do
            proc, Ex. procMDFe_v1.00.xsd.
        :ivar NSU: número sequencial único do Ambiente Autorizador
        :ivar ipTransmissor:
        """
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            }
        )
        schema_value: Optional[str] = field(
            default=None,
            metadata={
                "name": "schema",
                "type": "Attribute",
                "required": True,
            }
        )
        NSU: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[0-9]{15}",
            }
        )
        ipTransmissor: Optional[str] = field(
            default=None,
            metadata={
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

    :ivar tpAmb: Identificação do Ambiente:  1 - Produção  2 -
        Homologação
    :ivar verAplic: Versão do Aplicativo que solicitou a distribuição de
        DF-e
    :ivar indDFe: Indicador de DF-e solicitados: 0 - DF-e autorizados
        pela UF; 1 - DF-e com carregamento na UF; 2 – DF-e com
        descarregamento na UF; 3 – DF-e com percurso pela UF; 8 – DF-e
        carregados  (1), descarregados (2)  e que tiveram percurso na UF
        (3); 9 - Todos DF-e que fazem referência a UF.
    :ivar indCompRet: Indicador de Compactação da Mensagem de retorno:
        0 - sem compactação;  1 - compactação padrão gZip
    :ivar ultNSU: último NSU recebido, caso seja informado com zero, o
        Ambiente Autorizador tentará localizar o primeiro DF-e
        existente.
    :ivar versao:
    """
    class Meta:
        name = "TDistDFe"

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
    indDFe: Optional[TdistDfeIndDfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    indCompRet: Optional[TdistDfeIndCompRet] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "required": True,
        }
    )
    ultNSU: Optional[str] = field(
        default=None,
        metadata={
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

    :ivar tpAmb: Identificação do Ambiente:  1 - Produção  2 -
        Homologação
    :ivar verAplic: Versão do Aplicativo que atendeu a pedido de
        distribuição de DF-e
    :ivar cStat: código do status de resultado da pesquisa
    :ivar xMotivo: descrição do resultado do pesquisa
    :ivar ultNSU: último NSU
    :ivar loteDistMDFeComp:
    :ivar loteDistMDFe:
    :ivar versao:
    """
    class Meta:
        name = "TRetDistDFe"

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
    ultNSU: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "pattern": r"[0-9]{15}",
        }
    )
    loteDistMDFeComp: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/mdfe",
            "format": "base64",
        }
    )
    loteDistMDFe: Optional[TloteDistDfe] = field(
        default=None,
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
