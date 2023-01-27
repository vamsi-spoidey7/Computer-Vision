# Adaptive Thresholding algorithm provide the image in which Threshold values vary over the image as a  function of  local image characteristics. 
# So Adaptive Thresholding involves two following steps
# (i) Divide image into strips 
# (ii) Apply global threshold method to each strip.

# Adaptive thresholding changes the threshold dynamically over the image. 
# Adaptive thresholding typically takes a gray scale or color image as input and, in the simplest implementation, outputs a binary image representing the segmentation.

import cv2
import numpy as np

img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/suduko.jpg",0)

_,th1 = cv2.threshold(img,125,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2) 
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2) 
# parameters (src,maxValue,AdaptiveMethod,ThresholdType,blockSize,Constant)
# cv2.ADAPTIVE_THRESH_MEAN_C the threshold value is mean of blockSize x blockSize neighborhood of (x,y) minus C
# the threshold value is weighted sum (cross-correlation with a Guassian Window) of blockSize x blockSize neighborhood of (x,y) minus C

cv2.imshow('Image',img)
cv2.imshow('Binary',th1)
cv2.imshow('Adaptive Mean',th2)
cv2.imshow('Adaptive Gaussian',th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
