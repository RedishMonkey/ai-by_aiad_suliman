import pandas as pd


path = 'C:/Users/ofirn/ofir things/gitRepositories/ai-by_aiad_suliman/half simester work/project ai/project ai/bank.csv'
# Sample data (replace with your dataset if reading from a file)
dataArr = []
columns = []

# Convert the data into a DataFrame
df = pd.read_csv(path)

# 1. Map 'default' column to numerical values (0 for 'no', 1 for 'yes')
for column in df:
    colData = df[column]
    if type(colData[0]) == str:
        print('entered')
        encodedValsCount = 0
        mapDict = {}
        for value in df[column]:
            if value not in mapDict:
                mapDict[value] = encodedValsCount
                encodedValsCount += 1
        print(mapDict)
        df[column] = df[column].map(mapDict)
    

path = 'C:/Users/ofirn/ofir things/gitRepositories/ai-by_aiad_suliman/half simester work/project ai/project ai'
processedFileName = 'processedBank.csv'
fullPath = path + "/" + processedFileName
df.to_csv(fullPath, index=False)


# print(df)


