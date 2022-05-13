import os
import tempfile
import io

import pytest

from logic.html_converter import HtmlPagesConverter, FileAccessWrapper

class TestHtmlPages:
    def test_insert_br_tags_for_linebreaks(self):
        filename = os.path.join(tempfile.gettempdir(), "afile.txt")
        f = open(filename, "w", encoding="UTF-8")
        f.write("plain text\n")
        f.close()
        converter = HtmlPagesConverter(FileAccessWrapper(filename))
        new_text = converter.get_html_page(0)
        assert new_text == "plain text<br />"
    
    def test_quotes_escaped(self):
        converter = HtmlPagesConverter(FakeFileWrapper("text with 'quotes'"))
        new_text = converter.get_html_page(0)
        assert "text with &#x27;quotes&#x27;<br />" == new_text

# test fakes have logic and functionality
class FakeFileWrapper:
    def __init__(self, text):
        self.text = text
    
    def open(self):
        # Python's fake files (in memory)
        return io.StringIO(self.text)
