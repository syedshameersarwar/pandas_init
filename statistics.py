import pandas as pd
import numpy as np
from pandas_datareader import data as web

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
print(df)
print('Summing:')
print(df.sum())  # column wise sum
print(df.sum(axis=1))  # row wise sum,in book if all values in
# row/columns are NaN
# then result of operation will contain NaN
# but in this code, pandas are giving 0
# instead of NaN
print('Keeping NaN values:')
print(df.mean(axis=1, skipna=False))  # keeping NaN values

# idxmin and idxmax, return indirect statistics like the index value
# where the minimum or maximum values are attained:
print(" idxmin and idxmax, return indirect statistics like the index value \
      where the minimum or maximum values are attained: ")
print(df.idxmax())
print(df.idxmin())


# accumulations
print("Cumulative sums:")
print(df.cumsum())


# neither reduction nor accumulation
print('neither reduction nor accumulation: describe')
print(df.describe())  # column wise statistics

print('describe on series:')
obj = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(obj.describe())


'''
Table 5-10. Descriptive and summary statistics
Method Description
count Number of non-NA values
describe Compute set of summary statistics for Series or each DataFrame column
min, max Compute minimum and maximum values
argmin, argmax Compute index locations (integers) at which minimum or maximum value obtained, respectively
idxmin, idxmax Compute index values at which minimum or maximum value obtained, respectively
quantile Compute sample quantile ranging from 0 to 1
sum Sum of values
mean Mean of values
median Arithmetic median (50% quantile) of values
mad Mean absolute deviation from mean value
var Sample variance of values
std Sample standard deviation of values
skew Sample skewness (3rd moment) of values
kurt Sample kurtosis (4th moment) of values
cumsum Cumulative sum of values
cummin, cummax Cumulative minimum or maximum of values, respectively
cumprod Cumulative product of values
diff Compute 1st arithmetic difference (useful for time series)
pct_change Compute percent changes
'''


# read world scenario
print("DataFrames of stock prices and volumes obtained from \
      Yahoo! Finance")
all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')
price = pd.DataFrame({tic: data['Adj Close']
                      for tic, data in all_data.items()})
volume = pd.DataFrame({tic: data['Volume']
                       for tic, data in all_data.items()})

print('Price:')
print(price)
print('Volume:')
print(volume)
print('Percent changes of price')
print(price.pct_change().tail())  # tail return last row from array of elements


# The corr method of Series computes the correlation of the overlapping, non-NA,
# aligned-by-index values in two Series. Relatedly, cov computes the covariance:
print('Series corr method:')
print(price.pct_change().MSFT.corr(price.pct_change().IBM))
print('Series cov method:')
print(price.pct_change().MSFT.cov(price.pct_change().IBM))

print('Dataframe corr and cov method:')
print('corr')
print(price.pct_change().corr())
print('cov')
print(price.pct_change().cov())


'''
Using DataFrame’s corrwith method, you can compute pairwise correlations between
a DataFrame’s columns or rows with another Series or DataFrame. Passing a Series
returns a Series with the correlation value computed for each column
'''
print('Using dataframe corrwith method(passing series):')
print(price.pct_change().corrwith(price.pct_change().IBM))
print('Using dataframe corrwith method(passing dataframe):')
print(price.pct_change().corrwith(volume))


# unique values, value counts and membership
print("unique values, value counts and membership")
series = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
print(series.unique())  # not necessarily in sorted order

print('calculating frequencies:')
print(series.value_counts())  # frequencies, descending order
# value_count is also provided with top level pandas library
# pd.value_counts()

# vectorized set membership
print("vectorized set membership")
mask = series.isin(['b', 'a'])
print(mask)
print(series[mask])


# you may want to compute a histogram on multiple related columns in
# a DataFrame
print('Computing Histogram:')
data = pd. DataFrame({'Qu1': [1, 3, 4, 3, 4],
                      'Qu2': [2, 3, 1, 2, 3],
                      'Qu3': [1, 5, 2, 4, 4]})
print(data)
print(data.apply(pd.value_counts).fillna(0))  # histogram
