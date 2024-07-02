from gtts import gTTS
from playsound import playsound
from tkinter import filedialog
from PyPDF2 import PdfReader
import PyPDF2


def process_file():
    right_file = False
    while right_file is False:
        file_path = filedialog.askopenfilename(title="Select a file",
                                               filetypes=[("text files", "txt"), ("PDF files", "*.pdf")])
        file_type = [char for char in file_path.split("/")[-1]]
        file_type = "".join(file_type[-4:])
        if file_type == ".pdf":
            pdf = PdfReader(file_path)
            pdf_object = open(file_path, "rb")
            pdfreader = PyPDF2.PdfReader(pdf_object)
            text = ''
            for i in range(0, len(pdfreader.pages)):
                # creating a page object
                page_obj = pdfreader.pages[i]
                # extracting text from page
                text = text + page_obj.extract_text()

            tts_obj = gTTS(text=text, lang='en')
            tts_obj.save('audio.mp3')
            playsound('audio.mp3')
            right_file = True
        elif file_type == ".txt":
            with open(file_path, "r") as f:
                text = f.read()
                tts_obj = gTTS(text=text, lang='en')
                tts_obj.save('audio.mp3')
                playsound('audio.mp3')
                right_file = True
        else:
            print("File type not supported.\n"
                  "Try Again.")


process_file()
