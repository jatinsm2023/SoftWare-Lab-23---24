import numpy as np
import time
# function to read and convert array
start = time.time()
def read_convert_array(filename):
    data = np.genfromtxt(filename, delimiter="\t", skip_header=1, dtype=int)
    new = data[:,1]
    return new

# reading and converting arrays from files
np_a1 = read_convert_array("book1.csv")
np_a2 = read_convert_array("book2.csv")
np_a3 = read_convert_array("book3.csv")

# list of all arrays
list_of_all_array = [np_a1, np_a2, np_a3]
list_of_means = [np.mean(np_a1), np.mean(np_a2), np.mean(np_a3)]
print(f"Median of Every Array: {list_of_means}")
end = time.time()

print(f"Time taken: {end - start} seconds")