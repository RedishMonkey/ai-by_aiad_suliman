# Decision Tree Regression

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1 : Importing the dataset
path = "C:/Users/ofirn/ofir things/gitRepositories/ai-by_aiad_suliman/half simester work/project ai/project ai/decision-trees"
csv_file = "processedBank.csv"
csv_file_path = path+ "/"+ csv_file
dataset = pd.read_csv(csv_file_path)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X)

print(np.shape(X))
# Fitting Decision Tree Regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, y)


# # Visualising the Decision Tree Regression results (higher resolution)
# X_grid = np.arange(np.min(X[:,0]), np.max(X[:,0]), 0.01)
# X_grid = X_grid.reshape((len(X_grid), 1))
# plt.scatter(X, y, color = 'red')
# plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
# plt.title('Truth or Bluff (Decision Tree Regression)')
# plt.xlabel('Position level')
# plt.ylabel('Salary')
# plt.show()

from sklearn.metrics import mean_squared_error, r2_score


y_pred = regressor.predict(X)

# Calculating R-squared (coefficient of determination)
r2 = r2_score(y, y_pred)
print(f"R-squared: {r2}")

# Calculating Mean Squared Error (MSE)
mse = mean_squared_error(y, y_pred)
print(f"Mean Squared Error: {mse}")

# Visualising the Decision Tree Regression results (higher resolution)
X_grid = np.arange(np.min(X), np.max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()