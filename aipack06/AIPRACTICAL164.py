# B) Multivariate Plots
# ******************************************
#     #1) - Correlation Matrix Plot.
#     #2) - Scatter Matrix Plot.
import warnings
warnings.filterwarnings(action="ignore")

# Correlations Matrix Plot
import matplotlib.pyplot as plt
import pandas as pd
import numpy
pd.set_option('display.width', 1000)
pd.set_option('display.max_column', None)

hnames = ['preg', 'plas', 'pres',
          'skin', 'test', 'mass',
          'pedi', 'age', 'class']

dataframe = pd.read_csv(filepath_or_buffer='indians-diabetes.data.csv', names=hnames)

correlations = dataframe.corr()
print(correlations)
fig = plt.figure()

# Following will add matrix and side bar in entire area
subFig = fig.add_subplot(111)

cax = subFig.matshow(correlations, vmin=-1, vmax=1)

fig.colorbar(cax)

# ----------------------------
ticks = numpy.arange(0, 9)  # It will generate values from 0,1,2,3,4,5,6,7,8
subFig.set_xticks(ticks)
subFig.set_yticks(ticks)
subFig.set_xticklabels(hnames)
subFig.set_yticklabels(hnames)
# ----------------------------

plt.show()
