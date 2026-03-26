# How we can inport CSV (Common-seperated value)

'''NOTE : You need some data to work with.For demonstration we need a CSV File and a JSOM 
           File.For this demonstration you need some data to work with it '''

import pandas as pd

df = pd.read_csv('data.csv')
print(df) # it only prints 1st 5 rows and last 5 rows and rest all are truncated
print('----------------------------------')

''' if you want to print all the rows and not a truncated version following our dataframe 
    we will call the to_string function '''

print(df.to_string()) # be careful when working with a very large file
