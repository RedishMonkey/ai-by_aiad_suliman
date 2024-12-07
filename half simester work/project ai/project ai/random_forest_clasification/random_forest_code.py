# Random Forest Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Importing the dataset
path = os.path.dirname(__file__)
csv_file = "diabetes.csv"
csv_file_path = path+ "/"+ csv_file

dataset = pd.read_csv(csv_file_path)

X = dataset.iloc[:,:-1]
y = dataset.iloc[:,-1]

# splits the data into training and testing data and setting parameters (X) and the outcome (y)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=3, random_state=42, min_samples_split=10, max_depth=5)
regressor.fit(X_train, y_train)

# Visualising the Random Forest Regression results (higher resolution)
from sklearn.tree import plot_tree
for i,tree in enumerate(regressor.estimators_):
    plt.figure(figsize=(10, 5))
    plot_tree(tree, feature_names=dataset.columns[:-1], filled=True)
    plt.title(f"Tree {i + 1}")
    plt.show()


# Evaluate R² and MSE on both sets
from sklearn.metrics import mean_squared_error, r2_score

y_train_pred = regressor.predict(X_train)
y_test_pred = regressor.predict(X_test)

print("Training Performance:")
print(f"R² (Train): {r2_score(y_train, y_train_pred)}")
print(f"MSE (Train): {mean_squared_error(y_train, y_train_pred)}")

print("\nTesting Performance:")
print(f"R² (Test): {r2_score(y_test, y_test_pred)}")
print(f"MSE (Test): {mean_squared_error(y_test, y_test_pred)}")

