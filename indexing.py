import pandas as pd
import numpy as np

series = pd.Series([2, 3, 4, 44], index=['a', 'b', 'c', 'd'])
print(series.index)

# series.index[1] = 'd' #mutating index object is not allowed

# defining index, useful for sharing across series and dataframes
index = pd.Index(np.arange(3))
obj2 = pd.Series([57, 75, 44], index=index)
print(obj2.index is index)

# type of indexes in pandas
# 1) index (general)
# 2) int64index
# 3) multi index(hirearchical)
# 4) datatimeindex (nanoseconds timestamps, numpy(datetime64))
# 5) periodIndex (specialized for period data(timespans))


population = {'Nevada': {2001: 2.4, 2002: 2.9},
              'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame = pd.DataFrame(population)
print(frame.index)
print('Ohio' in frame.columns)
print(2001 in frame.index)
f = frame.index.insert(2, 2004)
print(f, frame.index)

'''
Table 5-3. Index methods and properties
Method: Description
append: Concatenate with additional Index objects, producing a new Index
diff: Compute set difference as an Index
intersection: Compute set intersection
union: Compute set union
isin: Compute boolean array indicating whether each value is contained in the passed collection
delete: Compute new Index with element at index i deleted
drop: Compute new index by deleting passed values
insert: Compute new Index by inserting element at index i
is_monotonic: Returns True if each element is greater than or equal to the previous element
is_unique: Returns True if the Index has no duplicate values
unique: Compute the array of unique values in the Index
'''

# re-indexing
ob = pd.Series([4.5, 7.2, -5.3, 3.6], index=['a', 'b', 'c', 'd'])
print(ob)
obj2 = ob.reindex(['e', 'd', 'c', 'b', 'a'])
print(obj2)  # values remain consistent to their older indexes,
# placing NaN to newly introduced index element(e)

# re-indexing with fill_value
obj3 = ob.reindex(['e', 'd', 'c', 'b', 'a'], fill_value=0)
print('reindexing with fill:')
print(obj3)

# re-indexing with method parameter, (for interpolation)
colors = pd.Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print(colors)
print("interpolated_colors(forward):")
print(colors.reindex(range(6), method='ffill'))  # ffill or pad: fill
                                                #(or carry) values forward

print("interpolated_colors(backward):")
print(colors.reindex(range(6), method='bfill'))  # bfill or backfill Fill 
                                                #(or carry) values backward

frame2 = pd.DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                  columns=['Ohio', 'Texas', 'California'])
print(frame2)
#reindexing columns
states = ['Texas','Utah','California']
reindexed = frame2.reindex(columns = states)
print('Re-indexed columns: ')
print(reindexed)

hybrid_reindexing = frame2.reindex(
    index=['a', 'b', 'c', 'd'], columns= states).ffill()
print('Hybrid re-indexing(rows & cols simultaneously)')
print(hybrid_reindexing) #interpolation(ffill) only applies to row axis(0)

#re-indexing using loc method(in book: ix)
using_ix = frame2.loc[['a','b','c','d'], states]
print(using_ix)

# dropping (series)
s = pd.Series(np.arange(5), index = ['a','b','c','d','e'])
print(s)
new_obj = s.drop('c')
print("Deleted c")
print(new_obj)
#deleting multiple
multiple = s.drop(['c','d'])
print('Multiple deleting: ')
print(multiple)

#dropping (dataframes)

data = pd.DataFrame(np.arange(16).reshape((4, 4)), \
                 index=['Ohio', 'Colorado', 'Utah', 'New York'], \
                 columns=['one', 'two', 'three', 'four'])

print(data)
print('Dropping rows')
print(data.drop(['Colorado','Utah'])) #passing list only will result
                                    # in dropping of rows
print(data.drop('New York'))

print('Dropping columns')
print(data.drop(['three','four'], axis = 1)) #axis = 1 for deleting columns
print(data.drop('two', axis= 1))


#indexing, selection & filtering
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj[1], obj['b'])
print(obj[2:4])
print(obj[['c','d']]) #same as above
print(obj[[2,3]]) #same as above

print('Booelan selection:')
print(obj[obj < 2]) 


#Slicing with labels(inclusive)
print('Slicing with labels in pandas(inclusive)')
print(obj['b':'d']) #includes d
#assigning label slices
obj['b':'d'] = 75
print(obj)

print(data['two']) #select column two
print(data[['two','three']]) #select column two and three
print("selects all rows in which value at 3rd column is greated than 5:")
print(data[data['three']>5]) #selects all rows in which value 
                            #at 3rd column is greated than 5
print("selects first two rows")
print(data[:2]) #selects first two rows


#boolean dataframe
print('Boolean Dataframe:')
print(data<5)
data[data<5] = 0
print(data)

#using ix
print('Using ix:')
print(data.ix[['Colorado','Utah'],[3,0,1]])
print(data.ix[2])
print(data.ix[:'Utah','two'])
print(data.loc[:'Utah',['two','three']])
print(data.ix[data.three>5,:3]) #selects only those rows where values
                                # in 3rd col is greater than 5
                                # and among then list result with
                                #  first 3 columns(first,second, third)


#arithmetic and data alignment
print("arithmetic and data alignment")
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print('s1')
print(s1)
print('s2')
print(s2)
print('s1+s2')
print(s1+s2)

#In the case of DataFrame, 
# alignment is performed on both the rows and the columns:
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list('bcd'), \
                index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list('bde'), \
                index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print('df1')
print(df1)
print('df2')
print(df2)
print('adding df1+df2:')
print(df1+df2)

#using df.add method for filling
print("using df.add method for filling")
print(df1.add(df2, fill_value=0))
print(df1.add(df2, fill_value =0).fillna(0))



#non unique indexing
print("non unique indexing")
ununique = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(ununique)
print(ununique.index.is_unique)

#for dataframes
print("non unique indexing(data frames)")
df = pd.DataFrame(np.random.randn(4, 3), index=['a', 'a', 'b', 'b'])
print(df)
print(df.ix['b'])
