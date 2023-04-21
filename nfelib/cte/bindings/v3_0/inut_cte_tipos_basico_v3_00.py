from dataclasses import dataclass, field
from typing import Optional
from nfelib.cte.bindings.v3_0.tipos_geral_cte_v3_00 import (
    Tamb,
    TcodUfIbge,
    TmodCtCargaOs,
)
from nfelib.cte.bindings.v3_0.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class TinutCte:
    """
    Tipo Pedido de Inutilização de Numeração do Conhecimento de Transporte
    eletrônico.

    :ivar infInut: Dados do Pedido de Inutilização de Numeração do
        Conhecimento de Transporte eletrônico
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TInutCTe"

    infInut: Optional["TinutCte.InfInut"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "pattern": r"3\.00",
        }
    )

    @dataclass
    class InfInut:
        """
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar xServ: Serviço Solicitado
        :ivar cUF: Código da UF solicitada
        :ivar ano: Ano de inutilização da numeração
        :ivar CNPJ: CNPJ do emitente
        :ivar mod: Modelo da CT-e (57 ou 67)
        :ivar serie: Série da CT-e
        :ivar nCTIni: Número da CT-e inicial
        :ivar nCTFin: Número da CT-e final
        :ivar xJust: Justificativa do pedido de inutilização
        :ivar Id:
        """
        tpAmb: Optional[Tamb] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        xServ: str = field(
            init=False,
            default="INUTILIZAR",
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        cUF: Optional[TcodUfIbge] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        ano: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "pattern": r"[0-9]{1,2}",
            }
        )
        CNPJ: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{14}",
            }
        )
        mod: Optional[TmodCtCargaOs] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        serie: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,2}",
            }
        )
        nCTIni: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        nCTFin: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        xJust: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 15,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        Id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"ID[0-9]{39}",
            }
        )


@dataclass
class TretInutCte:
    """
    Tipo retorno do Pedido de Inutilização de Numeração do Conhecimento de
    Transporte eletrônico.

    :ivar infInut: Dados do Retorno do Pedido de Inutilização de
        Numeração do Conhecimento de Transporte eletrônico
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TRetInutCTe"

    infInut: Optional["TretInutCte.InfInut"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
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
            "pattern": r"3\.00",
        }
    )

    @dataclass
    class InfInut:
        """
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar verAplic: Versão do Aplicativo que processou a CT-e
        :ivar cStat: Código do status da mensagem enviada.
        :ivar xMotivo: Descrição literal do status do serviço
            solicitado.
        :ivar cUF: Código da UF solicitada
        :ivar ano: Ano de inutilização da numeração
        :ivar CNPJ: CNPJ do emitente
        :ivar mod: Modelo da CT-e (57 ou 67)
        :ivar serie: Série da CT-e
        :ivar nCTIni: Número da CT-e inicial
        :ivar nCTFin: Número da CT-e final
        :ivar dhRecbto: Data e hora de recebimento, no formato AAAA-MM-
            DDTHH:MM:SS TZD. Deve ser preenchida com data e hora da
            gravação no Banco em caso de Confirmação. Em caso de
            Rejeição, com data e hora do recebimento do Pedido de
            Inutilização.
        :ivar nProt: Número do Protocolo de Status do CT-e. 1 posição (1
            – Secretaria de Fazenda Estadual , 3 - SEFAZ Virtual RS, 5 -
            SEFAZ Virtual SP); 2 - código da UF - 2 posições ano; 10
            seqüencial no ano.
        :ivar Id:
        """
        tpAmb: Optional[Tamb] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        verAplic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{3}",
            }
        )
        xMotivo: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "collapse",
            }
        )
        cUF: Optional[TcodUfIbge] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        ano: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "pattern": r"[0-9]{1,2}",
            }
        )
        CNPJ: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[0-9]{14}",
            }
        )
        mod: Optional[TmodCtCargaOs] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
            }
        )
        serie: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,2}",
            }
        )
        nCTIni: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        nCTFin: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        dhRecbto: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        nProt: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        Id: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            }
        )


@dataclass
class TprocInutCte:
    """
    Tipo Pedido de inutilzação de númeração de CT-e processado.

    :ivar inutCTe:
    :ivar retInutCTe:
    :ivar versao:
    :ivar ipTransmissor: IP do transmissor do documento fiscal para o
        ambiente autorizador
    :ivar nPortaCon: Porta de origem utilizada na conexão (De 0 a 65535)
    :ivar dhConexao: Data e Hora da Conexão de Origem
    """
    class Meta:
        name = "TProcInutCTe"

    inutCTe: Optional[TinutCte] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    retInutCTe: Optional[TretInutCte] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
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
    ipTransmissor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])",
        }
    )
    nPortaCon: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9]{1,5}",
        }
    )
    dhConexao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
