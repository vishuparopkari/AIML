import warnings
from statistics import correlation

from hvplot import scatter_matrix

warnings.filterwarnings(action="ignore")
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix





hnames=['preg','plas','pres',
        'skin', 'test', 'mass',
        'pedi','age','class',]

dataframe=pd.read_csv('indians-diabetes.data.csv',names=hnames)

scatter_matrix(dataframe)
plt.show()