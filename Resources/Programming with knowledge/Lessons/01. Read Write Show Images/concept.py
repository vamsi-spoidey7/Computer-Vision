import cv2

## Reading(Loading) Image
img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/lena.png",0)
# 0  -> load image in greyscale
# 1  -> load image in color
# -1 -> load image including alpha channel

print(img) # Prints the matrix

cv2.imshow("ImageFrame",img) ## Show image
cv2.waitKey(5000) & 0xFF ## Image appears for 5sec and include mask(for 64bit)
# cv2.waitkey(0) Then appears till any key is pressed
cv2.imwrite('lena_copy.png',img)
cv2.destroyAllWindows()

### Practice Question
## if user presses escape key then image disappers and
## if presses 's' the save the image in greyscale

