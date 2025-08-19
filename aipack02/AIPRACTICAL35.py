#practical Part 1

import numpy as np
n1 = np.array([4,5,6])
print (n1 + 1)

#practical Part 2

import numpy as np

n4 = np.array([10, -1, 0, 90, 300, 3, -6, 2])
print("Before: n4 =", n4)

n5 = sorted(n4, reverse=True)  # External Sorting
print("n5 =", n5)
print("After: n4 =", n4)

n4.sort()  # Internal Sorting or In-place sorting
print("After n4.sort() =", n4)
print("After n4.sort() =", list(reversed(n4)))
print("After n4.sort() =", tuple(reversed(n4)))

