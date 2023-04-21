from dataclasses import dataclass, field
from typing import List, Optional
from nfelib.nfe_dist_dfe.bindings.v1_0.tipos_dist_dfe_v1_01 import (
    Tamb,
    TverDistDfe,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetDistDfeInt:
    """
    Schema do resultado do pedido de distribuição de DF-e de interesse.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar verAplic: Versão do Web Service NFeDistribuicaoDFe
    :ivar cStat: Código do status de processamento da requisição
    :ivar xMotivo: Descrição literal do status do processamento da
        requisição
    :ivar dhResp: Data e Hora de processamento da requisição no formato
        AAAA-MM-DDTHH:MM:SSTZD
    :ivar ultNSU: Último NSU pesquisado no Ambiente Nacional. Se for o
        caso, o solicitante pode continuar a consulta a partir deste NSU
        para obter novos resultados.
    :ivar maxNSU: Maior NSU existente no Ambiente Nacional para o
        CNPJ/CPF informado
    :ivar loteDistDFeInt: Conjunto de informações resumidas e documentos
        fiscais eletrônicos de interesse da pessoa ou empresa.
    :ivar versao:
    """
    class Meta:
        name = "retDistDFeInt"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
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
            "required": True,
            "max_length": 3,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    dhResp: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    ultNSU: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{15}",
        }
    )
    maxNSU: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{15}",
        }
    )
    loteDistDFeInt: Optional["RetDistDfeInt.LoteDistDfeInt"] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    versao: Optional[TverDistDfe] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass
    class LoteDistDfeInt:
        """
        :ivar docZip: Informação resumida ou documento fiscal eletrônico
            de interesse da pessoa ou empresa. O conteúdo desta tag
            estará compactado no padrão gZip. O tipo do campo é
            base64Binary.
        """
        docZip: List["RetDistDfeInt.LoteDistDfeInt.DocZip"] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )

        @dataclass
        class DocZip:
            """
            :ivar value:
            :ivar NSU: NSU do documento fiscal
            :ivar schema_value: Identificação do Schema XML que será
                utilizado para validar o XML existente no conteúdo da
                tag docZip. Vai identificar o tipo do documento e sua
                versão. Exemplos: resNFe_v1.00.xsd, procNFe_v3.10.xsd,
                resEvento_1.00.xsd, procEventoNFe_v1.00.xsd
            """
            value: Optional[bytes] = field(
                default=None,
                metadata={
                    "required": True,
                    "format": "base64",
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
            schema_value: Optional[str] = field(
                default=None,
                metadata={
                    "name": "schema",
                    "type": "Attribute",
                    "required": True,
                }
            )
