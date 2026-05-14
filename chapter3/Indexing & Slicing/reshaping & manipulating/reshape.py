"""
if dimentions match, then you can do reshape

"""

import numpy as np

numbers = np.array([1,3,4,5,6,7,8,9,6,5,4,3])

reshape_array = numbers.reshape(4,3)

print(reshape_array)