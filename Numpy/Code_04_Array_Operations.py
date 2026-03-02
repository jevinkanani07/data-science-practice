# NumPy Code 04
# Topic: Array Operations and Broadcasting

import numpy as np

# Create arrays
arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])

print("Array 1:", arr1)
print("Array 2:", arr2)

print("------------------")

# Arithmetic Operations
print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

print("------------------")

# Broadcasting (single value with array)
print("Add 5 to arr1:", arr1 + 5)
print("Multiply arr1 by 2:", arr1 * 2)

print("------------------")

# Statistical Operations
print("Mean:", np.mean(arr1))
print("Sum:", np.sum(arr1))
print("Max:", np.max(arr1))
print("Min:", np.min(arr1))