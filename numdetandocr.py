import cv2
import numpy as np
import pytesseract
import cv2
import os
import re
def numdet():
    frameWidth = 640    #Frame Width
    franeHeight = 480   # Frame Height

    plateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
    minArea = 500

    path = 'images/2.jpg'
    
    # Using cv2.imread() method
    # cap = cv2.imread(path)

    # cap =cv2.VideoCapture(0)
    # cap.set(3,frameWidth)
    # cap.set(4,franeHeight)
    # cap.set(10,150)
    count = 0


    img  = cv2.imread(path)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade .detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            imgRoi = img[y:y+h,x:x+w]
            # cv2.imshow("ROI",imgRoi)
    # cv2.imshow("Result",img)
    # if cv2.waitKey(1) & 0xFF ==ord('s'):
    cv2.imwrite("numberplate/images"+str(count)+".jpg",imgRoi)
    # cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
    # cv2.putText(img,"Scan Saved",(15,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
    # cv2.imshow("Result",img)
    # cv2.waitKey(500)
    # count+=1
def ocr():
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
    # If you don't have tesseract executable in your PATH, include the following:
    # pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
    # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

    # point to license plate image (works well with custom crop function)
    gray = cv2.imread("images0.jpg", 0)
    # gray = cv2.resize( gray, None, fx = 3, fy = 3, interpolation = cv2.INTER_CUBIC)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    gray = cv2.medianBlur(gray, 3)
    # perform otsu thresh (using binary inverse since opencv contours work better with white text)
    ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    # cv2.imshow("Otsu", thresh)
    # cv2.waitKey(0)
    rect_kern = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

    # apply dilation 
    dilation = cv2.dilate(thresh, rect_kern, iterations = 1)
    #cv2.imshow("dilation", dilation)
    #cv2.waitKey(0)
    # find contours
    try:
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    except:
        ret_img, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    sorted_contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])

    # create copy of image
    im2 = gray.copy()

    plate_num = ""
    # loop through contours and find letters in license plate
    for cnt in sorted_contours:
        x,y,w,h = cv2.boundingRect(cnt)
        height, width = im2.shape
        
        # if height of box is not a quarter of total height then skip
        if height / float(h) > 6: continue
        ratio = h / float(w)
        # if height to width ratio is less than 1.5 skip
        if ratio < 1.5: continue
        area = h * w
        # if width is not more than 25 pixels skip
        if width / float(w) > 15: continue
        # if area is less than 100 pixels skip
        if area < 100: continue
        # draw the rectangle
        rect = cv2.rectangle(im2, (x,y), (x+w, y+h), (0,255,0),2)
        roi = thresh[y-5:y+h+5, x-5:x+w+5]
        roi = cv2.bitwise_not(roi)
        roi = cv2.medianBlur(roi, 5)
        #cv2.imshow("ROI", roi)
        #cv2.waitKey(0)
        text = pytesseract.image_to_string(roi, config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8 --oem 3')
        #print(text)
        clean_text=re.sub('[\W_]+','',text)
        plate_num += clean_text
        print(plate_num)
        # cv2.imshow("Character's Segmented", im2)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
numdet()
ocr()