import cv2
cam=cv2.VideoCapture(0)
import numpy as np
import pytesseract

cv2.namedWindow("test")
img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to garb frame")
        break
    cv2.imshow('test',frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        print("closing....")
        break
    if k%256 == 32:
        img_name = "opencv_frame_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{}written!".format(img_name))
        img_counter +=1
cam.release()



pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'

# 1. Load the image
img = cv2.imread("opencv_frame_0.jpg")

# 2. Resize the image
img = cv2.resize(img, None, fx=0.5, fy=0.5)

# 3. Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 4. Convert image to black and white (using adaptive threshold)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)

config = "--psm 3"
text = pytesseract.image_to_string(adaptive_threshold, config=config, lang="eng")
print(text)

#cv2.imshow("gray", gray)
cv2.imshow("adaptive th", adaptive_threshold)
cv2.waitKey(0)