import sys, os, pytest
sys.path.append(os.getcwd()+ '/..')
import vkbeautify as vkb

#
# Testing XML
#

def test_xml_beautify():
    xml_expected = '<a>\n    <b></b>\n</a>'
    xml_pretty = vkb.xml('<a><b></b></a>')
    assert xml_pretty == xml_expected

def test_xml_beautify_with_custom_tab():
    xml_expected = '<a>\n        <b></b>\n</a>'
    xml_pretty = vkb.xml('<a><b></b></a>', 8) #set tab 8 spaces
    assert xml_pretty == xml_expected

def test_xml_minify():
    xml_expected = '<a><!--b></b--></a>'
    xml_mini = vkb.xml.min('<a>\n    <!--b></b-->\n</a>')
    assert xml_mini == xml_expected

def test_xml_minify_with_remove_comments():
    xml_expected = '<a></a>'
    xml_mini = vkb.xml.min('<a><!--b></b--></a>', False)
    assert xml_mini == xml_expected

def test_xml_beautify_and_save(tmpdir):
    file = tmpdir.join('output.xml')
    xml_pretty = vkb.xml('<a><b></b></a>', file.strpath)
    assert xml_pretty == 20

def test_xml_minify_and_save(tmpdir):
    file = tmpdir.join('output.xml')
    xml_mini = vkb.xml.min('<a>\n    <!--b></b-->\n</a>', file.strpath)
    assert xml_mini == 19

#
# Testing JSON
#

def test_json_beautify():
    json_expected = ' {\n    "menu":\n    {\n        "id":"file"\n    }\n}'
    json_pretty = vkb.json('{"menu":{"id":"file"}}')
    assert json_pretty == json_expected

def test_json_beautify_with_custom_tab():
    json_expected = ' {\n  "menu":\n  {\n    "id":"file"\n  }\n}'
    json_pretty = vkb.json('{"menu":{"id":"file"}}', 2) #set tab 2 spaces
    assert json_pretty == json_expected

def test_json_minify():
    json_expected = '{"menu":{"id":"file"}}'
    json_mini = vkb.json.min(' {\n  "menu":\n  {\n    "id":"file"\n  }\n}')
    assert json_mini == json_expected

def test_xml_beautify_and_save(tmpdir):
    file = tmpdir.join('output.json')
    json_pretty = vkb.json('{"menu":{"id":"file"}}', file.strpath)
    assert json_pretty == 48

def test_xml_minify_and_save(tmpdir):
    file = tmpdir.join('output.json')
    json_mini = vkb.json.min(' {\n  "menu":\n  {\n    "id":"file"\n  }\n}', file.strpath)
    assert json_mini == 22


#
# Testing CSS
#

def test_css_beautify():
    css_expected = '.head{\n    margin:0 8px;\n    /*display:none*/\n}\na:active{\n    color:red\n}'
    css_pretty = vkb.css('.head{margin:0 8px;/*display:none*/}a:active{color:red}')
    assert css_pretty.strip() == css_expected.strip()

def test_css_beautify_with_custom_tab():
    css_expected = '.head{\n  margin:0 8px;\n  /*display:none*/\n}\na:active{\n  color:red\n}'
    css_pretty = vkb.css('.head{margin:0 8px;/*display:none*/}a:active{color:red}', 2) #set tab 2 spaces
    assert css_pretty.strip() == css_expected.strip()

def test_css_minify():
    css_expected = '.head{margin:0 8px;/*display:none*/}a:active{color:red }'
    css_mini = vkb.css.min('.head{\n    margin:0 8px;\n    /*display:none*/\n}\na:active{\n    color:red\n}')
    assert css_mini.strip() == css_expected.strip()

def test_css_minify_with_remove_comments():
    css_expected = '.head{margin:0 8px;}a:active{color:red }'
    css_mini = vkb.css.min('.head{\n    margin:0 8px;\n    /*display:none*/\n}\na:active{\n    color:red\n}',
                            False)
    assert css_mini == css_expected

def test_css_beautify_and_save(tmpdir):
    file = tmpdir.join('output.xml')
    css_pretty = vkb.css('.head{margin:0 8px;/*display:none*/}a:active{color:red}', file.strpath)
    assert css_pretty == 74

def test_css_minify_and_save(tmpdir):
    file = tmpdir.join('output.xml')
    css_mini = vkb.css.min('.head{\n    margin:0 8px;\n    /*display:none*/\n}\na:active{\n    color:red\n}',
                            file.strpath)
    assert css_mini == 56


