import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
image = cv2.imread('images01.jpg')
text = pytesseract.image_to_string(image,lang='eng')
print('Texto: ',text)
      
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()




# C:\Program Files\Tesseract-OCR\tesseract.exe