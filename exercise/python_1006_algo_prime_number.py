from datetime import datetime

'''
brute force means: try all possibilities
brute force simply takes advantage of the computer power to exhaust all possibilities.
brute force do not implement any optimization, or implement very limited optimization.
brute force is a bad algorithm
brute force takes a long time
brute force is the last choice
'''

# solution 1 - brute force
# stops working if max_number = 100,000
def solution1_brute_force(max_number):

    check_times = 0
    prime_number_list = []

    for prime_candidate in range(2, max_number):

        # brute force - check till prime_candidate
        for potential_factor in range(2, prime_candidate):
            check_times+=1
            if (prime_candidate % potential_factor == 0):
                break
        else:
            prime_number_list.append(prime_candidate)

    return (prime_number_list, check_times)



# solution 2 - check till square root

def solution2_check_till_sqrt(max_number):

    check_times = 0
    prime_number_list = []

    for prime_candidate in range(2, max_number):

        # optimized - check till the square root of prime_candidate
        sqrt_of_number_to_be_checked = int(prime_candidate ** 0.5) + 1

        for potential_factor in range(2, sqrt_of_number_to_be_checked):
            check_times+=1
            if (prime_candidate % potential_factor == 0):
                break
        else:
            prime_number_list.append(prime_candidate)

    return (prime_number_list, check_times)



# solution 3 - check all primes till square root
# This is even slower than solution 2
# The only possible reason is:
# prime_to_be_checked = [e for e in prime_number_list if e <= sqrt_of_number_to_be_checked + 1] is slow
def solution3_check_prim_till_sqrt(max_number):

    check_times = 0
    prime_number_list = []

    for prime_candidate in range(2, max_number):

        sqrt_of_number_to_be_checked = int(prime_candidate ** 0.5) + 1

        # filter using list comprehension
        prime_to_be_checked = [e for e in prime_number_list if e <= sqrt_of_number_to_be_checked + 1]

        for potential_factor in prime_to_be_checked:
            check_times+=1
            if (prime_candidate % potential_factor == 0):
                break
        else:
            prime_number_list.append(prime_candidate)

    return (prime_number_list, check_times)



'''
Performance Summary:
max_number = 1,000,000
prime_count = 78,498
check_count = 13,927,401
'''
def solution4_check_prim_till_sqrt(max_number):

    check_times = 0
    prime_number_list = []

    index_of_max_prime_smaller_than_prime_candidate = 0;

    for prime_candidate in range(2, max_number):

        sqrt_of_number_to_be_checked = int(prime_candidate ** 0.5) + 1

        # calculate index_of_max_prime_smaller_than_prime_candidate
        while len(prime_number_list) > 0 and len(prime_number_list) > index_of_max_prime_smaller_than_prime_candidate and prime_number_list[index_of_max_prime_smaller_than_prime_candidate] < sqrt_of_number_to_be_checked:
            index_of_max_prime_smaller_than_prime_candidate += 1

        for index in range(0, index_of_max_prime_smaller_than_prime_candidate):
            potential_factor = prime_number_list[index]
            check_times+=1
            if (prime_candidate % potential_factor == 0):
                break
        else:
            prime_number_list.append(prime_candidate)

    return (prime_number_list, check_times)





max_num = 1000000
start_time = datetime.now()

# result1 = solution1_brute_force(max_num)
# result1 = solution2_check_till_sqrt(max_num)
# result1 = solution3_check_prim_till_sqrt(max_num)
result1 = solution4_check_prim_till_sqrt(max_num)


end_time = datetime.now()
print(len(result1[0]))
print(result1[1])
print(f'Spent {(end_time - start_time).seconds} seconds')

