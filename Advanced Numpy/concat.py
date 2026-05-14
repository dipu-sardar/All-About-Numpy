"""
যদি ২ তা এরে জোর লাগাতে হয় 
np.concatenate((array1, array2,), axis = 0)

axix = 0  --- vartical stacking 
axis =1    --- horizontally staking
"""

import numpy as np 

array1 = np.array([1,2,3,4])
array2 = np.array([5,6,7,8])

new_array = np.concatenate((array1,array2), axis = 0)

print(new_array)


