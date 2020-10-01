# Copyright (C) 2019 - TODAY Raphaël Valyi - Akretion

import sys
import os
from lxml import etree as etree_
sys.path.append(os.path.dirname(__file__))
import retEnviNFe as supermod


def parsexml_(infile, parser=None, keep_signature=False, **kwargs):
    "accepts both NFe and nfeProc documents"
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    if doc.getroot().tag == '{http://www.portalfiscal.inf.br/nfe}nfeProc':
        root = doc.getroot()[0]
    else:
        root = doc.getroot()
    # remove Signature element before XML comparison
    if not keep_signature:
        for child in root:
            if child.tag in ["{http://www.w3.org/2000/09/xmldsig#}Signature",
                             "{http://www.w3.org/2000/09/xmldsig#}\
                             ds:Signature"]:
                root.remove(child)
    subtree = etree_.ElementTree(root)
    return subtree

#
# Globals
#

ExternalEncoding = ''

#
# Data representation classes
#


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = supermod.get_root_tag(rootNode)
    if rootClass is None:
        rootClass = supermod.TNFe
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        export(rootObj)
    return rootObj


def export(doc, nfeProc=True, stream=sys.stdout):
    stream.write('<?xml version="1.0" ?>\n')
    if nfeProc:
        stream.write('<nfeProc xmlns="http://www.portalfiscal.inf.br/nfe" \
                         versao="4.00">\n')
    doc.export(stream, 0, namespaceprefix_='', name_='NFe',
               namespacedef_='xmlns="http://www.portalfiscal.inf.br/nfe"')
    if nfeProc:
        # TODO deal with infProt
        stream.write('</nfeProc>\n')


USAGE_TEXT = """
Usage: python nfe_sub.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    main()
