#
# vkBeautify - python plugin to pretty-print or minify text in XML, JSON and CSS formats.
#
# Version - 0.3.0
# Copyright (c) 2016 Vadim Kiryukhin
# vkiryukhin @ gmail.com
# https://github.com/vkiryukhin/vkbeautify-python
#
# MIT license:
#   http://www.opensource.org/licenses/mit-license.php
#

import sys, re, os.path

##########################################
#            Interface
##########################################

def xml(src, dest=False, shift=4):
    """Beautify XML

    Args:
        src: xml string or path-to-file with text to beautify (mandatory)
        dest: path-to-file to save beautified xml string; if file doesn't exist
              it is created automatically; (optional)
              if this arg is skept function returns string
        shift: can be either integer or string
                1) if int - number of spaces in tab, for example shift=8
                <a>
                        <b></b>
                </a>
               2) if string - pattern, for example shift='....'
                <a>
                ....<b></b>
                </a>

    Returns: 1) beautified XML string if dest is not provided
             2) length of saved file if dest is provided

    Example:
            xml('path/to/file.xml')
            xml('path/to/file.xml', 'path/to/save/result.xml')
            xml('path/to/file.xml', 8)
            xml('path/to/file.xml', '____')
            xml('path/to/file.xml', 'path/to/save/result.xml', 2)
    """
    if not dest:
        return _xml(_text(src)) # returns string
    else:
        if type(dest) is int:  # dest is skept, custom pattern provided at dist place
            return _xml(_text(src), dest)
        else:
            with open(dest, 'w') as f2:
                return f2.write(_xml(_text(src), shift))


def json(src, dest=False, shift=4):
    """Beautify JSON

    Args:
        src: JSON string or path-to-file with text to beautify (mandatory)
        dest: path-to-file to save beautified json string; (optional)
              if file doesn't exist it is created automatically;
              if this arg is skept function returns string
        shift: can be either integer or string (optional)
                1) if shift is int: number of spaces in tab, for example shift=8
                <a>
                        <b></b>
                </a>
               2) if shift is string: pattern (for example shift='....' )
                <a>
                ....<b></b>
                </a>

    Returns: 1) beautified JSON string if dest is not provided
             2) length of saved file if dest is provided

    Example:
            json('path/to/file.json')
            json('path/to/file.json', 'path/to/save/result.json')
            json('path/to/file.json', 8)
            json('path/to/file.json', '____')
            json('path/to/file.json', 'path/to/save/result.json', 2)
    """
    if not dest:
        return _json(_text(src)) # returns string
    else:
        if type(dest) is int:  # dest is skept, custom pattern provided at dist place
            return _json(_text(src), dest)
        else:
            with open(dest, 'w') as f2:
                return f2.write(_json(_text(src), shift))


def css(src, dest=False, shift=4):
    """Beautify CSS

    Args:
        src: css string or path-to-file with text to beautify (mandatory)
        dest: path-to-file to save beautified css string; if file doesn't exist
              it is created automatically; (optional)
              if this arg is skept function returns string
        shift: can be either integer or string
                1) if int - number of spaces in tab, for example shift=8
                <a>
                        <b></b>
                </a>
               2) if string - pattern, for example shift='....'
                <a>
                ....<b></b>
                </a>

    Returns: 1) beautified XML string if dest is not provided
             2) length of saved file if dest is provided

    Example:
            css('path/to/file.css')
            css('path/to/file.css', 'path/to/save/result.css')
            css('path/to/file.css', 8)
            css('path/to/file.css', '____')
            css('path/to/file.css', 'path/to/save/result.css', 2)
    """
    if not dest: # all default
        return _css(_text(src))
    else:
        if type(dest) is int:  #dest is skept, custom pattern provided at dist place
            return _css(_text(src), dest)
        else:
            with open(dest, 'w') as f2:
                return f2.write(_css(_text(src), shift))


def _xml_min(src, dest='', preserve_comments=True):
    """Minify XML

    Args:
        src: xml string or path-to-file with text to minify (mandatory)
        dest: path-to-file to save minified xml string; if file doesn't exist
              it is created automatically; (optional)
              if this arg is skept function returns string
        preserve_comments: if set False, all comments are removed from minified text
                           default is True (comments are preserved)

    Returns: 1) minified XML string if dest is not provided
             2) length of saved file if dest is provided

    Example:
            xml.min('path/to/file.xml')
            xml.min('path/to/file.xml', 'path/to/save/result.xml')
            xml.min('path/to/file.xml', False)
            xml.min('path/to/file.xml', 'path/to/save/result.xml', False)
    """

    if dest == '':
        return _xml_min_exec(_text(src)) # returns string
    else:
        if type(dest) is bool:  # dest is skept, custom pattern provided at dist place
            return _xml_min_exec(_text(src), dest)
        else:
            with open(dest, 'w') as f2:
                return f2.write(_xml_min_exec(_text(src), preserve_comments))



