# NumPy Code 08
# Topic: Boolean Indexing and Filtering

import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50, 60])

print("Original array:", arr)

print("------------------")

# Boolean condition
condition = arr > 30
print("Condition (arr > 30):", condition)

print("------------------")

# Filtering using condition
filtered = arr[arr > 30]
print("Values greater than 30:", filtered)

print("------------------")

# Multiple conditions
filtered2 = arr[(arr > 20) & (arr < 60)]
print("Values between 20 and 60:", filtered2)

print("------------------")

# Replace values using condition
arr[arr > 40] = 100
print("Modified array:", arr)