import PIL.Image #Pillow
import pytesseract #Pytesseract
import sys

pytesseract.pytesseract.tesseract_cmd \
=r'C:/Program Files/Tesseract-OCR/tesseract' #Tesseract'ın kurulu olduğu dizin.

output=pytesseract.image_to_string(PIL.Image.open('test.png').convert("RGB"),lang='tur') #"test.png" okumak istediğiniz dosya, "lang" ise dil.
print(output) #Çıkış
