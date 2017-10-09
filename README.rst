nfelib Python library
=====================

A nfelib é uma biblioteca para ler e gerir notas fiscais electronicas brasileiras (NFe's). Ja existem varias outras bibliotecas, porem na Akretion queriamos algo que fosse simples de manter para usar com o ERP open source Odoo. A nfelib nao tem a pretençao de solucionar toda burocracia do SPED sozinha, mas apenas a questao da geraçao da NFe. Tambem criamos outras bibliotecas semelhantes para os outros documentos electronicos do SPED.

A nfelib permite de:

* Gerir os XMLs dos documentos fiscais.
* Validar os dados com as mesmas validaçoes dos XSDs ao montar os objetos, o que evita detetar os erros apenas ao transmitir o XML.
* Importar XMLs e transfoma-los em objetos Python. Usando um sistema de sub-classes, fica facil mapear esses objetos em outros objetos ou adicionar qualquer metodo customizado.

A nfelibe é:

* **Simples e confiavel**. O codigo é gerido pelo generateDS a partir dos XSD's da Fazenda usando o script generate de menos de **70 linhas de codigo** apenas.
* Compativel com **Python 2 e Python 3**.
* Capaz de carregar **varias versoes dos esquemas**. Isso pode ser bem util ao receber uma nota fiscal com um layout antigo.

As tecnologias XML (XSD, WSDL, SOAP...) usadas pelo site da Fazenda foram criadas inicialmente para Java e .Net. Durante um bom tempo essas tecnologias ficaram para tras no mundo do Python. Por isso varias pessoas foram criar bibliotecas manualmente com milhares de linhas e poucos testes para montar os XMLs dos documentos electronicos. Mas hoje é um absurdo usar biblitecas escritas manualmente e depender do autor inicial a cada atualizaçao dos esquemas ou quando seu programa deve migrar para Python 3. Veja o conceito do 'Truck Factor' <https://en.wikipedia.org/wiki/Bus_factor>

É debativel qual é a melhor forma de transmitir esses documentos electronicos para o site da Fazenda (talvez com essas bibliotecas que ja existem, talvez com outras bibilotecas em Java especializadas em transmitir os documentos electronicos). Porem na questao de montar os XML e poder efetuar validaçoes dos dados o mais cedo possivel (perto do momento em qual o usuario preenchou os dados), dificilmente uma biblioteca de milhares de linhas escrita manualmente fica mais confiavel do que codigo gerido a partir dos XSD da Fazenda apenas. As classes da nfelib sao geridas usando a ferramenta generateDS. A funcionalidade de sub-classes do generateDS tambem ajuda na questao dos mapeamentos entre o modelo de dados dos esquemas da fazenda e o modelo de dados do seu software (ERP por examplo). Finalmente ficou possivel fazer com Python o que o pessoal do Java ja fazia ha muito tempo com as tecnologias do tipo JAXB.

Voce pode aprender mais sobre o generateDS.py aqui: <http://www.davekuhlman.org/generateDS.html>

como instalar
=============

.. code::

  pip install git+https://github.com/akretion/nfelib.git#egg=nfelib

como usar
=========

.. code::

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
