
import numpy as np

print('\n\n1 dimensional array ------------------------------------\n\n')

one_dimensional_array = np.arange(10)
print(f"one_dimensional_array is {one_dimensional_array}")

'''
1 dimensional array looks like a line.
[0 1 2 3 4 5 6 7 8 9]
'''

print(f"one_dimensional_array.shape is {one_dimensional_array.shape}") # (10,)
# There is no value after the comma, this is a one-dimensional array

#Access the array
print(f"one_dimensional_array[3] is {one_dimensional_array[3]}")

print('\n\n2 dimensional array ------------------------------------\n\n')


# definition:
# reshape(5,4) will convert the 1 dimensional array to 2 dimensional array - 5 rows / 4 columns
# What is a 2 dimensional array?
# 2 dimensional array is an array whose elements are 1 dimensional array.
two_dimensional_array = np.arange(20).reshape(5, 4)
print(f"two_dimensional_array is {two_dimensional_array}")

'''
2 dimensional array looks like a rectangle:

(5 rows * 4 columns)
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]]
'''

print(f"two_dimensional_array.shape is {two_dimensional_array.shape}") # (5, 4)

#Access the array
print(f"two_dimensional_array[3] is {two_dimensional_array[3]}") # [12 13 14 15]
print(f"two_dimensional_array[3][2] is {two_dimensional_array[3][2]}") # 14

print('\n\n3 dimensional array ------------------------------------\n\n')

# definition
# reshape(3,4,5) will convert a 1 dimensional array to 3 dimensional array - 3 layer / 4 rows / 5 columns
# What is a 3 dimensional array?
# 3 dimensional array is an array whose elements are 2 dimensional array.
three_dimensional_array = np.arange(60).reshape(3,4,5)
print(f"three_dimensional_array is {three_dimensional_array}")

'''
3 dimensional array looks like a cube:
[[[ 0  1  2  3  4]
  [ 5  6  7  8  9]
  [10 11 12 13 14]
  [15 16 17 18 19]]

 [[20 21 22 23 24]
  [25 26 27 28 29]
  [30 31 32 33 34]
  [35 36 37 38 39]]

 [[40 41 42 43 44]
  [45 46 47 48 49]
  [50 51 52 53 54]
  [55 56 57 58 59]]]
'''

#shape
print(f"three_dimensional_array.shape is {three_dimensional_array.shape}") #(3,4,5)

# Access the array
print(f"three_dimensional_array[2] is {three_dimensional_array[2]}")
'''
[[40 41 42 43 44]
  [45 46 47 48 49]
  [50 51 52 53 54]
  [55 56 57 58 59]]
'''

print(f"three_dimensional_array[2][2] is {three_dimensional_array[2][2]}")
'''
[50 51 52 53 54]
'''

print(f"three_dimensional_array[2][2][2] is {three_dimensional_array[2][2][2]}")
'''
52
'''