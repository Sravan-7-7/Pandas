import pandas as pd

df = pd.read_csv('data.csv')

'''NOW RATHER THAN SELECTING THE ENTIRE DATAFRAME WE WILL SELECT A SINGLE COLUMN BY USING
   THE SUBSCRIPT OPERATOR THEN SELECTING A COLOUMN...'''

print(df['Height'].mean()) # SINCE HEIGHT IS A NUMERIC VALUE SO WE DON'T HAVE TO PASS NUMERIC_ONLY KEYWORD ARGUMENT...
print('-----------------------------')
print(df['Weight'].sum()) # SINCE HEIGHT IS A NUMERIC VALUE SO WE DON'T HAVE TO PASS NUMERIC_ONLY KEYWORD ARGUMENT...
print('------------------------------') 
print(df['Height'].min()) # SINCE HEIGHT IS A NUMERIC VALUE SO WE DON'T HAVE TO PASS NUMERIC_ONLY KEYWORD ARGUMENT...
print('------------------------------') 
print(df['Legendary'].max()) # SINCE HEIGHT IS A NUMERIC VALUE SO WE DON'T HAVE TO PASS NUMERIC_ONLY KEYWORD ARGUMENT...
print('------------------------------') 
print(df['Type2'].count())
print('------------------------------') 




