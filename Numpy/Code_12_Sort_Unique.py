# NumPy Code 12
# Topic: Sorting and Unique Values

import numpy as np

# Create array with duplicates
arr = np.array([5, 2, 8, 2, 9, 5, 1])

print("Original array:", arr)

print("------------------")

# Sort array
sorted_arr = np.sort(arr)
print("Sorted array:", sorted_arr)

print("------------------")

# Unique values
unique_vals = np.unique(arr)
print("Unique values:", unique_vals)

print("------------------")

# Count unique values
unique_vals, counts = np.unique(arr, return_counts=True)

print("Values:", unique_vals)
print("Counts:", counts)

print("------------------")

# Create 2D array
matrix = np.array([[3, 1, 2],
                   [9, 5, 4]])

print("Original matrix:\n", matrix)

# Sort rows
print("Row-wise sort:\n", np.sort(matrix))

# Sort columns
print("Column-wise sort:\n", np.sort(matrix, axis=0))