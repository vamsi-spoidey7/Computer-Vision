# Show all simple threshold in one matplod window
from matplotlib import pyplot as plt
import cv2

img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/bnwgradient.jpg",1)

_,th1 = cv2.threshold(img,125,255,cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img,125,225,cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img,127,225,cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img,124,255,cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img,125,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray') # for subplot paramneters are rows,columns,index
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
