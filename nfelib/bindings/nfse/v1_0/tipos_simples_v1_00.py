from enum import Enum

__NAMESPACE__ = "http://www.sped.fazenda.gov.br/nfse"


class TcobjetoLocacao(Enum):
    """Tipo de objetos da locação, sublocação, arrendamento, direito de
    passagem ou permissão de uso:

    1 - Ferrovia;
    2 - Rodovia;
    3 - Postes;
    4 - Cabos;
    5 - Dutos;
    6 - Condutos de qualquer natureza;
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class TsambGeradorEvt(Enum):
    """Tipo Ambiente gerador do evento:

    1- Prefeitura;
    2- Sefin Nacional;
    3- Ambiente Nacional.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TsambGeradorNfse(Enum):
    """Tipo Ambiente Gerador de NFS-e:

    1 - Prefeitura;
    2 - Sistema Nacional da NFS-e;
    """
    VALUE_1 = "1"
    VALUE_2 = "2"


class TscategVeic(Enum):
    """Categorias de veículos para cobrança:

    00 - Categoria de Veículos (tipo não informado na nota de origem);
    01 - Automóvel, caminhonete e furgão;
    02 - Caminhão leve, ônibus, caminhão trator e furgão;
    03 - Automóvel e caminhonete com semireboque;
    04 - Caminhão, caminhão-trator, caminhão-trator com semi-reboque e ônibus;
    05 - Automóvel e caminhonete com reboque;
    06 - Caminhão com reboque e caminhãotrator com semi-reboque;
    07 - Caminhão com reboque e caminhãotrator com semi-reboque;
    08 - Caminhão com reboque e caminhãotrator com semi-reboque;
    09 - Motocicletas, motonetas e bicicletas motorizadas;
    10 - Veículo especial;
    11 - Veículo Isento;
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"


class TscategoriaServico(Enum):
    """Categorias do serviço:

    1 - Locação;
    2 - Sublocação;
    3 - Arrendamento;
    4 - Direito de passagem;
    5 - Permissão de uso;
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


class TscodJustAnaliseFiscalCanc(Enum):
    """Código do motivo da solicitação de análise fiscal para cancelamento de
    NFS-e:

    1 - Erro na Emissão;
    2 - Serviço não Prestado;
    3 - Outros.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_9 = "9"


class TscodJustAnaliseFiscalCancDef(Enum):
    """Resposta da análise da solicitação do cancelamento extemporâneo de
    NFS-e:

    1 - Cancelamento Extemporâneo Deferido.
    """
    VALUE_1 = "1"


class TscodJustAnaliseFiscalCancIndef(Enum):
    """Resposta da análise da solicitação do cancelamento extemporâneo de
    NFS-e:

    1 - Cancelamento Extemporâneo Indeferido;
    2 - Cancelamento Extemporâneo Indeferido Sem Análise de Mérito.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"


class TscodJustCanc(Enum):
    """Código de justificativa de cancelamento:

    1 - Erro na Emissão;
    2 - Serviço não Prestado;
    9 - Outros;
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_9 = "9"


class TscodJustSubst(Enum):
    """Código de justificativa para substituição de NFS-e:

    01 - Desenquadramento de NFS-e do Simples Nacional;
    02 - Enquadramento de NFS-e no Simples Nacional;
    03 - Inclusão Retroativa de Imunidade/Isenção para NFS-e;
    04 - Exclusão Retroativa de Imunidade/Isenção para NFS-e;
    05 - Rejeição de NFS-e pelo tomador ou pelo intermediário se responsável pelo recolhimento do tributo;
    99 - Outros;
    """
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_99 = "99"


class TscodMotivoRejeicao(Enum):
    """Motivo da Rejeição da NFS-e:

    1 - NFS-e em duplicidade;
    2 - NFS-e já emitida pelo tomador;
    3 - Não ocorrência do fato gerador;
    4 - Erro quanto a responsabilidade tributária;
    5 - Erro quanto ao valor do serviço, valor das deduções ou serviço prestado ou data do fato gerador;
    9 - Outros;
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_9 = "9"


