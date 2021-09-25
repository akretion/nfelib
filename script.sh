erpbrasil-edoc-gen-download-schema -n nfe -v v4_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=lhqXSmnywl4=
rm -rf schemas/nfe
cp -rf /tmp/generated/schemas/nfe schemas/nfe
xsdata generate schemas/nfe/v4_0 --package nfelib.nfe.v4_0

# Pacote de Liberação Distribuição de DF-e v1.02 (Atualizado em 25/10/16)
erpbrasil-edoc-gen-download-schema -n nfe_dist_dfe -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=n3Kn9%20YZNak=
rm -rf schemas/nfe_dist_dfe
cp -rf /tmp/generated/schemas/nfe_dist_dfe schemas/nfe_dist_dfe
xsdata generate schemas/nfe_dist_dfe/v1_0 --package nfelib.nfe_dist_dfe.v1_0

# Pacote de Liberação Evento Generico v1.01 (Atualizado em 30/05/2014)
erpbrasil-edoc-gen-download-schema -n nfe_evento_generico -v v1_0 -u   http://hom.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=YaiBe2csOmA=
rm -rf schemas/nfe_evento_generico
cp -rf /tmp/generated/schemas/nfe_evento_generico schemas/nfe_evento_generico
xsdata generate schemas/nfe_evento_generico/v1_0 --package nfelib.nfe_evento_generico.v1_0

# Pacote de Liberação Evento Canc v1.01 (30/05/2014)
erpbrasil-edoc-gen-download-schema -n nfe_evento_cancel -v v1_0 -u  http://hom.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=MtjAJ1Rurjc=
rm -rf schemas/nfe_evento_cancel
cp -rf /tmp/generated/schemas/nfe_evento_cancel schemas/nfe_evento_cancel
xsdata generate schemas/nfe_evento_cancel/v1_0 --package nfelib.nfe_evento_cancel.v1_0

# Pacote de Liberação Evento CCe v1.01 (30/05/2014)
erpbrasil-edoc-gen-download-schema -n nfe_evento_cce -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=P/FXaGiLKo0=
rm -rf schemas/nfe_evento_cce
cp -rf /tmp/generated/schemas/nfe_evento_cce schemas/nfe_evento_cce
xsdata generate schemas/nfe_evento_cce/v1_0 --package nfelib.nfe_evento_cce.v1_0

# Pacote de Liberação Evento Manifesta Destinatário v1.01 (30/05/2014)
erpbrasil-edoc-gen-download-schema -n nfe_evento_mde -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=y2nVL6/GFlU=
# mude o encoding desse arquivo xsd de iso-8859-1 para utf-8 e amaldiçoe o cara que usou iso-8859-1
iconv -f iso-8859-1 /tmp/generated/schemas/nfe_evento_mde/v1_0/retEnvConfRecebto_v1.00.xsd -t UTF-8 -o  /tmp/generated/schemas/nfe_evento_mde/v1_0/retEnvConfRecebto_v1.00.xsd
rm -rf schemas/nfe_evento_mde
cp -rf /tmp/generated/schemas/nfe_evento_mde schemas/nfe_evento_mde
xsdata generate schemas/nfe_evento_mde/v1_0 --package nfelib.nfe_evento_mde.v1_0

# Consulta Cadastro - Pacote de Liberação No. 6t (21/03/2014)
erpbrasil-edoc-gen-download-schema -n nfe_cons -v v2_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=/KLQ3Wi0ckY=
rm -rf /tmp/generated/schemas/nfe_cons/v2_0/*v2.00.xsd
rm -rf schemas/nfe_cons
cp -rf /tmp/generated/schemas/nfe_cons schemas/nfe_cons
xsdata generate schemas/nfe_cons/v2_0 --package nfelib.nfe_cons.v2_0

# Evento Ator Interessado na NF-e - Transportador. Publicado em 28/01/2021.
erpbrasil-edoc-gen-download-schema -n nfe_ator_interessado -v v1_0 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=ufthUw%20oQd8=
rm -rf schemas/nfe_ator_interessado
cp -rf /tmp/generated/schemas/nfe_ator_interessado schemas/nfe_ator_interessado
xsdata generate schemas/nfe_ator_interessado/v1_0 --package nfelib.nfe_ator_interessado.v1_0
