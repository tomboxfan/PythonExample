'''
Given an list of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

# solution 1 brute force
def two_sum_solution1_brute_force(numbers, target):

    #Shortcut key - rename - Shift + F6

    # we knowthere are 2 numbers, added together, their result is target
    # Let's try one by one, start from index 0, till the last one
    # time complexity - O(n^2)
    for number_with_big_index in range(len(numbers)):

        # Then let's try all numbers whose index is smaller than number_with_big_index
        for number_with_small_index in range(number_with_big_index):

            if numbers[number_with_small_index] + numbers[number_with_big_index] == target:
                return [number_with_small_index, number_with_big_index]


def two_sum_solution2_dict(numbers, target):

    # convert list to dict - value:index map
    # For example:

    # [2,7,11,15] is converted to {2:0, 7:1, 11:2, 15:3}
    # [3,2,4]     is converted to {3:0, 2:1, 4:2}
    number_index_dict = {}
    index = 0
    for i in numbers:
        number_index_dict[i] = index
        index += 1


    index = 0
    for i in numbers:
        if (target - i) in number_index_dict and index != number_index_dict[target-i]:
            return [index, number_index_dict[target - i]]
        index += 1





#
# result = two_sum_solution1_brute_force([2, 7, 11, 15], 9)
# print(result) # [0, 1]
#
# result = two_sum_solution1_brute_force([3, 2, 4], 6)
# print(result) # [1, 2]
#
# result = two_sum_solution1_brute_force([3, 3], 6)
# print(result) # [0, 1]

result = two_sum_solution2_dict([2, 7, 11, 15], 9)
print(result) # [0, 1]

result = two_sum_solution2_dict([3, 2, 4], 6)
print(result) # [1, 2]

result = two_sum_solution2_dict([3, 3], 6)
print(result) # [0, 1]
