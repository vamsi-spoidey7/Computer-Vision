# Morphological Transformations are some simple operations based on the image shape
# normally performed on binary images

from matplotlib import pyplot as plt
import cv2
import numpy as np

img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/balls.jpg",cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,220,225,cv2.THRESH_BINARY_INV)

kernal = np.ones([2,2],np.uint8)

dilation = cv2.dilate(mask,kernal,iterations=2)
erosion = cv2.erode(mask,kernal,iterations=1)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal) # erosion + dilutuion
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal) # dilution + erosion
mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal) # difference b/w dilation and erosion
th = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal) # difference b/w input and opening

titles = ['image','Mask','Dilation','Erosion','Opening','Closing','Gradient','TOPHAT']
images = [img,mask,dilation,erosion,opening,closing,mg,th]

for i in range(8):
    plt.subplot(2,4,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()