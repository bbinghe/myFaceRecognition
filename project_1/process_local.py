import numpy as np
import cv2

# Load an color Image in grayscale
img = cv2.imread('geisel.jpg',0)

#from PIL import image
#from resizeimage import resizeimage

#fd_img = open('geisel.jpg')
#img = image.open(fd_img)

height,width = img.shape
img2 = cv2.resize(img, fx=0.5, fy=0.5)
img3 = cv2.resize(img, [width/2, height/2])


img4 = cv2.rectangle(img, color[white], 
