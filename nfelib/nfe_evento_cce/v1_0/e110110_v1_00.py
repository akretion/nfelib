from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from nfelib.nfe_evento_cce.v1_0.leiaute_cce_v1_00 import (
    DetEventoDescEvento1,
    DetEventoVersao1,
    DetEventoXCondUso1,
)

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


class DetEventoDescEvento2(Enum):
    CARTA_DE_CORRE_O = "Carta de Correção"
    CARTA_DE_CORRECAO = "Carta de Correcao"


class DetEventoVersao2(Enum):
    VALUE_1_00 = "1.00"


class DetEventoXCondUso2(Enum):
    A_CARTA_DE_CORRE_O_DISCIPLINADA_PELO_1_A_DO_ART_7_DO_CONV_NIO_S_N_DE_15_DE_DEZEMBRO_DE_1970_E_PODE_SER_UTILIZADA_PARA_REGULARIZA_O_DE_ERRO_OCORRIDO_NA_EMISS_O_DE_DOCUMENTO_FISCAL_DESDE_QUE_O_ERRO_N_O_ESTEJA_RELACIONADO_COM_I_AS_VARI_VEIS_QUE_DETERMINAM_O_VALOR_DO_IMPOSTO_TAIS_COMO_BASE_DE_C_LCULO_AL_QUOTA_DIFEREN_A_DE_PRE_O_QUANTIDADE_VALOR_DA_OPERA_O_OU_DA_PRESTA_O_II_A_CORRE_O_DE_DADOS_CADASTRAIS_QUE_IMPLIQUE_MUDAN_A_DO_REMETENTE_OU_DO_DESTINAT_RIO_III_A_DATA_DE_EMISS_O_OU_DE_SA_DA = "A Carta de Correção é disciplinada pelo § 1º-A do art. 7º do Convênio S/N, de 15 de dezembro de 1970 e pode ser utilizada para regularização de erro ocorrido na emissão de documento fiscal, desde que o erro não esteja relacionado com: I - as variáveis que determinam o valor do imposto tais como: base de cálculo, alíquota, diferença de preço, quantidade, valor da operação ou da prestação; II - a correção de dados cadastrais que implique mudança do remetente ou do destinatário; III - a data de emissão ou de saída."
    A_CARTA_DE_CORRECAO_E_DISCIPLINADA_PELO_PARAGRAFO_1O_A_DO_ART_7O_DO_CONVENIO_S_N_DE_15_DE_DEZEMBRO_DE_1970_E_PODE_SER_UTILIZADA_PARA_REGULARIZACAO_DE_ERRO_OCORRIDO_NA_EMISSAO_DE_DOCUMENTO_FISCAL_DESDE_QUE_O_ERRO_NAO_ESTEJA_RELACIONADO_COM_I_AS_VARIAVEIS_QUE_DETERMINAM_O_VALOR_DO_IMPOSTO_TAIS_COMO_BASE_DE_CALCULO_ALIQUOTA_DIFERENCA_DE_PRECO_QUANTIDADE_VALOR_DA_OPERACAO_OU_DA_PRESTACAO_II_A_CORRECAO_DE_DADOS_CADASTRAIS_QUE_IMPLIQUE_MUDANCA_DO_REMETENTE_OU_DO_DESTINATARIO_III_A_DATA_DE_EMISSAO_OU_DE_SAIDA = "A Carta de Correcao e disciplinada pelo paragrafo 1o-A do art. 7o do Convenio S/N, de 15 de dezembro de 1970 e pode ser utilizada para regularizacao de erro ocorrido na emissao de documento fiscal, desde que o erro nao esteja relacionado com: I - as variaveis que determinam o valor do imposto tais como: base de calculo, aliquota, diferenca de preco, quantidade, valor da operacao ou da prestacao; II - a correcao de dados cadastrais que implique mudanca do remetente ou do destinatario; III - a data de emissao ou de saida."


@dataclass
class DetEvento:
    """
    Schema XML de validação do evento do carta de correção e1101110.

    :ivar desc_evento: Descrição do Evento - “Carta de Correção”
    :ivar x_correcao: Correção a ser considerada
    :ivar x_cond_uso: Texto Fixo com as condições de uso da Carta de
        Correção
    :ivar versao:
    """
    class Meta:
        name = "detEvento"
        namespace = "http://www.portalfiscal.inf.br/nfe"

    desc_evento: Optional[DetEventoDescEvento1] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    x_correcao: Optional[str] = field(
        default=None,
        metadata={
            "name": "xCorrecao",
            "type": "Element",
            "required": True,
            "min_length": 15,
            "max_length": 1000,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_cond_uso: Optional[DetEventoXCondUso1] = field(
        default=None,
        metadata={
            "name": "xCondUso",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    versao: Optional[DetEventoVersao1] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "white_space": "preserve",
        }
    )
