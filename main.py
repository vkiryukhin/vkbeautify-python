import sys, getopt
import vkbeautify

def main(argv):

    inputfile = ''
    outputfile = ''
    action = '1'
    ext = 'xml'

    try:
        opts, args = getopt.getopt(argv,"hi:o:a:",["ifile=","ofile=","action="])
    except getopt.GetoptError:
        print('main.py -i <inputfile> -o <outputfile> -a <action>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -i <inputfile> -o <outputfile> -a <action>')
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
            print(vkbeautify.cssfile(inputfile, outputfile, action))
        else:
            print(vkbeautify.cssfile(inputfile, action))
    else:
        if outputfile:
            print(vkbeautify.xmlfile(inputfile, outputfile, action))
        else:
            print(vkbeautify.xmlfile(inputfile, action))

    #print(vkbeautify.file(inputfile, outputfile))

if __name__ =='__main__':
    main(sys.argv[1:])


