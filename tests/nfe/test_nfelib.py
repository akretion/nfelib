# -*- coding: utf-8 -*-

import os
import sys
from os import path
try:
    import StringIO
except ImportError:
    from io import StringIO
from xmldiff import main
sys.path.append(path.join(path.dirname(__file__), '..', 'nfelib'))
from nfelib.v4_00 import leiauteNFe_sub as parser


def test_in_out():
    path = 'tests/nfe/v4_00'
    for filename in os.listdir(path):
        subtree = parser.parsexml_('%s/%s' % (path, filename,))
        inputfile = 'tests/input.xml'
        subtree.write(inputfile, encoding='utf-8')

        # agora vamos importar o XML da nota e transforma-lo em objeto Python:
        nota = parser.parse(inputfile)#'%s/%s' % (path, filename,))
        # agora podemos trabalhar em cima do objeto e fazer operaçoes como:
        nota.infNFe.emit.CNPJ

        filename = 'tests/output.xml'
        with open(filename, 'w') as f:
            parser.export(nota, nfeProc=False, stream=f)

        diff = main.diff_files('tests/input.xml', 'tests/output.xml')
        print(diff)
        assert len(diff) == 0
