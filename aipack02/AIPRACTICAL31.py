# Practical-31
import numpy as np

# we can create numpy array from range
ar = np.arange(11 , 16-1 )  # Rule of II & EE
ar1 = np.arange(-11 , -1 )

print("ar = ", ar)
# ar = [11, 12, 13, 14, 15]
#       0   1   2   3   4
print("ar = ", ar1)

ar[3] = 77

print("After updating, ar = ", ar)
# [11, 12, 13, 77, 15]
