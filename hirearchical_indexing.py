import pandas as pd
import numpy as np

data = pd.Series(np.random.randn(10),
                 index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                        [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data)
# The “gaps” in the index display mean
# “use the label directly above”
print(data['b'])
print(data['b':'c'])
print(data.ix[['b', 'd']])
print('Selection from inner level:')
print(data[:, 2])

# for re-arranging into data frame, use unstack() method
print('Using unstack for rearrangine df:')
print(data.unstack())  # series converted to dataframe
print('Inverse of unstack is stack():')
print(data.unstack().stack())


# With a DataFrame, either axis can
# have a hierarchical index:
print("With a DataFrame, either axis can have a hierarchical index:")
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])
print(frame)
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print('Giving names to multi level(hirearchical) indexes:')
print(frame)
# With partial column indexing you can similarly select groups of columns:
print('partial column indexing:')
print(frame['Ohio'])


# The swaplevel takes two level numbers or names and
# returns a new object with the levels
# interchanged(but the data is otherwise unaltered)
print('Using swaplevel method:')
print(frame.swaplevel('key1', 'key2'))


# sortlevel, on the other hand,
# sorts the data (stably) using only the
# values in a single level
print('Using sort_index/sortlevel method:')
# print(frame.sortlevel(1)) #deprecated
# print(frame.swaplevel(0, 1).sortlevel(0)) #sortlevel deprecated(but in book)
print(frame)
print(frame.sort_index(level=1))
print(frame.swaplevel(0, 1).sort_index(level=0))


# we can sum by level on either the rows or columns like so
print("we can sum by level on either the rows or columns like so:")
print(frame)
print(frame.sum(level='key2'))
print(frame.sum(level='color', axis=1))


# Using dataframe's columns
print("Using Dataframe columns:")
frame2 = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                       'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                       'd': [0, 1, 2, 0, 1, 2, 3]})
print(frame2)
# using set_index method
print("DataFrame’s set_index function will create a new DataFrame using one or more of its\
      columns as the index:")
print(frame2.set_index(['c', 'd']))

# By default the columns are removed from the DataFrame,
# though you can leave them in
print(frame2.set_index(['c', 'd'], drop=False))

# reset_index, on the other hand, does the opposite of
# set_index; the hierarchical index
# levels are are moved into the columns:
print(frame2.set_index(['c', 'd']).reset_index())
