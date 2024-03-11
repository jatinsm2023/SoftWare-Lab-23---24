import numpy as np

arr = np.genfromtxt("book1.csv", delimiter="\t", dtype=int) 

np_array = arr[1 : arr.size]
np_array = np_array[:, 1]

np_array.sort()
new_array = np.flip(np_array)

print(new_array)