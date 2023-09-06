from pdf2docx import Converter

pdf_file = "sample.pdf"
docx_path = "sample.docx"

cv = Converter(pdf_file=pdf_file)
cv.convert(docx_filename=docx_path)
cv.close()





