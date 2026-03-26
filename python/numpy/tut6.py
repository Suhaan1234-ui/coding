import numpy as np
#element wise arithmetic
myarr1=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
myarr2=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(myarr1+myarr2) # this will add the corresponding elements of the two arrays
print(myarr1-myarr2) # this will subtract the corresponding elements of the two arrays, which will give an array of zeros since the two arrays are the same
print(myarr1*myarr2) # this will multiply the corresponding elements of the two arrays, which will give an array where each element is the square of the corresponding element in the original arrays
print(myarr1/myarr2) # this will divide the corresponding elements of the two arrays, which will give an array of ones since the two arrays are the same
print(myarr1%myarr2) # this will give the remainder when the corresponding elements of the two arrays are divided, which will give an array of zeros since the two arrays are the same              
print(myarr1**myarr2)#this will give the result of raising the corresponding elements of the first array to the power of the corresponding elements of the second array, which will give an array where each element is the cube of the corresponding element in the original arrays since each element is raised to the power of itself.
#for this to work the two arrays must have the same shape, otherwise we will get a ValueError. If the shapes of the arrays are different but compatible for broadcasting, then the smaller array will be broadcasted to match the shape of the larger array and the operation will be performed element-wise.