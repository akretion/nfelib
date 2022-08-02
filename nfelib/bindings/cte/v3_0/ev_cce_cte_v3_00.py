from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class EvCceCteDescEvento(Enum):
    CARTA_DE_CORRE_O = "Carta de Correção"
    CARTA_DE_CORRECAO = "Carta de Correcao"


class EvCceCteXCondUso(Enum):
    A_CARTA_DE_CORRE_O_DISCIPLINADA_PELO_ART_58_B_DO_CONV_NIO_SINIEF_06_89_FICA_PERMITIDA_A_UTILIZA_O_DE_CARTA_DE_CORRE_O_PARA_REGULARIZA_O_DE_ERRO_OCORRIDO_NA_EMISS_O_DE_DOCUMENTOS_FISCAIS_RELATIVOS_PRESTA_O_DE_SERVI_O_DE_TRANSPORTE_DESDE_QUE_O_ERRO_N_O_ESTEJA_RELACIONADO_COM_I_AS_VARI_VEIS_QUE_DETERMINAM_O_VALOR_DO_IMPOSTO_TAIS_COMO_BASE_DE_C_LCULO_AL_QUOTA_DIFEREN_A_DE_PRE_O_QUANTIDADE_VALOR_DA_PRESTA_O_II_A_CORRE_O_DE_DADOS_CADASTRAIS_QUE_IMPLIQUE_MUDAN_A_DO_EMITENTE_TOMADOR_REMETENTE_OU_DO_DESTINAT_RIO_III_A_DATA_DE_EMISS_O_OU_DE_SA_DA = "A Carta de Correção é disciplinada pelo Art. 58-B do CONVÊNIO/SINIEF 06/89: Fica permitida a utilização de carta de correção, para regularização de erro ocorrido na emissão de documentos fiscais relativos à prestação de serviço de transporte, desde que o erro não esteja relacionado com: I - as variáveis que determinam o valor do imposto tais como: base de cálculo, alíquota, diferença de preço, quantidade, valor da prestação;II - a correção de dados cadastrais que implique mudança do emitente, tomador, remetente ou do destinatário;III - a data de emissão ou de saída."
    A_CARTA_DE_CORRECAO_E_DISCIPLINADA_PELO_ART_58_B_DO_CONVENIO_SINIEF_06_89_FICA_PERMITIDA_A_UTILIZACAO_DE_CARTA_DE_CORRECAO_PARA_REGULARIZACAO_DE_ERRO_OCORRIDO_NA_EMISSAO_DE_DOCUMENTOS_FISCAIS_RELATIVOS_A_PRESTACAO_DE_SERVICO_DE_TRANSPORTE_DESDE_QUE_O_ERRO_NAO_ESTEJA_RELACIONADO_COM_I_AS_VARIAVEIS_QUE_DETERMINAM_O_VALOR_DO_IMPOSTO_TAIS_COMO_BASE_DE_CALCULO_ALIQUOTA_DIFERENCA_DE_PRECO_QUANTIDADE_VALOR_DA_PRESTACAO_II_A_CORRECAO_DE_DADOS_CADASTRAIS_QUE_IMPLIQUE_MUDANCA_DO_EMITENTE_TOMADOR_REMETENTE_OU_DO_DESTINATARIO_III_A_DATA_DE_EMISSAO_OU_DE_SAIDA = "A Carta de Correcao e disciplinada pelo Art. 58-B do CONVENIO/SINIEF 06/89: Fica permitida a utilizacao de carta de correcao, para regularizacao de erro ocorrido na emissao de documentos fiscais relativos a prestacao de servico de transporte, desde que o erro nao esteja relacionado com: I - as variaveis que determinam o valor do imposto tais como: base de calculo, aliquota, diferenca de preco, quantidade, valor da prestacao;II - a correcao de dados cadastrais que implique mudanca do emitente, tomador, remetente ou do destinatario;III - a data de emissao ou de saida."


@dataclass
class EvCceCte:
    """
    Schema XML de validação do evento carta de correção 110110.

    :ivar desc_evento: Descrição do Evento - “Carta de Correção”
    :ivar inf_correcao: Grupo de Informações de Correção
    :ivar x_cond_uso: Condições de uso da Carta de Correção, informar a
        literal :Condições de uso da Carta de Correção, informar a
        literal: “A Carta de Correção é disciplinada pelo Art. 58-B do
        CONVÊNIO/SINIEF 06/89: Fica permitida a utilização de carta de
        correção, para regularização de erro ocorrido na emissão de
        documentos fiscais relativos à prestação de serviço de
        transporte, desde que o erro não esteja relacionado com: I - as
        variáveis que determinam o valor do imposto tais como: base de
        cálculo, alíquota, diferença de preço, quantidade, valor da
        prestação;II - a correção de dados cadastrais que implique
        mudança do emitente, tomador, remetente ou do destinatário;III -
        a data de emissão ou de saída.” (texto com acentuação)  ou “A
        Carta de Correcao e disciplinada pelo Art. 58-B do
        CONVENIO/SINIEF 06/89: Fica permitida a utilizacao de carta de
        correcao, para regularizacao de erro ocorrido na emissao de
        documentos fiscais relativos a prestacao de servico de
        transporte, desde que o erro nao esteja relacionado com: I - as
        variaveis que determinam o valor do imposto tais como: base de
        calculo, aliquota, diferenca de preco, quantidade, valor da
        prestacao;II - a correcao de dados cadastrais que implique
        mudança do emitente, tomador, remetente ou do destinatario;III -
        a data de emissao ou de saida.” (texto sem acentuação)
    """
    class Meta:
        name = "evCCeCTe"
        namespace = "http://www.portalfiscal.inf.br/cte"

    desc_evento: Optional[EvCceCteDescEvento] = field(
        default=None,
        metadata={
            "name": "descEvento",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    inf_correcao: List["EvCceCte.InfCorrecao"] = field(
        default_factory=list,
        metadata={
            "name": "infCorrecao",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    x_cond_uso: Optional[EvCceCteXCondUso] = field(
        default=None,
        metadata={
            "name": "xCondUso",
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )

    @dataclass
    class InfCorrecao:
        """
        :ivar grupo_alterado: Indicar o grupo de informações que
            pertence o campoAlterado. Ex: ide
        :ivar campo_alterado: Nome do campo modificado do CT-e Original.
        :ivar valor_alterado: Valor correspondente à alteração.
        :ivar nro_item_alterado: Preencher com o indice do item alterado
            caso a alteração ocorra em uma lista. OBS: O indice inicia
            sempre  em 1
        """
        grupo_alterado: Optional[str] = field(
            default=None,
            metadata={
                "name": "grupoAlterado",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
            }
        )
        campo_alterado: Optional[str] = field(
            default=None,
            metadata={
                "name": "campoAlterado",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 20,
                "white_space": "preserve",
            }
        )
        valor_alterado: Optional[str] = field(
            default=None,
            metadata={
                "name": "valorAlterado",
                "type": "Element",
                "required": True,
                "min_length": 1,
                "max_length": 500,
                "white_space": "preserve",
            }
        )
        nro_item_alterado: Optional[str] = field(
            default=None,
            metadata={
                "name": "nroItemAlterado",
                "type": "Element",
                "white_space": "preserve",
                "pattern": r"[1-9][0-9]|0?[1-9]",
            }
        )
