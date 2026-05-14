import numpy as np  

numbers = np.array([1.2, 2.5, 3.8])

print(numbers)
print(numbers.dtype)

int_arr = numbers.astype(int)

print(int_arr)
print(int_arr.dtype)
