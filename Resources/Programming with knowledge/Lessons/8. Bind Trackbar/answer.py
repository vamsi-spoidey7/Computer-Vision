import cv2

def nothing(x):
    pass

cv2.namedWindow('image')

cv2.createTrackbar('POS','image',10,400,nothing)
switch = 'ON OFF'
cv2.createTrackbar(switch,'image',0,1,nothing)

while True:

    img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/lena.png",1)
    if cv2.waitKey(1) & 0xFF == 'q':
        break

    pos = cv2.getTrackbarPos('POS','image')
    s = cv2.getTrackbarPos(switch,'image')

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(pos),(50,100),font,3,(255,255,255),5,cv2.LINE_AA)

    if s!=0:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    img = cv2.imshow('image',img)

cv2.destroyAllWindows()
