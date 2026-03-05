# NumPy Code 13
# Topic: Searching and Conditional Functions

import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50, 60])

print("Array:", arr)

print("------------------")

# Find index of value
index = np.where(arr == 30)
print("Index of 30:", index)

print("------------------")

# Find values greater than 35
greater_vals = np.where(arr > 35)
print("Indices where value > 35:", greater_vals)

print("------------------")

# Replace values using condition
modified = np.where(arr > 40, 100, arr)
print("Replace values > 40 with 100:", modified)

print("------------------")

# Search in 2D array
matrix = np.array([[5, 10, 15],
                   [20, 25, 30]])

print("Matrix:\n", matrix)

indices = np.where(matrix > 15)
print("Positions where value > 15:", indices)