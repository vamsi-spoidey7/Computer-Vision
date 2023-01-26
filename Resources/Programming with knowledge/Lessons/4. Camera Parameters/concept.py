import cv2

cam = cv2.VideoCapture(0)

print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

cam.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

print(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cam.isOpened() :
    success,frame = cam.read()
    cv2.imshow("VideoFrame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()


## Question
# Put cam properties and date on the video
