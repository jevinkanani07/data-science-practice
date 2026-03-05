# NumPy Code 11
# Topic: Stacking and Splitting Arrays

import numpy as np

# Create arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("Array 1:", arr1)
print("Array 2:", arr2)

print("----------------------")

# Vertical stacking
v_stack = np.vstack((arr1, arr2))
print("Vertical Stack:\n", v_stack)

print("----------------------")

# Horizontal stacking
h_stack = np.hstack((arr1, arr2))
print("Horizontal Stack:", h_stack)

print("----------------------")

# Create larger array
arr = np.array([10, 20, 30, 40, 50, 60])
print("Original array:", arr)

print("----------------------")

# Split array
split_arrays = np.split(arr, 3)
print("Split arrays:", split_arrays)