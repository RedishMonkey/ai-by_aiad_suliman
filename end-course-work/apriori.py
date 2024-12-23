# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Data Preprocessing
folder_path = os.path.dirname(__file__)

print(f"Folder Path: {folder_path}")
# Step 1 : Importing the dataset
path = os.path.dirname(__file__)
csv_file = "GroceryDataset.csv"
csv_file_path = path+ "/"+ csv_file
dataset = pd.read_csv(csv_file_path, header = None)
transactions = []

for i in range(0, 1758):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 8)])

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.01, min_confidence = 0.1, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)

for rule in results:
    print(rule)
    print("\n\n")
