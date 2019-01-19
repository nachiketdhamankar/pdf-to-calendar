from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from pathlib import Path

PDF_FILES = Path(Path().absolute().parent / 'pdf-files')

os.chdir(PDF_FILES)

input1 = PdfFileReader(open(str(Path(PDF_FILES / '1.pdf')), "rb"))

print("There are %d" % input1.getNumPages())
page = input1.getPage(0)
# print(page.extractText())
test = input1.getFields()
test2 = input1.outlines
print(test2)
