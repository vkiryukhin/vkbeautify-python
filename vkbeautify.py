import re

def createShiftArr(step):
    shift = ['\n']
    ix = 0
    space = ' '*step if type(step) is int else step

    while ix<100:
        shift.append(shift[ix]+space)
        ix = ix+1

    return shift;

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
    ix = 0
    shift = createShiftArr(step) if step else createShiftArr(step)

    while ix<len(ar):
        if re.search('\{', ar[ix]):
            str += shift[deep]+ar[ix]
            deep = deep+1
        elif re.search('\}', ar[ix]):
            deep = deep-1
            str += shift[deep]+ar[ix]
        elif re.search('\*\\\\', ar[ix]):
            str += shift[deep]+ar[ix]
        else:
            str += shift[deep]+ar[ix]

        ix += 1

    return str


#
# Minify CSS
#

def cssmin(text, preserveComments=True):

    if preserveComments:
        str = text
    else:
        str = re.sub('\/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+\/', '', text)

    str = re.sub('\s{1,}', ' ', str)
    str = re.sub('\{\s{1,}', '{', str)
    str = re.sub('\}\s{1,}', '}', str)
    str = re.sub('\;\s{1,}', ';', str)
    str = re.sub('\/\*\s{1,}', '/*', str)
    str = re.sub('\*\/\s{1,}', '*/', str)

    return str













