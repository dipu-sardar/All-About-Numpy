"""
যেখানে যেখানে missing values পাবে সেখানে সেখানে গিয়ে সেট করা value দিয়ে রিপ্লেস করে দিবে সবগুলো, মনে যত গুলো মিসিং পাবে সবগুলো একটা স্পেসিফিক সেট করা নাম্বার দিয়ে পূরণ করে দিবে

"""

import numpy as np

arr = np.array( [1,2, np.nan, 4, np.nan, 61])
cleaned_arr = np.nan_to_num(arr, nan=100)

print (cleaned_arr)