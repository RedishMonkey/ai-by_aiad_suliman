# Multiple Linear Regression

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1 : Importing the dataset
print("Begin Step 1 : Importing the dataset:")
# ================================
path = "K:/academia.Kineret/2020-2021/2nd/Script Languages/Lectures/Regression"
csv_file = "50_Startups.csv"
csv_file_path = path+ "/"+ csv_file
dataset = pd.read_csv(csv_file_path)
# ================================
print(dataset)
print("End Step 1 : Importing the dataset: \"", csv_file, "\"")
print()

# Step 3 : Encoding categorical data
print("Begin Step 3 : Encoding categorical data")
State = {'New York': 1,'California': 2, 'Florida': 3}
dataset.State = [State[item] for item in dataset.State]
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
print(dataset)
print("End Step 3 : Encoding categorical data")
print()

# Step 4 :  Feature Scaling
print("Begin Step 4 : Feature Scaling")
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
dataset = scaler.fit_transform(dataset)
print(dataset)
print("End Step 4 : Feature Scaling")
print()

# Step 5 : Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X = dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

print(regressor.intercept_)
print(regressor.coef_)