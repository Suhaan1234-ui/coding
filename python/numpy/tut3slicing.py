import numpy as np
myarr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
#myarr[index:index:step] is used to slice the array and print rows in 2d array
print(myarr[0:4:2]) # this will print the first and third row of the array, which are [1.2, 3] and [7, 8, 9]. The step of 2 means that we are skipping every other row in the array. If we had used a step of 1, it would have printed all the rows in the array.
print(myarr[-1])
print(myarr[-1][0]) # this will print the first element of the last row of the array, which is 10. The index -1 is used to access the last row of the array, and the index 0 is used to access the first element of that row.
print(myarr[::-2])
#this is only for row selection, if we want to select columns we can use myarr[:,index:index:step]
print(myarr[:,0])#: selects all the rows and 0 gives the first column
print(myarr[:,-2])
#myarr[rowselection, columnselection]
print(myarr[0:2,0:2]) # this will print the first two rows and the first two columns of the array, which are [[1, 2], [4, 5]]. The row selection 0:2 means that we are selecting the first two rows of the array, and the column selection 0:2 means that we are selecting the first two columns of the array.