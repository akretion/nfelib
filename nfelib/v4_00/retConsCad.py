#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated  by generateDS.py version 2.38.6.
# Python 3.8.5 (default, Jul 28 2020, 12:59:40)  [GCC 9.3.0]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('--no-dates', '')
#   ('--member-specs', 'list')
#   ('--use-getter-setter', 'none')
#   ('-f', '')
#   ('-o', '/home/rvalyi/DEV/nfelib2/nfelib/v4_00/retConsCad.py')
#
# Command line arguments:
#   /tmp/generated/schemas/nfe/v4_00/retConsCad_v2.00.xsd
#
# Command line:
#   /usr/local/bin/generateDS.py --no-namespace-defs --no-dates --member-specs="list" --use-getter-setter="none" -f -o "/home/rvalyi/DEV/nfelib2/nfelib/v4_00/retConsCad.py" /tmp/generated/schemas/nfe/v4_00/retConsCad_v2.00.xsd
#
# Current working directory (os.getcwd()):
#   v4_00
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ModulenotfoundExp_ :
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    
    class GeneratedsSuper(object):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer values')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return_value = '%s' % input_data
            if '.' in return_value:
                return_value = return_value.rstrip('0')
                if return_value.endswith('.'):
                    return_value = return_value.rstrip('.')
            return return_value
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return ' '.join([self.gds_format_decimal(item) for item in input_data])
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=0, max_occurs=1, required=None):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None :
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()))
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        min_occurs, length))
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(),
                        max_occurs, length))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return all(x == y for x, y in zip_longest(
                filter(excl_select_objs_, self.__dict__.items()),
                filter(excl_select_objs_, other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element, mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self, mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class TAmb(str, Enum):
    """Tipo Ambiente"""
    _1='1'
    _2='2'


class TCodUfIBGE(str, Enum):
    """Tipo Código da UF da tabela do IBGE"""
    _1_1='11'
    _1_2='12'
    _1_3='13'
    _1_4='14'
    _1_5='15'
    _1_6='16'
    _1_7='17'
    _2_1='21'
    _2_2='22'
    _2_3='23'
    _2_4='24'
    _2_5='25'
    _2_6='26'
    _2_7='27'
    _2_8='28'
    _2_9='29'
    _3_1='31'
    _3_2='32'
    _3_3='33'
    _3_5='35'
    _4_1='41'
    _4_2='42'
    _4_3='43'
    _5_0='50'
    _5_1='51'
    _5_2='52'
    _5_3='53'


class TMod(str, Enum):
    """Tipo Modelo Documento Fiscal"""
    _5_5='55'


class TUf(str, Enum):
    """Tipo Sigla da UF"""
    AC='AC'
    AL='AL'
    AM='AM'
    AP='AP'
    BA='BA'
    CE='CE'
    DF='DF'
    ES='ES'
    GO='GO'
    MA='MA'
    MG='MG'
    MS='MS'
    MT='MT'
    PA='PA'
    PB='PB'
    PE='PE'
    PI='PI'
    PR='PR'
    RJ='RJ'
    RN='RN'
    RO='RO'
    RR='RR'
    RS='RS'
    SC='SC'
    SE='SE'
    SP='SP'
    TO='TO'
    EX='EX'


class TUfCons(str, Enum):
    """Tipo Sigla da UF consultada"""
    AC='AC'
    AL='AL'
    AM='AM'
    AP='AP'
    BA='BA'
    CE='CE'
    DF='DF'
    ES='ES'
    GO='GO'
    MA='MA'
    MG='MG'
    MS='MS'
    MT='MT'
    PA='PA'
    PB='PB'
    PE='PE'
    PI='PI'
    PR='PR'
    RJ='RJ'
    RN='RN'
    RO='RO'
    RR='RR'
    RS='RS'
    SC='SC'
    SE='SE'
    SP='SP'
    TO='TO'
    SU='SU'


class TUfEmi(str, Enum):
    """Tipo Sigla da UF de emissor // acrescentado em 24/10/08"""
    AC='AC'
    AL='AL'
    AM='AM'
    AP='AP'
    BA='BA'
    CE='CE'
    DF='DF'
    ES='ES'
    GO='GO'
    MA='MA'
    MG='MG'
    MS='MS'
    MT='MT'
    PA='PA'
    PB='PB'
    PE='PE'
    PI='PI'
    PR='PR'
    RJ='RJ'
    RN='RN'
    RO='RO'
    RR='RR'
    RS='RS'
    SC='SC'
    SE='SE'
    SP='SP'
    TO='TO'


class Tpais(str, Enum):
    """Tipo Código do Pais
    // PL_005d - 11/08/09
    eliminado:
    4235-LEBUAN, ILHAS -
    acrescentado:
    7200 SAO TOME E PRINCIPE, ILHAS,
    8958 ZONA DO CANAL DO PANAMA
    9903 PROVISAO DE NAVIOS E AERONAVES
    9946 A DESIGNAR
    9950 BANCOS CENTRAIS
    9970 ORGANIZACOES INTERNACIONAIS
    // PL_005b - 24/10/08
    // Acrescentado:
    4235 - LEBUAN,ILHAS
    4885 - MAYOTTE (ILHAS FRANCESAS)
    // NT2011/004
    acrescentado a tabela de paises
    //PL_006t - 21/03/2014
    acrescentado:
    5780 - Palestina
    7600 - Sudão do Sul"""
    _1_32='132'
    _1_75='175'
    _2_30='230'
    _3_10='310'
    _3_70='370'
    _4_00='400'
    _4_18='418'
    _4_34='434'
    _4_77='477'
    _5_31='531'
    _5_90='590'
    _6_39='639'
    _6_47='647'
    _6_55='655'
    _6_98='698'
    _7_28='728'
    _7_36='736'
    _7_79='779'
    _8_09='809'
    _8_17='817'
    _8_33='833'
    _8_50='850'
    _8_76='876'
    _8_84='884'
    _9_06='906'
    _9_30='930'
    _9_73='973'
    _9_81='981'
    _0_132='0132'
    _0_175='0175'
    _0_230='0230'
    _0_310='0310'
    _0_370='0370'
    _0_400='0400'
    _0_418='0418'
    _0_434='0434'
    _0_477='0477'
    _0_531='0531'
    _0_590='0590'
    _0_639='0639'
    _0_647='0647'
    _0_655='0655'
    _0_698='0698'
    _0_728='0728'
    _0_736='0736'
    _0_779='0779'
    _0_809='0809'
    _0_817='0817'
    _0_833='0833'
    _0_850='0850'
    _0_876='0876'
    _0_884='0884'
    _0_906='0906'
    _0_930='0930'
    _0_973='0973'
    _0_981='0981'
    _1_015='1015'
    _1_058='1058'
    _1_082='1082'
    _1_112='1112'
    _1_155='1155'
    _1_198='1198'
    _1_279='1279'
    _1_376='1376'
    _1_414='1414'
    _1_457='1457'
    _1_490='1490'
    _1_504='1504'
    _1_508='1508'
    _1_511='1511'
    _1_538='1538'
    _1_546='1546'
    _1_589='1589'
    _1_600='1600'
    _1_619='1619'
    _1_635='1635'
    _1_651='1651'
    _1_694='1694'
    _1_732='1732'
    _1_775='1775'
    _1_830='1830'
    _1_872='1872'
    _1_902='1902'
    _1_937='1937'
    _1_953='1953'
    _1_961='1961'
    _1_988='1988'
    _1_996='1996'
    _2_291='2291'
    _2_321='2321'
    _2_356='2356'
    _2_399='2399'
    _2_402='2402'
    _2_437='2437'
    _2_445='2445'
    _2_453='2453'
    _2_461='2461'
    _2_470='2470'
    _2_496='2496'
    _2_518='2518'
    _2_534='2534'
    _2_550='2550'
    _2_593='2593'
    _2_674='2674'
    _2_712='2712'
    _2_755='2755'
    _2_810='2810'
    _2_852='2852'
    _2_895='2895'
    _2_917='2917'
    _2_933='2933'
    _2_976='2976'
    _3_018='3018'
    _3_050='3050'
    _3_093='3093'
    _3_131='3131'
    _3_174='3174'
    _3_255='3255'
    _3_298='3298'
    _3_310='3310'
    _3_344='3344'
    _3_379='3379'
    _3_417='3417'
    _3_450='3450'
    _3_514='3514'
    _3_557='3557'
    _3_573='3573'
    _3_595='3595'
    _3_611='3611'
    _3_654='3654'
    _3_697='3697'
    _3_727='3727'
    _3_751='3751'
    _3_794='3794'
    _3_832='3832'
    _3_867='3867'
    _3_913='3913'
    _3_964='3964'
    _3_999='3999'
    _4_030='4030'
    _4_111='4111'
    _4_200='4200'
    _4_235='4235'
    _4_260='4260'
    _4_278='4278'
    _4_316='4316'
    _4_340='4340'
    _4_383='4383'
    _4_405='4405'
    _4_421='4421'
    _4_456='4456'
    _4_472='4472'
    _4_499='4499'
    _4_502='4502'
    _4_525='4525'
    _4_553='4553'
    _4_588='4588'
    _4_618='4618'
    _4_642='4642'
    _4_677='4677'
    _4_723='4723'
    _4_740='4740'
    _4_766='4766'
    _4_774='4774'
    _4_855='4855'
    _4_880='4880'
    _4_885='4885'
    _4_901='4901'
    _4_936='4936'
    _4_944='4944'
    _4_952='4952'
    _4_979='4979'
    _4_985='4985'
    _4_995='4995'
    _5_010='5010'
    _5_053='5053'
    _5_070='5070'
    _5_088='5088'
    _5_118='5118'
    _5_177='5177'
    _5_215='5215'
    _5_258='5258'
    _5_282='5282'
    _5_312='5312'
    _5_355='5355'
    _5_380='5380'
    _5_428='5428'
    _5_452='5452'
    _5_487='5487'
    _5_517='5517'
    _5_568='5568'
    _5_665='5665'
    _5_738='5738'
    _5_754='5754'
    _5_762='5762'
    _5_780='5780'
    _5_800='5800'
    _5_860='5860'
    _5_894='5894'
    _5_932='5932'
    _5_991='5991'
    _6_033='6033'
    _6_076='6076'
    _6_114='6114'
    _6_238='6238'
    _6_254='6254'
    _6_289='6289'
    _6_408='6408'
    _6_475='6475'
    _6_602='6602'
    _6_653='6653'
    _6_700='6700'
    _6_750='6750'
    _6_769='6769'
    _6_777='6777'
    _6_781='6781'
    _6_858='6858'
    _6_874='6874'
    _6_904='6904'
    _6_912='6912'
    _6_955='6955'
    _6_971='6971'
    _7_005='7005'
    _7_056='7056'
    _7_102='7102'
    _7_153='7153'
    _7_200='7200'
    _7_285='7285'
    _7_315='7315'
    _7_358='7358'
    _7_370='7370'
    _7_412='7412'
    _7_447='7447'
    _7_480='7480'
    _7_501='7501'
    _7_544='7544'
    _7_560='7560'
    _7_595='7595'
    _7_600='7600'
    _7_641='7641'
    _7_676='7676'
    _7_706='7706'
    _7_722='7722'
    _7_765='7765'
    _7_803='7803'
    _7_820='7820'
    _7_838='7838'
    _7_889='7889'
    _7_919='7919'
    _7_951='7951'
    _8_001='8001'
    _8_052='8052'
    _8_109='8109'
    _8_150='8150'
    _8_206='8206'
    _8_230='8230'
    _8_249='8249'
    _8_273='8273'
    _8_281='8281'
    _8_311='8311'
    _8_338='8338'
    _8_451='8451'
    _8_478='8478'
    _8_486='8486'
    _8_508='8508'
    _8_583='8583'
    _8_630='8630'
    _8_664='8664'
    _8_702='8702'
    _8_737='8737'
    _8_885='8885'
    _8_907='8907'
    _8_958='8958'
    _9_903='9903'
    _9_946='9946'
    _9_950='9950'
    _9_970='9970'


class cSitType(str, Enum):
    """Situação cadastral do contribuinte:
    0 - não habilitado
    1 - habilitado"""
    _0='0'
    _1='1'


class indCredCTeType(str, Enum):
    """Indicador de contribuinte credenciado a emitir CT-e.
    0 - Não credenciado para emissão da CT-e;
    1 - Credenciado;
    2 - Credenciado com obrigatoriedade para todas operações;
    3 - Credenciado com obrigatoriedade parcial;
    4 – a SEFAZ não fornece a informação.
    Este indicador significa apenas que o contribuinte é credenciado para
    emitir CT-e na SEFAZ consultada."""
    _0='0'
    _1='1'
    _2='2'
    _3='3'
    _4='4'


class indCredNFeType(str, Enum):
    """Indicador de contribuinte credenciado a emitir NF-e.
    0 - Não credenciado para emissão da NF-e;
    1 - Credenciado;
    2 - Credenciado com obrigatoriedade para todas operações;
    3 - Credenciado com obrigatoriedade parcial;
    4 – a SEFAZ não fornece a informação.
    Este indicador significa apenas que o contribuinte é credenciado para
    emitir NF-e na SEFAZ consultada."""
    _0='0'
    _1='1'
    _2='2'
    _3='3'
    _4='4'


class xServType(str, Enum):
    """Serviço Solicitado"""
    CONSCAD='CONS-CAD'


class TConsCad(GeneratedsSuper):
    """Tipo Pedido de Consulta de cadastro de contribuintes"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('versao', 'TVerConsCad', 0, 0, {'use': 'required'}),
        MemberSpec_('infCons', 'infConsType', 0, 0, {'name': 'infCons', 'type': 'infConsType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, versao=None, infCons=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.versao = _cast(None, versao)
        self.versao_nsprefix_ = None
        self.infCons = infCons
        self.infCons_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TConsCad)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TConsCad.subclass:
            return TConsCad.subclass(*args_, **kwargs_)
        else:
            return TConsCad(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TVerConsCad(self, value):
        # Validate type TVerConsCad, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TVerConsCad_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TVerConsCad_patterns_, ))
    validate_TVerConsCad_patterns_ = [['^(2\\.00)$']]
    def hasContent_(self):
        if (
            self.infCons is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TConsCad', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TConsCad')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TConsCad':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TConsCad')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TConsCad', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TConsCad'):
        if self.versao is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            outfile.write(' versao=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.versao), input_name='versao')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TConsCad', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.infCons is not None:
            namespaceprefix_ = self.infCons_nsprefix_ + ':' if (UseCapturedNS_ and self.infCons_nsprefix_) else ''
            self.infCons.export(outfile, level, namespaceprefix_, namespacedef_='', name_='infCons', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('versao', node)
        if value is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            self.versao = value
            self.versao = ' '.join(self.versao.split())
            self.validate_TVerConsCad(self.versao)    # validate type TVerConsCad
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'infCons':
            obj_ = infConsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.infCons = obj_
            obj_.original_tagname_ = 'infCons'
# end class TConsCad


class TRetConsCad(GeneratedsSuper):
    """Tipo Retorno Pedido de Consulta de cadastro de contribuintes"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('versao', 'TVerConsCad', 0, 0, {'use': 'required'}),
        MemberSpec_('infCons', 'infConsType1', 0, 0, {'name': 'infCons', 'type': 'infConsType1'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, versao=None, infCons=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.versao = _cast(None, versao)
        self.versao_nsprefix_ = None
        self.infCons = infCons
        self.infCons_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TRetConsCad)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TRetConsCad.subclass:
            return TRetConsCad.subclass(*args_, **kwargs_)
        else:
            return TRetConsCad(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TVerConsCad(self, value):
        # Validate type TVerConsCad, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TVerConsCad_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TVerConsCad_patterns_, ))
    validate_TVerConsCad_patterns_ = [['^(2\\.00)$']]
    def hasContent_(self):
        if (
            self.infCons is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TRetConsCad', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TRetConsCad')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TRetConsCad':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TRetConsCad')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TRetConsCad', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TRetConsCad'):
        if self.versao is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            outfile.write(' versao=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.versao), input_name='versao')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TRetConsCad', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.infCons is not None:
            namespaceprefix_ = self.infCons_nsprefix_ + ':' if (UseCapturedNS_ and self.infCons_nsprefix_) else ''
            self.infCons.export(outfile, level, namespaceprefix_, namespacedef_='', name_='infCons', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('versao', node)
        if value is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            self.versao = value
            self.versao = ' '.join(self.versao.split())
            self.validate_TVerConsCad(self.versao)    # validate type TVerConsCad
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'infCons':
            obj_ = infConsType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.infCons = obj_
            obj_.original_tagname_ = 'infCons'
# end class TRetConsCad


class TEndereco(GeneratedsSuper):
    """Tipo Dados do Endereço"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('xLgr', ['xLgrType', 'TString', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'xLgr', 'type': 'xs:string'}, None),
        MemberSpec_('nro', ['nroType', 'TString', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'nro', 'type': 'xs:string'}, None),
        MemberSpec_('xCpl', ['xCplType', 'TString', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'xCpl', 'type': 'xs:string'}, None),
        MemberSpec_('xBairro', ['xBairroType', 'TString', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'xBairro', 'type': 'xs:string'}, None),
        MemberSpec_('cMun', ['TCodMunIBGE', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'cMun', 'type': 'xs:string'}, None),
        MemberSpec_('xMun', ['xMunType', 'TString', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'xMun', 'type': 'xs:string'}, None),
        MemberSpec_('CEP', ['CEPType', 'xs:token'], 0, 1, {'minOccurs': '0', 'name': 'CEP', 'type': 'xs:token'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, xLgr=None, nro=None, xCpl=None, xBairro=None, cMun=None, xMun=None, CEP=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.xLgr = xLgr
        self.validate_xLgrType(self.xLgr)
        self.xLgr_nsprefix_ = None
        self.nro = nro
        self.validate_nroType(self.nro)
        self.nro_nsprefix_ = None
        self.xCpl = xCpl
        self.validate_xCplType(self.xCpl)
        self.xCpl_nsprefix_ = None
        self.xBairro = xBairro
        self.validate_xBairroType(self.xBairro)
        self.xBairro_nsprefix_ = None
        self.cMun = cMun
        self.validate_TCodMunIBGE(self.cMun)
        self.cMun_nsprefix_ = None
        self.xMun = xMun
        self.validate_xMunType(self.xMun)
        self.xMun_nsprefix_ = None
        self.CEP = CEP
        self.validate_CEPType(self.CEP)
        self.CEP_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TEndereco)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TEndereco.subclass:
            return TEndereco.subclass(*args_, **kwargs_)
        else:
            return TEndereco(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_xLgrType(self, value):
        result = True
        # Validate type xLgrType, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on xLgrType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on xLgrType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_xLgrType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_xLgrType_patterns_, ))
                result = False
        return result
    validate_xLgrType_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_nroType(self, value):
        result = True
        # Validate type nroType, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on nroType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on nroType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_nroType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nroType_patterns_, ))
                result = False
        return result
    validate_nroType_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_xCplType(self, value):
        result = True
        # Validate type xCplType, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on xCplType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on xCplType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_xCplType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_xCplType_patterns_, ))
                result = False
        return result
    validate_xCplType_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_xBairroType(self, value):
        result = True
        # Validate type xBairroType, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on xBairroType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on xBairroType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_xBairroType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_xBairroType_patterns_, ))
                result = False
        return result
    validate_xBairroType_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_TCodMunIBGE(self, value):
        result = True
        # Validate type TCodMunIBGE, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TCodMunIBGE_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TCodMunIBGE_patterns_, ))
                result = False
        return result
    validate_TCodMunIBGE_patterns_ = [['^([0-9]{7})$']]
    def validate_xMunType(self, value):
        result = True
        # Validate type xMunType, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on xMunType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on xMunType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_xMunType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_xMunType_patterns_, ))
                result = False
        return result
    validate_xMunType_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_CEPType(self, value):
        result = True
        # Validate type CEPType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_CEPType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_CEPType_patterns_, ))
                result = False
        return result
    validate_CEPType_patterns_ = [['^([0-9]{7,8})$']]
    def hasContent_(self):
        if (
            self.xLgr is not None or
            self.nro is not None or
            self.xCpl is not None or
            self.xBairro is not None or
            self.cMun is not None or
            self.xMun is not None or
            self.CEP is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TEndereco', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TEndereco')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TEndereco':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TEndereco')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TEndereco', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TEndereco'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TEndereco', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.xLgr is not None:
            namespaceprefix_ = self.xLgr_nsprefix_ + ':' if (UseCapturedNS_ and self.xLgr_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxLgr>%s</%sxLgr>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xLgr), input_name='xLgr')), namespaceprefix_ , eol_))
        if self.nro is not None:
            namespaceprefix_ = self.nro_nsprefix_ + ':' if (UseCapturedNS_ and self.nro_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snro>%s</%snro>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.nro), input_name='nro')), namespaceprefix_ , eol_))
        if self.xCpl is not None:
            namespaceprefix_ = self.xCpl_nsprefix_ + ':' if (UseCapturedNS_ and self.xCpl_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxCpl>%s</%sxCpl>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xCpl), input_name='xCpl')), namespaceprefix_ , eol_))
        if self.xBairro is not None:
            namespaceprefix_ = self.xBairro_nsprefix_ + ':' if (UseCapturedNS_ and self.xBairro_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxBairro>%s</%sxBairro>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xBairro), input_name='xBairro')), namespaceprefix_ , eol_))
        if self.cMun is not None:
            namespaceprefix_ = self.cMun_nsprefix_ + ':' if (UseCapturedNS_ and self.cMun_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scMun>%s</%scMun>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cMun), input_name='cMun')), namespaceprefix_ , eol_))
        if self.xMun is not None:
            namespaceprefix_ = self.xMun_nsprefix_ + ':' if (UseCapturedNS_ and self.xMun_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxMun>%s</%sxMun>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xMun), input_name='xMun')), namespaceprefix_ , eol_))
        if self.CEP is not None:
            namespaceprefix_ = self.CEP_nsprefix_ + ':' if (UseCapturedNS_ and self.CEP_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCEP>%s</%sCEP>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CEP), input_name='CEP')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'xLgr':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xLgr')
            value_ = self.gds_validate_string(value_, node, 'xLgr')
            self.xLgr = value_
            self.xLgr_nsprefix_ = child_.prefix
            # validate type xLgrType
            self.validate_xLgrType(self.xLgr)
        elif nodeName_ == 'nro':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nro')
            value_ = self.gds_validate_string(value_, node, 'nro')
            self.nro = value_
            self.nro_nsprefix_ = child_.prefix
            # validate type nroType
            self.validate_nroType(self.nro)
        elif nodeName_ == 'xCpl':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xCpl')
            value_ = self.gds_validate_string(value_, node, 'xCpl')
            self.xCpl = value_
            self.xCpl_nsprefix_ = child_.prefix
            # validate type xCplType
            self.validate_xCplType(self.xCpl)
        elif nodeName_ == 'xBairro':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xBairro')
            value_ = self.gds_validate_string(value_, node, 'xBairro')
            self.xBairro = value_
            self.xBairro_nsprefix_ = child_.prefix
            # validate type xBairroType
            self.validate_xBairroType(self.xBairro)
        elif nodeName_ == 'cMun':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cMun')
            value_ = self.gds_validate_string(value_, node, 'cMun')
            self.cMun = value_
            self.cMun_nsprefix_ = child_.prefix
            # validate type TCodMunIBGE
            self.validate_TCodMunIBGE(self.cMun)
        elif nodeName_ == 'xMun':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xMun')
            value_ = self.gds_validate_string(value_, node, 'xMun')
            self.xMun = value_
            self.xMun_nsprefix_ = child_.prefix
            # validate type xMunType
            self.validate_xMunType(self.xMun)
        elif nodeName_ == 'CEP':
            value_ = child_.text
            if value_:
                value_ = re_.sub(String_cleanup_pat_, " ", value_).strip()
            else:
                value_ = ""
            value_ = self.gds_parse_string(value_, node, 'CEP')
            value_ = self.gds_validate_string(value_, node, 'CEP')
            self.CEP = value_
            self.CEP_nsprefix_ = child_.prefix
            # validate type CEPType
            self.validate_CEPType(self.CEP)
# end class TEndereco


class infConsType(GeneratedsSuper):
    """Dados do Pedido de Consulta de cadastro de contribuintesargumento de
    pesquisa"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('xServ', ['xServType', 'TServ', 'nfe:TString'], 0, 0, {'name': 'xServ', 'type': 'xs:string'}, None),
        MemberSpec_('UF', ['TUfCons', 'xs:token'], 0, 0, {'name': 'UF', 'type': 'xs:token'}, None),
        MemberSpec_('IE', ['TIe', 'xs:string'], 0, 0, {'name': 'IE', 'type': 'xs:string'}, 1),
        MemberSpec_('CNPJ', ['TCnpjVar', 'xs:string'], 0, 0, {'name': 'CNPJ', 'type': 'xs:string'}, 1),
        MemberSpec_('CPF', ['TCpfVar', 'xs:string'], 0, 0, {'name': 'CPF', 'type': 'xs:string'}, 1),
    ]
    subclass = None
    superclass = None
    def __init__(self, xServ=None, UF=None, IE=None, CNPJ=None, CPF=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.xServ = xServ
        self.validate_xServType(self.xServ)
        self.xServ_nsprefix_ = None
        self.UF = UF
        self.validate_TUfCons(self.UF)
        self.UF_nsprefix_ = None
        self.IE = IE
        self.validate_TIe(self.IE)
        self.IE_nsprefix_ = None
        self.CNPJ = CNPJ
        self.validate_TCnpjVar(self.CNPJ)
        self.CNPJ_nsprefix_ = None
        self.CPF = CPF
        self.validate_TCpfVar(self.CPF)
        self.CPF_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, infConsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if infConsType.subclass:
            return infConsType.subclass(*args_, **kwargs_)
        else:
            return infConsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_xServType(self, value):
        result = True
        # Validate type xServType, a restriction on TServ.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['CONS-CAD']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on xServType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_xServType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_xServType_patterns_, ))
                result = False
        return result
    validate_xServType_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_TUfCons(self, value):
        result = True
        # Validate type TUfCons, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'SU']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TUfCons' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_TIe(self, value):
        result = True
        # Validate type TIe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TIe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TIe_patterns_, ))
                result = False
        return result
    validate_TIe_patterns_ = [['^([0-9]{2,14}|ISENTO)$']]
    def validate_TCnpjVar(self, value):
        result = True
        # Validate type TCnpjVar, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TCnpjVar_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TCnpjVar_patterns_, ))
                result = False
        return result
    validate_TCnpjVar_patterns_ = [['^([0-9]{3,14})$']]
    def validate_TCpfVar(self, value):
        result = True
        # Validate type TCpfVar, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TCpfVar_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TCpfVar_patterns_, ))
                result = False
        return result
    validate_TCpfVar_patterns_ = [['^([0-9]{3,11})$']]
    def hasContent_(self):
        if (
            self.xServ is not None or
            self.UF is not None or
            self.IE is not None or
            self.CNPJ is not None or
            self.CPF is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infConsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('infConsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'infConsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='infConsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='infConsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='infConsType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infConsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.xServ is not None:
            namespaceprefix_ = self.xServ_nsprefix_ + ':' if (UseCapturedNS_ and self.xServ_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxServ>%s</%sxServ>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xServ), input_name='xServ')), namespaceprefix_ , eol_))
        if self.UF is not None:
            namespaceprefix_ = self.UF_nsprefix_ + ':' if (UseCapturedNS_ and self.UF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sUF>%s</%sUF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.UF), input_name='UF')), namespaceprefix_ , eol_))
        if self.IE is not None:
            namespaceprefix_ = self.IE_nsprefix_ + ':' if (UseCapturedNS_ and self.IE_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIE>%s</%sIE>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.IE), input_name='IE')), namespaceprefix_ , eol_))
        if self.CNPJ is not None:
            namespaceprefix_ = self.CNPJ_nsprefix_ + ':' if (UseCapturedNS_ and self.CNPJ_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCNPJ>%s</%sCNPJ>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CNPJ), input_name='CNPJ')), namespaceprefix_ , eol_))
        if self.CPF is not None:
            namespaceprefix_ = self.CPF_nsprefix_ + ':' if (UseCapturedNS_ and self.CPF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCPF>%s</%sCPF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CPF), input_name='CPF')), namespaceprefix_ , eol_))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'xServ':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xServ')
            value_ = self.gds_validate_string(value_, node, 'xServ')
            self.xServ = value_
            self.xServ_nsprefix_ = child_.prefix
            # validate type xServType
            self.validate_xServType(self.xServ)
        elif nodeName_ == 'UF':
            value_ = child_.text
            if value_:
                value_ = re_.sub(String_cleanup_pat_, " ", value_).strip()
            else:
                value_ = ""
            value_ = self.gds_parse_string(value_, node, 'UF')
            value_ = self.gds_validate_string(value_, node, 'UF')
            self.UF = value_
            self.UF_nsprefix_ = child_.prefix
            # validate type TUfCons
            self.validate_TUfCons(self.UF)
        elif nodeName_ == 'IE':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'IE')
            value_ = self.gds_validate_string(value_, node, 'IE')
            self.IE = value_
            self.IE_nsprefix_ = child_.prefix
            # validate type TIe
            self.validate_TIe(self.IE)
        elif nodeName_ == 'CNPJ':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CNPJ')
            value_ = self.gds_validate_string(value_, node, 'CNPJ')
            self.CNPJ = value_
            self.CNPJ_nsprefix_ = child_.prefix
            # validate type TCnpjVar
            self.validate_TCnpjVar(self.CNPJ)
        elif nodeName_ == 'CPF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CPF')
            value_ = self.gds_validate_string(value_, node, 'CPF')
            self.CPF = value_
            self.CPF_nsprefix_ = child_.prefix
            # validate type TCpfVar
            self.validate_TCpfVar(self.CPF)
