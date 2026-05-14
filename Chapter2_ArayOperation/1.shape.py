#কিভাবে দেখব array এর size, shape এবং type কেমন। এটা তো খুবই ইম্পর্টান্ট array সম্পর্কে আগে জানা, তারপরে সেটা নিয়ে কাজ করা

import numpy as np 

arr_2d = np.array([[1,2,3], 
                  [4,5,6],
                  [3,4,2],
                  [3,5,1],
                  [2,5,7]])

print(arr_2d.shape) #এটা দিয়ে check করা যায় যে, আমার array টায় কতগুলো row আর column আছে



