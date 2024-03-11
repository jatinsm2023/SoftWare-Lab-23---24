import numpy as np
import cv2
import time as t

original = cv2.imread('a.png')
X = np.mean(original, axis=2, dtype=int).astype(np.uint8)

# Transpose of X 
Y = np.zeros((X.shape[1], X.shape[0]), dtype=int)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Y[j][i] = X[i][j]

print(X.shape)
print(Y.shape)
# Define matrices as lists
x = X.tolist()
y = Y.tolist()

# Multyply both matrices and store in a matrix without using numpy function
t1 = t.time()
r1 = X.shape[0]
c2 = Y.shape[1]
c1 = X.shape[1]
result = [[0 for j in range(c2)] for i in range(r1)]
for i in range(r1):
    print(i)
    for j in range(c2):
        for k in range(c1):
            result[i][j] += x[i][k] * y[k][j]

t2 = t.time()
print("Time taken without using numpy function: ", t2 - t1)

