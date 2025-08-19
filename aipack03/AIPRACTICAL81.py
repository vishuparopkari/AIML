import warnings
warnings.filterwarnings(action="ignore")

import matplotlib.pyplot as plt

plt.figure(1)

plt.subplot(311)
plt.plot([1, 2, 3])

plt.subplot(312)
plt.plot([4, 5, 6])

plt.subplot(313)
plt.plot([7, 8, 9])

plt.figure(2)
plt.plot([11, 12, 13])


plt.figure(1)
plt.subplot(311)
plt.title('Easy as 1,2,3')

plt.figure(3)
import numpy as np
x = np.arange(1,6)
y = x ** 2
plt.plot(x, y,'ro-')
plt.show()