import pandas as pd
import numpy as np

print("numpy matrix = \n\n", np.random.randn(6,4))

df = pd.DataFrame(np.random.randn(6,4),
                  index = pd.date_range('20190101', periods=6, freq='D'),
                  columns = ['A','B','C','D'] )

print("Original \n",df)

print("\n\n")

print(df.sort_index(axis=1, ascending=False))

print("\n\n")
print(df.sort_index(axis=0, ascending=False))