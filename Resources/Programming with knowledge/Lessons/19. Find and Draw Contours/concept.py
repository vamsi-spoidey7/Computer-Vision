# Contours are curves joining all continuous points along the boundary which are having same color or intensity
# Useful for shape analysis, object detection and object recognition 
# For better accuracy we use binary images for finding contours

import cv2
import numpy as np

img = cv2.imread("open-cv.png")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,th = cv2.threshold(imgray,127,255,0)
contours,hierarchy = cv2.findContours(th,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# contours is a python list of all the contours in the image
# Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object
print('Number of contours:',str(len(contours)))
print(contours[0])

# To draw contours
# parameters : img,contours,contourIndex,color,thickness
# if contourIndex = -1 then displayes all contours
# to display individual contour then specify its index(ex if contour size=12 then index can be 0-11)
cv2.drawContours(img,contours,0,(0,255,0),4)

cv2.imshow('image-gray',imgray)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()