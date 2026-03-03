# NumPy Code 07
# Topic: Axis Operations and Advanced Broadcasting

import numpy as np

# Create 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Array:\n", arr)

print("------------------")

# Axis operations
print("Sum of all elements:", np.sum(arr))

# Column-wise sum (axis=0)
print("Column-wise sum:", np.sum(arr, axis=0))

# Row-wise sum (axis=1)
print("Row-wise sum:", np.sum(arr, axis=1))

print("------------------")

# Mean along axis
print("Column-wise mean:", np.mean(arr, axis=0))
print("Row-wise mean:", np.mean(arr, axis=1))

print("------------------")

# Broadcasting example
vector = np.array([10, 20, 30])

print("Vector:", vector)

# Add vector to each row
result = arr + vector
print("After Broadcasting:\n", result)