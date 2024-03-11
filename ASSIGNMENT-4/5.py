import cv2
import numpy as np


X = cv2.imread('a.png')
cv2.imshow("image", X)
cv2.waitKey(0)
cv2.destroyAllWindows() # Press Any key to close the window
print(X.ndim) # to check the dimension


# Y = X
# Z = Y * X
# print(Z)