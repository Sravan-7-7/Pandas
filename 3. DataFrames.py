# DataFrame = A tabular data structure with rows and coloumns. (2 Dimensinal)
#              Similar to an Excel spreadsheet.

import pandas as pd

data = {'Name': ["spongebob", "patrick", "squidward"],
        'Age': [30,35,50]
        }

df = pd.DataFrame(data, index=[1, 2, 3])

# we can also add index to it to change the s.no of the dataframe...

print(df)
print('----------------------------')

# if you need to select a single row you can access the loc property...

print(df.loc[1]) # as all we know loc means location by label..
print('----------------------------')

# we can also select by integer location by using iloc property...

print(df.iloc[1])
print('----------------------------')

# we can also add a coloumn .... so let's add a new coloumn.

df['job'] = ['cook', 'N/A', 'cashier']
print(df)
print('----------------------------')

''' we can also add a new row, here's how you can add a new row an easy way to create a new row is to create a
    new dataframe, then concatenate it ... '''

new_row = pd.DataFrame([{'Name': 'sandy', 'Age': 28, "job": 'Engineer'}],
                       index=[4])

'''we have to concatenate it to our existing dataframe. we will reassign our dataframe'''

df = pd.concat([df, new_row,])

print(df)
print('----------------------------')

# also we can add multiple rows by adding more dictinaries.. let's see how to add mew rows..

new_rows = pd.DataFrame([{'Name': 'sandy', 'Age': 28, "job": 'Engineer'},
                         {'Name': 'Mr.Krabs', 'Age':'60' , "job": 'Manager'}],
                       index=[4, 5])
df = pd.concat([df, new_rows])

print(df)
print('-------------------------')