#solution 1 -----------------------------------------------------
def declare_example1():
    p = {1,2,3,4,5}
    print('p = ', p)
    print('p is a ', type(p))


#solution 2 - using set constructor ------------------------------
def declare_example2():
    # empty set
    s1 = set()
    print('s1 = ', s1)
    print('s1 is a ', type(s1))
    print('---------------------------------')

    # list to set
    # 自动去除重复
    list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
    s2 = set(list1)
    print('s2 = ', s2)
    print('s2 is a ', type(s2))
    print('---------------------------------')

    # range to set
    range1 = range(1,10)
    s3 = set(range1)
    print('s3 = ', s2)
    print('s3 is a ', type(s2))

    # alert! this is a dictionary, this is NOT a set
    dict1 = {}
    print('dict1 is a', type(dict1))
    print('---------------------------------')


def loop_example():
    for x in {1,2,3,4,5}:
        print(x)


def in_example():
    q = {2,9,6,4}
    print('2 is in set q:', 2 in q)
    print('10 is in set q:', 10 in q)


def add_example():
    k = {81,180}
    print(k)
    k.add(54)
    print(k)
    k.add(12)
    print(k)
    k.add(180)
    print(k)


def update_example():
    k = {81,180}
    print(k)            # {81, 180}
    k.update([1,2,3])   # add a list to the set
    print(k)            # {1, 2, 3, 81, 180}
    k.update({4,5,6})   # add a set to the set
    print(k)            #{1, 2, 3, 4, 5, 6, 81, 180}


def remove_example():
    k = {81,180}
    print(k)            # {81, 180}
    k.remove(81)
    print(k)            # {180}
    k.remove(82)        # KeyError happens
    print(k)            # won't get executed, because error happens above


def discard_example():
    k = {81,180}
    print(k)            # {81, 180}
    k.discard(82)       # KeyError WONT happen
    print(k)            # {81, 180}


def copy_example():
    k = {81,180}
    # Solution 1
    j = k.copy()        # Shallow copy! 注意, shallow copy 不是 j = k. 而是仅仅copy element的references. 这里太复杂，以后再给同学们讲shallow copy & deep copy. # https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
    print(j)            # {81, 180}
    # Solution 2
    l = set(k)
    print(l)            # {81, 180}


def operation_example():
    set_divisible_by_2 = set(range(0, 20, 2))
    set_divisible_by_3 = set(range(0, 20, 3))
    set_divisible_by_5 = set(range(0, 20, 5))
    print(set_divisible_by_2)
    print(set_divisible_by_3)
    print(set_divisible_by_5)

    # 并集
    set_divisible_by_2_or_5 = set_divisible_by_2.union(set_divisible_by_5)
    print("divisible_by_2_or_5", set_divisible_by_2_or_5)

    # 交集
    set_divisible_by_2_and_5 = set_divisible_by_2.intersection(set_divisible_by_5)
    print("divisible_by_2_and_5", set_divisible_by_2_and_5)

    # 差集
    set_divisible_by_2_but_not_5 = set_divisible_by_2.difference(set_divisible_by_5)
    print("divisible_by_2_but_not_5", set_divisible_by_2_but_not_5)

    # 对称差集
    set_divisible_by_2_or_5_but_not_both = set_divisible_by_2.symmetric_difference(set_divisible_by_5)
    print("divisible_by_2_or_5_but_not_both", set_divisible_by_2_or_5_but_not_both)

    # 并集 = 交集 + 对称差集
    print("union == intersection + symmetric_difference:", set_divisible_by_2_or_5 == (set_divisible_by_2_or_5.union(set_divisible_by_2_or_5_but_not_both)))



# declare_example1()
# declare_example2()
# loop_example()
# in_example()
# add_example() # add single element to a set
# update_example() # add multiple elements to a set
# remove_example() # KeyError happens in e doesn't exist in the set
# discard_example() #KeyError WONT happen in e doesn't exist in the set
# copy_example()
operation_example()

