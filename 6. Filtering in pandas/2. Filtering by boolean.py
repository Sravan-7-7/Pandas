
import pandas as pd

df = pd.read_csv('data.csv')

# filtering any pokemon that are legendary ...

legendary_pokemon = df[df['Legendary'] == 1]
print(legendary_pokemon)
print('----------------------------------------')

# by using boolean function..

legendary_pokemon = df[df['Legendary'] == True]
print(legendary_pokemon)
print('----------------------------------------')


