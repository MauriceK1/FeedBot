from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2 as cv
import sys
   
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
mouth_cascade = cv.CascadeClassifier('haarcascade_smile.xml')

def get(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    # Find face
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        
        # find mouth
        mouth = mouth_cascade.detectMultiScale(roi_gray)
        lowestY = 0
        lowestX = 0
        lowestW = 0
        lowestH = 0 
        third = (y + h) * (2/5)
        
        for (ex,ey,ew,eh) in mouth:
            if ey > third and ey > lowestY:
                lowestY = ey
                lowestX = ex
                lowestW = ew
                lowestH = eh
        cv.rectangle(roi_color,(lowestX,lowestY),(lowestX+lowestW,lowestY+lowestH),(0,255,0),2)
        
        # get x, y, z
        z = int(sys.stdin.readline().strip())
        width = z * (13/12)
        height = z * (5/4)
        
        x = (x + lowestX + lowestW / 2) - (320 / 2)
        y = (y + lowestY + lowestH / 2) - (240 / 2)
        
        x = x * width / 640
        y = y * height / 480
        
        print(x + " " + y + " " + z)
        return
    print("error")

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

#Iterate through frames
#Is it for one frame or for camera.framerate (32)?
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array
    
    get(image)
    
    rawCapture.truncate(0)


