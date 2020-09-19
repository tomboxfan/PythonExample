# From Yixuan / Natalie
import math


def factorise(n):

    print(n, '=', end = ' ')

    m = int(math.sqrt(n)) + 1


    # this is not possible
    # origianl = a * b * c * d * e
    # sqr root < d and e
    #



    # if it is prime, then output should be n = 1 * n
    is_prime = True

    # loop from 2 to square root m
    for i in range(2, m):

        # 0 -> False
        # not 0 -> True
        # n % i 取余数
        # if n % i == 0, it means n is divisble by i
        # if n % i != 0, it means n is NOT divisble by i
        # n % i == 0, 0 is False
        # not (n % i) ： 只要i 是n的prime factor, 我就一直loop
        while not (n % i):
            is_prime = False
            print(i, end = ' ')
            n = n / i

            if n > 1:
                print("*", end = ' ')


    if is_prime:
        print("1 *", end = ' ')

    # 14 = 2 * 7
    if n != 1:
        print(n, end =' ')

    print()

factorise(1000)