"""
np.delete(array, index, axis = none)

"""

import numpy as np 

numbers = np.array([1,2,3,4,5,6,7,8,9])

new_array = np.delete(numbers, 2, axis=0 )
print(new_array)