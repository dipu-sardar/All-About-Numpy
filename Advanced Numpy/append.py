"""
এটা দিলে শেষ এ এলিমেন্ট অ্যাড হবে। সিনটেক্স insert  এর মতোই।
"""

import numpy as np 

numbers = np.array([10,20,30])
marks = np.append(numbers, [40,50,60])

print(marks)

