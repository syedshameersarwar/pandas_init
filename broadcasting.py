import pandas as pd
import numpy as np

arr = np.arange(12.).reshape((3, 4))
print(arr)
print(arr[0])
print(arr-arr[0])  # row broadcasting, subtract 0th row from every row of arr

frame = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
series = frame.ix[0]
print(series)
print('Subtracting series from frame(row broadcasting default)')
print(frame-series)

# If an index value is not found in either the DataFrame’s
# columns or the Series’s index, the objects will be
# reindexed to form the union
s = pd.Series(range(3), index=list('bfe'))
print(frame)
print(s)
print(frame-s)
# default broadcasting is on row(row operations like matrix)

# to broadcast on columns(column operations like matrix)
# use arithmetic methods
print("broadcast on columns(column operations like matrix)")
col = frame['e']
print(frame.sub(col, axis=0))  # for matching on rows : axis = 0
