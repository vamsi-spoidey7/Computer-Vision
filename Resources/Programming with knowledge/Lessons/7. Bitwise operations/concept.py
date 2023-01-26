import cv2
import numpy as np

img1 = np.zeros([250,500,3],np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
img2 = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/bnw.png",1)

bitAnd = cv2.bitwise_and(img1,img2)
bitOr = cv2.bitwise_or(img1,img2)
bitXOR = cv2.bitwise_xor(img1,img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.imshow('AND',bitAnd)
cv2.imshow('OR',bitOr)
cv2.imshow('XOR',bitXOR)
cv2.imshow('Notimg1',bitNot1)
cv2.imshow('Notimg2',bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()

