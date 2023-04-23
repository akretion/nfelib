#! /bin/sh

#DOWNLOAD_SCHEMAS=1

# Pacote de Liberação nº 9 (Novo leiaute da NF-e, NT 2020.005, 2020.006 e NT 2021.002). Publicado em 29/06/2021.
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n nfe -v v4_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=lhqXSmnywl4=
  rm -rf nfelib/nfe/schemas
  cp -rf /tmp/generated/nfe/schemas nfelib/nfe/schemas
fi
xsdata generate nfelib/nfe/schemas/v4_0 --package nfelib.nfe.bindings.v4_0

# patch o campo IPI caso o patch no xsdata não foi aplicado
# ver detalhes aqui https://github.com/akretion/nfelib/issues/40
# sed  -e 's/IPI: List\[Tipi\] = field(/IPI: Optional\[Tipi\] = field(/' -i nfelib/nfe/bindings/v4_0/leiaute_nfe_v4_00.py
# infelizmente teria que trocar a outra linha depois tb default_factory=List por default=None para funcionar.
# vou deixar essa tentativa de patch com sed desativada por enquanto.

# Pacote de Liberação Distribuição de DF-e v1.02 (Atualizado em 25/10/16)
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n nfe_dist_dfe -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=n3Kn9%20YZNak=
  rm -rf nfelib/nfe_dist_dfe/schemas
  cp -rf /tmp/generated/nfe_dist_dfe/schemas nfelib/nfe_dist_dfe/schemas
fi
xsdata generate nfelib/nfe_dist_dfe/schemas/v1_0 --package nfelib.nfe_dist_dfe.bindings.v1_0

# Pacote de Liberação Evento Generico v1.01 (Atualizado em 30/05/2014)
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n nfe_evento_generico -v v1_0 -u   http://hom.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=YaiBe2csOmA=
  rm -rf nfelib/nfe_evento_generico/schemas
  cp -rf /tmp/generated/nfe_evento_generico/schemas nfelib/nfe_evento_generico/schemas
fi
xsdata generate nfelib/nfe_evento_generico/schemas/v1_0 --package nfelib.nfe_evento_generico.bindings.v1_0

# Pacote de Liberação Evento Canc v1.01 (30/05/2014)
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n nfe_evento_cancel -v v1_0 -u  http://hom.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=MtjAJ1Rurjc=
  rm -rf nfelib/nfe_evento_cancel/schemas
  cp -rf /tmp/generated/nfe_evento_cancel/schemas nfelib/nfe_evento_cancel/schemas
fi
xsdata generate nfelib/nfe_evento_cancel/schemas/v1_0 --package nfelib.nfe_evento_cancel.bindings.v1_0

# Pacote de Liberação Evento CCe v1.01 (30/05/2014)
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n nfe_evento_cce -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=P/FXaGiLKo0=
  rm -rf nfelib/nfe_evento_cce/schemas
  cp -rf /tmp/generated/nfe_evento_cce/schemas nfelib/nfe_evento_cce/schemas
fi
xsdata generate nfelib/nfe_evento_cce/schemas/v1_0 --package nfelib.nfe_evento_cce.bindings.v1_0

# Pacote de Liberação Evento Manifesta Destinatário v1.01 (30/05/2014)
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n nfe_evento_mde -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=y2nVL6/GFlU=
  # mude o encoding desse arquivo xsd de iso-8859-1 para utf-8 e amaldiçoe o cara que usou iso-8859-1
  iconv -f iso-8859-1 /tmp/generated/nfe_evento_mde/schemas/v1_0/retEnvConfRecebto_v1.00.xsd -t UTF-8 -o  /tmp/generated/nfe_evento_mde/schemas/v1_0/retEnvConfRecebto_v1.00.xsd
  rm -rf nfelib/nfe_evento_mdef/schemas
  cp -rf /tmp/generated/nfe_evento_mde/schemas nfelib/nfe_evento_mde/schemas
fi
xsdata generate nfelib/nfe_evento_mde/schemas/v1_0 --package nfelib.nfe_evento_mde.bindings.v1_0

