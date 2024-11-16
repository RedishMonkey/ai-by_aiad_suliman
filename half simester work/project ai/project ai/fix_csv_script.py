try:
    # Open the input file in read mode
    path = 'C:\\Users\\543\\Desktop\\project ai\\bank.csv'
    with open(path, 'r') as infile:
        lines = infile.readlines()

    # Open the output file in write mode
    with open(path, 'w') as outfile:
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
except:
    print("problem")