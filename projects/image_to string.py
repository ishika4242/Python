'''
This python code is used to convert the text of image to the written format.

For this one has to save the image with name "img.jpg" and it will create it in written text in the command prompt.
'''

import pytesseract
from PIL import Image 

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x32)\Tesseract-OCR\tesseract.exe"

img=Image.open('img.jpg')
text=pytesseract.image_to_string(img)
print(text)
