import numpy as np
import cv2

# Load an color Image in grayscale
img = cv2.imread('geisel.jpg',0)

#from PIL import image
#from resizeimage import resizeimage

#fd_img = open('geisel.jpg')
#img = image.open(fd_img)

height,width = img.shape
dsize = (width/2, height/2)
img3 = cv2.resize(img, dsize)

center1 = dsize[0]/2
center2 = dsize[1]/2
print("Original Size: {} x {} :: Boxed : {}, {}".format(dsize[0], dsize[1], center1, center2))
cv2.rectangle(img3,(center1-50, center2+50), (center1+50, center2-50), (255, 255, 255))
cv2.imshow('test2', img3)
cv2.waitKey(0)

#cv2.imwrite("newgeisel.jpg", img4)
