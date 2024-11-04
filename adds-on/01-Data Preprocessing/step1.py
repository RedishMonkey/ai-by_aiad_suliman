# Importing the libraries
import pandas as pd


# Step 1 : Importing the dataset
print("Begin Step 1 : Importing the dataset:")
path = "C:/Users/ofirn/ofir things/studying/college/kinneret college/year 2/ai by aiad suliman/adds-on/01-Data Preprocessing"
csv_file = "data.csv"
csv_file_path = path+ "/"+ csv_file
dataset = pd.read_csv(csv_file_path)
print(dataset)
print("End Step 1 : Importing the dataset: \"", csv_file, "\"")
print()
