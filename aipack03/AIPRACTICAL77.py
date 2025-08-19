import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0,5.0,0.2)

print(t)
plt.plot(t, t, 'r*-',
               t, t+3, 'bs-',
               t, t+6 , 'go-',
               t, t+9, 'g-',
               t, t+9, 'ro',
               markersize=7)

plt.show()