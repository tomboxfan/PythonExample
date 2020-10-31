'''
brute force means: try all possibilities
brute force simply takes advantage of the computer power to exhaust all possibilities
brute force does not implement any optimization, or implement very limited optimization
brute force is a BAD algorithm
brute force takes a long time
brute force is the last choice
'''

def solution1_brute_force(max_number):

    check_times = 0
    prime_number_list = []

    for number_to_be_checked in range(2, max_number):

        # brute force - check all numbers till number_to_be_checked
        for potential_factor in range(2, number_to_be_checked):
            check_times += 1
            if(number_to_be_checked % potential_factor == 0):
                break
        else:   # else clause
            prime_number_list.append(number_to_be_checked)


    return (prime_number_list, check_times)


def solution2_check_till_sqrt(max_number):

    check_times = 0
    prime_number_list = []

    for number_to_be_checked in range(2, max_number):

        sqrt_of_number_to_be_checked = int(number_to_be_checked ** 0.5) + 1
        for potential_factor in range(2, sqrt_of_number_to_be_checked):
            check_times += 1
            if(number_to_be_checked % potential_factor == 0):
                break
        else:   # else clause
            prime_number_list.append(number_to_be_checked)

    return (prime_number_list, check_times)



def solution3_check_prime_till_sqrt(max_number):

    check_times = 0
    prime_number_list = []

    for number_to_be_checked in range(2, max_number):

        sqrt_of_number_to_be_checked = int(number_to_be_checked ** 0.5) + 1

        prime_to_be_checked = [n          for n in prime_number_list        if n <= sqrt_of_number_to_be_checked  ]

        for potential_factor in prime_to_be_checked:
            check_times += 1
            if(number_to_be_checked % potential_factor == 0):
                break
        else:   # else clause
            prime_number_list.append(number_to_be_checked)

    return (prime_number_list, check_times)




# this algo cannot work if max_numbers == 100,000
# result = solution1_brute_force(100000)
# print('there are', len(result[0]), 'prime numbers. They are:', result[0])
# print('In total, it takes', result[1], 'checks.')

# this algo cannot work if max_numbers == 1,000,000 (almost)
# result = solution2_check_till_sqrt(1000000)
# print('there are', len(result[0]), 'prime numbers. They are:', result[0])
# print('In total, it takes', result[1], 'checks.')

result = solution3_check_prime_till_sqrt(1000000)
print('there are', len(result[0]), 'prime numbers. They are:', result[0])
print('In total, it takes', result[1], 'checks.')
