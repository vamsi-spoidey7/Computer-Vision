import cv2
import numpy as np

apple = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/apple.jpg")
orange = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/orange.jpg")

# using h-stack
apple_orange = np.hstack((apple[:,:256],orange[:,256:]))

# Steps
# 1. Load the two images of apple and orange.
# 2. Find the Gaussian Pyramids for apple and orange(in this particular example, number of levels is 6)
# 3. From Gaussian Pyramids, find their Laplacian Pyramids
# 4. Now join the left half of apple and right half of orange in each levels of pyramids
# 5. Finally from this joint image pyramids, reconstruct the original image

# gaussian pyramid for apple
gp_apple = [apple]
layer = apple.copy()
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp_apple.append(layer)
# laplacian pyramid for apple
lp_apple = [gp_apple[6]]
for i in range(6,0,-1):
    gaussian_extended = cv2.pyrUp(gp_apple[i])
    lp_apple.append(cv2.subtract(gp_apple[i-1],gaussian_extended))

# gaussian pyramid for orange
gp_orange = [orange]
layer = orange.copy()
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp_orange.append(layer)
    # laplacian pyramid for orange
lp_orange = [gp_orange[6]]
for i in range(6,0,-1):
    gaussian_extended = cv2.pyrUp(gp_orange[i])
    lp_orange.append(cv2.subtract(gp_orange[i-1],gaussian_extended))


# join the left half of apple and right half of orange in each levels of pyramids
apple_orange_pyramid = []
for apple_lap,orange_lap in zip(lp_apple,lp_orange):
    cols,rows,ch = apple_lap.shape
    apple_orange_pyramid.append(np.hstack((apple_lap[:,:int(cols/2)],orange_lap[:,int(cols/2):])))


# reconstruct the original image from joint image pyramids
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1,7):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i],apple_orange_reconstruct)

print(apple.shape)
print(orange.shape)

cv2.imshow('Apple',apple)
cv2.imshow('Ornage',orange)
cv2.imshow('Apple_Orange',apple_orange)
cv2.imshow('apple_orange_reconstruct',apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()

