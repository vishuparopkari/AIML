import numpy as np
n1 = np.full([5,7],7)

print("Array=\n",n1)

print("Sum of 1st row =", n1[1,:].sum())
print("Sum of 1st column =", n1[:,1].sum())

print("Total sum = ", n1.sum())