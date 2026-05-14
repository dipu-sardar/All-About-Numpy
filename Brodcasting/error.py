import numpy as np 

array1 = np.array([[1,2,3],
                    [4,5,6]])

array2 = np.array([1,2])

Result = array1 + array2

print(Result)  #এখেনে প্রিন্ট হয় নি, কারণ হলো এখেনে shape  match করে নি। 

