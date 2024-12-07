# try:
lines = ""
# Open the input file in read mode
path = 'C:/Users/ofirn/ofir things/gitRepositories/ai-by_aiad_suliman/half simester work/project ai/project ai/'
readFileName = 'bank.csv'
processedFileName = 'processedBank'
fullPath = path + readFileName
with open(fullPath, 'r') as infile:
    lines = infile.readlines()

fullPath = path + processedFileName
# Open the output file in write mode
with open(fullPath, 'w') as outfile:
    for line in lines:
        # Find the first comma in the line
        comma_index = line.find(',')

        # If a comma exists, insert a quote before it
        if comma_index != -1:
            modified_line = line[:]
        else:
            modified_line = line
            
        # Write the modified line to the output file
        outfile.write(modified_line)
# except Exception as e:
#     print(e)