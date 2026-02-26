import numpy as np

# Create 1D array
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1)

# Create 2D array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n2D Array:")
print(arr2)

# Check type
print("\nType of arr1:", type(arr1))

# Check shape
print("Shape of arr2:", arr2.shape)

# Check number of dimensions
print("Dimensions of arr2:", arr2.ndim)