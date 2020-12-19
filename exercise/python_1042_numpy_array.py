'''
Numpy is the core library for scientific computing in Python.
'''

'''
what is array?
Array is very similar to list. An array is almost a list.

What is the difference between array and list?
1) array is fixed size.
   list is not fixed size.
   
2) array is homogeneous (array can only put 1 type of value)
   list is heterogeneous (list can be mixed type of value)
   
3) array is much / much faster than list and save space in memory      
'''

import numpy as np

# definition - you pass in a list [1,2,3] to np.array() function
# np.array([1,2,3]) will give you an array
array_1 = np.array([1,2,3])

# read the array
print(array_1)    # [1 2 3]
print(array_1[1]) # 2

# write the array
array_1[1] = 4
print(array_1)    # [1 4 3]

# You can only put int value into array_1
# ValueError: invalid literal for int() with base 10: 'Tom'
# array_1[1] = 'Tom'

# You can use list comprehension in array definition
# Revise 1005 if you can't remember list comprehension
array_2 = np.array([i for i in range(20)])
print(array_2) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]


# You can use list slice in array as well
# Revise indexing_and_slicing_example.py if you can't remember list slicing
array_3 = array_2[::-1]
print(array_3) # [19 18 17 16 15 14 13 12 11 10  9  8  7  6  5  4  3  2  1  0]

array_4 = array_2[2:16:2]
print(array_4) # [ 2  4  6  8 10 12 14]