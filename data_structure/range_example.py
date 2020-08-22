# https://www.geeksforgeeks.org/python-range-function/

def one_param_example():
    # printing first 10  whole number
    for i in range(10):
        print(i, end=" ")
    print()

    # printing first 20 whole number
    for i in range(20):
        print(i, end=" ")


def two_param_example():
    # printing a natural number upto 20
    for i in range(1, 20):
        print(i, end=" ")
    print()

    # printing a natural number from 5 t0 20
    for i in range(5, 20):
        print(i, end=" ")

def three_param_example():
    # divisible by 3
    for i in range(0, 30, 3):
        print(i, end=" ")
    print()

    # divisible by 5
    for i in range(0, 50, 5):
        print(i, end=" ")
    print()

    # incremented by 2
    for i in range(2, 25, 2):
        print(i, end=" ")
    print()

    # incremented by 4
    for i in range(0, 30, 4):
        print(i, end=" ")
    print()

    # incremented by 3
    for i in range(15, 25, 3):
        print(i, end=" ")


def decrement_example():
    # incremented by -2
    for i in range(25, 2, -2):
        print(i, end=" ")
    print()

    # incremented by -4
    for i in range(30, 1, -4):
        print(i, end=" ")
    print()

    # incremented by -3
    for i in range(25, -6, -3):
        print(i, end=" ")

# one_param_example()
# two_param_example()
# three_param_example()
decrement_example()
