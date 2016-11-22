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
    shift = createShiftArr(step)

    while ix < length:
        # start comment or <![CDATA[...]]> or <!DOCTYPE
        if re.search('<!', ar[ix]):
            str += shift[deep]+ar[ix]
            inComment = True
            # end comment  or <![CDATA[...]]>
            if re.search('-->', ar[ix]) or re.search('\]>', ar[ix]) or re.search('!DOCTYPE',ar[ix]):
                inComment = False

        # end comment  or <![CDATA[...]]>
        elif re.search('-->',ar[ix]) or re.search('\]>',ar[ix]):
            str += ar[ix]
            inComment = False
        # <elm></elm>
        elif ( re.search(r'^<\w',ar[ix-1]) and
               re.search(r'^</\w', ar[ix]) and
               ( re.search('^<[\w:\-\.\,]+',ar[ix-1]).group(0) == re.sub('/','', re.search(r'^</[\w:\-\.\,]+', ar[ix]).group(0)) )
            ):
            str += ar[ix]
            if not inComment:
                deep -= 1

        # <elm>
        elif (re.search('<\w',ar[ix]) and not re.search('<\/',ar[ix]) and not re.search('\/>', ar[ix]) ):
            if not inComment:
                str += shift[deep]+ar[ix]
                deep += 1
            else:
                str += ar[ix]
         # <elm>...</elm>
        elif re.search('<\w', ar[ix]) and re.search(r'</',ar[ix]):
            if not inComment:
                str += shift[deep]+ar[ix]
            else:
                str += ar[ix]
        # </elm>
        elif re.search(r'</', ar[ix]):
            #print(ar[ix])
            if not inComment:
                deep -= 1
                str += shift[deep]+ar[ix]
            else:
                str += ar[ix]
        # <elm/>
        elif re.search('\/>', ar[ix]):
            if not inComment:
                str += shift[deep]+ar[ix]
            else:
                str += ar[ix]
        # <? xml ... ?>
        elif re.search('<\?', ar[ix]):
            str += shift[deep]+ar[ix]
        # xmlns
        elif re.search('xmlns\:', ar[ix]) or re.search('xmlns\=',ar[ix]):
            str += shift[deep]+ar[ix];
        else:
            str += ar[ix];


        ix += 1


    return str
'''
        else
         // <elm> //
        if(ar[ix].search(/<\w/) > -1 && ar[ix].search(/<\//) == -1 && ar[ix].search(/\/>/) == -1 ) {
            str = !inComment ? str += shift[deep++]+ar[ix] : str += ar[ix];
        } else
         // <elm>...</elm> //
        if(ar[ix].search(/<\w/) > -1 && ar[ix].search(/<\//) > -1) {
            str = !inComment ? str += shift[deep]+ar[ix] : str += ar[ix];
        } else
        // </elm> //
        if(ar[ix].search(/<\//) > -1) {
            str = !inComment ? str += shift[--deep]+ar[ix] : str += ar[ix];
        } else
        // <elm/> //
        if(ar[ix].search(/\/>/) > -1 ) {
            str = !inComment ? str += shift[deep]+ar[ix] : str += ar[ix];
        } else
        // <? xml ... ?> //
        if(ar[ix].search(/<\?/) > -1) {
            str += shift[deep]+ar[ix];
        } else
        // xmlns //
        if( ar[ix].search(/xmlns\:/) > -1  || ar[ix].search(/xmlns\=/) > -1) {
            str += shift[deep]+ar[ix];
        }

        else {
            str += ar[ix];
        }
    }

    return  (str[0] == '\n') ? str.slice(1) : str;
'''
        ##ix += 1



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
    shift = createShiftArr(step)

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













