import pandas as pd
import numpy as np

# 1)dict of lists
data = {'state': ["Karachi", "Lahore", "Islamabad"], 'year': [2000, 2004, 2002],
        'population': [200000, 50000, 10000]}
frame = pd.DataFrame(data)
print(frame)

# custom columns order
frame2 = pd.DataFrame(data, columns=['population', 'state', 'year'])
print(frame2)

# passing column explicitly that is not present is data dict
frame2 = pd.DataFrame(data, columns=['population', 'state', 'year', 'debt'],
                      index=['one', 'two', 'three'])
print(frame2)
print(frame2.columns)

# retrieiving columns
print(frame2.state)
print(frame2['year'])

# retrieving rows
print(frame2.loc['three'])


# assigning columns
frame2['debt'] = 75.5
print(frame2)  # changed all values in debt column to 75.5
frame2['debt'] = np.arange(3.)
print(frame2)
frame2['debt'] = pd.Series([1.5, 7.5, 4.5, 7.3], index=[
                           'two', 'three', 'four', 'one'])
print(frame2)

# assignment to non-existant columns result in creation of that column
frame2['north'] = frame2.state == 'Islamabad'
print(frame2)  # column north is created with boolean indicator if state
# is Islamabad or not


# deleting column
del frame2['north']
print(frame2)


# 2) from dicts of dicts
population = {'Nevada': {2001: 2.4, 2002: 2.9},
              'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(population)
print(frame3)
print(frame3.T)  # frame transpose

# explicit indexing
frame4 = pd.DataFrame(population, index=[2001, 2002, 2003])
print('Explicit indexing: ')
print(frame4)


# 3) Dict of series
dict_series = {'Nevada': frame3['Nevada'][:2], 'Ohio': frame3['Ohio'][:-1]}

frame5 = pd.DataFrame(dict_series)
print('From dict of series: ')
print(frame5)

# setting names of columns and rows indexes
frame5.index.name = 'year'
frame5.columns.name = 'states'
print('With names of index and columns')
print(frame5)

# printing out frame values
print(frame3.values)
print(frame3.values.dtype)

print(frame2.values)
print(frame2.values.dtype)
