import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5],[1,2,3,4,5],'bo-',label='Team 1', linewidth=3)
plt.plot([1,2,3,4,5],[1,4,9,16,25],'rs--',label='Team 2', linewidth=10)


plt.axis([-3,6,-5,50])

plt.legend(loc="upper left")

plt.show()