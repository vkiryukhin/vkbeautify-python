import re

def createShiftArr(step):
    shift = []
    ix = 0

    shift.append('\n') # array of shifts

    if type(step) is int :  # argument is integer
        space = ' '*step
    else:                   # argument is string
        space = step;

    while ix<100:
        shift.append(shift[ix]+space)
        ix = ix+1

    return shift;

#
# css
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


    length = len(ar)
    deep = 0
    str = ''
    ix = 0

    if step:
        shift = createShiftArr(step)
    else:
        createShiftArr(4)


    while ix<length:
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

        ix = ix+1


    return str




