# vkBeautify

Python  plugin to **pretty-print** or **minify**
text in **XML** and **CSS** formats.

**Version** - 0.3.0

**Copyright** (c) 2016 Vadim Kiryukhin ( vkiryukhin @ gmail.com )

**Home page:** [http://www.eslinstructor.net/vkbeautify/](http://www.eslinstructor.net/vkbeautify/)

**License:** MIT:

[http://www.opensource.org/licenses/mit-license.php](http://www.opensource.org/licenses/mit-license.php)


   **Pretty print**
```
        vkbeautify.xml(src [,dest, [,tab_size]);
        vkbeautify.css(src [,dest, [,tab_size]);


        @src      - XML string or path to XML file to beatufy;
        @dest     - path to file to save beautified data (optional)
        @tab_size - number of white spaces to shift (optional; default is 4)

        @return - string (if @dest is not provided)
                  int (length of saved file) if @dest is provided
```

  **Minify**
```
        vkbeautify.xml.min(src [,dest [,preserve_comments]]);
        vkbeautify.css.min(src [,dest [,preserve_comments]]);

        @src   - XML string or path to XML file to minify;
        @dest  - path to file to save beautified data (optional)
        @preserve_comments - bool (optional, default is True);
                            Set this flag to False to remove comments from @src

        @return - string (if @dest is not provided)
                  int (length of saved file) if @dest is provided
```

   **Examples**
```python
import vkbeautify as vkb

vkb.xml(text)
vkb.xml(text, 'path/to/dest/file')
vkb.xml('path/to/src/file')
vkb.xml('path/to/src/file', 'path/to/dest/file')
vkb.xml('path/to/src/file', 8)
vkb.xml('path/to/src/file', 'path/to/dest/file', 5)


vkb.xml.min(text)
vkb.xml.min(text, 'path/to/dest/file')
vkb.xml.min('path/to/src/file')
vkb.xml.min('path/to/src/file', 'path/to/dest/file')
vkb.xml.min('path/to/src/file', False)
vkb.xml.min('path/to/src/file', 'path/to/dest/file', False)
```