class TscodNaoNif(Enum):
    """Motivo para não informação do NIF:

    0 - Não informado na nota de origem;
    1 - Dispensado do NIF;
    2 - Não exigência do NIF;
    """
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"


class TscodigoEventoNfse(Enum):
    """
    Código de evento da NFS-e.
    """
    E101101 = "e101101"
    E105102 = "e105102"
    E105104 = "e105104"
    E105105 = "e105105"
    E305101 = "e305101"
    E907202 = "e907202"
    E967203 = "e967203"


class TsemitenteDps(Enum):
    """Emitente da DPS:

    1 - Prestador
    2 - Tomador
    3 - Intermediário
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TsenvMdic(Enum):
    """Compartilhar as informações da NFS-e gerada a partir desta DPS com a
    Secretaria de Comércio Exterior:

    0 - Não enviar para o MDIC;
    1 - Enviar para o MDIC;
    """
    VALUE_0 = "0"
    VALUE_1 = "1"


class TsideDedRed(Enum):
    """Identificação da Dedução/Redução:

    1 – Alimentação e bebidas/frigobar; 2 – Materiais; 3 – Produção
    externa; 4 – Reembolso de despesas; 5 – Repasse consorciado; 6 –
    Repasse plano de saúde; 7 – Serviços; 8 – Subempreitada de mão de
    obra; 99 – Outras deduções;
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"
    VALUE_99 = "99"


class TsmecAfcomExPrest(Enum):
    """Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo prestador
    do serviço:

    00 - Desconhecido (tipo não informado na nota de origem);
    01 - Nenhum;
    02 - ACC - Adiantamento sobre Contrato de Câmbio – Redução a Zero do IR e do IOF;
    03 - ACE – Adiantamento sobre Cambiais Entregues - Redução a Zero do IR e do IOF;
    04 - BNDES-Exim Pós-Embarque – Serviços;
    05 - BNDES-Exim Pré-Embarque - Serviços;
    06 - FGE - Fundo de Garantia à Exportação;
    07 - PROEX - EQUALIZAÇÃO
    08 - PROEX - Financiamento;
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"


class TsmecAfcomExToma(Enum):
    """Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo tomador
    do serviço:

    00 - Desconhecido (tipo não informado na nota de origem);
    01 - Nenhum;
    02 - Adm. Pública e Repr. Internacional;
    03 - Alugueis e Arrend. Mercantil de maquinas, equip., embarc. e aeronaves;
    04 - Arrendamento Mercantil de aeronave para empresa de transporte aéreo público;
    05 - Comissão a agentes externos na exportação;
    06 - Despesas de armazenagem, mov. e transporte de carga no exterior;
    07 - Eventos FIFA (subsidiária);
    08 - Eventos FIFA;
    09 - Fretes, arrendamentos de embarcações ou aeronaves e outros;
    10 - Material Aeronáutico;
    11 - Promoção de Bens no Exterior;
    12 - Promoção de Dest. Turísticos Brasileiros;
    13 - Promoção do Brasil no Exterior;
    14 - Promoção Serviços no Exterior;
    15 - RECINE;
    16 - RECOPA;
    17 - Registro e Manutenção de marcas, patentes e cultivares;
    18 - REICOMP;
    19 - REIDI;
    20 - REPENEC;
    21 - REPES;
    22 - RETAERO;
    23 - RETID;
    24 - Royalties, Assistência Técnica, Científica e Assemelhados;
    25 - Serviços de avaliação da conformidade vinculados aos Acordos da OMC;
    26 - ZPE;
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"


