#shuffling an array and gettinga  random number
import numpy as np

arr=np.arange(1,6)
print(arr.ndim)
rng=np.random.default_rng() 
rng.shuffle(arr) # this will shuffle the elements of the array in place, meaning that the original array will be modified and the elements will be rearranged in a random order. The shuffle() function does not return a new array, it modifies the original array directly.
print(arr)
print(rng.choice(arr,2)) # this will return a random element from the array, which is a single value that is randomly selected from the array. The choice() function does not modify the original array, it simply returns a random element from it.