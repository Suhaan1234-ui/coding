#aggregate functions = functions that perform a calculation on a set of values and return a single value as a result. These functions are commonly used in data analysis and statistics to summarize and analyze data. Some examples of aggregate functions include:
import numpy as np
myarr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(np.sum(myarr)) # this will print the sum of all the elements in the array, which is 78
print(np.sum(myarr, axis=0)) # this will print the sum of each column in the array, which is [22, 26, 30]. The axis=0 means that we are summing along the columns of the array. If we had used axis=1, it would have summed along the rows of the array and given us [6, 15, 24, 33].
print(np.sum(myarr, axis=1)) # this will print the sum of each row      
print(np.mean(myarr)) # this will print the mean of all the elements in the array, which is 6.5
print(np.std(myarr)) # this will print the standard deviation of all the elements in the array, which is 3.452052529534663
print(np.var(myarr)) # this will print the variance of all the elements in the array
print(np.min(myarr)) # this will print the minimum value in the array, which is 1
print(np.max(myarr)) # this will print the maximum value in the array, which is 12
print(np.argmin(myarr)) # this will print the index of the minimum value in the array, which is 0 since the minimum value is 1 and it is located at index 0 in the flattened version of the array
print(np.argmax(myarr)) # this will print the index of the maximum value in the array   
# we can use axis in any of them fuctions