from PyPDF2 import PdfFileWriter, PdfFileReader

# x = [1, 3, 2]
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
        input_file = PdfFileReader(file)
        for index in input_file.getNumPages():
            output.addPage(input_file.getPage(index))
    with open("result.pdf", "wb") as f:
        output.write(f)
    return output

def delete_pdf_page(file, page_no):
    input_file = PdfFileReader(file)
    output = PdfFileWriter()
    for index in input_file.getNumPages():
        if index != page_no - 1:
            output.addPage(input_file.getPage(index))
    with open("result.pdf", "wb") as f:
        output.write(f)
    return output