def _json_min(src, dest=''):
    """Minify JSON

    Args:
        src: json string or path-to-file with text to minify (mandatory)
        dest: path-to-file to save minified xml string; (optional)
              - if file doesn't exist it is created automatically;
              - if this arg is skept function returns string

    Returns: 1) minified JSON string if dest is not provided
             2) length of saved file if dest is provided

    Example:
            json.min('path/to/file.json')
            json.min('path/to/file.json', 'path/to/save/result.json')
    """

    if dest == '':
        return _json_min_exec(_text(src)) # returns string
    else:
        if type(dest) is bool:  # dest is skept, custom pattern provided at dist place
            return _json_min_exec(_text(src), dest)
        else:
            with open(dest, 'w') as f2:
                return f2.write(_json_min_exec(_text(src)))



def _css_min(src, dest='', preserve_comments=True):
    """Minify CSS

    Args:
        src: css string or path-to-file with text to beautify (mandatory)
        dest: path-to-file to save beautified css string; if file doesn't exist
              it is created automatically; (optional)
              if this arg is skept function returns string
        preserve_comments: if set False, all comments are removed from minified text
                           default is True (comments are preserved)

    Returns: 1) minified CSS string if dest is not provided
             2) length of saved file if dest is provided

    Example:
            css.min('path/to/file.css')
            css.min('path/to/file.css', 'path/to/save/result.css')
            css.min('path/to/file.css', False)
            css.min('path/to/file.css', 'path/to/save/result.css', False)
    """

    if dest == '': # all default
        return _css_min_exec(_text(src))
    else:
        if type(dest) is bool:  #dest is skept, custom pattern provided at dist place
            return _css_min_exec(_text(src), dest)
        else:
            with open(dest, 'w') as f2:
                return f2.write(_css_min_exec(_text(src), preserve_comments))

# to make interface user friendly let's add minify function as attribute
xml.min = _xml_min
json.min = _json_min
css.min = _css_min

##########################################################
#                  XML Processor
##########################################################

def _xml(text, step=4):

    ar = re.sub('>\s{0,}<', "><", text)
    ar = re.sub('<', "~::~<", ar)
    ar = re.sub('\s*xmlns\:', "~::~xmlns:", ar)
    ar = re.sub('\s*xmlns\=', "~::~xmlns=", ar)
    ar = ar.split('~::~')

    length = len(ar)
    inComment = False
    deep = 0
    str = ''
    ix = 0
    shift = _create_shift_arr(step)

    while ix < length:
        # start comment or <![CDATA[...]]> or <!DOCTYPE
        if re.search('<!', ar[ix]):
            str += shift[deep] + ar[ix]
            inComment = True
            # end comment  or <![CDATA[...]]>
            if (re.search('-->', ar[ix]) or
                re.search('\]>', ar[ix]) or
                re.search('!DOCTYPE',ar[ix])
                ):
                inComment = False

        # end comment  or <![CDATA[...]]>
        elif re.search('-->',ar[ix]) or re.search('\]>',ar[ix]):
            str += ar[ix]
            inComment = False
        # <elm></elm>
        elif ( re.search(r'^<\w',ar[ix-1]) and
               re.search(r'^</\w', ar[ix]) and
               (
                 re.search('^<[\w:\-\.\,]+',ar[ix-1]).group(0) ==
                 re.sub('/','', re.search(r'^</[\w:\-\.\,]+', ar[ix]).group(0))
                )
            ):
            str += ar[ix]
            if not inComment:
                deep -= 1

        # <elm>
        elif (re.search('<\w',ar[ix]) and not re.search('<\/',ar[ix])
                                      and not re.search('\/>', ar[ix])):
            if not inComment:
                str += shift[deep]+ar[ix]
                deep += 1
            else:
                str += ar[ix]
         # <elm>...</elm>
        elif re.search('<\w', ar[ix]) and re.search(r'</',ar[ix]):
            str = str + shift[deep]+ar[ix] if not inComment else str + ar[ix]
        # </elm>
        elif re.search(r'</', ar[ix]):
            if not inComment:
                deep -= 1
                str += shift[deep]+ar[ix]
            else:
                str += ar[ix]
        # <elm/>
        elif re.search('\/>', ar[ix]):
            str = str + shift[deep]+ar[ix] if not inComment else str + ar[ix]
        # <? xml ... ?>
        elif re.search('<\?', ar[ix]):
            str += shift[deep]+ar[ix]
        # xmlns
        elif re.search('xmlns\:', ar[ix]) or re.search('xmlns\=',ar[ix]):
            str += shift[deep]+ar[ix];
        else:
            str += ar[ix];

        ix += 1

    return str[1:] if str[0] in ['\n','\r'] else str


