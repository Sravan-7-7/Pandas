'''AGGREGATION FUNCTION : Redices a set of values into a single summary value used to summarize
                          and analyze data often used with the groupby() function...'''

import pandas as pd

df = pd.read_csv('data.csv')

'''NOTE: In this demonstration i have a dataframe that contains original 150 pokemons.Let's say
         for some of these columns such as the numbers, the Height, the Weight, and a Legendary
         status, I would like to find the mean or the average. To find the mean for all numerical
         columns we could the following...'''

'''WE CANNOT USE THE MEAN FUNCTION ON ANY COLUMNS THAT ARE NON-NUMERIC. WE CAN'T FIND THE MEAN 
   FOR ANYTHING THAT'S NON-NUMERIC SUCH AS POKEMON NAMES'''

'''SO WE CAN USE NUMERIC_ONLY == TRUE, WE ARE TELLING PANDAS FIND THE MEAN OF ANY COLUMN THAT ARE NUMERIC'''

# finding the mean of all numeric cclumns....

print(df.mean(numeric_only=True))
print('-----------------------------')

# finding the sum all the numeric columns...

print(df.sum(numeric_only=True))
print('------------------------------') 

# finding the minimum of all numerical coloumns...

print(df.min(numeric_only=True))
print('------------------------------') 

# finding the maximunof all numerical coloumns...

print(df.max(numeric_only=True))
print('------------------------------') 


# finding the count of all numerical coloumns...

print(df.count())
print('------------------------------') 








 