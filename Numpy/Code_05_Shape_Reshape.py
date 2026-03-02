# NumPy Code 05
# Topic: Shape, Reshape and Dimensions

import numpy as np

# Create 1D array
arr = np.array([1, 2, 3, 4, 5, 6])
print("Original Array:", arr)

print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Total elements:", arr.size)

print("------------------")

# Reshape into 2D (2 rows, 3 columns)
arr_2d = arr.reshape(2, 3)
print("Reshaped 2D Array:\n", arr_2d)

print("New Shape:", arr_2d.shape)
print("New Dimensions:", arr_2d.ndim)

print("------------------")

# Reshape into 3x2
arr_3x2 = arr.reshape(3, 2)
print("Reshaped 3x2 Array:\n", arr_3x2)

print("------------------")

# Flatten back to 1D
flat_arr = arr_2d.flatten()
print("Flattened Array:", flat_arr)