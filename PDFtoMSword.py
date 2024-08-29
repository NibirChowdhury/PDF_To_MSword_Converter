import os

from pdf2docx import Converter


#path of the pdf
pdf_file_path="Ashraf Chowodhury CV with Cover Letter.pdf"

#create a doc
docx_file_path = "Ashraf Chowodhury CV with Cover Letter.docx"

converter = Converter(pdf_file_path)

converter.convert(docx_file_path)

if os.path.exists(docx_file_path):
    print("Conversion completed")
else:
    print("Conversion Failed!")