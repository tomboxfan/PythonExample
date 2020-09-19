

def construct_example():

    # empty tuple
    tuple_empty = ()

    tuple_1 = (1,)
    tuple_multiple = (1,2,3,4,5)

    # Doesn't work! tuple is IMMUTABLE
    # tuple_multiple[0] = -1

    #mix type
    tup_mix1 = ('physics', 1997, True)
    tup_mix2 = 'a', 'b', 'c', 'd', 123, True # 省略括号

    tup_mix3 = (
                    {'food': 'icecream', 'country':'China'}, # dict
                    [1,2,3,4,5] # list
                )

    # create a tuple using existing tuple
    # tuple concatenation
    tup_compo1 = tuple_empty + tuple_1 + tup_mix1 + tuple_multiple + tup_mix2
    print('tup_compo1:', tup_compo1)

    tup_compo2 = tuple_empty , tuple_1 , tup_mix1 , tuple_multiple , tup_mix2
    print('tup_compo2:', tup_compo2)

    tup_compo3 = tuple_multiple * 3
    print('tup_compo3:', tup_compo3)

    zeros_tuple = (0,) * 100
    print('zeros_tuple:', zeros_tuple)

    #create a tuple from a list
    list1 = ["Apple", 'Orange', 'Banana', "Pear"]
    tup_from_list = tuple(list1)
    print('tup_from_list:', tup_from_list)


def access_example():
    tup4 = (1,2,3,4,5)

    #max() / min()
    print("max(tup4):", max(tup4))
    print("min(tup4):", min(tup4))

    tup5 = 'a', 'b', 'c', 'd', 123, True # 省略括号

    print("tup5[0]: ",     tup5[0])     #  a
    print("tup5[1:5]: ",   tup5[1:5])   #  ('b', 'c', 'd', 123)
    print("tup5[1:5:2]: ", tup5[1:5:2]) #  ('b',      'd'     )
    print("len(tup5): ", len(tup5))   #  6


def loop_example():

    tup5 = 'a', 'b', 'c', 'd', 123, True # 省略括号

    for e in tup5:
        print(e, end=' ')


def unpacking_example():
    x = 'jelly'
    y = 'bean'

    # 首先使用y, x; 创建1个tuple -> (y,x)
    # 第二步，使用tuple的unpacking, 把tuple 打开, 然后重新赋值给x, y
    x,y = y,x
    print(x, y) # bean jelly

    # another example
    (a, (b, (c, d))) = (4, (3, (2, 1)))
    print(a, b, c, d)


def minmax(items):
    return min(items), max(items)


def unpacking_example2():
    lower, upper = minmax([1, 2, 3, 4, 5])  # pass in list
    print(lower, upper)
    lower, upper = minmax("Apple")  # pass in String
    print(lower, upper)
    lower, upper = minmax({1, 3, 2, -100})  # pass in set
    print(lower, upper)
    lower, upper = minmax(("Tom", "Billy", "Sandy", "Sue"))  # pass in a tuple
    print(lower, upper)

def unpacking_example3():
    a = ("NUS", 5000, "Computer Science")
    university, student, department = a
    print(university, student, department)
    x, *y, z = (10, "Geeks", "for", "Geeks", 50)
    print(x)
    print(y)
    print(type(y))  # list
    print(z)
    x, y, *z = (10, "Geeks", "for", "Geeks", 50)
    print(x)
    print(y)
    print(z)
    print(type(z))  # list


construct_example()
access_example()
loop_example()
unpacking_example()
unpacking_example2()
unpacking_example3()
