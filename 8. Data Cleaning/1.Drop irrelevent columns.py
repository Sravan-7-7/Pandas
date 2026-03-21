# Data Cleaning = the process of fxing / removing:
#                 incomplete, incorrect, or irrelevent data.
#                 ~75% of work done witn pandas is data cleaning
                 
import pandas as pd

df = pd.read_csv('data.csv')

 # NOW LET'S SAY YOU WOULD LIKE TO DROP A COLUMN BECAUSE IT'S NOT RELEVENT..

df = df.drop(columns=['Legendary'])

print(df) # PRINT'S ALL DATAFRAME EXCEPT LEGENDARY...
print('-------------------------------------------')

# NOW LET'S SAY YOU DON'T NEED NUMBER'S...

df = df.drop(columns=['No'])
print(df)
print('--------------------------------------------')

# WE CAN DO ALTERNATIVE METHOD TO SAVE TIME...

df = df.drop(columns=['Legendary', 'No']) # YOU CAN ALSO WRITE BOTH COLUMNS...
print(df)
print('--------------------------------------')

