# Numpy Linear Algebra 1

import numpy as np

A = np.array([[7, 1, 1, 8],
              [4, -2, 5, -5],
              [2, 8, 4, -4],
              [3, 6,-1, 7] ])

print(" Array A= ")
print(A)

# Rank of the matrix
print("Rank of matrix A:", np.linalg.matrix_rank(A))

# Shape of matrix 

print("Shape of matrix A:", A.shape)

# Trace of matrix A
print("Trace of A:", np.trace(A))

# Inverse of matrix A
print("\nInverse of A:\n", np.linalg.inv(A))


print("\nMatrix A raised to power 2:\n",
           np.linalg.matrix_power(A, 2))