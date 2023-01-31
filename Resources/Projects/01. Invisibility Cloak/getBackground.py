import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

while cap.isOpened():

    ret, frame = cap.read()
    cv2.imshow("image",frame)

    k = cv2.waitKey(1)
    if k == 27:
        break
    elif k == ord('s'):
        cv2.imwrite('Background.jpg',frame)

cap.release()
cv2.destroyAllWindows()