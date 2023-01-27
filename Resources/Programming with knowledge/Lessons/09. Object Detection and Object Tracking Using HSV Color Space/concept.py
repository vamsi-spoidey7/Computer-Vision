# HSV(Hue Saturation Value)
# Hue corresponds to color components (base pigmnet), hence just by selecting a range of Hue you can select any color.
# Hue value (0-360)
# Saturation is the amount of color (depth  of the pigmnet)(dominance of Hue)(0-100%)
# Value is basically the brightness of the color (0-100%)
import cv2
import numpy as np

def nothing(x):
    pass

# cam = cv2.VideoCapture(0)

# cam.set(cv2.CAP_PROP_FRAME_WIDTH,300)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT,300)

# we will use trackbar to adjust lower and ubber bound hsv for color, as it is difficult to remember
cv2.namedWindow("Tracking")

cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)

cv2.createTrackbar("UH","Tracking",255,255,nothing)
cv2.createTrackbar("US","Tracking",255,255,nothing)
cv2.createTrackbar("UV","Tracking",255,255,nothing)

while True:
    frame = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/balls.jpg",1)
    # _,frame = cam.read()
    cv2.resize(frame,[100,100])
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos('LH','Tracking')
    l_s = cv2.getTrackbarPos('LS','Tracking')
    l_v = cv2.getTrackbarPos('LV','Tracking')

    u_h = cv2.getTrackbarPos('UH','Tracking')
    u_s = cv2.getTrackbarPos('US','Tracking')
    u_v = cv2.getTrackbarPos('UV','Tracking')

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    # lower and upper hsv for blue
    # l_b = np.array([110,50,50])
    # u_b = np.array([130,255,255])

    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# cam.release()
cv2.destroyAllWindows()