# Image gradient is a directional change in the intensity or color in an image
import matplotlib.pyplot as plt
import cv2
import numpy as np

# img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/messi.jpg",cv2.IMREAD_GRAYSCALE)
img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/suduko.jpg",cv2.IMREAD_GRAYSCALE)


# Laplacian Gradient
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY = cv2.Sobel(img,cv2.CV_64F,0,1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX,sobelY)

images = [img,lap,sobelX,sobelY,sobelCombined]
titles = ['image','Laplacian','SobelX','SobelY','SobelCombined']

for i in range(5):
    plt.subplot(2,3,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
