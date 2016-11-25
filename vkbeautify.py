import sys, re

##########################################
#            Preprocessor
##########################################

def xmlfile(source, dest=False, act=1):
    return _exec(source, dest, act, 'xml')


def cssfile(source, dest=False, act=1):
    return _exec(source, dest, act, 'css')

#
# Process generic file
#

def _exec(source, dest, act, mode):

    fn = getattr(sys.modules[__name__], mode)
    fn_min = getattr(sys.modules[__name__], mode+'_min')
    text = ''

    with open(source, 'r') as f1:
        text = f1.read()

    if not dest:          # beautify and print
        return fn(text)

    if dest.isdigit():
        if int(dest) == 1: # beautify and print
            return fn(text)
        else:              # minify and print
            return fn_min(text)

    if int(act) == 1:      # beautify and save in dest file
        with open(dest, 'w') as f2:
            return f2.write(fn(text))
    else:                   # minify and save in dest file
        with open(dest, 'w') as f2:
            return f2.write(fn_min(text))


##########################################################
#                     Processor
##########################################################

#
# Beautify XML
#

def xml(text, step=4):

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


#
# minify XML
#

def xml_min (text, preserveComments=True):

    str = re.sub('[ \r\n\t]{1,}xmlns', ' xmlns', text)
    reg_exp = '\<![ \r\n\t]*(--([^\-]|[\r\n]|-[^\-])*--[ \r\n\t]*)\>'

    if not preserveComments:
        str = re.sub(reg_exp, '', str)

    return re.sub('>\s{0,}<', '><', str)


#
# Beautify CSS
#

def css(text, step=4):
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

#
# Minify CSS
#

def css_min(text, preserveComments=True):

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
#             Helpers
##############################################

def _create_shift_arr(step):
    shift = ['\n']
    ix = 0
    space = ' '*step if type(step) is int else step

    while ix < 100:
        shift.append(shift[ix]+space)
        ix = ix + 1

    return shift;


