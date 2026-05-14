#np.isinf(array)

import numpy as np

numbers = np.array([1,2,np.inf,4,-np.inf, 6])

print(np.isinf(numbers))

cleaned_arr = np.nan_to_num(numbers, posinf=1000, neginf=-1000)

print(cleaned_arr)



