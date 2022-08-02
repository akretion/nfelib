from dataclasses import dataclass, field
from typing import List, Optional
from nfelib.bindings.nfe_dist_dfe.v1_0.tipos_dist_dfe_v1_01 import (
    Tamb,
    TverDistDfe,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class RetDistDfeInt:
    """
    Schema do resultado do pedido de distribuição de DF-e de interesse.

    :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
        Homologação
    :ivar ver_aplic: Versão do Web Service NFeDistribuicaoDFe
    :ivar c_stat: Código do status de processamento da requisição
    :ivar x_motivo: Descrição literal do status do processamento da
        requisição
    :ivar dh_resp: Data e Hora de processamento da requisição no formato
        AAAA-MM-DDTHH:MM:SSTZD
    :ivar ult_nsu: Último NSU pesquisado no Ambiente Nacional. Se for o
        caso, o solicitante pode continuar a consulta a partir deste NSU
        para obter novos resultados.
    :ivar max_nsu: Maior NSU existente no Ambiente Nacional para o
        CNPJ/CPF informado
    :ivar lote_dist_dfe_int: Conjunto de informações resumidas e
        documentos fiscais eletrônicos de interesse da pessoa ou
        empresa.
    :ivar versao:
    """
    class Meta:
        name = "retDistDFeInt"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    tp_amb: Optional[Tamb] = field(
        default=None,
        metadata={
            "name": "tpAmb",
            "type": "Element",
            "required": True,
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
    c_stat: Optional[str] = field(
        default=None,
        metadata={
            "name": "cStat",
            "type": "Element",
            "required": True,
            "max_length": 3,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    x_motivo: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMotivo",
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    dh_resp: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhResp",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
    ult_nsu: Optional[str] = field(
        default=None,
        metadata={
            "name": "ultNSU",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{15}",
        }
    )
    max_nsu: Optional[str] = field(
        default=None,
        metadata={
            "name": "maxNSU",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{15}",
        }
    )
    lote_dist_dfe_int: Optional["RetDistDfeInt.LoteDistDfeInt"] = field(
        default=None,
        metadata={
            "name": "loteDistDFeInt",
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
        :ivar doc_zip: Informação resumida ou documento fiscal
            eletrônico de interesse da pessoa ou empresa. O conteúdo
            desta tag estará compactado no padrão gZip. O tipo do campo
            é base64Binary.
        """
        doc_zip: List["RetDistDfeInt.LoteDistDfeInt.DocZip"] = field(
            default_factory=list,
            metadata={
                "name": "docZip",
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 50,
            }
        )

        @dataclass
        class DocZip:
            """
            :ivar value:
            :ivar nsu: NSU do documento fiscal
            :ivar schema: Identificação do Schema XML que será utilizado
                para validar o XML existente no conteúdo da tag docZip.
                Vai identificar o tipo do documento e sua versão.
                Exemplos: resNFe_v1.00.xsd, procNFe_v3.10.xsd,
                resEvento_1.00.xsd, procEventoNFe_v1.00.xsd
            """
            value: Optional[bytes] = field(
                default=None,
                metadata={
                    "required": True,
                    "format": "base64",
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
            schema: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
