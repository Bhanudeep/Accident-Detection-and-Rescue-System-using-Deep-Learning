from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
basewidth = 1200
img = Image.open('numberplate/images0.jpg')
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), Image.ANTIALIAS)
img.save('numberplate/images0.jpg')

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('numberplate/images0.jpg')
i=0
while i<11:
    dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    i+=1
cv2.imwrite('numberplate/images0.jpg',dst)
gray = cv2.imread("numberplate/images0.jpg", 0)
blur = cv2.GaussianBlur(gray, (5,5), 0)
gray = cv2.medianBlur(gray, 3)
# perform otsu thresh (using binary inverse since opencv contours work better with white text)
ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
# cv2.imshow("Otsu", thresh)
# cv2.waitKey(0)
rect_kern = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

# apply dilation 
dilation = cv2.dilate(thresh, rect_kern, iterations = 1)
cv2.imwrite('numberplate/images0.jpg',dilation)
# roi=cv2.imread("numberplate/images0.jpg",0)
# text = pytesseract.image_to_string(roi, config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3')
# print(text)