# Pacote de Liberação nº 9 (Novo leiaute da NF-e, NT 2020.005, 2020.006 e NT 2021.002). Publicado em 29/06/2021.
erpbrasil-edoc-gen-download-schema -n nfe -v v4_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=lhqXSmnywl4=
rm -rf nfelib/schemas/nfe
cp -rf /tmp/generated/schemas/nfe nfelib/schemas/nfe
xsdata generate schemas/nfe/v4_0 --package nfelib.bindings.nfe.v4_0

# Pacote de Liberação Distribuição de DF-e v1.02 (Atualizado em 25/10/16)
erpbrasil-edoc-gen-download-schema -n nfe_dist_dfe -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=n3Kn9%20YZNak=
rm -rf nfelib/schemas/nfe_dist_dfe
cp -rf /tmp/generated/schemas/nfe_dist_dfe nfelib/schemas/nfe_dist_dfe
xsdata generate schemas/nfe_dist_dfe/v1_0 --package nfelib.bindings.nfe_dist_dfe.v1_0

# Pacote de Liberação Evento Generico v1.01 (Atualizado em 30/05/2014)
erpbrasil-edoc-gen-download-schema -n nfe_evento_generico -v v1_0 -u   http://hom.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=YaiBe2csOmA=
rm -rf nfelib/schemas/nfe_evento_generico
cp -rf /tmp/generated/schemas/nfe_evento_generico nfelib/schemas/nfe_evento_generico
xsdata generate schemas/nfe_evento_generico/v1_0 --package nfelib.bindings.nfe_evento_generico.v1_0

# Pacote de Liberação Evento Canc v1.01 (30/05/2014)
erpbrasil-edoc-gen-download-schema -n nfe_evento_cancel -v v1_0 -u  http://hom.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=MtjAJ1Rurjc=
rm -rf nfelib/schemas/nfe_evento_cancel
cp -rf /tmp/generated/schemas/nfe_evento_cancel nfelib/schemas/nfe_evento_cancel
xsdata generate schemas/nfe_evento_cancel/v1_0 --package nfelib.bindings.nfe_evento_cancel.v1_0

# Pacote de Liberação Evento CCe v1.01 (30/05/2014)
erpbrasil-edoc-gen-download-schema -n nfe_evento_cce -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=P/FXaGiLKo0=
rm -rf nfelib/schemas/nfe_evento_cce
cp -rf /tmp/generated/schemas/nfe_evento_cce nfelib/schemas/nfe_evento_cce
xsdata generate schemas/nfe_evento_cce/v1_0 --package nfelib.bindings.nfe_evento_cce.v1_0

# Pacote de Liberação Evento Manifesta Destinatário v1.01 (30/05/2014)
erpbrasil-edoc-gen-download-schema -n nfe_evento_mde -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=y2nVL6/GFlU=
# mude o encoding desse arquivo xsd de iso-8859-1 para utf-8 e amaldiçoe o cara que usou iso-8859-1
iconv -f iso-8859-1 /tmp/generated/schemas/nfe_evento_mde/v1_0/retEnvConfRecebto_v1.00.xsd -t UTF-8 -o  /tmp/generated/schemas/nfe_evento_mde/v1_0/retEnvConfRecebto_v1.00.xsd
rm -rf nfelib/schemas/nfe_evento_mdef
cp -rf /tmp/generated/schemas/nfe_evento_mde nfelib/schemas/nfe_evento_mde
xsdata generate schemas/nfe_evento_mde/v1_0 --package nfelib.bindings.nfe_evento_mde.v1_0

