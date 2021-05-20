# -*- coding: utf-8 -*-
# Copyright (C) 2019 - TODAY Raphaël Valyi - Akretion

import os
import sys
from os import path
from xmldiff import main
sys.path.append(path.join(path.dirname(__file__), '..', 'nfelib'))
from nfelib.v4_00 import leiauteNFe_sub as nfe_sub
from nfelib.v4_00 import retEnviNFe as nfe
from nfelib.v4_00 import retInutNFe
from nfelib.v4_00 import retConsStatServ
from nfelib.v4_00 import retConsSitNFe
from nfelib.v4_00 import distDFeInt
from nfelib.v4_00 import retDistDFeInt
from nfelib.v4_00 import retEnvEvento
from nfelib.v4_00 import retEnvEventoCancNFe
from nfelib.v4_00 import retEnvCCe
from nfelib.v4_00 import retEnvConfRecebto
from nfelib.v4_00 import retConsCad


def test_in_out_leiauteNFe():
    path = 'tests/nfe/v4_00/leiauteNFe'
    for filename in os.listdir(path):
        # primeiro filtramos a root tag e a possivel assinatura:
        subtree = nfe_sub.parsexml_('%s/%s' % (path, filename,))
        inputfile = 'tests/input.xml'
        subtree.write(inputfile, encoding='utf-8')

        # agora vamos importar o XML da nota e transforma-lo em objeto Python:
        obj = nfe_sub.parse(inputfile)#'%s/%s' % (path, filename,))
        # agora podemos trabalhar em cima do objeto e fazer operaçoes como:
        obj.infNFe.emit.CNPJ

        outputfile = 'tests/output.xml'
        with open(outputfile, 'w') as f:
            nfe_sub.export(obj, nfeProc=False, stream=f)

        diff = main.diff_files(inputfile, outputfile)
        print(diff)
        assert len(diff) == 0

def test_in_out_leiauteInutNFe():
    path = 'tests/nfe/v4_00/leiauteInutNFe'
    for filename in os.listdir(path):
        inputfile = '%s/%s' % (path, filename,)
        doc = retInutNFe.parsexml_(inputfile, None)
        obj = retInutNFe.TInutNFe.factory().build(doc.getroot())

        outputfile = 'tests/output.xml'
        with open(outputfile, 'w') as f:
            obj.export(f, level=0, name_='inutNFe',
                namespacedef_='xmlns="http://www.portalfiscal.inf.br/nfe"')

        diff = main.diff_files(inputfile, outputfile)
        print(diff)
        assert len(diff) == 0

def test_stat():
    raiz = retConsStatServ.TConsStatServ(
        versao='4.00',
        tpAmb='1',
        cUF='SP',
        xServ='STATUS',
    )
    raiz.export(sys.stdout, 0)

def test_cons_sit():
    raiz = retConsSitNFe.TConsSitNFe(
        versao='4.00',
        tpAmb='1',
        xServ='CONSULTAR',
        chNFe='NFe35180803102452000172550010000474641681223493',
    )
    raiz.export(sys.stdout, 0)

def test_distDFe():
    distDFeInt.distNSUType.factory()
    distDFeInt.consNSUType.factory()
    distDFeInt.consChNFeType.factory()
    distDFeInt.distDFeInt()
    retDistDFeInt.retDistDFeInt.factory()

def test_evento_generico():
    raiz = retEnvEvento.TEnvEvento(versao="1.00", idLote='42')
    raiz.export(sys.stdout, 0)
    retEnvEvento.TRetEnvEvento()

def test_evento_cancelamento():
    retEnvEventoCancNFe.TEvento()
    retEnvEventoCancNFe.infEventoType()
    retEnvEventoCancNFe.detEventoType()

def test_cce():
    retEnvCCe.infEventoType()
    retEnvCCe.detEventoType()

def test_in_out_leiauteCCe():
    path = 'tests/cce/v1_00/leiauteCCe'
    for filename in os.listdir(path):
        inputfile = '%s/%s' % (path, filename,)
        doc = retInutNFe.parsexml_(inputfile, None)
        obj = retEnvCCe.TEvento.factory().build(doc.getroot())

        outputfile = 'tests/output.xml'
        with open(outputfile, 'w') as f:
            obj.export(f, level=0, name_='evento',
                namespacedef_='xmlns="http://www.portalfiscal.inf.br/nfe"')

        diff = main.diff_files(inputfile, outputfile)
        print(diff)
        assert len(diff) == 0

def test_mde():
    retEnvConfRecebto.TEvento()
    retEnvConfRecebto.infEventoType()
    retEnvConfRecebto.detEventoType()
    retEnvConfRecebto.tpEventoType('210200')
    retEnvConfRecebto.descEventoType('Confirmacao da Operacao')

def test_consulta():
    infCons = retConsCad.infConsType(
        xServ='CONS-CAD',
        UF='SP',
        IE='alguma IE',
        CNPJ='algum CNPJ',
        CPF=None,
    )
    raiz = retConsCad.TConsCad(
        versao='2.00',
        infCons=infCons,
    )
    raiz.original_tagname_ = 'ConsCad'

def test_init_all():
    for mod in [nfe, retInutNFe, distDFeInt, retDistDFeInt, retEnvEvento,
            retEnvEventoCancNFe, retEnvCCe, retEnvConfRecebto, retConsCad]:
        for class_name in mod.__all__:
            cls = getattr(mod, class_name)
            if issubclass(cls, mod.GeneratedsSuper):
                cls()
