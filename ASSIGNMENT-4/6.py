# Program
import numpy as np
import cv2

original = cv2.imread('a.png')
X = np.mean(original, axis=2, dtype=int).astype(np.uint8)
cv2.imshow("GrayScale Image", X)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(X.ndim) 