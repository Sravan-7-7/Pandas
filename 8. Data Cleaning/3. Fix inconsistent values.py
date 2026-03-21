
'''NOW WE'RE GOING TO FIX ANY INCONSISTENT VLAUES.WE CAN REPLACE ANY INSTANCE OF A VALUE WITH
   ANOTHER ONE'''



import pandas as pd

df = pd.read_csv('data.csv')

# WITHIN TYPE ONE, LET'S SELECT ANY GRASS TYPES. WE'LL CHANGE ANY INSTANCE OF GRASS TO BE ALL UPPERCASE LETTERS. HERE'S HOW YOU CAN DO THAT..

df['Type1'] = df['Type1'].replace({'Grass': 'GRASS'})
print(df.to_string())
print('--------------------------------')

# IT WON'T CHANGE ANY INSTANCE OF TYPE2. BECAUSE WE SELECTED TYPE1...

# WITHIN OUR DICTINORY WE CAN PASS MORE THAN ONE KEY VALUE PAIR. LET'S REPLACE ANY INSSTANCE OF Fire WITH FIRE..

df['Type1'] = df['Type1'].replace({'Grass': 'GRASS',
                                   'Fire': 'FIRE',
                                   'Water': 'WATER'})
print(df.to_string())
print('--------------------------------')
