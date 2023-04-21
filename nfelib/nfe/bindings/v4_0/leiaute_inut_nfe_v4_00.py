from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from nfelib.nfe.bindings.v4_0.tipos_basico_v4_00 import (
    Tamb,
    TcodUfIbge,
    Tmod,
)
from nfelib.nfe.bindings.v4_0.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class InfInutXServ(Enum):
    INUTILIZAR = "INUTILIZAR"


@dataclass
class TinutNfe:
    """
    Tipo Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica.

    :ivar infInut: Dados do Pedido de Inutilização de Numeração da Nota
        Fiscal Eletrônica
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TInutNFe"

    infInut: Optional["TinutNfe.InfInut"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "pattern": r"4\.00",
        }
    )

    @dataclass
    class InfInut:
        """
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar xServ: Serviço Solicitado
        :ivar cUF: Código da UF do emitente
        :ivar ano: Ano de inutilização da numeração
        :ivar CNPJ: CNPJ do emitente
        :ivar mod: Modelo da NF-e (55, 65 etc.)
        :ivar serie: Série da NF-e
        :ivar nNFIni: Número da NF-e inicial
        :ivar nNFFin: Número da NF-e final
        :ivar xJust: Justificativa do pedido de inutilização
        :ivar Id:
        """
        tpAmb: Optional[Tamb] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        xServ: Optional[InfInutXServ] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        cUF: Optional[TcodUfIbge] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        ano: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[0-9]{2}",
            }
        )
        CNPJ: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r"[0-9]{14}",
            }
        )
        mod: Optional[Tmod] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        serie: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,2}",
            }
        )
        nNFIni: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        nNFFin: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        xJust: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                "pattern": r"ID[0-9]{41}",
            }
        )


@dataclass
class TretInutNfe:
    """
    Tipo retorno do Pedido de Inutilização de Numeração da Nota Fiscal
    Eletrônica.

    :ivar infInut: Dados do Retorno do Pedido de Inutilização de
        Numeração da Nota Fiscal Eletrônica
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TRetInutNFe"

    infInut: Optional["TretInutNfe.InfInut"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
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
            "pattern": r"4\.00",
        }
    )

    @dataclass
    class InfInut:
        """
        :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar verAplic: Versão do Aplicativo que processou a NF-e
        :ivar cStat: Código do status da mensagem enviada.
        :ivar xMotivo: Descrição literal do status do serviço
            solicitado.
        :ivar cUF: Código da UF que atendeu a solicitação
        :ivar ano: Ano de inutilização da numeração
        :ivar CNPJ: CNPJ do emitente
        :ivar mod: Modelo da NF-e (55, etc.)
        :ivar serie: Série da NF-e
        :ivar nNFIni: Número da NF-e inicial
        :ivar nNFFin: Número da NF-e final
        :ivar dhRecbto: Data e hora de recebimento, no formato AAAA-MM-
            DDTHH:MM:SS. Deve ser preenchida com data e hora da gravação
            no Banco em caso de Confirmação. Em caso de Rejeição, com
            data e hora do recebimento do Pedido de Inutilização.
        :ivar nProt: Número do Protocolo de Status da NF-e. 1 posição (1
            – Secretaria de Fazenda Estadual 2 – Receita Federal); 2 -
            código da UF - 2 posições ano; 10 seqüencial no ano.
        :ivar Id:
        """
        tpAmb: Optional[Tamb] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        verAplic: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        cUF: Optional[TcodUfIbge] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        ano: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"[0-9]{2}",
            }
        )
        CNPJ: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r"[0-9]{14}",
            }
        )
        mod: Optional[Tmod] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
            }
        )
        serie: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"0|[1-9]{1}[0-9]{0,2}",
            }
        )
        nNFIni: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        nNFFin: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        dhRecbto: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        nProt: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 15,
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
class TprocInutNfe:
    """
    Tipo Pedido de inutilzação de númeração de  NF-e processado.
    """
    class Meta:
        name = "TProcInutNFe"

    inutNFe: Optional[TinutNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    retInutNFe: Optional[TretInutNfe] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"4\.00",
        }
    )
