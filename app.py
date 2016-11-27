import sys, getopt
import vkbeautify as vkb

def main(argv):

    inputfile = ''
    outputfile = ''
    action = False

    try:
        opts, args = getopt.getopt(argv,"hi:o:a:",["ifile=","ofile=","action="])
    except getopt.GetoptError:
        print('main.py -i <inputfile> -o <outputfile> -a <action>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: app.py -i <inputfile> -o <outputfile> -a <action>')
            print('       beautify: no  <action> ')
            print('       minify:   set <action> to 1')

            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-a", "--action"):
            action = arg

    if not inputfile:
        print('usage: main.py -i <inputfile> -o <outputfile> -a <action>'
               '\ninput file is mandatory')
        sys.exit(2)


    if inputfile[-4:] == '.css':
        if outputfile:
            if action: #minify
                print(vkb.css.min(inputfile, outputfile, True))
            else:
                print(vkb.css(inputfile, outputfile))
        else:
            if action: #minify
                print(vkb.css.min(inputfile, True))
            else:
                print(vkb.css(inputfile))
    else:
        if outputfile:
            if action: #minify
                print(vkb.xml.min(inputfile, outputfile, False))
            else:
                print(vkb.xml(inputfile, outputfile))
        else:
            if action: #minify
                print(vkb.xml.min(inputfile, False))
            else:
                print(vkb.xml(inputfile))


if __name__ =='__main__':
    main(sys.argv[1:])


