"""This file was generated by xsdata, v24.11, on 2025-07-14 05:12:19

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""

from dataclasses import dataclass, field
from typing import Optional

from nfelib import CommonMixin
from nfelib.cte.bindings.v4_0.tipos_geral_cte_v4_00 import (
    Tamb,
    TcodUfIbge,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


@dataclass
class TconsStatServ(CommonMixin):
    """
    Tipo Pedido de Consulta do Status do Serviço CTe.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar cUF: Código da UF a ser verificado o status Utilizar a Tabela
        do IBGE.
    :ivar xServ: Serviço Solicitado
    :ivar versao:
    """

    class Meta:
        name = "TConsStatServ"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        },
    )
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        },
    )
    xServ: str = field(
        init=False,
        default="STATUS",
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"4\.00",
        },
    )


@dataclass
class TretConsStatServ(CommonMixin):
    """
    Tipo Resultado da Consulta do Status do Serviço CTe.

    :ivar tpAmb: Identificação do Ambiente: 1 - Produção 2 - Homologação
    :ivar verAplic: Versão do Aplicativo que processou o CT-e
    :ivar cStat: Código do status da mensagem enviada.
    :ivar xMotivo: Descrição literal do status do serviço solicitado.
    :ivar cUF: Código da UF responsável pelo serviço
    :ivar dhRecbto: AAAA-MM-DDTHH:MM:SS TZD
    :ivar tMed: Tempo médio de resposta do serviço (em segundos) dos
        últimos 5 minutos
    :ivar dhRetorno: AAAA-MM-DDTHH:MM:SSDeve ser preenchida com data e
        hora previstas para o retorno dos serviços prestados.
    :ivar xObs: Campo observação utilizado para incluir informações ao
        contribuinte
    :ivar versao:
    """

    class Meta:
        name = "TRetConsStatServ"

    tpAmb: Optional[Tamb] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        },
    )
    verAplic: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )
    cStat: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{3,4}",
        },
    )
    xMotivo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )
    cUF: Optional[TcodUfIbge] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        },
    )
    dhRecbto: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        },
    )
    tMed: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "pattern": r"[0-9]{1,4}",
        },
    )
    dhRetorno: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\d):[0-5]\d:[0-5]\d([\-,\+](0[0-9]|10|11):00|([\+](12):00))",
        },
    )
    xObs: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    versao: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"4\.00",
        },
    )
