# Decision Tree Regression

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1 : Importing the dataset
print("Begin Step 1 : Importing the dataset:")
# ================================
path = "K:/academia.Kineret/2020-2021/2nd/Script Languages/Lectures/Regression"
csv_file = "Position_Salaries.csv"
csv_file_path = path+ "/"+ csv_file
dataset = pd.read_csv(csv_file_path)
# ================================

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)


# Visualising the Decision Tree Regression results (higher resolution)
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