class TsmodoPrestacao(Enum):
    """Modo de Prestação:

    0 - Desconhecido (tipo não informado na nota de origem);
    1 - Transfronteiriço;
    2 - Consumo no Brasil;
    3 - Presença Comercial no Exterior;
    4 - Movimento Temporário de Pessoas Físicas;
    """
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


class TsmovTempBens(Enum):
    """Operação está vinculada à Movimentação Temporária de Bens:

    0 - Desconhecido (tipo não informado na nota de origem);
    1 - Não
    2 - Vinculada - Declaração de Importação
    3 - Vinculada - Declaração de Exportação
    """
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TsopConsumServ(Enum):
    """Opção para que o emitente informe onde ocorreu o consumo do serviço
    prestado.

    0 - Consumo do serviço prestado ocorrido no município do local da prestação;
    1 - Consumo do serviço prestado ocorrido ocorrido no exterior ;
    """
    VALUE_0 = "0"
    VALUE_1 = "1"


class TsopExigSuspensa(Enum):
    """Opção para Exigibilidade Suspensa:

    1 - Exigibilidade Suspensa por Decisão Judicial;
    2 - Exigibilidade Suspensa por Processo Administrativo;
    """
    VALUE_1 = "1"
    VALUE_2 = "2"


class TsopSimpNac(Enum):
    """Situação perante o Simples Nacional:

    1 - Não Optante;
    2 - Optante - Microempreendedor Individual (MEI);
    3 - Optante - Microempresa ou Empresa de Pequeno Porte (ME/EPP);
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TsopTipoBm(Enum):
    """Tipo do Benefício Municipal:

    1 - Alíquota Diferenciada;
    2 - Redução da BC;
    3 - Isenção;
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TsprocEmissao(Enum):
    """Processo de Emissão da DPS:

    1 - Emissão com aplicativo do contribuinte (via Web Service);
    2 - Emissão com aplicativo disponibilizado pelo fisco (Web);
    3 - Emissão com aplicativo disponibilizado pelo fisco (App);
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TsregEspTrib(Enum):
    """Tipos de Regimes Especiais de Tributação:

    0 - Nenhum;
    1 - Ato Cooperado (Cooperativa);
    2 - Estimativa;
    3 - Microempresa Municipal;
    4 - Notário ou Registrador;
    5 - Profissional Autônomo;
    6 - Sociedade de Profissionais;
    """
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class TsregimeApuracaoSimpNac(Enum):
    """Opção para que o contribuinte optante pelo Simples Nacional ME/EPP (opSimpNac = 3) possa indicar, ao emitir o documento fiscal, em qual regime de apuração os tributos federais e municipal estão inseridos, caso tenha ultrapassado algum sublimite ou limite definido para o Simples Nacional.
    1 – Regime de apuração dos tributos federais e municipal pelo SN;
    2 – Regime de apuração dos tributos federais pelo SN e ISSQN  por fora do SN conforme respectiva legislação municipal do tributo;
    3 – Regime de apuração dos tributos federais e municipal por fora do SN conforme respectivas legilações federal e municipal de cada tributo;"""
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class Tsrodagem(Enum):
    """Tipo de rodagem:

    1 - Simples;
    2 - Dupla;
    """
    VALUE_1 = "1"
    VALUE_2 = "2"


class TstipoAmbiente(Enum):
    """Tipos de ambiente do Sistema Nacional NFS-e: 1 - Produção; 2 - Homologação;"""
    VALUE_1 = "1"
    VALUE_2 = "2"


class TstipoCst(Enum):
    """Código de Situação Tributária do PIS/COFINS (CST):

    00 - Nenhum;
    01 - Operação Tributável com Alíquota Básica;
    02 - Operação Tributável com Alíquota Diferenciada;
    03 - Operação Tributável com Alíquota por Unidade de Medida de Produto;
    04 - Operação Tributável monofásica - Revenda a Alíquota Zero;
    05 - Operação Tributável por Substituição Tributária;
    06 - Operação Tributável a Alíquota Zero;
    07 - Operação Tributável da Contribuição;
    08 - Operação sem Incidência da Contribuição;
    09 - Operação com Suspensão da Contribuição;
    """
    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"


class TstipoEmissao(Enum):
    """Tipo de emissão da NFS-e:

    1 - Emissão normal no modelo da NFS-e Nacional;
    2 - Emissão original em leiaute próprio do município com transcrição para o modelo da NFS-e Nacional.
    """
    VALUE_1 = "1"
    VALUE_2 = "2"


class TstipoImunidadeIssqn(Enum):
    """Identificação da Imunidade do ISSQN – somente para o caso de Imunidade.
    Tipos de Imunidades:

    0 - Imunidade (tipo não informado na nota de origem);
    1 - Patrimônio, renda ou serviços, uns dos outros (CF88, Art 150, VI, a);
    2 - Templos de qualquer culto (CF88, Art 150, VI, b);
    3 - Patrimônio, renda ou serviços dos partidos políticos, inclusive suas fundações, das entidades sindicais dos trabalhadores, das instituições de        educação e de assistência social, sem fins lucrativos, atendidos os requisitos da lei (CF88, Art 150, VI, c);
    4 - Livros, jornais, periódicos e o papel destinado a sua impressão (CF88, Art 150, VI, d);
    5 - Fonogramas e videofonogramas musicais produzidos no Brasil contendo obras musicais ou literomusicais de autores brasileiros e/ou obras em geral interpretadas por artistas brasileiros bem como os suportes materiais ou arquivos digitais que os contenham, salvo na etapa de replicação industrial de mídias ópticas de leitura a laser.   (CF88, Art 150, VI, e);
    """
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


class TstipoIndTotTrib(Enum):
    """Indicador de informação de valor total de tributos. Possui valor fixo
    igual a zero (indTotTrib=0). Não informar nenhum valor estimado para os
    Tributos (Decreto 8.264/2014).

    0 - Não;
    """
    VALUE_0 = "0"


class TstipoRetIssqn(Enum):
    """Tipo de retencao do ISSQN:

    1 - Não Retido;
    2 - Retido pelo Tomador;
    3 - Retido pelo Intermediario;
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TstipoRetPiscofins(Enum):
    """Tipo de retencao do Pis/Cofins:

    1 - Retido;
    2 - Não Retido;
    """
    VALUE_1 = "1"
    VALUE_2 = "2"


