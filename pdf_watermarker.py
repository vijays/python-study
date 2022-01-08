import PyPDF2

input_pdf = PyPDF2.PdfFileReader(open('pdf/sample_pdf.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('pdf/draft_watermark.pdf', 'rb'))
output_pdf = PyPDF2.PdfFileWriter()

# get each page of pdf and watermark it

for i in range(input_pdf.getNumPages()):
    input_pdf_page = input_pdf.getPage(i)
    input_pdf_page.mergePage(watermark.getPage(0))
    output_pdf.addPage(input_pdf_page)
    
with open('pdf/watermarked_sample_pdf.pdf', 'wb') as file:
    output_pdf.write(file)