def _xml_min_exec (text, preserveComments=True):

    str = re.sub('[ \r\n\t]{1,}xmlns', ' xmlns', text)
    reg_exp = '\<![ \r\n\t]*(--([^\-]|[\r\n]|-[^\-])*--[ \r\n\t]*)\>'

    if not preserveComments:
        str = re.sub(reg_exp, '', str)

    return re.sub('>\s{0,}<', '><', str)


##########################################################
#                  JSON Processor
##########################################################

def _json(text, step=4):

    ar = _json_min_exec(text)

    ar = re.sub("\{", "~::~{~::~", ar)
    ar = re.sub("\[", "[~::~", ar)
    ar = re.sub("\}", "~::~}", ar)
    ar = re.sub("\]", "~::~]", ar)
    ar = re.sub("\"\,", '",~::~', ar)
    ar = re.sub("\,\"", ',~::~"', ar)
    ar = re.sub("\]\,", '],~::~', ar)
    ar = re.sub("~::~\s{0,}~::~", "~::~", ar)
    ar = ar.split('~::~')

    deep = 0
    str = ''

    shift = _create_shift_arr(step)

    for item in ar:
        if re.search('\{', item):
            str += shift[deep] + item
            deep += 1
        elif re.search('\[', item):
            str += shift[deep] + item
            deep += 1
        elif re.search('\]', item):
            deep -= 1
            str += shift[deep] + item
        elif re.search('\}', item):
            deep -= 1
            str += shift[deep] + item
        else:
            str += shift[deep] + item

    str = re.sub('(\[\s*?\])', '[]', str)
    str = re.sub('^\n{1,}',' ', str)

    return str


def _json_min_exec(text):
    str = ''

    str = re.sub('\s{0,}\{\s{0,}', '{', text)
    str = re.sub('\s{0,}\[$', '[', str)
    str = re.sub('\[\s{0,}', '[', str)
    str = re.sub(':\s{0,}\[',':[', str)
    str = re.sub('\s{0,}\}\s{0,}', '}', str)
    str = re.sub('\s{0,}\]\s{0,}',']', str)
    str = re.sub('\"\s{0,}\,', '",', str)
    str = re.sub('\,\s{0,}\"', ',"', str)
    str = re.sub('\"\s{0,}:', '":', str)
    str = re.sub(':\s{0,}\"', ':"', str)
    str = re.sub(':\s{0,}\[', ':[', str)
    str = re.sub('\,\s{0,}\[', ',[', str)
    str = re.sub('\,\s{2,}',   ', ', str)
    str = re.sub('\]\s{0,},\s{0,}\[', '],[', str)

    return str

##########################################################
#                  CSS Processor
##########################################################

def _css(text, step=4):
    ar = re.sub('\s{1,}', ' ', text)
    ar = re.sub('\{', '{~::~', ar)
    ar = re.sub('\{',"{~::~", ar)
    ar = re.sub('\}',"~::~}~::~", ar)
    ar = re.sub('\;',";~::~", ar)
    ar = re.sub('\/\*',"~::~/*", ar)
    ar = re.sub('\*\/',"*/~::~", ar)
    ar = re.sub('~::~\s{0,}~::~',"~::~", ar)
    ar = ar.split('~::~')

    deep = 0
    str = ''
    shift = _create_shift_arr(step)

    for item in ar:
        if re.search('\{', item):
            str += shift[deep]+item
            deep = deep+1
        elif re.search('\}', item):
            deep = deep-1
            str += shift[deep]+item
        elif re.search('\*\\\\', item):
            str += shift[deep]+item
        else:
            str += shift[deep]+item

    return str[1:] if str[0] in ['\n','\r'] else str


def _css_min_exec(text, preserveComments=True):

    str = text
    reg_exp = '\/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+\/'

    if not preserveComments:
        str = re.sub(reg_exp, '', text)

    str = re.sub('\s{1,}', ' ', str)
    str = re.sub('\{\s{1,}', '{', str)
    str = re.sub('\}\s{1,}', '}', str)
    str = re.sub('\;\s{1,}', ';', str)
    str = re.sub('\/\*\s{1,}', '/*', str)
    str = re.sub('\*\/\s{1,}', '*/', str)

    return str

##############################################
#             Helper
##############################################

def _create_shift_arr(step):
    shift = ['\n']
    ix = 0
    space = ' '*step if type(step) is int else step

    while ix < 100:
        shift.append(shift[ix]+space)
        ix = ix + 1

    return shift;


def _text(src):
    if(os.path.isfile(src)):  # load data from file
        with open(src, 'r') as f1:
            return f1.read()

    return src




