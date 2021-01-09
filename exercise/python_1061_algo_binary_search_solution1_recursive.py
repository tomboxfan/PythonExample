'''
What is binary search?
You have a SORTED list: [2,5,8,12,16,23,38,56,72,91]
You want to see whether 23 is in the list or not.(In reality, the list can contain 1 million numbers. much mucher longer than the list we see here)

Solution 1) linear search
You check from the beginning, 1 after another, until you meet your target_number 23.
If you are very unlucky, your target_number is at the end of the list, you need to check all numbers in the list, very slow.

Solution 2) Binary search
You check the middle number.
If the middle number is smaller than your target_number, you throw away all the numbers on the left.
If the middle number is bigger than your target_number, you throw away all the numbers on the right.
Let's say, there are total 1024 numbers in the list, after this, there are only 512 numbers left.

In the remaining numbers, you check the middle number again, throw away half number again, now there are only 256 numbers left.
So worst case, for 1024 numbers, you only need to check log2(1024)=10 times.

'''

total_check_times = 0


# Returns index of target_number in original_list
# if not present, return -1
def binary_search(original_list, index_left, index_right, target_number):

    # base case 1:
    if index_right < index_left: # target_number is not present in the list.
        return -1

    # till now, index_right is still equals or bigger than index_left

    # base case 2:
    index_middle = index_left + (index_right - index_left) // 2

    global total_check_times
    total_check_times += 1

    if original_list[index_middle] == target_number: # find it!
        return index_middle

    # recursive call:
    # if target_number is smaller than mid number, then it can only be present in the left
    elif original_list[index_middle] > target_number:
        return binary_search(original_list, index_left, index_middle - 1, target_number)
        # Because the new index_right is mid - 1, so possibly, the index_right can be smaller than index_left

    else:  #original_list[mid] < target_number
        return binary_search(original_list, index_middle + 1, index_right, target_number)
        # Because the new index_left is mid + 1, so possibly, the index_left can be bigger than index_right





list_1 = [2,5,8,12,16,23,38,56,72,91]
target_number = 23
target_number_index = binary_search(list_1, 0, len(list_1) - 1, target_number)

if target_number_index != -1:
    print(f"Element is present at index {target_number_index}")
else:
    print("Element is not present in the list.")

print(f"Total check times: {total_check_times}")


# ------------------------------------------------------------------
# the best part of binary search is: it is super fast!
# Time complexity is O(log(n))
#
# Time Complexity represents how your program scales.
# if len(list) change from 1024 to 8192.
# In linear search, your program run time will expand 8 times.
# In binary search, your program run time will expand 1.3 times. log2(1024)=10; log2(8192)=13
# So google search is super fast.
#
# Again!
# Binary search can only applied on a SORTED list.
# So sorting algorithm is very important!
# ------------------------------------------------------------------
