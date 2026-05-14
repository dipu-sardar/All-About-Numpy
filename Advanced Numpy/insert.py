"""
এটা দিয়া কোনও একটা array এর মধ্যে নতুন ভ্যালু দেয়, 
np.insert(array, idex, value, axis=Nome)

array - original array 
indec
value 
asix
axis = 0   row-wie 
axis = 1   column-wise
"""
import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

dipu = np.insert(numbers, 1,  99, axis= 0 )

print(dipu)




