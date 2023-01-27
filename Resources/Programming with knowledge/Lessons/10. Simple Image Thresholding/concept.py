# Thresholding is a segmentation technique used to seperate an object from its background
# Process of thresholding involves comparing each pixel of image with predefined threshold value
# It divides all the pixels of input image into two groups
# 1st group involves pixels having intensity lower than threshold value and 2nd with intensity greater then threshold value

# From a grayscale image, thresholding can be used to create binary images.
# In Thresholding we Pick a threshold T.
# 1.Pixels above threshold get new intensity A.
# 2.Pixels above threshold get new intensity B.  
# In Thresholding, pixels that are alike in gray scale(or in some other feature) are grouped together.

import cv2
import numpy as np

img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/bnwgradient.jpg",1)

_,th1 = cv2.threshold(img,125,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,125,225,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,127,225,cv2.THRESH_TRUNC) # upto pixel 127 same as img and then after it all pixels are valued 127
_,th4 = cv2.threshold(img,124,255,cv2.THRESH_TOZERO) # upto 124 all pixels are 0 and from 124 all pixels remain as it is
_,th5 = cv2.threshold(img,125,255,cv2.THRESH_TOZERO_INV)


cv2.imshow('Image',img)
cv2.imshow('Binary',th1)
cv2.imshow('Binary Inverse',th2)
cv2.imshow('Trunc',th3)
cv2.imshow('ToZero',th4)
cv2.imshow('ToZero Inverse',th5)

cv2.waitKey(0)
cv2.destroyAllWindows()
