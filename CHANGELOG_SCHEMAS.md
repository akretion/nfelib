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

The sections are consolidated by the commit that introduces this mechanism and kept up
to date with the release: every binding package documents the exact published package it
was generated from, and each schema update commit also records its source package in its
commit message. A binding without a section here simply gets no metadata injected.

## nfe (v4_0)

- binding_dir: `nfe/bindings/v4_0`
- version: `PL_010f`
- package: `Pacote de Liberação 010f (zip PL_010f_v1.04)`
- nota_tecnica: `NT 2025.002 v1.50, NT 2026.007 v1.00`
- published_at: `2026-08-31`
- source_url:
  `https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=8ITFuBLltXs=`

## cte (v4_0)

- binding_dir: `cte/bindings/v4_0`
- version: `PL_CTe_400_NT2026.002_RTC_1.01_corr`
- package: `Pacote de Liberação 4.00`
- nota_tecnica: `NT 2026.001 v1.01c, NT 2026.002 v1.01`
- published_at: `2026-08-24`
- source_url:
  `https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=qGIe20MvWf4=`

## mdfe (v3_0)

- binding_dir: `mdfe/bindings/v3_0`
- version: `PL_MDFe_300b_NT012025_1.04`
- package: `Pacote de Liberação MDF-e 3.00b (zip dir PL_MDFe_300b_NT012025_1.05)`
- nota_tecnica: `NT 2025.001`
- published_at: `2026-04-25 (zip build date)`
- source_url:
  `https://dfe-portal.svrs.rs.gov.br/MDFE/DownloadArquivoEstatico/?sistema=MDFE&tipoArquivo=2&nomeArquivo=PL_MDFe_300b_NT012025_1.04.zip`

## nfse (v1_0)

- binding_dir: `nfse/bindings/v1_0`
- version: `NFSe-ESQUEMAS_XSD-v1.01-20260209 (leiaute 1.00)`
- package: `NFSe-ESQUEMAS_XSD-v1.01-20260209, diretório Schemas/1.00`
- nota_tecnica: `Leiaute NFSe 1.00 (eventos, tipos atualizados) + CNC`
- published_at: `2026-02-09`
- source_url:
  `https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/documentacao-atual/nfse-esquemas_xsd-v1-01-20260209.zip`

The same package also ships the 1.01 layout (`Schemas/1.01/`); it is not part of this
binding yet.
