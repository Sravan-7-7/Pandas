import pandas as pd

df = pd.read_csv('data.csv')

'''IN MY DATAFRAME THERE ARE MANY POKEMON THAT DON'T HAVE A SECOND TYPE, BUT ALL THE POKEMONS
   DO HAVE A FIRST TYPE ... '''

# IF A ROW IS MISSING A VALUE WITHIN TYPE TWO WE'RE GOING TO DROP THAT ENTIRE ROW . HERE'S HOW TO DO THAT...

df = df.dropna(subset=['Type2'])

# dropna = DROP NOT AVALIABLE

print(df.to_string())
print('---------------------------------------')

'''IN PLACE OF DROPPING ANY ROWS WHERE THE VALUES ARE NOT AVALIABLE, LET'S REPLACE THEM INSTEAD WITH A DIFFERENT FUNCTION'''

df = df.fillna({'Type2' :'None' })

# fillna = FILL ANY NOT AVALIABLE VALUES

print(df.to_string())
print('----------------------------------------')
