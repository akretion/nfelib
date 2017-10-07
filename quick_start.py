#!/usr/bin/env python

"""
Create package directory structure and files from template library archive.

Replace schema name in files producing boiler plate.
The boiler plate will contain the following:
- project name = schema-name
- library-name = schema-name + 'lib'
"""


#
# Imports

import sys
from optparse import OptionParser
import re
import os


#
# Globals and constants

# List of files to be scanned
File_names = [
    'README.txt',
    'docs/conf.py',
    'docs/index.txt',
    'docs/intro.txt',
    'docs/module_contents.txt',
    'docs/Makefile',
    'docs/make.bat',
    'sample_code/README.txt',
    'sample_code/example01.py',
    'schemas/README.txt',
    ]

Schema_name_pat = re.compile(r'{{\w*(schema_name)\w*}}')

#
# Functions for external use



#
# Classes



#
# Functions for internal use and testing


## def transform_line(line, schema_name):
##     line, change_count = Schema_name_pat.subn(schema_name, line)
##     return line, change_count


def quick_start(options):
    schema_name = options.schema_name
    for filename in File_names:
        infile = open(filename, 'r')
        content = infile.read()
        infile.close()
        content, change_count = Schema_name_pat.subn(schema_name, content)
        if change_count > 0:
            outfile = open(filename, 'w')
            outfile.write(content)
            outfile.close()
    outfilename = '%sutils.py' % (schema_name, )
    os.rename('schema_name_utils.py', outfilename)


USAGE_TEXT = """
    python %prog [options] <archive.zip>
Example:
    python %prog --schema-name=collada templatelib-1.0a.zip"""

def usage(parser):
    parser.print_help()
    sys.exit(1)


def main():
    parser = OptionParser(__doc__ + USAGE_TEXT)
    parser.add_option("-s", "--schema-name",
        dest="schema_name", default=None, type='string',
        help="the name of the project and of your schema")
##     parser.add_option("-f", "--force", action="store_true",
##         dest="force", default=False,
##         help="force overwrite without asking")
##     parser.add_option("--spec-file-name",
##         dest="spec_file_name", default='', type='string',
##         help="read list of input/output files from spec file")
    (options, args) = parser.parse_args()
    if len(args) == 0 and options.schema_name is not None:
        quick_start(options)
    else:
        usage(parser)

        
if __name__ == "__main__":
    #import pdb; pdb.set_trace()
    main()

