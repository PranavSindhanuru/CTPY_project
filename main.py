from fastapi import FastAPI, File, UploadFile, Query
from fastapi.responses import FileResponse
import uvicorn
from typing import List
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import img2pdf
from PIL import Image

app = FastAPI()

def sort_pdf(file, order_list):
    input_file = PdfFileReader(file)
    output = PdfFileWriter()
    for page_no in order_list:
        output.addPage(input_file.getPage(page_no-1))
    with open("result.pdf", "wb") as f:
        output.write(f)
    return output

def merge_pdf(file_list):
    output = PdfFileWriter()
    for file in file_list:
        input_file = PdfFileReader(file.file)
        for index in input_file.getNumPages():
            output.addPage(input_file.getPage(index))
    with open("result.pdf", "wb") as f:
        output.write(f)
    return output

def delete_pdf(file, pages):
    input_file = PdfFileReader(file)
    output = PdfFileWriter()
    pages = [x - 1 for x in pages]
    for index in input_file.getNumPages():
            if index not in pages:
                output.addPage(input_file.getPage(index))
    with open("result.pdf", "wb") as f:
        output.write(f)
    return output

def rotate_page(file, pages, rotation):
    input_file = PdfFileReader(file)
    output = PdfFileWriter()
    pages = [x - 1 for x in pages]
    for index in input_file.getNumPages():
        if index in pages:
            output.addPage(input_file.getPage(index).rotateClockwise(rotation))
        else:
            output.addPage(input_file.getPage(index))
    with open("result.pdf", "wb") as f:
        output.write(f)
    return output

def watermark_pdf_pages(file, watermark):
    input_file = PdfFileReader(file)
    watermark_file = PdfFileReader(watermark)
    watermark_page = watermark_file.getPage(0)
    output = PdfFileWriter()
    for i in range(input_file.getNumPages()):
        page = input_file.getPage(i)
        page.mergePage(watermark_page)
        output.addPage(page)
    with open("result.pdf", "wb") as f:
        output.write(f)
    return output

def pdf_to_text(file):
    input_file = PdfFileReader(file)
    text_file = open("result.txt", "a")
    for i in range(input_file.getNumPages()):
        txt = input_file.getPage(i).extractText()
        text_file.writelines(txt)
    text_file.close()
    

def image_to_pdf_file(file):
    pdf_bytes = img2pdf.convert(file)
    with open("result.pdf", "wb") as f:
        f.write(pdf_bytes)

@app.post("/sort/")
async def sort_pdf_file(order: List[int] = Query(None), file: UploadFile = File(...)):
    sort_pdf(file.file, order)
    return FileResponse('result.pdf', headers={'content-disposition': 'attachment; filename=result.pdf'}) 

@app.post("/merge/")
async def merge_pdf_file(files: List[UploadFile] = File(...)):
    merge_pdf(files)
    return FileResponse('result.pdf', headers={'content-disposition': 'attachment; filename=result.pdf'}) 

@app.post("/delete/")
async def delete_pdf_pages(pages: List[int] = Query(None), file: UploadFile = File(...)):
    delete_pdf(file.file, pages)
    return FileResponse('result.pdf', headers={'content-disposition': 'attachment; filename=result.pdf'})

@app.post("/rotate/")
async def rotate_pdf_pages(rotation: int, pages: List[int] = Query(None), file: UploadFile = File(...)):
    rotate_page(file.file, pages, rotation)
    return FileResponse('result.pdf', headers={'content-disposition': 'attachment; filename=result.pdf'})

@app.post("/watermark/")
async def watermark_pdf(file: UploadFile = File(...), watermark: UploadFile = File(...)):
    watermark_pdf_pages(file.file, watermark.file)
    return FileResponse('result.pdf', headers={'content-disposition': 'attachment; filename=result.pdf'})

@app.post("/pdf_to_text/")
async def pdf_to_text_file(file: UploadFile = File(...)):
    pdf_to_text(file.file)
    return FileResponse('result.txt', headers={'content-disposition': 'attachment; filename=result.txt'})

@app.post("/image_to_pdf/")
async def image_to_pdf(file: UploadFile = File(...)):
    image_to_pdf_file(file.file)
    return FileResponse('result.pdf', headers={'content-disposition': 'attachment; filename=result.pdf'})
    

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    
# webbrowser.open("http://localhost:8000/docs")
