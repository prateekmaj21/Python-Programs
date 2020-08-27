# Numpy Linear Algebra 2

import numpy as np
from numpy import linalg as lin

#creating the numpy array
a = np.array([[5, -3j], [8j, 3]])

print("Array :")
print(a)

print("Type of array :", type(a))


# calculating an eigen value
# using eigh() function

e, f = lin.eigh(a)

print("Eigen value is :", e)
print("Eigen value is :", f)