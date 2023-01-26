import cv2

img = cv2.imread("C:/Users/MY PC/OneDrive/Desktop/Train/Python/Computer Vision/lena.png",0)
cv2.imshow("ImageFrame",img)
k = cv2.waitKey(0) & 0xFF

if k==27:
    cv2.destroyAllWindows
elif k == ord('s') :
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()