# end class infConsType


class infConsType1(GeneratedsSuper):
    """Dados do Resultado doDados do Pedido de Consulta de cadastro de
    contribuintesargumento de pesquisa"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('verAplic', ['TVerAplic', 'nfe:TString'], 0, 0, {'name': 'verAplic', 'type': 'xs:string'}, None),
        MemberSpec_('cStat', ['TStat', 'xs:string'], 0, 0, {'name': 'cStat', 'type': 'xs:string'}, None),
        MemberSpec_('xMotivo', ['TMotivo', 'nfe:TString'], 0, 0, {'name': 'xMotivo', 'type': 'xs:string'}, None),
        MemberSpec_('UF', ['TUfCons', 'xs:token'], 0, 0, {'name': 'UF', 'type': 'xs:token'}, None),
        MemberSpec_('IE', ['TIe', 'xs:string'], 0, 0, {'name': 'IE', 'type': 'xs:string'}, 2),
        MemberSpec_('CNPJ', ['TCnpjVar', 'xs:string'], 0, 0, {'name': 'CNPJ', 'type': 'xs:string'}, 2),
        MemberSpec_('CPF', ['TCpfVar', 'xs:string'], 0, 0, {'name': 'CPF', 'type': 'xs:string'}, 2),
        MemberSpec_('dhCons', 'xs:dateTime', 0, 0, {'name': 'dhCons', 'type': 'xs:dateTime'}, None),
        MemberSpec_('cUF', ['TCodUfIBGE', 'xs:string'], 0, 0, {'name': 'cUF', 'type': 'xs:string'}, None),
        MemberSpec_('infCad', 'infCadType', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'infCad', 'type': 'infCadType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, verAplic=None, cStat=None, xMotivo=None, UF=None, IE=None, CNPJ=None, CPF=None, dhCons=None, cUF=None, infCad=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.verAplic = verAplic
        self.validate_TVerAplic(self.verAplic)
        self.verAplic_nsprefix_ = None
        self.cStat = cStat
        self.validate_TStat(self.cStat)
        self.cStat_nsprefix_ = None
        self.xMotivo = xMotivo
        self.validate_TMotivo(self.xMotivo)
        self.xMotivo_nsprefix_ = None
        self.UF = UF
        self.validate_TUfCons(self.UF)
        self.UF_nsprefix_ = None
        self.IE = IE
        self.validate_TIe(self.IE)
        self.IE_nsprefix_ = None
        self.CNPJ = CNPJ
        self.validate_TCnpjVar(self.CNPJ)
        self.CNPJ_nsprefix_ = None
        self.CPF = CPF
        self.validate_TCpfVar(self.CPF)
        self.CPF_nsprefix_ = None
        if isinstance(dhCons, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dhCons, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = dhCons
        self.dhCons = initvalue_
        self.dhCons_nsprefix_ = None
        self.cUF = cUF
        self.validate_TCodUfIBGE(self.cUF)
        self.cUF_nsprefix_ = None
        if infCad is None:
            self.infCad = []
        else:
            self.infCad = infCad
        self.infCad_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, infConsType1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if infConsType1.subclass:
            return infConsType1.subclass(*args_, **kwargs_)
        else:
            return infConsType1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TVerAplic(self, value):
        result = True
        # Validate type TVerAplic, a restriction on nfe:TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TVerAplic' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TVerAplic' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TVerAplic_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TVerAplic_patterns_, ))
                result = False
        return result
    validate_TVerAplic_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_TStat(self, value):
        result = True
        # Validate type TStat, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TStat_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TStat_patterns_, ))
                result = False
        return result
    validate_TStat_patterns_ = [['^([0-9]{3})$']]
    def validate_TMotivo(self, value):
        result = True
        # Validate type TMotivo, a restriction on nfe:TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 255:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TMotivo' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TMotivo' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TMotivo_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TMotivo_patterns_, ))
                result = False
        return result
    validate_TMotivo_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_TUfCons(self, value):
        result = True
        # Validate type TUfCons, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'SU']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TUfCons' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_TIe(self, value):
        result = True
        # Validate type TIe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TIe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TIe_patterns_, ))
                result = False
        return result
    validate_TIe_patterns_ = [['^([0-9]{2,14}|ISENTO)$']]
    def validate_TCnpjVar(self, value):
        result = True
        # Validate type TCnpjVar, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TCnpjVar_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TCnpjVar_patterns_, ))
                result = False
        return result
    validate_TCnpjVar_patterns_ = [['^([0-9]{3,14})$']]
    def validate_TCpfVar(self, value):
        result = True
        # Validate type TCpfVar, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TCpfVar_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TCpfVar_patterns_, ))
                result = False
        return result
    validate_TCpfVar_patterns_ = [['^([0-9]{3,11})$']]
    def validate_TCodUfIBGE(self, value):
        result = True
        # Validate type TCodUfIBGE, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TCodUfIBGE' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.verAplic is not None or
            self.cStat is not None or
            self.xMotivo is not None or
            self.UF is not None or
            self.IE is not None or
            self.CNPJ is not None or
            self.CPF is not None or
            self.dhCons is not None or
            self.cUF is not None or
            self.infCad
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infConsType1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('infConsType1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'infConsType1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='infConsType1')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='infConsType1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='infConsType1'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infConsType1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.verAplic is not None:
            namespaceprefix_ = self.verAplic_nsprefix_ + ':' if (UseCapturedNS_ and self.verAplic_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sverAplic>%s</%sverAplic>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.verAplic), input_name='verAplic')), namespaceprefix_ , eol_))
        if self.cStat is not None:
            namespaceprefix_ = self.cStat_nsprefix_ + ':' if (UseCapturedNS_ and self.cStat_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scStat>%s</%scStat>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cStat), input_name='cStat')), namespaceprefix_ , eol_))
        if self.xMotivo is not None:
            namespaceprefix_ = self.xMotivo_nsprefix_ + ':' if (UseCapturedNS_ and self.xMotivo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxMotivo>%s</%sxMotivo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xMotivo), input_name='xMotivo')), namespaceprefix_ , eol_))
        if self.UF is not None:
            namespaceprefix_ = self.UF_nsprefix_ + ':' if (UseCapturedNS_ and self.UF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sUF>%s</%sUF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.UF), input_name='UF')), namespaceprefix_ , eol_))
        if self.IE is not None:
            namespaceprefix_ = self.IE_nsprefix_ + ':' if (UseCapturedNS_ and self.IE_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIE>%s</%sIE>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.IE), input_name='IE')), namespaceprefix_ , eol_))
        if self.CNPJ is not None:
            namespaceprefix_ = self.CNPJ_nsprefix_ + ':' if (UseCapturedNS_ and self.CNPJ_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCNPJ>%s</%sCNPJ>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CNPJ), input_name='CNPJ')), namespaceprefix_ , eol_))
        if self.CPF is not None:
            namespaceprefix_ = self.CPF_nsprefix_ + ':' if (UseCapturedNS_ and self.CPF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCPF>%s</%sCPF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CPF), input_name='CPF')), namespaceprefix_ , eol_))
        if self.dhCons is not None:
            namespaceprefix_ = self.dhCons_nsprefix_ + ':' if (UseCapturedNS_ and self.dhCons_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdhCons>%s</%sdhCons>%s' % (namespaceprefix_ , self.gds_format_datetime(self.dhCons, input_name='dhCons'), namespaceprefix_ , eol_))
        if self.cUF is not None:
            namespaceprefix_ = self.cUF_nsprefix_ + ':' if (UseCapturedNS_ and self.cUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scUF>%s</%scUF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cUF), input_name='cUF')), namespaceprefix_ , eol_))
        for infCad_ in self.infCad:
            namespaceprefix_ = self.infCad_nsprefix_ + ':' if (UseCapturedNS_ and self.infCad_nsprefix_) else ''
            infCad_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='infCad', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'verAplic':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'verAplic')
            value_ = self.gds_validate_string(value_, node, 'verAplic')
            self.verAplic = value_
            self.verAplic_nsprefix_ = child_.prefix
            # validate type TVerAplic
            self.validate_TVerAplic(self.verAplic)
        elif nodeName_ == 'cStat':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cStat')
            value_ = self.gds_validate_string(value_, node, 'cStat')
            self.cStat = value_
            self.cStat_nsprefix_ = child_.prefix
            # validate type TStat
            self.validate_TStat(self.cStat)
        elif nodeName_ == 'xMotivo':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xMotivo')
            value_ = self.gds_validate_string(value_, node, 'xMotivo')
            self.xMotivo = value_
            self.xMotivo_nsprefix_ = child_.prefix
            # validate type TMotivo
            self.validate_TMotivo(self.xMotivo)
        elif nodeName_ == 'UF':
            value_ = child_.text
            if value_:
                value_ = re_.sub(String_cleanup_pat_, " ", value_).strip()
            else:
                value_ = ""
            value_ = self.gds_parse_string(value_, node, 'UF')
            value_ = self.gds_validate_string(value_, node, 'UF')
            self.UF = value_
            self.UF_nsprefix_ = child_.prefix
            # validate type TUfCons
            self.validate_TUfCons(self.UF)
        elif nodeName_ == 'IE':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'IE')
            value_ = self.gds_validate_string(value_, node, 'IE')
            self.IE = value_
            self.IE_nsprefix_ = child_.prefix
            # validate type TIe
            self.validate_TIe(self.IE)
        elif nodeName_ == 'CNPJ':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CNPJ')
            value_ = self.gds_validate_string(value_, node, 'CNPJ')
            self.CNPJ = value_
            self.CNPJ_nsprefix_ = child_.prefix
            # validate type TCnpjVar
            self.validate_TCnpjVar(self.CNPJ)
        elif nodeName_ == 'CPF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CPF')
            value_ = self.gds_validate_string(value_, node, 'CPF')
            self.CPF = value_
            self.CPF_nsprefix_ = child_.prefix
            # validate type TCpfVar
            self.validate_TCpfVar(self.CPF)
        elif nodeName_ == 'dhCons':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.dhCons = dval_
            self.dhCons_nsprefix_ = child_.prefix
        elif nodeName_ == 'cUF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cUF')
            value_ = self.gds_validate_string(value_, node, 'cUF')
            self.cUF = value_
            self.cUF_nsprefix_ = child_.prefix
            # validate type TCodUfIBGE
            self.validate_TCodUfIBGE(self.cUF)
        elif nodeName_ == 'infCad':
            obj_ = infCadType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.infCad.append(obj_)
            obj_.original_tagname_ = 'infCad'
# end class infConsType1


class infCadType(GeneratedsSuper):
    """Informações cadastrais do contribuinte consultado"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('IE', ['TIe', 'xs:string'], 0, 0, {'name': 'IE', 'type': 'xs:string'}, None),
        MemberSpec_('CNPJ', ['TCnpjVar', 'xs:string'], 0, 0, {'name': 'CNPJ', 'type': 'xs:string'}, 3),
        MemberSpec_('CPF', ['TCpfVar', 'xs:string'], 0, 0, {'name': 'CPF', 'type': 'xs:string'}, 3),
        MemberSpec_('UF', ['TUf', 'xs:string'], 0, 0, {'name': 'UF', 'type': 'xs:string'}, None),
        MemberSpec_('cSit', ['cSitType', 'xs:token'], 0, 0, {'name': 'cSit', 'type': 'xs:token'}, None),
        MemberSpec_('indCredNFe', ['indCredNFeType', 'xs:string'], 0, 0, {'name': 'indCredNFe', 'type': 'xs:string'}, None),
        MemberSpec_('indCredCTe', ['indCredCTeType', 'xs:string'], 0, 0, {'name': 'indCredCTe', 'type': 'xs:string'}, None),
        MemberSpec_('xNome', ['xNomeType', 'TString', 'xs:string'], 0, 0, {'name': 'xNome', 'type': 'xs:string'}, None),
        MemberSpec_('xFant', ['xFantType', 'TString', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'xFant', 'type': 'xs:string'}, None),
        MemberSpec_('xRegApur', ['xRegApurType', 'xs:token'], 0, 1, {'minOccurs': '0', 'name': 'xRegApur', 'type': 'xs:token'}, None),
        MemberSpec_('CNAE', ['CNAEType', 'xs:token'], 0, 1, {'minOccurs': '0', 'name': 'CNAE', 'type': 'xs:token'}, None),
        MemberSpec_('dIniAtiv', 'xs:date', 0, 1, {'minOccurs': '0', 'name': 'dIniAtiv', 'type': 'xs:date'}, None),
        MemberSpec_('dUltSit', 'xs:date', 0, 1, {'minOccurs': '0', 'name': 'dUltSit', 'type': 'xs:date'}, None),
        MemberSpec_('dBaixa', 'xs:date', 0, 1, {'minOccurs': '0', 'name': 'dBaixa', 'type': 'xs:date'}, None),
        MemberSpec_('IEUnica', ['TIe', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'IEUnica', 'type': 'xs:string'}, None),
        MemberSpec_('IEAtual', ['TIe', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'IEAtual', 'type': 'xs:string'}, None),
        MemberSpec_('ender', 'TEndereco', 0, 1, {'minOccurs': '0', 'name': 'ender', 'type': 'TEndereco'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, IE=None, CNPJ=None, CPF=None, UF=None, cSit=None, indCredNFe=None, indCredCTe=None, xNome=None, xFant=None, xRegApur=None, CNAE=None, dIniAtiv=None, dUltSit=None, dBaixa=None, IEUnica=None, IEAtual=None, ender=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.IE = IE
        self.validate_TIe(self.IE)
        self.IE_nsprefix_ = None
        self.CNPJ = CNPJ
        self.validate_TCnpjVar(self.CNPJ)
        self.CNPJ_nsprefix_ = None
        self.CPF = CPF
        self.validate_TCpfVar(self.CPF)
        self.CPF_nsprefix_ = None
        self.UF = UF
        self.validate_TUf(self.UF)
        self.UF_nsprefix_ = None
        self.cSit = cSit
        self.validate_cSitType(self.cSit)
        self.cSit_nsprefix_ = None
        self.indCredNFe = indCredNFe
        self.validate_indCredNFeType(self.indCredNFe)
        self.indCredNFe_nsprefix_ = None
        self.indCredCTe = indCredCTe
        self.validate_indCredCTeType(self.indCredCTe)
        self.indCredCTe_nsprefix_ = None
        self.xNome = xNome
        self.validate_xNomeType(self.xNome)
        self.xNome_nsprefix_ = None
        self.xFant = xFant
        self.validate_xFantType(self.xFant)
        self.xFant_nsprefix_ = None
        self.xRegApur = xRegApur
        self.validate_xRegApurType(self.xRegApur)
        self.xRegApur_nsprefix_ = None
        self.CNAE = CNAE
        self.validate_CNAEType(self.CNAE)
        self.CNAE_nsprefix_ = None
        if isinstance(dIniAtiv, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dIniAtiv, '%Y-%m-%d').date()
        else:
            initvalue_ = dIniAtiv
        self.dIniAtiv = initvalue_
        self.dIniAtiv_nsprefix_ = None
        if isinstance(dUltSit, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dUltSit, '%Y-%m-%d').date()
        else:
            initvalue_ = dUltSit
        self.dUltSit = initvalue_
        self.dUltSit_nsprefix_ = None
        if isinstance(dBaixa, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dBaixa, '%Y-%m-%d').date()
        else:
            initvalue_ = dBaixa
        self.dBaixa = initvalue_
        self.dBaixa_nsprefix_ = None
        self.IEUnica = IEUnica
        self.validate_TIe(self.IEUnica)
        self.IEUnica_nsprefix_ = None
        self.IEAtual = IEAtual
        self.validate_TIe(self.IEAtual)
        self.IEAtual_nsprefix_ = None
        self.ender = ender
        self.ender_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, infCadType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if infCadType.subclass:
            return infCadType.subclass(*args_, **kwargs_)
        else:
            return infCadType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TIe(self, value):
        result = True
        # Validate type TIe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TIe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TIe_patterns_, ))
                result = False
        return result
    validate_TIe_patterns_ = [['^([0-9]{2,14}|ISENTO)$']]
    def validate_TCnpjVar(self, value):
        result = True
        # Validate type TCnpjVar, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TCnpjVar_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TCnpjVar_patterns_, ))
                result = False
        return result
    validate_TCnpjVar_patterns_ = [['^([0-9]{3,14})$']]
    def validate_TCpfVar(self, value):
        result = True
        # Validate type TCpfVar, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TCpfVar_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TCpfVar_patterns_, ))
                result = False
        return result
    validate_TCpfVar_patterns_ = [['^([0-9]{3,11})$']]
    def validate_TUf(self, value):
        result = True
        # Validate type TUf, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO', 'EX']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TUf' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_cSitType(self, value):
        result = True
        # Validate type cSitType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['0', '1']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on cSitType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_indCredNFeType(self, value):
        result = True
        # Validate type indCredNFeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['0', '1', '2', '3', '4']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on indCredNFeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_indCredCTeType(self, value):
        result = True
        # Validate type indCredCTeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['0', '1', '2', '3', '4']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on indCredCTeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_xNomeType(self, value):
        result = True
        # Validate type xNomeType, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on xNomeType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on xNomeType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_xNomeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_xNomeType_patterns_, ))
                result = False
        return result
    validate_xNomeType_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_xFantType(self, value):
        result = True
        # Validate type xFantType, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on xFantType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on xFantType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_xFantType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_xFantType_patterns_, ))
                result = False
        return result
    validate_xFantType_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_xRegApurType(self, value):
        result = True
        # Validate type xRegApurType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on xRegApurType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on xRegApurType' % {"value" : value, "lineno": lineno} )
                result = False
        return result
    def validate_CNAEType(self, value):
        result = True
        # Validate type CNAEType, a restriction on xs:token.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_CNAEType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_CNAEType_patterns_, ))
                result = False
        return result
    validate_CNAEType_patterns_ = [['^([0-9]{6,7})$']]
    def hasContent_(self):
        if (
            self.IE is not None or
            self.CNPJ is not None or
            self.CPF is not None or
            self.UF is not None or
            self.cSit is not None or
            self.indCredNFe is not None or
            self.indCredCTe is not None or
            self.xNome is not None or
            self.xFant is not None or
            self.xRegApur is not None or
            self.CNAE is not None or
            self.dIniAtiv is not None or
            self.dUltSit is not None or
            self.dBaixa is not None or
            self.IEUnica is not None or
            self.IEAtual is not None or
            self.ender is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infCadType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('infCadType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'infCadType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='infCadType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='infCadType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='infCadType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infCadType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IE is not None:
            namespaceprefix_ = self.IE_nsprefix_ + ':' if (UseCapturedNS_ and self.IE_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIE>%s</%sIE>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.IE), input_name='IE')), namespaceprefix_ , eol_))
        if self.CNPJ is not None:
            namespaceprefix_ = self.CNPJ_nsprefix_ + ':' if (UseCapturedNS_ and self.CNPJ_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCNPJ>%s</%sCNPJ>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CNPJ), input_name='CNPJ')), namespaceprefix_ , eol_))
        if self.CPF is not None:
            namespaceprefix_ = self.CPF_nsprefix_ + ':' if (UseCapturedNS_ and self.CPF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCPF>%s</%sCPF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CPF), input_name='CPF')), namespaceprefix_ , eol_))
        if self.UF is not None:
            namespaceprefix_ = self.UF_nsprefix_ + ':' if (UseCapturedNS_ and self.UF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sUF>%s</%sUF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.UF), input_name='UF')), namespaceprefix_ , eol_))
        if self.cSit is not None:
            namespaceprefix_ = self.cSit_nsprefix_ + ':' if (UseCapturedNS_ and self.cSit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scSit>%s</%scSit>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cSit), input_name='cSit')), namespaceprefix_ , eol_))
        if self.indCredNFe is not None:
            namespaceprefix_ = self.indCredNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.indCredNFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sindCredNFe>%s</%sindCredNFe>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.indCredNFe), input_name='indCredNFe')), namespaceprefix_ , eol_))
        if self.indCredCTe is not None:
            namespaceprefix_ = self.indCredCTe_nsprefix_ + ':' if (UseCapturedNS_ and self.indCredCTe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sindCredCTe>%s</%sindCredCTe>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.indCredCTe), input_name='indCredCTe')), namespaceprefix_ , eol_))
        if self.xNome is not None:
            namespaceprefix_ = self.xNome_nsprefix_ + ':' if (UseCapturedNS_ and self.xNome_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxNome>%s</%sxNome>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xNome), input_name='xNome')), namespaceprefix_ , eol_))
        if self.xFant is not None:
            namespaceprefix_ = self.xFant_nsprefix_ + ':' if (UseCapturedNS_ and self.xFant_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxFant>%s</%sxFant>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xFant), input_name='xFant')), namespaceprefix_ , eol_))
        if self.xRegApur is not None:
            namespaceprefix_ = self.xRegApur_nsprefix_ + ':' if (UseCapturedNS_ and self.xRegApur_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxRegApur>%s</%sxRegApur>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xRegApur), input_name='xRegApur')), namespaceprefix_ , eol_))
        if self.CNAE is not None:
            namespaceprefix_ = self.CNAE_nsprefix_ + ':' if (UseCapturedNS_ and self.CNAE_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCNAE>%s</%sCNAE>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CNAE), input_name='CNAE')), namespaceprefix_ , eol_))
        if self.dIniAtiv is not None:
            namespaceprefix_ = self.dIniAtiv_nsprefix_ + ':' if (UseCapturedNS_ and self.dIniAtiv_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdIniAtiv>%s</%sdIniAtiv>%s' % (namespaceprefix_ , self.gds_format_date(self.dIniAtiv, input_name='dIniAtiv'), namespaceprefix_ , eol_))
        if self.dUltSit is not None:
            namespaceprefix_ = self.dUltSit_nsprefix_ + ':' if (UseCapturedNS_ and self.dUltSit_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdUltSit>%s</%sdUltSit>%s' % (namespaceprefix_ , self.gds_format_date(self.dUltSit, input_name='dUltSit'), namespaceprefix_ , eol_))
        if self.dBaixa is not None:
            namespaceprefix_ = self.dBaixa_nsprefix_ + ':' if (UseCapturedNS_ and self.dBaixa_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdBaixa>%s</%sdBaixa>%s' % (namespaceprefix_ , self.gds_format_date(self.dBaixa, input_name='dBaixa'), namespaceprefix_ , eol_))
        if self.IEUnica is not None:
            namespaceprefix_ = self.IEUnica_nsprefix_ + ':' if (UseCapturedNS_ and self.IEUnica_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIEUnica>%s</%sIEUnica>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.IEUnica), input_name='IEUnica')), namespaceprefix_ , eol_))
        if self.IEAtual is not None:
            namespaceprefix_ = self.IEAtual_nsprefix_ + ':' if (UseCapturedNS_ and self.IEAtual_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sIEAtual>%s</%sIEAtual>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.IEAtual), input_name='IEAtual')), namespaceprefix_ , eol_))
        if self.ender is not None:
            namespaceprefix_ = self.ender_nsprefix_ + ':' if (UseCapturedNS_ and self.ender_nsprefix_) else ''
            self.ender.export(outfile, level, namespaceprefix_, namespacedef_='', name_='ender', pretty_print=pretty_print)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'IE':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'IE')
            value_ = self.gds_validate_string(value_, node, 'IE')
            self.IE = value_
            self.IE_nsprefix_ = child_.prefix
            # validate type TIe
            self.validate_TIe(self.IE)
        elif nodeName_ == 'CNPJ':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CNPJ')
            value_ = self.gds_validate_string(value_, node, 'CNPJ')
            self.CNPJ = value_
            self.CNPJ_nsprefix_ = child_.prefix
            # validate type TCnpjVar
            self.validate_TCnpjVar(self.CNPJ)
        elif nodeName_ == 'CPF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CPF')
            value_ = self.gds_validate_string(value_, node, 'CPF')
            self.CPF = value_
            self.CPF_nsprefix_ = child_.prefix
            # validate type TCpfVar
            self.validate_TCpfVar(self.CPF)
        elif nodeName_ == 'UF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'UF')
            value_ = self.gds_validate_string(value_, node, 'UF')
            self.UF = value_
            self.UF_nsprefix_ = child_.prefix
            # validate type TUf
            self.validate_TUf(self.UF)
        elif nodeName_ == 'cSit':
            value_ = child_.text
            if value_:
                value_ = re_.sub(String_cleanup_pat_, " ", value_).strip()
            else:
                value_ = ""
            value_ = self.gds_parse_string(value_, node, 'cSit')
            value_ = self.gds_validate_string(value_, node, 'cSit')
            self.cSit = value_
            self.cSit_nsprefix_ = child_.prefix
            # validate type cSitType
            self.validate_cSitType(self.cSit)
        elif nodeName_ == 'indCredNFe':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'indCredNFe')
            value_ = self.gds_validate_string(value_, node, 'indCredNFe')
            self.indCredNFe = value_
            self.indCredNFe_nsprefix_ = child_.prefix
            # validate type indCredNFeType
            self.validate_indCredNFeType(self.indCredNFe)
        elif nodeName_ == 'indCredCTe':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'indCredCTe')
            value_ = self.gds_validate_string(value_, node, 'indCredCTe')
            self.indCredCTe = value_
            self.indCredCTe_nsprefix_ = child_.prefix
            # validate type indCredCTeType
            self.validate_indCredCTeType(self.indCredCTe)
        elif nodeName_ == 'xNome':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xNome')
            value_ = self.gds_validate_string(value_, node, 'xNome')
            self.xNome = value_
            self.xNome_nsprefix_ = child_.prefix
            # validate type xNomeType
            self.validate_xNomeType(self.xNome)
        elif nodeName_ == 'xFant':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xFant')
            value_ = self.gds_validate_string(value_, node, 'xFant')
            self.xFant = value_
            self.xFant_nsprefix_ = child_.prefix
            # validate type xFantType
            self.validate_xFantType(self.xFant)
        elif nodeName_ == 'xRegApur':
            value_ = child_.text
            if value_:
                value_ = re_.sub(String_cleanup_pat_, " ", value_).strip()
            else:
                value_ = ""
            value_ = self.gds_parse_string(value_, node, 'xRegApur')
            value_ = self.gds_validate_string(value_, node, 'xRegApur')
            self.xRegApur = value_
            self.xRegApur_nsprefix_ = child_.prefix
            # validate type xRegApurType
            self.validate_xRegApurType(self.xRegApur)
        elif nodeName_ == 'CNAE':
            value_ = child_.text
            if value_:
                value_ = re_.sub(String_cleanup_pat_, " ", value_).strip()
            else:
                value_ = ""
            value_ = self.gds_parse_string(value_, node, 'CNAE')
            value_ = self.gds_validate_string(value_, node, 'CNAE')
            self.CNAE = value_
            self.CNAE_nsprefix_ = child_.prefix
            # validate type CNAEType
            self.validate_CNAEType(self.CNAE)
        elif nodeName_ == 'dIniAtiv':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.dIniAtiv = dval_
            self.dIniAtiv_nsprefix_ = child_.prefix
        elif nodeName_ == 'dUltSit':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.dUltSit = dval_
            self.dUltSit_nsprefix_ = child_.prefix
        elif nodeName_ == 'dBaixa':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_)
            self.dBaixa = dval_
            self.dBaixa_nsprefix_ = child_.prefix
        elif nodeName_ == 'IEUnica':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'IEUnica')
            value_ = self.gds_validate_string(value_, node, 'IEUnica')
            self.IEUnica = value_
            self.IEUnica_nsprefix_ = child_.prefix
            # validate type TIe
            self.validate_TIe(self.IEUnica)
        elif nodeName_ == 'IEAtual':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'IEAtual')
            value_ = self.gds_validate_string(value_, node, 'IEAtual')
            self.IEAtual = value_
            self.IEAtual_nsprefix_ = child_.prefix
            # validate type TIe
            self.validate_TIe(self.IEAtual)
        elif nodeName_ == 'ender':
            obj_ = TEndereco.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ender = obj_
            obj_.original_tagname_ = 'ender'
