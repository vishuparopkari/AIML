# Practical-37: Using np.pi and np.linspace with NumPy

import numpy as np

# Value of π from NumPy
print("np.pi = ", np.pi)

# Generating 11 evenly spaced values from -5 to 5
print("\n", np.linspace(-5, 5, 11))

# Generating 21 evenly spaced values from -5 to 5
print("\n", np.linspace(-5, 5, 21))

# Generating 255 evenly spaced values from -π to π
print("\n", np.linspace(-np.pi, np.pi, 255))

