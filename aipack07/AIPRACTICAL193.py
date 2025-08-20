import warnings
warnings.filterwarnings(action="ignore")

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Step 2: Load dataset
df = pd.read_csv("customers_LDA2.csv")
print("Dataset:\n", df)
# Step 2: Separate data for visualization
X = df["Age"]
Y = df["Salary"]
Z = df["Buy"]

# Step 3: Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot Buy=1 in green and Buy=0 in red
ax.scatter(X[Z==1], Y[Z==1], Z[Z==1], c='green', marker='o', label='Buy')
ax.scatter(X[Z==0], Y[Z==0], Z[Z==0], c='red', marker='x', label='Not Buy')

# Step 4: Set labels
ax.set_xlabel("Age")
ax.set_ylabel("Salary")
ax.set_zlabel("Buy (0=No, 1=Yes)")
ax.set_title("3D Visualization of Customers Dataset")

ax.legend()
plt.show()
