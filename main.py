import sys
import vkbeautify

def main():
    #name = sys.argv[1]
    #print(vkbeautify.greeting('Vadim    Kir', 4))
    cssStr = '.headbg{margin:0 8px  /*display:none*/}a:link,a:focus{color:#00c }a:active{color:red }'
    print(vkbeautify.css(cssStr))

if __name__ =='__main__':
    main()