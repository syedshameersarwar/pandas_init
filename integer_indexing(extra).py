import pandas as pd
import numpy as np

ser = pd.Series(np.arange(3.))
# print(ser[-1]) #in_correct for integer index(integer labels)
print(ser[2])

# On the other hand, with a non-integer index,
# there is no potential for ambiguity:
ser2 = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
print(ser2[-1])

# To keep things consistent, if you have an axis
# index containing indexers, data selection
# with integers will always be label-oriented.
# This includes slicing with ix, too:
print(ser.ix[:1])

'''
In cases where you need reliable position-based indexing
 regardless of the index type, you can use the iget_value
 method from Series and irow and icol methods from DataFrame
'''
ser3 = pd.Series(range(3), index=[-5, 1, 3])
# print(ser3.iget_value(2)) #book: iget_value, but deprecated
print(ser3.iat[2])

frame = pd.DataFrame(np.arange(6).reshape(3, 2), index=[2, 0, 1])
print(frame)
# print(frame.irow(0)) used in book, deprecated
# print(frame.icol(0)) used in book, deprecated
print('using irow/iloc[i]')
print(frame.iloc[0])
print('using irow/iloc[:i]')
print(frame.iloc[:, 0])


'''
Panel Data
While not a major topic of this book, pandas has a Panel data structure, 
which you can think of as a three-dimensional analogue of DataFrame.


To create a Panel, you can use a dict of DataFrame objects or a three-dimensional
ndarray:
import pandas.io.data as web
pdata = pd.Panel(dict((stk, web.get_data_yahoo(stk, '1/1/2009', '6/1/2012'))
 for stk in ['AAPL', 'GOOG', 'MSFT', 'DELL']))

 Each item (the analogue of columns in a DataFrame) in the Panel is a DataFrame:

In [297]: pdata
Out[297]:
<class 'pandas.core.panel.Panel'>
Dimensions: 4 (items) x 861 (major) x 6 (minor)
Items: AAPL to MSFT
Major axis: 2009-01-02 00:00:00 to 2012-06-01 00:00:00
Minor axis: Open to Adj Close
In [298]: pdata = pdata.swapaxes('items', 'minor')
In [299]: pdata['Adj Close']
Out[299]:
<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 861 entries, 2009-01-02 00:00:00 to 2012-06-01 00:00:00
Data columns:
AAPL 861 non-null values
DELL 861 non-null values
GOOG 861 non-null values
MSFT 861 non-null values
dtypes: float64(4)



In [301]: pdata.ix['Adj Close', '5/22/2012':, :]
Out[301]:
            AAPL DELL GOOG MSFT
Date
2012-05-22 556.97 15.08 600.80 29.76
2012-05-23 570.56 12.49 609.46 29.11
2012-05-24 565.32 12.45 603.66 29.07
2012-05-25 562.29 12.46 591.53 29.06
2012-05-29 572.27 12.66 594.34 29.56
2012-05-30 579.17 12.56 588.23 29.34



An alternate way to represent panel data, especially for fitting statistical models, is in
“stacked” DataFrame form:
In [302]: stacked = pdata.ix[:, '5/30/2012':, :].to_frame() =>  organized

DataFrame has a related to_panel method, the inverse of to_frame:
stacked.to_panel()
'''
