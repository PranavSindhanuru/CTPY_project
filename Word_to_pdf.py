import os
import comtypes.client
import time

wdFormatPDF = 17

in_file = r'C:\Users\risha\Downloads\Documents\ABCD.docx'
out_file = r'C:\Users\risha\Downloads\Documents\ABCD.pdf'

word = comtypes.client.CreateObject('Word.Application')
word.Visible = True
time.sleep(3)

doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Visible = False
word.Quit()

