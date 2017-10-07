#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Usage:
    python example01.py [options] instancedoc.xml
Options:
    -h, --help      Display this help message.
    -v, --verbose   Show additional information.
    -n NAME, --name=NAME
                    A name.
Example:
    python example01.py ../sample_data/some_instance_doc.xml
"""


#
# Imports

import sys
import getopt
import {{schema_name}}lib


#
# Globals and constants


#
# Functions for external use


#
# Classes



#
# Functions for internal use and testing

def parse(inFileName):
    doc = {{schema_name}}lib.parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = {{schema_name}}lib.get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'libraryRefType'
        rootClass = libraryRefType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
##     sys.stdout.write('<?xml version="1.0" ?>\n')
##     rootObj.export(sys.stdout, 0, name_=rootTag, 
##         namespacedef_='')
    return rootObj




def test(inFileName, name, verbose):
    rootObj = parse(inFileName)
    #
    # Add some application specific code here.
    #
    rootObj.export(sys.stdout, 0)



USAGE_TEXT = __doc__

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args, 'hn:', ['help',
            'verbose', 'name=', ])
    except:
        usage()
    verbose = False
    name = 'nobody'
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt in ('-v', '--verbose'):
            verbose = True
        elif opt in ('-n', '--name'):
            name = val
    if len(args) != 1:
        usage()
    inFileName = args[0]
    test(inFileName, name, verbose)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


