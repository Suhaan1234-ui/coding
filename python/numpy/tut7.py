#comparison arithmetic 
import numpy as np
score=np.array([1,5,10,7,9])
print(score==9) #returns a boolean array 
print(score>5)
score[score>5]=0
print(score)