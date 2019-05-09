from PIL import Image
import PIL.Image
import cv2
from pytesseract import image_to_string
import pytesseract

imgPath = "capture.png"
config = ('-l eng --oem 1 --psm 3')
im = cv2.imread(imgPath, cv2.IMREAD_COLOR)
text = pytesseract.image_to_string(im, config=config)
print(text)