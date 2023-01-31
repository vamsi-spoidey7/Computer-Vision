import cv2
import numpy as np

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[x,y,2]
        myColorImage = np.zeros([512,512,3],np.uint8)
        myColorImage[:] = [blue,green,red]
        cv2.imshow('color',myColorImage)


img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/lena.png",1)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
