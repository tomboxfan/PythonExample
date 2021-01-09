def binary_search(original_list, target_number):

    index_left = 0
    index_right = len(original_list) - 1

    while index_left <= index_right:
        index_middle = (index_left + index_right) // 2
        if original_list[index_middle] == target_number:
            return index_middle
        elif target_number < original_list[index_middle]:
            index_right = index_middle - 1 # move index_right to the middle
        else:
            index_left = index_middle + 1 # move index_left to the middle

    # We cannot find it in the original_list
    return -1

original_list = [-2, 3, 4, 7, 8, 9, 11, 13]
assert binary_search(original_list, 11) == 6
assert binary_search(original_list, 13) == 7
assert binary_search(original_list, -2) == 0
assert binary_search(original_list, 8) == 4
assert binary_search(original_list, 6) == -1

original_list = [3]
assert binary_search(original_list, 6) == -1
assert binary_search(original_list, 2) == -1
assert binary_search(original_list, 3) == 0