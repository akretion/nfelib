# Copyright (C) 2019 - TODAY Raphaël Valyi - Akretion

import os
import sys
from os import path
from xmldiff import main
sys.path.append(path.join(path.dirname(__file__), '..', 'nfelib'))

from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from pathlib import Path

from nfelib.bindings.nfe.v4_0.proc_nfe_v4_00  import NfeProc
from nfelib.bindings.nfe.v4_0.inut_nfe_v4_00 import InutNfe
from nfelib.bindings.nfe.v4_0.leiaute_cons_stat_serv_v4_00 import TconsStatServ
from nfelib.bindings.nfe.v4_0.leiaute_cons_sit_nfe_v4_00 import TconsSitNfe

from nfelib.bindings.nfe_dist_dfe.v1_0.dist_dfe_int_v1_01 import DistDfeInt

from nfelib.bindings.nfe_evento_generico.v1_0.leiaute_evento_v1_00 import TenvEvento

def test_in_out_leiauteNFe():
    path = os.path.join("nfelib", "tests", "nfe", "v4_00", "leiauteNFe")
    for filename in os.listdir(path):
        input_file = os.path.join(path, filename)
        parser = XmlParser()
        obj = parser.from_path(Path(input_file), NfeProc)
        serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
        xml = serializer.render(
            obj=obj,
            ns_map={None:"http://www.portalfiscal.inf.br/nfe"}
        )

        # agora podemos trabalhar em cima do objeto e fazer operaçoes como:
        # TODO FIXME
#        obj.infNFe.emit.CNPJ

        output_file = 'nfelib/tests/output_nfe.xml'
        with open(output_file, 'w') as f:
            f.write(xml)

        diff = main.diff_files(input_file, output_file)
        assert len(diff) == 0
        if len(diff) != 0:
            break

def test_in_out_leiauteInutNFe():
    path = os.path.join("nfelib", "tests", "nfe", "v4_00", "leiauteInutNFe")
    for filename in os.listdir(path):
        input_file = os.path.join(path, filename)
        parser = XmlParser()
        obj = parser.from_path(Path(input_file), InutNfe)
        serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
        xml = serializer.render(
            obj=obj,
            ns_map={None:"http://www.portalfiscal.inf.br/nfe"}
        )

        # TODO FIXME
#        doc = retInutNFe.parsexml_(inputfile, None)
#        obj = retInutNFe.TInutNFe.factory().build(doc.getroot())

        output_file = 'nfelib/tests/output.xml'
        with open(output_file, 'w') as f:
            f.write(xml)

        diff = main.diff_files(input_file, output_file)
        assert len(diff) == 0

#        with open(outputfile, 'w') as f:
#            obj.export(f, level=0, name_='inutNFe',
#                namespacedef_='xmlns="http://www.portalfiscal.inf.br/nfe"')

def test_stat():
    obj = TconsStatServ(
        versao='4.00',
        tp_amb='1',
        c_uf='SP',
        x_serv='STATUS',
    )
    serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
    xml = serializer.render(obj=obj)

def test_cons_sit():
    obj = TconsSitNfe(
        versao='4.00',
        tp_amb='1',
        x_serv='CONSULTAR',
        ch_nfe='NFe35180803102452000172550010000474641681223493',
    )
    serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
    xml = serializer.render(obj=obj)

def test_distDFe():
    obj = DistDfeInt(
        versao='4.00',
        tp_amb='1',
        c_ufautor='SP',
        dist_nsu=DistDfeInt.DistNsu(
            ult_nsu='35180803102452000172550010000474641681223493'
        ),
        cons_nsu=DistDfeInt.ConsNsu(
            nsu='35180803102452000172550010000474641681223493'
        ),
    )
    serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
    xml = serializer.render(obj=obj)

def test_evento_generico():
    obj = TenvEvento(versao="1.00", id_lote='42')
    serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
    xml = serializer.render(obj=obj)

# def test_evento_cancelamento():
#     retEnvEventoCancNFe.TEvento()
#     retEnvEventoCancNFe.infEventoType()
#     retEnvEventoCancNFe.detEventoType()

# def test_cce():
#     retEnvCCe.infEventoType()
#     retEnvCCe.detEventoType()

# def test_in_out_leiauteCCe():
#     path = 'tests/cce/v1_00/leiauteCCe'
#     for filename in os.listdir(path):
#         inputfile = '%s/%s' % (path, filename,)
#         doc = retInutNFe.parsexml_(inputfile, None)
#         obj = retEnvCCe.TEvento.factory().build(doc.getroot())

#         outputfile = 'tests/output.xml'
#         with open(outputfile, 'w') as f:
#             obj.export(f, level=0, name_='evento',
#                 namespacedef_='xmlns="http://www.portalfiscal.inf.br/nfe"')

#         diff = main.diff_files(inputfile, outputfile)
#         print(diff)
#         assert len(diff) == 0

# def test_mde():
#     retEnvConfRecebto.TEvento()
#     retEnvConfRecebto.infEventoType()
#     retEnvConfRecebto.detEventoType()
#     retEnvConfRecebto.tpEventoType('210200')
#     retEnvConfRecebto.descEventoType('Confirmacao da Operacao')

# def test_consulta():
#     infCons = retConsCad.infConsType(
#         xServ='CONS-CAD',
#         UF='SP',
#         IE='alguma IE',
#         CNPJ='algum CNPJ',
#         CPF=None,
#     )
#     obj = retConsCad.TConsCad(
#         versao='2.00',
#         infCons=infCons,
#     )
#     obj.original_tagname_ = 'ConsCad'

# def test_init_all():
#     for mod in [nfe, retInutNFe, distDFeInt, retDistDFeInt, retEnvEvento,
#             retEnvEventoCancNFe, retEnvCCe, retEnvConfRecebto, retConsCad]:
#         for class_name in mod.__all__:
#             cls = getattr(mod, class_name)
#             if issubclass(cls, mod.GeneratedsSuper):
#                 cls()
