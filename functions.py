import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])


def f(x): return x.max() - x.min()


print(frame.apply(f))  # apply in row direction(downwards)
print(frame.apply(f, axis=1))  # apply in column direction(forwards)
# axis 0 will preserve columns
# axis 1 will preserve rows


# The function passed to apply need not return a scalar value,
# it can also return a Series with multiple values:
def f2(x):
    return pd.Series([x.max(), x.min()], index=['max', 'min'])


print(frame.apply(f2))


# for applying function element wise
print("applying function element wise")


def format(x): return '%.2f' % x


print(frame.applymap(format))


# applying element wise function on series
print("applying element wise function on series")
print(frame['d'].map(format))
