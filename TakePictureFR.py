import numpy as np
import cv2 as cv
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
rawCapture = PiRGBArray(camera)
 
time.sleep(0.1)

camera.capture(rawCapture, format="bgr")
image = rawCapture.array

face_cascade = cv.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
mouth_cascade = cv.CascadeClassifier('/home/pi/opencv/data/haarcascades/haarcascade_smile.xml')
img = image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    mouth = mouth_cascade.detectMultiScale(roi_gray)
    lowestY = 0
    lowestX = 0
    lowestW = 0
    lowestH = 0
    for (ex,ey,ew,eh) in mouth:
        if ey > lowestY & ex < (x+w)/2:
            lowestY = ey
            lowestX = ex
            lowestW = ew
            lowestH = eh
    cv.rectangle(roi_color,(lowestX,lowestY),(lowestX+lowestW,lowestY+lowestH),(0,255,0),2)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()