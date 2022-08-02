from dataclasses import dataclass, field
from typing import Optional
from nfelib.bindings.cte.v3_0.tipos_geral_cte_v3_00 import (
    Tamb,
    TcodUfIbge,
    TmodCtCargaOs,
)
from nfelib.bindings.cte.v3_0.xmldsig_core_schema_v1_01 import Signature

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class TinutCte:
    """
    Tipo Pedido de Inutilização de Numeração do Conhecimento de Transporte
    eletrônico.

    :ivar inf_inut: Dados do Pedido de Inutilização de Numeração do
        Conhecimento de Transporte eletrônico
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TInutCTe"

    inf_inut: Optional["TinutCte.InfInut"] = field(
        default=None,
        metadata={
            "name": "infInut",
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
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar x_serv: Serviço Solicitado
        :ivar c_uf: Código da UF solicitada
        :ivar ano: Ano de inutilização da numeração
        :ivar cnpj: CNPJ do emitente
        :ivar mod: Modelo da CT-e (57 ou 67)
        :ivar serie: Série da CT-e
        :ivar n_ctini: Número da CT-e inicial
        :ivar n_ctfin: Número da CT-e final
        :ivar x_just: Justificativa do pedido de inutilização
        :ivar id:
        """
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        x_serv: str = field(
            init=False,
            default="INUTILIZAR",
            metadata={
                "name": "xServ",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            }
        )
        c_uf: Optional[TcodUfIbge] = field(
            default=None,
            metadata={
                "name": "cUF",
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
        cnpj: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJ",
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
        n_ctini: Optional[str] = field(
            default=None,
            metadata={
                "name": "nCTIni",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        n_ctfin: Optional[str] = field(
            default=None,
            metadata={
                "name": "nCTFin",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "pattern": r"ID[0-9]{39}",
            }
        )


@dataclass
class TretInutCte:
    """
    Tipo retorno do Pedido de Inutilização de Numeração do Conhecimento de
    Transporte eletrônico.

    :ivar inf_inut: Dados do Retorno do Pedido de Inutilização de
        Numeração do Conhecimento de Transporte eletrônico
    :ivar signature:
    :ivar versao:
    """
    class Meta:
        name = "TRetInutCTe"

    inf_inut: Optional["TretInutCte.InfInut"] = field(
        default=None,
        metadata={
            "name": "infInut",
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
        :ivar tp_amb: Identificação do Ambiente: 1 - Produção 2 -
            Homologação
        :ivar ver_aplic: Versão do Aplicativo que processou a CT-e
        :ivar c_stat: Código do status da mensagem enviada.
        :ivar x_motivo: Descrição literal do status do serviço
            solicitado.
        :ivar c_uf: Código da UF solicitada
        :ivar ano: Ano de inutilização da numeração
        :ivar cnpj: CNPJ do emitente
        :ivar mod: Modelo da CT-e (57 ou 67)
        :ivar serie: Série da CT-e
        :ivar n_ctini: Número da CT-e inicial
        :ivar n_ctfin: Número da CT-e final
        :ivar dh_recbto: Data e hora de recebimento, no formato AAAA-MM-
            DDTHH:MM:SS TZD. Deve ser preenchida com data e hora da
            gravação no Banco em caso de Confirmação. Em caso de
            Rejeição, com data e hora do recebimento do Pedido de
            Inutilização.
        :ivar n_prot: Número do Protocolo de Status do CT-e. 1 posição
            (1 – Secretaria de Fazenda Estadual , 3 - SEFAZ Virtual RS,
            5 - SEFAZ Virtual SP); 2 - código da UF - 2 posições ano; 10
            seqüencial no ano.
        :ivar id:
        """
        tp_amb: Optional[Tamb] = field(
            default=None,
            metadata={
                "name": "tpAmb",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
            }
        )
        ver_aplic: Optional[str] = field(
            default=None,
            metadata={
                "name": "verAplic",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "required": True,
                "min_length": 1,
                "max_length": 255,
                "white_space": "collapse",
            }
        )
        c_uf: Optional[TcodUfIbge] = field(
            default=None,
            metadata={
                "name": "cUF",
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
        cnpj: Optional[str] = field(
            default=None,
            metadata={
                "name": "CNPJ",
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
        n_ctini: Optional[str] = field(
            default=None,
            metadata={
                "name": "nCTIni",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        n_ctfin: Optional[str] = field(
            default=None,
            metadata={
                "name": "nCTFin",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"[1-9]{1}[0-9]{0,8}",
            }
        )
        dh_recbto: Optional[str] = field(
            default=None,
            metadata={
                "name": "dhRecbto",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
                "white_space": "preserve",
                "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
            }
        )
        n_prot: Optional[str] = field(
            default=None,
            metadata={
                "name": "nProt",
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/cte",
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
class TprocInutCte:
    """
    Tipo Pedido de inutilzação de númeração de CT-e processado.

    :ivar inut_cte:
    :ivar ret_inut_cte:
    :ivar versao:
    :ivar ip_transmissor: IP do transmissor do documento fiscal para o
        ambiente autorizador
    :ivar n_porta_con: Porta de origem utilizada na conexão (De 0 a
        65535)
    :ivar dh_conexao: Data e Hora da Conexão de Origem
    """
    class Meta:
        name = "TProcInutCTe"

    inut_cte: Optional[TinutCte] = field(
        default=None,
        metadata={
            "name": "inutCTe",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )
    ret_inut_cte: Optional[TretInutCte] = field(
        default=None,
        metadata={
            "name": "retInutCTe",
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
    ip_transmissor: Optional[str] = field(
        default=None,
        metadata={
            "name": "ipTransmissor",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])",
        }
    )
    n_porta_con: Optional[str] = field(
        default=None,
        metadata={
            "name": "nPortaCon",
            "type": "Attribute",
            "pattern": r"[0-9]{1,5}",
        }
    )
    dh_conexao: Optional[str] = field(
        default=None,
        metadata={
            "name": "dhConexao",
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        }
    )
