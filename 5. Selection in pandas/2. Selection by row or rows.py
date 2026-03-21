'''                              SELECTION BY ROW OR ROWS                        '''



'''NOTE: We can access loc property,then pass in a label.So since i didm't set a label
         for each of these rows, zero would correspond with the first row where we have
         bulvasaur, but optinally what you could do, I can set one of the coloumns to serve
         as the index so that you can access ont of the name by label using the loc property.
         You probanly not going to remenber which pokemon is 145, but yoy'll remenber by
         it's name, so it's easier to look up. So what could you do is that when we read
         our CSV file, we can pass our second argumen, a keyword argument index like given below'''

 #                df = pd.read_csv('data.csv',index_col='Name')


import pandas as pd

df = pd.read_csv('data.csv', index_col='Name')

print(df.loc['Pikachu']) 
print('-------------------------------')
# let's find charizard...

print(df.loc['Charizard'])
print('----------------------------------')

'''if you don't want all the data dispalying on you row when locating by label, we can pass 
   a second argument we could pass in a python list of all the coloumns we would like to select
   so with charizard i would just like the height and weight '''

print(df.loc['Charizard', ['Height', 'Weight']])
print('--------------------------------------------')

'''So we will pass in a python list as the second argument that contains the coloumn we
   would like to display'''

# now also you can select a range of rows as well. for that we going to use slice operator which is a colon

print(df.loc['Charizard': 'Blastoise', ['Height', 'Weight']])

# you can also use iloc property...

print(df.iloc[0:11]) # you can also step of two
print('-------------------------------------------')
print(df.iloc[0:11:2])
print('-------------------------------------------')
'''As a second argument you can select ihe indicies of which coloumn you would like... '''

print(df.iloc[0:11:2, 0:3])