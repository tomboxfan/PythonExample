# import time module
import time

def time_example():


    # IMPORTANT!!! ------------------------------------------
    #
    # time.time() tells you how many seconds has passed since 1970 Jan 1st 00:00:00 till now.
    #
    # 1970 Jan 1st 00:00:00 is a special time in computer world. It is called 'Epoch Time' or 'the epoch'.
    #
    # You see 2 time in time.time()
    # time.       is the time module
    # time()      is the time method
    # -------------------------------------------------------
    second_count = time.time()
    print(f'There are {second_count:,} seconds from 1970 Jan 1st 00:00:00 till now.')

    # Let's prove that!
    total_second_count_in_1_day = 60 * 60 * 24
    total_second_count_in_1_year = total_second_count_in_1_day * 365
    year_count = second_count / total_second_count_in_1_year
    print(f'There are {year_count} years now from 1970')


time_example()