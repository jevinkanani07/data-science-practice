# NumPy Code 02
# Topic: Array Creation

import numpy as np

# 1D Array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

print("----------------")

# 2D Array
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr2)

print("----------------")

# Zeros array
zeros_array = np.zeros((2, 3))
print("Zeros Array:\n", zeros_array)

print("----------------")

# Ones array
ones_array = np.ones((2, 2))
print("Ones Array:\n", ones_array)

print("----------------")

# Range array
range_array = np.arange(0, 10, 2)
print("Range Array:", range_array)