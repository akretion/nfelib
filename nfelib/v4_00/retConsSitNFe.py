#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated  by generateDS.py version 2.38.6.
# Python 3.10.4 (main, Apr  2 2022, 09:04:19) [GCC 11.2.0]
#
# Command line options:
#   ('--no-namespace-defs', '')
#   ('--no-dates', '')
#   ('--member-specs', 'list')
#   ('--use-getter-setter', 'none')
#   ('-f', '')
#   ('-o', '/tmp/nfelib-master/nfelib/v4_00/retConsSitNFe.py')
#
# Command line arguments:
#   /tmp/nfelib-master/schemas/nfe/v4_00/retConsSitNFe_v4.00.xsd
#
# Command line:
#   /usr/local/bin/generateDS.py --no-namespace-defs --no-dates --member-specs="list" --use-getter-setter="none" -f -o "/tmp/nfelib-master/nfelib/v4_00/retConsSitNFe.py" /tmp/nfelib-master/schemas/nfe/v4_00/retConsSitNFe_v4.00.xsd
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


class TCOrgaoIBGE(str, Enum):
    """Tipo Código de orgão (UF da tabela do IBGE + 90 RFB)"""
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
    _9_0='90'
    _9_1='91'
    _9_2='92'


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
    _6_5='65'


class TTransformURI(str, Enum):
    HTTPWWWW_3ORG_2000_09XMLDSIGENVELOPEDSIGNATURE='http://www.w3.org/2000/09/xmldsig#enveloped-signature'
    HTTPWWWW_3ORGTR_2001RECXMLC_14_N_20010315='http://www.w3.org/TR/2001/REC-xml-c14n-20010315'


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


class TVerConsSitNFe(str, Enum):
    """Tipo Versão do Leiaute da Cosulta situação NF-e - 4.00"""
    _4_00='4.00'


class xServType(str, Enum):
    """Serviço Solicitado"""
    CONSULTAR='CONSULTAR'


class TConsSitNFe(GeneratedsSuper):
    """Tipo Pedido de Consulta da Situação Atual da Nota Fiscal Eletrônica"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('versao', 'TVerConsSitNFe', 0, 0, {'use': 'required'}),
        MemberSpec_('tpAmb', ['TAmb', 'xs:string'], 0, 0, {'name': 'tpAmb', 'type': 'xs:string'}, None),
        MemberSpec_('xServ', ['xServType', 'TServ', 'nfe:TString'], 0, 0, {'name': 'xServ', 'type': 'xs:string'}, None),
        MemberSpec_('chNFe', ['TChNFe', 'xs:string'], 0, 0, {'name': 'chNFe', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, versao=None, tpAmb=None, xServ=None, chNFe=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.versao = _cast(None, versao)
        self.versao_nsprefix_ = None
        self.tpAmb = tpAmb
        self.validate_TAmb(self.tpAmb)
        self.tpAmb_nsprefix_ = None
        self.xServ = xServ
        self.validate_xServType(self.xServ)
        self.xServ_nsprefix_ = None
        self.chNFe = chNFe
        self.validate_TChNFe(self.chNFe)
        self.chNFe_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TConsSitNFe)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TConsSitNFe.subclass:
            return TConsSitNFe.subclass(*args_, **kwargs_)
        else:
            return TConsSitNFe(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TAmb(self, value):
        result = True
        # Validate type TAmb, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1', '2']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TAmb' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_xServType(self, value):
        result = True
        # Validate type xServType, a restriction on TServ.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['CONSULTAR']
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
    def validate_TChNFe(self, value):
        result = True
        # Validate type TChNFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TChNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TChNFe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TChNFe_patterns_, ))
                result = False
        return result
    validate_TChNFe_patterns_ = [['^([0-9]{44})$']]
    def validate_TVerConsSitNFe(self, value):
        # Validate type TVerConsSitNFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['4.00']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TVerConsSitNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.tpAmb is not None or
            self.xServ is not None or
            self.chNFe is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TConsSitNFe', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TConsSitNFe')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TConsSitNFe':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TConsSitNFe')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TConsSitNFe', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TConsSitNFe'):
        if self.versao is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            outfile.write(' versao=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.versao), input_name='versao')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TConsSitNFe', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.tpAmb is not None:
            namespaceprefix_ = self.tpAmb_nsprefix_ + ':' if (UseCapturedNS_ and self.tpAmb_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stpAmb>%s</%stpAmb>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tpAmb), input_name='tpAmb')), namespaceprefix_ , eol_))
        if self.xServ is not None:
            namespaceprefix_ = self.xServ_nsprefix_ + ':' if (UseCapturedNS_ and self.xServ_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxServ>%s</%sxServ>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xServ), input_name='xServ')), namespaceprefix_ , eol_))
        if self.chNFe is not None:
            namespaceprefix_ = self.chNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.chNFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%schNFe>%s</%schNFe>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.chNFe), input_name='chNFe')), namespaceprefix_ , eol_))
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
            self.validate_TVerConsSitNFe(self.versao)    # validate type TVerConsSitNFe
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'tpAmb':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tpAmb')
            value_ = self.gds_validate_string(value_, node, 'tpAmb')
            self.tpAmb = value_
            self.tpAmb_nsprefix_ = child_.prefix
            # validate type TAmb
            self.validate_TAmb(self.tpAmb)
        elif nodeName_ == 'xServ':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xServ')
            value_ = self.gds_validate_string(value_, node, 'xServ')
            self.xServ = value_
            self.xServ_nsprefix_ = child_.prefix
            # validate type xServType
            self.validate_xServType(self.xServ)
        elif nodeName_ == 'chNFe':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'chNFe')
            value_ = self.gds_validate_string(value_, node, 'chNFe')
            self.chNFe = value_
            self.chNFe_nsprefix_ = child_.prefix
            # validate type TChNFe
            self.validate_TChNFe(self.chNFe)
# end class TConsSitNFe


class TRetConsSitNFe(GeneratedsSuper):
    """Tipo Retorno de Pedido de Consulta da Situação Atual da Nota Fiscal
    Eletrônica"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('versao', 'TVerConsSitNFe', 0, 0, {'use': 'required'}),
        MemberSpec_('tpAmb', ['TAmb', 'xs:string'], 0, 0, {'name': 'tpAmb', 'type': 'xs:string'}, None),
        MemberSpec_('verAplic', ['TVerAplic', 'nfe:TString'], 0, 0, {'name': 'verAplic', 'type': 'xs:string'}, None),
        MemberSpec_('cStat', ['TStat', 'xs:string'], 0, 0, {'name': 'cStat', 'type': 'xs:string'}, None),
        MemberSpec_('xMotivo', ['TMotivo', 'nfe:TString'], 0, 0, {'name': 'xMotivo', 'type': 'xs:string'}, None),
        MemberSpec_('cUF', ['TCodUfIBGE', 'xs:string'], 0, 0, {'name': 'cUF', 'type': 'xs:string'}, None),
        MemberSpec_('dhRecbto', ['TDateTimeUTC', 'xs:string'], 0, 0, {'name': 'dhRecbto', 'type': 'xs:string'}, None),
        MemberSpec_('chNFe', ['TChNFe', 'xs:string'], 0, 0, {'name': 'chNFe', 'type': 'xs:string'}, None),
        MemberSpec_('protNFe', 'TProtNFe', 0, 1, {'minOccurs': '0', 'name': 'protNFe', 'type': 'TProtNFe'}, None),
        MemberSpec_('retCancNFe', 'TRetCancNFe', 0, 1, {'minOccurs': '0', 'name': 'retCancNFe', 'type': 'TRetCancNFe'}, None),
        MemberSpec_('procEventoNFe', 'TProcEvento', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'procEventoNFe', 'type': 'TProcEvento'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, versao=None, tpAmb=None, verAplic=None, cStat=None, xMotivo=None, cUF=None, dhRecbto=None, chNFe=None, protNFe=None, retCancNFe=None, procEventoNFe=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.versao = _cast(None, versao)
        self.versao_nsprefix_ = None
        self.tpAmb = tpAmb
        self.validate_TAmb(self.tpAmb)
        self.tpAmb_nsprefix_ = None
        self.verAplic = verAplic
        self.validate_TVerAplic(self.verAplic)
        self.verAplic_nsprefix_ = None
        self.cStat = cStat
        self.validate_TStat(self.cStat)
        self.cStat_nsprefix_ = None
        self.xMotivo = xMotivo
        self.validate_TMotivo(self.xMotivo)
        self.xMotivo_nsprefix_ = None
        self.cUF = cUF
        self.validate_TCodUfIBGE(self.cUF)
        self.cUF_nsprefix_ = None
        self.dhRecbto = dhRecbto
        self.validate_TDateTimeUTC(self.dhRecbto)
        self.dhRecbto_nsprefix_ = None
        self.chNFe = chNFe
        self.validate_TChNFe(self.chNFe)
        self.chNFe_nsprefix_ = None
        self.protNFe = protNFe
        self.protNFe_nsprefix_ = None
        self.retCancNFe = retCancNFe
        self.retCancNFe_nsprefix_ = None
        if procEventoNFe is None:
            self.procEventoNFe = []
        else:
            self.procEventoNFe = procEventoNFe
        self.procEventoNFe_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TRetConsSitNFe)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TRetConsSitNFe.subclass:
            return TRetConsSitNFe.subclass(*args_, **kwargs_)
        else:
            return TRetConsSitNFe(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TAmb(self, value):
        result = True
        # Validate type TAmb, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1', '2']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TAmb' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
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
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TStat' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
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
    def validate_TDateTimeUTC(self, value):
        result = True
        # Validate type TDateTimeUTC, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TDateTimeUTC_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TDateTimeUTC_patterns_, ))
                result = False
        return result
    validate_TDateTimeUTC_patterns_ = [['^((((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\\d):[0-5]\\d:[0-5]\\d([\\-,\\+](0[0-9]|10|11):00|([\\+](12):00)))$']]
    def validate_TChNFe(self, value):
        result = True
        # Validate type TChNFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TChNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TChNFe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TChNFe_patterns_, ))
                result = False
        return result
    validate_TChNFe_patterns_ = [['^([0-9]{44})$']]
    def validate_TVerConsSitNFe(self, value):
        # Validate type TVerConsSitNFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['4.00']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TVerConsSitNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.tpAmb is not None or
            self.verAplic is not None or
            self.cStat is not None or
            self.xMotivo is not None or
            self.cUF is not None or
            self.dhRecbto is not None or
            self.chNFe is not None or
            self.protNFe is not None or
            self.retCancNFe is not None or
            self.procEventoNFe
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TRetConsSitNFe', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TRetConsSitNFe')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TRetConsSitNFe':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TRetConsSitNFe')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TRetConsSitNFe', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TRetConsSitNFe'):
        if self.versao is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            outfile.write(' versao=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.versao), input_name='versao')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TRetConsSitNFe', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.tpAmb is not None:
            namespaceprefix_ = self.tpAmb_nsprefix_ + ':' if (UseCapturedNS_ and self.tpAmb_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stpAmb>%s</%stpAmb>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tpAmb), input_name='tpAmb')), namespaceprefix_ , eol_))
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
        if self.cUF is not None:
            namespaceprefix_ = self.cUF_nsprefix_ + ':' if (UseCapturedNS_ and self.cUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scUF>%s</%scUF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cUF), input_name='cUF')), namespaceprefix_ , eol_))
        if self.dhRecbto is not None:
            namespaceprefix_ = self.dhRecbto_nsprefix_ + ':' if (UseCapturedNS_ and self.dhRecbto_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdhRecbto>%s</%sdhRecbto>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.dhRecbto), input_name='dhRecbto')), namespaceprefix_ , eol_))
        if self.chNFe is not None:
            namespaceprefix_ = self.chNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.chNFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%schNFe>%s</%schNFe>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.chNFe), input_name='chNFe')), namespaceprefix_ , eol_))
        if self.protNFe is not None:
            namespaceprefix_ = self.protNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.protNFe_nsprefix_) else ''
            self.protNFe.export(outfile, level, namespaceprefix_, namespacedef_='', name_='protNFe', pretty_print=pretty_print)
        if self.retCancNFe is not None:
            namespaceprefix_ = self.retCancNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.retCancNFe_nsprefix_) else ''
            self.retCancNFe.export(outfile, level, namespaceprefix_, namespacedef_='', name_='retCancNFe', pretty_print=pretty_print)
        for procEventoNFe_ in self.procEventoNFe:
            namespaceprefix_ = self.procEventoNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.procEventoNFe_nsprefix_) else ''
            procEventoNFe_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='procEventoNFe', pretty_print=pretty_print)
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
            self.validate_TVerConsSitNFe(self.versao)    # validate type TVerConsSitNFe
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'tpAmb':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tpAmb')
            value_ = self.gds_validate_string(value_, node, 'tpAmb')
            self.tpAmb = value_
            self.tpAmb_nsprefix_ = child_.prefix
            # validate type TAmb
            self.validate_TAmb(self.tpAmb)
        elif nodeName_ == 'verAplic':
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
        elif nodeName_ == 'cUF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cUF')
            value_ = self.gds_validate_string(value_, node, 'cUF')
            self.cUF = value_
            self.cUF_nsprefix_ = child_.prefix
            # validate type TCodUfIBGE
            self.validate_TCodUfIBGE(self.cUF)
        elif nodeName_ == 'dhRecbto':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dhRecbto')
            value_ = self.gds_validate_string(value_, node, 'dhRecbto')
            self.dhRecbto = value_
            self.dhRecbto_nsprefix_ = child_.prefix
            # validate type TDateTimeUTC
            self.validate_TDateTimeUTC(self.dhRecbto)
        elif nodeName_ == 'chNFe':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'chNFe')
            value_ = self.gds_validate_string(value_, node, 'chNFe')
            self.chNFe = value_
            self.chNFe_nsprefix_ = child_.prefix
            # validate type TChNFe
            self.validate_TChNFe(self.chNFe)
        elif nodeName_ == 'protNFe':
            obj_ = TProtNFe.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.protNFe = obj_
            obj_.original_tagname_ = 'protNFe'
        elif nodeName_ == 'retCancNFe':
            obj_ = TRetCancNFe.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.retCancNFe = obj_
            obj_.original_tagname_ = 'retCancNFe'
        elif nodeName_ == 'procEventoNFe':
            obj_ = TProcEvento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.procEventoNFe.append(obj_)
            obj_.original_tagname_ = 'procEventoNFe'
