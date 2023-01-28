# Smoothing is used to remove noise in the images
# Homogeneous filter is the most simple filter, each output pixel is the mean of its kernel neighbors
import cv2
import matplotlib.pyplot as plt
import numpy as np

# img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/open-cv.png")
img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/water.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# In homogeneous filter kernal K = 1/(Kwidth*kheight)[matrix of ones with kwidth rows and kheight columns]
kernal = np.ones([5,5],np.float32)/25
dst = cv2.filter2D(img,-1,kernal)

# Images can also be filtered with various low-pass-filers(LPF), high-pass-filters(HPF), etc.
# LPF helps in removing the noise or blurring the image
blur = cv2.blur(img,(5,5))
# HPF helps in finding edges in the image

# In gaussian filter we are using different-weighted-kernel in both x and y direction
# in this matrix middle values are greater than surroundings
gblur = cv2.GaussianBlur(img,(5,5),0)

# Median filter is something that replaces each pixels's value with the median of its neighboring pixels
# This method is great when dealing with "salt and pepper noise"
median = cv2.medianBlur(img,5)

# bilateral filter is used to preserve edges
bilateral = cv2.bilateralFilter(img,9,75,75)

titles = ['image','2D-Convolution','blur','GaussianBlur','MedianBlur','BiLateral']
images = [img,dst,blur,gblur,median,bilateral]



for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

