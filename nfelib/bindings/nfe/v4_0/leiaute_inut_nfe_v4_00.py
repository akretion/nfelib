from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from nfelib.bindings.nfe.v4_0.tipos_basico_v4_00 import (
    Tamb,
    TcodUfIbge,
    Tmod,
)
from nfelib.bindings.nfe.v4_0.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class InfInutXServ(Enum):
    INUTILIZAR = "INUTILIZAR"


@dataclass
class TinutNfe:
    """
    Tipo Pedido de Inutilização de Numeração da Nota Fiscal Eletrônica.

    :ivar inf_inut: Dados do Pedido de Inutilização de Numeração da Nota
        Fiscal Eletrônica
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TInutNFe"

    inf_inut: Optional["TinutNfe.InfInut"] = field(
        default=None,
        metadata={
            "name": "infInut",
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
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar x_serv: Serviço Solicitado
        :ivar c_uf: Código da UF do emitente
        :ivar ano: Ano de inutilização da numeração
        :ivar cnpj: CNPJ do emitente
        :ivar mod: Modelo da NF-e (55, 65 etc.)
        :ivar serie: Série da NF-e
        :ivar n_nfini: Número da NF-e inicial
        :ivar n_nffin: Número da NF-e final
        :ivar x_just: Justificativa do pedido de inutilização
        :ivar id:
        """
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        x_serv: Optional[InfInutXServ] = field(
            default=None,
            metadata={
                "name": "xServ",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        c_uf: Optional[TcodUfIbge] = field(
            default=None,
            metadata={
                "name": "cUF",
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
        cnpj: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJ",
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
        n_nfini: Optional[str] = field(
            default=None,
            metadata={
                "name": "nNFIni",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        n_nffin: Optional[str] = field(
            default=None,
            metadata={
                "name": "nNFFin",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        x_just: Optional[str] = field(
            default=None,
            metadata={
                "name": "xJust",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 15,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
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

    :ivar inf_inut: Dados do Retorno do Pedido de Inutilização de
        Numeração da Nota Fiscal Eletrônica
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TRetInutNFe"

    inf_inut: Optional["TretInutNfe.InfInut"] = field(
        default=None,
        metadata={
            "name": "infInut",
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
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar ver_aplic: Versão do Aplicativo que processou a NF-e
        :ivar c_stat: Código do status da mensagem enviada.
        :ivar x_motivo: Descrição literal do status do serviço
            solicitado.
        :ivar c_uf: Código da UF que atendeu a solicitação
        :ivar ano: Ano de inutilização da numeração
        :ivar cnpj: CNPJ do emitente
        :ivar mod: Modelo da NF-e (55, etc.)
        :ivar serie: Série da NF-e
        :ivar n_nfini: Número da NF-e inicial
        :ivar n_nffin: Número da NF-e final
        :ivar dh_recbto: Data e hora de recebimento, no formato AAAA-MM-
            DDTHH:MM:SS. Deve ser preenchida com data e hora da gravação
            no Banco em caso de Confirmação. Em caso de Rejeição, com
            data e hora do recebimento do Pedido de Inutilização.
        :ivar n_prot: Número do Protocolo de Status da NF-e. 1 posição
            (1 – Secretaria de Fazenda Estadual 2 – Receita Federal); 2
            - código da UF - 2 posições ano; 10 seqüencial no ano.
        :ivar id:
        """
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
            }
        )
        ver_aplic: Optional[str] = field(
            default=None,
            metadata={
                "name": "verAplic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                "namespace": "http://www.portalfiscal.inf.br/nfe",
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
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        c_uf: Optional[TcodUfIbge] = field(
            default=None,
            metadata={
                "name": "cUF",
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
        cnpj: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJ",
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
        n_nfini: Optional[str] = field(
            default=None,
            metadata={
                "name": "nNFIni",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        n_nffin: Optional[str] = field(
            default=None,
            metadata={
                "name": "nNFFin",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        dh_recbto: Optional[str] = field(
            default=None,
            metadata={
                "name": "dhRecbto",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "required": True,
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        n_prot: Optional[str] = field(
            default=None,
            metadata={
                "name": "nProt",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe",
                "max_length": 15,
                "white_space": "preserve",
                "pattern": r"[0-9]{15}",
            }
        )
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "Id",
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

    inut_nfe: Optional[TinutNfe] = field(
        default=None,
        metadata={
            "name": "inutNFe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/nfe",
            "required": True,
        }
    )
    ret_inut_nfe: Optional[TretInutNfe] = field(
        default=None,
        metadata={
            "name": "retInutNFe",
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
