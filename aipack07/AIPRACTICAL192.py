'''
1) LinearRegression    (y=mx+c)
2) LogisticRegression (sigmoid function)
3) NB Algorithm (Condition Probability)
4) DecisionTree Algo (CART) (Entropy & I.G. OR Ginni Index)
5) RandomForest Algo [ensemble of bagging{=Bootstrap Aggregation} ]
6) Support Vector Machine Algo (Maximize the minimum margin between two diff classes )
7) KNN Algo (Euclidian Distance )
8) LDA
'''
import warnings
warnings.filterwarnings(action="ignore")

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Step 2: Load dataset
df = pd.read_csv("customers_LDA2.csv")
print("Dataset:\n", df)

# Step 3: Define features and target for training
X = df[['Age','Salary']]
y = df['Buy']

#step4 : Train LDA model
lda = LinearDiscriminantAnalysis()
lda.fit(X, y)

#step 5: make prediction
# Example: predict for a costumer (age=30,salary=32000)
age=int(input("Enter age: "))
salary=int(input("Enter salary: "))
sample = [[age,salary]]
prediction = lda.predict(sample)

result = None
if prediction == 1:
    result = "Buy"
else:
    result = "not Buy"

print(f"\nprediction for age {age} salary{salary}:", result)
