from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

#Define path to image
path_to_image = 'extract text from the image.png'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Open image with PIL
img = Image.open(path_to_image)

#Extract text from image
mytext = pytesseract.image_to_string(img)

print(mytext)

# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os



# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")

'''
from PIL import Image
from pytesseract import pytesseract
import os

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Define path to images folder
path_to_images = r'images/'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Get the file names in the directory
for root, dirs, file_names in os.walk(path_to_images):
    #Iterate over each file name in the folder
    for file_name in file_names:
        #Open image with PIL
        img = Image.open(path_to_images + file_name)

        #Extract text from image
        text = pytesseract.image_to_string(img)

        print(text)
'''
