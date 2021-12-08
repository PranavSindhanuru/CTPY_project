import PyPDF2 as pd
pdffileobj = open(r"C:\Users\risha\Downloads\Documents\ase.pdf","rb")
pdfreader = pd.PdfFileReader(pdffileobj)
x = pdfreader.numPages
pageobj = pdfreader.getPage(x-1)
text = pageobj.extractText()

file1 = open(r"C:\Users\risha\Downloads\Documents\\ase.txt", "a")
file1.writelines(text)
file1.close()
