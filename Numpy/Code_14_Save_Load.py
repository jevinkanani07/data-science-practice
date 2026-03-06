# NumPy Code 14
# Topic: Saving and Loading Arrays

import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50])

print("Original array:", arr)

print("------------------")

# Save array as .npy file
np.save("data.npy", arr)
print("Array saved as data.npy")

print("------------------")

# Load array from .npy file
loaded_arr = np.load("data.npy")
print("Loaded array:", loaded_arr)

print("------------------")

# Save as text file
np.savetxt("data.txt", arr)

print("Array saved as data.txt")

print("------------------")

# Load text file
loaded_txt = np.loadtxt("data.txt")
print("Loaded from text file:", loaded_txt)