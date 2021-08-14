[![Build Status](https://travis-ci.org/akretion/nfelib.svg?branch=master_gen_v4_00)](https://travis-ci.org/akretion/nfelib)

[![nfelib](https://raw.githubusercontent.com/akretion/nfelib/master/ext/nfe.jpg)](https://github.com/akretion/nfelib/) by [![Akretion](https://raw.githubusercontent.com/akretion/nfelib/master/ext/akretion-logo2.png)](https://akretion.com/pt_BR)

# nfelib Python Library

A nfelib é uma biblioteca para ler e gerir notas fiscais eletrônicas brasileiras (NFe's). A nfelib não tem a pretensão de solucionar toda burocracia do SPED sozinha, mas foca apenas na questão do parsing e da geração da NFe.

* Para transmitir as NFe's para a receita, aconselhamos a biblioteca Python Zeep, ou entao por examplo https://github.com/erpbrasil/erpbrasil.edoc.
* E para imprimir o DANFE, é possivel usar https://github.com/erpbrasil/erpbrasil.edoc.pdf

Na Akretion queriamos algo modular, simples de se manter para usar com o ERP Odoo que adaptamos para as necessidades fiscais brasileiras. Também criamos outras bibliotecas semelhantes para os outros documentos eletrônicos do SPED (e especialmente para NFS-e, MDFe, CTe, E-Social e SPED-Reinf, GNRE, BP-e).

Durante anos usamos o https://github.com/aricaldeira/PySPED. Porém no PySPED, o autor partiu para escrever e manter manualmente **mais de 10 000 de linhas de código**, apenas nessa parte para montar o leiaute da NFe https://github.com/aricaldeira/PySPED/tree/master/pysped/nfe/leiaute. Mas isso ocasiona um custo de manutenção proibitivo a cada atualização dos esquemas sem falar que por se tratar de código manual tem vários erros com as TAGs pouco usadas e na Akretion cansamos de escrever patch na urgência no PySPED a cada vez que um cliente Odoo nosso não consegue transmitir uma NF'e. Na verdade o equivalente dessas 10 000 linhas de código (anos de trabalho do autor) podem ser geradas por **esse único comando** com a ferramenta [generateDS](http://www.davekuhlman.org/generateDS.html) usada por essa lib:

```bash
generateDS -o leiauteNFe.py leiauteNFe_v4.00.xsd
```

A nfelib permite de:

* Gerir os XMLs dos documentos fiscais.
* Validar os dados com **as mesmas validações dos XSD's ao montar os objetos**, o que evita detectar os erros apenas ao transmitir o XML.
* Importar XMLs e transforma-los em objetos Python. Usando um sistema de sub-classes, fica fácil mapear esses objetos em outros objetos ou adicionar qualquer método customizado.

A nfelib é:

* **Simples e confiável**. O código é gerido pelo generateDS a partir dos XSD's da Fazenda. Ele **reflete exatamente a especificação fiscal** da versão do esquema escolhida sem que você deva se perguntar qual é o grau de aderência do código.
* Compatível com **Python 3** (e com Python 2 se botar patches no generateDS e usar uma versao anterior)
* Capaz de carregar **várias versões dos esquemas**. Isso pode ser bem útil ao receber uma nota fiscal com um leiaute antigo.

Além disso, usando outros recursos do GenerateDS, é possível ir além dessa biblioteca nfelib e gerir automaticamente o modelo de dados do ERP pelo menos no ERP Odoo que tem um framework bastante poderoso. Sendo assim, é possivel montar dinamicamente as telas do usuário, a geração do XML ou a importação do XML quase que sem escrever código (apenas relacionar os campos mapeados com os campos já existentes do ERP). Fica então bem mais razoável para manter quando tem que atualizar os esquemas e assim também fica finalmente possível manter os dados do SPED dentro do ERP com um custo de manutenção compatível com o modelo open source.

Você pode aprender mais sobre o generateDS [aqui](http://www.davekuhlman.org/generateDS.html)

# Como Instalar

Nesse momento inicial nos ainda não atualizamos o pacote no Pypi e recomendamos a instalação pelo git abaixo, possivelmente especificando uma revisão git:

```bash
pip install git+https://github.com/akretion/nfelib.git@master_gen_v4_00#egg=nfelib
```

# Gerir a lib novamente / processo de release
**Muito importante:** as fonte estao mantido na branch **master**. Entao voce tem que fazer primeiro

```
git checkout master
```

Depois seria possível rodar o generateDS manualmente em cada arquivo xsd do esquema que interessa. Porem é interessante instalar essa pequena ferramenta https://github.com/akretion/erpbrasil.edoc.gen para automatizar as operações. Depois da lib instalada (ela puxa o pacote GenerateDS), basta fazer:
```bash
# Download dos esquemas de NFe do portal da Fazenda: https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=/fwLvLUSmU8=

# Pacote de Liberação nº 9 (Novo leiaute da NF-e, NT 2020.005, 2020.006 e NT 2021.002). Publicado em 29/06/2021.
erpbrasil-edoc-gen-download-schema -n nfe -v v4.00 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=lhqXSmnywl4=
erpbrasil-edoc-gen-generate-python -n nfe -v v4.00 -i "retConsStatServ|retConsSitNFe|retEnviNFe|retConsReciNFe|retInutNFe" -d .

# Pacote de Liberação Distribuição de DF-e v1.02 (Atualizado em 25/10/16)
erpbrasil-edoc-gen-download-schema -n nfe -v v4.00 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=n3Kn9%20YZNak=
erpbrasil-edoc-gen-generate-python -n nfe -v v4.00 -i "distDFeInt|retDistDFeInt" -d .

# Pacote de Liberação Evento Generico v1.01 (Atualizado em 30/05/2014)
erpbrasil-edoc-gen-download-schema -n nfe -v v4.00 -u   http://hom.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=YaiBe2csOmA=
erpbrasil-edoc-gen-generate-python -n nfe -v v4.00 -i "retEnvEvento" -d .

# Pacote de Liberação Evento Canc v1.01 (30/05/2014)
erpbrasil-edoc-gen-download-schema -n nfe -v v4.00 -u  http://hom.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=MtjAJ1Rurjc=
erpbrasil-edoc-gen-generate-python -n nfe -v v4.00 -i "retEnvEventoCancNFe" -d .

# Pacote de Liberação Evento CCe v1.01 (30/05/2014)
erpbrasil-edoc-gen-download-schema -n nfe -v v4.00 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=P/FXaGiLKo0=
erpbrasil-edoc-gen-generate-python -n nfe -v v4.00 -i "retEnvCCe" -d .

# Pacote de Liberação Evento Manifesta Destinatário v1.01 (30/05/2014)
erpbrasil-edoc-gen-download-schema -n nfe -v v4.00 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=y2nVL6/GFlU=
# mude o encoding desse arquivo xsd de iso-8859-1 para utf-8 e amaldiçoe o cara que usou iso-8859-1
iconv -f iso-8859-1 /tmp/generated/schemas/nfe/v4_00/retEnvConfRecebto_v1.00.xsd -t UTF-8 -o /tmp/generated/schemas/nfe/v4_00/retEnvConfRecebto_v1.00.xsd
erpbrasil-edoc-gen-generate-python -n nfe -v v4.00 -i "retEnvConfRecebto" -d .

# Consulta Cadastro - Pacote de Liberação No. 6t (21/03/2014)
erpbrasil-edoc-gen-download-schema -n nfe -v v4.00 -u https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=/KLQ3Wi0ckY=
erpbrasil-edoc-gen-generate-python -n nfe -v v4.00 -i "retConsCad" -d .
```
Depois você pode olhar os arquivos Python geridos na pasta nfelib/v4_00/ e rodar os testes por examplo (`python3 -m pytest  tests -v`).

Se você quiser criar uma nova versão do nfelib no Github, depois de gerir voce tem fazer um commit do README.md com a receita do bolo atualizada (essa parte) e dos testes atualizados.
Depois voce tem que trocar de branch de novo para a branch onde fica o codigo gerido e gerir de novo:
```bash
rm -r nfelib
git checkout master_gen_v4_00
git merge master -X theirs
# gera de novo com o script acima (erpbrasil-edoc-gen-generate-python...)
# roda os tests para ver se esta tudo OK
python3 -m pytest  tests -v
# copia os schemas, por examplo com
rm -r schemas/nfe
cp -r /tmp/generated/schemas/nfe schemas/nfe
git add schemas
git add nfelib
# ai vc pode fazer um commit e um push com as mudanças (e 2 PRs para as branches master e master_gen_v4_00 eventualmente)
```

# Rodar os testes

```bash
python3 -m pytest  tests -v
```

# Como Usar

```python
  # nfelib permite ler os dados de uma nota fiscal, por exemplo no formato 4.00:
  >>> from nfelib.v4_00 import leiauteNFe_sub as parser
  # vamos importar o XML da nota e transforma-lo em objeto Python:
  >>> nota = parser.parse(inputfile)
  # agora podemos trabalhar em cima do objeto e fazer operaçoes como:
  >>> nota.infNFe.emit.CNPJ
  '03102552000172'
  >>> len(nota.infNFe.det)
  42
  # (a nota tem 42 linhas)

  # podemos tambem alterar os dados:
  nota.infNFe.emit.CNPJ = ...

  # e finalmente podemos exportar a nota num arquivo de novo por examplo
  >>> with open(filename, 'w') as f:
  >>>     parser.export(nota, nfeProc=False, stream=f)


  # nfelib também permite de montar o XML de uma nota fiscal com todas validações dos XSDs já nos objetos:
  >>> from nfelib.v4_00 import retEnviNFe as leiauteNFe
  >>> enderEmit=leiauteNFe.TEnderEmi(xLgr='NKwaAJ5ZJ49aQYmqBvxMhBzkGUqvtXnqusGEtjDzKCXPGwrEZCS8LGKHyBbV',
  nro='11mzXHR8rZTgfE35EqfGhiShiIwQfLCAziFDXVgs3EjLSPkZkCvfGNLMEf5y',
  xCpl='Fr3gSvoAeKbGpQD3r98KFeB50P3Gq14XBVsv5fpiaBvJ3HTOpREiwYGs20Xw',
  xBairro='67LQFlXOBK0JqAE1rFi2CEyUGW5Z8QmmHhzmZ9GABVLKa9AbV0uFR0onl7nU',
  cMun='9999999',
  xMun='s1Cr2hWP6bptQ80A9vWBuTaODR1U82LtKQi1DEm3LsAXu9AbkSeCtfXJVTKG',
  UF='RS',
  CEP='88095550',
  cPais=1058,
  fone='12345678901324')

  # se tentar montar algum objeto com algum dado inválido:
  >>> emitente=leiauteNFe.emitType(enderEmit=enderEmit, CPF='Brazil is a f*cking bureaucracy', xNome='Raphael', IE='12345678901234', IEST='84', IM='zjfBnFVG8TBq8iW', CNAE='0111111', CRT='3')
>>> leiauteNFe.emitType(enderEmit=enderEmit, CPF='Brazil is a f*cking bureaucracy', xNome='Raphael', IE='12345678901234', IEST='84', IM='zjfBnFVG8TBq8iW', CNAE='0111111', CRT='3')
/home/rvalyi/DEV/nfelib-edocs-gen/nfelib/v4_00/leiauteNFe.py:5821: UserWarning: Value "b'Brazil is a f*cking bureaucracy'" does not match xsd maxLength restriction on TCpf
  warnings_.warn('Value "%(value)s" does not match xsd maxLength restriction on TCpf' % {"value" : value.encode("utf-8")} )
/home/rvalyi/DEV/nfelib-edocs-gen/nfelib/v4_00/leiauteNFe.py:5824: UserWarning: Value "b'Brazil is a f*cking bureaucracy'" does not match xsd pattern restrictions: [['^([0-9]{11})$']]
  warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_TCpf_patterns_, ))
<nfelib.v4_00.leiauteNFe.emitType object at 0x7f623c4be748>

  # para gerir o XML:
  >>> import sys
  >>> emitente.export(sys.stdout, 0)
  <emitType>
    <CPF>12345678901</CPF>
    <xNome>Raphael</xNome>
    <enderEmit>
        <xLgr>NKwaAJ5ZJ49aQYmqBvxMhBzkGUqvtXnqusGEtjDzKCXPGwrEZCS8LGKHyBbV</xLgr>
        <nro>11mzXHR8rZTgfE35EqfGhiShiIwQfLCAziFDXVgs3EjLSPkZkCvfGNLMEf5y</nro>
        <xCpl>Fr3gSvoAeKbGpQD3r98KFeB50P3Gq14XBVsv5fpiaBvJ3HTOpREiwYGs20Xw</xCpl>
        <xBairro>67LQFlXOBK0JqAE1rFi2CEyUGW5Z8QmmHhzmZ9GABVLKa9AbV0uFR0onl7nU</xBairro>
        <cMun>9999999</cMun>
        <xMun>s1Cr2hWP6bptQ80A9vWBuTaODR1U82LtKQi1DEm3LsAXu9AbkSeCtfXJVTKG</xMun>
        <UF>RS</UF>
        <CEP>88095550</CEP>
        <cPais>1058</cPais>
        <fone>12345678901324</fone>
    </enderEmit>
    <IE>12345678901234</IE>
    <IEST>84</IEST>
    <IM>zjfBnFVG8TBq8iW</IM>
    <CNAE>0111111</CNAE>
    <CRT>3</CRT>
  </emitType>
```

# Uso no ERP Odoo

Para cada documento eletrônico para o qual existe esquema XSD's, a Akretion fez um repo Github com uma lib desse tipo.

Mas fomos além: eu tambem criei um gerador de modelos abstratos (mixins) Odoo, de forma que para os documentos fiscais complexos como a NFe vc tem um marshalling/unmarshalling automatico dos dados ate os modelos persistentes do ERP e se remapeando nos objetos nativos do Odoo https://github.com/akretion/generateds-odoo

O uso dessa lib no Odoo para emitir e importar NFe's pode ser visto nesse módulo da OCA: https://github.com/OCA/l10n-brazil/tree/12.0/l10n_br_nfe
