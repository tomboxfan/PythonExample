import random

# define a list which contains 1 million number from 0 - 1,000,000
import time


def test_list():
    list1 = list(range(1000001))
    # shuffle list
    random.shuffle(list1)
    # print(list1)
    time_start = time.time()
    # look up where are the numbers from 0 - 100
    for i in range(101):
        print(i, 'is at index:', list1.index(i))  # tell you the index of the number in the list
    time_end = time.time()
    print('time cost', time_end - time_start, 'seconds')


def test_dict():
    dict1 = {}
    for i in range(1000001):
        dict1[i] = i
    print(dict1)
    time_start = time.time()
    for i in range(100):
        print(i, 'is found in dict: ', dict[i])
    time_end = time.time()
    print('time cost', time_end - time_start, 'seconds')


test_list()
test_dict()



