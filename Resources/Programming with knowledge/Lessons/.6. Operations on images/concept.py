import cv2
import numpy as np

img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/lena.png",1)
img2 = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/lion.jpg",1)

print(img.shape) # returns tuple of number of rows,columns,channels 
print(img.size) # returns total number of pixels
print(img.dtype) # returns image datatype

# split and merge
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

#ROI(Region of intrest)
eye = img[253:289,270:358]
img[178:214,356:444] = eye

# resize image
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

# add two images
dest = cv2.add(img,img2)

# add weighted images
dest2 = cv2.addWeighted(img,0.6,img2,0.4,0)

cv2.imshow('image',dest)
cv2.imshow('image2',dest2)
cv2.waitKey(0)
cv2.destroyAllWindows()