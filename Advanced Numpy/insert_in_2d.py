import numpy as np

numbers = np.array([[10, 20, 30, 40, 50, 60, 70, 80, 90],[1,2,3,4,5,6,7,8,9]])

print(numbers)
print()

dipu = np.insert(numbers, 3,[77, 78, ], axis=1)

print(dipu)




