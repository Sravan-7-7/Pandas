'''                                                                  SELECTION BY COLOMN                                                                         '''

import pandas as pd

df = pd.read_csv('data.csv')
print(df['Name']) # prints first five rows and last five rows(truncated_version)
print('-----------------------------------')
print(df['Name'].to_string()) # by using to_string() it prints all rows(non-truncated_version)
print('------------------------------------')

print(df['Height'].to_string()) # prints only heights(m) of all rows
print('---------------------------')
print(df['Weight'].to_string()) # prints only weights(kg) of all rows
print('---------------------------')
print(df[['Name', 'Height', 'Weight']].to_string()) # prints name, height, weight of all rows
print('----------------------------')