# end class TRetConsSitNFe


class TProtNFe(GeneratedsSuper):
    """Tipo Protocolo de status resultado do processamento da NF-e"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('versao', 'TVerNFe', 0, 0, {'use': 'required'}),
        MemberSpec_('infProt', 'infProtType', 0, 0, {'name': 'infProt', 'type': 'infProtType'}, None),
        MemberSpec_('Signature', 'SignatureType', 0, 1, {'minOccurs': '0', 'name': 'Signature', 'ref': 'Signature', 'type': 'Signature'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, versao=None, infProt=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.versao = _cast(None, versao)
        self.versao_nsprefix_ = None
        self.infProt = infProt
        self.infProt_nsprefix_ = None
        self.Signature = Signature
        self.Signature_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TProtNFe)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TProtNFe.subclass:
            return TProtNFe.subclass(*args_, **kwargs_)
        else:
            return TProtNFe(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TVerNFe(self, value):
        # Validate type TVerNFe, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TVerNFe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TVerNFe_patterns_, ))
    validate_TVerNFe_patterns_ = [['^([1-9]{1}\\.[0-9]{2})$'], ['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def hasContent_(self):
        if (
            self.infProt is not None or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TProtNFe', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TProtNFe')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TProtNFe':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TProtNFe')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TProtNFe', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TProtNFe'):
        if self.versao is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            outfile.write(' versao=%s' % (quote_attrib(self.versao), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TProtNFe', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.infProt is not None:
            namespaceprefix_ = self.infProt_nsprefix_ + ':' if (UseCapturedNS_ and self.infProt_nsprefix_) else ''
            self.infProt.export(outfile, level, namespaceprefix_, namespacedef_='', name_='infProt', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            self.Signature.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Signature', pretty_print=pretty_print)
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
            self.validate_TVerNFe(self.versao)    # validate type TVerNFe
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'infProt':
            obj_ = infProtType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.infProt = obj_
            obj_.original_tagname_ = 'infProt'
        elif nodeName_ == 'Signature':
            obj_ = SignatureType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signature = obj_
            obj_.original_tagname_ = 'Signature'
# end class TProtNFe


class TRetCancNFe(GeneratedsSuper):
    """Tipo retorno Pedido de Cancelamento da Nota Fiscal Eletrônica"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('versao', 'TVerCancNFe', 0, 0, {'use': 'required'}),
        MemberSpec_('infCanc', 'infCancType', 0, 0, {'name': 'infCanc', 'type': 'infCancType'}, None),
        MemberSpec_('Signature', 'SignatureType', 0, 1, {'minOccurs': '0', 'name': 'Signature', 'ref': 'Signature', 'type': 'Signature'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, versao=None, infCanc=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.versao = _cast(None, versao)
        self.versao_nsprefix_ = None
        self.infCanc = infCanc
        self.infCanc_nsprefix_ = None
        self.Signature = Signature
        self.Signature_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TRetCancNFe)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TRetCancNFe.subclass:
            return TRetCancNFe.subclass(*args_, **kwargs_)
        else:
            return TRetCancNFe(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TVerCancNFe(self, value):
        # Validate type TVerCancNFe, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TVerCancNFe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TVerCancNFe_patterns_, ))
    validate_TVerCancNFe_patterns_ = [['^([1-9]{1}\\.[0-9]{2})$'], ['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def hasContent_(self):
        if (
            self.infCanc is not None or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TRetCancNFe', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TRetCancNFe')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TRetCancNFe':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TRetCancNFe')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TRetCancNFe', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TRetCancNFe'):
        if self.versao is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            outfile.write(' versao=%s' % (quote_attrib(self.versao), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TRetCancNFe', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.infCanc is not None:
            namespaceprefix_ = self.infCanc_nsprefix_ + ':' if (UseCapturedNS_ and self.infCanc_nsprefix_) else ''
            self.infCanc.export(outfile, level, namespaceprefix_, namespacedef_='', name_='infCanc', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            self.Signature.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Signature', pretty_print=pretty_print)
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
            self.validate_TVerCancNFe(self.versao)    # validate type TVerCancNFe
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'infCanc':
            obj_ = infCancType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.infCanc = obj_
            obj_.original_tagname_ = 'infCanc'
        elif nodeName_ == 'Signature':
            obj_ = SignatureType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signature = obj_
            obj_.original_tagname_ = 'Signature'
# end class TRetCancNFe


class TEvento(GeneratedsSuper):
    """Tipo Evento"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('versao', 'TVerEvento', 0, 0, {'use': 'required'}),
        MemberSpec_('infEvento', 'infEventoType', 0, 0, {'name': 'infEvento', 'type': 'infEventoType'}, None),
        MemberSpec_('Signature', 'SignatureType', 0, 0, {'name': 'Signature', 'ref': 'Signature', 'type': 'Signature'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, versao=None, infEvento=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.versao = _cast(None, versao)
        self.versao_nsprefix_ = None
        self.infEvento = infEvento
        self.infEvento_nsprefix_ = None
        self.Signature = Signature
        self.Signature_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TEvento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TEvento.subclass:
            return TEvento.subclass(*args_, **kwargs_)
        else:
            return TEvento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TVerEvento(self, value):
        # Validate type TVerEvento, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TVerEvento_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TVerEvento_patterns_, ))
    validate_TVerEvento_patterns_ = [['^([1-9]{1}\\.[0-9]{2})$'], ['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def hasContent_(self):
        if (
            self.infEvento is not None or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TEvento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TEvento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TEvento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TEvento')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TEvento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TEvento'):
        if self.versao is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            outfile.write(' versao=%s' % (quote_attrib(self.versao), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TEvento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.infEvento is not None:
            namespaceprefix_ = self.infEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.infEvento_nsprefix_) else ''
            self.infEvento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='infEvento', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            self.Signature.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Signature', pretty_print=pretty_print)
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
            self.validate_TVerEvento(self.versao)    # validate type TVerEvento
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'infEvento':
            obj_ = infEventoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.infEvento = obj_
            obj_.original_tagname_ = 'infEvento'
        elif nodeName_ == 'Signature':
            obj_ = SignatureType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signature = obj_
            obj_.original_tagname_ = 'Signature'
# end class TEvento


class TRetEvento(GeneratedsSuper):
    """Tipo retorno do Evento"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('versao', 'TRetVerEvento', 0, 0, {'use': 'required'}),
        MemberSpec_('infEvento', 'infEventoType1', 0, 0, {'name': 'infEvento', 'type': 'infEventoType1'}, None),
        MemberSpec_('Signature', 'SignatureType', 0, 1, {'minOccurs': '0', 'name': 'Signature', 'ref': 'Signature', 'type': 'Signature'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, versao=None, infEvento=None, Signature=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.versao = _cast(None, versao)
        self.versao_nsprefix_ = None
        self.infEvento = infEvento
        self.infEvento_nsprefix_ = None
        self.Signature = Signature
        self.Signature_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TRetEvento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TRetEvento.subclass:
            return TRetEvento.subclass(*args_, **kwargs_)
        else:
            return TRetEvento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TRetVerEvento(self, value):
        # Validate type TRetVerEvento, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TRetVerEvento_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TRetVerEvento_patterns_, ))
    validate_TRetVerEvento_patterns_ = [['^([1-9]{1}\\.[0-9]{2})$'], ['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def hasContent_(self):
        if (
            self.infEvento is not None or
            self.Signature is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TRetEvento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TRetEvento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TRetEvento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TRetEvento')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TRetEvento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TRetEvento'):
        if self.versao is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            outfile.write(' versao=%s' % (quote_attrib(self.versao), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TRetEvento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.infEvento is not None:
            namespaceprefix_ = self.infEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.infEvento_nsprefix_) else ''
            self.infEvento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='infEvento', pretty_print=pretty_print)
        if self.Signature is not None:
            namespaceprefix_ = self.Signature_nsprefix_ + ':' if (UseCapturedNS_ and self.Signature_nsprefix_) else ''
            self.Signature.export(outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='Signature', pretty_print=pretty_print)
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
            self.validate_TRetVerEvento(self.versao)    # validate type TRetVerEvento
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'infEvento':
            obj_ = infEventoType1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.infEvento = obj_
            obj_.original_tagname_ = 'infEvento'
        elif nodeName_ == 'Signature':
            obj_ = SignatureType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Signature = obj_
            obj_.original_tagname_ = 'Signature'
# end class TRetEvento


class TProcEvento(GeneratedsSuper):
    """Tipo procEvento"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('versao', 'TVerEvento', 0, 0, {'use': 'required'}),
        MemberSpec_('evento', 'TEvento', 0, 0, {'name': 'evento', 'type': 'TEvento'}, None),
        MemberSpec_('retEvento', 'TRetEvento', 0, 0, {'name': 'retEvento', 'type': 'TRetEvento'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, versao=None, evento=None, retEvento=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.versao = _cast(None, versao)
        self.versao_nsprefix_ = None
        self.evento = evento
        self.evento_nsprefix_ = None
        self.retEvento = retEvento
        self.retEvento_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TProcEvento)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TProcEvento.subclass:
            return TProcEvento.subclass(*args_, **kwargs_)
        else:
            return TProcEvento(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TVerEvento(self, value):
        # Validate type TVerEvento, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TVerEvento_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TVerEvento_patterns_, ))
    validate_TVerEvento_patterns_ = [['^([1-9]{1}\\.[0-9]{2})$'], ['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def hasContent_(self):
        if (
            self.evento is not None or
            self.retEvento is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TProcEvento', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TProcEvento')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TProcEvento':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TProcEvento')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TProcEvento', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TProcEvento'):
        if self.versao is not None and 'versao' not in already_processed:
            already_processed.add('versao')
            outfile.write(' versao=%s' % (quote_attrib(self.versao), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='TProcEvento', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.evento is not None:
            namespaceprefix_ = self.evento_nsprefix_ + ':' if (UseCapturedNS_ and self.evento_nsprefix_) else ''
            self.evento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='evento', pretty_print=pretty_print)
        if self.retEvento is not None:
            namespaceprefix_ = self.retEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.retEvento_nsprefix_) else ''
            self.retEvento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='retEvento', pretty_print=pretty_print)
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
            self.validate_TVerEvento(self.versao)    # validate type TVerEvento
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'evento':
            obj_ = TEvento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.evento = obj_
            obj_.original_tagname_ = 'evento'
        elif nodeName_ == 'retEvento':
            obj_ = TRetEvento.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.retEvento = obj_
            obj_.original_tagname_ = 'retEvento'
# end class TProcEvento


class SignatureType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('SignedInfo', 'SignedInfoType', 0, 0, {'name': 'SignedInfo', 'type': 'SignedInfoType'}, None),
        MemberSpec_('SignatureValue', 'SignatureValueType', 0, 0, {'name': 'SignatureValue', 'type': 'SignatureValueType'}, None),
        MemberSpec_('KeyInfo', 'KeyInfoType', 0, 0, {'name': 'KeyInfo', 'type': 'KeyInfoType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, SignedInfo=None, SignatureValue=None, KeyInfo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.SignedInfo = SignedInfo
        self.SignedInfo_nsprefix_ = "ds"
        self.SignatureValue = SignatureValue
        self.SignatureValue_nsprefix_ = "ds"
        self.KeyInfo = KeyInfo
        self.KeyInfo_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureType.subclass:
            return SignatureType.subclass(*args_, **kwargs_)
        else:
            return SignatureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.SignedInfo is not None or
            self.SignatureValue is not None or
            self.KeyInfo is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SignedInfo is not None:
            namespaceprefix_ = self.SignedInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.SignedInfo_nsprefix_) else ''
            self.SignedInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SignedInfo', pretty_print=pretty_print)
        if self.SignatureValue is not None:
            namespaceprefix_ = self.SignatureValue_nsprefix_ + ':' if (UseCapturedNS_ and self.SignatureValue_nsprefix_) else ''
            self.SignatureValue.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SignatureValue', pretty_print=pretty_print)
        if self.KeyInfo is not None:
            namespaceprefix_ = self.KeyInfo_nsprefix_ + ':' if (UseCapturedNS_ and self.KeyInfo_nsprefix_) else ''
            self.KeyInfo.export(outfile, level, namespaceprefix_, namespacedef_='', name_='KeyInfo', pretty_print=pretty_print)
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
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'SignedInfo':
            obj_ = SignedInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignedInfo = obj_
            obj_.original_tagname_ = 'SignedInfo'
        elif nodeName_ == 'SignatureValue':
            obj_ = SignatureValueType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignatureValue = obj_
            obj_.original_tagname_ = 'SignatureValue'
        elif nodeName_ == 'KeyInfo':
            obj_ = KeyInfoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.KeyInfo = obj_
            obj_.original_tagname_ = 'KeyInfo'
# end class SignatureType


class SignatureValueType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('valueOf_', 'base64Binary', 0),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureValueType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureValueType.subclass:
            return SignatureValueType.subclass(*args_, **kwargs_)
        else:
            return SignatureValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureValueType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureValueType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureValueType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureValueType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureValueType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignatureValueType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignatureValueType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SignatureValueType


class SignedInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('CanonicalizationMethod', 'CanonicalizationMethodType', 0, 0, {'name': 'CanonicalizationMethod', 'type': 'CanonicalizationMethodType'}, None),
        MemberSpec_('SignatureMethod', 'SignatureMethodType', 0, 0, {'name': 'SignatureMethod', 'type': 'SignatureMethodType'}, None),
        MemberSpec_('Reference', 'ReferenceType', 0, 0, {'name': 'Reference', 'type': 'ReferenceType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, CanonicalizationMethod=None, SignatureMethod=None, Reference=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.CanonicalizationMethod = CanonicalizationMethod
        self.CanonicalizationMethod_nsprefix_ = None
        self.SignatureMethod = SignatureMethod
        self.SignatureMethod_nsprefix_ = None
        self.Reference = Reference
        self.Reference_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignedInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignedInfoType.subclass:
            return SignedInfoType.subclass(*args_, **kwargs_)
        else:
            return SignedInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.CanonicalizationMethod is not None or
            self.SignatureMethod is not None or
            self.Reference is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignedInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignedInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignedInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignedInfoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignedInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='SignedInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='SignedInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CanonicalizationMethod is not None:
            namespaceprefix_ = self.CanonicalizationMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.CanonicalizationMethod_nsprefix_) else ''
            self.CanonicalizationMethod.export(outfile, level, namespaceprefix_, namespacedef_='', name_='CanonicalizationMethod', pretty_print=pretty_print)
        if self.SignatureMethod is not None:
            namespaceprefix_ = self.SignatureMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.SignatureMethod_nsprefix_) else ''
            self.SignatureMethod.export(outfile, level, namespaceprefix_, namespacedef_='', name_='SignatureMethod', pretty_print=pretty_print)
        if self.Reference is not None:
            namespaceprefix_ = self.Reference_nsprefix_ + ':' if (UseCapturedNS_ and self.Reference_nsprefix_) else ''
            self.Reference.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Reference', pretty_print=pretty_print)
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
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'CanonicalizationMethod':
            obj_ = CanonicalizationMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.CanonicalizationMethod = obj_
            obj_.original_tagname_ = 'CanonicalizationMethod'
        elif nodeName_ == 'SignatureMethod':
            obj_ = SignatureMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SignatureMethod = obj_
            obj_.original_tagname_ = 'SignatureMethod'
        elif nodeName_ == 'Reference':
            obj_ = ReferenceType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Reference = obj_
            obj_.original_tagname_ = 'Reference'
# end class SignedInfoType


class ReferenceType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('URI', 'URIType', 0, 0, {'use': 'required'}),
        MemberSpec_('Type', 'anyURI', 0, 1, {'use': 'optional'}),
        MemberSpec_('Transforms', 'TransformsType', 0, 0, {'name': 'Transforms', 'type': 'TransformsType'}, None),
        MemberSpec_('DigestMethod', 'DigestMethodType', 0, 0, {'name': 'DigestMethod', 'type': 'DigestMethodType'}, None),
        MemberSpec_('DigestValue', ['DigestValueType', 'base64Binary'], 0, 0, {'name': 'DigestValue', 'type': 'xs:base64Binary'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, URI=None, Type=None, Transforms=None, DigestMethod=None, DigestValue=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.URI = _cast(None, URI)
        self.URI_nsprefix_ = None
        self.Type = _cast(None, Type)
        self.Type_nsprefix_ = None
        self.Transforms = Transforms
        self.Transforms_nsprefix_ = "ds"
        self.DigestMethod = DigestMethod
        self.DigestMethod_nsprefix_ = None
        self.DigestValue = DigestValue
        self.validate_DigestValueType(self.DigestValue)
        self.DigestValue_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ReferenceType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ReferenceType.subclass:
            return ReferenceType.subclass(*args_, **kwargs_)
        else:
            return ReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_DigestValueType(self, value):
        result = True
        # Validate type DigestValueType, a restriction on base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def validate_URIType(self, value):
        # Validate type URIType, a restriction on anyURI.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on URIType' % {"value" : value, "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.Transforms is not None or
            self.DigestMethod is not None or
            self.DigestValue is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='ReferenceType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ReferenceType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'ReferenceType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ReferenceType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ReferenceType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='ReferenceType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
        if self.URI is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            outfile.write(' URI=%s' % (quote_attrib(self.URI), ))
        if self.Type is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            outfile.write(' Type=%s' % (quote_attrib(self.Type), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='ReferenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Transforms is not None:
            namespaceprefix_ = self.Transforms_nsprefix_ + ':' if (UseCapturedNS_ and self.Transforms_nsprefix_) else ''
            self.Transforms.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Transforms', pretty_print=pretty_print)
        if self.DigestMethod is not None:
            namespaceprefix_ = self.DigestMethod_nsprefix_ + ':' if (UseCapturedNS_ and self.DigestMethod_nsprefix_) else ''
            self.DigestMethod.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DigestMethod', pretty_print=pretty_print)
        if self.DigestValue is not None:
            namespaceprefix_ = self.DigestValue_nsprefix_ + ':' if (UseCapturedNS_ and self.DigestValue_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sDigestValue>%s</%sDigestValue>%s' % (namespaceprefix_ , self.gds_format_base64(self.DigestValue, input_name='DigestValue'), namespaceprefix_ , eol_))
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
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
        value = find_attr_value_('URI', node)
        if value is not None and 'URI' not in already_processed:
            already_processed.add('URI')
            self.URI = value
            self.validate_URIType(self.URI)    # validate type URIType
        value = find_attr_value_('Type', node)
        if value is not None and 'Type' not in already_processed:
            already_processed.add('Type')
            self.Type = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Transforms':
            obj_ = TransformsType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transforms = obj_
            obj_.original_tagname_ = 'Transforms'
        elif nodeName_ == 'DigestMethod':
            obj_ = DigestMethodType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DigestMethod = obj_
            obj_.original_tagname_ = 'DigestMethod'
        elif nodeName_ == 'DigestValue':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'DigestValue')
            else:
                bval_ = None
            self.DigestValue = bval_
            self.DigestValue_nsprefix_ = child_.prefix
            # validate type DigestValueType
            self.validate_DigestValueType(self.DigestValue)
# end class ReferenceType


class TransformsType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Transform', 'TransformType', 1, 0, {'maxOccurs': '2', 'minOccurs': '2', 'name': 'Transform', 'type': 'TransformType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Transform=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if Transform is None:
            self.Transform = []
        else:
            self.Transform = Transform
        self.Transform_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransformsType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransformsType.subclass:
            return TransformsType.subclass(*args_, **kwargs_)
        else:
            return TransformsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.Transform
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformsType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransformsType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransformsType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransformsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransformsType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='TransformsType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Transform_ in self.Transform:
            namespaceprefix_ = self.Transform_nsprefix_ + ':' if (UseCapturedNS_ and self.Transform_nsprefix_) else ''
            Transform_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Transform', pretty_print=pretty_print)
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
        if nodeName_ == 'Transform':
            obj_ = TransformType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Transform.append(obj_)
            obj_.original_tagname_ = 'Transform'
# end class TransformsType


class TransformType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'ds:TTransformURI', 0, 0, {'use': 'required'}),
        MemberSpec_('XPath', 'xs:string', 1, 1, {'maxOccurs': 'unbounded', 'minOccurs': '0', 'name': 'XPath', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Algorithm=None, XPath=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
        if XPath is None:
            self.XPath = []
        else:
            self.XPath = XPath
        self.XPath_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TransformType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TransformType.subclass:
            return TransformType.subclass(*args_, **kwargs_)
        else:
            return TransformType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TTransformURI(self, value):
        # Validate type ds:TTransformURI, a restriction on anyURI.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['http://www.w3.org/2000/09/xmldsig#enveloped-signature', 'http://www.w3.org/TR/2001/REC-xml-c14n-20010315']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TTransformURI' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.XPath
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TransformType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'TransformType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TransformType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TransformType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='TransformType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='TransformType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for XPath_ in self.XPath:
            namespaceprefix_ = self.XPath_nsprefix_ + ':' if (UseCapturedNS_ and self.XPath_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sXPath>%s</%sXPath>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(XPath_), input_name='XPath')), namespaceprefix_ , eol_))
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
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
            self.validate_TTransformURI(self.Algorithm)    # validate type TTransformURI
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'XPath':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'XPath')
            value_ = self.gds_validate_string(value_, node, 'XPath')
            self.XPath.append(value_)
            self.XPath_nsprefix_ = child_.prefix
# end class TransformType


class KeyInfoType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'ID', 0, 1, {'use': 'optional'}),
        MemberSpec_('X509Data', 'X509DataType', 0, 0, {'name': 'X509Data', 'type': 'X509DataType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, X509Data=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.X509Data = X509Data
        self.X509Data_nsprefix_ = "ds"
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, KeyInfoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if KeyInfoType.subclass:
            return KeyInfoType.subclass(*args_, **kwargs_)
        else:
            return KeyInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.X509Data is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyInfoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('KeyInfoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'KeyInfoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='KeyInfoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='KeyInfoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='KeyInfoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (quote_attrib(self.Id), ))
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='KeyInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.X509Data is not None:
            namespaceprefix_ = self.X509Data_nsprefix_ + ':' if (UseCapturedNS_ and self.X509Data_nsprefix_) else ''
            self.X509Data.export(outfile, level, namespaceprefix_, namespacedef_='', name_='X509Data', pretty_print=pretty_print)
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
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'X509Data':
            obj_ = X509DataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.X509Data = obj_
            obj_.original_tagname_ = 'X509Data'
# end class KeyInfoType


class X509DataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('X509Certificate', 'xs:string', 0, 0, {'name': 'X509Certificate', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, X509Certificate=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.X509Certificate = X509Certificate
        self.X509Certificate_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, X509DataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if X509DataType.subclass:
            return X509DataType.subclass(*args_, **kwargs_)
        else:
            return X509DataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.X509Certificate is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='X509DataType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('X509DataType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'X509DataType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='X509DataType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='X509DataType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='ds:', name_='X509DataType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='ds:', namespacedef_='', name_='X509DataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.X509Certificate is not None:
            namespaceprefix_ = self.X509Certificate_nsprefix_ + ':' if (UseCapturedNS_ and self.X509Certificate_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sX509Certificate>%s</%sX509Certificate>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.X509Certificate), input_name='X509Certificate')), namespaceprefix_ , eol_))
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
        if nodeName_ == 'X509Certificate':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'X509Certificate')
            value_ = self.gds_validate_string(value_, node, 'X509Certificate')
            self.X509Certificate = value_
            self.X509Certificate_nsprefix_ = child_.prefix
# end class X509DataType


class infProtType(GeneratedsSuper):
    """Dados do protocolo de status"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'xs:string', 0, 1, {'use': 'optional'}),
        MemberSpec_('tpAmb', ['TAmb', 'xs:string'], 0, 0, {'name': 'tpAmb', 'type': 'xs:string'}, None),
        MemberSpec_('verAplic', ['TVerAplic', 'nfe:TString'], 0, 0, {'name': 'verAplic', 'type': 'xs:string'}, None),
        MemberSpec_('chNFe', ['TChNFe', 'xs:string'], 0, 0, {'name': 'chNFe', 'type': 'xs:string'}, None),
        MemberSpec_('dhRecbto', 'xs:dateTime', 0, 0, {'name': 'dhRecbto', 'type': 'xs:dateTime'}, None),
        MemberSpec_('nProt', ['TProt', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'nProt', 'type': 'xs:string'}, None),
        MemberSpec_('digVal', ['DigestValueType', 'base64Binary'], 0, 1, {'minOccurs': '0', 'name': 'digVal', 'type': 'xs:base64Binary'}, None),
        MemberSpec_('cStat', ['TStat', 'xs:string'], 0, 0, {'name': 'cStat', 'type': 'xs:string'}, None),
        MemberSpec_('xMotivo', ['TMotivo', 'nfe:TString'], 0, 0, {'name': 'xMotivo', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, tpAmb=None, verAplic=None, chNFe=None, dhRecbto=None, nProt=None, digVal=None, cStat=None, xMotivo=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.tpAmb = tpAmb
        self.validate_TAmb(self.tpAmb)
        self.tpAmb_nsprefix_ = None
        self.verAplic = verAplic
        self.validate_TVerAplic(self.verAplic)
        self.verAplic_nsprefix_ = None
        self.chNFe = chNFe
        self.validate_TChNFe(self.chNFe)
        self.chNFe_nsprefix_ = None
        if isinstance(dhRecbto, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dhRecbto, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = dhRecbto
        self.dhRecbto = initvalue_
        self.dhRecbto_nsprefix_ = None
        self.nProt = nProt
        self.validate_TProt(self.nProt)
        self.nProt_nsprefix_ = None
        self.digVal = digVal
        self.validate_DigestValueType(self.digVal)
        self.digVal_nsprefix_ = None
        self.cStat = cStat
        self.validate_TStat(self.cStat)
        self.cStat_nsprefix_ = None
        self.xMotivo = xMotivo
        self.validate_TMotivo(self.xMotivo)
        self.xMotivo_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, infProtType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if infProtType.subclass:
            return infProtType.subclass(*args_, **kwargs_)
        else:
            return infProtType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TAmb(self, value):
        result = True
        # Validate type TAmb, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1', '2']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TAmb' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
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
    def validate_TChNFe(self, value):
        result = True
        # Validate type TChNFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TChNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TChNFe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TChNFe_patterns_, ))
                result = False
        return result
    validate_TChNFe_patterns_ = [['^([0-9]{44})$']]
    def validate_TProt(self, value):
        result = True
        # Validate type TProt, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TProt' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TProt_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TProt_patterns_, ))
                result = False
        return result
    validate_TProt_patterns_ = [['^([0-9]{15})$']]
    def validate_DigestValueType(self, value):
        result = True
        # Validate type DigestValueType, a restriction on base64Binary.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            pass
        return result
    def validate_TStat(self, value):
        result = True
        # Validate type TStat, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TStat' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
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
    def hasContent_(self):
        if (
            self.tpAmb is not None or
            self.verAplic is not None or
            self.chNFe is not None or
            self.dhRecbto is not None or
            self.nProt is not None or
            self.digVal is not None or
            self.cStat is not None or
            self.xMotivo is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infProtType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('infProtType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'infProtType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='infProtType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='infProtType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='infProtType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infProtType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.tpAmb is not None:
            namespaceprefix_ = self.tpAmb_nsprefix_ + ':' if (UseCapturedNS_ and self.tpAmb_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stpAmb>%s</%stpAmb>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tpAmb), input_name='tpAmb')), namespaceprefix_ , eol_))
        if self.verAplic is not None:
            namespaceprefix_ = self.verAplic_nsprefix_ + ':' if (UseCapturedNS_ and self.verAplic_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sverAplic>%s</%sverAplic>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.verAplic), input_name='verAplic')), namespaceprefix_ , eol_))
        if self.chNFe is not None:
            namespaceprefix_ = self.chNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.chNFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%schNFe>%s</%schNFe>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.chNFe), input_name='chNFe')), namespaceprefix_ , eol_))
        if self.dhRecbto is not None:
            namespaceprefix_ = self.dhRecbto_nsprefix_ + ':' if (UseCapturedNS_ and self.dhRecbto_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdhRecbto>%s</%sdhRecbto>%s' % (namespaceprefix_ , self.gds_format_datetime(self.dhRecbto, input_name='dhRecbto'), namespaceprefix_ , eol_))
        if self.nProt is not None:
            namespaceprefix_ = self.nProt_nsprefix_ + ':' if (UseCapturedNS_ and self.nProt_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snProt>%s</%snProt>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.nProt), input_name='nProt')), namespaceprefix_ , eol_))
        if self.digVal is not None:
            namespaceprefix_ = self.digVal_nsprefix_ + ':' if (UseCapturedNS_ and self.digVal_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdigVal>%s</%sdigVal>%s' % (namespaceprefix_ , self.gds_format_base64(self.digVal, input_name='digVal'), namespaceprefix_ , eol_))
        if self.cStat is not None:
            namespaceprefix_ = self.cStat_nsprefix_ + ':' if (UseCapturedNS_ and self.cStat_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scStat>%s</%scStat>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cStat), input_name='cStat')), namespaceprefix_ , eol_))
        if self.xMotivo is not None:
            namespaceprefix_ = self.xMotivo_nsprefix_ + ':' if (UseCapturedNS_ and self.xMotivo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxMotivo>%s</%sxMotivo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xMotivo), input_name='xMotivo')), namespaceprefix_ , eol_))
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
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'tpAmb':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tpAmb')
            value_ = self.gds_validate_string(value_, node, 'tpAmb')
            self.tpAmb = value_
            self.tpAmb_nsprefix_ = child_.prefix
            # validate type TAmb
            self.validate_TAmb(self.tpAmb)
        elif nodeName_ == 'verAplic':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'verAplic')
            value_ = self.gds_validate_string(value_, node, 'verAplic')
            self.verAplic = value_
            self.verAplic_nsprefix_ = child_.prefix
            # validate type TVerAplic
            self.validate_TVerAplic(self.verAplic)
        elif nodeName_ == 'chNFe':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'chNFe')
            value_ = self.gds_validate_string(value_, node, 'chNFe')
            self.chNFe = value_
            self.chNFe_nsprefix_ = child_.prefix
            # validate type TChNFe
            self.validate_TChNFe(self.chNFe)
        elif nodeName_ == 'dhRecbto':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.dhRecbto = dval_
            self.dhRecbto_nsprefix_ = child_.prefix
        elif nodeName_ == 'nProt':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nProt')
            value_ = self.gds_validate_string(value_, node, 'nProt')
            self.nProt = value_
            self.nProt_nsprefix_ = child_.prefix
            # validate type TProt
            self.validate_TProt(self.nProt)
        elif nodeName_ == 'digVal':
            sval_ = child_.text
            if sval_ is not None:
                try:
                    bval_ = base64.b64decode(sval_)
                except (TypeError, ValueError) as exp:
                    raise_parse_error(child_, 'requires base64 encoded string: %s' % exp)
                bval_ = self.gds_validate_base64(bval_, node, 'digVal')
            else:
                bval_ = None
            self.digVal = bval_
            self.digVal_nsprefix_ = child_.prefix
            # validate type DigestValueType
            self.validate_DigestValueType(self.digVal)
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
# end class infProtType


