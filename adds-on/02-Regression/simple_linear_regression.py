# Simple Linear Regression

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1 : Importing the dataset
print("Begin Step 1 : Importing the dataset:")
# ================================
path = "K:/academia.Kineret/2020-2021/2nd/Script Languages/Lectures/Regression"
csv_file = "Salary_Data.csv"
csv_file_path = path+ "/"+ csv_file
dataset = pd.read_csv(csv_file_path)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
# ================================
print(dataset)
print("End Step 1 : Importing the dataset: \"", csv_file, "\"")
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
# ================================
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
# ================================

# Fitting Simple Linear Regression to the Training set
# ================================
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

print(regressor.intercept_)
print(regressor.coef_)

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


