import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i] ## for all events in cv2
print(events)

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x)+', '+str(y)
        cv2.putText(img,text,(x,y),font,0.5,(255,255,255),1,cv2.LINE_AA)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(blue)+', '+str(green)+', '+str(red)
        cv2.putText(img,text,(x,y),font,0.5,(255,255,255),1,cv2.LINE_AA)
        cv2.imshow('image',img)

img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/lena.png",1)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Questions
#1. Draw a cirlce and line connecting them when clicked
#2. When a point is clicked open new window with that particular color