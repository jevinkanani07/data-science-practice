# NumPy Code 06
# Topic: Random and Statistical Functions

import numpy as np

# Set seed (for same random results every time)
np.random.seed(42)

# Generate random integers
random_int = np.random.randint(1, 100, size=5)
print("Random integers:", random_int)

print("------------------")

# Generate random float numbers
random_float = np.random.rand(3)
print("Random floats:", random_float)

print("------------------")

# Generate random 2D array
random_matrix = np.random.randint(0, 10, size=(2, 3))
print("Random 2D matrix:\n", random_matrix)

print("------------------")

# Statistical functions
data = np.array([10, 20, 30, 40, 50])

print("Data:", data)
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Sum:", np.sum(data))