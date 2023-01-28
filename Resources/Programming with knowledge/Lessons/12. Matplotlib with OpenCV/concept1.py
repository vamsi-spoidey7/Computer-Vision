# Matplotlib is a python 2D plotting library which produces publication quality figures in a variety of hardcopy formats.
from matplotlib import pyplot as plt
import cv2

img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/lena.png",1)
cv2.imshow("image",img)

#matplotlib reads image in rgb format
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# to hide ticks
plt.xticks([]),plt.yticks([])
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()