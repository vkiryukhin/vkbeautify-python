import sys, getopt
import vkbeautify

def main(argv):

    inputfile = ''
    outputfile = ''
    direction = '1'
    ext = 'xml'

    try:
        opts, args = getopt.getopt(argv,"hi:o:d:",["ifile=","ofile=","direction="])
    except getopt.GetoptError:
        print('main.py -i <inputfile> -o <outputfile> -d <direction>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -i <inputfile> -o <outputfile> -d <direction>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-d", "--direction"):
            direction = arg

    if not inputfile:
        print('usage: main.py -i <inputfile> -o <outputfile> -d <direction>'
               '\ninput file is mandatory')
        sys.exit(2)


    if inputfile[-4:] == '.css':
        if outputfile:
            print(vkbeautify.cssfile(inputfile, outputfile, direction))
        else:
            print(vkbeautify.cssfile(inputfile, direction))
    else:
        if outputfile:
            print(vkbeautify.xmlfile(inputfile, outputfile, direction))
        else:
            print(vkbeautify.xmlfile(inputfile, direction))

    #print(vkbeautify.file(inputfile, outputfile))

if __name__ =='__main__':
    main(sys.argv[1:])


