import numpy as np
myarr=np.array([1,2,3,4,5])
print(myarr.ndim) # this will print the number of dimensions of the array, which is 1 in this case.
myarr=np.array([[1,2,3],
                [4,5,6]])
print(myarr.ndim) # this will print the number of dimensions of the array, which is 2 in this case.
myarr=np.array([[[1,2,3], [4,5,6]],
                [[7,8,9], [10,11,12]]])
print(myarr.ndim) # this will print the number of dimensions of the array, which is 3 in this case.
print(myarr.shape) # this will print the shape of the array, which is (2, 2, 3) in this case. The shape of an array is a tuple that gives the size of the array along each dimension. In this case, the array has 2 blocks, each block has 2 rows and 3 columns.