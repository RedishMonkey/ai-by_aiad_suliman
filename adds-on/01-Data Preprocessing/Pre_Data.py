# Importing the libraries
import pandas as pd


# Step 1 : Importing the dataset
print("Begin Step 1 : Importing the dataset:")
path = "K:/"
csv_file = "data.csv"
csv_file_path = path+ "/"+ csv_file
dataset = pd.read_csv(csv_file_path)
print(dataset)
print("End Step 1 : Importing the dataset: \"", csv_file, "\"")
print()

# Step 2 : Check out the Missing Values
print("Begin Step 2 : After dropping the Missing Values")
import numpy
dataset = dataset.replace(0, numpy.NaN)
# fill missing values with mean column values
dataset.fillna(dataset.median(), inplace=True)
print(dataset)
print("End Step 2 : After dropping the Missing Values")
print()

# Step 3 : Encoding categorical data
print("Begin Step 3 : Encoding categorical data")
State = {'New York': 1,'California': 2, 'Florida': 3}
dataset.State = [State[item] for item in dataset.State]
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
print("Step 5 : Splitting the dataset into the Training set and Test set")
print("X_train")
print(X_train)
print()
print("X_test")
print(X_test)
print()
print("y_train")
print(y_train)
print()
print("y_test")
print(y_test)
print()
