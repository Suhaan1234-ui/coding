#random number

import numpy as np
rng=np.random.default_rng(seed=1) # this will create a random number generator object that we can use to generate random numbers
print(rng.integers(1,100,size=(5,2)))
#we can set a seed to get the same result 
np.random.seed(seed=2)
print(np.random.uniform(1,2,3))#gives floating point integer\
#to get random values remove the seed