# Consulta Cadastro - Pacote de Liberação No. 6t (21/03/2014)
erpbrasil-edoc-gen-download-schema -n nfe_cons -v v2_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=/KLQ3Wi0ckY=
rm -rf /tmp/generated/schemas/nfe_cons/v2_0/*v2.00.xsd
rm -rf nfelib/schemas/nfe_cons
cp -rf /tmp/generated/schemas/nfe_cons nfelib/schemas/nfe_cons
xsdata generate schemas/nfe_cons/v2_0 --package nfelib.bindings.nfe_cons.v2_0

# Evento Ator Interessado na NF-e - Transportador. Publicado em 28/01/2021.
erpbrasil-edoc-gen-download-schema -n nfe_ator_interessado -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ufthUw%20oQd8=
rm -rf nfelib/schemas/nfe_ator_interessado
cp -rf /tmp/generated/schemas/nfe_ator_interessado nfelib/schemas/nfe_ator_interessado
xsdata generate schemas/nfe_ator_interessado/v1_0 --package nfelib.bindings.nfe_ator_interessado.v1_0

# Evento Prévio de Emissão em Contingência (EPEC) - v1.01 (30/05/2014)
erpbrasil-edoc-gen-download-schema -n nfe_epec -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=HcoVPI2JvY0=
rm -rf nfelib/schemas/nfe_epec
cp -rf /tmp/generated/schemas/nfe_ator_interessado nfelib/schemas/nfe_epec
xsdata generate schemas/nfe_epec/v1_0 --package nfelib.bindings.nfe_epec.v1_0

# Evento Comprovante Entrega da NF-e . Publicado em 19/05/2021 (Atualizado em 15/06/2021)
erpbrasil-edoc-gen-download-schema -n nfe_entrega -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=2AWmHNFOCe8=
rm -rf nfelib/schemas/nfe_entrega
cp -rf /tmp/generated/schemas/nfe_entrega nfelib/schemas/nfe_entrega
xsdata generate schemas/nfe_entrega/v1_0 --package nfelib.bindings.nfe_entrega.v1_0

# CT-e - Pacote de Liberação 3.00a (ZIP) - (NT 2021.001) (Publicado em 22/03/2021)
erpbrasil-edoc-gen-download-schema -n cte -v v3_0 -u https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=hFnCT8GrfTY=
rm -rf nfelib/schemas/cte
cp -rf /tmp/generated/schemas/cte nfelib/schemas/cte
xsdata generate schemas/cte/v3_0 --package nfelib.bindings.cte.v3_0

# CT-e - Web Service Distribuição de DF-e de Interesse dos Atores do CT-e
erpbrasil-edoc-gen-download-schema -n cte_dist_dfe -v v1_0 -u https://www.cte.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=l6I2ehbBicE=
rm -rf nfelib/schemas/cte_dist_dfe
cp -rf /tmp/generated/schemas/cte_dist_dfe nfelib/schemas/cte_dist_dfe
xsdata generate schemas/cte_dist_dfe/v1_0 --package nfelib.bindings.cte_dist_dfe.v1_0

# MDF-e - Manifesto Eletrônico de Documentos Fiscais - Schema NT 2021.002 (05/04/2021)
erpbrasil-edoc-gen-download-schema -n mdfe -v v3_0 -u https://mdfe-portal.svrs.rs.gov.br/MDFE/DownloadArquivoEstatico/?sistema=MDFE&tipoArquivo=2&nomeArquivo=PL_MDFe_300a_NT022021.zip
# NOTE this one was actually downloaded manually to /tmp/generated/schemas/mdfe/v3_0
rm -rf nfelib/schemas/mdfe
cp -rf /tmp/generated/schemas/mdfe nfelib/schemas/mdfe
xsdata generate schemas/mdfe/v3_0 --package nfelib.bindings.mdfe.v3_0

# BP-e - Bilhete de Passagem Eletrônico - Schemas NT 2021.001 (26/01/2021)
erpbrasil-edoc-gen-download-schema -n bpe -v v1_0 -u https://dfe-portal.svrs.rs.gov.br/BPE/DownloadArquivoEstatico/?sistema=BPE&tipoArquivo=2&nomeArquivo=PL_BPe_100b_NT012021.zip
# NOTE this one was actually downloaded manually to /tmp/generated/schemas/bpe/v1_0
rm -rf nfelib/schemas/bpe
cp -rf /tmp/generated/schemas/bpe nfelib/schemas/bpe
xsdata generate schemas/bpe/v1_0 --package nfelib.bindings.bpe.v1_0
