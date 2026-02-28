# NumPy Code 03
# Topic: Indexing and Slicing

import numpy as np

# 1D Array
arr1 = np.array([10, 20, 30, 40, 50])

print("Array:", arr1)
print("First element:", arr1[0])
print("Last element:", arr1[-1])

print("Slice 1 to 3:", arr1[1:4])

print("------------------")

# 2D Array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print("2D Array:\n", arr2)

# Access single element
print("Element at row 1, col 2:", arr2[1, 2])

# Access full row
print("Second row:", arr2[1, :])

# Access full column
print("Third column:", arr2[:, 2])

# Slicing 2D
print("Top-left 2x2 block:\n", arr2[0:2, 0:2])