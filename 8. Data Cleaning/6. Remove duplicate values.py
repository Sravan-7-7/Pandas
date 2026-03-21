'''NOTE: BEFORE GOING TO PERFORME THIS CODE MAKE SURE YOU COPY SAME NAMES IN YOUR CSV FILE AND SAVE THEM... '''

import pandas as pd

df = pd.read_csv('data.csv')

df = df.drop_duplicates()

print(df.to_string())
