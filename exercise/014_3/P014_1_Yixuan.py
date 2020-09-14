import math
import sys

n = int(input("enter an integer ≤1000: "))

# Issue 1：
# | 是 bitwise operator, 不是logical operator
# 这里你应该使用 or
if (n<2) | (n> 1000):
    print("Your number is too big or too small.")
    sys.exit()

print(n, '=', end=' ')


# Issue 2:
# int(2.3) = 2
# 所以你这里后面应该 + 1
m = int(math.sqrt(n))

for i in range(2, m):

    # Issue 2：
    # & 是 bitwise operator, 不是logical operator
    # 这里你应该使用 and
    while (not(n % i)) & (i < n):
        print(i, '*', end=' ')
        n = n / i

    if i >= n:
        break

print(int(n))
