import sys
import vkbeautify

def main():
    #name = sys.argv[1]
    #print(vkbeautify.greeting('Vadim    Kir', 4))
    css_str = '.headbg{margin:0 8px  /*display:none*/}a:link,a:focus{color:#00c }a:active{color:red }'
    #xml_str = '<a><b>bbb</b></a>'
    xml_str = '<?xml version="1.0" encoding="UTF-8" ?><!DOCTYPE foo SYSTEM "Foo.dtd"><a><!--b>bbb</b--><c/><d><soapenv:Envelope xmlns:soapenv="http://xxx" xmlns:xsd="http://yyy" xmlns:xsi="http://zzz"></soapenv></d><e><![CDATA[ <z></z> ]]></e><f><g></g></f></a>'
    css = vkbeautify.css(css_str);
    #print(css)
    cssmin = vkbeautify.cssmin(css, False)
    #print(cssmin)
    xml = vkbeautify.xml(xml_str);
    #print(xml)

    xmlmin = vkbeautify.xmlmin(xml, False)

    print(xmlmin)

    print(vkbeautify.xml(xmlmin))

if __name__ =='__main__':
    main()