import pandas as pd
import numpy as np
obj = pd.Series(range(4), index=['d', 'a', 'b', 'c'])

# sorting series
print(obj.sort_index())

# With a DataFrame, you can sort by index on either axis
frame = pd.DataFrame(np.arange(8).reshape((2, 4)), index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])
print(frame)
print(frame.sort_index())  # sort row
print(frame.sort_index(axis=1))  # sort columns
print(frame.sort_index(axis=1, ascending=False))  # sort columns, descending


# sorting series by value
print("sorting series by value")
ob = pd.Series([4, np.nan, 7, np.nan, -3, 2])
print(ob.sort_values())


# On DataFrame, you may want to sort by the values in one or
# more columns. To do so, pass one or more column
# names to the by option:
print('Sorting dataframes by values in columns:')
frame2 = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame2)
print(frame2.sort_index(by='b'))
print(frame2.sort_index(by=['a', 'b']))  # by values in multiple columns


# ranking
print('Ranking....')
r = pd.Series([7, -5, 7, 4, 2, 0, 4]) #Equal values are assigned a rank that 
print(r.rank())                         # is the average of the ranks of those
                                      # values, rank of 7 at 2nd index = 6
                                      #and rank of 7 at i0th index = 7
                                      # 6+7/2 = 6.5


#Ranks can also be assigned according to the order
#  they’re observed in the data
print('Rank with tie function:first')
print(r.rank(method = 'first'))
# you can rank in descending order, too
print('Rank with tie function: max and in descending order')
print(r.rank(ascending=False, method='max'))


#dataframe ranking
print("Dataframe ranking:")
frame3 = pd.DataFrame({'b': [4.3, 7, -3, 2], 'a': [0, 1, 0, 1], \
            'c': [-2, 5, 8, -2.5]})
print(frame3)
print(frame3.rank()) #across rows(downwards)
print(frame3.rank(axis = 1)) #across colums(forwards)
