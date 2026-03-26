#create a multiplication table till 10 using numpy
import numpy as np
myarr1=np.arange(1,11) # this will create an array of numbers from 1 to 10
myarr2=np.arange(1,11) # this will create another array of numbers from 1 to 10
myarr1=myarr1.reshape(10,1) # this will reshape the first array into a column vector with 10 rows and 1 column
myarr2=myarr2.reshape(1,10) # this will reshape the second array into a row vector with 1 row and 10 columns
multiplication_table=myarr1*myarr2 # this will perform element-wise multiplication between the two arrays, which will give us a multiplication table of size 10x10
print(multiplication_table) # this will print the multiplication table