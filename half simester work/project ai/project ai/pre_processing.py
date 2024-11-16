import pandas as pd
import csv

path = 'C:\\Users\\543\\Desktop\\project ai\\bank.csv'
# Sample data (replace with your dataset if reading from a file)
dataArr = []
columns = []

# Convert the data into a DataFrame
df = pd.read_csv(path)

# 1. Map 'default' column to n  umerical values (0 for 'no', 1 for 'yes')
for column in df:
    colData = df[column]
    if type(colData) == str:
        encodedValsCount = 0
        mapDict = {}
        print("entered")
        for value in df[column]:
            if value not in mapDict:
                mapDict[value] = encodedValsCount
                encodedValsCount += 1
        print(mapDict)
        # df[column] = df[column].map(mapDict)
# print(df)
# dict = {"key1":1, 2:"key2"}
# print(f'"key1" in dict: {"key1" in dict}')
# print(f'"1" in dict: {1 in dict}')
# print(f'"2" in dict: {2 in dict}')
# print(f'"key2" in dict: {"key2" in dict}')
# # 2. Treat 'unknown' or -1 values in 'default' column as 'no' (0)
# df['default'].fillna(0, inplace=True)
#
# # 3. Replace -1 with NaN for balance, pdays, and previous columns (to be handled separately if needed)
# df.replace(-1, pd.NA, inplace=True)
#
# # 4. One-hot encode categorical columns
# categorical_columns = ['job', 'marital', 'education', 'housing', 'loan', 'contact', 'month', 'poutcome', 'y']
# df_encoded = pd.get_dummies(df, columns=categorical_columns, drop_first=True)
#
# # 5. Display the processed DataFrame
# print(df_encoded)
#
# # Optionally, save the processed DataFrame to a new file
# # df_encoded.to_csv('processed_data.csv', index=False)