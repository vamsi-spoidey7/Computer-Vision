import cv2

cam = cv2.VideoCapture(0) ## 0 for default camera orelse we can give file name

# for write video 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4',fourcc,20.0,(640,480))

while cam.isOpened() :
    success,frame = cam.read() # returns true to first variable if frame is available 
    
    if success == True : 

        print(cam.get(cv2.CAP_PROP_FRAME_WIDTH)) # prints cam width
        print(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)) # prints cam height

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # convert video to gerayscale

        out.write(frame)

        cv2.imshow("VideoFrame",gray) # display video
        if cv2.waitKey(1) & 0xFF == ord('q'):  # stop video if q is pressed
            break

    else:
        break


#release resources
cam.release()
out.release()

cv2.destroyAllWindows()
