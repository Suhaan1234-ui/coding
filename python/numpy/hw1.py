import numpy as np
myarr=np.array([[["a", "b", "c"], ["d", "e", "f"] , ["g", "h", "i"]] ,
                [["j", "k", "l"], ["m", "n", "o"] , ["p", "q", "r"]],
                [["s", "t", "u"], ["v", "w", "x"] , ["y", "z", ""]]                                        
                                   ])
print(myarr.shape) 
word=myarr[0,0,0]+myarr[1,0,0]+myarr[2,0,0]
print(word) # this will print "ajs" which is the first element of each block in the array. We can access the elements of the array using indexing, where the first index is the block number, the second index is the row number, and the third index is the column number. In this case, we are accessing the first element of each block, which is "a", "j", and "s".