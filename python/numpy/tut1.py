import numpy as n 
print(n.__version__)
#python is slow so we use numpy to speed up the process of calculations.
#numpy is a library in python which is used for scientific computing and data analysis. It provides
# a powerful array object and a collection of functions for working with arrays. It is widely used in data science, machine learning, and scientific computing.
#numpy is built on top of C and Fortran, which makes it much faster than pure Python for numerical computations. It also provides a convenient way to work with large datasets and perform complex mathematical operations efficiently.
myarr=[1,2,3,4,5]
print(myarr*2) # this will not work as expected because it will concatenate the list instead of multiplying each element by 2.
myarr=n.array(myarr) # we convert the list to a numpy array, we use n to access the numpy library
print(myarr*2) # this will work as expected because it will multiply each element by 2. This is called broadcasting in numpy, which allows us to perform operations on arrays of different shapes and sizes.