import pandas as pd
import os

# getting csv file
dir_path = os.path.dirname(__file__)
csv_path = dir_path + '/' + 'Social_Network_Ads.csv'

df = pd.read_csv(csv_path)


# mapping the Gender column

gender_map = {'Male':1, 'Female':0}
df['Gender'] = df['Gender'].map(gender_map)

# writing the processed csv into a new file

df.to_csv('processed_csv.csv')