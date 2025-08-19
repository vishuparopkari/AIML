# Practical-36: Transposing arrays using NumPy

import numpy as np

# Creating a 2x3 matrix
na = np.array([[1, 2, 3],
               [4, 5, 6]])

# Original array
print("na = \n", na)

# Transpose using .transpose() method
print("na.transpose() = \n", na.transpose())

# Transpose using .T shorthand
print("na.T = \n", na.T)

# Confirming original array is unchanged
print("na = \n", na)