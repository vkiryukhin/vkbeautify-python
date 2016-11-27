import unittest
import vkbeautify as vkb

class VkbeautifyTest(unittest.TestCase):

    #
    # Testing XML
    #

    def test_xml_prettyfy(self):
        xml_expected = '<a>\n    <b></b>\n</a>'
        xml_pretty = vkb.xml('<a><b></b></a>')
        self.assertEqual(xml_pretty, xml_expected)

    def test_xml_prettyfy_custom_tab(self):
        xml_expected = '<a>\n        <b></b>\n</a>'
        xml_pretty = vkb.xml('<a><b></b></a>', 8) #set tab 8 spaces
        self.assertEqual(xml_pretty, xml_expected)

    def test_xml_minify(self):
        xml_expected = '<a><!--b></b--></a>'
        xml_mini = vkb.xml.min('<a>\n    <!--b></b-->\n</a>')
        self.assertEqual(xml_mini, xml_expected)

    def test_xml_minify_remove_comments(self):
        xml_expected = '<a></a>'
        xml_mini = vkb.xml.min('<a><!--b></b--></a>', False)
        self.assertEqual(xml_mini, xml_expected)

    #
    # Testing CSS
    #

    def test_css_prettyfy(self):
        css_expected = '.head{\n    margin:0 8px;\n    /*display:none*/\n}\na:active{\n    color:red\n}'
        css_pretty = vkb.css('.head{margin:0 8px;/*display:none*/}a:active{color:red}')
        self.assertEqual(css_pretty.strip(), css_expected.strip())

    def test_css_prettyfy_custom_tab(self):
        css_expected = '.head{\n  margin:0 8px;\n  /*display:none*/\n}\na:active{\n  color:red\n}'
        css_pretty = vkb.css('.head{margin:0 8px;/*display:none*/}a:active{color:red}', 2) #set tab 2 spaces
        self.assertEqual(css_pretty.strip(), css_expected.strip())

    def test_css_minify(self):
        css_expected = '.head{margin:0 8px;/*display:none*/}a:active{color:red }'
        css_mini = vkb.css.min('.head{\n    margin:0 8px;\n    /*display:none*/\n}\na:active{\n    color:red\n}')
        self.assertEqual(css_mini.strip(), css_expected.strip())

    def test_css_minify_remove_comments(self):
        css_expected = '.head{margin:0 8px;}a:active{color:red }'
        css_mini = vkb.css.min('.head{\n    margin:0 8px;\n    /*display:none*/\n}\na:active{\n    color:red\n}', False)
        self.assertEqual(css_mini, css_expected)


if __name__ == '__main__':
    unittest.main()