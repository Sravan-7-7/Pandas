'''FILTERING : Keeping the rows that match a condition when working with the dataframe...'''


import pandas as pd

df = pd.read_csv('data.csv')

# filtering any pokemon that have a height above 2 meters 

tall_pokemons = df[df['Height'] >= 2]
print(tall_pokemons)
print('-----------------------------------')

# filtering any pokemon that have a weighy above 100kg...

heavy_pokemon = df[df['Weight'] >= 100]
print(heavy_pokemon)
print('----------------------------------------')
