import pandas as pd

df = pd.read_csv('data.csv')

# let's find water pokemons...

water_pokemon = df[df['Type1'] == 'Water']
print(water_pokemon)
print('--------------------------------------------------------------------')


# by using OR logical operators..

water_pokemon = df[(df['Type1'] == 'Water') | (df['Type2'] == 'Water')]

print(water_pokemon) # IF THE FIRST AND SECOND TYPE IS WATER IT RETURN'S THAT ROW..

print('--------------------------------------------------------------------')


# by using AND logical operator...

ff_pokemon = df[(df['Type1'] == 'Fire') & (df['Type2'] == 'Flying')]

print(ff_pokemon) # ..

print('------------------------------')
