import numpy as np

def read_file(filename):
    # Use genfromtxt to read data from CSV file, skipping the first row (header)
    arr = np.genfromtxt(filename, delimiter="\t", skip_header=1, dtype=int)
    
    # Extract the second column from each row
    new_array = arr[:, 1]

    return new_array

# Example usage
np_a1 = read_file("book1.csv")
np_a2 = read_file("book2.csv")
np_a3 = read_file("book3.csv")

List = [np_a1, np_a2, np_a3]
List2 = [np.mean(np_a1), np.mean(np_a2), np.mean(np_a3)]
print(List2)
