#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utility functions, classes, globals, etc for {{schema_name}}lib
"""


#
# Imports

import sys


#
# Globals and constants


#
# Functions for external use


#
# Classes



#
# Functions for internal use and testing

def test():
    pass



USAGE_TEXT = __doc__

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 0:
        usage()
    test()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()



