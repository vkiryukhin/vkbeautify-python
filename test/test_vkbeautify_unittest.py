import sys, os, unittest
sys.path.append(os.getcwd()+ '/..')
import vkbeautify as vkb

class VkbeautifyTest(unittest.TestCase):

    #
    # Testing XML
    #

    def test_xml_beautify(self):
        xml_expected = '<a>\n    <b></b>\n</a>'
        xml_pretty = vkb.xml('<a><b></b></a>')
        self.assertEqual(xml_pretty, xml_expected)

    def test_xml_beautify_with_custom_tab(self):
        xml_expected = '<a>\n        <b></b>\n</a>'
        xml_pretty = vkb.xml('<a><b></b></a>', 8) #set tab 8 spaces
        self.assertEqual(xml_pretty, xml_expected)

    def test_xml_minify(self):
        xml_expected = '<a><!--b></b--></a>'
        xml_mini = vkb.xml.min('<a>\n    <!--b></b-->\n</a>')
        self.assertEqual(xml_mini, xml_expected)

    def test_xml_minify_with_remove_comments(self):
        xml_expected = '<a></a>'
        xml_mini = vkb.xml.min('<a><!--b></b--></a>', False)
        self.assertEqual(xml_mini, xml_expected)


    #
    # Testing JSON
    #

    def test_json_beautify(self):
        json_expected = ' {\n    "menu":\n    {\n        "id":"file"\n    }\n}'
        json_pretty = vkb.json('{"menu":{"id":"file"}}')
        self.assertEqual(json_pretty, json_expected)

    def test_json_beautify_with_custom_tab(self):
        json_expected = ' {\n  "menu":\n  {\n    "id":"file"\n  }\n}'
        json_pretty = vkb.json('{"menu":{"id":"file"}}', 2) #set tab 2 spaces
        self.assertEqual(json_pretty, json_expected)

    def test_json_minify(self):
        json_expected = '{"menu":{"id":"file"}}'
        json_mini = vkb.json.min(' {\n  "menu":\n  {\n    "id":"file"\n  }\n}')
        self.assertEqual(json_mini, json_expected)


    #
    # Testing CSS
    #

    def test_css_beautify(self):
        css_expected = '.head{\n    margin:0 8px;\n    /*display:none*/\n}\na:active{\n    color:red\n}'
        css_pretty = vkb.css('.head{margin:0 8px;/*display:none*/}a:active{color:red}')
        self.assertEqual(css_pretty.strip(), css_expected.strip())

    def test_css_beautify_with_custom_tab(self):
        css_expected = '.head{\n  margin:0 8px;\n  /*display:none*/\n}\na:active{\n  color:red\n}'
        css_pretty = vkb.css('.head{margin:0 8px;/*display:none*/}a:active{color:red}', 2) #set tab 2 spaces
        self.assertEqual(css_pretty.strip(), css_expected.strip())

    def test_css_minify(self):
        css_expected = '.head{margin:0 8px;/*display:none*/}a:active{color:red }'
        css_mini = vkb.css.min('.head{\n    margin:0 8px;\n    /*display:none*/\n}\na:active{\n    color:red\n}')
        self.assertEqual(css_mini.strip(), css_expected.strip())

    def test_css_minify_with_remove_comments(self):
        css_expected = '.head{margin:0 8px;}a:active{color:red }'
        css_mini = vkb.css.min('.head{\n    margin:0 8px;\n    /*display:none*/\n}\na:active{\n    color:red\n}', False)
        self.assertEqual(css_mini, css_expected)

