'''TO DEMONSTRATE, WITHIN OUR NAME COLUMN,LET'S TAKE ALL THE INDIVIDUAL NAMES AND MAKE THEM LOWERCASES...'''

import pandas as pd

df = pd.read_csv('data.csv')


df['Name'] = df['Name'].str.lower()
print(df.to_string())
print('-------------------------------------')
