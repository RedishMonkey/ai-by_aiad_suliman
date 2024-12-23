# Decision Tree Regression

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.tree import plot_tree

folder_path = os.path.dirname(__file__)

print(f"Folder Path: {folder_path}")

# Step 1 : Importing the dataset
path = os.path.dirname(__file__)
csv_file = "diabetes.csv"
csv_file_path = path+ "/"+ csv_file
dataset = pd.read_csv(csv_file_path)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# split data into training data and testing data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeClassifier
regressor = DecisionTreeClassifier(max_depth=5, min_samples_split=10, random_state = 0)
regressor.fit(X_train, y_train)







y_train_pred = regressor.predict(X_train)
y_test_pred = regressor.predict(X_test)


plt.figure(figsize=(12, 8))  # Adjust the figure size for better visibility
plot_tree(regressor, feature_names=dataset.columns[:-1], filled=True)
plt.title("Decision Tree Visualization")
plt.show()



from sklearn.metrics import precision_score, recall_score

precision = precision_score(y_test, y_test_pred)
recall = recall_score(y_test, y_test_pred)


print("\nperformance test:")
print(f"precision: {precision}")
print(f"recall: {recall}")