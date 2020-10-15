import sys
import PyPDF2
import textract

file = str(sys.argv[1])

#write some error catching for if the file doesn't work
def GetTextFromPDF(file):
    pdf = open(file, 'rb')
    pdfFile = PyPDF2.PdfFileReader(pdf)
    num_pages = pdfFile.numPages
    count = 0
    text = ""

    while count < num_pages:
        pageObj = pdfFile.getPage(count)
        count += 1
        text += pageObj.extractText()

    if text != "":
        text = text
    else:
        text = textract.process(file)

    return text


GetTextFromPDF(file)
