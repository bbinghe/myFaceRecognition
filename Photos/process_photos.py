import cv2
import numpy as np
import os



face_cascade = cv2.CascadeClassifier('/home/pi/opencv-2.4.13.4/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv-2.4.13.4/data/haarcascades/haarcascade_eye.xml')


for i in range(1, 160):



    image = cv2.imread('./image/photo (' + str(i) + ').JPG')

    
    dim = image.shape
    dsize = 240, 320
    photo=cv2.resize(image, dsize)

    gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
   
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)   
    for (x, y, w, h) in faces:
        #cv2.rectangle(gray, (x,y),(x+w, y+h), 1)
        cropped = gray[y:y+h, x:x+w]
        #rol_color = gray[y:y+h, x:x+w]
    
         #cv2.imshow("HYEBEEN", cropped)
         #cv2.waitKey(0)    


        cv2.imwrite("./cropped/" + str(i) + ".jpg", cropped)
    
