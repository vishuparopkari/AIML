# Understand Your Data With Visualization

# A) - Univariate Plots
#     A.1) Univariate Histogram Plot.
#     A.2) Univariate Density Plots.
#     A.3) Univariate Box and Whisker Plots.

import pandas
import matplotlib.pyplot as plt

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pandas.read_csv(filename, names=hnames)
print(dataframe)
dataframe.hist()
plt.tight_layout()
plt.show()
