import pandas as pd
calories={"day1":420,"day2":380,"day3":390}
myvar=pd.Series(calories)
print(myvar.loc["day2"]) # this will print the value at index "day2" which is 380
print(myvar.loc["day1":"day3"]) # this will print the values from index "day1" to index "day3" which are 420, 380, and 390. The loc function is used to access a group of rows and columns by labels or a boolean array. In this case, we are using it to access a range of indices from "day1" to "day3".
print(myvar[0:2]) # this will print the first two values of the series, which are 420 and 380. The index selection 0:2 means that we are selecting the first two indices of the series, which correspond to "day1" and "day2". The index selection is based on the position of the indices in the series, rather than their labels.'
print(myvar[myvar>380]) # this will print the values that are greater than 380, which are 420 and 390. The condition myvar>380 creates a boolean series that indicates which values in the original series satisfy the condition, and then we use this boolean series to filter the original series and return only the values that satisfy the condition.