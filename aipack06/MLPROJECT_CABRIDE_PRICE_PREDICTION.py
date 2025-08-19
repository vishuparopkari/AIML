'''

MLProject Cab Ride Price Prediction
==================================
Assignment Part-01: Import Libraries
Question: Which libraries are imported for data manipulation, visualization, and machine learning?

Assignment Part-02: Configure Pandas Display
Question: How would you configure pandas to display all rows/columns and set the display width to 1000?

Assignment Part-03: Load Data
Question: Write code to load a CSV dataset named rideshare_dataset.csv into a variable of DataFrame named as 'data'.

Assignment Part-04: Create DataFrame Copy
Question: How do you create a new duplicate working copy of a DataFrame 'data' to 'df'?

Assignment Part-05: Inspect Missing Values
Question: How would you check for missing values in each column of df?

Assignment Part-06: Handle Missing Values
Question: Write code to drop rows with missing values specifically in the price column.

Assignment Part-07: Drop Irrelevant Columns
Question: Remove columns ['id', 'latitude', 'longitude', 'product_id', 'timezone'] from df in-place.

Assignment Part-08: Analyze Temporal Data
Question: How would you check the minimum and maximum values in the datetime column?

Assignment Part-09: Filter Columns by Correlation
Question: How do you select only following given environment-related columns and price from 'df' dataframe?

enviroment_cols = ['temperature', 'apparentTemperature',
'precipIntensity', 'precipProbability', 'humidity', 'windSpeed',
'windGust', 'windGustTime', 'visibility', 'temperatureHigh',
'temperatureHighTime', 'temperatureLow', 'temperatureLowTime',
'apparentTemperatureHigh', 'apparentTemperatureHighTime',
'apparentTemperatureLow', 'apparentTemperatureLowTime',
'dewPoint', 'pressure', 'windBearing', 'cloudCover', 'uvIndex',
'visibility.1', 'ozone', 'sunriseTime', 'sunsetTime', 'moonPhase',
'precipIntensityMax', 'uvIndexTime', 'temperatureMin',
'temperatureMinTime', 'temperatureMax', 'temperatureMaxTime',
'apparentTemperatureMin', 'apparentTemperatureMinTime',
'apparentTemperatureMax', 'apparentTemperatureMaxTime', 'price']


Assignment Part-10: Drop Low-Correlation Features
Question: If environment columns have low correlation with price,
how would you drop all 36 environment related columns except price column?

Assignment Part-11: Handle Boolean Values in Categorical Encoded Variables
Question: Use the follwoing python code to convert given categorical columns in one-hot encoding and then
replace True / False values in 'df_prep' dataframe with 1 / 0.
df_prep = pd.get_dummies(df, columns=['icon', 'source', 'destination', 'cab_type', 'name'])

Assignment Part-12: Detect Outliers with Boxplot
Question: Generate a boxplot to visualize outliers in the price column using boxplot() function of seaborn.

Assignment Part-13: Remove Outliers Using IQR
Question: For the price column, calculate IQR and filter rows where price < Q3 + 1.5*IQR.




===============================================================================


Assignment Part-14: Train-Test Split
Question: Split features x and target y into 20% training and 80% testing sets.

Assignment Part-15: Standardize Features
Question: Standardize x using StandardScaler and fit-transform on training data.

Assignment Part-16: Train Linear Regression Model
Question: Initialize and train a LinearRegression model on x_train and y_train.

Assignment Part-17: Calculate Regression Metrics
Question: For predictions y_pred, compute MAE, MSE, and R².

Assignment Part-18: Train Random Forest Model
Question: Fit a RandomForestRegressor on the training data and generate predictions.


'''

# Assignment Part-01: Import Libraries
#
# Libraries imported for:
# - Data manipulation and analysis: pandas
# - Numerical operations: numpy
# - Data visualization: matplotlib.pyplot and seaborn
# - Machine learning: scikit-learn (sklearn)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets, linear_model

# ---

# Assignment Part-02: Configure Pandas Display
#
# This configures pandas to display all rows and columns without truncation,
# and sets the display width to 1000 characters for better readability.
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# ---

# Assignment Part-03: Load Data
#
# The `rideshare_dataset.csv` file is loaded into a pandas DataFrame
# and assigned to the variable 'data'.
try:
    data = pd.read_csv('rideshare_dataset.csv')
    print("Dataset 'rideshare_dataset.csv' loaded successfully.")
except FileNotFoundError:
    print("Error: The file 'rideshare_dataset.csv' was not found.")
    data = None # Assign None to handle the missing file gracefully

# ---

# Assignment Part-04: Create DataFrame Copy
#
# A duplicate working copy of the 'data' DataFrame is created and assigned
# to a new variable 'df'. Using `.copy()` is crucial to prevent `SettingWithCopyWarning`
# and ensure changes to 'df' do not affect the original 'data' DataFrame.
if data is not None:
    df = data.copy()
    print("\nWorking copy of the DataFrame created as 'df'.")

# ---

# Assignment Part-05: Inspect Missing Values
#
# This code checks for and sums up the number of missing values (NaN) in
# each column of the 'df' DataFrame. The result shows the count of
# missing values per column.
if 'df' in locals():
    print("\nChecking for missing values in the DataFrame 'df':")
    missing_values = df.isnull().sum()
    print(missing_values)