class infCancType(GeneratedsSuper):
    """Dados do Resultado do Pedido de Cancelamento da Nota Fiscal
    Eletrônica"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'xs:string', 0, 1, {'use': 'optional'}),
        MemberSpec_('tpAmb', ['TAmb', 'xs:string'], 0, 0, {'name': 'tpAmb', 'type': 'xs:string'}, None),
        MemberSpec_('verAplic', ['TVerAplic', 'nfe:TString'], 0, 0, {'name': 'verAplic', 'type': 'xs:string'}, None),
        MemberSpec_('cStat', ['TStat', 'xs:string'], 0, 0, {'name': 'cStat', 'type': 'xs:string'}, None),
        MemberSpec_('xMotivo', ['TMotivo', 'nfe:TString'], 0, 0, {'name': 'xMotivo', 'type': 'xs:string'}, None),
        MemberSpec_('cUF', ['TCodUfIBGE', 'xs:string'], 0, 0, {'name': 'cUF', 'type': 'xs:string'}, None),
        MemberSpec_('chNFe', ['TChNFe', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'chNFe', 'type': 'xs:string'}, None),
        MemberSpec_('dhRecbto', 'xs:dateTime', 0, 1, {'minOccurs': '0', 'name': 'dhRecbto', 'type': 'xs:dateTime'}, None),
        MemberSpec_('nProt', ['TProt', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'nProt', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, tpAmb=None, verAplic=None, cStat=None, xMotivo=None, cUF=None, chNFe=None, dhRecbto=None, nProt=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.tpAmb = tpAmb
        self.validate_TAmb(self.tpAmb)
        self.tpAmb_nsprefix_ = None
        self.verAplic = verAplic
        self.validate_TVerAplic(self.verAplic)
        self.verAplic_nsprefix_ = None
        self.cStat = cStat
        self.validate_TStat(self.cStat)
        self.cStat_nsprefix_ = None
        self.xMotivo = xMotivo
        self.validate_TMotivo(self.xMotivo)
        self.xMotivo_nsprefix_ = None
        self.cUF = cUF
        self.validate_TCodUfIBGE(self.cUF)
        self.cUF_nsprefix_ = None
        self.chNFe = chNFe
        self.validate_TChNFe(self.chNFe)
        self.chNFe_nsprefix_ = None
        if isinstance(dhRecbto, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(dhRecbto, '%Y-%m-%dT%H:%M:%S')
        else:
            initvalue_ = dhRecbto
        self.dhRecbto = initvalue_
        self.dhRecbto_nsprefix_ = None
        self.nProt = nProt
        self.validate_TProt(self.nProt)
        self.nProt_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, infCancType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if infCancType.subclass:
            return infCancType.subclass(*args_, **kwargs_)
        else:
            return infCancType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TAmb(self, value):
        result = True
        # Validate type TAmb, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1', '2']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TAmb' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
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
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TStat' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
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
    def validate_TChNFe(self, value):
        result = True
        # Validate type TChNFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TChNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TChNFe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TChNFe_patterns_, ))
                result = False
        return result
    validate_TChNFe_patterns_ = [['^([0-9]{44})$']]
    def validate_TProt(self, value):
        result = True
        # Validate type TProt, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TProt' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TProt_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TProt_patterns_, ))
                result = False
        return result
    validate_TProt_patterns_ = [['^([0-9]{15})$']]
    def hasContent_(self):
        if (
            self.tpAmb is not None or
            self.verAplic is not None or
            self.cStat is not None or
            self.xMotivo is not None or
            self.cUF is not None or
            self.chNFe is not None or
            self.dhRecbto is not None or
            self.nProt is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infCancType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('infCancType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'infCancType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='infCancType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='infCancType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='infCancType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infCancType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.tpAmb is not None:
            namespaceprefix_ = self.tpAmb_nsprefix_ + ':' if (UseCapturedNS_ and self.tpAmb_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stpAmb>%s</%stpAmb>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tpAmb), input_name='tpAmb')), namespaceprefix_ , eol_))
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
        if self.cUF is not None:
            namespaceprefix_ = self.cUF_nsprefix_ + ':' if (UseCapturedNS_ and self.cUF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scUF>%s</%scUF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cUF), input_name='cUF')), namespaceprefix_ , eol_))
        if self.chNFe is not None:
            namespaceprefix_ = self.chNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.chNFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%schNFe>%s</%schNFe>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.chNFe), input_name='chNFe')), namespaceprefix_ , eol_))
        if self.dhRecbto is not None:
            namespaceprefix_ = self.dhRecbto_nsprefix_ + ':' if (UseCapturedNS_ and self.dhRecbto_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdhRecbto>%s</%sdhRecbto>%s' % (namespaceprefix_ , self.gds_format_datetime(self.dhRecbto, input_name='dhRecbto'), namespaceprefix_ , eol_))
        if self.nProt is not None:
            namespaceprefix_ = self.nProt_nsprefix_ + ':' if (UseCapturedNS_ and self.nProt_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snProt>%s</%snProt>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.nProt), input_name='nProt')), namespaceprefix_ , eol_))
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
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'tpAmb':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tpAmb')
            value_ = self.gds_validate_string(value_, node, 'tpAmb')
            self.tpAmb = value_
            self.tpAmb_nsprefix_ = child_.prefix
            # validate type TAmb
            self.validate_TAmb(self.tpAmb)
        elif nodeName_ == 'verAplic':
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
        elif nodeName_ == 'cUF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cUF')
            value_ = self.gds_validate_string(value_, node, 'cUF')
            self.cUF = value_
            self.cUF_nsprefix_ = child_.prefix
            # validate type TCodUfIBGE
            self.validate_TCodUfIBGE(self.cUF)
        elif nodeName_ == 'chNFe':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'chNFe')
            value_ = self.gds_validate_string(value_, node, 'chNFe')
            self.chNFe = value_
            self.chNFe_nsprefix_ = child_.prefix
            # validate type TChNFe
            self.validate_TChNFe(self.chNFe)
        elif nodeName_ == 'dhRecbto':
            sval_ = child_.text
            dval_ = self.gds_parse_datetime(sval_)
            self.dhRecbto = dval_
            self.dhRecbto_nsprefix_ = child_.prefix
        elif nodeName_ == 'nProt':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nProt')
            value_ = self.gds_validate_string(value_, node, 'nProt')
            self.nProt = value_
            self.nProt_nsprefix_ = child_.prefix
            # validate type TProt
            self.validate_TProt(self.nProt)
# end class infCancType


class infEventoType(GeneratedsSuper):
    """Identificação do autor do eventoIdentificador da TAG a ser assinada, a
    regra de formação do Id é:
    “ID” + tpEvento + chave da NF-e + nSeqEvento"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'IdType', 0, 0, {'use': 'required'}),
        MemberSpec_('cOrgao', ['TCOrgaoIBGE', 'xs:string'], 0, 0, {'name': 'cOrgao', 'type': 'xs:string'}, None),
        MemberSpec_('tpAmb', ['TAmb', 'xs:string'], 0, 0, {'name': 'tpAmb', 'type': 'xs:string'}, None),
        MemberSpec_('CNPJ', ['TCnpjOpc', 'xs:string'], 0, 0, {'name': 'CNPJ', 'type': 'xs:string'}, 1),
        MemberSpec_('CPF', ['TCpf', 'xs:string'], 0, 0, {'name': 'CPF', 'type': 'xs:string'}, 1),
        MemberSpec_('chNFe', ['TChNFe', 'xs:string'], 0, 0, {'name': 'chNFe', 'type': 'xs:string'}, None),
        MemberSpec_('dhEvento', ['TDateTimeUTC', 'xs:string'], 0, 0, {'name': 'dhEvento', 'type': 'xs:string'}, None),
        MemberSpec_('tpEvento', ['tpEventoType', 'xs:string'], 0, 0, {'name': 'tpEvento', 'type': 'xs:string'}, None),
        MemberSpec_('nSeqEvento', ['nSeqEventoType', 'xs:string'], 0, 0, {'name': 'nSeqEvento', 'type': 'xs:string'}, None),
        MemberSpec_('verEvento', ['verEventoType', 'xs:string'], 0, 0, {'name': 'verEvento', 'type': 'xs:string'}, None),
        MemberSpec_('detEvento', 'detEventoType', 0, 0, {'name': 'detEvento', 'type': 'detEventoType'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, cOrgao=None, tpAmb=None, CNPJ=None, CPF=None, chNFe=None, dhEvento=None, tpEvento=None, nSeqEvento=None, verEvento=None, detEvento=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.cOrgao = cOrgao
        self.validate_TCOrgaoIBGE(self.cOrgao)
        self.cOrgao_nsprefix_ = None
        self.tpAmb = tpAmb
        self.validate_TAmb(self.tpAmb)
        self.tpAmb_nsprefix_ = None
        self.CNPJ = CNPJ
        self.validate_TCnpjOpc(self.CNPJ)
        self.CNPJ_nsprefix_ = None
        self.CPF = CPF
        self.validate_TCpf(self.CPF)
        self.CPF_nsprefix_ = None
        self.chNFe = chNFe
        self.validate_TChNFe(self.chNFe)
        self.chNFe_nsprefix_ = None
        self.dhEvento = dhEvento
        self.validate_TDateTimeUTC(self.dhEvento)
        self.dhEvento_nsprefix_ = None
        self.tpEvento = tpEvento
        self.validate_tpEventoType(self.tpEvento)
        self.tpEvento_nsprefix_ = None
        self.nSeqEvento = nSeqEvento
        self.validate_nSeqEventoType(self.nSeqEvento)
        self.nSeqEvento_nsprefix_ = None
        self.verEvento = verEvento
        self.validate_verEventoType(self.verEvento)
        self.verEvento_nsprefix_ = None
        self.detEvento = detEvento
        self.detEvento_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, infEventoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if infEventoType.subclass:
            return infEventoType.subclass(*args_, **kwargs_)
        else:
            return infEventoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TCOrgaoIBGE(self, value):
        result = True
        # Validate type TCOrgaoIBGE, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '90', '91', '92']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TCOrgaoIBGE' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_TAmb(self, value):
        result = True
        # Validate type TAmb, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1', '2']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TAmb' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_TCnpjOpc(self, value):
        result = True
        # Validate type TCnpjOpc, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 14:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TCnpjOpc' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TCnpjOpc_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TCnpjOpc_patterns_, ))
                result = False
        return result
    validate_TCnpjOpc_patterns_ = [['^([0-9]{0}|[0-9]{14})$']]
    def validate_TCpf(self, value):
        result = True
        # Validate type TCpf, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 11:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TCpf' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TCpf_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TCpf_patterns_, ))
                result = False
        return result
    validate_TCpf_patterns_ = [['^([0-9]{11})$']]
    def validate_TChNFe(self, value):
        result = True
        # Validate type TChNFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TChNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TChNFe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TChNFe_patterns_, ))
                result = False
        return result
    validate_TChNFe_patterns_ = [['^([0-9]{44})$']]
    def validate_TDateTimeUTC(self, value):
        result = True
        # Validate type TDateTimeUTC, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TDateTimeUTC_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TDateTimeUTC_patterns_, ))
                result = False
        return result
    validate_TDateTimeUTC_patterns_ = [['^((((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\\d):[0-5]\\d:[0-5]\\d([\\-,\\+](0[0-9]|10|11):00|([\\+](12):00)))$']]
    def validate_tpEventoType(self, value):
        result = True
        # Validate type tpEventoType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpEventoType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpEventoType_patterns_, ))
                result = False
        return result
    validate_tpEventoType_patterns_ = [['^([0-9]{6})$']]
    def validate_nSeqEventoType(self, value):
        result = True
        # Validate type nSeqEventoType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_nSeqEventoType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nSeqEventoType_patterns_, ))
                result = False
        return result
    validate_nSeqEventoType_patterns_ = [['^([1-9][0-9]{0,1})$']]
    def validate_verEventoType(self, value):
        result = True
        # Validate type verEventoType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def validate_IdType(self, value):
        # Validate type IdType, a restriction on xs:ID.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_IdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_IdType_patterns_, ))
    validate_IdType_patterns_ = [['^(ID[0-9]{52})$']]
    def hasContent_(self):
        if (
            self.cOrgao is not None or
            self.tpAmb is not None or
            self.CNPJ is not None or
            self.CPF is not None or
            self.chNFe is not None or
            self.dhEvento is not None or
            self.tpEvento is not None or
            self.nSeqEvento is not None or
            self.verEvento is not None or
            self.detEvento is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infEventoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('infEventoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'infEventoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='infEventoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='infEventoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='infEventoType'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infEventoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.cOrgao is not None:
            namespaceprefix_ = self.cOrgao_nsprefix_ + ':' if (UseCapturedNS_ and self.cOrgao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scOrgao>%s</%scOrgao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cOrgao), input_name='cOrgao')), namespaceprefix_ , eol_))
        if self.tpAmb is not None:
            namespaceprefix_ = self.tpAmb_nsprefix_ + ':' if (UseCapturedNS_ and self.tpAmb_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stpAmb>%s</%stpAmb>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tpAmb), input_name='tpAmb')), namespaceprefix_ , eol_))
        if self.CNPJ is not None:
            namespaceprefix_ = self.CNPJ_nsprefix_ + ':' if (UseCapturedNS_ and self.CNPJ_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCNPJ>%s</%sCNPJ>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CNPJ), input_name='CNPJ')), namespaceprefix_ , eol_))
        if self.CPF is not None:
            namespaceprefix_ = self.CPF_nsprefix_ + ':' if (UseCapturedNS_ and self.CPF_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCPF>%s</%sCPF>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CPF), input_name='CPF')), namespaceprefix_ , eol_))
        if self.chNFe is not None:
            namespaceprefix_ = self.chNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.chNFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%schNFe>%s</%schNFe>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.chNFe), input_name='chNFe')), namespaceprefix_ , eol_))
        if self.dhEvento is not None:
            namespaceprefix_ = self.dhEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.dhEvento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdhEvento>%s</%sdhEvento>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.dhEvento), input_name='dhEvento')), namespaceprefix_ , eol_))
        if self.tpEvento is not None:
            namespaceprefix_ = self.tpEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.tpEvento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stpEvento>%s</%stpEvento>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tpEvento), input_name='tpEvento')), namespaceprefix_ , eol_))
        if self.nSeqEvento is not None:
            namespaceprefix_ = self.nSeqEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.nSeqEvento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snSeqEvento>%s</%snSeqEvento>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.nSeqEvento), input_name='nSeqEvento')), namespaceprefix_ , eol_))
        if self.verEvento is not None:
            namespaceprefix_ = self.verEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.verEvento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sverEvento>%s</%sverEvento>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.verEvento), input_name='verEvento')), namespaceprefix_ , eol_))
        if self.detEvento is not None:
            namespaceprefix_ = self.detEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.detEvento_nsprefix_) else ''
            self.detEvento.export(outfile, level, namespaceprefix_, namespacedef_='', name_='detEvento', pretty_print=pretty_print)
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
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
            self.validate_IdType(self.Id)    # validate type IdType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'cOrgao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cOrgao')
            value_ = self.gds_validate_string(value_, node, 'cOrgao')
            self.cOrgao = value_
            self.cOrgao_nsprefix_ = child_.prefix
            # validate type TCOrgaoIBGE
            self.validate_TCOrgaoIBGE(self.cOrgao)
        elif nodeName_ == 'tpAmb':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tpAmb')
            value_ = self.gds_validate_string(value_, node, 'tpAmb')
            self.tpAmb = value_
            self.tpAmb_nsprefix_ = child_.prefix
            # validate type TAmb
            self.validate_TAmb(self.tpAmb)
        elif nodeName_ == 'CNPJ':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CNPJ')
            value_ = self.gds_validate_string(value_, node, 'CNPJ')
            self.CNPJ = value_
            self.CNPJ_nsprefix_ = child_.prefix
            # validate type TCnpjOpc
            self.validate_TCnpjOpc(self.CNPJ)
        elif nodeName_ == 'CPF':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CPF')
            value_ = self.gds_validate_string(value_, node, 'CPF')
            self.CPF = value_
            self.CPF_nsprefix_ = child_.prefix
            # validate type TCpf
            self.validate_TCpf(self.CPF)
        elif nodeName_ == 'chNFe':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'chNFe')
            value_ = self.gds_validate_string(value_, node, 'chNFe')
            self.chNFe = value_
            self.chNFe_nsprefix_ = child_.prefix
            # validate type TChNFe
            self.validate_TChNFe(self.chNFe)
        elif nodeName_ == 'dhEvento':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dhEvento')
            value_ = self.gds_validate_string(value_, node, 'dhEvento')
            self.dhEvento = value_
            self.dhEvento_nsprefix_ = child_.prefix
            # validate type TDateTimeUTC
            self.validate_TDateTimeUTC(self.dhEvento)
        elif nodeName_ == 'tpEvento':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tpEvento')
            value_ = self.gds_validate_string(value_, node, 'tpEvento')
            self.tpEvento = value_
            self.tpEvento_nsprefix_ = child_.prefix
            # validate type tpEventoType
            self.validate_tpEventoType(self.tpEvento)
        elif nodeName_ == 'nSeqEvento':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nSeqEvento')
            value_ = self.gds_validate_string(value_, node, 'nSeqEvento')
            self.nSeqEvento = value_
            self.nSeqEvento_nsprefix_ = child_.prefix
            # validate type nSeqEventoType
            self.validate_nSeqEventoType(self.nSeqEvento)
        elif nodeName_ == 'verEvento':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'verEvento')
            value_ = self.gds_validate_string(value_, node, 'verEvento')
            self.verEvento = value_
            self.verEvento_nsprefix_ = child_.prefix
            # validate type verEventoType
            self.validate_verEventoType(self.verEvento)
        elif nodeName_ == 'detEvento':
            obj_ = detEventoType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.detEvento = obj_
            obj_.original_tagname_ = 'detEvento'
