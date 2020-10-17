import string


def compare_str():
    print('a > c', 'a' > 'c') # a > c False
    print('a > A', 'a' > 'A') # a > A True
    print('z > A', 'z' > 'A') # z > A True
    print('apple > cat', 'apple' > 'cat') # apple > cat False

# compare_str()

# built-in function. ord()
# 计算机给所有的字符，每个都安排了一个数字，这个数字叫做Unicode.
# ord()函数告诉你每个字符的Unicode
def ord_example():
    print('a', ord('a')) # a 97
    print('c', ord('c')) # c 99
    print('z', ord('z')) # z 122
    print('A', ord('A')) # A 65

# ord_example()


def to_binary_example():
    for character in 'Apple':
        unicode_value = ord(character)
        bin_value = bin(unicode_value) # built-in function bin() : return the 'binary string' of integer unicode_value
        print(character, 'unicode value is', unicode_value, 'binary value is', bin_value)

# to_binary_example()

def ord_example2():
    print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
    for i in string.ascii_lowercase:
        print(i, ord(i), end=' ')

    print("\n--------------------------")

    print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    for i in string.ascii_uppercase:
        print(i, ord(i), end=' ')
    print("\n--------------------------")

    print('a < z is', 'a' < 'z', 'because ord("a") is ', ord('a'), ' and ord("z") is ', ord('z'))

# ord_example2()

def chr_example():
    # for i in range(100000):
    #     print(i, chr(i))

    num_list = [33539,32769,24072,24456,26834,33]
    for i in num_list:
        print(chr(i), end='')


chr_example()
