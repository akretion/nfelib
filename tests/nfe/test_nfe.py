# Copyright (C) 2019 - TODAY Raphaël Valyi - Akretion

import os
import sys
from os import path
import importlib
import inspect
from enum import EnumMeta
from xmldiff import main

sys.path.append(path.join(path.dirname(__file__), "..", "nfelib"))

from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from pathlib import Path
import pkgutil

from nfelib.bindings.nfe.v4_0 import leiaute_nfe_v4_00
from nfelib.bindings.nfe.v4_0.leiaute_cons_stat_serv_v4_00 import TconsStatServ
from nfelib.bindings.nfe.v4_0.leiaute_cons_sit_nfe_v4_00 import TconsSitNfe

from nfelib.bindings.nfe_dist_dfe.v1_0.dist_dfe_int_v1_01 import DistDfeInt

from nfelib.bindings.nfe_evento_generico.v1_0.leiaute_evento_v1_00 import TenvEvento


def test_in_out_leiauteNFe():
    path = os.path.join("nfelib", "samples", "nfe", "v4_0", "leiauteNFe")
    for filename in os.listdir(path):
        input_file = os.path.join(path, filename)
        parser = XmlParser()
        obj = parser.from_path(Path(input_file))
        serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
        xml = serializer.render(
            obj=obj, ns_map={None: "http://www.portalfiscal.inf.br/nfe"}
        )
        # agora podemos trabalhar em cima do objeto e fazer operaçoes como:
        #        obj.infNFe.emit.CNPJ

        output_file = "tests/output_nfe2.xml"
        with open(output_file, "w") as f:
            f.write(xml)

        diff = main.diff_files(input_file, output_file)
        assert len(diff) == 0
        if len(diff) != 0:
            break


def test_in_out_leiauteInutNFe():
    path = os.path.join("nfelib", "samples", "nfe", "v4_0", "leiauteInutNFe")
    for filename in os.listdir(path):
        input_file = os.path.join(path, filename)
        parser = XmlParser()
        obj = parser.from_path(Path(input_file))
        serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
        xml = serializer.render(
            obj=obj, ns_map={None: "http://www.portalfiscal.inf.br/nfe"}
        )

        output_file = "tests/output.xml"
        with open(output_file, "w") as f:
            f.write(xml)

        diff = main.diff_files(input_file, output_file)
        assert len(diff) == 0


def test_stat():
    obj = TconsStatServ(
        versao="4.00",
        tpAmb="1",
        cUF="12",
        xServ="STATUS",
    )
    serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
    xml = serializer.render(obj=obj)


def test_cons_sit():
    obj = TconsSitNfe(
        versao="4.00",
        tpAmb="1",
        xServ="CONSULTAR",
        chNFe="NFe35180803102452000172550010000474641681223493",
    )
    serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
    xml = serializer.render(obj=obj)


def test_distDFe():
    obj = DistDfeInt(
        versao="4.00",
        tpAmb="1",
        cUFAutor="SP",
        distNSU=DistDfeInt.DistNsu(
            ultNSU="35180803102452000172550010000474641681223493"
        ),
        consNSU=DistDfeInt.ConsNsu(NSU="35180803102452000172550010000474641681223493"),
    )
    serializer = XmlSerializer(config=SerializerConfig(pretty_print=True))
    xml = serializer.render(obj=obj)


def test_evento_generico():
    obj = TenvEvento(versao="1.00", idLote="42")
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