# end class infEventoType


class detEventoType(GeneratedsSuper):
    """Detalhe Específico do Evento"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('__ANY__', '__ANY__', 1, 0, {'maxOccurs': 'unbounded', 'processContents': 'skip'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_
        self.anyAttributes_ = {}
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, detEventoType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if detEventoType.subclass:
            return detEventoType.subclass(*args_, **kwargs_)
        else:
            return detEventoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.anytypeobjs_
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='detEventoType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('detEventoType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'detEventoType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='detEventoType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='detEventoType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='detEventoType'):
        unique_counter = 0
        for name, value in self.anyAttributes_.items():
            xsinamespaceprefix = 'xsi'
            xsinamespace1 = 'http://www.w3.org/2001/XMLSchema-instance'
            xsinamespace2 = '{%s}' % (xsinamespace1, )
            if name.startswith(xsinamespace2):
                name1 = name[len(xsinamespace2):]
                name2 = '%s:%s' % (xsinamespaceprefix, name1, )
                if name2 not in already_processed:
                    already_processed.add(name2)
                    outfile.write(' %s=%s' % (name2, quote_attrib(value), ))
            else:
                mo = re_.match(Namespace_extract_pat_, name)
                if mo is not None:
                    namespace, name = mo.group(1, 2)
                    if name not in already_processed:
                        already_processed.add(name)
                        if namespace == 'http://www.w3.org/XML/1998/namespace':
                            outfile.write(' %s=%s' % (
                                name, quote_attrib(value), ))
                        else:
                            unique_counter += 1
                            outfile.write(' xmlns:%d="%s"' % (
                                unique_counter, namespace, ))
                            outfile.write(' %d:%s=%s' % (
                                unique_counter, name, quote_attrib(value), ))
                else:
                    if name not in already_processed:
                        already_processed.add(name)
                        outfile.write(' %s=%s' % (
                            name, quote_attrib(value), ))
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='detEventoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(obj_)
                outfile.write('\n')
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
        self.anyAttributes_ = {}
        for name, value in attrs.items():
            if name not in already_processed:
                self.anyAttributes_[name] = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        content_ = self.gds_build_any(child_, 'detEventoType')
        self.add_anytypeobjs_(content_)
# end class detEventoType


class infEventoType1(GeneratedsSuper):
    """Identificação do destinatpario da NF-e"""
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Id', 'IdType4', 0, 1, {'use': 'optional'}),
        MemberSpec_('tpAmb', ['TAmb', 'xs:string'], 0, 0, {'name': 'tpAmb', 'type': 'xs:string'}, None),
        MemberSpec_('verAplic', ['TVerAplic', 'nfe:TString'], 0, 0, {'name': 'verAplic', 'type': 'xs:string'}, None),
        MemberSpec_('cOrgao', ['TCOrgaoIBGE', 'xs:string'], 0, 0, {'name': 'cOrgao', 'type': 'xs:string'}, None),
        MemberSpec_('cStat', ['TStat', 'xs:string'], 0, 0, {'name': 'cStat', 'type': 'xs:string'}, None),
        MemberSpec_('xMotivo', ['TMotivo', 'nfe:TString'], 0, 0, {'name': 'xMotivo', 'type': 'xs:string'}, None),
        MemberSpec_('chNFe', ['TChNFe', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'chNFe', 'type': 'xs:string'}, None),
        MemberSpec_('tpEvento', ['tpEventoType2', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'tpEvento', 'type': 'xs:string'}, None),
        MemberSpec_('xEvento', ['xEventoType', 'TString', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'xEvento', 'type': 'xs:string'}, None),
        MemberSpec_('nSeqEvento', ['nSeqEventoType3', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'nSeqEvento', 'type': 'xs:string'}, None),
        MemberSpec_('CNPJDest', ['TCnpjOpc', 'xs:string'], 0, 1, {'name': 'CNPJDest', 'type': 'xs:string'}, 2),
        MemberSpec_('CPFDest', ['TCpf', 'xs:string'], 0, 1, {'name': 'CPFDest', 'type': 'xs:string'}, 2),
        MemberSpec_('emailDest', ['emailDestType', 'TString', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'emailDest', 'type': 'xs:string'}, None),
        MemberSpec_('dhRegEvento', ['TDateTimeUTC', 'xs:string'], 0, 0, {'name': 'dhRegEvento', 'type': 'xs:string'}, None),
        MemberSpec_('nProt', ['TProt', 'xs:string'], 0, 1, {'minOccurs': '0', 'name': 'nProt', 'type': 'xs:string'}, None),
    ]
    subclass = None
    superclass = None
    def __init__(self, Id=None, tpAmb=None, verAplic=None, cOrgao=None, cStat=None, xMotivo=None, chNFe=None, tpEvento=None, xEvento=None, nSeqEvento=None, CNPJDest=None, CPFDest=None, emailDest=None, dhRegEvento=None, nProt=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Id = _cast(None, Id)
        self.Id_nsprefix_ = None
        self.tpAmb = tpAmb
        self.validate_TAmb(self.tpAmb)
        self.tpAmb_nsprefix_ = None
        self.verAplic = verAplic
        self.validate_TVerAplic(self.verAplic)
        self.verAplic_nsprefix_ = None
        self.cOrgao = cOrgao
        self.validate_TCOrgaoIBGE(self.cOrgao)
        self.cOrgao_nsprefix_ = None
        self.cStat = cStat
        self.validate_TStat(self.cStat)
        self.cStat_nsprefix_ = None
        self.xMotivo = xMotivo
        self.validate_TMotivo(self.xMotivo)
        self.xMotivo_nsprefix_ = None
        self.chNFe = chNFe
        self.validate_TChNFe(self.chNFe)
        self.chNFe_nsprefix_ = None
        self.tpEvento = tpEvento
        self.validate_tpEventoType2(self.tpEvento)
        self.tpEvento_nsprefix_ = None
        self.xEvento = xEvento
        self.validate_xEventoType(self.xEvento)
        self.xEvento_nsprefix_ = None
        self.nSeqEvento = nSeqEvento
        self.validate_nSeqEventoType3(self.nSeqEvento)
        self.nSeqEvento_nsprefix_ = None
        self.CNPJDest = CNPJDest
        self.validate_TCnpjOpc(self.CNPJDest)
        self.CNPJDest_nsprefix_ = None
        self.CPFDest = CPFDest
        self.validate_TCpf(self.CPFDest)
        self.CPFDest_nsprefix_ = None
        self.emailDest = emailDest
        self.validate_emailDestType(self.emailDest)
        self.emailDest_nsprefix_ = None
        self.dhRegEvento = dhRegEvento
        self.validate_TDateTimeUTC(self.dhRegEvento)
        self.dhRegEvento_nsprefix_ = None
        self.nProt = nProt
        self.validate_TProt(self.nProt)
        self.nProt_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, infEventoType1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if infEventoType1.subclass:
            return infEventoType1.subclass(*args_, **kwargs_)
        else:
            return infEventoType1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TAmb(self, value):
        result = True
        # Validate type TAmb, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['1', '2']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TAmb' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
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
    def validate_TCOrgaoIBGE(self, value):
        result = True
        # Validate type TCOrgaoIBGE, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '35', '41', '42', '43', '50', '51', '52', '53', '90', '91', '92']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on TCOrgaoIBGE' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_TStat(self, value):
        result = True
        # Validate type TStat, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TStat' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
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
    def validate_TChNFe(self, value):
        result = True
        # Validate type TChNFe, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 44:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TChNFe' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TChNFe_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TChNFe_patterns_, ))
                result = False
        return result
    validate_TChNFe_patterns_ = [['^([0-9]{44})$']]
    def validate_tpEventoType2(self, value):
        result = True
        # Validate type tpEventoType2, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_tpEventoType2_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_tpEventoType2_patterns_, ))
                result = False
        return result
    validate_tpEventoType2_patterns_ = [['^([0-9]{6})$']]
    def validate_xEventoType(self, value):
        result = True
        # Validate type xEventoType, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on xEventoType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 5:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on xEventoType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_xEventoType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_xEventoType_patterns_, ))
                result = False
        return result
    validate_xEventoType_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_nSeqEventoType3(self, value):
        result = True
        # Validate type nSeqEventoType3, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_nSeqEventoType3_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_nSeqEventoType3_patterns_, ))
                result = False
        return result
    validate_nSeqEventoType3_patterns_ = [['^([1-9][0-9]{0,1})$']]
    def validate_TCnpjOpc(self, value):
        result = True
        # Validate type TCnpjOpc, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 14:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TCnpjOpc' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TCnpjOpc_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TCnpjOpc_patterns_, ))
                result = False
        return result
    validate_TCnpjOpc_patterns_ = [['^([0-9]{0}|[0-9]{14})$']]
    def validate_TCpf(self, value):
        result = True
        # Validate type TCpf, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 11:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TCpf' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TCpf_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TCpf_patterns_, ))
                result = False
        return result
    validate_TCpf_patterns_ = [['^([0-9]{11})$']]
    def validate_emailDestType(self, value):
        result = True
        # Validate type emailDestType, a restriction on TString.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 60:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on emailDestType' % {"value": value, "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on emailDestType' % {"value" : value, "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_emailDestType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_emailDestType_patterns_, ))
                result = False
        return result
    validate_emailDestType_patterns_ = [['^([!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1})$']]
    def validate_TDateTimeUTC(self, value):
        result = True
        # Validate type TDateTimeUTC, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_TDateTimeUTC_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TDateTimeUTC_patterns_, ))
                result = False
        return result
    validate_TDateTimeUTC_patterns_ = [['^((((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))T(20|21|22|23|[0-1]\\d):[0-5]\\d:[0-5]\\d([\\-,\\+](0[0-9]|10|11):00|([\\+](12):00)))$']]
    def validate_TProt(self, value):
        result = True
        # Validate type TProt, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 15:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TProt' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TProt_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TProt_patterns_, ))
                result = False
        return result
    validate_TProt_patterns_ = [['^([0-9]{15})$']]
    def validate_IdType4(self, value):
        # Validate type IdType4, a restriction on xs:ID.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_IdType4_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_IdType4_patterns_, ))
    validate_IdType4_patterns_ = [['^(ID[0-9]{15})$']]
    def hasContent_(self):
        if (
            self.tpAmb is not None or
            self.verAplic is not None or
            self.cOrgao is not None or
            self.cStat is not None or
            self.xMotivo is not None or
            self.chNFe is not None or
            self.tpEvento is not None or
            self.xEvento is not None or
            self.nSeqEvento is not None or
            self.CNPJDest is not None or
            self.CPFDest is not None or
            self.emailDest is not None or
            self.dhRegEvento is not None or
            self.nProt is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infEventoType1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('infEventoType1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'infEventoType1':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='infEventoType1')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='infEventoType1', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='infEventoType1'):
        if self.Id is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            outfile.write(' Id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.Id), input_name='Id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='infEventoType1', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.tpAmb is not None:
            namespaceprefix_ = self.tpAmb_nsprefix_ + ':' if (UseCapturedNS_ and self.tpAmb_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stpAmb>%s</%stpAmb>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tpAmb), input_name='tpAmb')), namespaceprefix_ , eol_))
        if self.verAplic is not None:
            namespaceprefix_ = self.verAplic_nsprefix_ + ':' if (UseCapturedNS_ and self.verAplic_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sverAplic>%s</%sverAplic>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.verAplic), input_name='verAplic')), namespaceprefix_ , eol_))
        if self.cOrgao is not None:
            namespaceprefix_ = self.cOrgao_nsprefix_ + ':' if (UseCapturedNS_ and self.cOrgao_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scOrgao>%s</%scOrgao>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cOrgao), input_name='cOrgao')), namespaceprefix_ , eol_))
        if self.cStat is not None:
            namespaceprefix_ = self.cStat_nsprefix_ + ':' if (UseCapturedNS_ and self.cStat_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scStat>%s</%scStat>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.cStat), input_name='cStat')), namespaceprefix_ , eol_))
        if self.xMotivo is not None:
            namespaceprefix_ = self.xMotivo_nsprefix_ + ':' if (UseCapturedNS_ and self.xMotivo_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxMotivo>%s</%sxMotivo>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xMotivo), input_name='xMotivo')), namespaceprefix_ , eol_))
        if self.chNFe is not None:
            namespaceprefix_ = self.chNFe_nsprefix_ + ':' if (UseCapturedNS_ and self.chNFe_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%schNFe>%s</%schNFe>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.chNFe), input_name='chNFe')), namespaceprefix_ , eol_))
        if self.tpEvento is not None:
            namespaceprefix_ = self.tpEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.tpEvento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stpEvento>%s</%stpEvento>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tpEvento), input_name='tpEvento')), namespaceprefix_ , eol_))
        if self.xEvento is not None:
            namespaceprefix_ = self.xEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.xEvento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sxEvento>%s</%sxEvento>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.xEvento), input_name='xEvento')), namespaceprefix_ , eol_))
        if self.nSeqEvento is not None:
            namespaceprefix_ = self.nSeqEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.nSeqEvento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snSeqEvento>%s</%snSeqEvento>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.nSeqEvento), input_name='nSeqEvento')), namespaceprefix_ , eol_))
        if self.CNPJDest is not None:
            namespaceprefix_ = self.CNPJDest_nsprefix_ + ':' if (UseCapturedNS_ and self.CNPJDest_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCNPJDest>%s</%sCNPJDest>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CNPJDest), input_name='CNPJDest')), namespaceprefix_ , eol_))
        if self.CPFDest is not None:
            namespaceprefix_ = self.CPFDest_nsprefix_ + ':' if (UseCapturedNS_ and self.CPFDest_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCPFDest>%s</%sCPFDest>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CPFDest), input_name='CPFDest')), namespaceprefix_ , eol_))
        if self.emailDest is not None:
            namespaceprefix_ = self.emailDest_nsprefix_ + ':' if (UseCapturedNS_ and self.emailDest_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%semailDest>%s</%semailDest>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.emailDest), input_name='emailDest')), namespaceprefix_ , eol_))
        if self.dhRegEvento is not None:
            namespaceprefix_ = self.dhRegEvento_nsprefix_ + ':' if (UseCapturedNS_ and self.dhRegEvento_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdhRegEvento>%s</%sdhRegEvento>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.dhRegEvento), input_name='dhRegEvento')), namespaceprefix_ , eol_))
        if self.nProt is not None:
            namespaceprefix_ = self.nProt_nsprefix_ + ':' if (UseCapturedNS_ and self.nProt_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%snProt>%s</%snProt>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.nProt), input_name='nProt')), namespaceprefix_ , eol_))
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
        value = find_attr_value_('Id', node)
        if value is not None and 'Id' not in already_processed:
            already_processed.add('Id')
            self.Id = value
            self.validate_IdType4(self.Id)    # validate type IdType4
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'tpAmb':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tpAmb')
            value_ = self.gds_validate_string(value_, node, 'tpAmb')
            self.tpAmb = value_
            self.tpAmb_nsprefix_ = child_.prefix
            # validate type TAmb
            self.validate_TAmb(self.tpAmb)
        elif nodeName_ == 'verAplic':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'verAplic')
            value_ = self.gds_validate_string(value_, node, 'verAplic')
            self.verAplic = value_
            self.verAplic_nsprefix_ = child_.prefix
            # validate type TVerAplic
            self.validate_TVerAplic(self.verAplic)
        elif nodeName_ == 'cOrgao':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'cOrgao')
            value_ = self.gds_validate_string(value_, node, 'cOrgao')
            self.cOrgao = value_
            self.cOrgao_nsprefix_ = child_.prefix
            # validate type TCOrgaoIBGE
            self.validate_TCOrgaoIBGE(self.cOrgao)
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
        elif nodeName_ == 'chNFe':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'chNFe')
            value_ = self.gds_validate_string(value_, node, 'chNFe')
            self.chNFe = value_
            self.chNFe_nsprefix_ = child_.prefix
            # validate type TChNFe
            self.validate_TChNFe(self.chNFe)
        elif nodeName_ == 'tpEvento':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tpEvento')
            value_ = self.gds_validate_string(value_, node, 'tpEvento')
            self.tpEvento = value_
            self.tpEvento_nsprefix_ = child_.prefix
            # validate type tpEventoType2
            self.validate_tpEventoType2(self.tpEvento)
        elif nodeName_ == 'xEvento':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'xEvento')
            value_ = self.gds_validate_string(value_, node, 'xEvento')
            self.xEvento = value_
            self.xEvento_nsprefix_ = child_.prefix
            # validate type xEventoType
            self.validate_xEventoType(self.xEvento)
        elif nodeName_ == 'nSeqEvento':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nSeqEvento')
            value_ = self.gds_validate_string(value_, node, 'nSeqEvento')
            self.nSeqEvento = value_
            self.nSeqEvento_nsprefix_ = child_.prefix
            # validate type nSeqEventoType3
            self.validate_nSeqEventoType3(self.nSeqEvento)
        elif nodeName_ == 'CNPJDest':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CNPJDest')
            value_ = self.gds_validate_string(value_, node, 'CNPJDest')
            self.CNPJDest = value_
            self.CNPJDest_nsprefix_ = child_.prefix
            # validate type TCnpjOpc
            self.validate_TCnpjOpc(self.CNPJDest)
        elif nodeName_ == 'CPFDest':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CPFDest')
            value_ = self.gds_validate_string(value_, node, 'CPFDest')
            self.CPFDest = value_
            self.CPFDest_nsprefix_ = child_.prefix
            # validate type TCpf
            self.validate_TCpf(self.CPFDest)
        elif nodeName_ == 'emailDest':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'emailDest')
            value_ = self.gds_validate_string(value_, node, 'emailDest')
            self.emailDest = value_
            self.emailDest_nsprefix_ = child_.prefix
            # validate type emailDestType
            self.validate_emailDestType(self.emailDest)
        elif nodeName_ == 'dhRegEvento':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'dhRegEvento')
            value_ = self.gds_validate_string(value_, node, 'dhRegEvento')
            self.dhRegEvento = value_
            self.dhRegEvento_nsprefix_ = child_.prefix
            # validate type TDateTimeUTC
            self.validate_TDateTimeUTC(self.dhRegEvento)
        elif nodeName_ == 'nProt':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'nProt')
            value_ = self.gds_validate_string(value_, node, 'nProt')
            self.nProt = value_
            self.nProt_nsprefix_ = child_.prefix
            # validate type TProt
            self.validate_TProt(self.nProt)
# end class infEventoType1


class CanonicalizationMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'anyURI', 0, 0, {'use': 'required'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, Algorithm='http://www.w3.org/TR/2001/REC-xml-c14n-20010315', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CanonicalizationMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CanonicalizationMethodType.subclass:
            return CanonicalizationMethodType.subclass(*args_, **kwargs_)
        else:
            return CanonicalizationMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CanonicalizationMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CanonicalizationMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'CanonicalizationMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CanonicalizationMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CanonicalizationMethodType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='CanonicalizationMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='CanonicalizationMethodType', fromsubclass_=False, pretty_print=True):
        pass
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
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class CanonicalizationMethodType


class SignatureMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'anyURI', 0, 0, {'use': 'required'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, Algorithm='http://www.w3.org/2000/09/xmldsig#rsa-sha1', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, SignatureMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SignatureMethodType.subclass:
            return SignatureMethodType.subclass(*args_, **kwargs_)
        else:
            return SignatureMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SignatureMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('SignatureMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'SignatureMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='SignatureMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='SignatureMethodType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='SignatureMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='SignatureMethodType', fromsubclass_=False, pretty_print=True):
        pass
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
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class SignatureMethodType


class DigestMethodType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    member_data_items_ = [
        MemberSpec_('Algorithm', 'anyURI', 0, 0, {'use': 'required'}),
    ]
    subclass = None
    superclass = None
    def __init__(self, Algorithm='http://www.w3.org/2000/09/xmldsig#sha1', gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.Algorithm = _cast(None, Algorithm)
        self.Algorithm_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DigestMethodType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DigestMethodType.subclass:
            return DigestMethodType.subclass(*args_, **kwargs_)
        else:
            return DigestMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DigestMethodType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DigestMethodType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None and name_ == 'DigestMethodType':
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DigestMethodType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DigestMethodType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DigestMethodType'):
        if self.Algorithm is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            outfile.write(' Algorithm=%s' % (quote_attrib(self.Algorithm), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='', name_='DigestMethodType', fromsubclass_=False, pretty_print=True):
        pass
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
        value = find_attr_value_('Algorithm', node)
        if value is not None and 'Algorithm' not in already_processed:
            already_processed.add('Algorithm')
            self.Algorithm = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DigestMethodType


GDSClassesMapping = {
    'Signature': SignatureType,
    'retConsSitNFe': TRetConsSitNFe,
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
        rootTag = 'TRetConsSitNFe'
        rootClass = TRetConsSitNFe
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
        rootTag = 'TRetConsSitNFe'
        rootClass = TRetConsSitNFe
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
        rootTag = 'TRetConsSitNFe'
        rootClass = TRetConsSitNFe
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
        rootTag = 'TRetConsSitNFe'
        rootClass = TRetConsSitNFe
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from retConsSitNFe import *\n\n')
        sys.stdout.write('import retConsSitNFe as model_\n\n')
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
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TCodMunIBGE',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TChNFe',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TProt',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TRec', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TStat',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TCnpj',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TCnpjVar',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TCnpjOpc',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TCpf', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TCpfVar',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0104v',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0204v',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0302a04',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0302a04Opc',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0302Max100',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0304Max100',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0302a04Max100',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_0803v',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1104',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1104v',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1104Opc',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1110v',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1203',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1204',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1204v',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1204Opc',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1204temperatura',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1302',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDec_1302Opc',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TIeDest',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TIeDestNaoIsento',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TIeST',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TIe', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TMod', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TNF', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TSerie',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TUf', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TUfEmi',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TAmb', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TVerAplic',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TMotivo',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TJust',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TServ',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('Tano', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TMed', 'tiposBasico_v4.00.xsd', 'ST'),
                                        ('TString',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TData',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TTime',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TDateTimeUTC',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TPlaca',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TCOrgaoIBGE',
                                         'tiposBasico_v4.00.xsd',
                                         'ST'),
                                        ('TVerNFe',
                                         'leiauteConsSitNFe_v4.00.xsd',
                                         'ST'),
                                        ('TVerCancNFe',
                                         'leiauteConsSitNFe_v4.00.xsd',
                                         'ST'),
                                        ('TVerEvento',
                                         'leiauteConsSitNFe_v4.00.xsd',
                                         'ST'),
                                        ('TRetVerEvento',
                                         'leiauteConsSitNFe_v4.00.xsd',
                                         'ST'),
                                        ('TVerConsSitNFe',
                                         'leiauteConsSitNFe_v4.00.xsd',
                                         'ST'),
                                        ('TConsSitNFe',
                                         'leiauteConsSitNFe_v4.00.xsd',
                                         'CT'),
                                        ('TRetConsSitNFe',
                                         'leiauteConsSitNFe_v4.00.xsd',
                                         'CT'),
                                        ('TProtNFe',
                                         'leiauteConsSitNFe_v4.00.xsd',
                                         'CT'),
                                        ('TRetCancNFe',
                                         'leiauteConsSitNFe_v4.00.xsd',
                                         'CT'),
                                        ('TEvento',
                                         'leiauteConsSitNFe_v4.00.xsd',
                                         'CT'),
                                        ('TRetEvento',
                                         'leiauteConsSitNFe_v4.00.xsd',
                                         'CT'),
                                        ('TProcEvento',
                                         'leiauteConsSitNFe_v4.00.xsd',
                                         'CT')],
 'http://www.w3.org/2000/09/xmldsig#': [('DigestValueType',
                                         'xmldsig-core-schema_v1.01.xsd',
                                         'ST'),
                                        ('TTransformURI',
                                         'xmldsig-core-schema_v1.01.xsd',
                                         'ST'),
                                        ('SignatureType',
                                         'xmldsig-core-schema_v1.01.xsd',
                                         'CT'),
                                        ('SignatureValueType',
                                         'xmldsig-core-schema_v1.01.xsd',
                                         'CT'),
                                        ('SignedInfoType',
                                         'xmldsig-core-schema_v1.01.xsd',
                                         'CT'),
                                        ('ReferenceType',
                                         'xmldsig-core-schema_v1.01.xsd',
                                         'CT'),
                                        ('TransformsType',
                                         'xmldsig-core-schema_v1.01.xsd',
                                         'CT'),
                                        ('TransformType',
                                         'xmldsig-core-schema_v1.01.xsd',
                                         'CT'),
                                        ('KeyInfoType',
                                         'xmldsig-core-schema_v1.01.xsd',
                                         'CT'),
                                        ('X509DataType',
                                         'xmldsig-core-schema_v1.01.xsd',
                                         'CT')]}

__all__ = [
    "CanonicalizationMethodType",
    "DigestMethodType",
    "KeyInfoType",
    "ReferenceType",
    "SignatureMethodType",
    "SignatureType",
    "SignatureValueType",
    "SignedInfoType",
    "TConsSitNFe",
    "TEvento",
    "TProcEvento",
    "TProtNFe",
    "TRetCancNFe",
    "TRetConsSitNFe",
    "TRetEvento",
    "TransformType",
    "TransformsType",
    "X509DataType",
    "detEventoType",
    "infCancType",
    "infEventoType",
    "infEventoType1",
    "infProtType"
]
