# This is our main python file !
# we code all the MAIN stuff in this
from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
from fastapi import FastAPI, File, UploadFile

from PyPDF2 import PdfFileWriter, PdfFileReader

app = FastAPI()

def f(x):
    input1 = PdfFileReader(x)
    output = PdfFileWriter()
    output.addPage(input1.getPage(0))
    output.addPage(input1.getPage(1).rotateClockwise(90))
    with open("result.pdf", "wb") as f:
        output.write(f)
    return output

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    f(file.file)
    return FileResponse('result.pdf', headers={'content-disposition': 'attachment; filename=blah.pdf'})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)