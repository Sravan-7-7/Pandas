
'''NOW I AM GOING TO SHOW YOY HOW WE CAN FIX OR CHANGE DATA TYPES'''

import pandas as pd

df = pd.read_csv('data.csv')

# NOW LET'S CHANGE THE LENGENDARY INTO BOOLEAN TYPE...

df['Legendary'] = df['Legendary'].astype(bool)
print(df.to_string())
print('--------------------------------')