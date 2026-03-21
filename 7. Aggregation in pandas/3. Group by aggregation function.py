'''Group by(): It is a function that we can arrange our dataframe into different groups 
               together rows by something that they have in common...'''

'''LET'S GROUP OUR DATAFRAME BY EACH CREATURE'S TYPE...'''

import pandas as pd

df = pd.read_csv('data.csv')

# grouping the mean of the height in type1

group = df.groupby('Type1')

print(group['Height'].mean())
print('--------------------------')

# grouping the sum of the height in type1

print(group['Height'].sum())
print('--------------------------')

# grouping the minimum height in type1

print(group['Height'].min())
print('--------------------------')

# grouping the maximum height in type1

print(group['Height'].max())
print('--------------------------')

# grouping the count height in type1

print(group['Height'].count())
print('--------------------------')


