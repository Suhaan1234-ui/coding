#broadcasting is a powerful mechanism in NumPy that allows operations to be performed on arrays of different shapes and sizes without the need for explicit loops. It enables element-wise operations to be applied to arrays of different dimensions, making code more concise and efficient.
#it allows numpy to perform operations on arrays of different shapes and sizes by automatically broadcasting the smaller array to match the shape of the larger array. This is done by following a set of rules that determine how the arrays are aligned and how the operations are performed.
#the rules of broadcasting are as follows:  
#1. If the arrays have different numbers of dimensions, the shape of the smaller array is padded with ones on the left side until both shapes have the same number of dimensions.
#2. If the shapes of the arrays do not match in any dimension, the array with a shape of 1 in that dimension is stretched to match the shape of the other array.
#3. If the shapes of the arrays match in all dimensions, the arrays are compatible for broadcasting and the operation can be performed element-wise.
#4. If the shapes of the arrays do not match and cannot be broadcasted, a   ValueError is raised.
#so basicaly we go from right to left and check if the dimensions are same or if one of them is 1 , if yes they aare compatible adn we can broadcast the two arrays together, if not we raise an error.
import numpy as np
myarr1=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])   
myarr2=np.array([[1,2,3]]) 
print(myarr1.shape)
print(myarr2.shape)
print(myarr1+myarr2) # this will add the corresponding elements of the two arrays, which will give an array where each row of the first array is added to the corresponding element of the second array since the second array has a shape of (1, 3) and is broadcasted to match the shape of the first array.
#Broadcasting is a powerful feature in NumPy that allows arrays of different shapes to be combined in arithmetic operations without explicitly reshaping them. Instead of manually repeating or resizing arrays, NumPy automatically "stretches" the smaller array across the larger one when possible.