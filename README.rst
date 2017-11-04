nfelib Python library
=====================

A nfelib é uma biblioteca para ler e gerir notas fiscais electronicas brasileiras (NFe's). A nfelib não tem a pretenção de solucionar toda burocracia do SPED sozinha, mas foca apenas na questão do parsing e da geração da NFe. Para transmitir as NFe's para a receita, aconselhamos a biblioteca `PyTrustNFe <https://github.com/danimaribeiro/PyTrustNFe>`_. Na Akretion queriamos algo modular, simples de se manter para usar com o ERP Odoo que adaptamos para as necessidades fiscais brasileiras. Tambem criamos outras bibliotecas semelhantes para os outros documentos electronicos do SPED (especialmente para mdf, cte, e-social e sped-reinf).

Durante anos usamos o `pysped <https://github.com/aricaldeira/PySPED>`_. Porem no pysped, o autor partiu para escrever e manter manualmente **mais de 10 000 de linhas de codigo**, apenas `nessa parte para montar o leiaute da NFe <https://github.com/aricaldeira/PySPED/tree/master/pysped/nfe/leiaute>`_. Mas isso ocasiona um custo de manutenção prohibitivo a cada atualização dos esquemas sem falar que por se tratar de codigo manual tem varios erros com as tags poucas usadas e na Akretion cansamos de escrever patch na urgencia no pysped a cada vez que um cliente Odoo nosso não consegue transmistir uma NF'e. Na verdade o equivalente dessas 10 000 linhas de codigo podem ser geradas por um unico comando com a ferramenta GenerateDS (pois é de chorar mesmo):

.. code-block:: bash

  python generateDS.py -o leiauteNFe.py leiauteNFe_v3.10.xsd

A nfelib permite de:

* Gerir os XMLs dos documentos fiscais.
* Validar os dados com **as mesmas validaçoes dos XSD's ao montar os objetos**, o que evita detetar os erros apenas ao transmitir o XML.
* Importar XMLs e transfoma-los em objetos Python. Usando um sistema de sub-classes, fica facil mapear esses objetos em outros objetos ou adicionar qualquer metodo customizado.

A nfelibe é:

* **Simples e confiavel**. O codigo é gerido pelo generateDS a partir dos XSD's da Fazenda. Ele **reflete exactamente a especificação fiscal** da versão do esquema escolhida sem que vc deve se perguntar qual é o grau de aderencia do codigo.
* Compativel com **Python 3** e com Python 2.
* Capaz de carregar **varias versoes dos esquemas**. Isso pode ser bem util ao receber uma nota fiscal com um layout antigo.

As tecnologias XML (XSD, WSDL, SOAP...) usadas pelo site da Fazenda foram criadas inicialmente para Java e .Net. Durante um bom tempo essas tecnologias ficaram para tras no mundo do Python. Por isso varias pessoas foram criar bibliotecas manualmente com milhares de linhas e poucos testes para montar os XMLs dos documentos electronicos. Mas hoje é um absurdo usar biblitecas escritas manualmente e depender do autor inicial a cada atualização dos esquemas ou quando seu programa deve migrar para Python 3. Veja o conceito do `Truck Factor <https://en.wikipedia.org/wiki/Bus_factor>`_

Alem disso, usando outros recursos do GenerateDS, é possivel ir alem dessa biblioteca nfelib e gerir automaticamente o modelo de dado do ERP pelo menos no ERP Odoo que tem um framework bastante poderoso. Sendo assim, é possivel montar dinamicamente as telas do usuario, a geração do XML ou a importação do XML quasi que sem escrever codigo (apenas os campos que se mapeamem em campos ja existes do ERP). Fica então bem mais razovel para manter quando tem que atualizar os esquemas e assim tambem fica finalmente possivel manter os dados do SPED dentro do ERP com um custo de manutenção compativel com o modelo open source.

Voce pode aprender mais sobre o generateDS.py `aqui: <http://www.davekuhlman.org/generateDS.html>`_

como instalar
=============

.. code-block:: bash

  pip install nfelib

como usar
=========

.. code-block:: python

  # nfelib permite de ler os dados de uma nota fiscal, por examplo no formato 3.10:
  >>> from nfelib.v3_10 import leiauteNFe as leiauteNFe3
  # voce usaria from nfelib.v4_00 import leiauteNFe as leiauteNFe4 para usar a versao 4.00 do layout
  >>> nota = leiauteNFe3.parse("/algum_caminho/alguma_nota.xml")
  >>> nota.get_infNFe().get_emit().get_CPF()
  '12345678901'


  # nfelib tambem permite de montar o XML de uma nota fiscal com todas validaçoes dos XSDs ja nos objetos:
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

  # se tentar montar algum objeto com algum dado invalido:
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


uso no ERP Odoo
===============

para cada documento electronico para quais existem schemas XSD's, a Akretion fez um repo Github com uma lib desse tipo.
Mas fomos alem: para cada repo existe uma branch 'generated_odoo' com o modelo de dados dos documento para o ERP livre Odoo.
Esses modelos sao abstratos e podem ser injectados de forma inteligente no ERP Odoo para nao ter que manter manualmente os
campos fiscais e o mapeamento desses dados. Em breve a Akretion ira mostrar como fazer isso dentro de modulos da OCA.

