import numpy as np
import pandas as pd
import numpy

oldExcel = 'C:/Users/ofirn/ofir things/studying/college/kinneret/year2/ai by aiad suliman/classwork 1/UpdatedExcelFile.xlsx'
# os.remove(oldExcel)

# step 1
path = "C:/Users/ofirn/ofir things/studying/college/kinneret/year2/ai by aiad suliman/classwork 1"
excel_file = "ElectionsData.xlsx"
excel_file_path = path + "/" + excel_file
dataset = pd.read_excel(excel_file_path)
print(dataset)
print(f"End Step 1 : Importing the dataset: \"{excel_file}, \"")
print()

# hash table of all none number data types
datasetHashTable = {}

# create a big dictionary that has a hash table for each none number datatype
for colName in dataset:

    if type(dataset[colName][0]) == str: # checks if its a non number datatype

        datasetHashTable[colName] = {}
        currHashTable = datasetHashTable[colName]
        count = 0
        for itemData in dataset[colName]:
            colValueRanges = currHashTable.keys()

            if pd.isna(itemData): # checks if the cell is empty
                # currHashTable['none'] = None

            elif itemData not in colValueRanges: # if not empty cell and didnt add value index yet then add it
                currHashTable[itemData] = count
                count += 1


colNames = datasetHashTable.keys()

# turn non number values into number values
for col in colNames:
    dataset[col] = dataset[col].map(datasetHashTable[col])

# fill none cells
for col in dataset:
    median = numpy.floor(dataset[col].median())
    dataset[col] = dataset[col].fillna(median)

# normalizing data thats not in a fixed range
for col in dataset:
    if col not in colNames:
        minVal = dataset[col].min()
        maxVal = dataset[col].max()
        dataset[col] = numpy.subtract(dataset[col], minVal)
        dataset[col] = numpy.divide(dataset[col], maxVal - minVal)




print(f"End Step 2 : filling and indexing data")


updated_path = "C:/Users/ofirn/ofir things/studying/college/kinneret/year2/ai by aiad suliman/classwork 1/UpdatedExcelFile.xlsx"
dataset.to_excel(updated_path, index=False)