
"""
Read the outline.txt asshole. It has important information like where exactly you were stuck.
"""
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import os.path as path

PROJECT_DIR = path.abspath(path.join(__file__, "../.."))
PDF_FILES = path.join(PROJECT_DIR, "pdf-files")

def main():
    pdf_operations()

def pdf_operations():
    input_pdf = PdfFileReader(open(path.join(PDF_FILES, "1.pdf"), "rb"))
    print("There are %d" % input_pdf.getNumPages())
    input_page = input_pdf.getPage(0)
    print(input_page.extractText().encode('utf-8'))


if __name__ == '__main__':
    main()
