# NumPy Code 09
# Topic: Linear Algebra Operations

import numpy as np

# Create matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("------------------")

# Dot product
dot_product = np.dot(A, B)
print("Dot Product:\n", dot_product)

print("------------------")

# Matrix multiplication
matmul = A @ B
print("Matrix Multiplication:\n", matmul)

print("------------------")

# Transpose
print("Transpose of A:\n", A.T)

print("------------------")

# Determinant
det_A = np.linalg.det(A)
print("Determinant of A:", det_A)

print("------------------")

# Inverse
inverse_A = np.linalg.inv(A)
print("Inverse of A:\n", inverse_A)