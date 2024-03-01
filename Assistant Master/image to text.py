import pytesseract as tess
from PIL import Image

# Set the path to the Tesseract executable
tess.pytesseract.tesseract_cmd = r"C:\Sachin Sharma\Programming\Softwares\Tesseract\tesseract.exe"

# Open the image file
image_path = 'C:/Sachin Sharma/Programming/Assistant Master/text.png'
img = Image.open(image_path)

# Use pytesseract to do OCR on the image
text = tess.image_to_string(img)

# Print the extracted text
print(text)
