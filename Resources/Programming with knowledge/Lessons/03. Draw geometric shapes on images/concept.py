import cv2
import numpy as np

img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/lena.png",1)

## Create image using numpy
img = np.zeros([800,800,3],np.uint8) # Black Image
#np.zeroes([height,width,channels],dtype)
img = np.ones([800,800,3],np.uint8)*255 # White Image

## Draw line
img = cv2.line(img,(0,0),(255,255),(0,0,255),5) 
# parameters : (image,point1,point2,color(BGR),Thickness)

## Draw arrowed line
img = cv2.arrowedLine(img,(0,255),(255,255),(0,0,255),5) 

## Draw Rectangle
img = cv2.rectangle(img,(255,0),(344,456),(255,34,66),3) # if thickness=-1 then it fills

## Draw circle
img= cv2.circle(img,(600,600),30,(255,255,255),7) 
# parameters : (image,center,radius,color(BGR),Thickness)

## Adding text
font = cv2.FONT_HERSHEY_SIMPLEX # fontFace or font
img = cv2.putText(img,"Nani",(200,200),font,3,(255,255,255),3,cv2.LINE_AA)
#parameters : (image,text,point,fontFace,fontScale,color,thickness,lineType)
cv2.imshow("ImageFrame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()