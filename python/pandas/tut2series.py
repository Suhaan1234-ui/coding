import pandas as pd
data = [1, 2, 3, 4, 5]
myseries=pd.Series(data)
print(myseries)
myseries2=pd.Series(data,index=['a','b','c','d','e']) #Series is a constructor
print(myseries2)
#to access a value from a sereis we use loc and iloc , and index
print(myseries2.loc['c']) # this will print the value at index 'c'
print(myseries2.iloc[2]) # this will print the value at index 2, which is the same as index 'c'
print(myseries2[myseries2>3]) # this will print the values that are greater than 3, which are 4 and 5. The condition myseries2>3 creates a boolean series that indicates which values in the original series satisfy the condition, and then we use this boolean series to filter the original series and return only the values that satisfy the condition.