# end class infCadType


GDSClassesMapping = {
    'retConsCad': TRetConsCad,
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'TRetConsCad'
        rootClass = TRetConsCad
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, nsmap=None):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'TRetConsCad'
        rootClass = TRetConsCad
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if mapping is None:
        mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping, nsmap_=nsmap)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'TRetConsCad'
        rootClass = TRetConsCad
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'TRetConsCad'
        rootClass = TRetConsCad
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from retConsCad import *\n\n')
        sys.stdout.write('import retConsCad as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
}

#
# Mapping of namespaces to types defined in them
# and the file in which each is defined.
# simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {'http://www.portalfiscal.inf.br/nfe': [('TCodUfIBGE',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TCodMunIBGE',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TChNFe',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TProt',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TRec', 'tiposBasico_v1.03.xsd', 'ST'),
                                        ('TStat',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TCnpj',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TCnpjVar',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TCnpjOpc',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TCpf', 'tiposBasico_v1.03.xsd', 'ST'),
                                        ('TCpfVar',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_0302',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_0302Opc',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_0803',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_0803Opc',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_0804',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_0804Opc',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_1104',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_1104Opc',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_1203',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_1203Opc',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_1204',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_1204Opc',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_1302',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_1302Opc',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_1110',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TDec_1104v',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TIeDest',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TIeST',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TIe', 'tiposBasico_v1.03.xsd', 'ST'),
                                        ('TMod', 'tiposBasico_v1.03.xsd', 'ST'),
                                        ('TNF', 'tiposBasico_v1.03.xsd', 'ST'),
                                        ('TSerie',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('Tpais',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TUf', 'tiposBasico_v1.03.xsd', 'ST'),
                                        ('TUfEmi',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TAmb', 'tiposBasico_v1.03.xsd', 'ST'),
                                        ('TVerAplic',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TMotivo',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TJust',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TServ',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('Tano', 'tiposBasico_v1.03.xsd', 'ST'),
                                        ('TMed', 'tiposBasico_v1.03.xsd', 'ST'),
                                        ('TString',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TData',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TTime',
                                         'tiposBasico_v1.03.xsd',
                                         'ST'),
                                        ('TUfCons',
                                         'leiauteConsultaCadastro_v2.00.xsd',
                                         'ST'),
                                        ('TVerConsCad',
                                         'leiauteConsultaCadastro_v2.00.xsd',
                                         'ST'),
                                        ('TConsCad',
                                         'leiauteConsultaCadastro_v2.00.xsd',
                                         'CT'),
                                        ('TRetConsCad',
                                         'leiauteConsultaCadastro_v2.00.xsd',
                                         'CT'),
                                        ('TEndereco',
                                         'leiauteConsultaCadastro_v2.00.xsd',
                                         'CT')]}

__all__ = [
    "TConsCad",
    "TEndereco",
    "TRetConsCad",
    "infCadType",
    "infConsType",
    "infConsType1"
]
