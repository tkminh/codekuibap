import numpy as np
import pandas as pd
from pandas.io.pytables import HDFStore

# series
# s = pd.Series([12, -4, 7, 9])
# print(s.values)
# print(s[3])
# print(s[0:2])

# arr = np.array([1,2,3,4])
# s3 = pd.Series(arr)
# print(s3)

# # filter
# print(s3[s3>2])

# # +-x/
# print(s3/2)

# s2 = pd.Series([1, -7, -4, -4, 7, 9])
# print(s2.unique())
# print(s2.value_counts())
# print(s2.isin([7, 9, 3, 1]))
# print(s2[s2.isin([7, 9, 3, 1])])

# # NAN , isnull, notnull
# s4 = pd.Series([5, -3, pd.NaT, 14])
# print(s4)

# # dictionary
# mydict = {'red': 100,'blue': 20, 'black': 50}
# s5 = pd.Series(mydict)
# print(s5)

# color = ['red', 'blue', 'black', 'green']
# s6 = pd.Series(mydict, color)
# print(s6)
# print(s6[s6.isnull()])


# print(s5+ s6)


# dataframe

data = {
    'color': ['blue', 'red', 'yellow'],
    'object':['ball', 'pencil', 'car'],
    'price':[1.5, 2.3, 4.9]
}

frame = pd.DataFrame(data)
print(frame)

frame2 = pd.DataFrame(data,columns=['object', 'color'])
print(frame2)

# print(frame + frame2)


# print(frame.columns)
# print(frame.values)
# print(frame.index)
# print(frame['color'])
# print(frame.color)
# print(frame.color[1])
# print(frame.loc[2])

# print(frame.loc[[0,2,1]])
print(frame[0:1])
print(np.random.random(4))
frame['newcol']= np.arange(0,3)
print(frame)

print(frame.T)

frame2 = pd.DataFrame(np.arange(16).reshape((4,4)),
    index=['red','blue','yellow','white'],
    columns=['ball','pen','pencil','paper'])
print(frame2)
print(frame2.apply(lambda x: x.max() - x.min()))
print(frame2.apply(lambda x: x.max() - x.min(), axis=1))