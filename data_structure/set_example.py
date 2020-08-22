def print_set(p):
    print('p = ', p)
    print('p is a ', type(p))
    print("----------------------------")


def declare_example1():
    p1 = {1, 2, 3, 4, 5}
    print_set(p1)

    #Alert! This is a dictionary!!
    p2 = {}
    print_set(p2)


def declare_example2():
    s1 = set()
    print_set(s1)

    #list to set
    list1 = [1,2,3,4,5,1,2,3,4,5]
    s2 = set(list1)
    print_set(s2)

    #range to set
    range1 = range(0,20,3)
    s3 = set(range1)
    print_set(s3)

def loop_set():
    for x in set(range(0, 20, 3)):
        print(x, end=" ")
        print()

def in_example():
    q = {2, 4, 6, 9}
    print('2 in set:', 2 in q)
    print('10 in set:', 10 in q)




# declare_example1()
# declare_example2()
# in_example()
# loop_set()

set_divisible_by_2 = set(range(0,20,2))
set_divisible_by_3 = set(range(0,20,3))
set_divisible_by_5 = set(range(0,20,5))
print(set_divisible_by_2)
print(set_divisible_by_3)
print(set_divisible_by_5)

# 并集
set_divisible_by_2_or_5 = set_divisible_by_2.union(set_divisible_by_5)
print(set_divisible_by_2_or_5)

# 交集
set_divisible_by_2_and_5 = set_divisible_by_2.intersection(set_divisible_by_5)
print(set_divisible_by_2_and_5)

# 差集
set_divisible_by_2_but_not_5 = set_divisible_by_2.difference(set_divisible_by_5)
print(set_divisible_by_2_but_not_5)

# 对称差集
set_divisible_by_2_or_5_but_not_both = set_divisible_by_2.symmetric_difference(set_divisible_by_5)
print(set_divisible_by_2_or_5_but_not_both)

# 并集 = 交集 + 对称差集
print(set_divisible_by_2_or_5 == set_divisible_by_2_and_5.union(set_divisible_by_2_or_5_but_not_both))

