def howmanyin_no_recursion(target_list):
    return len(target_list)

'''
if list is empty:  list -> False
if list is NOT empty: list - True
'''

# [solution 1]
# def howmanyin(target_list):
#     if target_list[1:]:
#         # recursive call
#         return 1 + howmanyin(target_list[1:])
#     else:
#         # base case
#         return 1

# [solution 2]

'''
Summary: 
1) howmanyin(target_list) is converted to 1 + howmanyin(target_list[1:])
'''
def howmanyin(target_list):
    # base case
    if len(target_list) == 1:
        return 1

    # recursive call
    return 1 + howmanyin(target_list[1:])


l1 = [n for n in range(10)]
# print(f'list size is {howmanyin_no_recursion(l1)}')
print(f'list size is {howmanyin(l1)}')