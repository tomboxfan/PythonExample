'''
Given an list of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

# solution 1 brute force
def two_sum(nums, target):
    pass

result = two_sum([2,7,11,15], 9)
print(result) # [0, 1]

result = two_sum([3,2,4], 6)
print(result) # [1, 2]

result = two_sum([3,3], 6)
print(result) # [0, 1]
