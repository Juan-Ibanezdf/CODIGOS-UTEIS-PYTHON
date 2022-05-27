# Create AudioBook with Python
# pip install pyttsx3
# pip install PyPDF2
import pyttsx3
import PyPDF2
def Generate_AudioBook(file_name):
    pdf =PyPDF2.PdfFileReader(open(file_name,'rb'))
    pages = pdf.numPages
    audiobook=pyttsx3.init()
    for page in range(pages):
        data=pdf.getPage(page).extractText()
        audiobook.say(data)
        audiobook.runAndWait()
    audiobook.stop()
    audiobook.save_to_file(data,'audiobook.mp3')
    audiobook.runAndWait()
Generate_AudioBook("Book.pdf")