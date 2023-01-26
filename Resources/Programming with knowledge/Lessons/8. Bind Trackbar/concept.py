## Trackbars are used to change values in image dynamically
import cv2
import numpy as np

def nothing(x):
    print(x)

img = np.zeros([300,512,3],np.uint8)
cv2.namedWindow("image")

cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('R','image',0,255,nothing)

switch = '0 : OFF\n1 : ON'
cv2.createTrackbar(switch,'image',0,1,nothing)

while True:
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

    b = cv2.getTrackbarPos('B','image')
    g = cv2.getTrackbarPos('G','image')
    r = cv2.getTrackbarPos('R','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s==0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()

# problem
# print value of trackbar on image and switch to toogle to greyscale