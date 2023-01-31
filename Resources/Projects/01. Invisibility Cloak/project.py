import cv2
import numpy as np

def nothing():
    print()

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
bg = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/Background.jpg",1)

four_cc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Output.mp4',four_cc,10.0,(1280,720))

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

# cv2.namedWindow("bars")

# cv2.createTrackbar("upper_hue","bars",255,255,nothing)
# cv2.createTrackbar("upper_saturation","bars",255,255,nothing)
# cv2.createTrackbar("upper_value","bars",255,255,nothing)
# cv2.createTrackbar("lower_hue","bars",0,255,nothing)
# cv2.createTrackbar("lower_saturation","bars",0,255,nothing)
# cv2.createTrackbar("lower_value","bars",0,255,nothing)


while cap.isOpened():

    ret, frame = cap.read()
    frameGray = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # upper_hue = cv2.getTrackbarPos("upper_hue","bars")
    # upper_saturation = cv2.getTrackbarPos("upper_saturation","bars")
    # upper_value = cv2.getTrackbarPos("upper_value","bars")
    # lower_hue = cv2.getTrackbarPos("lower_hue","bars")
    # lower_saturation = cv2.getTrackbarPos("lower_saturation","bars")
    # lower_value = cv2.getTrackbarPos("lower_value","bars")

    # upper_hsv = np.array((upper_hue,upper_saturation,upper_value))
    # lower_hsv = np.array((lower_hue,lower_saturation,lower_value))

    upper_hsv = np.array((243,238,231))
    lower_hsv = np.array((160,82,17))

    mask = cv2.inRange(frameGray,lower_hsv,upper_hsv)
    mask = cv2.medianBlur(mask,3)
    mask = cv2.dilate(mask,(3,3),0)

    mask_inv = 255-mask

    # b,g,r = cv2.split(frame)
    # b = cv2.bitwise_and(mask_inv,b)
    # g = cv2.bitwise_and(mask_inv,g)
    # r = cv2.bitwise_and(mask_inv,r)
    # frame_inv = cv2.merge((b,g,r))

    # b,g,r = cv2.split(bg)
    # b = cv2.bitwise_and(mask,b)
    # g = cv2.bitwise_and(mask,g)
    # r = cv2.bitwise_and(mask,r)
    # blanket_area = cv2.merge((b,g,r))

    frame_inv = cv2.bitwise_and(frame,frame,mask=mask_inv)
    blanket_area = cv2.bitwise_and(bg,bg,mask=mask)

    final = cv2.bitwise_or(frame_inv,blanket_area)

    cv2.imshow("image",final)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    out.write(final)


out.release()
cap.release()
cv2.destroyAllWindows()
