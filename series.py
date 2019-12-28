import pandas as pd
import numpy as np

series = pd.Series([75, -4, 32, 12])
print(series)
print(series.values, series.index)

custom_index_series = pd.Series([100, 50, 75, 50], index=[
                                "1st", "2nd", "3rd", "4th"])
print(custom_index_series)
print(custom_index_series.values, custom_index_series.index)

name_series = pd.Series([30, 40, 50], index=[
                        'a', 'b', 'c'], name="Series with name")
print(name_series.index)


canteen = pd.Series([20, 10, 5, 4, 5, 12, 10], index=['Mon', 'Tue', 'Wed',
                                                      'Thurs', 'Fri', 'Sat', 'Sun'], name="Canteen's week sandwiches sale")
print(canteen)
print(canteen.values, canteen.index)

# Accessing Series
print(canteen[0])  # 20
print(canteen['Sat'])  # 12, like dict access
# print(canteen['Sat', 'Sun'])  # error, incorrect multiple indexing
print(canteen[['Sat', 'Sun']])  # correct multiple indexing
print(canteen[[0, 1]])  # correct integer multiple indexing(mon,tues)

print(canteen[canteen >= 10])  # conditional indexing, return all values >= 10


# arithmetic on pandas series
print(canteen*2)  # multiply each value with 2 but does not mutate original series
print(canteen/2)  # dividing will result in float values, i.e dtype =float
canteen = canteen*2  # redefining original series
print(canteen)

print('Mon' in canteen)  # checking for index

# pandas Series data sources
# 1) from python list as argument, show above
# 2) from numpy arrays
val = np.array([1, 2, 3])
ind = np.array(['a', 'b', 'c'])
numpy_series = pd.Series(val, index=ind)
print('From numpy: ')
print(numpy_series)

# 3) from python dict
dic = {44: 'Shameer', 54: 'Kazim'}

dict_series = pd.Series(dic)
print('From python dict:')
print(dict_series)
# changing dict keys order manually
modified_dict_series = pd.Series(dic, index=[54, 44])  # persist values
print('With Modified index of:')
print(modified_dict_series)
dic2 = {'kar': 74200, 'lah': 74900}
dict_series2 = pd.Series(dic2)
print(dict_series2)
taxes = {'Ohio': 350000, 'Oregon': 16000, 'Texas': 71000, 'Utah': 5000}
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj = pd.Series(taxes, index=states)
print(obj)  # map values for states from taxes dict
# and place NaN where value is not found
# also converted to float, due to NaN maybe


# null functions
print(pd.isnull(obj))  # return true where value is NaN
print(pd.notnull(obj))  # return false where value is NaN
print(obj.isnull())  # return true where value is NaN(instance method)

# data alignment in arithmetic operations
obj1 = pd.Series(taxes)
obj2 = obj.copy()
print(obj1, obj2)
print('Adding series: '+str(obj1+obj2))  # data aligns automatically, values of
# Oregon state from both objects will be summed up to form a
# single value under Oregon key, keys that donot appear in both
# objects will result in NaN value

# name properties of series
obj.name = 'Taxes of US states'
obj.index.name = 'States'
print(obj)
print(obj[['Ohio','Texas']])
print(obj.index.name) # index name will only shown if explicitly call
                       #unlike series name which will be shown
                       # everytime after being set 


#inplace alteration using assignment
print(obj) #correct
obj.index = ['Ohio','Texas','California','Oregon'] #new index order
print('In place alteration: ') #will result in same value order 
print(obj)                     # but indexes from new index list
                              #i.e California was NaN before
                              # now its values os 16000.0
                              # as its on 2nd index on newly
                              # create index list, Similarly Ohio is Nan
                              # now


#mutating series
obj['Ohio'] = '750000'
print(obj)