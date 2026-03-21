'''SERIES : a pandas 1-dimensional labeled array that can hold any data type...'''

import pandas as pd
data = [100, 102, 104]
series = pd.Series(data)
print(series)
print('------------------')

# changing the the data to decimals...
data = [100.1, 102.2, 104.3]
series = pd.Series(data)
print(series)
print('------------------')

# changing the data to strings...
data = ['A', 'B', 'C']
series = pd.Series(data)
print(series)
print('------------------')

# changing the data to boolean values...
data = [True, False, True]
series = pd.Series(data)
print(series)
print('------------------')

'''we can also set index, by passing a list, tuple, dictionary, a numpy array, or even an another series...'''

data = [100, 102, 104]
series = pd.Series(data, index=['a', 'b', 'c'])
print(series)
print('------------------')

'''if at any time you need to access a vlaue directly within a series, you'll take your series, access the "loc" property, loc means
location by label, but people just say loc...'''

# return the value where the label is 'a' or 'b' or 'c'...

data = [100, 102, 104]
series = pd.Series(data, index=['a', 'b', 'c'])
print(series.loc['a'])   # this will return the value of index 'a' which is 100
print(series.loc['b'])   # this will return the value of index 'b' which is 102
print(series.loc['c'])   # this will return the value of index 'c' which is 104
print('------------------')

# to change the value in data with loc property...
data = [100, 102, 104]
series = pd.Series(data, index=['a', 'b', 'c'])
series.loc['a'] = 200
series.loc['b'] = 202
series.loc['c'] = 204
print(series)
print('------------------')

# we can also access the value by using "iloc" property, iloc means location by integer position, but people just say iloc...
data = [100, 102, 104]
series = pd.Series(data, index=['a', 'b', 'c'])
print(series.iloc[0])   # this will return the value of index 'a' which is 100
print(series.iloc[1])   # this will return the value of index 'b' which
print(series.iloc[2])   # this will return the value of index 'c' which is 104
print('------------------')

# filter by values 

data = [100, 102, 104, 200, 202]
series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print(series[series >= 200])   # this will return the values which are above '200'...
print('------------------')
print(series[series < 200])    # this will return the values which are below '200'...

# let's use dictinary instead of python list...

'''by taking an example of to record how many calories we eat in a day, we can use a dictionary to record the calories for each meal...'''

calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}
series = pd.Series(calories)
print(series)
print('------------------')

# let's access loc property to find how many calories I've eaten per a certain day...

print(series.loc['Day 1'])   # this will return the value of index 'Day 1' which is 1750
print(series.loc['Day 2'])   # this will return the value of index 'Day 2' which is 2100
print(series.loc['Day 3'])   # this will return the value of index 'Day 3' which is 1700
print('------------------')

# let's change the value of calories for a certain day..

series.loc['Day 3'] += 500
print(series.loc['Day 3'])   # this will return the value of index 'Day 3' which is 2200
print('------------------')
print(series)
print('------------------')

# filter by values...

print(series[series >= 2000])   # this will return the values which are above '2000'...
print('------------------')
print(series[series < 2000])    # this will return the values which are below '2000'...
