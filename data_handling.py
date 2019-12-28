import pandas as pd
import numpy as np

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print(string_data)
print(string_data.isnull())

# The built-in Python None value is also
#  treated as NA in object arrays
string_data[0] = None
print(string_data.isnull())

# filtering out missing data
print('Filtering out missing data(dropna):')
d = pd.Series([1, np.nan, 3.5, np.nan, 7])
print(d.dropna())
print(d[d.notnull()])  # alternative


# for dataframes, dropna  by default drops
# any row containing a missing value
print('Dropna on dataframe:')
df = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan],
                   [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
print(df.dropna())
print('Dropping only rows that are all NA:')
print(df.dropna(how='all'))

# Dropping columns in the same way is only a
#  matter of passing axis=1:
print('Dropping columns that are all NA')
df[4] = np.nan
print(df)
print(df.dropna(axis=1, how='all'))


# you want to keep only rows containing a certain number
#  of observations. You can
# indicate this with the thresh argument:
print('Threshing data frame"')
df2 = pd.DataFrame(np.random.randn(7, 3))
df2.ix[:4, 1] = np.nan
df2.ix[:2, 2] = np.nan
print(df2)
print(df2.dropna(thresh=3))


# Filling in missing data
print("Filling in missing data: fillna")
print(df2.fillna(0))
print("Filling in missing data:fillna=> passing dict")
# Calling fillna with a dict you can use a different
# fill value for each column
print(df2.fillna({1: 0.5, 2: -1}))
# modify existing dataframe
print('Inplace fillna:')
df2.fillna(0, inplace=True)
print(df2)


# using filling methods:
# same interpolation methods available for reindexing
# can be used with fillna:

df3 = pd.DataFrame(np.random.randn(6, 3))
df3.ix[:2, 1] = np.nan
df3.ix[4:, 2] = np.nan
print('Using filling methods with fillna:')
print(df3)
print(df3.fillna(method='ffill'))
print('fillna with method & limit:')
print(df.fillna(method='ffill', limit=2))


# little creativity
print('Little creativity:')
un_cleaned = pd.Series([1., np.nan, 3.5, np.nan, 7])
print(un_cleaned.fillna(un_cleaned.mean()))
# limit For forward and backward filling,
#  maximum number of consecutive periods to fill
