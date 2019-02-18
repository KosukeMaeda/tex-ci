from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import sys
import re

rsrcmgr = PDFResourceManager()
codec = 'utf-8'
params = LAParams()

def pdf2text(filepath):
    with StringIO() as buf:
        converter = TextConverter(rsrcmgr, buf, codec=codec, laparams=params)
        with open(filepath, 'rb') as input:
            interpreter = PDFPageInterpreter(rsrcmgr, converter)
            for page in PDFPage.get_pages(input):
                interpreter.process_page(page)
        converter.close()
        text = buf.getvalue()
    return text


if __name__ == '__main__':
    text = pdf2text(sys.argv[1])
    
    if text.find('[?]') > 0:
        print('found citation error!')
        sys.exit(1)