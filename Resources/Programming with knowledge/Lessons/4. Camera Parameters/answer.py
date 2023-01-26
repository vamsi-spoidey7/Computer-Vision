import cv2
import datetime
cam = cv2.VideoCapture(0)

while cam.isOpened() :
    success,frame = cam.read()
    if success:
        font = cv2.FONT_HERSHEY_SIMPLEX

        text = 'Width: '+str(cam.get(cv2.CAP_PROP_FRAME_WIDTH))+' Height: '+str(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame = cv2.putText(frame,text,(0,30),font,1,(0,0,0),1,cv2.LINE_AA)

        date = str(datetime.datetime.now())
        frame = cv2.putText(frame,date,(0,70),font,1,(0,0,0),1,cv2.LINE_AA)
        
        cv2.imshow("VideoFrame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cam.release()
cv2.destroyAllWindows()