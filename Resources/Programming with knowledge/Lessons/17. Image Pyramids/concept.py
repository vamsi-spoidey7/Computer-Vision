# Using image pyramids we create images of different resolutions and search for object
# There are two kinds of Image Pyramids. 1) Gaussian Pyramid and 2) Laplacian Pyramids
# These pyramids helps us to blend the images and reconstruction of images

import cv2
import numpy as np

img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/lena.jpg",cv2.IMREAD_GRAYSCALE)

# Gaussian Pyramid
lr = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr)
hr1 = cv2.pyrUp(lr2)
hr2 = cv2.pyrUp(hr1)

# Multiple image pyramid
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i),layer)

# Laplacian Pyramids
# A level in Laplacian pyramid is formed by the difference b/w 
# that level in  gaussian pyramid and expanded version of its upper level in Gaussian pyramid

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)

cv2.imshow('Image',img)
# cv2.imshow('pyrDown 1',lr)
# cv2.imshow('pyrDown 2',lr2) 
# cv2.imshow('pyrUp 1',hr1) 
# cv2.imshow('pyrUp 2',hr2) 

cv2.waitKey(0)
cv2.destroyAllWindows()
