#vectorized maths fn
import numpy as np
myarr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(np.sqrt(myarr)) # this will print the square root of each element in the array    
print(np.exp(myarr)) # this will print the exponential of each element in the array, which is e raised to the power of each element   
myarr2=np.array([1.67, 2.34, 3.45, 4.56])
print(np.round(myarr2)) # this will round each element in the array to the nearest
print(np.floor(myarr2)) # this will round each element in the array down to the nearest integer, which is the largest integer that is less than or equal to each element
print(np.ceil(myarr2)) # this will round each element in the array up to the nearest integer, which is the smallest integer that is greater than or equal to each element