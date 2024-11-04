# Importing the libraries
import pandas as pd
import numpy

# Step 1 : Importing the dataset
print("Begin Step 1 : Importing the dataset:")
path = "C:/Users/ofirn/ofir things/studying/college/kinneret/year2/ai by aiad suliman/adds-on/01-Data Preprocessing"
csv_file = "data.csv"
csv_file_path = path + "/" + csv_file
dataset = pd.read_csv(csv_file_path)
print(dataset)
print("End Step 1 : Importing the dataset: \"", csv_file, "\"")
print()


# Step 2 : Check out the Missing Values
print("Begin Step 2 : After dropping the Missing Values")

dataset = dataset.replace(0, numpy.nan)
# fill missing values with mean column values
dataset.fillna(dataset.median(axis=0,numeric_only=True), inplace=True)
print(dataset)
print("End Step 2 : After dropping the Missing Values")
print()

# Step 3 : Encoding categorical data
print("Begin Step 3 : Encoding categorical data")
State = {'France': 1,'Spain': 2, 'Germany': 3}
print()
dataset.Country = [State[item] for item in dataset.Country]
y = dataset['Purchased'].values
print(dataset)
print("End Step 3 : Encoding categorical data")
print()
