import PyPDF2 as pd
pdffileobj = open(r"C:\Users\risha\Downloads\Documents\ase.pdf","rb")
pdfreader = pd.PdfFileReader(pdffileobj)
x = pdfreader.numPages
pageobj = pdfreader.getPage(x-1)
text = pageobj.extractText()

file1 = open(r"C:\Users\risha\Downloads\Documents\\ase.txt", "a")
file1.writelines(text)
file1.close()

import img2pdf
from PIL import Image
import os
img_path = "sample image.png"
pdf_path = "yashnafile.pdf"
image = Image.open(img_path)
pdf_bytes = img2pdf.convert(image.filename)
file = open(pdf_path, "wb")
file.write(pdf_bytes)
image.close()
file.close()
print("Successfully made pdf file")