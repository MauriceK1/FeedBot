from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
import cv2 as cv
import cv2  


def get_im(image):
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        print(x,y,w,h)
        cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            print(ex,ey,ew,eh)   
    cv.imshow('img',image)
##    cv.waitKey(500)
    cv2.waitKey(1)
##    & 0xFF
##    cv.destroyAllWindows()


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr" , use_video_port=True):
    image = frame.array
    get_im(image)
##    cv2.imshow("Frame" , image)
##    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
##    if key == ord("q"):
##        break
##    get_im(image)
    
  