# Consulta Cadastro - Pacote de Liberação No. 6t (21/03/2014)
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n nfe_cons -v v2_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=/KLQ3Wi0ckY=
  rm -rf /tmp/generated/nfe_cons/schemas/v2_0/*v2.00.xsd
  rm -rf nfelib/nfe_cons/schemas
  cp -rf /tmp/generated/nfe_cons/schemas nfelib/nfe_cons/schemas
fi
xsdata generate nfelib/nfe_cons/schemas/v2_0 --package nfelib.nfe_cons.bindings.v2_0

# Evento Ator Interessado na NF-e - Transportador. Publicado em 28/01/2021.
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n nfe_ator_interessado -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ufthUw%20oQd8=
  rm -rf nfelib/nfe_ator_interessado/schemas
  cp -rf /tmp/generated/nfe_ator_interessado/schemas nfelib/nfe_ator_interessado/schemas
fi
xsdata generate nfelib/nfe_ator_interessado/schemas/v1_0 --package nfelib.nfe_ator_interessado.bindings.v1_0

# Evento Prévio de Emissão em Contingência (EPEC) - v1.01 (30/05/2014)
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n nfe_epec -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=HcoVPI2JvY0=
  rm -rf nfelib/nfe_epec/schemas
  cp -rf /tmp/generated/nfe_ator_interessado/schemas nfelib/nfe_epec/schemas
fi
# xsdata generate nfelib/nfe_epec/schemas/v1_0 --package nfelib.nfe_epec.bindings.v1_0
# fix the main two files with -ss single-package to avoid circular deps:
xsdata generate nfelib/nfe_epec/schemas/v1_0/e110140_v1.00.xsd -ss single-package --package=nfelib.nfe_epec.bindings.v1_0.e110140_v1_00
xsdata generate nfelib/nfe_epec/schemas/v1_0/leiauteEPEC_v1.00.xsd -ss single-package --package=nfelib.nfe_epec.bindings.v1_0.leiaute_epec_v1_00

# Evento Comprovante Entrega da NF-e . Publicado em 19/05/2021 (Atualizado em 15/06/2021)
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n nfe_entrega -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=2AWmHNFOCe8=
  rm -rf nfelib/nfe_entrega/schemas
  cp -rf /tmp/generated/nfe_entrega/schemas nfelib/nfe_entrega/schemas
fi
xsdata generate nfelib/nfe_entrega/schemas/v1_0 --package nfelib.nfe_entrega.bindings.v1_0

# CT-e - Pacote de Liberação 3.00a (ZIP) - (NT 2021.001) (Publicado em 22/03/2021)
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n cte -v v3_0 -u https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=hFnCT8GrfTY=
  rm -rf nfelib/cte/schemas
  cp -rf /tmp/generated/cte/schemas nfelib/cte/schemas
fi
xsdata generate nfelib/cte/schemas/v3_0 --package nfelib.cte.bindings.v3_0

# CT-e - Web Service Distribuição de DF-e de Interesse dos Atores do CT-e
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n cte_dist_dfe -v v1_0 -u https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=l6I2ehbBicE=
  rm -rf nfelib/cte_dist_dfe/schemas
  cp -rf /tmp/generated/cte_dist_dfe/schemas nfelib/cte_dist_dfe/schemas
fi
xsdata generate nfelib/cte_dist_dfe/schemas/v1_0 --package nfelib.cte_dist_dfe.bindings.v1_0

# MDF-e - Manifesto Eletrônico de Documentos Fiscais - Schema NT 2021.002 (05/04/2021)
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n mdfe -v v3_0 -u https://mdfe-portal.svrs.rs.gov.br/MDFE/DownloadArquivoEstatico/?sistema=MDFE&tipoArquivo=2&nomeArquivo=PL_MDFe_300a_NT022021.zip
  # NOTE this one was actually downloaded manually to /tmp/generated/mdfe/schemas/v3_0
  rm -rf nfelib/mdfe/schemas
  cp -rf /tmp/generated/mdfe/schemas nfelib/mdfe/schemas
fi
xsdata generate nfelib/mdfe/schemas/v3_0 --package nfelib.mdfe.bindings.v3_0

# MDF-e - Web Service Distribuição de DF-e de Interesse dos Atores do MDF-e
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n cte_dist_dfe -v v1_0 -u https://dfe-portal.svrs.rs.gov.br/MDFE/DownloadArquivoEstatico/?sistema=MDFE&tipoArquivo=2&nomeArquivo=PL_MDFeDistDFe_100.zip
  rm -rf nfelib/mdfe_dist_dfe/schemas
  cp -rf /tmp/generated/mdfe_dist_dfe/schemas nfelib/mdfe_dist_dfe/schemas
fi
xsdata generate nfelib/mdfe_dist_dfe/schemas/v1_0 --package nfelib.mdfe_dist_dfe.bindings.v1_0

# BP-e - Bilhete de Passagem Eletrônico - Schemas NT 2021.001 (26/01/2021)
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n bpe -v v1_0 -u https://dfe-portal.svrs.rs.gov.br/BPE/DownloadArquivoEstatico/?sistema=BPE&tipoArquivo=2&nomeArquivo=PL_BPe_100b_NT012021.zip
  # NOTE this one was actually downloaded manually to /tmp/generated/bpe/schemas/v1_0
  rm -rf nfelib/bpe/schemas
  cp -rf /tmp/generated/bpe/schemas nfelib/bpe/schemas
fi
xsdata generate nfelib/bpe/schemas/v1_0 --package nfelib.bpe.bindings.v1_0

# NFS-e Pacote de esquemas XSD V1.00.02 - (16/09/2022)
if [$DOWNLOAD_SCHEMAS]; then
  erpbrasil-edoc-gen-download-schema -n nfse -v v1_0 -u https://www.gov.br/nfse/pt-br/documentacao-tecnica/xsd_pl_nfse_1-00-producao.zip/@@download/file/XSD_PL_NFSe_1.00-Produ%C3%A7%C3%A3o.zip
  rm -rf nfelib/nfse/schemas
  cp -rf /tmp/generated/nfse/schemas nfelib/nfse/schemas
  xsdata generate nfelib/nfse/schemas/v1_0 --package nfelib.nfse.bindings.v1_0
fi
