# Schema update history

This file tracks the XSD schema packages used to generate the bindings in this
repository. It is read by `generate_bindings.py` to inject metadata into the generated
`__init__.py` files.

Expected format for each section:

- `binding_dir`: relative path of the binding directory (e.g. `nfe/bindings/v4_0`)
- `version`: short package identifier (e.g. `PL_010e_v1.01`)
- `package`: human-readable package name (e.g. `Pacote de Liberação 010e v1.01`)
- `nota_tecnica`: technical note(s) the package implements
- `published_at`: publication date (YYYY-MM-DD or free text)
- `source_url`: download URL on the Fazenda portal

## nfe (v4_0)

- binding_dir: `nfe/bindings/v4_0`
- version: `PL_010e_v1.01`
- package: `Pacote de Liberação 010e v1.01`
- nota_tecnica: `NT 2025.002 v1.40, NT 2026.002 v1.0, NT 2026.003 v1.0`
- published_at: `2026-06-26`
- source_url:
  `https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=JcM57FABN1M`

## cte (v4_0)

- binding_dir: `cte/bindings/v4_0`
- version: `PL_CTe_400_NT2026.001_RTC_VincPgto_1.01c_corr`
- package: `Pacote de Liberação 4.00`
- nota_tecnica: `NT 2026.001 v1.01 corrected`
- published_at: `2026-06-08`
- source_url:
  `https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=1hNQGC4YA/o=`

## cte_dist_dfe (v1_0)

- binding_dir: `cte_dist_dfe/bindings/v1_0`
- version: `CTe_DistribuicaoDFe_1.0`
- package: `Web Service Distribuição de DF-e de Interesse dos Atores do CT-e`
- nota_tecnica: `-`
- published_at: `2016-10-25`
- source_url:
  `https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=l6I2ehbBicE=`

## mdfe (v3_0)

- binding_dir: `mdfe/bindings/v3_0`
- version: `PL_MDFe_300a_NT022021`
- package: `Pacote de Liberação 3.00a`
- nota_tecnica: `NT 2021.002`
- published_at: `2021-04-05`
- source_url:
  `https://mdfe-portal.svrs.rs.gov.br/MDFE/DownloadArquivoEstatico/?sistema=MDFE&tipoArquivo=2&nomeArquivo=PL_MDFe_300a_NT022021.zip`

## mdfe_dist_dfe (v1_0)

- binding_dir: `mdfe_dist_dfe/bindings/v1_0`
- version: `PL_MDFeDistDFe_100`
- package: `Web Service Distribuição de DF-e de Interesse dos Atores do MDF-e`
- nota_tecnica: `-`
- published_at: `2016-10-25`
- source_url:
  `https://dfe-portal.svrs.rs.gov.br/MDFE/DownloadArquivoEstatico/?sistema=MDFE&tipoArquivo=2&nomeArquivo=PL_MDFeDistDFe_100.zip`

## bpe (v1_0)

- binding_dir: `bpe/bindings/v1_0`
- version: `PL_BPe_100b_NT012021`
- package: `Pacote de Liberação 1.00b`
- nota_tecnica: `NT 2021.001`
- published_at: `2021-01-26`
- source_url:
  `https://dfe-portal.svrs.rs.gov.br/BPE/DownloadArquivoEstatico/?sistema=BPE&tipoArquivo=2&nomeArquivo=PL_BPe_100b_NT012021.zip`

## nfse (v1_0)

- binding_dir: `nfse/bindings/v1_0`
- version: `XSD_PL_NFSe_1.00-Produção`
- package: `Pacote de esquemas XSD V1.00.02`
- nota_tecnica: `-`
- published_at: `2022-09-16`
- source_url:
  `https://www.gov.br/nfse/pt-br/documentacao-tecnica/xsd_pl_nfse_1-00-producao.zip/@@download/file/XSD_PL_NFSe_1.00-Produção.zip`

## nfe_dist_dfe (v1_0)

- binding_dir: `nfe_dist_dfe/bindings/v1_0`
- version: `PL_DFeDistNFe_1.04`
- package: `Pacote de Liberação Distribuição de DF-e v1.04`
- nota_tecnica: `-`
- published_at: `2026-07-03`
- source_url:
  `https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=IzuP2y0G6hk=`

## nfe_evento_generico (v1_0)

- binding_dir: `nfe_evento_generico/bindings/v1_0`
- version: `v1.01`
- package: `Pacote de Liberação Evento Genérico v1.01`
- nota_tecnica: `-`
- published_at: `2014-05-30`
- source_url:
  `http://hom.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=YaiBe2csOmA=`

## nfe_evento_cancel (v1_0)

- binding_dir: `nfe_evento_cancel/bindings/v1_0`
- version: `v1.01`
- package: `Pacote de Liberação Evento Cancelamento v1.01`
- nota_tecnica: `-`
- published_at: `2014-05-30`
- source_url:
  `http://hom.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=MtjAJ1Rurjc=`

## nfe_evento_cce (v1_0)

- binding_dir: `nfe_evento_cce/bindings/v1_0`
- version: `v1.01`
- package: `Pacote de Liberação Evento CCe v1.01`
- nota_tecnica: `-`
- published_at: `2014-05-30`
- source_url:
  `https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=P/FXaGiLKo0=`

## nfe_evento_mde (v1_0)

- binding_dir: `nfe_evento_mde/bindings/v1_0`
- version: `v1.01`
- package: `Pacote de Liberação Evento Manifestação Destinatário v1.01`
- nota_tecnica: `-`
- published_at: `2014-05-30`
- source_url:
  `https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=y2nVL6/GFlU=`

## nfe_cons (v2_0)

- binding_dir: `nfe_cons/bindings/v2_0`
- version: `No. 6t`
- package: `Pacote de Liberação No. 6t`
- nota_tecnica: `-`
- published_at: `2014-03-21`
- source_url:
  `https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=/KLQ3Wi0ckY=`

## nfe_ator_interessado (v1_0)

- binding_dir: `nfe_ator_interessado/bindings/v1_0`
- version: `v1.01`
- package: `Evento Ator Interessado na NF-e - Transportador`
- nota_tecnica: `-`
- published_at: `2021-01-28`
- source_url:
  `https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ufthUw%20oQd8=`

## nfe_epec (v1_0)

- binding_dir: `nfe_epec/bindings/v1_0`
- version: `v1.01`
- package: `Evento Prévio de Emissão em Contingência (EPEC) v1.01`
- nota_tecnica: `-`
- published_at: `2014-05-30`
- source_url:
  `https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=HcoVPI2JvY0=`

## nfe_entrega (v1_0)

- binding_dir: `nfe_entrega/bindings/v1_0`
- version: `v1.01`
- package: `Pacote de Liberação Evento Comprovante Entrega da NF-e v1.01`
- nota_tecnica: `-`
- published_at: `2021-06-15`
- source_url:
  `https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=2AWmHNFOCe8=`

## nfe_insucesso (v1_0)

- binding_dir: `nfe_insucesso/bindings/v1_0`
- version: `v1.00`
- package: `Evento Insucesso na Entrega da NF-e`
- nota_tecnica: `-`
- published_at: `2024-04-26`
- source_url:
  `https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=qvyq5vuft74=`
