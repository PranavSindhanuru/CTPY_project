# This is our main python file !
# we code all the MAIN stuff in this
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
from fastapi import FastAPI, File, UploadFile
from typing import List
from PyPDF2 import PdfFileWriter, PdfFileReader

app = FastAPI()


def f(x):
    input_file = PdfFileReader(x)
    output = PdfFileWriter()
    output.addPage(input_file.getPage(0))
    output.addPage(input_file.getPage(1).rotateClockwise(90))
    with open("result.pdf", "wb") as f:
        output.write(f)
    return output


@app.post("/uploadfile/")
async def create_upload_file(files: List[UploadFile] = File(...)):
    for file in files:
        f(file.file)
    return FileResponse('result.pdf', headers={'content-disposition': 'attachment; filename=result.pdf'})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
