from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from nfelib.bindings.cte.v3_0.tipos_geral_cte_v3_00 import Tuf

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class FerrovTpTraf(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TrafMutFerrEmi(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


class TrafMutRespFat(Enum):
    VALUE_1 = "1"
    VALUE_2 = "2"


@dataclass
class TenderFer:
    """
    Tipo Dados do Endereço.

    :ivar x_lgr: Logradouro
    :ivar nro: Número
    :ivar x_cpl: Complemento
    :ivar x_bairro: Bairro
    :ivar c_mun: Código do município Utilizar a tabela do IBGE Informar
        9999999 para operações com o exterior.
    :ivar x_mun: Nome do município Informar EXTERIOR para operações com
        o exterior.
    :ivar cep: CEP
    :ivar uf: Sigla da UF Informar EX para operações com o exterior.
    """
    class Meta:
        name = "TEnderFer"

    x_lgr: Optional[str] = field(
        default=None,
        metadata={
            "name": "xLgr",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 2,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    nro: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_cpl: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCpl",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_bairro: Optional[str] = field(
        default=None,
        metadata={
            "name": "xBairro",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    c_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "cMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    x_mun: Optional[str] = field(
        default=None,
        metadata={
            "name": "xMun",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    cep: Optional[str] = field(
        default=None,
        metadata={
            "name": "CEP",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )
    uf: Optional[Tuf] = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://www.portalfiscal.inf.br/cte",
            "required": True,
        }
    )


@dataclass
class Ferrov:
    """
    Informações do modal Ferroviário.

    :ivar tp_traf: Tipo de Tráfego Preencher com: 0-Próprio; 1-Mútuo;
        2-Rodoferroviário; 3-Rodoviário.
    :ivar traf_mut: Detalhamento de informações para o tráfego mútuo
    :ivar fluxo: Fluxo Ferroviário Trata-se de um número identificador
        do contrato firmado com o cliente
    """
    class Meta:
        name = "ferrov"
        namespace = "http://www.portalfiscal.inf.br/cte"

    tp_traf: Optional[FerrovTpTraf] = field(
        default=None,
        metadata={
            "name": "tpTraf",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    traf_mut: Optional["Ferrov.TrafMut"] = field(
        default=None,
        metadata={
            "name": "trafMut",
            "type": "Element",
        }
    )
    fluxo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "min_length": 1,
            "max_length": 10,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )

    @dataclass
    class TrafMut:
        """
        :ivar resp_fat: Responsável pelo Faturamento Preencher com:
            1-Ferrovia de origem; 2-Ferrovia de destino
        :ivar ferr_emi: Ferrovia Emitente do CTe Preencher com:
            1-Ferrovia de origem; 2-Ferrovia de destino
        :ivar v_frete: Valor do Frete do Tráfego Mútuo
        :ivar ch_cte_ferro_origem: Chave de acesso do CT-e emitido pelo
            ferrovia de origem
        :ivar ferro_env: Informações das Ferrovias Envolvidas
        """
        resp_fat: Optional[TrafMutRespFat] = field(
            default=None,
            metadata={
                "name": "respFat",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
            }
        )
        ferr_emi: Optional[TrafMutFerrEmi] = field(
            default=None,
            metadata={
                "name": "ferrEmi",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
            }
        )
        v_frete: Optional[str] = field(
            default=None,
            metadata={
                "name": "vFrete",
                "type": "Element",
                "required": True,
                "white_space": "preserve",
                "pattern": r"0|0\.[0-9]{2}|[1-9]{1}[0-9]{0,12}(\.[0-9]{2})?",
            }
        )
        ch_cte_ferro_origem: Optional[str] = field(
            default=None,
            metadata={
                "name": "chCTeFerroOrigem",
                "type": "Element",
                "max_length": 44,
                "white_space": "preserve",
                "pattern": r"[0-9]{44}",
            }
        )
        ferro_env: List["Ferrov.TrafMut.FerroEnv"] = field(
            default_factory=list,
            metadata={
                "name": "ferroEnv",
                "type": "Element",
            }
        )

        @dataclass
        class FerroEnv:
            """
            :ivar cnpj: Número do CNPJ Informar o CNPJ da Ferrovia
                Envolvida. Caso a Ferrovia envolvida não seja inscrita
                no CNPJ o campo deverá preenchido com zeros. Informar os
                zeros não significativos.
            :ivar c_int: Código interno da Ferrovia envolvida Uso da
                transportadora
            :ivar ie: Inscrição Estadual
            :ivar x_nome: Razão Social ou Nome
            :ivar ender_ferro: Dados do endereço da ferrovia envolvida
            """
            cnpj: Optional[str] = field(
                default=None,
                metadata={
                    "name": "CNPJ",
                    "type": "Element",
                    "required": True,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{14}",
                }
            )
            c_int: Optional[str] = field(
                default=None,
                metadata={
                    "name": "cInt",
                    "type": "Element",
                    "min_length": 1,
                    "max_length": 10,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IE",
                    "type": "Element",
                    "max_length": 14,
                    "white_space": "preserve",
                    "pattern": r"[0-9]{2,14}",
                }
            )
            x_nome: Optional[str] = field(
                default=None,
                metadata={
                    "name": "xNome",
                    "type": "Element",
                    "required": True,
                    "min_length": 2,
                    "max_length": 60,
                    "white_space": "preserve",
                    "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
                }
            )
            ender_ferro: Optional[TenderFer] = field(
                default=None,
                metadata={
                    "name": "enderFerro",
                    "type": "Element",
                    "required": True,
                }
            )
