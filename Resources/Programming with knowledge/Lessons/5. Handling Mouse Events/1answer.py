import cv2
import numpy as np

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),5,(0,0,255),-1)
        points.append((x,y))
        if len(points)>1:
            cv2.line(img,points[-2],points[-1],(255,0,0),2)
        cv2.imshow('image',img)

img = np.zeros([512,512,3],np.uint8)
points = []
cv2.imshow('image',img)


cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()