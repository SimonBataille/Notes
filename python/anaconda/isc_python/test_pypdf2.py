'''
conda install conda-forge::pypdf2
'''

from PyPDF2 import PdfReader, PdfWriter

# Merge and encrypt pdf files
pdf_writer = PdfWriter()
for pdf in ['page1.pdf', 'page2.pdf', 'page3.pdf']:
    pdf_reader = PdfReader(pdf)
    for page in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page])

pdf_writer.encrypt('password')

with open('merge.pdf', 'bw') as out: # on cree un flux out
    pdf_writer.write(out)


# Read text from pdf file
#pdf_reader = PdfReader('page1.pdf')
#for page in range(len(pdf_reader.pages)):
#    print(pdf_reader.pages[page].extract_text())
