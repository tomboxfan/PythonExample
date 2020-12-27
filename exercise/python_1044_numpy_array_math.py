import numpy as np

array1 = np.array([i * 10 for i in range(1,6)])
print(array1) # [10 20 30 40 50]

array2 = np.arange(5)
print(array2) # [0 1 2 3 4]

array3 = array1 + array2
print(array3) # [10 21 32 43 54]

print(f"array1 shape - {array1.shape}") # (5,)
print(f"array2 shape - {array2.shape}") # (5,)
print(f"array3 shape - {array3.shape}") # (5,)

# array1 and array4 shape are different
# ValueError: operands could not be broadcast together with shapes (5,) (4,)
# array4 = np.array([1,2,3,4])
# array5 = array1 + array4

array6 = array1 * 2
print(array6) # [20 40 60 80 100]

array7 = np.power(array2, 3)
print(array7) # [0 1 8 27 64]

array8 = array1 >= 30
print(array8) # [False False  True  True  True]

# 2 dimensional array
two_dimensional_array1 = np.array([[3, 2], [0, 1]])
print(two_dimensional_array1)
'''
[[3 2]
 [0 1]]
'''

two_dimensional_array2 = np.array([[3, 1], [2, 1]])
print(two_dimensional_array2)
'''
[[3 1]
 [2 1]]
'''

two_dimensional_array3 = two_dimensional_array1 + two_dimensional_array2
print(two_dimensional_array3)
'''
[[6 3]
 [2 2]]
'''