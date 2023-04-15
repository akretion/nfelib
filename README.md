<h2 align="center">nfelib Python Library</h2>

<p align="center">
<a href="https://github.com/akretion/nfelib" > 
 <img src="https://raw.githubusercontent.com/akretion/nfelib/master/ext/nfe.jpg"/> 
</a>
by
<a href="https://akretion.com/pt_BR" > 
 <img src="https://raw.githubusercontent.com/akretion/nfelib/master/ext/akretion-logo2.png"/> 
</a>
</p>

<p align="center">
<a href="https://codecov.io/gh/akretion/nfelib" > 
 <img src="https://codecov.io/gh/akretion/nfelib/branch/generated/graph/badge.svg?token=IqcCHJzhuw"/> 
</a>
<a href="https://pypi.org/project/nfelib/"><img alt="PyPI" src="https://img.shields.io/pypi/v/nfelib"></a>
<a href="https://pepy.tech/project/nfelib"><img alt="Downloads" src="https://pepy.tech/badge/nfelib"></a>
</p>


# nfelib Python Library

A nfelib é uma biblioteca para ler e gerar notas fiscais eletrônicas brasileiras (NFe's).

* Para transmitir as NFe's para a receita, aconselhamos a biblioteca Python Zeep, PyNFe ou entao por examplo https://github.com/erpbrasil/erpbrasil.edoc.
* E para imprimir o DANFE, é possivel usar https://github.com/erpbrasil/erpbrasil.edoc.pdf

Na versão 1.x os "bindings" eram gerados usando generateDS e agora na versão 2.x usamos [xsdata](https://xsdata.readthedocs.io/en/latest/).
Se vc estiver procurando o codigo "legacy da versão 1.x, ele esta na branch [master_gen_v4_00](https://github.com/akretion/nfelib/tree/master_gen_v4_00)

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

```bash
pip install nfelib-xsdata
```
# Gerir a lib novamente / processo de release
TODO

```

# Rodar os testes

```bash
pytest
```

# Como Usar

TODO

# Uso no ERP Odoo

TODO
