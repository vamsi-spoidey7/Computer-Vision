# Canny edge detection algorithm is composed of 5 steps:
# 1. Noise reduction
# 2. Gradient calculation
# 3. Non-maximum suppression
# 4. Double threshold
# 5. Edge tracking by Hysteresis

import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/messi.jpg",cv2.IMREAD_GRAYSCALE)

canny = cv2.Canny(img,100,200) # the orther two parameters are threshold 1 & 2 used for hysteresis

images = [img,canny]
titles = ['image','Canny']

for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