class TstribIssqn(Enum):
    """Tributação do ISSQN sobre o serviço prestado:

    1 - Operação tributável;
    2 - Exportação de serviço;
    3 - Não Incidência;
    4 - Imunidade;
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


class Tsuf(Enum):
    """
    Tipo Sigla da UF.
    """
    AC = "AC"
    AL = "AL"
    AM = "AM"
    AP = "AP"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MG = "MG"
    MS = "MS"
    MT = "MT"
    PA = "PA"
    PB = "PB"
    PE = "PE"
    PI = "PI"
    PR = "PR"
    RJ = "RJ"
    RN = "RN"
    RO = "RO"
    RR = "RR"
    RS = "RS"
    SC = "SC"
    SE = "SE"
    SP = "SP"
    TO = "TO"


class TsvincPrest(Enum):
    """Vínculo entre as partes no negócio:

    0 - Sem vínculo com o tomador/ Prestador
    1 - Controlada;
    2 - Controladora;
    3 - Coligada;
    4 - Matriz;
    5 - Filial ou sucursal;
    6 - Outro vínculo;
    """
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"


class Tstat(Enum):
    """100 - NFS-e Gerada;
    101 - NFS-e de Substituição Gerada;
    102 - NFS-e de Decisão Judicial;
    103 - NFS-e Avulsa;" """
    VALUE_100 = "100"
    VALUE_101 = "101"
    VALUE_102 = "102"
    VALUE_103 = "103"
