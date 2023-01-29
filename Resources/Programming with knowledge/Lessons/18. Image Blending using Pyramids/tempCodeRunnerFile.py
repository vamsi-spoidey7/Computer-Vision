gp_orange = [orange]
# layer = orange.copy()
# for i in range(6):
#     layer = cv2.pyrDown(layer)
#     gp_apple.append(layer)
# lp_orange = []
# for i in range(6,0,-1):
#     gaussian_extended = cv2.pyrUp(gp_orange[i])
#     lp_orange.append(cv2.subtract(gp_orange[i-1],gaussian_extended))

# apple_orange_pyramid = []
# for apple_lap,orange_lap in zip(lp_apple,lp_orange):
#     cols,rows,ch = apple_lap.shape
#     apple_orange_pyramid.append(np.hstack((apple_lap[:,:int(cols/2)],orange_lap[:,int(cols/2):])))

# apple_orange_reconstruct = apple_orange_pyramid[0]
# for i in range(1,6):
#     apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
#     apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i],apple_orange_reconstruct)

# print(apple.shape)
# print(orange.shape)

# cv2.imshow('Apple',apple)
# cv2.imshow('Ornage',orange)
# cv2.imshow('Apple_Orange',apple_orange)
# cv2.imshow('apple_orange_reconstruct',apple_orange_reconstruct)