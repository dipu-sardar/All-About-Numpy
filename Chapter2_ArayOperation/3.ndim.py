#number of dimension 

import numpy as np

arr_1d = np.array([1,2,3])
arr_2d = np.array([[1,2,3],
                   [4,5,6]])
arr_3d = np.array([[[1,2],[3,4],[5,6],[7,8]]])

print(arr_1d.ndim) #এটা হচ্ছে 1d array
print(arr_2d.ndim) #এটা হচ্ছে 2d array
print(arr_3d.ndim) #এটা হচ্ছে 3d array



