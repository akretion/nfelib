NFeLib Python Library
=====================

A NFeLib é uma biblioteca para ler e gerir notas fiscais eletrônicas brasileiras (NFe's). A NFeLib não tem a pretensão de solucionar toda burocracia do SPED sozinha, mas foca apenas na questão do parsing e da geração da NFe. Para transmitir as NFe's para a receita, aconselhamos a biblioteca `PyTrustNFe <https://github.com/danimaribeiro/PyTrustNFe>`_. Na Akretion queriamos algo modular, simples de se manter para usar com o ERP Odoo que adaptamos para as necessidades fiscais brasileiras. Também criamos outras bibliotecas semelhantes para os outros documentos eletrônicos do SPED (especialmente para MDF, CTe, E-Social e SPED-Reinf).

Durante anos usamos o `pysped <https://github.com/aricaldeira/PySPED>`_. Porém no PySPED, o autor partiu para escrever e manter manualmente **mais de 10 000 de linhas de código**, apenas `nessa parte para montar o leiaute da NFe <https://github.com/aricaldeira/PySPED/tree/master/pysped/nfe/leiaute>`_. Mas isso ocasiona um custo de manutenção proibitivo a cada atualização dos esquemas sem falar que por se tratar de código manual tem vários erros com as TAGs pouco usadas e na Akretion cansamos de escrever patch na urgência no PySPED a cada vez que um cliente Odoo nosso não consegue transmistir uma NF'e. Na verdade o equivalente dessas 10 000 linhas de código podem ser geradas por um único comando com a ferramenta GenerateDS (pois é de chorar mesmo):

.. code-block:: bash

  python generateDS.py -o leiauteNFe.py leiauteNFe_v3.10.xsd

A NFeLib permite:

* Gerir os XMLs dos documentos fiscais.
* Validar os dados com **as mesmas validações dos XSD's ao montar os objetos**, o que evita detectar os erros apenas ao transmitir o XML.
* Importar XMLs e transforma-los em objetos Python. Usando um sistema de sub-classes, fica fácil mapear esses objetos em outros objetos ou adicionar qualquer método customizado.

A NFeLib é:

* **Simples e confiável**. O código é gerido pelo generateDS a partir dos XSD's da Fazenda. Ele **reflete exatamente a especificação fiscal** da versão do esquema escolhida sem que você deva se perguntar qual é o grau de aderência do código.
* Compatível com **Python 3** e com Python 2.
* Capaz de carregar **várias versões dos esquemas**. Isso pode ser bem útil ao receber uma nota fiscal com um leiaute antigo.

As tecnologias XML (XSD, WSDL, SOAP...) usadas pelo site da Fazenda foram criadas inicialmente para Java e .Net. Durante um bom tempo essas tecnologias ficaram para trás no mundo do Python. Por isso várias pessoas foram criar bibliotecas manualmente com milhares de linhas e poucos testes para montar os XMLs dos documentos eletrônicos. Mas hoje é um absurdo usar biblitecas escritas manualmente e depender do autor inicial a cada atualização dos esquemas ou quando seu programa deve migrar para Python 3. Veja o conceito do `Truck Factor <https://en.wikipedia.org/wiki/Bus_factor>`_

Além disso, usando outros recursos do GenerateDS, é possível ir além dessa biblioteca NFeLib e gerir automaticamente o modelo de dados do ERP pelo menos no ERP Odoo que tem um framework bastante poderoso. Sendo assim, é possivel montar dinamicamente as telas do usuário, a geração do XML ou a importação do XML quase que sem escrever código (apenas relacionar os campos mapeados com os campos já existentes do ERP). Fica então bem mais razoável para manter quando tem que atualizar os esquemas e assim também fica finalmente possível manter os dados do SPED dentro do ERP com um custo de manutenção compatível com o modelo open source.

Você pode aprender mais sobre o generateDS.py `aqui: <http://www.davekuhlman.org/generateDS.html>`_

Como Instalar
=============

.. code-block:: bash

  pip install nfelib

Como Usar
=========

.. code-block:: python

  # nfelib permite ler os dados de uma nota fiscal, por exemplo no formato 3.10:
  >>> from nfelib.v3_10 import leiauteNFe as leiauteNFe3
  # você usaria from nfelib.v4_00 import leiauteNFe as leiauteNFe4 para usar a versão 4.00 do leiaute

  # primeiro, temos que recortar a nota processada (tag rais nfeProc) no primeiro filho (tag NFe)
  # pois para evitar ter uma biblioteca enorme, o parser so funciona para o elemento NFe:
  >>> from lxml import etree
  >>> tree = etree.parse("/algum_caminho/alguma_nota.xml")
  >>> root = tree.getroot()
  >>> import tempfile
  >>> new_file, filename = tempfile.mkstemp()
  >>> subtree = etree.ElementTree(root[0]) # exportamentos apenas o primeiro filho
  >>> subtree.write(filename, encoding='utf-8')

  # agora vamos importar o XML da nota e transforma-lo em objeto Python:
  >>> nota = leiauteNFe3.parse(filename)
  # agora podemos trabalhar em cima do objeto e fazer operaçoes como:
  >>> nota.get_infNFe().get_emit().get_CNPJ()
  '03102552000172'
  >>> len(nota.get_infNFe().get_det())
  42
  # (a nota tem 42 linhas)

  # podemos tambem alterar os dados usandos os getters e setters...

  # e finalmente podemos exportar a nota num arquivo de novo por examplo
  # com Python2, hoje para exportar num arquivo, temos que primeiro exportar num
  # buffer StringIO e depois jogar ele dentro de um arquivo para poder garantir o encoding utf-8:
  >>> import StringIO
  >>> output = StringIO.StringIO()
  >>> nota.export(output, 0)
  >>> contents = output.getvalue()
  >>> output.close()

  >>> new_file, filename = tempfile.mkstemp()
  >>> with open(filename, 'w') as f:
  ...     write_txt = contents.encode('utf8')
  ...     f.write(write_txt)

  >>> print filename
  # basta abrir o arquivo filename, e conferir que ele eh semelhante ao arquivo de entrada (apenas recortado e formatado)


  # no Python3, o export é mais facil, basta fazer:
  >>> new_file, filename = tempfile.mkstemp()
  >>> nota.export(open(filename, 'w'), 0)
  >>> print(filename)


  # nfelib também permite de montar o XML de uma nota fiscal com todas validações dos XSDs já nos objetos:
  >>> enderEmit=leiauteNFe3.TEnderEmi(xLgr='NKwaAJ5ZJ49aQYmqBvxMhBzkGUqvtXnqusGEtjDzKCXPGwrEZCS8LGKHyBbV',
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
  >>> emitente=leiauteNFe3.emitType(enderEmit=enderEmit, CPF='Brazil is a f*cking bureaucracy', xNome='Raphael', IE='12345678901234', IEST='84', IM='zjfBnFVG8TBq8iW', CNAE='0111111', CRT='3')
  nfelib/v3_10/leiauteNFe.py:5560: UserWarning: Value "Brazil is a f*cking bureaucracy" does not match xsd maxLength restriction on TCpf
    warnings_.warn('Value "%(value)s" does not match xsd maxLength restriction on TCpf' % {"value" : value.encode("utf-8")} )
  nfelib/v3_10/leiauteNFe.py:5563: UserWarning: Value "Brazil is a f*cking bureaucracy" does not match xsd pattern restrictions: [['^[0-9]{11}$']]
    warnings_.warn('Value "%s" does not match xsd pattern restrictions: %s' % (value.encode('utf-8'), self.validate_TCpf_patterns_,

  >>> emitente=leiauteNFe3.emitType(enderEmit=enderEmit, CPF='12345678901', xNome='Raphael', IE='12345678901234', IEST='84', IM='zjfBnFVG8TBq8iW', CNAE='0111111', CRT='3')

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


Uso no ERP Odoo
===============

Para cada documento eletrônico para o qual existe esquema XSD's, a Akretion fez um repo Github com uma lib desse tipo.
Mas fomos além: para cada repo existe uma branch `'generated_odoo': <https://github.com/akretion/nfelib/tree/generated_odoo>` com o modelo de dados dos documento para o ERP livre Odoo.
Esses modelos são abstratos e podem ser injetados de forma inteligente no ERP Odoo para não ter que manter manualmente os campos fiscais e o mapeamento desses dados. Em breve a Akretion irá mostrar como fazer isso dentro de módulos da OCA.

