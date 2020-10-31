'''
list comprehension: create list
'''


# format : new_list = [expression   for n in list]
# ----------------------------------------------------------------------
# Example 1:
# Requirement:Given a list numbers, create a new list which contains all elements * 2 in list numbers.

numbers = [1,2,3,4,5]

def print_list_multiply_2_old():
    doubled_numbers = []
    for n in numbers:
        doubled_numbers.append(n * 2)
    print(doubled_numbers)


def print_list_multiply_2_list_comprehension():
    # you usually do for loop numbesr in this : for n in numbers
    doubled_numbers = [n * 2 for n in numbers]      # [n * 2        for n in numbers]
    print(doubled_numbers)





# format : new_list = [expression   for n in list     if condition]
# ----------------------------------------------------------------------
# Example2:
# Requirement: Given a list numbers, create a new list which contains all ODD elements * 2 in lists numbers.
def print_list_multiply_odd_2_old():
    doubled_odd = []
    for n in numbers:
        if n % 2 == 1:
            doubled_odd.append(n * 2)
    print(doubled_odd)

# precise code
def print_list_multiply_odd_2_list_comprehension():
    doubled_odd = [ n * 2    for n in numbers   if n % 2 == 1]
    print(doubled_odd)



def findVowels():
    sentence = 'The rocket came back from Mars!'
    vowels = [n    for n in sentence    if n in 'aeiou']
    print(vowels)


def sum_all_square_num():
    sqr_list = [ i ** 2   for i in range(1, 1001)   ]
    print(sqr_list)
    print('The total is:', sum(sqr_list)) # built-in function sum()






print_list_multiply_2_old()
print_list_multiply_2_list_comprehension()
print_list_multiply_odd_2_old()
print_list_multiply_odd_2_list_comprehension()
findVowels()
sum_all_square_num()